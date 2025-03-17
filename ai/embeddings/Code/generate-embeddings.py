import os
import json
import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer

# Define the embedding models
EMBEDDING_MODELS = {
    "mteb": "thenlper/gte-large",
    "e5_large_v2": "intfloat/e5-large-v2",
    "instructor_xl": "hkunlp/instructor-xl"
}

def list_directories(path):
    return [item for item in os.listdir(path) if os.path.isdir(os.path.join(path, item))]

def load_json(filepath):
    """Load preprocessed JSON file."""
    with open(filepath, "r", encoding="cp1252") as f:
        return json.load(f)

def embed_texts(texts, model_name):
    """Generate embeddings for a list of texts using the specified model."""
    model = SentenceTransformer(EMBEDDING_MODELS[model_name])
    return model.encode(texts, convert_to_numpy=True)

def save_embeddings_numpy(embeddings, output_file):
    """Save embeddings to a NumPy file."""
    np.save(output_file, embeddings)

def save_embeddings_parquet(embeddings, texts, output_file):
    """Save embeddings to a Parquet file along with text data."""
    df = pd.DataFrame({"text": texts, "embedding": embeddings.tolist()})
    df.to_parquet(output_file, index=False)

def process_files(input_folder, output_folder, model_name, storage_format="numpy"):
    """Generate and store embeddings from JSON preprocessed files."""
    os.makedirs(output_folder, exist_ok=True)
    
    for file in os.listdir(input_folder):
        if file.endswith(".json"):
            filepath = os.path.join(input_folder, file)
            data = load_json(filepath)
            
            texts = [
 	        entry["text"] for section in data 
    	 	for entry in section.get("subsections", []) 
    		if isinstance(entry.get("text"), str) and entry["text"].strip()
	    ]
            embeddings = embed_texts(texts, model_name)
            
            output_filename = os.path.join(output_folder, file.replace(".json", f"_{model_name}.{storage_format}"))
            
            if storage_format == "numpy":
                save_embeddings_numpy(embeddings, output_filename)
            elif storage_format == "parquet":
                save_embeddings_parquet(embeddings, texts, output_filename)
            
            print(f"Saved embeddings to {output_filename}")

# Example usage
if __name__ == "__main__":
    for directory in list_directories("../../preprocessing"):
        for model in EMBEDDING_MODELS:
            for format in ["parquet", "numpy"]:
                output_directory = "../" + directory + "-" + model + "-" + format
                input_directory = "../../preprocessing/" + directory + "/jsonOutput"
                process_files(
                    input_folder=input_directory,
                    output_folder=output_directory, 
                    model_name=model,  # Change to "e5_large_v2" or "instructor_xl" or "mteb" as needed
                    storage_format=format  # Change to "parquet" or "numpy" as needed
                )
