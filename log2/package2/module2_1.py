import logging

logger=logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

def func2_1():
    logger.debug({"trace" : True
                  , "message" : "debug log"})
    logger.error({"trace" : True
                  , "message" : "error log"})