# 📚 Dynamic Knowledge Base Updater

A Python-based system for dynamically expanding a chatbot's knowledge base by automatically processing new medical documents, generating vector embeddings, and updating the local vector database.

## 📌 Project Overview

This project demonstrates how a chatbot can continuously learn from newly added documents without rebuilding the entire knowledge base.

New documents are automatically processed, embedded using Sentence Transformers, stored in a vector database, and made available for future retrieval.

---

## ✨ Features

- Automatic document ingestion
- Dynamic knowledge base expansion
- Vector embedding generation
- Automatic vector database updates
- Local CSV knowledge storage
- Processed file management
- Scheduler for periodic updates
- Streamlit dashboard
- Input validation for incomplete documents

---

## 🏗️ Project Structure

```
Task-03-Knowledge-Base-Updater
│
├── app.py
├── loader.py
├── updater.py
├── scheduler.py
├── vector_store.py
├── requirements.txt
├── README.md
│
├── database/
│   ├── knowledge.csv
│   └── embeddings.pkl
│
├── new_documents/
│
└── processed/
```

---

## ⚙️ Workflow

```
New Document
      │
      ▼
new_documents/
      │
      ▼
Document Loader
      │
      ▼
Sentence Transformer
      │
      ▼
Generate Embeddings
      │
      ▼
Update knowledge.csv
      │
      ▼
Update embeddings.pkl
      │
      ▼
Move file to processed/
```

---

## 🚀 Installation

Clone the repository

```bash
git clone <repository-url>
```

Create virtual environment

```bash
python -m venv .venv
```

Activate virtual environment

Windows

```bash
.\.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

### Start Scheduler

```bash
python scheduler.py
```

The scheduler periodically checks the `new_documents` folder and updates the vector database automatically.

---

### Launch Dashboard

```bash
streamlit run app.py
```

---

## 📤 Adding New Knowledge

### Method 1 (Recommended)

Launch the Streamlit application and upload a medical text document.

### Method 2

Place a `.txt` file inside:

```
new_documents/
```

The scheduler will automatically:

- Read the document
- Generate embeddings
- Update the knowledge base
- Move the document to `processed`

---

## 🧠 Technologies Used

- Python
- Streamlit
- Pandas
- Sentence Transformers
- Pickle
- Local Vector Database

---

## 📈 Future Improvements

- PDF document support
- DOCX document support
- Automatic file monitoring using Watchdog
- FAISS vector indexing
- Semantic search integration
- Cloud storage support

---

## 👨‍💻 Developed By

Ashmit Kumar