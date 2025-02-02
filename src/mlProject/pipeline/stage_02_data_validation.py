from mlProject.config.configuration import ConfigurationManager
from mlProject.components.data_validation import DataValidation
from mlProject import logger

STAGE_NAME = "Data Validation stage"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        """
        This is the main method that creates an instance of the ConfigurationManager class and calls the get_data_ingestion_config method
        to get the configuration for the data ingestion. It then creates an instance of the DataIngestion class and calls the download_file and extract_zip_file methods
        to download and extract the data from the source URL.
        """
        config_manager = ConfigurationManager()
        data_validation_config = config_manager.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_columns()


if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e