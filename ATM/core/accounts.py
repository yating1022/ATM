"""
account - 

Author: 水果捞
Date: 2024/4/17
Github:https://github.com/yating1022
"""
"""
用于处理用户信息的load 或 dump
"""
from ATM.core import db_handle
from ATM.conf import settings
import json
def load_account(account_id):
    """
    读取文件中的用户信息
    :return: 用户信息的字典
    """
    db_path = db_handle.handle(settings.DATABASE)#通过多个引用，最后得到用户配置文件的路径
    account_file = "%s/%s.json" %(db_path, account_id)
    with open(account_file, "r",encoding="utf-8") as f:
        account_data = json.load(f)
        return account_data
def dump_account(account_data):
    """
    将已更改的用户信息更新到用户文件
    :param account_data: 每操作后用户的信息
    :return:
    """
    db_path = db_handle.handle(settings.DATABASE)#通过多个引用，最后得到用户配置文件的路径
    print("====================%s"%db_path)
    account_file = "%s/%s.json" %(db_path,account_data["id"])
    with open(account_file, "w+",encoding="utf-8") as f :
        json.dump(account_data,f)
    print("更新用户")