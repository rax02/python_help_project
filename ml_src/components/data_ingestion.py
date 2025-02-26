import os
import pandas as pd
from dataclasses import dataclass
from sklearn.model_selection import train_test_split
from ml_src.logging import logging


@dataclass
class DataIngestionConfig:
    raw_data_path: str=os.path.join('raw_file', 'data.csv')

@dataclass
class DataIngestionArtifact:
    train_data_path: str=os.path.join('artifacts', 'train_data.csv')
    test_data_path: str=os.path.join('artifacts', 'test_data.csv')
    validation_data_path: str=os.path.join('artifacts', 'validation_data.csv')


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
        self.ingestion_artifact = DataIngestionArtifact()

    def initiate_data_ingestion(self):
        logging.logger.info("Initiating data ingestion...")
        try:
            df = pd.read_csv("data_source/data.csv")
            
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path, index=False)

            os.makedirs(os.path.dirname(self.ingestion_artifact.train_data_path), exist_ok=True)
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            train_set.to_csv(self.ingestion_artifact.train_data_path, index=False)
            test_set.to_csv(self.ingestion_artifact.test_data_path, index=False)

            return (
                self.ingestion_artifact.train_data_path,
                self.ingestion_artifact.test_data_path,
            )

        except Exception as e:
            logging.logger.error(f"unexpected: {e}")
