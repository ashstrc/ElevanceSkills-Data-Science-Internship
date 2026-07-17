# 🌍 Task-06: Multilingual AI Assistant

> **ElevanceSkills Data Science Internship - Task 06**

A modular **Multilingual Multi-Modal AI Assistant** capable of understanding **text, images, and multilingual conversations** while preserving conversation context, user intent, and continuity across language switches.

The project extends the architecture developed in **Task-05** by introducing a dedicated multilingual processing pipeline that automatically detects languages, translates when required, preserves canonical conversation memory, and generates responses in the user's preferred language.

---

# 📌 Assignment Objective

Develop a multilingual AI assistant capable of:

- Understanding multilingual text conversations
- Automatically detecting user language
- Translating user queries into a canonical language
- Maintaining conversation context across language switches
- Supporting multilingual image-based reasoning
- Generating localized responses
- Demonstrating cross-lingual reasoning using open-source models

---

# ✨ Features

## 🌐 Multilingual Conversations

Supports automatic language detection and translation.

Current supported languages:

- 🇺🇸 English
- 🇮🇳 Hindi
- 🇪🇸 Spanish
- 🇫🇷 French
- 🇩🇪 German
- 🇯🇵 Japanese

---

## 💬 Text Chat

- General multilingual conversations
- Automatic language detection
- Automatic translation
- Context preservation
- Response localization

Powered by

- SmolLM2
- XLM-RoBERTa
- Meta NLLB-200

---

## 🖼 Image Analysis

- Upload any image
- Automatic visual understanding
- Structured visual evidence extraction
- Language independent

Extracted information includes

- Objects
- Animals
- People
- Activities
- Environment
- Colors
- Visible Text
- Important Details

---

## 🧠 Image + Question

Supports multilingual visual reasoning.

Example

Hindi

```
यह जानवर क्या कर रहा है?
```

Spanish

```
¿Qué animal aparece en la imagen?
```

French

```
Décrivez cette image.
```

English

```
What is happening in this image?
```

All produce the same reasoning pipeline.

---

# 🚀 Key Highlights

- ✅ Open-source models only
- ✅ Modular architecture
- ✅ Automatic language detection
- ✅ Cross-lingual reasoning
- ✅ Context-aware conversations
- ✅ Conversation continuity
- ✅ Translation pipeline
- ✅ Evidence-first reasoning
- ✅ Response validation
- ✅ Streamlit interface
- ✅ CPU compatible

# 🏗 System Architecture

```text
                          User
                            │
                            ▼
                  Language Processor
                            │
          ┌─────────────────┴─────────────────┐
          │                                   │
          ▼                                   ▼
   Language Detection                 Translation Layer
     (XLM-RoBERTa)                   (Meta NLLB-200)
          │                                   │
          └─────────────────┬─────────────────┘
                            ▼
                    Mode Selector
                            │
      ┌─────────────────────┼─────────────────────┐
      ▼                     ▼                     ▼
  Text Chat          Image Analysis      Image + Question
      │                     │                     │
      ▼                     ▼                     ▼
   SmolLM2            Qwen2.5-VL           Qwen2.5-VL
                                                │
                                                ▼
                                  Visual Evidence Extraction
                                                │
                                                ▼
                                         Scene Builder
                                                │
                                                ▼
                                        Question Router
                             ┌──────────────────┴─────────────────┐
                             ▼                                    ▼
                    Evidence Answerer                 Reasoning Engine
                             │                                    │
                             └──────────────────┬─────────────────┘
                                                ▼
                                       Response Validator
                                                ▼
                                   Conversation Memory
                                                ▼
                                     Response Localization
                                                ▼
                                        Final Response
```

---

# 🔄 System Workflow

## Step 1 — Language Processing

```text
User
   │
   ▼
Language Detection
   │
   ▼
Translation (if required)
   │
   ▼
Canonical English Query
```

---

## Step 2 — Assistant Processing

```text
Canonical Query
        │
        ▼
Mode Selection
        │
        ▼
Text Chat / Image Analysis / Image Question
        │
        ▼
Reasoning Pipeline
```

---

## Step 3 — Response Localization

```text
Assistant Response
        │
        ▼
Translation Layer
        │
        ▼
Localized Response
        │
        ▼
User
```

---

# 📂 Project Structure

```text
Task-06-Multilingual-AI-Assistant/

│
├── app.py
├── main.py
├── requirements.txt
├── README.md
│
├── answering/
├── assistant/
├── data/
├── language/
│   ├── detector.py
│   ├── translator.py
│   ├── processor.py
│   └── schemas.py
│
├── llm/
├── memory/
├── models/
├── reasoning/
├── routing/
├── validation/
├── vision/
```

---

# 🧠 Models Used

| Component | Model |
|-----------|-------|
| Vision Understanding | Qwen2.5-VL-3B-Instruct |
| Reasoning | SmolLM2-1.7B-Instruct |
| Language Detection | papluca/xlm-roberta-base-language-detection |
| Translation | facebook/nllb-200-distilled-600M |
| Framework | Hugging Face Transformers |
| Interface | Streamlit |

---

# 💡 Design Principles

The assistant follows a modular pipeline where every component has a dedicated responsibility.

Major design decisions include:

- Separation of language understanding from reasoning
- Language-independent conversation memory
- Automatic language detection
- Automatic translation pipeline
- Evidence-first reasoning
- Visual reasoning over structured scene representation
- Independent response validation
- Conversation continuity across language switches
- Lazy loading of AI models
- Fully open-source implementation

# ⚙️ Installation

## Clone the Repository

```bash
git clone https://github.com/ashstrc/ElevanceSkills-Data-Science-Internship.git

cd Task-06-Multilingual-AI-Assistant
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

## Streamlit Application

```bash
streamlit run app.py
```

---

## Command Line Interface

```bash
python main.py
```

---

# 🌍 Supported Languages

| Language | Code |
|----------|------|
| English | en |
| Hindi | hi |
| Spanish | es |
| French | fr |
| German | de |
| Japanese | ja |

The assistant automatically detects the user's language and generates responses in the same language whenever translation is required.

---

# 💬 Example Conversation

## English

```
User:
What is shown in this image?

Assistant:
The image shows a tiger resting on the grass.
```

---

## Hindi

```
User:
यह चित्र क्या दिखाता है?

Assistant:
यह चित्र घास पर आराम करते हुए एक बाघ को दिखाता है।
```

---

## Spanish

```
User:
¿Qué muestra esta imagen?

Assistant:
La imagen muestra un tigre descansando sobre el césped.
```

---

## French

```
User:
Que montre cette image ?

Assistant:
L'image montre un tigre se reposant sur l'herbe.
```

---

# 📊 Technologies Used

- Python
- Streamlit
- PyTorch
- Hugging Face Transformers
- SmolLM2
- Qwen2.5-VL
- XLM-RoBERTa
- Meta NLLB-200
- Pillow

---

# 📈 Performance Characteristics

- Lazy loading of language and vision models
- Automatic language detection before reasoning
- Canonical English processing pipeline
- Localized multilingual responses
- CPU compatible
- GPU acceleration supported through CUDA
- Modular architecture for easy extension


# 💻 Hardware Requirements

## Minimum

- Python 3.11+
- 16 GB RAM
- CPU Supported

The assistant is fully compatible with CPU-only systems. Running on a CPU may result in slower inference for larger language and vision models.

---

## Recommended

- NVIDIA GPU with CUDA support
- 16 GB+ VRAM
- 16 GB+ System RAM

or

- Google Colab (Tesla T4 / L4)
- Kaggle Notebook with GPU

---

# 🔮 Future Improvements

The modular architecture allows several future enhancements:

- 🎤 Voice-based multilingual conversations
- 📄 OCR for multilingual document understanding
- 🎥 Video understanding and reasoning
- 🖼 Multi-image comparison
- 📚 Retrieval-Augmented Generation (RAG)
- 🗂 Vector database integration
- 🌐 REST API deployment
- 🐳 Docker support
- ☁ Hugging Face Spaces deployment
- 📱 Mobile application integration
- 🧠 Persistent long-term memory
- 🌎 Additional language support
- ⚡ Streaming responses

---

# 📷 Suggested Demonstration

Recommended screenshots for the repository:

### 💬 Text Chat

- English conversation
- Hindi conversation
- Spanish conversation

---

### 🖼 Image Analysis

- Uploaded image
- Structured visual evidence

---

### 🧠 Image + Question

- Visual evidence extraction
- Multilingual question
- Assistant response
- Validation report

---

### 🌍 Language Detection

Display examples of:

- English
- Hindi
- Spanish
- French

showing automatic language detection and localized responses.

---

# 👨‍💻 Author

**Ashmit Kumar**

B.Tech Computer Science Engineering

ElevanceSkills Data Science Internship

---

# 🙏 Acknowledgements

Special thanks to the following open-source communities and organizations:

- ElevanceSkills
- Hugging Face
- Meta AI
- Qwen Team
- SmolLM Team
- Streamlit
- PyTorch

for providing the tools, frameworks, and models that made this project possible.

---

# 📄 License

This project is intended for educational and internship purposes.

All AI models used in this project are distributed under their respective open-source licenses.

---

# ⭐ Project Status

## ✅ Completed

Task-06 successfully extends the Task-05 Multimodal AI Assistant by introducing multilingual capabilities through:

- Automatic language detection using XLM-RoBERTa
- Multilingual translation using Meta NLLB-200
- Context-aware multilingual conversations
- Cross-lingual reasoning
- Language-independent conversation memory
- Multilingual multimodal reasoning
- Evidence-based response generation
- Response validation
- Modular and extensible architecture using open-source AI models

The project demonstrates multilingual conversational AI while preserving context, intent, and conversational continuity across language switches, fulfilling the objectives of the ElevanceSkills Data Science Internship Task-06.