"""Prompt templates - reading level ke hisaab se explanation adjust karte hain."""
READING_LEVELS = {
    "elementary": "Explain like the student is in grade 5-6. Use very simple words, short sentences, and a relatable everyday analogy.",
    "middle_school": "Explain like the student is in grade 8-9. Use clear language, define technical terms when you use them.",
    "high_school": "Explain at a grade 11-12 level. You can use standard scientific vocabulary but still explain any advanced terms.",
    "college": "Explain at an undergraduate level. Assume familiarity with basic scientific concepts and terminology."
}
def build_prompt(question: str, context_chunks: list[str], level: str) -> str:
    context = "\n\n---\n\n".join(context_chunks)
    level_instruction = READING_LEVELS.get(level, READING_LEVELS["middle_school"])
    return f"""You are a patient, encouraging science tutor.

{level_instruction}

Use ONLY the textbook excerpts below to answer. If the excerpts don't fully cover the question, say so honestly instead of making things up.

Textbook excerpts:
{context}

Student's question: {question}

Answer:"""
