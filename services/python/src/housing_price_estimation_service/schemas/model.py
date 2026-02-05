from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict

from housing_price_estimation_service.schemas.train import Metrics

class Artifacts(BaseModel):
    model_config = ConfigDict(extra="forbid")

    pipeline_path: str
    metadata_path: str

class ModelRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

class ModelResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    model_id: str
    trained_at: datetime
    model_type: Literal["linear"] = "linear"
    metrics: Metrics
    feature_columns: list[str]
    artifacts: Artifacts
