# main_B
# set configuration only for root Logger

import logging, logging.config

from package1.module1_1 import func1_1_1
from package1.package1a.module1a_1 import func1a_1_1
from package2.module2_1 import func2_1

MODE = "set_file_filter"

if __name__=="__main__":
    
    if MODE == "unexpected_log":
        # [非推奨] ← module0の書き方
        # you get the following output, though no handler is added.
        # NullHandlerが渡されているモジュールのログは表示されない。
        #   >>> module0 : without_handler
    
        from package0.module0 import func0
        func0()
    
    elif MODE == "set_root":
        # [推奨]小さなプロジェクト、簡単な確認ならこれでもよい
        # すべてのモジュールのINFOレベル以上のログが表示される
        logging.basicConfig(level=logging.INFO
                            , format = '%(asctime)s\t%(name)-12s\t%(funcName)s\t%(levelname)-8s\t%(message)s'
                            , handlers = [logging.StreamHandler()])
    elif MODE == "set_for":
        # [非推奨]これ自体をモジュールにしてもいいかもしれないが、ちょっと無理がある
        # モジュール毎に設定をプログラムで手書き
        # すべてのモジュールのINFOレベル以上のログが表示される
        for package in ["package1.module1_1","package2"]:
            logger = logging.getLogger(package)
            handler = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s\t%(name)-12s\t%(funcName)s\t%(levelname)-8s\t%(message)s')
            handler.setFormatter(formatter)
            logger.addHandler(handler)
            logger.setLevel(logging.INFO)
    elif MODE == "set_file":
        # [推奨]
        # yamlファイルに設定をまとめる
        
        import yaml
        
        with open("log2/logconfig.yaml", 'r') as yml:
            yaml_dic = yaml.safe_load(yml)
        logging.config.dictConfig(yaml_dic)
        
    elif MODE == "set_file_filter":
        # [推奨?]
        # Filterを使う場合にはクラス定義が必要なので、それを設定読み込みと同時にモジュール化する
        
        from logconfig import load_logconfig_dic # own module
        
        conf_dic = load_logconfig_dic("log2/logconfig2.yaml", filtering=True)
                         
        logging.config.dictConfig(conf_dic)
    
    
    func1_1_1()
    func1a_1_1()
    func2_1()
    