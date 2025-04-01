import os
import json
import markdown
from bs4 import BeautifulSoup
from langchain.text_splitter import CharacterTextSplitter

inputdirectory = "/home/niatecai/aiDrew/NIST-SP800-Data/llamaParsed1"
outputdirectory = "../by-token-500-200-o200k_base/jsonOutput"
indexfilename = "index.json"
encoding = "o200k_base"
chunksize = 500
overlap = 200

def parse_markdown(md_text):
    splitter = CharacterTextSplitter.from_tiktoken_encoder(encoding_name=encoding, chunk_size=chunksize, chunk_overlap=overlap)
    text_chunks = splitter.split_text(md_text)
    return text_chunks


def save_json(output, filename):
    with open(filename, "w", encoding="cp1252") as f:
        json.dump(output, f, indent=2)


index = []

for file in os.listdir(inputdirectory):
    print(file)
    with open(os.path.join(inputdirectory, file), 'r', encoding="cp1252") as f:
        text = f.read()
    
    parsed = parse_markdown(text)
    jsonName = os.path.join(outputdirectory, file.replace(".md", ".json"))
    save_json(parsed, jsonName)

    index.append({
        "filename": file,
        "json_filename": jsonName
    })

save_json(index, indexfilename)
