from functools import lru_cache
from pathlib import Path

import joblib
import pandas as pd

from src.schemas import PredictRequest


BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = (BASE_DIR / "../models/best_model.joblib").resolve()

FEATURE_COLUMNS = [
    "event_time",
    "category_id",
    "category_alias",
    "brand_id",
    "gender",
    "color",
    "metal",
    "gem",
]


@lru_cache
def load_model():
    if not MODEL_PATH.exists():
        raise FileNotFoundError(f"Модель не найдена по пути: {MODEL_PATH}")
    return joblib.load(MODEL_PATH)


def build_input_df(payload: PredictRequest) -> pd.DataFrame:
    data = payload.model_dump()

    for col in ["category_alias", "gender", "color", "metal", "gem"]:
        if data[col] is not None:
            data[col] = data[col].strip().lower()

    df = pd.DataFrame([data], columns=FEATURE_COLUMNS)
    return df


def predict_price(payload: PredictRequest) -> float:
    model = load_model()
    input_df = build_input_df(payload)
    prediction = model.predict(input_df)[0]
    return round(float(prediction), 2)
