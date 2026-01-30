# Rent Estimation Service

A production-ready microservice that trains and serves an explainable baseline rent estimation model using linear regression.

## Overview
The goal of this project is to predict a monthly rental price given a set of rental listing features. The service accepts structured listing data and returns a numeric rent estimate via a REST API.

Rent estimates are based on features such as:
- Square footage
- Neighborhood
- Walk score
- Distance to downtown
- Year built.

Linear regression is used as an intentionally simple and interpretable baseline model to learn relationships between 
these variables and rental prices.

Accurately estimating rental prices is useful for tenants, landlords, and housing platforms. This project demonstrates
how a well-validated, explainable baseline model can be deployed as a production-oriented service rather than remaining
a notebook-only experiment.

## MVP Success
- Train a linear regression model from tabular rental listing data
- Expose training and inference via a REST API
- Return evaluation metrics after training
- Validate inputs and return clear errors

## High-level architecture
Client → REST API → ML Pipeline → Model Registry → Prediction

## API Design
POST /train

POST /predict

GET  /model/{model_id}

GET  /health


## Local Development and Running
``` bash
# Run locally
make run

# Or with Docker
docker build -t rent-estimation-service .
docker run -p 8000:8000 rent-estimation-service
```

***
Built by Jason Dinger as a portfolio project focused on production-minded ML systems.
