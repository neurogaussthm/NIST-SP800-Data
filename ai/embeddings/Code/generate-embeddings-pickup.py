import os
import json
import numpy as np
import pandas as pd
import torch
from sentence_transformers import SentenceTransformer

EMBEDDING_MODELS = {
    "mteb": "thenlper/gte-large",
    "e5_large_v2": "intfloat/e5-large-v2"  #, "instructor_xl": "hkunlp/instructor-xl"  # Too large of model for Nvidia 4090 to handle without crashing.
}

def list_directories(path):
    return [item for item in os.listdir(path) if os.path.isdir(os.path.join(path, item))]

def load_json(filepath):
    with open(filepath, "r", encoding="cp1252") as f:
        return json.load(f)

def embed_texts(texts, model_name):
    model = SentenceTransformer(EMBEDDING_MODELS[model_name]) # , device="cpu")  # Tried CPU encoding since 4090 failed and it has 128GB of RAM.
    embeddings = model.encode(texts, convert_to_numpy=True) # , batch_size=128)  # With CPU encoding modified batch size to reduce time. Maybe possible for instructor-xl with CPU and lower batch size.

    # Clear CUDA memory after encoding
    if torch.cuda.is_available():
        torch.cuda.empty_cache()

    return embeddings

def save_embeddings_numpy(embeddings, output_file):
    """Save embeddings to a NumPy file."""
    np.save(output_file, embeddings)

def save_embeddings_parquet(embeddings, texts, output_file):
    """Save embeddings to a Parquet file along with text data."""
    df = pd.DataFrame({"text": texts, "embedding": embeddings.tolist()})
    df.to_parquet(output_file, index=False)

def extract_texts(data):
    texts = []

    def collect_text(entry):
        """Recursively collect text from different JSON structures."""
        if isinstance(entry, dict):
            if "text" in entry and isinstance(entry["text"], str) and entry["text"].strip():
                texts.append(entry["text"])
            elif "content" in entry:
                if isinstance(entry["content"], str) and entry["content"].strip():
                    texts.append(entry["content"])
                elif isinstance(entry["content"], list):
                    for sub_entry in entry["content"]:
                        collect_text(sub_entry)
            if "subsections" in entry and isinstance(entry["subsections"], list):
                for subsection in entry["subsections"]:
                    collect_text(subsection)
        elif isinstance(entry, list):
            for sub_entry in entry:
                collect_text(sub_entry)

    collect_text(data)
    return texts

def process_files(input_folder, output_folder, model_name, storage_format="numpy"):
    """Generate and store embeddings from JSON preprocessed files."""
    os.makedirs(output_folder, exist_ok=True)

    for file in os.listdir(input_folder):
        if file.endswith(".json"):
            filepath = os.path.join(input_folder, file)
            output_filename = os.path.join(output_folder, file.replace(".json", f"_{model_name}.{storage_format}"))

            # Skip if the file already exists
            if os.path.exists(output_filename) or os.path.exists(f"{output_filename}.npy"):
                print(f"Skipping {output_filename}, already exists.")
                continue

            data = load_json(filepath)
            texts = extract_texts(data)

            if not texts:
                print(f"Skipping {file}, no valid texts found.")
                continue

            embeddings = embed_texts(texts, model_name)

            if storage_format == "numpy":
                save_embeddings_numpy(embeddings, output_filename)
            elif storage_format == "parquet":
                save_embeddings_parquet(embeddings, texts, output_filename)

            print(f"Saved embeddings to {output_filename}")


if __name__ == "__main__":
    for model in EMBEDDING_MODELS:
        for directory in list_directories("../../preprocessing"):
            if directory == "venv" or directory == "Code":
                continue
            for format in ["parquet", "numpy"]:
                output_directory = f"../{directory}-{model}-{format}"
                input_directory = f"../../preprocessing/{directory}/jsonOutput"
                process_files(
                    input_folder=input_directory,
                    output_folder=output_directory, 
                    model_name=model, 
                    storage_format=format
                )
