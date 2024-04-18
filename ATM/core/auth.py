"""
auth.py
Author: leting130
Date: 2024/4/17
github:https://github.com/yating1022
"""
import os
import json
import time
from ATM.core import db_handle
from ATM.conf import settings
def access_auth(account,password,log_obj):
    """
    下面的access——login调用access_auth方法，用于登录
    :param account: 用户名
    :param password: 密码
    :return: 如果未超预期，返回字典，超期则打印对应提示
    """
    db_path = db_handle.handle(settings.DATABASE)
    # 调用db_handle下的handle方法，返回路径/db/accoutns
    #返回/home/leting130/DjangoProject/ATM/ATM/db/accounts
    account_file = "%s/%s.json"%(db_path,account)
    #此处的account是用户名，
    print("用户名：%s"%account)
    print(account_file)
    if os.path.isfile(account_file):#判断account目录下有没有用户名的json文件
        with open(account_file,'r',encoding="utf-8") as f:
            account_data = json.load(f)
            print(account_data)
            if account_data['password'] == password:
                expire_time = time.mktime(time.strptime(account_data["expire_date"],"%Y-%m-%d"))
                # 将json中的时间转换为%Y-%m-%d格式的时间戳，这里的时间戳是json中的过期时间
                if time.time() > expire_time:#time（）.time获取现在的时间，对比过期时间，看账户是否过期
                    log_obj.error("Account[%s] logging success"%account)
                    print("账号 %s 已经过期"%account)

                else:
                    log_obj.info("Account[%s] does not exist!"%account)
                    return account_data
    else:
        log_obj.error("Account[%s] does not exist!"%account)
        print("Account[%s] does not exist!"%account)
def access_login(user_data,log_obj):
    """
    用户登录，如果失败3次就退出
    :param user_data: main.py 里面的字典
    :return: 如果账号和密码都正常而且未过期，就返回用户数据的字典
    """
    retry = 0
    while not user_data["is_authenticated"] and retry < 3:
        #用户字典中的is_authenticated初始为False，在这里not后得True , retry 表示尝试次数，当失败超过3次就退出
        account = input("账号：")
        password = input("密码：")
        user_auth_data = access_auth(account,password,log_obj)
        if user_auth_data:
            user_data["is_authenticated"] = True
            user_data["account_id"]=account
            print("欢迎登录 %s"%account)
            return user_auth_data
        retry+=1
    else:
        print("用户 [%s] 尝试登录次数过多"%account)
        log_obj.error("用户 [%s] 尝试登录次数过多"%account)
        exit()