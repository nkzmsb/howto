import logging

logger=logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

def func2_1():
    logger.error("error log")