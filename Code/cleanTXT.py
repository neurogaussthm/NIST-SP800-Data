import os

folder_path = "manual/"  # Change this to your target folder
file_names = os.listdir(folder_path)
with open(folder_path + "SKIPPED - SP800-22 Rev. 1.txt", "w", encoding="utf-8") as f:
        text = f.write("\u201c \u201d \u2018 \u2019 \u2192")
for file in file_names:
    with open(folder_path + file, "r", encoding="utf-8") as f:
        text = f.read()
    text = text.replace("\u201c", "\u0022")
    text = text.replace("\u201d", "\u0022")
    text = text.replace("\u2018", "'")
    text = text.replace("\u2019", "'")
    text = text.replace("\u2192", "->")
    text = text.replace("", "•")
    with open(folder_path + file, "w", encoding="utf-8") as f:
        f.write(text)