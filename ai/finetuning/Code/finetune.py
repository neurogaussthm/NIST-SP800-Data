import time
import os
import datasets
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, TrainingArguments, BitsAndBytesConfig, EarlyStoppingCallback
from transformers.trainer_utils import get_last_checkpoint
from peft import LoraConfig, PeftModel
from trl import SFTTrainer, DataCollatorForCompletionOnlyLM

def finetune(model):
    datasetTrain = datasets.load_dataset("json", data_files=f"../faiss-training-7-{model}_2b/{model}-clean-all.jsonl")
    datasetTest = datasets.load_dataset("json", data_files=f"../faiss-training-7-{model}_2b/{model}-clean-test.jsonl")

    dataset = datasets.DatasetDict({"train": datasetTrain["train"], "test": datasetTest["train"]})

    startPull = time.perf_counter()
    if model == "granite3.1-dense":
        model_checkpoint = "ibm-granite/granite-3.1-2b-instruct"
    if model == "granite3.2":
        model_checkpoint = "ibm-granite/granite-3.2-2b-instruct"
    max_seq_length = 1024
    tokenizer = AutoTokenizer.from_pretrained(model_checkpoint, padding_side="right", model_max_length=max_seq_length)
    tokenizer.add_special_tokens({"pad_token": "[PAD]", "additional_special_tokens": ["<|user|>", "<|assistant|>", "<|system|>", "<|endoftext|>"]})

    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_use_double_quant=True,
        bnb_4bit_compute_dtype=torch.float16
    )

    model_base = AutoModelForCausalLM.from_pretrained(
    model_checkpoint,
    quantization_config=bnb_config,
    device_map="auto"

    )

    model_base.resize_token_embeddings(len(tokenizer))
    model_base.config.pad_token_id = tokenizer.pad_token_id

    timePull = time.perf_counter() - startPull
    print(f"{model} {timePull = }")

    startConfig = time.perf_counter()

    def formatting_prompts_func(example):
        texts = []
        for i in range(len(example["prompt"])):
            text = f"<|system|>\nYou are a helpful assistant who is also an expert on the NIST SP 800 series\n<|user|>\n{example['prompt'][i]}\n<|assistant|>\n{example['completion'][i]}{tokenizer.eos_token}"
            texts.append(text)
        tokenized = tokenizer(texts, padding=False, truncation=True, max_length=max_seq_length, return_attention_mask=True)
        return tokenized

    columns_remove = ["prompt", "completion"]
    tokenized_train = dataset["train"].map(formatting_prompts_func, batched=True, remove_columns=columns_remove)
    tokenized_test = dataset["test"].map(formatting_prompts_func, batched=True, remove_columns=columns_remove)

    response_template = "\n<|assistant|>\n"
    instruction_template = "\n<|user|>\n"

    response_template_ids = tokenizer.encode(response_template, add_special_tokens=False)[2:]
    instruction_template_ids = tokenizer.encode(instruction_template, add_special_tokens=False)
    collator = DataCollatorForCompletionOnlyLM(response_template=response_template_ids, tokenizer=tokenizer, instruction_template=instruction_template_ids, mlm=False)

    qlora_config = LoraConfig(
        r=64,  # The rank of the Low-Rank Adaptation
        lora_alpha=128,  # Scaling factor for the adapted layers
        target_modules=["q_proj", "v_proj", "k_proj", "o_proj", "gate_proj", "up_proj", "down_proj"],  # Layer names to apply LoRA to
        lora_dropout=0.1,
        bias="none",
        task_type="CAUSAL_LM"
    )
    output_dir = f"../faiss-training-7-{model}_2b/epochresults"
    training_args = TrainingArguments(
        output_dir=output_dir,
        logging_dir=f"../faiss-training-7-{model}_2b/logs",
        learning_rate=2e-6,
        weight_decay=0.01,
        per_device_train_batch_size=2,
        gradient_accumulation_steps=3,
        per_device_eval_batch_size=2,
        num_train_epochs=27,
        logging_steps=100,
        eval_strategy="epoch",
        save_strategy="epoch",
        save_total_limit=None,
        load_best_model_at_end=True,
        metric_for_best_model="eval_loss",
        greater_is_better=False,
        bf16=True, # fp16=True,
        report_to="none",
        remove_unused_columns=False,
        max_grad_norm=1.0
    )

    trainer = SFTTrainer(
        model=model_base,
        args=training_args,
        train_dataset=tokenized_train,
        eval_dataset=tokenized_test,
        peft_config = qlora_config,
        data_collator=collator,
        callbacks=[EarlyStoppingCallback(early_stopping_patience=3)],
    )

    last_checkpoint = get_last_checkpoint(output_dir)
    if last_checkpoint is not None:
        print(f"Resuming from {last_checkpoint = }")
        resume_from_checkpoint = last_checkpoint
    else:
        print("No checkpoint.")
        resume_from_checkpoint = None

    timeConfig = time.perf_counter() - startConfig
    print(f"{model} {timeConfig = }")

    startTrain = time.perf_counter()
    trainer.train(resume_from_checkpoint=resume_from_checkpoint)
    timeTrain = time.perf_counter() - startTrain
    print(f"{model} {timeTrain = }")
    print(f"Training time {model}: {timeTrain / 60:.2f} minutes")

    model_base.save_pretrained(f"../faiss-training-7-{model}_2b/baseoutput")
    tokenizer.save_pretrained(f"../faiss-training-7-{model}_2b/baseoutput")
    trainer.save_model(f"../faiss-training-7-{model}_2b/finaloutput")
    tokenizer.save_pretrained(f"../faiss-training-7-{model}_2b/finaloutput")

def mergeModel(model):
    startMerge = time.perf_counter()
    if model == "granite3.1-dense":
        model_base = "ibm-granite/granite-3.1-2b-instruct"
    if model == "granite3.2":
        model_base = "ibm-granite/granite-3.2-2b-instruct"
    tokenizer_base = AutoTokenizer.from_pretrained(model_base)
    tokenizer_base.add_special_tokens({"pad_token": "[PAD]", "additional_special_tokens": ["<|user|>", "<|assistant|>", "<|system|>", "<|endoftext|>"]})
    base_model = AutoModelForCausalLM.from_pretrained(model_base, device_map="auto", torch_dtype=torch.float16)
    base_model.resize_token_embeddings(len(tokenizer_base))
    base_model.config.pad_token_id = tokenizer_base.pad_token_id
    tokenizer = AutoTokenizer.from_pretrained(f"../faiss-training-7-{model}_2b/finaloutput")
    peft_model = PeftModel.from_pretrained(base_model, f"../faiss-training-7-{model}_2b/finaloutput")

    merged_model = peft_model.merge_and_unload()
    merged_model.save_pretrained(f"../faiss-training-7-{model}_2b/merged")
    tokenizer.save_pretrained(f"../faiss-training-7-{model}_2b/merged")
    timeMerge = time.perf_counter() - startMerge
    print(f"{model} {timeMerge = }")

for model in ["granite3.1-dense", "granite3.2"]:
    torch.cuda.empty_cache()
    finetune(model)
for model in ["granite3.1-dense", "granite3.2"]:
    mergeModel(model)


# Still need to convert to GGUF file with llama.cpp's convert.py script, like the following, but use convert_hf_to_gguf.py, slightly different format
# python3 convert.py \
#     --outfile ./granite3.1-2b-NIST.gguf \
#     --tokenizer_path ./merged_ \
#     --model_path ./merged \
#     --vocab-only false


# Then create Modelfile like: 
# FROM ./granite3.1-2b-NIST.gguf

# PARAMETER temperature 0.7
# PARAMETER top_p 0.95
# PARAMETER top_k 50
# PARAMETER repeat_penalty 1.1

# TEMPLATE \"\"\"<|system|>
# You are a helpful assistant who is also an expert on the NIST SP 800 series.
# <|user|>
# {{ .Prompt }}
# <|assistant|>
# \"\"\"


# Finally, run "ollama create NAME -f Modelfile" and "ollama run NAME"
