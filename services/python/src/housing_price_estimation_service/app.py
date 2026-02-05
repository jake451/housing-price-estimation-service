from fastapi import FastAPI
from housing_price_estimation_service.api.routes import router

def create_app() -> FastAPI:
    app = FastAPI(
        title="Housing Price Estimation Service",
        version="0.1.0",
        description="Production-minded ML service for housing price estimation."
    )

    app.include_router(router);

    return app

app = create_app()