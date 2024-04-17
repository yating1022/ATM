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
    account_file = "%s/%s"%(db_path,account)
    #此处的account是用户名，
    print(account_file)
    if os.path.isfile(account_file):#判断account目录下有没有用户名的json文件
        with open(account_file,'r',encoding="utf-8") as f:
            account_data = json.load(f)
            print(account_data)
            if account_data['password'] == password:
                expire_time = time.mktime(time.strptime(account_data["expire_date"],"%Y-%m-%d"))
                # 将json中的时间转换为%Y-%m-%d格式的时间戳
