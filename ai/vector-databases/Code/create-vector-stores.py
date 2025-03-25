import os
import faiss
import numpy as np
import weaviate
import pandas as pd
from pymilvus import connections, Collection, CollectionSchema, FieldSchema, DataType

def create_faiss_store(method_path, output_path):
    for embedding_file in os.listdir(method_path):
        embedding_path = os.path.join(method_path, embedding_file)
        if embedding_file.endswith(".npy"):
            embeddings = np.load(embedding_path)
            dimension = embeddings.shape[1]
            if os.path.exists(output_path):
                index = faiss.read_index(output_path)
            else:
                index = faiss.IndexFlatL2(dimension)
            index.add(embeddings)
            faiss.write_index(index, output_path)
    print(f"Successfully created FAISS store {output_path}")

def create_weaviate_store(method_path, collection_name):
    connection = weaviate.connect.ConnectionParams.from_params(http_host="localhost", http_port=8000, http_secure=False, grpc_host="localhost", grpc_port=50051, grpc_secure=False)
    client = weaviate.WeaviateClient(connection)
    client.connect()
    properties = [weaviate.classes.config.Property(name="text", data_type=weaviate.classes.config.DataType.TEXT)]
    config = weaviate.classes.config.Configure()
    try:
        for embedding_file in os.listdir(method_path):
            embedding_path = os.path.join(method_path, embedding_file)
            if embedding_file.endswith(".parquet"):
                df = pd.read_parquet(embedding_path)
                if not client.collections.exists(collection_name):
                    client.collections.create(name=collection_name, vectorizer_config=config.Vectorizer.none(), vector_index_config=config.VectorIndex.hnsw(distance_metric=weaviate.classes.config.VectorDistances.COSINE), properties=properties)
                collection = client.collections.get(collection_name)
                with collection.batch.fixed_size(batch_size=100) as batch:
                    for i, row in df.iterrows():
                        vector = row["embedding"].tolist()
                        data_object = { "text": row["text"] }
                        batch.add_object(properties=data_object, vector=vector)
        print(f"Successfully created Weaviate collection '{collection_name}'")
    finally:
        client.close()

def create_milvus_store(method_path, collection_name):
    connections.connect("default", host="localhost", port="19530")
    for embedding_file in os.listdir(method_path):
        embedding_path = os.path.join(method_path, embedding_file)
        if embedding_file.endswith(".parquet"):
            df = pd.read_parquet(embedding_path)
            vectors = np.array(df['embedding'].tolist())
            if vectors.dtype != np.float32:
                vectors = vectors.astype(np.float32)
            vector_dim = vectors.shape[1]
            if collection_name in Collection.list():
                collection = Collection(name=collection_name)
                collection.load()
                collection.insert([vectors])
            else:
                fields = [
                    FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, auto_id=True),
                    FieldSchema(name="vector", dtype=DataType.FLOAT_VECTOR, dim=vector_dim)
                ]
                schema = CollectionSchema(fields, description="Vector store")
                collection = Collection(name=collection_name, schema=schema)
                collection.insert([vectors])
                index_params = {
                    "metric_type": "L2",
                    "index_type": "IVF_FLAT",
                    "params": {"nlist": 128}
                }
                collection.create_index("vector", index_params)
                collection.load()
    print(f"Successfully created Milvus store {collection_name}")

def process_embeddings(base_embedding_dir, vector_store_dir):
    for method_dir in os.listdir(base_embedding_dir):
        method_path = os.path.join(base_embedding_dir, method_dir)
        if not os.path.isdir(method_path) or method_dir == "Code":
            continue

        output_faiss = os.path.join(vector_store_dir, f"{method_dir.replace('-', '').replace('_', '')}FAISS.index")
        create_faiss_store(method_path, output_faiss)
        collection_name = f"{method_dir.replace('-', '').replace('_', '')}WEAVIATE"
        create_weaviate_store(method_path, collection_name)
        collection_name = f"{method_dir.replace('-', '').replace('_', '')}MILVUS"
        create_milvus_store(method_path, collection_name)

if __name__ == "__main__":
    process_embeddings("../../embeddings", "../faiss")
