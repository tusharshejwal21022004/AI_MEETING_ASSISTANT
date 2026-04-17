from sentence_transformers import SentenceTransformer
import numpy as np
from rag_module.store_memory import index, memory_texts

model = SentenceTransformer("all-MiniLM-L6-v2")

def retrieve_context(query):
    query_embedding = model.encode([query])

    D, I = index.search(np.array(query_embedding).astype("float32"), 1)

    if len(memory_texts) == 0:
        return ""

    return memory_texts[I[0][0]]