import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s]: %(message)s"
# Creating a directory
log_dir = "logs"

# give the file path for our logging 
log_filepath = os.path.join(log_dir,"running_logs.log")

os.makedirs(log_dir,exist_ok=True)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        #all the file will be stored here
        logging.FileHandler(log_filepath),
        #all the messages will be stored here and showed in the cmd
        logging.StreamHandler(sys.stdout)]
)

#log object for calling out our logger
logger = logging.getLogger("CNNClassifier")