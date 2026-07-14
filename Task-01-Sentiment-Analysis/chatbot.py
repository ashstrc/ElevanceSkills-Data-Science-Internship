from sentiment import analyze_sentiment
from responses import get_response


def chatbot(message):

    sentiment = analyze_sentiment(message)

    reply = get_response(sentiment["label"])

    return {
        "message": message,
        "sentiment": sentiment["label"].capitalize(),
        "confidence": sentiment["score"],
        "reply": reply
    }