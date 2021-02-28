import setting
import time

set_dic = setting.setting()

if set_dic["MODE"] in ["WhereFrom", "FromHere"]:
    def main():
        import logging

        import module1, module2

        logging.basicConfig(level=logging.INFO)
        
        module1.f1()
        module1.f2()
        module2.f1()
        module2.f2()

        if False:
            logging.debug("debug log!!")

if set_dic["MODE"] == "NotBadExample":
    def main():
        import logging

        import module1, module2

        # logging.basicConfig(level=logging.INFO)
        
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s\t%(name)-12s\t%(module)s\t%(levelname)-8s\t%(message)s')
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        
        for i in range(5):
            time.sleep(1)
            
            if i>3:
                logger.warning({"action" : "check counter"
                                , "counter" : i
                                , "message" : "counter is too large!!"
                            })
            
            m1 = module1.devide(i)
            m2 = module2.product(i)
            
            val = m1 + m2
            
            logger.info({"action" : "check result"
                         , "counter" : i
                         , "result" : val
                         })
            
else:
    def main():
        pass



if __name__ == "__main__":
    main()