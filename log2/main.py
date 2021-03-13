# main_B
# set configuration only for root Logger

import logging, logging.config

import yaml

from package1.module1_1 import func1_1_1
from package1.package1a.module1a_1 import func1a_1_1
from package2.module2_1 import func2_1

MODE = "set_file_filter"

if __name__=="__main__":
    
    if MODE == "set_root":
        logging.basicConfig(level=logging.INFO
                            , format = '%(asctime)s\t%(name)-12s\t%(funcName)s\t%(levelname)-8s\t%(message)s'
                            , handlers = [logging.StreamHandler()])
    elif MODE == "set_for":
        for package in ["package1","package2"]:
            logger = logging.getLogger(package)
            handler = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s\t%(name)-12s\t%(funcName)s\t%(levelname)-8s\t%(message)s')
            handler.setFormatter(formatter)
            logger.addHandler(handler)
            logger.setLevel(logging.INFO)
    elif MODE == "set_file":
        with open("log2/logconfig.yaml", 'r') as yml:
            yaml_dic = yaml.safe_load(yml)
        logging.config.dictConfig(yaml_dic)
        
    elif MODE == "set_file_filter":
        
        import ast
        
        class MyFilter(logging.Filter):
            def filter(self, record):
                # TrueをreturnすればLogする
                log_message = record.getMessage()
                try:
                    log_message_dict = ast.literal_eval(log_message)
                    ret = not(log_message_dict["trace"])
                except:
                    ret = True
                return ret
        
        with open("log2/logconfig.yaml", 'r') as yml:
            yaml_dic = yaml.safe_load(yml)
        
        yaml_dic["filters"] = {"my_filter" : {'()': MyFilter}}
        yaml_dic['handlers']['console']["filters"] = ['my_filter']
                         
        logging.config.dictConfig(yaml_dic)
    
    
    func1_1_1()
    func1a_1_1()
    func2_1()