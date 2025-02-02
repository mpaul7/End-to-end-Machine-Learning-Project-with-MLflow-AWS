from mlProject.constants import *
from mlProject.utils.common import read_yaml, create_directories
from mlProject.entity.config_entity import DataIngestionConfig, DataValidationConfig
class ConfigurationManager:
    def __init__(
            self,
            config_filepath = CONFIG_FILE_PATH,
            params_filepath = PARAMS_FILE_PATH,
            schema_filepath = SCHEMA_FILE_PATH
        ):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)
        
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config_data_ingestion = self.config.data_ingestion
        create_directories([config_data_ingestion.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config_data_ingestion.root_dir,
            source_URL=config_data_ingestion.source_URL,
            local_data_file=config_data_ingestion.local_data_file,
            unzip_dir=config_data_ingestion.unzip_dir
        )
        return data_ingestion_config