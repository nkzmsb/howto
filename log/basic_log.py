import logging
import time

LOGFILE_NAME = "log/basic_log"

# logファイルの初期化
with open(LOGFILE_NAME, mode="w"):
    pass

print("===start: not use logging===")
# logレベルの設定
MODE = "INFO"
for i in range(5): # 適当な繰り返しの処理を再現
    a = i
    b = i * 2
    c = a + b
    time.sleep(1) # 適当な処理時間を再現
    if MODE == "DEBUG" or MODE == "INFO":
        print("a:{}, b:{}".format(a,b))
    if MODE == "INFO":
        with open(LOGFILE_NAME, mode='a') as f:
            f.write("c:{}\n".format(c))
    
print("===start: use logging===")
# logレベルの設定
logging.basicConfig(level=logging.INFO)
for i in range(5): # 適当な繰り返しの処理を再現
    a = i
    b = i * 2
    c = a + b
    time.sleep(1) # 適当な処理時間を再現

    logging.debug("a:{}, b:{}".format(a,b))


logging.warning("warning")