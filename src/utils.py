import os
import sys

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from src.logger import logging
from src.exception import CustomException


def save_object(file_path, obj):
    """
    Saves the given object to a file using pickle.
    
    Args:
        file_path (str): The path where the object will be saved.
        obj: The object to be saved.
    """
    import pickle
    try:
        with open(file_path, 'wb') as file:
            pickle.dump(obj, file)
        logging.info(f"Object saved at {file_path}")
    except Exception as e:
        logging.error(f"Error saving object: {e}")
        raise CustomException(e, sys) from e    