import streamlit as st
from agents.researchagent import ResearchAgent
from agents.writeragent import WriterAgent
from agents.criticagent import CriticAgent
from utils.logger import Logger
import os

st.set_page_config(page_title="Agentic AI Research-to-Article Pipeline", layout="wide")

st.title("🧠 Agentic AI — Research to Article Generator")

logger = Logger()

if "final_output" not in st.session_state:
    st.session_state.final_output = ""

topic = st.text_input("Enter a research topic:", placeholder="e.g., Artificial Intelligence in Healthcare")

if st.button("Run Pipeline"):
    if topic.strip():
        logger.log(f"Starting research on topic: {topic}")
        with st.spinner("🔍 Researching..."):
            research_agent = ResearchAgent()
            sources = research_agent.act(topic)

        st.subheader("📚 Research Sources")
        for s in sources:
            st.markdown(f"- **{s['title']}** — {s['summary']} ([link]({s['url']}))")

        with st.spinner("✍️ Drafting article..."):
            writer_agent = WriterAgent()
            draft = writer_agent.act(sources)

        st.subheader("📝 Drafted Article")
        st.text_area("Article Draft", draft["draft"], height=300)

        with st.spinner("🧩 Critiquing and improving..."):
            critic_agent = CriticAgent()
            final = critic_agent.act(draft)

        st.subheader("🔍 Critique Summary")
        if isinstance(final["critique"], list):
            for issue in final["critique"]:
                st.markdown(f"- {issue}")
        else:
            st.markdown(final["critique"])

        st.subheader("✅ Improved Final Article")
        st.text_area("Improved Article", final["improved_draft"], height=300)

        st.session_state.final_output = final["improved_draft"]

        os.makedirs("outputs", exist_ok=True)
        with open("outputs/final_article.txt", "w", encoding="utf-8") as f:
            f.write(final["improved_draft"])

        logger.log("Pipeline complete. Final article saved to outputs/final_article.txt")
        st.success("🎉 Pipeline complete! Final article saved to outputs/final_article.txt")
    else:
        st.warning("Please enter a valid topic to begin.")
