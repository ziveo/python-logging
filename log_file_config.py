import logging
from logging import config

config.fileConfig(fname="log_file_config.ini", disable_existing_loggers=False)


logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")
