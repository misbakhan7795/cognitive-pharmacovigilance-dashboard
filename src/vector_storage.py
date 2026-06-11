from sentence_transformers import SentenceTransformer
import pandas as pd
import faiss
import pickle

print("Loading FAERS records...")

df = pd.read_csv(
    "data/processed/faers_records.csv"
)

print("Rows:", len(df))

# Create searchable text

texts = (
    df["drug"].astype(str)
    + " adverse event "
    + df["reaction"].astype(str)
).tolist()

print("Loading embedding model...")

model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

print("Generating embeddings...")

embeddings = model.encode(
    texts,
    show_progress_bar=True
)

print("Building FAISS index...")

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(embeddings)

faiss.write_index(
    index,
    "data/processed/faiss_index.bin"
)

with open(
    "data/processed/faiss_texts.pkl",
    "wb"
) as f:
    pickle.dump(texts, f)

print("DONE")
print("Vectors:", index.ntotal)