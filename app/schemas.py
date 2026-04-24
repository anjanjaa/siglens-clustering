from pydantic import BaseModel
from typing import Dict, List


class AlertsRequest(BaseModel):
    alerts: List[str]


class ClustersResponse(BaseModel):
    clusters: Dict[str, List[str]]
