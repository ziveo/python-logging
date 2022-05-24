import logging

# logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(
    level=logging.DEBUG,
    filename="logs/main.log",
    filemode="a",
    # format="%(name)s - %(levelname)s - %(message)s",
    # format="%(asctime)s.%(msecs)05d - %(name)s - %(levelname)s - %(message)s",
    format="%(asctime)s.%(msecs)05d - %(name)s - %(levelname)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
)


logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")
