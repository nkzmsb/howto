import setting

set_dic = setting.setting()

if set_dic["MODE"] == "WhereFrom":
    import logging
    def f1():
        if False:
            logging.debug("debug log!!")
    def f2():
        if False:
            logging.debug("debug log!!")

if set_dic["MODE"] == "FromHere":
    import logging
    logger=logging.getLogger(__name__) # 推奨されるloggerの作り方
    logger.setLevel(logging.DEBUG)
    def f1():
        if False:
            logger.debug("debug log!!")
    def f2():
        if False:
            logger.debug("debug log!!")