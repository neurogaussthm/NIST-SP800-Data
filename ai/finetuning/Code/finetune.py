import time
import datasets
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, TrainingArguments, BitsAndBytesConfig, EarlyStoppingCallback
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
    tokenizer = AutoTokenizer.from_pretrained(model_checkpoint, padding_side="right")
    tokenizer.add_special_tokens({"additional_special_tokens": ["<|user|>", "<|assistant|>", "<|system|>", "<|endoftext|>"]})

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

    timePull = time.perf_counter() - startPull
    print(f"{model} {timePull = }")

    startConfig = time.perf_counter()

    max_seq_length = 1024

    def formatting_prompts_func(example):
        text = f"<|system|>\nYou are a helpful assistant who is also an expert on the NIST SP 800 series\n<|user|>\n{example['prompt']}\n<|assistant|>\n{example['completion']}{tokenizer.eos_token}"
        tokenized = tokenizer(text, padding="max_length", truncation=True, max_length=max_seq_length, return_attention_mask=True)
        return {"input_ids": tokenized["input_ids"], "attention_mask": tokenized["attention_mask"], "labels": tokenized["input_ids"].copy()}

    tokenized_train = dataset["train"].map(formatting_prompts_func, remove_columns=dataset["train"].column_names)
    tokenized_test = dataset["test"].map(formatting_prompts_func, remove_columns=dataset["test"].column_names)

    response_template = "\n<|assistant|>\n"
    instruction_template = "\n<|user|>\n"

    response_template_ids = tokenizer.encode(response_template, add_special_tokens=False)
    instruction_template_ids = tokenizer.encode(instruction_template, add_special_tokens=False)
    collator = DataCollatorForCompletionOnlyLM(response_template=response_template_ids, tokenizer=tokenizer, mlm=False) # , instruction_template=instruction_template_ids, mlm=False)

    qlora_config = LoraConfig(
        r=16,  # The rank of the Low-Rank Adaptation
        lora_alpha=32,  # Scaling factor for the adapted layers
        target_modules=["q_proj", "v_proj"],  # Layer names to apply LoRA to
        lora_dropout=0.1,
        bias="none",
        task_type="CAUSAL_LM"
    )

    training_args = TrainingArguments(
        output_dir=f"../faiss-training-7-{model}_2b/results",
        logging_dir=f"../faiss-training-7-{model}_2b/logs",
        learning_rate=2e-5,
        per_device_train_batch_size=3,
        gradient_accumulation_steps=2,
        per_device_eval_batch_size=3,
        num_train_epochs=7,
        logging_steps=100,
        eval_strategy="epoch",
        save_strategy="epoch",
        save_total_limit=3,
        load_best_model_at_end=True,
        metric_for_best_model="eval_loss",
        greater_is_better=False,
        fp16=True,
        report_to="none",
        remove_unused_columns=False
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

    timeConfig = time.perf_counter() - startConfig
    print(f"{model} {timeConfig = }")

    startTrain = time.perf_counter()
    trainer.train()
    timeTrain = time.perf_counter() - startTrain
    print(f"{model} {timeTrain = }")
    print(f"Training time {model}: {timeTrain / 60:.2f} minutes")

    model_base.save_pretrained(f"../faiss-training-7-{model}_2b/baseoutput")
    tokenizer.save_pretrained(f"../faiss-training-7-{model}_2b/baseoutput")
    trainer.save_model(f"../faiss-training-7-{model}_2b/output")
    tokenizer.save_pretrained(f"../faiss-training-7-{model}_2b/output")

def mergeModel(model):
    startMerge = time.perf_counter()
    if model == "granite3.1-dense":
        model_base = "ibm-granite/granite-3.1-2b-instruct"
    if model == "granite3.2":
        model_base = "ibm-granite/granite-3.2-2b-instruct"
    base_model = AutoModelForCausalLM.from_pretrained(model_base, device_map="auto", torch_dtype=torch.float16)
    tokenizer = AutoTokenizer.from_pretrained(f"../faiss-training-7-{model}_2b/output")
    peft_model = PeftModel.from_pretrained(base_model, f"../faiss-training-7-{model}_2b/output")

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


# Still need to convert to GGUF file with llama.cpp's convert.py script, like the following
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
