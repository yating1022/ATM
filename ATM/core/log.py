"""
log -

Author: 水果捞
Date: 2024/4/17
Github:https://github.com/yating1022
"""
import logging
from ATM.conf import settings
from ATM.core import db_handle

def log(logging_type):
    """
    main 模块调用access_logger = log.log("access")
    :param logging_type:“access”
    :return: 返回logger日志对象
    """
    logger = logging.getLogger(logging_type)
    logger.setLevel(settings.LOGIN_LEVEL)
    ch = logging.StreamHandler()
    ch.setLevel(settings.LOGIN_LEVEL)

    log_file = "%s/log/%s"%(settings.BASE_DIR,settings.LOGIN_TYPE[logging_type])
    fh = logging.FileHandler(log_file)
    fh.setLevel(settings.LOGIN_LEVEL)

    #日志格式
    formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')

    #输出格式
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)

    #把日志打印到指定的Handler
    logger.addHandler(ch)
    logger.addHandler(fh)

    return logger

