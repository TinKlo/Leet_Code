import logging
import os
import datetime


def setup_logger():
    logger = logging.getLogger("my_logger")
    logger.setLevel(logging.DEBUG)

    logging.getLogger().setLevel(logging.INFO)

    file_name = str(os.path.basename(__file__)).split(".")[0] + ".log"

    formatter = logging.Formatter('%(asctime)s %(levelname)-8s %(message)s')

    file_handler = logging.FileHandler(file_name)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)
    stream_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger
