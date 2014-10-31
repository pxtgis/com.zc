#coding=utf-8
__author__ = 'zhangchao'
# 获取每天要更新的数据，为插入数据做准备
from source_gtgj_mysql import *
import sys
sys.path.append('..')
from domain import gtgj_consumer_old
from util import dateutil

class SourceOrderDao(Mysql):
    def __init__(self):
        Mysql.__init__(self,dbtype='gtgj')

    def get_orders(self,_today):
        # sql需要更改！！！！
        #############
        # sql = "select * from bi_order where DATE_FORMAT(str_to_date(s_day,'%%Y-%%m-%%d'),'%%Y%%m%%d')>=DATE_FORMAT(DATE_SUB(str_to_date(%s,'%%Y-%%m-%%d'),INTERVAL 30 DAY),'%%Y%%m%%d')"
        # sql2="select CONCAT(YEAR(create_time),'-',MONTH(create_time),'-',  DAY(create_time)) s_day,sum(case when i_status=3 then 1 else 0 end) order_num,sum(case when i_status=3 then ticket_count else 0 end) ticket_num,count(DISTINCT uid) user_num from user_order GROUP BY s_day order by create_time;"
        sql_gtgj102="select CONCAT(YEAR(create_time),'-',MONTH(create_time),'-',  DAY(create_time)) s_day,count(*) order_num,sum(ticket_count) ticket_num,count(DISTINCT uid) user_num,sum(amount) amount from user_order where i_status=3 GROUP BY s_day order by create_time"
        # sql3="select * from bi_order "
        arg = [_today]
        # result = self.get_all(sql, arg)
        result=self.get_all(sql_gtgj102)
        # result=self.get_all(sql3)
        orders = []
        if not result:
            return False
        for row in result:
            order = gtgj_consumer_old.Order_statistics()
            order.s_day = row['s_day']
            order.order_num = row['order_num']
            order.ticket_num = row['ticket_num']
            order.user_num = row['user_num']
            order.amount = row['amount']
            orders.append(order)
        return orders

def test():
    today1=dateutil.DateUtil.getToday()
    test1=SourceOrderDao()
    print(test1._type)
    results=test1.get_orders(today1)
    print(results)
    # for row in results:
    #     print(row.s_day,row.order_num)
    # print()

if __name__ == '__main__':
     # test()
    print("OK")