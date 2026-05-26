import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin


class DateFeatureExtractor(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.copy()

        X["event_time"] = pd.to_datetime(X["event_time"],
                                         utc=True, errors="coerce")

        X["month"] = X["event_time"].dt.month
        X["day_of_week"] = X["event_time"].dt.dayofweek
        X["is_weekend"] = X["day_of_week"].isin([5, 6]).astype(int)
        X["is_holiday_season"] = X["month"].isin([12, 2, 3]).astype(int)

        X = X.drop(columns=["event_time"], errors="ignore")
        return X
