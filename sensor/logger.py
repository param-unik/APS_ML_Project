import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M')}.log"

logs_path = os.path.join(os.getcwd(),"logs")
os.makedirs(logs_path,exist_ok=True)
LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
        filename =LOG_FILE_PATH,
        format = "[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
        level = logging.INFO
)

# import logging
# 
# class CustomLogger(logging.Logger):
    # def __init__(self, name, level=logging.DEBUG):
        # super().__init__(name, level)
# 
        # Create a custom formatter
        # formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# 
        # Create a console handler
        # console_handler = logging.StreamHandler()
        # console_handler.setFormatter(formatter)
# 
        # Add the console handler to the logger
        # self.addHandler(console_handler)
# 
# 
# 
# if __name__ == "__main__":
    # 
    # Create a custom logger
    # logger = CustomLogger('my_logger')
    # 
    # Log a message
    # logger.info('This is a custom log message!')


