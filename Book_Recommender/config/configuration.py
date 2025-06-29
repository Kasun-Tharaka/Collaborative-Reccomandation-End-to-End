import os
import sys
from Book_Recommender.logger.log import logging
from Book_Recommender.exception.exception_handler import AppException
from Book_Recommender.utils.util import read_yaml_file
from Book_Recommender.entity.config_entity import DataIngestionConfig
from Book_Recommender.constant import *


class AppConfigurations:
    def __inint__(self, config_file_path: str = CONFIG_FILE_PATH):
        try:
            self.config_info = read_yaml_file(file_path=config_file_path)

        except Exception as e:
            raise AppConfigurations(e, sys) from e
        

    # this function returns data ingestion configs.
    def get_data_ingestion_config(self) -> DataIngestionConfig:

        try:
            data_ingestion_config = self.config_info['data_ingestion_config']
            artifacts_dir = self.config_info['artifacts_config']['artifacts_dir']
            dataset_dir = data_ingestion_config['dataset_dir']

            ingested_data_dir = os.path.join(artifacts_dir, dataset_dir, data_ingestion_config
                                             ['ingested_dir'])
            raw_data_dir = os.path.join(artifacts_dir, dataset_dir, data_ingestion_config['raw_data_dir'])

            response = DataIngestionConfig(
                dataset_download_url = data_ingestion_config['dataset_download_url'],
                raw_data_dir = raw_data_dir,
                ingested_dir = ingested_data_dir
            )

            logging.info(f"data ingestion confic {response}")
            return response
        
        except Exception as e:
            raise AppException(e, sys) from e