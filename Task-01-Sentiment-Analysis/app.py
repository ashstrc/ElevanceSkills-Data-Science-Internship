import streamlit as st
from chatbot import chatbot

st.set_page_config(
    page_title="AI Sentiment Analysis Assistant",
    page_icon="🤖",
    layout="centered"
)

# Sidebar
with st.sidebar:
    st.title("📊 Project Information")

    st.markdown("### Internship Task")
    st.write("Task 1 - Sentiment Analysis")

    st.markdown("### Model")
    st.code("cardiffnlp/twitter-roberta-base-sentiment-latest")

    st.markdown("### Framework")
    st.write("🤗 HuggingFace Transformers")
    st.write("🔥 PyTorch")
    st.write("🎈 Streamlit")

    st.markdown("---")
    st.caption("Developed by Ashmit Kumar")

# Header
st.title("🤖 AI Sentiment Analysis Assistant")
st.caption("Real-Time Emotion Detection using HuggingFace Transformers")

st.markdown("---")

message = st.text_area(
    "💬 Enter your message",
    placeholder="Example: I am really happy today!"
)

if st.button("🔍 Analyze Sentiment", use_container_width=True):

    if message.strip():

        result = chatbot(message)

        col1, col2 = st.columns(2)

        with col1:

            if result["sentiment"] == "Positive":
                st.success("🟢 Positive")

            elif result["sentiment"] == "Negative":
                st.error("🔴 Negative")

            else:
                st.warning("🟡 Neutral")

        with col2:

            confidence = result["confidence"]

            st.metric(
                "Confidence",
                f"{confidence*100:.2f}%"
            )

            st.progress(confidence)

        st.markdown("### 🤖 Bot Response")
        st.info(result["reply"])

    else:
        st.warning("Please enter a message.")

st.markdown("---")
st.caption("Powered by HuggingFace Transformers | Streamlit")