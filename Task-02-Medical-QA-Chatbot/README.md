# 🩺 Medical Question Answering Chatbot

A Medical Question Answering Chatbot developed as part of the **ElevanceSkills Data Science Internship - Task 2**.

The chatbot uses the **MedQuAD (Medical Question Answering Dataset)** and a **retrieval-based semantic search** approach to answer medical questions. It also performs **basic medical entity recognition** to identify diseases and medical categories such as symptoms, treatments, diagnosis, causes, prevention, and risk factors.

---

# Features

- 📂 Parses the MedQuAD XML dataset
- 🧠 Generates semantic embeddings using Sentence Transformers
- 🔍 Retrieval-based semantic search using cosine similarity
- 🏥 Basic Medical Entity Recognition
  - Disease Detection
  - Symptoms
  - Treatments
  - Diagnosis
  - Causes
  - Prevention
  - Risk Factors
- 📊 Displays similarity score
- 💻 Interactive Streamlit interface
- ⚠ Educational medical disclaimer

---

# Project Structure

```
Medical-QA_BOT/

│
├── app.py
├── README.md
├── requirements.txt
│
├── data/
│   └── MedQuAD Dataset
│
├── database/
│   ├── medical_qa.csv
│   └── embeddings.pkl
│
├── parser/
│   └── parse_medquad.py
│
├── retrieval/
│   ├── embedder.py
│   └── retriever.py
│
└── medical/
    └── entity_recognition.py
```

---

# Technologies Used

- Python
- Streamlit
- Pandas
- Sentence Transformers
- PyTorch
- MedQuAD Dataset

---

# Dataset

This project uses the **MedQuAD (Medical Question Answering Dataset)** developed from multiple NIH medical websites.

GitHub Repository:

https://github.com/abachaa/MedQuAD

---

# How It Works

```
User Medical Question
          │
          ▼
Medical Entity Recognition
(Disease + Medical Category)
          │
          ▼
Sentence Transformer
          │
          ▼
Semantic Embedding
          │
          ▼
Cosine Similarity Search
          │
          ▼
Best Matching Medical Question
          │
          ▼
Medical Answer
```

---

# Installation

## Clone the Repository

```bash
git clone https://github.com/your-username/Medical-QA_BOT.git
```

---

## Create Virtual Environment

```bash
python -m venv .venv
```

Activate it

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Project

## Step 1 — Parse the Dataset

```bash
python parser/parse_medquad.py
```

This creates

```
database/medical_qa.csv
```

---

## Step 2 — Generate Embeddings

```bash
python retrieval/embedder.py
```

This creates

```
database/embeddings.pkl
```

---

## Step 3 — Launch Streamlit

```bash
streamlit run app.py
```

---

# Example Questions

- What is diabetes?
- What are the symptoms of diabetes?
- How is asthma treated?
- What causes migraine?
- How is breast cancer diagnosed?
- What are the risk factors of hypertension?

---

# Example Output

The chatbot displays

- Detected Disease
- Detected Medical Category
- Retrieved Medical Topic
- Matched Question
- Similarity Score
- Medical Answer

---

# Basic Medical Entity Recognition

The chatbot recognizes:

- Diseases
- Symptoms
- Treatments
- Diagnosis
- Causes
- Prevention
- Risk Factors
- General Medical Queries

---

# Retrieval Method

Instead of generating responses, the chatbot retrieves the most semantically similar medical question from the MedQuAD dataset.

Workflow:

```
Question
    ↓
Sentence Embedding
    ↓
Cosine Similarity
    ↓
Best Matching Question
    ↓
Medical Answer
```

---

# Disclaimer

This chatbot is intended **only for educational and research purposes**.

It should **not** be considered a substitute for professional medical advice, diagnosis, or treatment. Always consult a qualified healthcare professional regarding any medical condition.

---

# Internship Task

**ElevanceSkills Data Science Internship**

**Task 2**

Develop a Medical Question Answering Chatbot using the MedQuAD dataset with:

- Retrieval-based Question Answering
- Basic Medical Entity Recognition
- Streamlit User Interface

---

# Author

**Ashmit Kumar**
