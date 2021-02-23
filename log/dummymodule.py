"""
A dummy module to chack the operation of logging
"""

import logging
import logging.config

import logconfig

conf_for_log=logconfig.readconfig()
logging.config.dictConfig(conf_for_log)
logger=logging.getLogger('simpleExample')

class O_NotString(Exception):
    """
    Original exception
    """
    pass


def testfunc(a):
    return a


def dm(*arg):
    try:
        a=arg[0]
    except IndexError as ex:
        logger.warning({
            'action': 'getarg',
            'exception' : ex,
            'massage' : 'guess that no arguments are set.'
        })
        a="INSERTED_DUMMY"

    if type(a)!=str:
        logger.error({
            'a' : a,
            'action': 'cheking type',
            'massage' : 'a is not str. program is stopped.',
            'type(a)' : type(a)
        })
        raise O_NotString("arg[0] should be str")

    result=testfunc(a)
    logger.debug({
            'a' : a
        })

    return result






if __name__=="__main__":
    print(dm(4))