# the most common functions that you use during development, write here and just import

import yaml
import sys
from Book_Recommender.exception.exception_handler import AppException


# function for read YAML files and return content as dictionary
def read_yaml_file(file_path : str) -> dict:
    try:
        with open(file_path, 'rb') as yaml_file:
            return yaml.safe_load(yaml_file)

    except Exception as e:
        raise AppException(e, sys) from e
    


