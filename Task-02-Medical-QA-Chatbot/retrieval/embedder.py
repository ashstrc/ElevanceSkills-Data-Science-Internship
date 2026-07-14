import os
import pickle
import pandas as pd
from sentence_transformers import SentenceTransformer

# -----------------------------
# Paths
# -----------------------------

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CSV_PATH = os.path.join(BASE_DIR, "database", "medical_qa.csv")
EMBEDDING_PATH = os.path.join(BASE_DIR, "database", "embeddings.pkl")

# -----------------------------
# Load Dataset
# -----------------------------

print("Loading dataset...")

df = pd.read_csv(CSV_PATH)

questions = df["Question"].tolist()

print(f"Questions Loaded : {len(questions)}")

# -----------------------------
# Load Model
# -----------------------------

print("Loading Sentence Transformer...")

model = SentenceTransformer("all-MiniLM-L6-v2")

print("Generating Embeddings...")

embeddings = model.encode(
    questions,
    show_progress_bar=True,
    convert_to_numpy=True
)

# -----------------------------
# Save Embeddings
# -----------------------------

with open(EMBEDDING_PATH, "wb") as f:
    pickle.dump(embeddings, f)

print("\nEmbeddings saved successfully!")
print(EMBEDDING_PATH)