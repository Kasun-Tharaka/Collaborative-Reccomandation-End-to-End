from Book_Recommender.components.stage_00_data_ingestion import DataIngestion

class Trainig_Pipeline:
    def __init__(self):
        self.data_ingestion = DataIngestion()

    def start_training_pipeline(self):
        # execute dowloading and extracting data(zipfile)
        self.data_ingestion.initiate_data_ingestion()