from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

memory_texts = []

dimension = 384
index = faiss.IndexFlatL2(dimension)

def store_text(text):
    global memory_texts

    embedding = model.encode([text])

    index.add(np.array(embedding).astype("float32"))

    memory_texts.append(text)

    print("Stored in memory")