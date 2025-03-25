from pymilvus import connections, utility
import weaviate


connections.connect("default", host="localhost", port="19530")
collection_names = utility.list_collections()
for collection_name in collection_names:
    utility.drop_collection(collection_name)

connection = weaviate.connect.ConnectionParams.from_params(http_host="localhost", http_port=8000, http_secure=False, grpc_host="localhost", grpc_port=50051, grpc_secure=False)
client = weaviate.WeaviateClient(connection)
client.connect()
existing = client.collections.list_all()
for collection in existing:
    client.collections.delete(collection)
client.close()
