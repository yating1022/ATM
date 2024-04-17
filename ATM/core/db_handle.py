# 处理与数据库的交互，若是file_db_storage,返回路径
def file_db_handle(datebase):
# 数据存在文件
# param datebase
# return：返回路径 ATM1/db/accounts
    db_path ="%s/%s"%(datebase["path"],datebase["name"])
    # print(db_path)
    return db_path
def mysql_db_handle(datebase):
    pass
def handle(datebase):
    if datebase["db_tool"]=="file_storage":
        return file_db_handle(datebase)
    if datebase["db_tool"]=="mysql":
        return mysql_db_handle(datebase)