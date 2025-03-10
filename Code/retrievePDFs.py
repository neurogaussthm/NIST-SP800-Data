import csv
import requests
from bs4 import BeautifulSoup
from pypdf import PdfReader
import io
import re

with open('Code\\nist_documents_SP_and_FIPS.csv', 'r') as f:
    reader = csv.reader(f)
    documents = list(reader)
print(len(documents))
i = 0
for document in documents:
    if i < 0:
        i = i + 1
    else:
        print(document[0] + document[1])
        pdf = requests.get(document[5])
        reader = PdfReader(io.BytesIO(pdf.content))
        text = ''
        for page in reader.pages:
            text += page.extract_text()
        text = re.sub(r'\[\d+\]', '', text)
        text = re.sub('\n', ' ', text)
        title = document[0] + document[1] + '.txt'
        with open(title, 'w', encoding='utf-8') as f:
            f.write(text)
        print(i)
        i = i + 1