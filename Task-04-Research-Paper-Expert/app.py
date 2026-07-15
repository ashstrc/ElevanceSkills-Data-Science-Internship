import streamlit as st

from retrieval.retriever import ResearchRetriever
from summarizer.summarizer import PaperSummarizer
from llm.explainer import ResearchExplainer
from utils.concept_extractor import ConceptExtractor
from visualization.concept_map import ConceptMap
from memory.conversation import ConversationMemory


# ===================================================
# Page Configuration
# ===================================================

st.set_page_config(
    page_title="AI Research Paper Expert",
    page_icon="📚",
    layout="wide"
)


# ===================================================
# Cached Resources
# ===================================================

@st.cache_resource
def load_retriever():
    return ResearchRetriever()


@st.cache_resource
def load_summarizer():
    return PaperSummarizer()


@st.cache_resource
def load_explainer():
    return ResearchExplainer()


@st.cache_resource
def load_extractor():
    return ConceptExtractor()


retriever = load_retriever()
summarizer = load_summarizer()
explainer = load_explainer()
extractor = load_extractor()


# ===================================================
# Conversation Memory
# ===================================================

if "memory" not in st.session_state:
    st.session_state.memory = ConversationMemory()

memory = st.session_state.memory


# ===================================================
# UI Header
# ===================================================

st.title("📚 AI Research Paper Expert")

st.markdown("""
Ask questions about **Artificial Intelligence research papers** and receive:

- 📄 Relevant Research Paper
- 📝 Automatic Paper Summary
- 💡 AI-generated Explanation
- 🧠 Concept Visualization
- 💬 Conversation Memory
""")


# ===================================================
# Variables
# ===================================================

paper = None
summary = None
explanation = None
figure = None


# ===================================================
# Chat Input
# ===================================================

question = st.chat_input(
    "Ask an AI research question..."
)


if question:

    with st.chat_message("user"):
        st.write(question)

    # ===============================================
    # Step 1 : Semantic Retrieval
    # ===============================================

    with st.spinner("🔍 Searching AI research papers..."):

        paper = retriever.search(question)

    if paper:

        # ===========================================
        # Step 2 : Summarization
        # ===========================================

        with st.spinner("📝 Generating paper summary..."):

            summary = summarizer.summarize(
                paper["abstract"]
            )

        # ===========================================
        # Step 3 : AI Explanation
        # ===========================================

        with st.spinner("🤖 Generating AI explanation..."):

            explanation = explainer.explain(
                question,
                summary
            )

        # ===========================================
        # Save Conversation
        # ===========================================

        memory.add_user_message(question)

        memory.add_assistant_message(explanation)

        # ===========================================
        # Step 4 : Concept Extraction
        # ===========================================

        concepts = extractor.extract(
            explanation
        )

        graph = ConceptMap()

        graph.build_graph(concepts)

        figure = graph.get_figure()

    # ===============================================
    # Assistant Status
    # ===============================================

    with st.chat_message("assistant"):

        if paper is None:

            st.error(
                "❌ No relevant AI research paper found."
            )

        else:

            st.success(
                "✅ Research paper retrieved successfully!"
            )


# ===================================================
# Main Layout
# ===================================================

st.divider()

col1, col2 = st.columns(2)


# ===================================================
# LEFT COLUMN
# ===================================================

with col1:

    st.subheader("📄 Retrieved Paper")

    if paper:

        st.markdown(
            f"**Title:** {paper['title']}"
        )

        st.markdown(
            f"**Authors:** {paper['authors']}"
        )

        st.markdown(
            f"**Categories:** {paper['categories']}"
        )

        st.markdown(
            f"**Similarity Score:** {paper['score'] * 100:.2f}%"
        )

        with st.expander("📖 View Abstract"):

            st.write(
                paper["abstract"]
            )

    else:

        st.info(
            "Search for an AI topic to retrieve a research paper."
        )

    st.divider()

    st.subheader("📝 Paper Summary")

    if summary:

        st.write(summary)

    else:

        st.info(
            "Summary will appear here."
        )


# ===================================================
# RIGHT COLUMN
# ===================================================

with col2:

    st.subheader("💡 AI Explanation")

    if explanation:

        st.write(explanation)

    else:

        st.info(
            "Explanation will appear here."
        )

    st.divider()

    st.subheader("🧠 Concept Map")

    if figure:

        st.pyplot(
            figure,
            clear_figure=True
        )

    else:

        st.info(
            "Concept map will appear here."
        )


# ===================================================
# Conversation History
# ===================================================

st.divider()

st.subheader("💬 Conversation History")

history = memory.get_history()

if history:

    for message in history:

        if message["role"] == "user":

            with st.chat_message("user"):

                st.write(message["content"])

        else:

            with st.chat_message("assistant"):

                st.write(message["content"])

else:

    st.info(
        "No conversation yet."
    )