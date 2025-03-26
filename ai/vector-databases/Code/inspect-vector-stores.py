import weaviate
from pymilvus import connections, Collection, utility
from pymilvus.exceptions import MilvusException

def inspect_milvus():
    print("\nInspecting Milvus Collections...\n" + "-"*40)
    try:
        connections.connect("default", host="localhost", port="19530")
        collections = utility.list_collections()
        print(f"Found {len(collections)} Milvus collections.")

        for name in collections:
            try:
                collection = Collection(name)
                print(f"\n Collection: {name}")
                print(f"   - Description: {collection.description}")
                print(f"   - Schema fields:")
                for field in collection.schema.fields:
                    print(f"     • {field.name} ({field.dtype})")
                print(f"   - num of entities: {collection.num_entities}")
                print(f"   - Indexes: {[idx.params for idx in collection.indexes]}")
            except MilvusException as e:
                print(f"rror inspecting collection '{name}': {e}")
    except Exception as e:
        print(f"Could not connect to Milvus: {e}")


def inspect_weaviate():
    print("\nInspecting Weaviate Classes...\n" + "-"*40)
    try:
        connection = weaviate.connect.ConnectionParams.from_params(http_host="localhost", http_port=8000, http_secure=False, grpc_host="localhost", grpc_port=50051, grpc_secure=False)
        client = weaviate.WeaviateClient(connection)
        client.connect()
        collections = client.collections.list_all()
        print(f"Found {len(collections)} Weaviate collections.")
        for name in collections:
            collection = client.collections.get(name)
            print(f"\n Collection: {name}")
            print("   - Properties:")
            config = collection.config.get()
            for prop in config.properties:
                print(f"      {prop.name} ({prop.data_type})")
            print(f"   - Total objects: {collection.aggregate.over_all(total_count=True).total_count}")
    except Exception as e:
        print(f"Weaviate inspection failed: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    inspect_milvus()
    inspect_weaviate()
