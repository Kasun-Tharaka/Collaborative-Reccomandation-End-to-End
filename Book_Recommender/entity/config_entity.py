# difine the returns of the functions

from collections import namedtuple

DataIngestionConfig = namedtuple("Datasetconfig", ['dataset_download_url',
                                                   'raw_data_dir',
                                                   'ingested_data'])