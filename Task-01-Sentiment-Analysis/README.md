# 🤖 AI Sentiment Analysis Assistant

A real-time sentiment analysis chatbot developed using **Python**, **Streamlit**, **Hugging Face Transformers**, and **PyTorch**.

The application analyzes user messages, classifies them as **Positive**, **Negative**, or **Neutral**, displays the model's confidence score, and generates an appropriate emotion-aware response.

---

## 📌 Internship Information

**Organization:** ElevanceSkills

**Internship Track:** Data Science Internship

**Task:** Task 1 – Sentiment Analysis Integration

---

## ✨ Features

- Detects **Positive**, **Negative**, and **Neutral** sentiment.
- Uses a pretrained Transformer model from Hugging Face.
- Displays prediction confidence.
- Generates emotion-aware chatbot responses.
- Interactive Streamlit web interface.
- Responsive and clean user interface.
- Randomized responses for a better user experience.

---

## 🛠️ Technologies Used

- Python 3.11+
- Streamlit
- Hugging Face Transformers
- PyTorch

---

## 🤖 Model Used

**Model Name**

```
cardiffnlp/twitter-roberta-base-sentiment-latest
```

The model is a pretrained RoBERTa-based sentiment classifier capable of classifying text into:

- Positive
- Neutral
- Negative

---

## 📂 Project Structure

```
sentiment-chatbot/
│
├── app.py
├── chatbot.py
├── sentiment.py
├── responses.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone <repository-url>
```

Move into the project directory

```bash
cd sentiment-chatbot
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will open in your browser at:

```
http://localhost:8501
```

---

## 🧠 How It Works

1. The user enters a message.
2. The sentiment analysis model processes the text.
3. The model predicts the sentiment:
   - Positive
   - Neutral
   - Negative
4. The confidence score is displayed.
5. The chatbot generates an appropriate response based on the detected sentiment.

---

## 📷 Example Outputs

### Example 1

**Input**

```
I absolutely love this chatbot.
```

**Output**

```
Sentiment: Positive

Confidence: 98.5%

Response:
😊 That's wonderful to hear! How else can I help you today?
```

---

### Example 2

**Input**

```
I'm disappointed with the service.
```

**Output**

```
Sentiment: Negative

Confidence: 91.8%

Response:
💙 I understand how you feel. Let's solve it together.
```

---

### Example 3

**Input**

```
Can you tell me your office timings?
```

**Output**

```
Sentiment: Neutral

Confidence: 94.2%

Response:
🙂 Please tell me more.
```

---

## 🎯 Internship Task Objective

The objective of this project is to integrate sentiment analysis into a chatbot so that it can:

- Detect customer emotions.
- Respond appropriately to different sentiments.
- Improve user interaction through emotion-aware responses.

---

## 👨‍💻 Developed By

**Ashmit Kumar**

Data Science Intern

ElevanceSkills