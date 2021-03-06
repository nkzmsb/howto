import setting

set_dic = setting.setting()

if set_dic["MODE"] == "WhereFrom":
    import logging
    def f1():
        if False:
            logging.info("debug log!!")
    def f2():
        if False:
            logging.info("debug log!!")

if set_dic["MODE"] == "FromHere":
    import logging
    logger=logging.getLogger(__name__) # 推奨されるloggerの作り方
    logger.setLevel(logging.DEBUG) # loggerのレベルを設定
    def f1():
        if False:
            logger.info("debug log!!")
    def f2():
        if False:
            logger.info("debug log!!")
            
if set_dic["MODE"] == "NotBadExample":
    import logging
    logger=logging.getLogger(__name__)
    logger.setLevel(logging.WARNING)
    formatter = logging.Formatter('%(asctime)s\t%(name)-12s\t%(funcName)s\t%(levelname)-8s\t%(message)s')
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    def devide(i):
        if i%2 != 0:
            logger.warning({"action" : "check arg"
                            , "arg" : i
                            , "message" : "i%2 != 0"
                            })
        else:
            logger.debug({"action" : "check arg"
                          , "arg" : i
                          })
        return i/2.
            