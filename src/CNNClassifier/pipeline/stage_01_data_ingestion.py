from CNNClassifier.components.stage_01_data_ingestion import DataIngestion
from CNNClassifier.config import ConfigurationManager
from CNNClassifier import logger

logger.info(f"Data Ingestion stage started")
config= ConfigurationManager()
data_ingestion_config = config.get_data_ingestion_config()


data_ingestion= DataIngestion(config = data_ingestion_config)

data_ingestion.download_file()

data_ingestion.unzip_and_clean()


logger.info("Data ingestion stage completed successfully")