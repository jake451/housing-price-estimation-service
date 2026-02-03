import json
from housing_price_estimation_service.schemas.predict import PredictRequest, PredictResponse

if __name__ == "__main__":
    request_schema = PredictRequest.model_json_schema()
    print(json.dumps(request_schema, indent=2))
    print("-" * 20)
    response_schema = PredictResponse.model_json_schema()
    print(json.dumps(response_schema, indent=2))