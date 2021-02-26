import logging

logging.basicConfig(level=logging.INFO)

logger=logging.getLogger('Mr_new_Logger')
logger.setLevel(logging.DEBUG)
logger.debug("logger debug!!")