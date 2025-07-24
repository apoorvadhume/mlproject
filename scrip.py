import os
import sys
import logging
import pandas as pd
from pathlib import Path
from src.exception import CustomException  # Import CustomException

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class DataIngestion:
    def __init__(self):
        # Define paths (adjust as needed)
        self.ingestion_config = type('', (), {
            'train_data_path': 'artifacts/train.csv',
            'raw_data_path': 'artifacts/raw_data.csv'
        })()

    def initiate_data_ingestion(self):
        logging.info("Entered the Data Ingestion method")
        try:
            # Read dataset (adjust path if needed)
            data_path = os.path.join('notebook', 'data', 'stud.csv')
            df = pd.read_csv(data_path)
            logging.info("Read the dataset as a DataFrame")

            # Create directory if it doesn't exist
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True)
            
            # Save raw data
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            logging.info("Raw data saved successfully")

        except Exception as e:
            logging.error("Error during data ingestion")
            raise CustomException(e, sys)  # Raise CustomException with context

if __name__ == "__main__":
    try:
        # Initialize and run data ingestion
        ingestion = DataIngestion()
        ingestion.initiate_data_ingestion()
    except Exception as e:
        logging.error(f"Script failed: {e}")
        sys.exit(1)