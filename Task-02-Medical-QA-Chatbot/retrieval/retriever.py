import os
import pickle
import pandas as pd
from sentence_transformers import SentenceTransformer, util


class MedicalRetriever:

    def __init__(self):

        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        csv_path = os.path.join(base_dir, "database", "medical_qa.csv")
        embedding_path = os.path.join(base_dir, "database", "embeddings.pkl")

        print("Loading Medical Dataset...")
        self.df = pd.read_csv(csv_path)

        print("Loading Embeddings...")
        with open(embedding_path, "rb") as f:
            self.embeddings = pickle.load(f)

        print("Loading Sentence Transformer...")
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

        print("Retriever Ready!")

    def search(self, query):

        query_embedding = self.model.encode(
            query,
            convert_to_tensor=True
    )

        cosine_scores = util.cos_sim(
        query_embedding,
        self.embeddings
    )[0]

        score, index = cosine_scores.max(dim=0)

    # Convert tensor to float
        score = float(score)

    # Reject unrelated questions
        if score < 0.50:
            return {
            "found": False,
            "score": score
        }

        row = self.df.iloc[int(index)]

        return {
            "found": True,
            "focus": row["Focus"],
            "question": row["Question"],
            "answer": row["Answer"],
            "question_type": row["QuestionType"],
            "source": row["Source"],
            "score": score
    }


if __name__ == "__main__":

    retriever = MedicalRetriever()

    while True:

        query = input("\nAsk a medical question: ")

        if query.lower() == "exit":
            break

        result = retriever.search(query)

        if not result["found"]:
            print("\nNo relevant medical information found.")
            print(f"Similarity Score : {result['score'] * 100:.2f}%")
            print("Please ask a medical question.")
            continue
        

        print("\n" + "=" * 60)
        print("Medical Topic :", result["focus"])
        print("Matched Question :", result["question"])
        print(f"Similarity Score : {result['score'] * 100:.2f}%")

        print("\nMedical Answer:\n")
        print(result["answer"])

        print("=" * 60)