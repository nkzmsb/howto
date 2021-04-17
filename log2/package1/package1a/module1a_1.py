import logging

logger=logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

def func1a_1_1():
    logger.debug({"message" : "debug log"})
    logger.error("error log")