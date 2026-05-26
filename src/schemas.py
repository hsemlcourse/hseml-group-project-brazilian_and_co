from datetime import datetime

from pydantic import BaseModel, Field


class PredictRequest(BaseModel):
    event_time: datetime = Field(...,
                                 description="Время события в ISO-формате")
    category_id: int | None = Field(default=None)
    category_alias: str | None = Field(default=None)
    brand_id: int | None = Field(default=None)
    gender: str | None = Field(default=None)
    color: str | None = Field(default=None)
    metal: str | None = Field(default=None)
    gem: str | None = Field(default=None)


class PredictResponse(BaseModel):
    prediction: float
