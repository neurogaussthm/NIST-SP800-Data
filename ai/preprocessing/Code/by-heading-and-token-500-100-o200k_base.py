import os
import json
import markdown
from bs4 import BeautifulSoup
from langchain.text_splitter import CharacterTextSplitter

inputdirectory = "/home/niatecai/aiDrew/NIST-SP800-Data/llamaParsed1"
outputdirectory = "../by-heading-and-token-500-100-o200k_base/jsonOutput"
indexfilename = "index.json"
encoding = "o200k_base"
chunksize = 500
overlap = 100

def parse_markdown(md_text):
    splitter = CharacterTextSplitter.from_tiktoken_encoder(encoding_name=encoding, chunk_size=chunksize, chunk_overlap=overlap)

    html = markdown.markdown(md_text)
    soup = BeautifulSoup(html, 'html.parser')
    
    structured_data = []
    current_section = None
    current_subsection = None
    
    for element in soup.find_all(['h1', 'h2', 'h3', 'p', 'ul', 'ol', 'table', 'pre']):
        if element.name == 'h1':
            if current_section:
                structured_data.append(current_section)
            current_section = {"title": element.text, "subsections": []}
            current_subsection = None
        elif element.name == 'h2':
            if current_subsection:
                current_section["subsections"].append(current_subsection)
            current_subsection = {"title": element.text, "content": []}
        elif element.name == 'h3':
            if current_subsection:
                current_subsection["content"].append({"subsection": element.text, "text": []})
        elif element.name in ['p', 'ul', 'ol', 'pre']:
            text_chunks = splitter.split_text(element.text)
            for chunk in text_chunks:
                if current_subsection:
                    current_subsection["content"].append({"text": chunk})
                elif current_section:
                    current_section["subsections"].append({"content": chunk})
    
    if current_section:
        structured_data.append(current_section)
    
    return structured_data


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
