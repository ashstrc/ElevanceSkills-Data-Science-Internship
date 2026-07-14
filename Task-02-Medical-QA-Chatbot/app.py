import streamlit as st

from retrieval.retriever import MedicalRetriever
from medical.entity_recognition import MedicalEntityRecognizer


st.set_page_config(
    page_title="Medical QA Chatbot",
    page_icon="🩺",
    layout="wide"
)

# Load models only once
@st.cache_resource
def load_components():
    retriever = MedicalRetriever()
    recognizer = MedicalEntityRecognizer()
    return retriever, recognizer


retriever, recognizer = load_components()

st.title("🩺 Medical Question Answering Chatbot")
st.write("Task 2 - Medical QA using MedQuAD Dataset")

st.divider()

query = st.text_area(
    "Enter your medical question",
    placeholder="Example: What are the symptoms of diabetes?"
)

if st.button("Get Answer"):

    if query.strip() == "":
        st.warning("Please enter a medical question.")
        st.stop()

    entities = recognizer.recognize(query)
    result = retriever.search(query)

    if not result["found"]:
        st.error("No relevant medical information found.")
        st.write(f"Similarity Score: **{result['score']*100:.2f}%**")
        st.stop()

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Detected Disease")
        st.success(entities["Disease"] if entities["Disease"] else "Not Found")

    with col2:
        st.subheader("Detected Intent")
        st.info(entities["Intent"])

    st.divider()

    st.subheader("Retrieved Information")

    st.write(f"**Medical Topic:** {result['focus']}")
    st.write(f"**Matched Question:** {result['question']}")
    st.write(f"**Similarity Score:** {result['score']*100:.2f}%")

    st.divider()

    st.subheader("Medical Answer")

    st.write(result["answer"])

    st.warning(
        "This chatbot provides educational information only and should not replace professional medical advice."
    )