import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass # To create class variables easily

# Data Ingestion Configuration
@dataclass # Using @dataclass to automatically generate special methods like __init__()
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', 'train.csv') #all output will be stored in artifacts folder
    test_data_path: str = os.path.join('artifacts', 'test.csv')
    raw_data_path: str = os.path.join('artifacts', 'data.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig() # Initialize the config, so we can use it in the methods

    def initiate_data_ingestion(self):
        logging.info("Entered the Data Ingestion method or component")
        try:
            df = pd.read_csv('notebook\data\stud.csv') # Copying relative path from the notebook
            logging.info("Read the dataset as dataframe")
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True) # Create directory if it doesn't exist
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True) #

            logging.info("Train test split initiated")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42) # Splitting the data into train and test sets
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)   # Saving the train set to a CSV file
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)     # Saving the test set to a CSV file
            logging.info("Ingestion of train and test data completed")
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
                self.ingestion_config.raw_data_path
            )
        except Exception as e:
            raise CustomException(e, sys)
        
if __name__ == "__main__":
    obj = DataIngestion()
    train_data, test_data, raw_data = obj.initiate_data_ingestion()
    print(train_data, test_data, raw_data)  # For testing purposes, you can print the paths