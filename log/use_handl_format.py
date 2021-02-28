import logging

logger=logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# create formatter
formatter = logging.Formatter('%(asctime)s\t%(name)-12s\t%(module)s\t%(levelname)-8s\t%(message)s'
                              # , datefmt='%y%m%d_%H:%M:%S' # asftimeの形式を指定することも可能
                              )

# create console handler
handler = logging.StreamHandler()

# add formatter to ch
handler.setFormatter(formatter)

# add handler to logger
logger.addHandler(handler)

logger.info("info!!")