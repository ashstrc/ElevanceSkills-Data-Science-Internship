from pathlib import Path


class DocumentLoader:

    def __init__(self, folder="new_documents"):
        self.folder = Path(folder)

    def load_documents(self):

        documents = []

        for file in self.folder.glob("*.txt"):

            with open(file, "r", encoding="utf-8") as f:

                text = f.read()

            documents.append({
                "filename": file.name,
                "content": text
            })

        return documents


if __name__ == "__main__":

    loader = DocumentLoader()

    docs = loader.load_documents()

    print(f"Found {len(docs)} document(s)\n")

    for doc in docs:

        print("=" * 50)
        print(doc["filename"])
        print("-" * 50)
        print(doc["content"])