models = ["granite3.1-dense", "granite3.2"]
sourceTypes = ["questions", "chat", "scenario"]

for model in models:
    with open(f"../faiss-training-7-{model}_2b/{model}-clean-all-2.jsonl", 'w') as f:
        f.write("")
    for sourceType in sourceTypes:
        file = f"../faiss-training-7-{model}_2b/{model}-clean-{sourceType}.jsonl"
        with open(file, 'r') as f:
            data = f.read()
        with open(f"../faiss-training-7-{model}_2b/{model}-clean-all-2.jsonl", 'a') as f:
            f.write(data)
