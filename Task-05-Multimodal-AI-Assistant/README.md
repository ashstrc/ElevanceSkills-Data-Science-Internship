# 🤖 Task-05: Multimodal AI Assistant

> **ElevanceSkills Data Science Internship - Task 05**

A modular **Multi-Modal AI Assistant** capable of understanding and reasoning over **both text and image inputs**. The assistant extracts structured visual evidence from images, intelligently routes user queries, performs evidence-based reasoning using an open-source LLM, validates generated responses, and maintains conversational context across multiple interactions.

Unlike traditional single-model implementations, this project separates **vision**, **reasoning**, **routing**, **validation**, and **memory** into independent modules, making the assistant more explainable, modular, and extensible.

---

# 📌 Assignment Objective

Develop a multi-modal AI assistant capable of:

- Understanding text and image inputs
- Extracting structured information from images
- Performing contextual reasoning
- Maintaining conversational memory
- Generating evidence-based responses
- Validating generated answers
- Demonstrating intelligent decision making instead of relying on direct model inference

---

# ✨ Features

### 💬 Text Chat

- Text-only conversational AI
- Powered by SmolLM2
- Independent from the vision model
- Lazy loading for faster startup

---

### 🖼 Image Analysis

- Upload any image
- Automatic visual understanding
- Structured evidence extraction
- No reasoning performed
- Pure computer vision pipeline

Extracted information includes:

- Objects
- Animals
- People
- Environment
- Activities
- Colors
- Visible Text
- Important Details

---

### 🧠 Image + Question

Interactive multimodal reasoning pipeline.

The assistant can:

- Understand uploaded images
- Answer factual questions
- Perform visual reasoning
- Explain observations
- Handle follow-up questions
- Maintain conversation context
- Validate generated responses

---

# 🚀 Key Highlights

- ✅ Open-source models only
- ✅ Modular architecture
- ✅ Context-aware reasoning
- ✅ Evidence-first pipeline
- ✅ Intelligent question routing
- ✅ Response validation
- ✅ Conversation memory
- ✅ Lazy model loading
- ✅ Streamlit Web Interface
- ✅ Google Colab compatible

---

# 🏗 System Architecture

```text
                    User
                      │
                      ▼
              Mode Selector
                      │
      ┌───────────────┼────────────────┐
      ▼               ▼                ▼
  Text Chat     Image Analysis   Image + Question
      │               │                │
      ▼               ▼                ▼
   SmolLM2      Qwen2.5-VL      Qwen2.5-VL
                                        │
                                        ▼
                              Visual Evidence Extraction
                                        │
                                        ▼
                                  Scene Builder
                                        │
                                        ▼
                                Question Router
                          ┌─────────────┴──────────────┐
                          ▼                            ▼
                 Evidence Answerer          Reasoning Engine
                          │                            │
                          └─────────────┬──────────────┘
                                        ▼
                               Response Validator
                                        ▼
                             Conversation Memory
                                        ▼
                                  Final Response
```

---

# 🔄 System Workflow

### Mode 1 — Text Chat

```text
User
   │
   ▼
SmolLM2
   │
   ▼
Answer
```

---

### Mode 2 — Image Analysis

```text
Image
   │
   ▼
Qwen2.5-VL
   │
   ▼
Structured Visual Evidence
```

---

### Mode 3 — Image + Question

```text
Image
   │
   ▼
Qwen2.5-VL
   │
   ▼
Visual Evidence
   │
   ▼
Scene Builder
   │
   ▼
Question Router
   │
 ┌─┴─────────────────────┐
 ▼                       ▼
Evidence            Visual
Answerer           Reasoning
 │                       │
 └──────────────┬────────┘
                ▼
        Response Validator
                ▼
     Conversation Memory
                ▼
         Final Response
```

---

# 📂 Project Structure

```
Task-05-Multimodal-AI-Assistant/
│
├── app.py
├── main.py
├── requirements.txt
├── README.md
│
├── assistant/
│
├── answering/
│
├── data/
│
├── llm/
│
├── memory/
│
├── reasoning/
│
├── routing/
│
├── validation/
│
└── vision/
```

---

# 🧠 Models Used

| Component | Model |
|-----------|-------|
| Vision Model | Qwen2.5-VL-3B-Instruct |
| Language Model | SmolLM2 |
| Framework | Hugging Face Transformers |
| UI | Streamlit |

---

# ⚙️ Installation

## Clone the Repository

```bash
git clone https://github.com/ashstrc/Task-05-Multimodal-AI-Assistant.git

cd Task-05-Multimodal-AI-Assistant
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv .venv

.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv

source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶ Running the Project

## Streamlit Web Interface

```bash
streamlit run app.py
```

---

## Command Line Interface

```bash
python main.py
```

---

# 🖥 Streamlit Modes

## 💬 Mode 1 — Text Chat

Features

- General AI conversation
- Knowledge-based questions
- Loads only SmolLM2
- No vision model required

Example:

```
What is a Transformer?
```

---

## 🖼 Mode 2 — Image Analysis

Features

- Upload an image
- Extract visual evidence
- Structured output
- No reasoning performed

Example Output

```
Animals:
Tiger

People:
None

Environment:
Grass

Activities:
Resting

Colors:
Orange, Black, White

Visible Text:
None
```

---

## 🧠 Mode 3 — Image + Question

Workflow

```
Upload Image

↓

Extract Visual Evidence

↓

Ask Question

↓

Question Routing

↓

Evidence Answer / Reasoning

↓

Response Validation

↓

Final Response
```

Example Questions

```
What animal is this?

What is it doing?

Why might it be resting?

Is the animal flying?

Describe the environment.

Compare this with the previous image.
```

---

# 📸 Example Outputs

## Text Chat

```
User:
What is CNN?

Assistant:
CNN (Convolutional Neural Network) is a deep learning
architecture commonly used for image recognition,
object detection, medical imaging and computer vision.
```

---

## Image Analysis

```
Animals:
Tiger

People:
None

Environment:
Grass

Activities:
Resting

Important Details:
Tiger lying on the ground surrounded by grass.
```

---

## Image + Question

```
Question:
What animal is this?

Answer:
The image shows a tiger resting on the ground.

Validation

Status:
SUPPORTED

Confidence:
HIGH
```

---

# 📊 Technologies Used

- Python
- Streamlit
- PyTorch
- Hugging Face Transformers
- Qwen2.5-VL-3B-Instruct
- SmolLM2
- Pillow

---

# 💡 Design Principles

The assistant follows a modular architecture instead of relying on a single model.

Major design decisions include:

- Separation of vision and reasoning
- Evidence-first response generation
- Intelligent question routing
- Independent response validation
- Conversation memory
- Lazy model loading for efficiency
- Support for both text-only and multimodal interactions

This architecture improves explainability, modularity, maintainability, and scalability.

---

# 💻 Hardware Requirements

## Minimum

- Python 3.11+
- 16 GB RAM
- CPU supported

Inference will be slower when using CPU-only systems.

---

## Recommended

- NVIDIA GPU (CUDA)
- 16 GB+ VRAM
- 16 GB+ RAM

or

Google Colab (Tesla T4 / L4 GPU)

---

# 🚀 Future Improvements

- Voice interaction
- OCR-based document understanding
- Video understanding
- Multi-image comparison
- Retrieval-Augmented Generation (RAG)
- Vector database integration
- Cloud deployment
- Docker support
- REST API
- Hugging Face Spaces deployment

---

# 📷 Screenshots

Add screenshots here after running the application.

Suggested screenshots:

- Text Chat
- Image Analysis
- Image + Question
- Validation Report

---

# 👨‍💻 Author

**Ashmit Kumar**

B.Tech Computer Science Engineering

ElevanceSkills Data Science Internship

---

# 🙏 Acknowledgements

Special thanks to:

- ElevanceSkills
- Hugging Face
- Qwen Team
- SmolLM2 Team
- Streamlit
- PyTorch

for providing the open-source tools and models that made this project possible.

---

# ⭐ Project Status

✅ Completed

The project successfully demonstrates a modular multimodal AI assistant capable of understanding both text and image inputs, extracting structured visual evidence, performing contextual reasoning, maintaining conversational memory, validating responses, and generating evidence-based answers using open-source AI models.