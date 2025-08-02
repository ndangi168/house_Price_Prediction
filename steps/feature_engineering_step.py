import pandas as pd
from src.feature_engineering import (
    FeatureEngineering,
    logTransformation,
    MinMaxScaler,
    OneHotEncoder,
    StandardScaler,
)
from zenml import step


@step
def feature_engineering_step(df: pd.DataFrame, strategy: str = "log", features: list = None) -> pd.DataFrame:

    if features is None:
        features = [] 

    if strategy == "log":
        engineer = FeatureEngineering(logTransformation(features))
    elif strategy == "standard_scaling":
        engineer = FeatureEngineering(StandardScaler(features))
    elif strategy == "minmax_scaling":
        engineer = FeatureEngineering(MinMaxScaler(features))
    elif strategy == "onehot_encoding":
        engineer = FeatureEngineering(OneHotEncoder(features))
    else:
        raise ValueError(f"Unsupported feature engineering strategy: {strategy}")

    transformed_df = engineer.apply_feature_engineering(df)
    return transformed_df