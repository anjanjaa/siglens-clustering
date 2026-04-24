from sentence_transformers import SentenceTransformer


model = SentenceTransformer("all-MiniLM-L6-v2")


def embed_alerts(alerts: list[str]):
    """
    Convert alert text into vector embeddings.
    """
    return model.encode(alerts)
    
