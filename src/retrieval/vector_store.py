"""Builds and queries the Chroma vector store."""
import chromadb
from chromadb.utils import embedding_functions
CHROMA_PATH = "data/processed/chroma_db"
COLLECTION_NAME = "textbook_chunks"
def get_client():
    return chromadb.PersistentClient(path=CHROMA_PATH)
def get_embedding_fn():
    return embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )
def build_collection(chunks: list[dict]):
    client = get_client()
    collection = client.get_or_create_collection(
        name=COLLECTION_NAME,
        embedding_function=get_embedding_fn()
    )
    collection.add(
        ids=[c["chunk_id"] for c in chunks],
        documents=[c["text"] for c in chunks],
        metadatas=[{"source": c["source"], "page": c["page"]} for c in chunks]
    )
    print(f"Indexed {len(chunks)} chunks into Chroma.")
def query_collection(query: str, n_results=4):
    client = get_client()
    collection = client.get_collection(
        name=COLLECTION_NAME,
        embedding_function=get_embedding_fn()
    )
    results = collection.query(query_texts=[query], n_results=n_results)
    return results
