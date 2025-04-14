import json

models = ["granite3.1-dense", "granite3.2"]
sourceTypes = ["questions", "chat", "scenario"]

def numInstancesSubstring(string, substring):
    indices = []
    startIndex = 0
    while True:
        index = string.find(substring, startIndex)
        if index == -1:
            break
        indices.append(index)
        startIndex = index + 1
    return indices

for model in models:
    for sourceType in sourceTypes:
        original = f"../faiss-training-7-{model}_2b/{model}-training-{sourceType}-answer.txt"
        destination = f"../faiss-training-7-{model}_2b/{model}-clean-{sourceType}.jsonl"

        if sourceType == "questions":
            responseKey = "response"
        else:
            responseKey = "completion"

        # Read original mixed input file
        with open(original, "r", encoding="utf-8") as f:
            raw_lines = f.readlines()

        # Buffer to collect entries
        json_objects = []
        buffer = ""
        numSkip = 0
        for n, line in enumerate(raw_lines):
            line = line.strip()
            if line in ["", "```", "```json"]:
                continue
            if "$$$$$" in line:
                buffer = ""
                numSkip += 1
                continue
            buffer += line
            if line == "}":  # end of JSON object
                try:
                    # Replace keys
                    obj = json.loads(buffer)
                    if isinstance(obj.get(responseKey), dict):
                        buffer = ""
                        numSkip += 1
                        continue
                    obj = {
                        "prompt": obj.get("query", "").strip(),
                        "completion": " " + obj.get(responseKey, "").strip()  # note: leading space helps fine-tuning
                    }
                    if len(numInstancesSubstring(obj.get("completion"), "\nUser:")) < len(numInstancesSubstring(obj.get("completion"), "\nAssistant:")):
                        buffer = ""
                        numSkip += 1
                        continue
                    json_objects.append(obj)
                except json.JSONDecodeError as e:
                    # print("⚠️ Could not parse line:\n", buffer)
                    # print(e)
                    if "{\"query\": " in buffer:
                        numSkip += 1
                buffer = ""

        # Write to a clean JSONL file
        with open(destination, "w", encoding="utf-8") as out_f:
            for obj in json_objects:
                out_f.write(json.dumps(obj) + "\n")

        print(f"✅ Wrote {len(json_objects)} entries to {destination}\nSkipped {numSkip} questions.")

