
import time

# print("===start: not use logging===")
# # logレベルの設定
# MODE = "INFO"
# for i in range(5): # 適当な繰り返しの処理を再現
#     # 適当な処理・処理時間を再現
#     a = i
#     b = i * 2
#     c = a + b
#     time.sleep(1)
# 
#     if MODE == "DEBUG" or MODE == "INFO":
#         print("a:{}, b:{}".format(a,b))
#     if MODE == "INFO":
#         print("c:{}".format(c))
    
print("===start: use logging===")
import logging

# logレベルの設定
logging.basicConfig(level=logging.DEBUG
                    , filename="log/basic_log.log" # This kwarg is not necessary when displaying imfomation on the screen
                    )
for i in range(5): # 適当な繰り返しの処理を再現
    # 適当な処理・処理時間を再現
    a = i
    b = i * 2
    c = a + b
    time.sleep(1)

    # DEBUGレベルの処理
    logging.debug("a:{}, b:{}".format(a,b))

    # INFOレベルの処理
    logging.info("c:{}".format(c))