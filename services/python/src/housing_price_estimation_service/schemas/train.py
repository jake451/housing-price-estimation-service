from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, ConfigDict

FILENAME_RE = r"^[A-Za-z0-9][A-Za-z0-9_.-]*\.csv$"

class Metrics(BaseModel):
    model_config = ConfigDict(extra="forbid")

    mae: float = Field(..., ge=0, description="Mean Absolute Error")
    rmse: float = Field(..., ge=0, description="Root Mean Squared Error")
    r2: float = Field(..., ge=-1, le=1, description="R^2 Score")

class Artifacts(BaseModel):
    model_config = ConfigDict(extra="forbid")

    pipeline_path: str
    metadata_path: str

class TrainRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    dataset: Optional[str] = Field(
        default=None,
        pattern=FILENAME_RE,
        description="CSV filename located in the server dataset directory (e.g., 'house_sales.csv'). " 
                    "Must not contain path separators or '..'. If omitted, the default dataset is used.",
        examples=["house_sales.csv"],
    )

class TrainResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    model_id: str
    metrics: Metrics
    trained_at: datetime
    feature_columns: list[str]
    artifacts: Optional[Artifacts] = None