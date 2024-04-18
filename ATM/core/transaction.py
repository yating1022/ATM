"""
transaction - 

Author: 水果捞
Date: 2024/4/17
Github:https://github.com/yating1022
"""
"""
交易模块,处理用户金额移动
"""
from ATM.conf import settings
from ATM.core import accounts
from ATM.core import log
def make_transaction(account_data,transcation_type,amount,log_obj,**kwargs):
    """
    处理用户交易
    :param account_data: 字典，用户的账户信息
    :param transcation_type: 用户交易的类型，repay or withdraw
    :param amount: 交易金额
    :return: 用户交易后账户的信息
    """
    amount = float(amount)
    if transcation_type in settings.TRANSACTION_TYPE:
        interest = amount * settings.TRANSACTION_TYPE[transcation_type]["interest"]#将类型中利息赋给interest
        old_balance = account_data["balance"]#账户原本的金额
        print(interest,old_balance)#输出利息和原来的金额
        #存款方法
        if settings.TRANSACTION_TYPE[transcation_type]["action"] == "plus":
            new_balance = old_balance + amount + interest
            log_obj.info("您的账户增加了%s,你现在的余额为%s"%(amount,new_balance))
        #取款方法
        elif settings.TRANSACTION_TYPE[transcation_type]["action"] == "minus":
            new_balance = old_balance - amount - interest
            log_obj.info("您的账户减少了%s，你现在的余额为%s"%(amount,new_balance))
            if new_balance <0:
                print("您的余额[%s] 不支持该业务 [-%s]"%(account_data["credit"],(amount+interest),old_balance))
                return
        account_data["balance"] = new_balance
        print("==============")
        print(account_data["balance"])
        print(account_data)
        accounts.dump_account(account_data)
        return account_data
    else:
        print("Transaction is not exist!")
