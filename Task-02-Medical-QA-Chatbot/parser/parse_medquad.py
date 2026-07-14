import os
import xml.etree.ElementTree as ET
import pandas as pd

# -----------------------------
# Project Paths
# -----------------------------

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATASET_PATH = os.path.join(BASE_DIR, "data", "medquad")
OUTPUT_DIR = os.path.join(BASE_DIR, "database")
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "medical_qa.csv")

# -----------------------------
# Statistics
# -----------------------------

records = []

total_files = 0
parsed_files = 0
failed_files = 0

# -----------------------------
# Parse Dataset
# -----------------------------

for dataset_folder in os.listdir(DATASET_PATH):

    dataset_path = os.path.join(DATASET_PATH, dataset_folder)

    if not os.path.isdir(dataset_path):
        continue

    source = dataset_folder.replace("_QA", "").replace("_XML", "")

    for root_dir, _, files in os.walk(dataset_path):

        for file in files:

            if not file.endswith(".xml"):
                continue

            total_files += 1

            file_path = os.path.join(root_dir, file)

            try:

                tree = ET.parse(file_path)
                root = tree.getroot()

                focus = root.findtext("Focus", default="Unknown")

                qa_pairs = root.find("QAPairs")

                if qa_pairs is None:
                    continue

                for pair in qa_pairs.findall("QAPair"):

                    question_node = pair.find("Question")
                    answer_node = pair.find("Answer")

                    question = (
                        question_node.text.strip()
                        if question_node is not None and question_node.text
                        else ""
                    )

                    answer = (
                        answer_node.text.strip()
                        if answer_node is not None and answer_node.text
                        else ""
                    )

                    qtype = (
                        question_node.attrib.get("qtype", "Unknown")
                        if question_node is not None
                        else "Unknown"
                    )

                    records.append(
                        {
                            "Focus": focus,
                            "Question": question,
                            "Answer": answer,
                            "QuestionType": qtype,
                            "Source": source,
                            "Dataset": dataset_folder,
                            "FileName": file,
                        }
                    )

                parsed_files += 1

            except Exception as e:

                failed_files += 1
                print(f"[ERROR] {file}")
                print(e)

# -----------------------------
# Create DataFrame
# -----------------------------

df = pd.DataFrame(records)

# Remove duplicates

df.drop_duplicates(inplace=True)

# Remove empty rows

df = df[df["Question"] != ""]
df = df[df["Answer"] != ""]

# -----------------------------
# Save CSV
# -----------------------------

os.makedirs(OUTPUT_DIR, exist_ok=True)

df.to_csv(OUTPUT_FILE, index=False)

# -----------------------------
# Report
# -----------------------------

print("\n" + "=" * 60)

print("MedQuAD Parsing Complete")

print("=" * 60)

print(f"Total XML Files      : {total_files}")
print(f"Successfully Parsed  : {parsed_files}")
print(f"Failed Files         : {failed_files}")
print(f"Total QA Pairs       : {len(df)}")
print(f"Unique Topics        : {df['Focus'].nunique()}")
print(f"Sources              : {df['Source'].nunique()}")

print("\nCSV Saved To:")
print(OUTPUT_FILE)

print("=" * 60)