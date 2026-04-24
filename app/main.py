from fastapi import FastAPI
from app.embed import embed_alerts
from app.cluster import cluster_embeddings

app = FastAPI()

@app.post("/cluster")
async def cluster(alerts: list[str]):
    embeddings = embed_alerts(alerts)
    clusters = cluster_embeddings(embeddings)

    result = {
        cluster: [alerts[i] for i in indices]
        for cluster, indices in clusters.items()
    }

    return result
