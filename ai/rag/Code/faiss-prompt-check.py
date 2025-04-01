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

top_k = 5
similarity_threshold = 0.3

def get_index_file(embed_file, model):
    index_file = [item for item in index_files if embed_file.split('-')[0] in item][0]
    return index_file

def get_top_k_chunks(question, model, embed_file, index_file, k=top_k, sim=similarity_threshold):
    query_embedding = SentenceTransformer(EMBEDDING_MODELS[model]).encode(question, normalize_embeddings=True).astype("float32")
    index_path = os.path.join(index_base, index_file)
    D, I = faiss.read_index(index_path).search(np.array([query_embedding]), k)
    path = os.path.join(embedding_base, embed_file)
    df = pd.read_parquet(path)
    filtered_chunks = [("Source document: ****" + df["source"].tolist()[i] + "****\n" + df["text"].tolist()[i]) for d, i in zip(D[0], I[0]) if d <= sim]
    return filtered_chunks

def build_prompt(question, context_chunks):
    context = "\n\n".join(context_chunks)
    prompt = f"""You are an AI assistant with expertise in cybersecurity policy, particularly the NIST SP 800 series. You can answer technical questions related to cybersecurity policy as well as general inquiries. You are also capable of engaging in casual conversation when appropriate.

                If helpful information is available, it will be included under "Context." If the context is directly relevant to the query, use it in your response and cite its source (marked with ****). If the context is **not relevant**, ignore it and answer naturally. If a question is unclear, ask for clarification. If you do not know an answer, say so rather than making something up.

                ### Context:
                {context}

                ### Query:
                {question}

                ### Answer: """
    print(prompt)
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
#        for file in embedding_files:
#            for model in EMBEDDING_MODELS:
#                if not model.replace('_', '') in file:
#                    continue
#                answer = rag_pipeline(q, file, model)
#                print(f"\nAnswer from {file}: {answer}\n")
        answer = rag_pipeline(q, "bytoken500200o200kbasemteb-SP800-ALL.parquet", "mteb")
        print(f"\nAnswer: {answer}\n")
