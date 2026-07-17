from transformers import pipeline


class LanguageDetector:
    def __init__(self):
        self.detector = pipeline(
            "text-classification",
            model="papluca/xlm-roberta-base-language-detection",
            top_k=2
        )

    def detect(self, text: str):
        predictions = self.detector(text)[0]

        primary = predictions[0]

        return {
            "primary_language": primary["label"],
            "confidence": round(primary["score"], 4)
        }