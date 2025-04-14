import json

def numInstancesSubstring(string, substring):
    indices = 0
    startIndex = 0
    while True:
        index = string.find(substring, startIndex)
        if index == -1:
            break
        indices += 1
        startIndex = index + 1
    return indices

with open("granite3.1-dense-training-questions-answer.txt", 'r') as f:
    datalist = f.readlines()
data = ""
for i in datalist:
    i = i.strip().replace("\\\"", "").replace(".\"\\", ".\\").replace("\"\"", "\"").replace("\"query\":", "\"prompt\":").replace("\"response\":", " \"completion\":")
    if i in ["", "```", "```json"]:
        continue
    if i == "}":
        data += i + '\n'
    else:
        data += i
data = data.split("\n")
with open("granite3.1-clean-questions.jsonl", 'w') as f:
    f.write("")
for d in data:
    with open("granite3.1-clean-questions.jsonl", 'a') as f:
        f.write(json.dumps(d) + '\n')
with open("granite3.1-clean-questions.jsonl", "r", encoding="utf-8") as f:
    for i, line in enumerate(f, 1):
        try:
            json.loads(line)
        except json.JSONDecodeError as e:
            print(f"❌ Line {i} is invalid: {e}")