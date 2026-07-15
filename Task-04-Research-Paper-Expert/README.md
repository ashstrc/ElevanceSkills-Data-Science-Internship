# 📚 AI Research Paper Expert

An AI-powered Research Paper Assistant developed as part of a Data Science Internship.

The application uses semantic search to retrieve the most relevant AI research paper from a dataset of research papers, automatically summarizes the paper, explains it in simple English using an open-source Large Language Model (SmolLM2), extracts important concepts, and visualizes them through an interactive concept graph.

---

## ✨ Features

- 🔍 Semantic Search using Sentence Transformers
- 📄 Automatic Research Paper Retrieval
- 📝 Research Paper Summarization
- 🤖 AI-powered Explanation using SmolLM2
- 🧠 Automatic Concept Extraction using spaCy
- 📊 Interactive Concept Graph using NetworkX
- 💬 Multi-turn Conversation Memory
- 🌐 Streamlit Web Interface

---

## 📁 Project Structure

```
Task-04-Research-Paper-Expert/
│
├── app.py
├── parser/
├── retrieval/
├── summarizer/
├── llm/
├── memory/
├── visualization/
├── utils/
├── database/
├── data/
├── README.md
└── requirements.txt
```

---

## ⚙️ Technologies Used

- Python
- Streamlit
- Sentence Transformers
- Hugging Face Transformers
- SmolLM2
- PyTorch
- spaCy
- NetworkX
- Matplotlib
- Pandas
- NumPy

---

## 🚀 Workflow

```
User Question
      │
      ▼
Semantic Retrieval
      │
      ▼
Relevant Research Paper
      │
      ▼
Paper Summarization
      │
      ▼
SmolLM2 Explanation
      │
      ▼
Concept Extraction
      │
      ▼
Concept Visualization
      │
      ▼
Conversation Memory
```

---

## 💻 Installation

### Clone the Repository

```bash
git clone <repository-url>
```

### Move into the Project

```bash
cd Task-04-Research-Paper-Expert
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Virtual Environment

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Download spaCy Language Model

```bash
python -m spacy download en_core_web_sm
```

### Run the Application

```bash
streamlit run app.py
```

---

## 📸 Application Features

The application provides:

- Semantic paper retrieval
- Paper metadata
- Abstract viewer
- AI-generated summary
- AI-generated explanation
- Dynamic concept graph
- Conversation history

---

## 📌 Example Query

**Question**

```
What is Machine Learning?
```

**Output**

- Most Relevant Research Paper
- Summary of the Paper
- AI-generated Explanation
- Concept Graph
- Conversation History

---

## 🔮 Future Improvements

- LLM-based Concept Extraction
- Better Concept Graph Relationships
- Multi-paper Comparison
- PDF Export
- Research Paper Recommendation System
- Citation Generation

---

## 👨‍💻 Author

**Ashmit Kumar**

Data Science Internship Project