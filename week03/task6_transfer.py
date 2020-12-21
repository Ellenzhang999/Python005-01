import pymysql
from dbconfig import read_db_config
from sqlalchemy import create_engine


class BalanceIsNotEnough(Exception):
    def __init__(self, ErrorInfo):
        super().__init__(self, ErrorInfo)
        self.errorinfo = ErrorInfo

    def __str__(self):
        return self.errorinfo


# 连接数据库
dbserver = read_db_config()
conn = pymysql.connect(**dbserver)


# 事务开始
conn.begin()

# 转账步骤：
# 检查user1账户额度是否超过转账金额->减少user1额度->增加user2额度->增加一条审计记录->提交
# 2.

transfer_amt = 400
transfer_from = 'user2'
transfer_to = 'user1'

try:
    # 查询user1账户额度
    with conn.cursor() as cursor:
        sql = "SELECT balance FROM finance WHERE account_id=(select account_id from account where account_name='" + \
            transfer_from + "')"
        # print(sql)
        # 使用 execute()  方法执行 SQL 查询
        cursor.execute(sql)
        balance = cursor.fetchone()[0]

        if balance >= transfer_amt:
            sql_fin_minus = "update finance set balance=balance-%s, updated_on = now() where account_id=(select account_id from account where account_name=%s)"
            value_fin_minus = (transfer_amt, transfer_from)

            sql_fin_add = "update finance set balance=balance+%s, updated_on = now() where account_id=(select account_id from account where account_name=%s)"
            value_fin_add = (transfer_amt, transfer_to)

            sql_audit = "insert into auditinfo(account_id_from,account_id_to,transfer_amt, transfer_time) select (select account_id from account where account_name=%s),(select account_id from account where account_name=%s),%s,now()"
            value_audit = (transfer_from, transfer_to, transfer_amt)
            
            # print(sql_fin_minus)
            # print(sql_fin_add)
            # print(sql_audit)
            
            cursor.execute(sql_fin_minus, value_fin_minus)
            cursor.execute(sql_fin_add, value_fin_add)
            cursor.execute(sql_audit, value_audit)

        # 如果余额不足
        else:
            raise BalanceIsNotEnough("余额不足，转账中止")

    # 提交事務
    conn.commit()

except Exception as e:
    print(f"操作失敗:{e}")
    # 回滾事務
    conn.rollback()
    raise

finally:
    # 关闭数据库连接
    conn.close()
