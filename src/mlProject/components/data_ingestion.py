import os
import zipfile as zip
from pathlib import Path
import urllib.request as request

from mlProject import logger
from mlProject.utils.common import get_size
from mlProject.entity.config_entity import DataIngestionConfig

"""_summary_
    Data Ingestion class
    This class is used to download and extract the data from the source URL
    It uses the DataIngestionConfig class to get the configuration for the data ingestion
    It has two methods: download_file and extract_zip_file
    The download_file method downloads the file from the source URL and saves it to the local data file
    The extract_zip_file method extracts the zip file and saves the data to the unzip directory
    The class has an init method that takes the config as an argument and assigns it to the instance variable
    The class has a main method that creates an instance of the class and calls the download_file and extract_zip_file methods  
    
"""
class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} downloaded with the following info: {headers}")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")

    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zip.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)