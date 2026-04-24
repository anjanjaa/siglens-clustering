# alert-semantic-clustering

Embedding-based system for grouping and analyzing alerts using semantic similarity.

---

## Context

Monitoring systems generate large volumes of alerts, often representing the same underlying issue across multiple services or nodes.

These alerts are structurally related but treated as separate signals, increasing noise and operational load.

This system introduces a semantic layer that groups alerts based on meaning rather than exact matching.

alerts → embeddings → clustering → grouped incidents

---

## Functionality

Given a set of alert messages, the system:

- converts alerts into vector embeddings  
- computes semantic similarity  
- groups related alerts into clusters  
- outputs grouped structures for downstream processing  

---

## Example

### Input

```json
[
  "High latency detected on gateway-1",
  "Latency spike on satellite node",
  "Packet loss increasing on link A",
  "High latency detected on gateway-2"
]
```

### Output

```json
{
  "cluster_1": [
    "High latency detected on gateway-1",
    "Latency spike on satellite node",
    "High latency detected on gateway-2"
  ],
  "cluster_2": [
    "Packet loss increasing on link A"
  ]
}
```

---

## Approach

- Text embeddings (OpenAI / sentence-transformers)
- Cosine similarity for distance calculation
- Clustering using simple algorithms (e.g. DBSCAN or hierarchical clustering)

---

## Architecture

- Embedding layer  
- Similarity computation  
- Clustering module  
- Structured output  

---

## Tech Stack

- Python  
- scikit-learn  
- numpy  
- OpenAI embeddings / sentence-transformers  

---

## Status

Minimal working prototype for alert grouping and semantic clustering.

---

## Direction

- integration with alert pipelines  
- correlation across metrics + logs + alerts  
- temporal clustering (event sequences)  
- integration with LLM-based interpretation layer  

---

## Run locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Then open:
```
http://127.0.0.1:8000/docs
```

Use the /cluster endpoint with the example JSON.
