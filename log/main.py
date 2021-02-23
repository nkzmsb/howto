"""
demonstrate logging and exception
"""

import logging.config
import time

import dummymodule
import logconfig


if __name__=="__main__":

    conf_for_log=logconfig.readconfig()
    logging.config.dictConfig(conf_for_log)

    print("="*3,"root")
    logging.critical({
        'massage' : 'root:critical'})
    logging.warning({
        'massage' : 'root:warning'}) 
    logging.debug({
        'massage' : 'root:debug'}) 
    
    print("="*3,"logger(simpleExample)")
    dummymodule.dm("good") # no problem

    def wrap(a):
        return dummymodule.dm(a)
    wrap("good_wrap")

    dummymodule.dm() # warning
    dummymodule.dm(3) # error and stop

    


