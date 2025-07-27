import os
import zipfile
from abc import ABC, abstractmethod

import pandas as pd 


# Abstract class for Data ingestor
class DataIngestor(ABC):
    @abstractmethod
    def ingest(self, file_path: str) -> pd.DataFrame:
        pass

# class for zip ingestion
class ZipDataIngestor(DataIngestor):
    def ingest(self, file_path: str) -> pd.DataFrame:
        # check for .zip
        if not file_path.endswith(".zip"):
            raise ValueError("Please provide Zip file")
        
        # Extract data from Zip into new dir "extracted_data"
        with zipfile.ZipFile(file_path, "r") as zip_ref:
            zip_ref.extractall("extracted_data")

        # Find extracted file
        extracted_file = os.listdir("extracted_data")
        csv_files = [f for f in extracted_file if f.endswith(".csv")]

        if len(csv_files) == 0:
            raise ValueError("No csv file found")
        if len(csv_files) > 1:
            raise ValueError("Multiple csv file found, please specify perticular one.")

        csv_files_path = os.path.join("extracted_data", csv_files[0])
        df = pd.read_csv(csv_files_path)

        return df

# Factory to create DataIngestor
class DataIngestorFactory:
    @staticmethod
    def get_data_ingestor(file_extension: str) -> DataIngestor:
        # return Zip data ingestor
        if file_extension == ".zip":
            return ZipDataIngestor()
        else:
            return ValueError(f"No ingestor available for extension: {file_extension}")

if __name__ == "__main__":

    # file_path = "/Users/nikhildangi/Documents/COde/housePricePrediction/data/archive.zip"

    # file_extension = os.path.splitext(file_path)[1]

    # data_ingestor = DataIngestorFactory.get_data_ingestor(file_extension)

    # df = data_ingestor.ingest(file_path)

    pass
