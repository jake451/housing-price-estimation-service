# Housing Price Estimation Service

A production-ready microservice that trains and serves an explainable baseline housing price estimation model using 
linear regression.

## Overview
The goal of this project is to predict the sale price of a residential property in Seattle given a set of structured 
property features. The service accepts property-level data and returns a numeric price estimate via a REST API.

Housing price estimates are based on features such as:
- Living area square footage
- Number of bedrooms and bathrooms
- Property condition and grade
- Year built and renovation status
- Location features (ZIP code / latitude & longitude)

Linear regression is used as an intentionally simple and interpretable baseline model to quantify how individual
property features contribute to overall price.

Accurately estimating housing prices is valuable for buyers, sellers, and real estate platforms. This project 
demonstrates how a well-validated, explainable baseline model can be deployed as a production-oriented service rather
than remaining a notebook-only experiment.

## Dataset
This project uses a publicly available dataset of Seattle home sales published on Kaggle.  
The dataset contains unit-level property features and historical sale prices and is used solely for educational and 
demonstration purposes.

## MVP Success
- Train a linear regression model from tabular housing data
- Expose training and inference via a REST API
- Return evaluation metrics after training (e.g., MAE, RMSE)
- Validate inputs and return clear, user-friendly errors

## Why Linear Regression?
Linear regression provides a fast, interpretable baseline that makes feature impact and model behavior easy to 
understand. Establishing a reliable baseline allows more complex models to be evaluated objectively and justified based on 
measurable improvements.

## High-Level Architecture
Client → REST API → ML Pipeline → Model Registry → Prediction

## API Design
### `POST /train`
  Train a new housing price estimation model from tabular data.

**Example request**
```bash 
curl -X POST "http://localhost:8000/train" \
  -H "Content-Type: application/json" \
  -d '{
    "dataset": "house_sales.csv"
  }'
```
**Example Response**
```json
{
  "model_id": "2026-02-03T19-12-01Z_abc123",
  "metrics": { "mae": 84213.5, "rmse": 121044.2, "r2": 0.72 },
  "trained_at": "2026-02-03T19:12:01Z",
  "feature_columns": ["bedrooms","bathrooms","sqft_living","zipcode", "..."]
}
```

### `POST /predict`
  Return a single price prediction for a set of property features.

**Example request**
```bash 
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "model_id": "latest",
    "features": {
      "bedrooms": 3,
      "bathrooms": 2.25,
      "sqft_living": 1960,
      "sqft_lot": 5000,
      "floors": 2,
      "waterfront": 0,
      "view": 0,
      "condition": 3,
      "grade": 7,
      "yr_built": 1996,
      "yr_renovated": 0,
      "zipcode": "98103",
      "lat": 47.6610,
      "long": -122.3426
    }
  }'
```
**Example Response**
```json
{
  "model_id": "2026-02-01T12-34-56Z_abc123",
  "prediction": 845230.12,
  "currency": "USD",
  "created_at": "2026-02-01T22:10:33.421Z"
}
```
### `GET  /model/{model_id}`
  Retrieve model metadata and evaluation metrics by model ID.

**Example request**
```bash 
curl -X GET "http://localhost:8000/model/{model_id}" \
  -H "Content-Type: application/json"
```
**Example Response**
```json
{
  "model_id": "2026-02-03T19-12-01Z_abc123",
  "trained_at": "2026-02-03T19:12:01Z",
  "model_type": "linear",
  "metrics": { "mae": 84213.5, "rmse": 121044.2, "r2": 0.72 },
  "feature_columns": ["bedrooms","bathrooms","sqft_living","zipcode", "..."],
  "artifacts": {
    "pipeline_path": "models/2026-02-03T19-12-01Z_abc123/model.joblib",
    "metadata_path": "models/2026-02-03T19-12-01Z_abc123/metadata.json"
  }
}
```
### `GET  /health`
  Health check endpoint used to verify the service is running.

**Example request**
```bash 
curl -X GET "http://localhost:8000/health"
```
**Example Response**
```json
{ 
  "status": "ok"
}
```

## Local Development and Running
```bash
# Run locally
make run

# Or with Docker
docker build -t housing-price-estimation-service .
docker run -p 8000:8000 housing-price-estimation-service
```

***
Built by Jason Dinger as a portfolio project focused on production-minded ML systems.
