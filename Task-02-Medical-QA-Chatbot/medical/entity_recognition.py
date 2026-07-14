import os
import pandas as pd


class MedicalEntityRecognizer:

    def __init__(self):

        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        csv_path = os.path.join(base_dir, "database", "medical_qa.csv")

        df = pd.read_csv(csv_path)

        self.diseases = sorted(
            df["Focus"].dropna().unique(),
            key=len,
            reverse=True
        )

        self.intent_keywords = {

            "Symptoms": [
                "symptom",
                "symptoms",
                "sign",
                "signs"
            ],

            "Treatment": [
                "treat",
                "treatment",
                "therapy",
                "medicine",
                "medication",
                "drug",
                "cure"
            ],

            "Diagnosis": [
                "diagnose",
                "diagnosis",
                "test",
                "screening"
            ],

            "Prevention": [
                "prevent",
                "prevention",
                "avoid"
            ],

            "Causes": [
                "cause",
                "causes",
                "reason"
            ],

            "Risk": [
                "risk",
                "risk factor"
            ],

            "Outlook": [
                "prognosis",
                "outlook"
            ]

        }

    def recognize(self, query):

        query_lower = query.lower()

        disease = None

        for item in self.diseases:

            if item.lower() in query_lower:
                disease = item
                break

        intent = "General"

        for name, keywords in self.intent_keywords.items():

            for word in keywords:

                if word in query_lower:
                    intent = name
                    break

        return {
            "Disease": disease,
            "Intent": intent
        }


if __name__ == "__main__":

    recognizer = MedicalEntityRecognizer()

    while True:

        query = input("\nEnter Question: ")

        if query.lower() == "exit":
            break

        result = recognizer.recognize(query)

        print("\nDetected Entities")
        print("-------------------------")
        print("Disease :", result["Disease"])
        print("Intent  :", result["Intent"])