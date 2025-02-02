import os
import pandas as pd
import zipfile as zip
from pathlib import Path
import urllib.request as request
from sklearn.model_selection import train_test_split
from mlProject import logger
from mlProject.utils.common import get_size
from mlProject.entity.config_entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config    

    def train_test_split(self):
        data = pd.read_csv(self.config.data_path)
        train_set, test_set = train_test_split(data, test_size=0.2, random_state=42)
        train_set.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test_set.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)

        logger.info(f"Train set size: {len(train_set)}")
        logger.info(f"Test set size: {len(test_set)}")  
        logger.info(f"Data split completed successfully")

