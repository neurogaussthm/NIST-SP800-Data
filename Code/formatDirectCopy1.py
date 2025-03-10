import re
import os

folder_path = "manual/"  # Change this to your target folder
file_names = os.listdir(folder_path)

print(file_names)  # List of all files and folders in the directory
for file in file_names:
    with open('manual\\' + file, 'r', encoding='UTF-8') as f:
        lines = f.readlines()

    doc = ''
    length = 0

    average = sum(len(line) for line in lines) / len(lines)

    for line in lines:
        if re.fullmatch(r'\d+\n', line) or ('.......' or '. . . .') in line:
            continue
        if re.match(r'\[\d+\]', line):
            line = re.sub(r'\[\d+\]', '', line)
        line = line.replace('\n', ' ') if len(line) > average else line
        doc = doc + line

    with open('manualFixed\\' + file, 'w', encoding='UTF-8') as f:
        f.write(doc)