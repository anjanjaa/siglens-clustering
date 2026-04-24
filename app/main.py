from fastapi import FastAPI

from app.cluster import cluster_embeddings
from app.embed import embed_alerts
from app.schemas import AlertsRequest, ClustersResponse


app = FastAPI(
    title="Alert Semantic Clustering",
    description="Embedding-based alert grouping using semantic similarity.",
    version="0.1.0",
)


@app.get("/")
async def root():
    return {
        "service": "alert-semantic-clustering",
        "status": "running",
    }


@app.post("/cluster", response_model=ClustersResponse)
async def cluster_alerts(request: AlertsRequest):
    embeddings = embed_alerts(request.alerts)
    cluster_indexes = cluster_embeddings(embeddings)

    clusters = {
        cluster_id: [request.alerts[index] for index in indexes]
        for cluster_id, indexes in cluster_indexes.items()
    }

    return {"clusters": clusters}
    
