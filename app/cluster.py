from sklearn.cluster import DBSCAN


def cluster_embeddings(embeddings, eps: float = 0.3, min_samples: int = 1):
    """
    Cluster embeddings using cosine distance.
    Returns a dictionary mapping cluster IDs to alert indexes.
    """
    clustering = DBSCAN(
        metric="cosine",
        eps=eps,
        min_samples=min_samples,
    )

    labels = clustering.fit_predict(embeddings)

    clusters = {}

    for index, label in enumerate(labels):
        cluster_id = f"cluster_{label + 1}"
        clusters.setdefault(cluster_id, []).append(index)

    return clusters
    
