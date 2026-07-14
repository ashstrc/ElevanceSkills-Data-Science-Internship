import random

responses = {

    "positive": [
        "😊 That's wonderful to hear! How else can I help you today?",
        "😄 I'm glad you're having a great experience.",
        "🎉 Awesome! Let me know if you need anything else."
    ],

    "negative": [
        "😔 I'm sorry you're experiencing this. Let me help.",
        "💙 I understand how you feel. Let's solve it together.",
        "🙏 I'm here for you. Tell me more about the issue."
    ],

    "neutral": [
        "🙂 Sure! How can I assist you?",
        "👍 I'm ready to help.",
        "😊 Please tell me more."
    ]

}


def get_response(sentiment):
    return random.choice(
        responses.get(sentiment, responses["neutral"])
    )