from fastapi import APIRouter
from datetime import datetime, timezone
from typing import Optional

from housing_price_estimation_service.schemas.predict import (
    PredictRequest,
    PredictResponse,
)
from housing_price_estimation_service.schemas.train import (
    TrainRequest,
    TrainResponse,
    Metrics,
)

from housing_price_estimation_service.schemas.model import (
    ModelRequest,
    ModelResponse, Artifacts,
)

DEFAULT_DATASET = "house_sales.csv"

router = APIRouter()

@router.post("/train", response_model=TrainResponse)
def train(request: Optional[TrainRequest] = None):
    dataset = DEFAULT_DATASET
    if request and request.dataset:
        dataset=request.dataset

    # stub for now
    return TrainResponse(
        model_id="stub",
        metrics=Metrics(
            mae=0.0,
            rmse=0.0,
            r2=0.0
        ),
        trained_at=datetime(2026,2,3,tzinfo=timezone.utc),
        feature_columns=[]
    )

@router.get("/predict", response_model=PredictResponse)
def predict(request: Optional[PredictRequest] = None) :
    return PredictResponse(
        model_id="stub",
        prediction=0.0,
        currency="USD",
        created_at=datetime(2026,2,3,tzinfo=timezone.utc),
    )

@router.get("/model/{model_id}", response_model=ModelResponse)
def model(model_id : str) :
    return ModelResponse(
        model_id = model_id,
        trained_at=datetime(2026,2,3,tzinfo=timezone.utc),
        model_type="linear",
        metrics=Metrics(
            mae=0.0,
            rmse=0.0,
            r2=0.0
        ),
        feature_columns=[],
        artifacts=Artifacts(
            pipeline_path="models/2026-02-03T19-12-01Z_abc123/model.joblib",
            metadata_path="models/2026-02-03T19-12-01Z_abc123/metadata.json"
        )
    )

@router.get("/health")
def health():
    return {"status": "ok"}