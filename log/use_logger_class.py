import logging

# これは現時点ではおまじない -> 解説後述予定
logging.basicConfig(level=logging.INFO)

logger=logging.getLogger('Mr_new_Logger') # Mr_new_Loggerという名前のLoggerクラスインスタンスをget
logger.setLevel(logging.DEBUG) # Mr_new_LoggerはDEBUGレベル以上をログします。
logger.info("logger info!!") # infoレベルのイベントを検知したメッセージを作成。