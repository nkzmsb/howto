"""
loggingの設定を定義する
 - sampleFormatterで指定された形式で、StreamHandlerを使って画面出力するように設定している
 - 'root'用のロガー（デフォルト設定）とは別にsimpleExampleというロガーも設定している
 - 'root'用のロガーで引っかかったものは、FileHandlerを使ってファイル出力するように設定している

>>> import logging.config

>>> conf_for_log=logconfig.readconfig()
>>> logging.config.dictConfig(conf_for_log)

>>> logger=logging.getLogger('simpleExample')
"""

import logging

def readconfig():
    dictconfig={
        'version' : 1,
        'formatters' : {
            'sampleFormatter' : {
                'format' : '%(asctime)s\t%(name)-12s\t%(module)s\t%(levelname)-8s\t%(message)s'}
        },
        'handlers' : {
            'sampleHandlers' : {
                'class' : 'logging.StreamHandler',
                'formatter' : 'sampleFormatter',
                'level' : logging.DEBUG
            },
            'fileHandler' : {
                'class' : 'logging.FileHandler',
                'formatter' : 'sampleFormatter',
                'filename' : 'samplelog.log',
                'level' : logging.DEBUG
            }
        },
        'root' : {
            'handlers' : ['sampleHandlers','fileHandler'],
            'level' : logging.WARNING
        },
        'loggers' : {
            'simpleExample' : {
                'handlers' : ['sampleHandlers'],
                'level' : logging.DEBUG,
                'propagate' : 0
            }
        }
    }

    return dictconfig
