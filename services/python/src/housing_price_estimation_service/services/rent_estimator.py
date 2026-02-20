from __future__ import annotations

from pathlib import Path

import pandas as pd

from housing_price_estimation_service.ml.train import train_model

PROJECT_ROOT = Path(__file__).resolve().parents[5]
DATA_DIR = PROJECT_ROOT / "data"

class RentEstimatorService:

    def train(self, dataset_filename: str):
        path = DATA_DIR / "raw" / dataset_filename
        if not path.exists():
            raise FileNotFoundError(f"Dataset not found: {dataset_filename}")

        house_sales_dataset = pd.read_csv(path)
        metrics = train_model(house_sales_dataset)

        return metrics