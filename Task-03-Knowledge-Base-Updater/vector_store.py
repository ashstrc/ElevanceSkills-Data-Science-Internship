import os
import pickle
import pandas as pd


class VectorStore:

    def __init__(self):

        self.database = "database"

        self.csv_path = os.path.join(
            self.database,
            "knowledge.csv"
        )

        self.embedding_path = os.path.join(
            self.database,
            "embeddings.pkl"
        )

    def load_database(self):

        if os.path.exists(self.csv_path):

            return pd.read_csv(self.csv_path)

        return pd.DataFrame(
            columns=["filename", "content"]
        )

    def save_database(self, dataframe):

        dataframe.to_csv(
            self.csv_path,
            index=False
        )

    def load_embeddings(self):

        if os.path.exists(self.embedding_path):

            with open(self.embedding_path, "rb") as f:

                return pickle.load(f)

        return []

    def save_embeddings(self, embeddings):

        with open(self.embedding_path, "wb") as f:

            pickle.dump(embeddings, f)