from sensor.exception import SensorException
from sensor.logger import logging

import sys 
import os 

def test_exception():
    try:
        logging.info("starting test exception function")
        a = 1/0
        print(a)
        logging.info("ended test exception function")
    except Exception as e:
        logging.error("Exception happend in test exception function!")
        raise SensorException(e, sys)
    

if __name__ == '__main__':
    try:
        test_exception()
    except Exception as e:
        print(e)
