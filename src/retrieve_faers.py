import pickle
import faiss

from sentence_transformers import SentenceTransformer

print("Loading embedding model...")

model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

print("Loading FAISS index...")

index = faiss.read_index(
    "data/processed/faiss_index.bin"
)

print("Loading records...")

with open(
    "data/processed/faiss_texts.pkl",
    "rb"
) as f:

    texts = pickle.load(f)

print("Ready")

def search_faers(
    query,
    k=5
):

    q = model.encode([query])

    D, I = index.search(q, k)

    results = []

    for idx in I[0]:
        results.append(texts[idx])

    return results