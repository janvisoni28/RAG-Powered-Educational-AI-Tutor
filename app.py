import streamlit as st
from src.generation.llm_chain import answer_question
st.set_page_config(page_title="AI Science Tutor", page_icon="🔬")
st.title("🔬 RAG-Powered Science Tutor")
st.caption("Ask a science question - I'll pull answers straight from your textbooks.")
level = st.selectbox(
    "Your reading level",
    ["elementary", "middle_school", "high_school", "college"],
    index=1
)
question = st.text_input("What do you want to understand?")
if st.button("Ask") and question:
    with st.spinner("Digging through the textbook..."):
        result = answer_question(question, level)
    st.markdown("### Answer")
    st.write(result["answer"])
    st.markdown("### Sources")
    for src in result["sources"]:
        st.caption(f"📖 {src['book']} - page {src['page']}")
