import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

documents = []
dimension = 384
index = faiss.IndexFlatL2(dimension)

def embed_text(text: str):
    return np.array(model.encode(text)).astype("float32")

def add_document(text: str):
    embedding = embed_text(text)
    documents.append(text)
    index.add(np.array([embedding]))

def query_document(question: str):
    if not documents:
        return "No documents uploaded yet."

    query_embedding = embed_text(question)
    _, I = index.search(np.array([query_embedding]), k=1)
    return documents[I[0][0]]
