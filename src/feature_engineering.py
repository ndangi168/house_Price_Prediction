import pandas as pd
import logging
from abc import ABC, abstractmethod
import numpy as np
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder, StandardScaler

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class FeatureEngineeringStrategy(ABC):
    @abstractmethod
    def apply_transformation(df: pd.DataFrame) -> pd.DataFrame:
        pass

class logTransformation(FeatureEngineeringStrategy):
    def __init__(self, features):
        self.features = features
    def apply_transformation(self, df: pd.DataFrame) -> pd.DataFrame:
        logging.info(f"Applying log transformation to features: {self.features}")
        df_tranform = df.copy()
        for feature in self.features:
            df_tranform[feature] = np.log1p(df[feature])
        logging.info("Log transformation completed.")
        return df_tranform
    
class StandardScaler(FeatureEngineeringStrategy):
    def __init__(self, features):
        self.features = features
    def apply_transformation(self, df: pd.DataFrame) -> pd.DataFrame:
        logging.info(f"Applying standard scaling to features: {self.features}")
        df_transform = df.copy()
        df_transform[self.features] = self.scaler.fit_transform(df[self.features])
        logging.info("Standard scaling completed.")
        return df_transform
    
class OneHotEncoder(FeatureEngineeringStrategy):
    def __init__(self, features, feature_range = (0,1)):
        self.features = features
        self.scaler = MinMaxScaler(feature_range=feature_range)
    def apply_transformation(self, df: pd.DataFrame) -> pd.DataFrame:
        logging.info(f"Applying one-hot encoding to features: {self.features}")
        df_transform = df.copy()
        encoded_df = pd.DataFrame(self.encoder.fit_tranform(df[self.features]), columns=self.encider.get_feature_names_out(self.features),)
        df_transform = df_transform.drop(columns=self.features).reset_index(drop=True)
        df_transform = pd.concat([df_transform, encoded_df], axis=1)
        logging.info("One-hot encoding completed.")
        return df_transform

class FeatureEngineering:
    def __init__(self, strategy: FeatureEngineeringStrategy):
        self._strategy = strategy
    def set_strategy(self, strategy: FeatureEngineeringStrategy):
        logging.info("Switching feature engineering strategy.")
        self._strategy = strategy
    def apply_feature_engineering(self, df: pd.DataFrame) -> pd.DataFrame:
        logging.info("Applying feature engineering strategy.")
        self._strategy.apply_transformation(df)

if __name__ == "__main__":
    # df = pd.read_csv('../extracted-data/your_data_file.csv')

    # Log Transformation Example
    # log_transformer = FeatureEngineer(LogTransformation(features=['SalePrice', 'Gr Liv Area']))
    # df_log_transformed = log_transformer.apply_feature_engineering(df)

    # Standard Scaling Example
    # standard_scaler = FeatureEngineer(StandardScaling(features=['SalePrice', 'Gr Liv Area']))
    # df_standard_scaled = standard_scaler.apply_feature_engineering(df)

    # Min-Max Scaling Example
    # minmax_scaler = FeatureEngineer(MinMaxScaling(features=['SalePrice', 'Gr Liv Area'], feature_range=(0, 1)))
    # df_minmax_scaled = minmax_scaler.apply_feature_engineering(df)

    # One-Hot Encoding Example
    # onehot_encoder = FeatureEngineer(OneHotEncoding(features=['Neighborhood']))
    # df_onehot_encoded = onehot_encoder.apply_feature_engineering(df)
    pass