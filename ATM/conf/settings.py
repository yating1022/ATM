 #配置文件

import logging
import os

BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))#找到路径
LOGIN_LEVEL = logging.INFO#定义日志的记录级别
DATABASE = {
    "db_tool":"file_storage",   #文件存储，这里可拓展成数据库形式的
    "name":"accounts",          #db 下的文件名
    "path":"%s/db"%BASE_DIR
}
#print(DATABASE)

#日志类型
LOGIN_TYPE={
    "access":"access.log",
    "transaction":"transaction.log"
}

#用户交易类型，每个类型对应一个字典，包括帐户金额变动方式，利息
TRANSACTION_TYPE={
    "repay":{"action":"plus","interest":0},
    "withdraw":{"action":"minus","interest":0.05},
    "transfer":{"action":"minus","interest":0}
}