import sys
import os


class AppException(Exception):
    def __init__(self, error_message: Exception, error_details: sys):
        super().__init__(error_message)
        self.error_message = AppException.error_message_detail(error_message, error_detail=error_details)



    @staticmethod
    def error_message_detail(error=Exception, error_detail=sys):
        _, _, exc_tb = error_detail.exc_info()
        file_name = exc_tb.tb_frame.f_code.co_filename

        
        error_message = f"Error occured [{file_name}] python file \n" \
                        f"Line number [{exc_tb.tb_lineno}] error meage [{error}]"
        
        return error_message
    


    def __repr__(self):
        return AppException.__name__.__str__()
    
    
    def __str__(self):
        return self.error_message