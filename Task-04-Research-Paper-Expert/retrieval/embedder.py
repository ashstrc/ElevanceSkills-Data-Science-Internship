import os
import pickle

import pandas as pd
from sentence_transformers import SentenceTransformer


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


def generate_embeddings():

    print("Loading AI Research Papers...")

    dataframe = pd.read_csv(CSV_PATH)

    print(f"Total Papers : {len(dataframe)}")

    print("Loading Sentence Transformer...")

    model = SentenceTransformer(
        "all-MiniLM-L6-v2"
    )

    embeddings = []

    print("\nGenerating Embeddings...\n")

    total = len(dataframe)

    for index, row in dataframe.iterrows():

        text = f"{row['title']} {row['abstract']}"

        embedding = model.encode(text)

        embeddings.append(embedding)

        if (index + 1) % 500 == 0:

            print(
                f"{index + 1} / {total} papers completed..."
            )

    print("\nSaving Embeddings...")

    with open(EMBEDDING_PATH, "wb") as file:

        pickle.dump(
            embeddings,
            file
        )

    print("\nEmbedding Generation Complete!")
    print(f"Embeddings Saved : {len(embeddings)}")


if __name__ == "__main__":

    generate_embeddings()