from __future__ import annotations

from datetime import datetime
from typing import Literal, Optional

from pydantic import BaseModel, Field, ConfigDict

class PropertyFeatures(BaseModel):
    model_config = ConfigDict(extra="forbid")

    bedrooms: int = Field(..., ge=0, le=20, description="Number of bedrooms")
    bathrooms: float = Field(..., ge=0, le=20, description="Number of bathrooms (can be fractional)")
    sqft_living: int = Field(..., ge=100, le=20000, description="Interior living area in square feet")
    sqft_lot: Optional[int] = Field(None, ge=0, le=200000, description="Lot size in square feet (if available)")
    floors: Optional[float] = Field(None, ge=0, le=10, description="Number of floors")
    waterfront: Optional[Literal[0, 1]] = Field(None, description="1 if waterfront, else 0")
    view: Optional[int] = Field(None, ge=0, le=4, description="View rating (0-4)")
    condition: Optional[int] = Field(None, ge=1, le=5, description="Condition rating (1-5)")
    grade: Optional[int] = Field(None, ge=1, le=13, description="Construction grade (1-13)")
    yr_built: int = Field(..., ge=1800, le=2100, description="Year built")
    yr_renovated: Optional[int] = Field(None, ge=0, le=2100, description="Year renovated, or 0/None if never")
    zipcode: str = Field(..., pattern=r"^\d{5}$", description="US 5-digit ZIP code")
    lat: Optional[float] = Field(None, ge=-90, le=90, description="Latitude")
    long: Optional[float] = Field(None, ge=-180, le=180, description="Longitude")

class PredictRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    model_id: Optional[str] = Field(None,
                                    description="Model version to use. If ommitted, the service uses the latest model.",
                                    examples=["2026-02-01T12-34-56Z_abc123"],
                                    )
    features: PropertyFeatures

class PredictResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    model_id: str
    prediction: float = Field(..., ge=0, le=1, description="Predicted sale price in USD")
    currency: Literal["USD"] = "USD"
    created_at: datetime