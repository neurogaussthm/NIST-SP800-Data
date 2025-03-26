import faiss
import numpy as np
import os
import json
import requests
import pandas as pd
from sentence_transformers import SentenceTransformer

embedding_base = "../../embeddings/SP800"
index_base = "../../vector-databases/faiss"

embedding_files = os.listdir(embedding_base)
index_files = os.listdir(index_base)
EMBEDDING_MODELS = {
    "mteb": "thenlper/gte-large",
    "e5_large_v2": "intfloat/e5-large-v2"
}
ollama_api_url = "http://localhost:11434/api/generate"
model_name = "mistral:latest"

top_k = 9

def get_index_file(embed_file, model):
    index_file = [item for item in index_files if embed_file.split('-')[0] in item][0]
    return index_file

def get_top_k_chunks(question, model, embed_file, index_file, k=top_k):
    query_embedding = SentenceTransformer(EMBEDDING_MODELS[model]).encode(question, normalize_embeddings=True).astype("float32")
    index_path = os.path.join(index_base, index_file)
    D, I = faiss.read_index(index_path).search(np.array([query_embedding]), k)
    return [pd.read_parquet(os.path.join(embedding_base, embed_file))["text"].tolist()[i] for i in I[0]]

def build_prompt(question, context_chunks):
    context = "\n\n".join(context_chunks)
    prompt = f"""User the following context to answer the question. Be concise and accurate, and say if you do not know instead of making something up.

                 Context:
                 {context}

                 Question: {question}
                 Answer: """
    return prompt

def query_ollama(prompt, model):
    response = requests.post(ollama_api_url, json={"model": "mistral:latest", "prompt": prompt, "stream": False})
    response.raise_for_status()
    return response.json()["response"]

def rag_pipeline(question, embed_file, model):
    index_file = get_index_file(embed_file, model)
    chunks = get_top_k_chunks(question, model, embed_file, index_file)
    prompt = build_prompt(question, chunks)
    answer = query_ollama(prompt, model)
    return answer

if __name__ == "__main__":
    while True:
        q = input("\nAsk a question (or 'exit'): ")
        if q.strip().lower() == "exit":
            break
        for file in embedding_files:
            for model in EMBEDDING_MODELS:
                if not model.replace('_', '') in file:
                    continue
                answer = rag_pipeline(q, file, model)
                print(f"\nAnswer from {file}: {answer}\n")
