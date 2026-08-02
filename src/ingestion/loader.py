"""Loads raw textbook PDFs and pulls out clean text per page."""
from pypdf import PdfReader
from pathlib import Path
def load_pdf(file_path: str) -> list[dict]:
    reader = PdfReader(file_path)
    book_name = Path(file_path).stem
    pages = []
    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        if text and text.strip():
            pages.append({
                "source": book_name,
                "page": i + 1,
                "text": text.strip()
            })
    return pages
def load_all_textbooks(folder_path: str) -> list[dict]:
    all_pages = []
    for pdf_file in Path(folder_path).glob("*.pdf"):
        print(f"Loading {pdf_file.name}...")
        all_pages.extend(load_pdf(str(pdf_file)))
    return all_pages
