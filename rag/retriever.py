from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

embed_model = SentenceTransformer('all-MiniLM-L6-v2')

docs = [
    "Chest pain can indicate heart attack and requires immediate attention.",
    "Fever is usually caused by infection and should be monitored.",
    "Headache may be due to stress or dehydration.",
    "Shortness of breath may indicate lung or heart issues."
]

doc_embeddings = embed_model.encode(docs)

index = faiss.IndexFlatL2(doc_embeddings.shape[1])
index.add(np.array(doc_embeddings))

def retrieve_context(query):
    q_emb = embed_model.encode([query])
    D, I = index.search(np.array(q_emb), k=2)
    return [docs[i] for i in I[0]]
