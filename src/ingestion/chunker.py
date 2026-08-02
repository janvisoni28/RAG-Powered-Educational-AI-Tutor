"""Splits page text into overlapping chunks for embedding."""
from langchain.text_splitter import RecursiveCharacterTextSplitter
def chunk_pages(pages: list[dict], chunk_size=800, chunk_overlap=120) -> list[dict]:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", ". ", " ", ""]
    )
    chunks = []
    for page in pages:
        pieces = splitter.split_text(page["text"])
        for idx, piece in enumerate(pieces):
            chunks.append({
                "text": piece,
                "source": page["source"],
                "page": page["page"],
                "chunk_id": f"{page['source']}_p{page['page']}_c{idx}"
            })
    return chunks
