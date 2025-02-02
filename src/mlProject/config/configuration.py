from mlProject.constants import *
from mlProject.utils.common import read_yaml, create_directories
from mlProject.entity.config_entity import (
    DataIngestionConfig, 
    DataValidationConfig,
    DataTransformationConfig,
    ModelTrainerConfig,
    ModelEvaluationConfig
)

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
    
    def get_data_validation_config(self) -> DataValidationConfig:
        config_data_validation = self.config.data_validation
        schema_data_validation = self.schema.COLUMNS
        create_directories([config_data_validation.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=config_data_validation.root_dir,
            unzip_data_dir=config_data_validation.unzip_data_dir,
            STATUS_FILE=config_data_validation.STATUS_FILE,
            all_schema=schema_data_validation
        )
        return data_validation_config
    
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config_data_transformation = self.config.data_transformation
        create_directories([config_data_transformation.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir=config_data_transformation.root_dir,
            data_path=config_data_transformation.data_path
        )
        return data_transformation_config
    
    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config_model_trainer = self.config.model_trainer
        params_model_trainer = self.params.ElasticNet
        schema_model_trainer = self.schema.TARGET_COLUMN
        create_directories([config_model_trainer.root_dir])

        model_trainer_config = ModelTrainerConfig(
            root_dir=config_model_trainer.root_dir,
            train_data_path=config_model_trainer.train_data_path,
            test_data_path=config_model_trainer.test_data_path,
            model_name=config_model_trainer.model_name,
            alpha=params_model_trainer.alpha,
            l1_ratio=params_model_trainer.l1_ratio,
            target_column=schema_model_trainer.name
        )
        return model_trainer_config
    
    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        config_model_evaluation = self.config.model_evaluation
        params_model_evaluation = self.params.ElasticNet
        schema_model_evaluation = self.schema.TARGET_COLUMN
        create_directories([config_model_evaluation.root_dir])

        model_evaluation_config = ModelEvaluationConfig(
            root_dir=config_model_evaluation.root_dir,
            test_data_path=config_model_evaluation.test_data_path,
            model_path=config_model_evaluation.model_path,
            all_params=params_model_evaluation,
            metric_file_name=config_model_evaluation.metric_file_name,
            target_column=schema_model_evaluation.name,
            mlflow_uri="https://dagshub.com/mpaul7/End-to-end-Machine-Learning-Project-with-MLflow-AWS.mlflow"
        )
        return model_evaluation_config