from src.components.data_ingestion import DataIngestion
import src.logging.logging as logging
from src.exception.exception import ProjectException


if __name__ == "__main__":
    try:
        
        data_ingestion = DataIngestion()
        train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()
        
    except ProjectException as e:
        logging.logger.error(f"ProjectException: {e}")

    except Exception as e:
        logging.logger.error(f"Unexpected error: {e}")