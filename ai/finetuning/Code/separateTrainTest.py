import random

models = ["granite3.1-dense", "granite3.2"]

for model in models:
    with open(f"../faiss-training-7-{model}_2b/{model}-clean-all.jsonl", 'r') as f:
        examples = f.readlines()
    testList = []
    for _ in range(250):
        randInt = random.randint(0, len(examples) - 1)
        testList.append(examples.pop(randInt))
    with open(f"../faiss-training-7-{model}_2b/{model}-clean-test.jsonl", 'w') as f:
        f.writelines(testList)
    with open(f"../faiss-training-7-{model}_2b/{model}-clean-all.jsonl", 'w') as f:
        f.writelines(examples)
