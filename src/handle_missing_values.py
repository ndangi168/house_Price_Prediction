import pandas as pd
import logging # zenml don't have print, it use logging
from abc import ABC, abstractmethod

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class MissingValueHandlingStrategy(ABC):
    @abstractmethod
    def handle(self, df: pd.DataFrame) -> pd.DataFrame:
        pass

class DropingMissingValues(MissingValueHandlingStrategy):
    def __init__(self, axis=0, thresh=None):
        self.axis = axis
        self.thresh = thresh

    def handle(self, df: pd.DataFrame) -> pd.DataFrame:
        logging.info(f"Dropping missing values with axis={self.axis} and thresh={self.thresh}")
        df_cleaned = df.dropna(axis=self.axis, thresh=self.thresh)
        logging.info("Missing values dropped.")
        return df_cleaned
    
class FillingMissingValues(MissingValueHandlingStrategy):
    def __init__(self, method="mean", fill_value=None):
        self.method = method
        self.fill_value = fill_value
    
    def handle(self, df: pd.DataFrame) -> pd.DataFrame:
        logging.info(f"Filling missing values using method: {self.method}")
        df_cleaned = df.copy()
        if self.method == "mean":
            num_col = df_cleaned.select_dtypes(include="number").columns
            df_cleaned[num_col] = df_cleaned[num_col].fillna(df[num_col].mean())
        elif self.method == "median":
            num_col = df_cleaned.select_dtypes(include="number").columns
            df_cleaned[num_col] = df_cleaned[num_col].fillna(df[num_col].median())
        elif self.method == "mode":
            for col in df_cleaned.columns:
                df_cleaned[col].fillna(df[col].mode().iloc[0], inplace=True)
        elif self.method == "constant":
            df_cleaned = df_cleaned.fillna(self.fill_value)
        else:
            logging.warning(f"Unknown method '{self.method}'. No missing values handled.")

        logging.info("Missing values filled.")
        return df_cleaned
    
class MissingValueHandler:
    def __init__(self, strategy: MissingValueHandlingStrategy):
        self._strategy = strategy
    
    def set_strategy(self, strategy: MissingValueHandlingStrategy):
        self._strategy = strategy

    def handle_missing_value(self, df: pd.DataFrame) -> pd.DataFrame:
        logging.info("Executing missing value handling strategy.")
        return self._strategy.handle(df)

if __name__ == "__main__":
    # df = pd.read_csv("")
    # missing_value_handler = MissingValueHandlingStrategy(DroppingMissingValues())
    # df_cleaned = missing_value_handler.handle(df)

    # missing_value_handler.set_strategy(FillinMissingValues())
    # df_cleaned = missing_value_handler.handle(df)
    pass