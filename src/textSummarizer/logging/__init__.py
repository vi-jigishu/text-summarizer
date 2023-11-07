#a custom log by the youtuber

import os
import sys
import logging

logging_str="[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"  #this logging string will store timestamp, lablename, module name(the root file), log message
log_dir="logs"
log_filepath = os.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir, exist_ok=True)

#instead of writing custom exception we will use 'box exception'



#logic for the logging_str
logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]  #it will log in two places- log_filepath and (dislay) in the terminal
)

logger= logging.getLogger("textSummarizerLogger")
