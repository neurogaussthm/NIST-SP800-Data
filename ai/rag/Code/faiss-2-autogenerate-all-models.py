import re
import faiss
import time
import numpy as np
import os
import json
import requests
import pandas as pd
from sentence_transformers import SentenceTransformer

embedding_base = "../../embeddings/SP800"
index_base = "../../vector-databases/faiss-cosine"

embedding_files = os.listdir(embedding_base)
index_files = os.listdir(index_base)
EMBEDDING_MODELS = {
    "mteb": "thenlper/gte-large",
    "e5_large_v2": "intfloat/e5-large-v2"
}
ollama_api_url = "http://localhost:11434/api/generate"
with open("./models.txt", "r") as f:
    model_names = [name.strip() for name in f.readlines()]

top_k = 5
similarity_threshold = 0.8
boost = 1.4

def get_index_file(embed_file, model):
    index_file = [item for item in index_files if embed_file.split('-')[0] in item][0]
    return index_file

def get_top_k_chunks(question, model, embed_file, index_file, k=top_k, sim=similarity_threshold):
    query_embedding = SentenceTransformer(EMBEDDING_MODELS[model]).encode(question, normalize_embeddings=True).astype("float32")
    index_path = os.path.join(index_base, index_file)
    D, I = faiss.read_index(index_path).search(np.array([query_embedding]), 2000)
    path = os.path.join(embedding_base, embed_file)
    df = pd.read_parquet(path)
    titles = set(df["source"].unique())
    matched_doc = None
    pattern = re.compile(r"SP\s*800-(\d+)|800-(\d+)", re.IGNORECASE)
    match = pattern.search(question)
    if match:
        doc_number = match.group(1) or match.group(2)
        for title in titles:
            if re.search(rf"SP?800-{doc_number}", title, re.IGNORECASE):
                matched_doc = title
                break
    boosted_results = []
    for d, i in zip(D[0], I[0]):
        source = df["source"].tolist()[i]
        text = df["text"].tolist()[i]
        if matched_doc and re.search(rf"SP?800-{doc_number}", source, re.IGNORECASE):
            d *= boost
        boosted_results.append((d, f"Source document: ****{source}****\n{text}"))
    boosted_results.sort(reverse=True, key=lambda x: x[0])
    return [i for d, i in boosted_results if d >= sim][:k]

def build_prompt(question, context_chunks):
    context = "\n\n".join(context_chunks)
    prompt = f"""You are an AI assistant with expertise in cybersecurity policy, particularly the NIST SP 800 series. You can answer technical questions related to cybersecurity policy as well as general inquiries. You are also capable of engaging in casual conversation when appropriate.

                If helpful information is available, it will be included under "Context." If the context is directly relevant to the query, use it in your response and cite its source (marked with ****), but just use it naturally, not using phrases like 'According to the context provided', as the user doesn't have access to the context you are given. If the context is **not relevant**, ignore it and answer naturally. If a question is unclear, ask for clarification. If you do not know an answer, say so rather than making something up.

                ### Context:
                {context}

                ### Query:
                {question}

                ### Answer: """
    return prompt

def query_ollama(prompt, llm_model):
    response = requests.post(ollama_api_url, json={"model": llm_model, "prompt": prompt, "stream": False})
    response.raise_for_status()
    return response.json()["response"]

def rag_pipeline(question, embed_file, model, llm_model):
    index_file = get_index_file(embed_file, model)
    chunks = get_top_k_chunks(question, model, embed_file, index_file)
    prompt = build_prompt(question, chunks)
    answer = query_ollama(prompt, llm_model)
    return answer

if __name__ == "__main__":
    with open("question-set-0.txt", 'r') as f:
        qs = f.readlines()
    for llm in model_names:
        for file in embedding_files:
            for model in EMBEDDING_MODELS:
                if not model.replace('_', '') in file:
                    continue
                for q in qs:
                    if q[0] != '#':
                        start_time = time.perf_counter()
                        answer = rag_pipeline(q, file, model, llm)
                        total_time = time.perf_counter() - start_time
                        print(f"\nAnswer from model: {llm} and file: {file}. Time: ({total_time}): {answer}\n")
                        output = f"{q}\n{total_time}\n\n{answer}\n\n"
                    else:
                        output = f"{q}\n\n"
                    if not os.path.exists(f"../faiss-responses-2-{llm}"):
                        os.makedirs(f"../faiss-responses-2-{llm}")
                    with open(f"../faiss-responses-2-{llm}/q0-answer{file.split('.')[0]}.txt", 'a') as f:
                        f.write(output)
                    sleep(0.05)
                    with open("missed-files.txt", 'a') as f:
                        f.write(f"{llm}-{file.split(',')[0]}")
