import pandas as pd
from abc import ABC, abstractmethod

class DataInspectionStatagey(ABC):
    @abstractmethod
    def inspect(self, df: pd.DataFrame):
        pass

class DataTypeInspection(DataInspectionStatagey):
    def inspect(self, df: pd.DataFrame):
        print("\nData Types and Non-null Counts:")
        print(df.info())

class DataStatsSummary(DataInspectionStatagey):
    def inspect(self, df: pd.DataFrame):
        print("\nSummary Statistics (Numerical Features):")
        print(df.describe())
        print("\nSummary Statistics (Categorical Features):")
        print(df.describe(include=["O"]))
    
class DataInspector:
    def __init__(self, strategy: DataInspectionStatagey):
        self._stategy = strategy

    def set_strategy(self, strategy: DataInspectionStatagey):
        self._stategy = strategy
    
    def execute_inspection(self, df: pd.DataFrame):
        self._strategy.inspect(df)

if __name__ == "__main__":
    # df = pd.read_csv('../extracted-data/your_data_file.csv')

    # inspector = DataInspector(DataTypesInspectionStrategy())
    # inspector.execute_inspection(df)

    # Change strategy to Summary Statistics and execute
    # inspector.set_strategy(SummaryStatisticsInspectionStrategy())
    # inspector.execute_inspection(df)
    pass