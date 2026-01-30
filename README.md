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
- `POST /train`
- `POST /predict`
- `GET  /model/{model_id}`
- `GET  /health`

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
