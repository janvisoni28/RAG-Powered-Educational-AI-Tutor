"""Run once (or whenever new textbooks are added) to build the vector index."""

from src.ingestion.loader import load_all_textbooks
from src.ingestion.chunker import chunk_pages
from src.retrieval.vector_store import build_collection

if __name__ == "__main__":
    pages = load_all_textbooks("data/textbooks")
    print(f"Loaded {len(pages)} pages")

    chunks = chunk_pages(pages)
    print(f"Created {len(chunks)} chunks")

    build_collection(chunks)
