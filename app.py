from Book_Recommender.exception.exception_handler import AppException
import sys
from Book_Recommender.logger.log import logging


# testing custom exception wit Loggings
try:
    k = 10/ 0

except Exception as e:
    
    logging.info(e)
    raise AppException(e, sys) from e