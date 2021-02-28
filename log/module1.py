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