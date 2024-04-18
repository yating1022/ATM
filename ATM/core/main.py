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


def repay(access_data):
    """
    :param access_data: 包括ID，is——authenticaed，用户账号信息
    还款
    :return:
    """
    print(access_data)
    print("存款")
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
        repay_amount = input("\033[31;输入存款金额(b = 退出:\033[0m").strip()
        if len(repay_amount) > 0 and  repay_amount.isdigit():
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
        repay_amount = input("\033[31;输入取款金额(b = 退出:\033[0m").strip()
        if len(repay_amount) > 0 and  repay_amount.isdigit():
            new_account_data = transaction.make_transaction(access_data,"withdraw",repay_amount,transaction_logger)
            if new_account_data:
                print("\033[42;lmNew Balance:%s\033[0m"%new_account_data["balance"])
        else:
            print("\033[31;lm%s 不是有效金额，请输入整数\033[0m"%(repay_amount))
        if repay_amount == "b" or repay_amount == "back":
            back_flag = True


def transfer(access_data):
    """
    转账 的 函数
    :return:
    """
    print(access_data)
    print("转账")
    access_data = accounts.load_account(access_data["account_id"])
    print(access_data)
    current_balance = """
    ---------------BALANCE INFO-----------------
    额度:%s
    余额:%s
    """ % (access_data["credit"], access_data["balance"])
    back_flag = False
    while not back_flag:
        print(current_balance)
        transfer_amount = input("\033[31;输入转账金额(b = 退出:\033[0m").strip()
        if len(transfer_amount) > 0 and transfer_amount.isdigit():
            new_account_data = transaction.make_transaction(access_data, "transfer", transfer_amount, transaction_logger)
            if new_account_data:
                print("\033[42;lmNew Balance:%s\033[0m" % new_account_data["balance"])
        else:
            print("\033[31;lm%s 不是有效金额，请输入整数\033[0m" % (transfer_amount))
        if transfer_amount == "b" or transfer_amount == "back":
            back_flag = True

#账单查看方法
def paycheck(access_data):
    """
    账单查看方法
    :return:
    """
    time = input("请输入时间 按照 （年-月-日）格式输入")
    log_file = "%s/log/%s"%(settings.BASE_DIR,settings.LOGIN_TYPE["transaction"])
    print(log_file)#输出路径
    with open(log_file, "r",encoding="utf-8") as f:
        for i in f.readlines():
            if time == i[0:10]:
                print(i)
            elif time == i[0:7]:
                print(i)
            elif time ==i[0:4]:
                print(i)



#退出登录函数
def logout(access_data):
    """
    退出登录
    :return:
    """
    q = input("如果你想要退出，，请输入q")
    if q == 'q':
        exit()


def interactive(access_data,**kwargs):
    """
    用户交互
    :param access_data:
    :param kwargs:
    :return:
    """
    msg = (
        """
        ----------------------交互菜单----------------------------
        \033[31;1m
        1、账户信息
        2、存款
        3、取款
        4、转账
        5、账单
        6、退出
        \033[0m"""
    )
    #创建一个菜单的字典，以实现快速调用
    menu_dic = {
        "1":account_info,
        "2":repay,
        "3":withdraw,
        "4":transfer,
        "5":paycheck,
        "6":logout
    }
    flag = False
    while not flag:
        print(msg)
        choice = input("<<<:").strip()
        if choice in menu_dic:
            menu_dic[choice](access_data)
        else:
            print("\033[31:1m 你输入的序号有误")


#运行函数
def run():
    """
    当程序启动时调用
    :return:
    """
    #调用认证模块，返回用户文件
    access_data = auth.access_login(user_data,access_logger)
    print("AA")
    if user_data["is_authenticated"]:#如果认证成功user_data["is_authenticated"]这个值会被赋予True
        print("认证成功")
        user_data["account_data"]  = access_data
        interactive(user_data)