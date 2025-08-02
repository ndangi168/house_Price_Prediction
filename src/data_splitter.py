import pandas as pd
from sklearn.model_selection import train_test_split
import logging
from abc import ABC, abstractmethod

class DataSplitterStrategy(ABC):
    @abstractmethod
    def split_data(self, df: pd.DataFrame, target_col: str):
        pass

class TrainTestSplitter(DataSplitterStrategy):
    def __init__(self, test_size = 0.2, random_state = 42):
        self.test_size = test_size
        self.random_state = random_state
    def split_data(self, df: pd.DataFrame, target_col: str):
        logging.info("Performing simple train-test split.")
        x = df.drop(columns=[target_col])
        y = df[target_col]

        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=self.test_size, random_state=self.random_state)

        logging.info("Train-test split completed.")
        return x_train, x_test, y_train, y_test
    
class DataSplitter:
    def __init__(self, strategy: DataSplitterStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: DataSplitterStrategy):
        logging.info("Switching data splitting strategy.")
        self._strategy = strategy

    def split(self, df: pd.DataFrame, target_column: str):
        logging.info("Splitting data using the selected strategy.")
        return self._strategy.split_data(df, target_column)


if __name__ == "__main__":
    # df = pd.read_csv('your_data.csv')

    # Initialize data splitter with a specific strategy
    # data_splitter = DataSplitter(SimpleTrainTestSplitStrategy(test_size=0.2, random_state=42))
    # X_train, X_test, y_train, y_test = data_splitter.split(df, target_column='SalePrice')

    pass

