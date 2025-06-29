import os
import sys
from six.moves import urllib # download data from urls
import zipfile
from Book_Recommender.logger.log import logging
from Book_Recommender.exception.exception_handler import AppException
from Book_Recommender.config.configuration import AppConfigurations


class DataIngestion:

    def __init__(self, app_config = AppConfigurations()):
        # initialize constructor which contains a Object for AppConfigurations(via object getting method)
        # via the method able to access all the data ingestion data
        try:
            logging.info(f"{'>'*20} data ingestion log started. {'<'*20}")
            self.data_ingestion_config = app_config.get_data_ingestion_config()
        
        except Exception as e:
            raise AppException(e, sys) from e
        

    def download_data(self):
        try:
            dataset_url = self.data_ingestion_config.dataset_download_url
            zip_download_dir = self.data_ingestion_config.raw_data_dir
            os.makedirs(zip_download_dir, exist_ok=True)

            data_file_name = os.path.join(zip_download_dir, data_file_name)
            zip_file_path = os.path.join(zip_download_dir, data_file_name)

            logging.info(f"Stat downloading data from {dataset_url} into file {zip_file_path}")
            #  Dowanload the data from link
            urllib.request.urlretrieve(dataset_url, zip_file_path)
            logging.info(f"Data downloaded from {dataset_url} into file {zip_file_path}")

            
            return zip_file_path
        
        except Exception as e:
            raise AppException(e, sys) from e
        

    def extract_zip_file(self, zip_file_pat:str):
        try:
            ingested_dir = self.data_ingestion_config.ingested_data
            os.makedirs(ingested_dir, exist_ok=True)
            
            with zipfile.ZipFile(zip_file_pat, 'r') as zip_ref:
                zip_ref.extractall(ingested_dir)
            logging.info(f"Extracting zip file {zip_file_pat} into {ingested_dir}")

        except Exception as e:
            raise AppException(e, sys) from e
        
    
    # download and extract the data
    def initiate_data_ingestion(self):
        try:
            zip_file_path = self.download_data()
            self.extract_zip_file(zip_file_pat=zip_file_path)
            logging.info(f"{'>'*20} Data Ingestion is Completed. {'<'*20}")
        except Exception as e:
            raise AppException(e, sys) from e