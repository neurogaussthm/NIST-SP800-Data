import json

# Read original mixed input file
with open("granite3.1-dense-training-questions-answer.txt", "r", encoding="utf-8") as f:
    raw_lines = f.readlines()

# Buffer to collect entries
json_objects = []
buffer = ""

for line in raw_lines:
    line = line.strip()
    if line in ["", "```", "```json"]:
        continue

    buffer += line
    if line == "}":  # end of JSON object
        try:
            # Replace keys
            obj = json.loads(buffer)
            obj = {
                "prompt": obj.get("query", "").strip(),
                "completion": " " + obj.get("response", "").strip()  # note: leading space helps fine-tuning
            }
            json_objects.append(obj)
        except json.JSONDecodeError as e:
            print("⚠️ Could not parse line:\n", buffer)
            print(e)
        buffer = ""

# Write to a clean JSONL file
with open("granite3.1-clean2-questions.jsonl", "w", encoding="utf-8") as out_f:
    for obj in json_objects:
        out_f.write(json.dumps(obj) + "\n")

print(f"✅ Wrote {len(json_objects)} entries to granite3.1-clean-questions.jsonl")
