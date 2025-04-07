import requests
import os
import json
import time

ollama_api_url = "http://localhost:11434/api/generate"
model_name = "mistral:latest"

def query_ollama(prompt, llm_model):
    response = requests.post(ollama_api_url, json={"model": llm_model, "prompt": prompt, "stream": False})
    response.raise_for_status()
    return response.json()["response"]

if __name__ == "__main__":
    with open("question-set-0.txt", 'r') as f:
        qs = f.readlines()
    for llm in mdoel_names:
        for q in qs:
            if q[0] != '#':
                start_time = time.perf_counter()
                answer = query_ollama(q, llm)
                total_time = time.perf_counter() - start_time
                print(f"\nAnswer from {llm} ({total_time}): {answer}\n")
                output = f"{q}\n{total_time}\n\n{answer}\n\n"
            else:
                output = f"{q}\n\n"
            with open(f"../faiss-responses-2-no-rag/q0-answer-{llm}-no-rag.txt", 'a') as f:
                f.write(output)
