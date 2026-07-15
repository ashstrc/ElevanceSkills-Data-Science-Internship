import os
import pickle

import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer, util


base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CSV_PATH = os.path.join(
    base_dir,
    "database",
    "papers.csv"
)

EMBEDDING_PATH = os.path.join(
    base_dir,
    "database",
    "embeddings.pkl"
)

MIN_SIMILARITY = 0.55


class ResearchRetriever:

    def __init__(self):

        print("Loading AI Research Papers...")

        self.dataframe = pd.read_csv(CSV_PATH)

        print("Loading Embeddings...")

        with open(EMBEDDING_PATH, "rb") as file:

            self.embeddings = np.array(
                pickle.load(file)
            )

        print("Loading Sentence Transformer...")

        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

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

        score = float(score)

        if score < MIN_SIMILARITY:

            return None

        row = self.dataframe.iloc[int(index)]

        return {

            "title": row["title"],

            "authors": row["authors"],

            "categories": row["categories"],

            "abstract": row["abstract"],

            "score": score

        }


if __name__ == "__main__":

    retriever = ResearchRetriever()

    while True:

        query = input("\nAsk an AI Research Question: ")

        if query.lower() == "exit":
            break

        paper = retriever.search(query)

        if paper is None:

            print("\nNo relevant AI research paper found.")

            continue

        print("\n" + "=" * 80)

        print(f"Title      : {paper['title']}")

        print(f"Authors    : {paper['authors']}")

        print(f"Categories : {paper['categories']}")

        print(f"Similarity : {paper['score'] * 100:.2f}%")

        print("\nAbstract:\n")

        print(paper["abstract"])

        print("\n" + "=" * 80)