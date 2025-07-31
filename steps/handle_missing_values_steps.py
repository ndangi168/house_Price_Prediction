from src.handle_missing_values import MissingValueHandler, DropingMissingValues, FillingMissingValues
import pandas as pd
from zenml import step

@step
def handle_missing_values_step(df: pd.DataFrame, strategy: str = "mean") -> pd.DataFrame:
    if strategy == "drop":
        handler = MissingValueHandler(DropingMissingValues(axis=0))
    elif strategy in ["mean", "mode", "median", "constant"]:
        handler = MissingValueHandler(FillingMissingValues(method=strategy))
    else:
        raise ValueError(f"Unsupported missing value handling strategy: {strategy}")
    
    cleaned_df = handler.handdle_missing_value(df)
    return cleaned_df