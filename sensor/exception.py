import sys

def error_message_detail(error, error_detail:sys):
    
    _, _, exc_tb = error_detail.exc_info()
    filename = exc_tb.tb_frame.f_code.co_filename
    line_no  = exc_tb.tb_lineno

    error_message = f">>> Error occured with the file name as -> [{filename}] and the line number is [{line_no}] and actual error is [{str(error)}] <<<"
    
    return error_message

class SensorException(Exception):
    
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error = error_message, error_detail = error_detail)
               
    def __str__(self):
        return self.error_message