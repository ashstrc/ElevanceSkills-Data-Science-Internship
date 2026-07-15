import json
import csv
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

INPUT_FILE = os.path.join(
    base_dir,
    "data",
    "arxiv-metadata-oai-snapshot.json"
)

OUTPUT_FILE = os.path.join(
    base_dir,
    "database",
    "papers.csv"
)

AI_CATEGORIES = [

    "cs.AI",

    "cs.LG",

    "cs.CL",

    "cs.CV"
]
MAX_PAPERS = 15000


def parse_dataset():

    print("Reading arXiv Dataset...")

    papers = 0

    os.makedirs(
        os.path.join(base_dir, "database"),
        exist_ok=True
    )

    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as csvfile:

        writer = csv.writer(csvfile)

        writer.writerow([
            "title",
            "authors",
            "categories",
            "abstract"
        ])

        with open(INPUT_FILE, "r", encoding="utf-8") as file:

            for line in file:

                paper = json.loads(line)

                categories = paper.get("categories", "")

                if not any(category in categories for category in AI_CATEGORIES):
                    continue

                writer.writerow([
                    paper.get("title", "").strip(),
                    paper.get("authors", "").strip(),
                    categories,
                    paper.get("abstract", "").replace("\n", " ").strip()
                ])

                papers += 1

                if papers % 1000 == 0:
                    print(f"{papers} AI papers extracted...")

                if papers >= MAX_PAPERS:
                    break

    print("\nParsing Complete!")
    print(f"Total AI Papers : {papers}")


if __name__ == "__main__":

    parse_dataset()