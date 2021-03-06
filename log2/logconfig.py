
# loggingのconfigファイルを辞書型に変換するモジュール
# filterの定義・付加が可能
# filterの定義や付加のさせ方はユーザーが変更する必要がある
# クライアントからはload_logconfig_dic()のみが参照される


import logging
import re
import yaml

# Filterの定義
class TraceCutFilter(logging.Filter):
    """traceモードをフィルタリング

    logのメッセージに
        "trace" : True
    の記述があるものをフィルタする
    
    一言でデバッグといっても、多くの情報をトレースしたい場合と、
    ピンポイント部分だけログしたい場合とがあるが、ログレベルはDEBUGしか用意されていない。
    そこで、前者の場合にはログメッセージに辞書型で{"trace" : True}と記入しておく。
    このフィルタはその記述があるものをカットする。
    """
    
    def filter(self, record):
        # TrueをreturnすればLogする
        log_message = record.getMessage()
        
        # traceの判定
        pattern = r"'trace': True"
        mach = re.search(pattern, log_message, re.IGNORECASE)
        
        if mach:
            ret = False
        else:
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
    
    # この部分をyamlファイルと付加させる対象にあわせて編集する
    filterinfo_dic = {"trace_cut_filter" : {'()': TraceCutFilter}}
    
    added_dic["filters"] = filterinfo_dic
    
    # 以下のように、ハンドラへのフィルター付加をここで行うことも可能だが、
    # 記述が複雑になるので、yamlファイル側でやる方がわかりやすい。
    # ただし、同じyamlファイルの内容へのフィルタの付け外しを頻繁に行う場合には、
    # この部分でハンドラへ付加して、load_logconfig_dicのfiltering引数を切り替えるほうが良い。
    # added_dic['handlers']['console']["filters"] = ['trace_cut_filter']
    
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