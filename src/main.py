from fastapi import FastAPI, HTTPException

from src.inference import MODEL_PATH, load_model, predict_price
from src.schemas import PredictRequest, PredictResponse


app = FastAPI(
    title="Jewelry Price Prediction API",
    version="1.0.0",
    description="API для предсказания цены ювелирного товара"
)


@app.on_event("startup")
def startup_event():
    load_model()


@app.get("/health")
def health():
    return {
        "status": "ok",
        "model_path": str(MODEL_PATH)
    }


@app.post("/predict", response_model=PredictResponse)
def predict(payload: PredictRequest):
    try:
        prediction = predict_price(payload)
        return PredictResponse(prediction=prediction)
    except FileNotFoundError as e:
        raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {e}")
