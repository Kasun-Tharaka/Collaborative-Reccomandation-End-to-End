from Book_Recommender.components.stage_00_data_ingestion import DataIngestion
from Book_Recommender.components.stage_01_data_validation import DataValidation


class Trainig_Pipeline:
    def __init__(self):
        self.data_ingestion = DataIngestion()
        self.data_validation = DataValidation()


    def start_training_pipeline(self):
        # execute dowloading and extracting data(zipfile)
        self.data_ingestion.initiate_data_ingestion()
        self.data_validation.initiate_data_validation()