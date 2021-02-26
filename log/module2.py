import setting

set_dic = setting.setting()

if set_dic["MODE"] == "WhereFrom":
    import logging
    def f1():
        if False:
            logging.debug("debug log!!")
    def f2():
        if True:
            logging.debug("debug log!!")