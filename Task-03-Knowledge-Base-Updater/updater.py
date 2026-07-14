import os
import shutil

from sentence_transformers import SentenceTransformer

from loader import DocumentLoader
from vector_store import VectorStore


MIN_CONTENT_LENGTH = 50


class KnowledgeUpdater:

    def __init__(self):

        self.loader = DocumentLoader()

        self.vector_store = VectorStore()

        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

    def update(self):

        docs = self.loader.load_documents()

        if len(docs) == 0:
            return

        dataframe = self.vector_store.load_database()

        embeddings = self.vector_store.load_embeddings()

        new_document_added = False

        for doc in docs:

            # Skip if already exists in the knowledge base
            if doc["filename"] in dataframe["filename"].values:
                continue

            content = doc["content"].strip()

            # Skip empty or incomplete documents
            if len(content) < MIN_CONTENT_LENGTH:
                print(f"Skipping '{doc['filename']}' (document is empty or incomplete).")
                continue

            embedding = self.model.encode(content)

            embeddings.append(embedding)

            dataframe.loc[len(dataframe)] = [

                doc["filename"],
                content

            ]

            source = f"new_documents/{doc['filename']}"
            destination = f"processed/{doc['filename']}"

            if os.path.exists(source):
                shutil.move(source, destination)

            print(f"{doc['filename']} added.")

            new_document_added = True

        if new_document_added:

            self.vector_store.save_database(dataframe)

            self.vector_store.save_embeddings(embeddings)

            print("\nKnowledge Base Updated!")


if __name__ == "__main__":

    updater = KnowledgeUpdater()

    updater.update()