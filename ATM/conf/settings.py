 #配置文件

import logging
import os

BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))#找到路径
"""
__file__ 是一个特殊变量，它指向当前执行的脚本文件的路径。
os.path.abspath(__file__) 用于获取当前脚本文件的绝对路径。
os.path.dirname() 函数返回指定路径的目录名称部分。
因此，os.path.dirname(os.path.abspath(__file__)) 将返回当前脚本文件所在的目录的路径。
然后，再次调用 os.path.dirname() 将返回该目录的父目录，即项目的根目录。
所以，BASE_DIR 将包含项目的根目录路径。
这里即输出/home/leting130/DjangoProject/ATM/ATM
"""
LOGIN_LEVEL = logging.INFO#定义日志的记录级别
DATABASE = {
    "db_tool":"file_storage",   #文件存储，这里可拓展成数据库形式的
    "name":"accounts",          #db 下的文件名
    "path":"%s/db"%BASE_DIR
    # 将/home/leting130/DjangoProject/ATM/ATM拼接/db，加上name 的accounts
    # /home/leting130/DjangoProject/ATM/ATM/db/accounts
    #最终得到22.json的绝对路径

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
def main():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(BASE_DIR)
if __name__ == '__main__':
    main()