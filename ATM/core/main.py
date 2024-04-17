"""
main - 

Author: 水果捞
Date: 2024/4/17
Github:https://github.com/yating1022
"""
"""
主逻辑交互模块
"""
from ATM.core import auth
from ATM.core import log
from ATM.core import transaction
from ATM.core import accounts
from ATM.core import db_handle
from ATM.conf import settings

import os

#用户数据信息
user_data = {
    'account_id':None,#账号ID
    'is_authenticated':False,#是否认证
    'account_data':None  #账户数据
}

#调用log文件下的log方法，返回日志对象
access_logger = log.log("access")
transaction_logger = log.log("transaction")
def account_info(access_data):
    """
    :param access_data: 包括ID，is——authenticaed，用户账号信息
    查看用户信息方法
    :return:
    """
    print(access_data)


def reoay(access_data):
    """
    :param access_data: 包括ID，is——authenticaed，用户账号信息
    还款
    :return:
    """
    print(access_data)
    print("还款")
    #调用account模块的load_accpimt方法，从数据库load出用户信息
    access_data = accounts.load_account(access_data["account_id"])
    print(access_data)
    current_balance= """
    ---------------BALANCE INFO-----------------
    额度:%s
    余额:%s
    """%(access_data["credit"],access_data["balance"])
    back_flag = False
    while not back_flag:
        print(current_balance)
        repay_amount = input("\033[31;输入还款金额(b = 退出:\033[0m").strip()
        if len(repay_amount) > 0 and  repay_amount.isdiggit():
            new_account_data = transaction.make_transaction(access_data,"repay",repay_amount,transaction_logger)
            if new_account_data:
                print("/033[42;lmNew Balance:%s\033[0m"%(new_account_data["balance"]))
        else:
            print("\033[31;lm%s is not valid amount, Only accept interget!\033[0m"%(repay_amount))
            if repay_amount == "b" or repay_amount == "back":
                back_flag = True
def withdraw(access_data):
    """
    取款
    :return:
    """
    print(access_data)
    print("取款")
