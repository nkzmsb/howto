import logging

logger=logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

def func1_1_1():
    logger.error("error log")