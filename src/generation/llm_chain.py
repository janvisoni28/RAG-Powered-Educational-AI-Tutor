"""Ties retrieval + prompt + LLM call together."""
import os
from dotenv import load_dotenv
from groq import Groq
from src.retrieval.vector_store import query_collection
from src.generation.prompt_templates import build_prompt
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
def answer_question(question: str, reading_level: str = "middle_school") -> dict:
    results = query_collection(question, n_results=4)
    docs = results["documents"][0]
    metas = results["metadatas"][0]
    prompt = build_prompt(question, docs, reading_level)
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4,
    )
    return {
        "answer": response.choices[0].message.content,
        "sources": [{"book": m["source"], "page": m["page"]} for m in metas]
    }
