import setting

set_dic = setting.setting()

if set_dic["MODE"] == "WhereFrom":
    import logging
    def f1():
        if False:
            logging.info("debug log!!")
    def f2():
        if True:
            logging.info("debug log!!")

if set_dic["MODE"] == "FromHere":
    import logging
    logger=logging.getLogger(__name__) # 推奨されるloggerの作り方
    logger.setLevel(logging.DEBUG) # loggerのレベルを設定
    def f1():
        if False:
            logger.info("debug log!!")
    def f2():
        if True:
            logger.info("debug log!!")
            
if set_dic["MODE"] == "NotBadExample":
    import logging
    
    logger=logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s\t%(name)-12s\t%(module)s\t%(levelname)-8s\t%(message)s')
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    def product(i):
        logger.debug({"action" : "check arg"
                      , "arg" : i
                      })
        return i*2.