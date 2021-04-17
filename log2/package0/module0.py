# 最終手段ハンドラを確認するためのモジュール

import logging

logger=logging.getLogger(__name__)

# Note
# any Handler is not added to logger

def func0():
        logger.error("module0 : without_handler")