# difine the returns of the functions

from collections import namedtuple

DataIngestionConfig = namedtuple("Datasetconfig", ['dataset_download_url',
                                                   'raw_data_dir',
                                                   'ingested_data'])


DataValidationConfig = namedtuple("DataValidationConfig", ["clean_data_dir",
                                                         "books_csv_file",
                                                         "ratings_csv_file",
                                                         "serialized_objects_dir"])


DataTransformationConfig = namedtuple("DataTransformationConfig", ["clean_data_file_path",
                                                                   "transformed_data_dir"])  


ModelTrainerConfig = namedtuple("ModelTrainerConfig", ["transformed_data_file_dir",
                                                      "trained_model_dir",
                                                      "trained_model_name"])


ModelRecommendationConfig = namedtuple("ModelRecommendationConfig", ["book_name_serialized_objects",
                                                      "book_pivot_serialized_objects",
                                                      "final_rating_serialized_objects",
                                                      "trained_model_path"])
