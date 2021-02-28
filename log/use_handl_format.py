import logging

logger=logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# create console handler
handler = logging.StreamHandler()

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
handler.setFormatter(formatter)

# add handler to logger
logger.addHandler(handler)

logger.info("info!!")