
# loggingのconfigファイルを辞書型に変換するモジュール
# filterの定義・付加が可能
# filterの定義や付加のさせ方はユーザーが変更する必要がある
# クライアントからはload_logconfig_dic()のみが参照される


import ast
import logging
import yaml

# Filterの定義
class TraceCutFilter(logging.Filter):
    """traceモードをフィルタリング

    logのメッセージに
        "trace" : True
    の記述があるものをフィルタする
    """
    def filter(self, record):
        # TrueをreturnすればLogする
        log_message = record.getMessage()
        
        # [ToDo]except発生前提のコード良くない
        try:
            log_message_dict = ast.literal_eval(log_message)
            ret = not(log_message_dict["trace"])
        except:
            ret = True
        return ret
 
def addfilter(logconfig_dic):
    """configにfilter情報を付加する
    
    Parameters
    ----------
    logconfig_dic : dict
        付加対象の辞書

    Returns
    -------
    dict
        filter情報が付加された辞書
        
    
    example of the config dictionary added filter
    LOGGING = {
        'version': 1,
        'filters': {
            'myfilter': {
                '()': MyFilter,
            }
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'filters': ['myfilter']
            }
        },
        'root': {
            'level': 'DEBUG',
            'handlers': ['console']
        },
    }
    """
    
    added_dic = logconfig_dic.copy()
    
    # [ToDo]モサイ
    added_dic["filters"] = {"my_filter" : {'()': TraceCutFilter}}
    added_dic['handlers']['console']["filters"] = ['my_filter']
    
    return added_dic



def load_logconfig_dic(yaml_filepath, filtering=False):
    """logging.config.dictConfigの引数をyamlファイルから生成

    Parameters
    ----------
    yaml_filepath : str
        元となるyamlファイルのパス
    filtering : bool, optional
        filterを付加するかどうか
        付加の仕方は、addfilter()を自分で編集する必要がある
        , by default False

    Returns
    -------
    dict
        logging.config.dictConfigの引数となる辞書
    """
    # yamlファイルを辞書に変換
    with open(yaml_filepath, 'r') as yml:
        yaml_dic = yaml.safe_load(yml)
    
    if filtering:
        yaml_dic = addfilter(yaml_dic)
              
    return yaml_dic


if __name__ == "__main__":
    print(load_logconfig_dic("log2/logconfig.yaml",filtering=True))