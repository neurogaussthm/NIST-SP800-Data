import random

models = ["granite3.1-dense", "granite3.2"]

for model in models:
    with open(f"../faiss-training-7-{model}_2b/{model}-clean-all-2.jsonl", 'r') as f:
        examples = f.readlines()
    testList = []
    for _ in range(600):
        randInt = random.randint(0, len(examples) - 1)
        testList.append(examples.pop(randInt))
    with open(f"../faiss-training-7-{model}_2b/{model}-clean-test-2.jsonl", 'w') as f:
        f.writelines(testList)
    with open(f"../faiss-training-7-{model}_2b/{model}-clean-all-2.jsonl", 'w') as f:
        f.writelines(examples)
