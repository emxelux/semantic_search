import numpy as np
from sentence_transformers import SentenceTransformer


class VectorDatabase:
    def __init__(self, model_name = "all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)
        self.documents = []
        self.embeddings = None

    
    def upsert(self, texts: list[str]):
        new_embeddings = self.model.encode(texts)
        self.documents.extend(texts)

        if  self.embeddings is None:
            self.embeddings = new_embeddings
        else:
            self.embeddings = np.vstack([self.embeddings, new_embeddings])
        
        return f"{len(self.embeddings)} Added to vector database successfully"
    

    def search(self, query:str, top_k = 5):
        q_embedding = self.model.encode([query])[0]
        dot_products = np.dot(self.embeddings, q_embedding)
        norms = np.linalg.norm(self.embeddings, axis=1) * np.linalg.norm(q_embedding)

        similarities = dot_products / norms

        print(f"documents of {len(self.documents)} vs similarity: {len(similarities)}")

        top_indices = np.argsort(similarities)[::-1][:top_k]
        return [(self.documents[i], float(similarities[i])) for i in top_indices]