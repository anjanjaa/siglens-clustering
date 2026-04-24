from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_alerts(alerts):
    return model.encode(alerts)
  
