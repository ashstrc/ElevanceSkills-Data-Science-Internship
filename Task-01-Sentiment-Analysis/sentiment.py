from transformers import pipeline

# Load model only once
classifier = pipeline(
    "sentiment-analysis",
    model="cardiffnlp/twitter-roberta-base-sentiment-latest"
)


def analyze_sentiment(text):

    result = classifier(text)[0]

    print(result)

    return {
        "label": result["label"].lower(),
        "score": round(result["score"], 3)
    }

    # result = classifier(text)[0]

    # return {
    #     "label": result["label"].lower(),
    #     "score": round(result["score"], 3)
    # }