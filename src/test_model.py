from sentence_transformers import SentenceTransformer

print("Starting...")

model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

print("Model Loaded")