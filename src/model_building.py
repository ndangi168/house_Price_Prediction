import logging
from abc import ABC, abstractmethod
import pandas as pd
from sklearn.base import RegressorMixin
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class ModelBuildigStrategy(ABC):
    @abstractmethod
    def build_and_train_model(self, x_train: pd.DataFrame, y_train: pd.Series):
        pass

class LinearRegressionStrategy(ModelBuildigStrategy):
    def build_and_train_model(self, x_train: pd.DataFrame, y_train: pd.Series):
        if not isinstance(x_train, pd.DataFrame):
            raise TypeError("X_train must be a pandas DataFrame.")
        if not isinstance(y_train, pd.Series):
            raise TypeError("y_train must be a pandas Series.")

        logging.info("Initializing Linear Regression model with scaling.")

        pipeline = Pipeline([
            ("scaler", StandardScaler())
            ("model", LinearRegression())
        ])
        logging.info("Training Linear Regression model.")
        pipeline.fit(x_train, y_train) 

        logging.info("Model training completed.")
        return pipeline
    
class ModelBuilder:
    def __init__(self, strategy: ModelBuildigStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: ModelBuildigStrategy):
        logging.info("Switching model building strategy.")
        self._strategy = strategy

    def build_model(self, X_train: pd.DataFrame, y_train: pd.Series) -> RegressorMixin:
        logging.info("Building and training the model using the selected strategy.")
        return self._strategy.build_and_train_model(X_train, y_train)


if __name__ == "__main__":
    # df = pd.read_csv('your_data.csv')
    # X_train = df.drop(columns=['target_column'])
    # y_train = df['target_column']

    # model_builder = ModelBuilder(LinearRegressionStrategy())
    # trained_model = model_builder.build_model(X_train, y_train)
    # print(trained_model.named_steps['model'].coef_)  # Print model coefficients

    pass
