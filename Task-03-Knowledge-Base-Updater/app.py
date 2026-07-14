import os
import shutil
import streamlit as st
import pandas as pd

from updater import KnowledgeUpdater

st.set_page_config(
    page_title="Knowledge Base Updater",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Dynamic Knowledge Base Updater")

st.divider()

updater = KnowledgeUpdater()

csv_path = "database/knowledge.csv"

if os.path.exists(csv_path):
    df = pd.read_csv(csv_path)
else:
    df = pd.DataFrame(columns=["filename", "content"])

processed_files = os.listdir("processed")

col1, col2, col3 = st.columns(3)

col1.metric("Documents Indexed", len(df))
col2.metric("Embeddings Stored", len(df))
col3.metric("Processed Files", len(processed_files))

st.divider()

uploaded_file = st.file_uploader(
    "Upload New Knowledge",
    type=["txt"]
)

if uploaded_file is not None:

    save_path = os.path.join(
        "new_documents",
        uploaded_file.name
    )

    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    updater.update()

    st.success("Knowledge Base Updated Successfully!")

st.divider()

st.subheader("Recently Processed Files")

if processed_files:

    for file in processed_files[::-1]:

        st.write("✅", file)

else:

    st.info("No processed files found.")

st.divider()

st.subheader("Knowledge Base")

st.dataframe(
    df,
    width="stretch"
)