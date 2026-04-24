from sklearn.cluster import DBSCAN
import numpy as np

def cluster_embeddings(embeddings):
    clustering = DBSCAN(metric="cosine", eps=0.3, min_samples=1)
    labels = clustering.fit_predict(embeddings)

    clusters = {}
    for idx, label in enumerate(labels):
        clusters.setdefault(f"cluster_{label}", []).append(idx)

    return clusters
  
