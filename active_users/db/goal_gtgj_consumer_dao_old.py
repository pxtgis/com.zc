__author__ = 'zhangchao'
from goal_mysql import *
import sys
sys.path.append('..')
from domain import gtgj_consumer_old
from util import dateutil

class GoaGtgjConsumerDao(Mysql):
    def __init__(self):
        Mysql.__init__(self)

    def insert_orders(self,orders):
        if (orders == None) or (len(orders) <= 0):
            pass
        else:
            db_name = 'bi_order_statistics'
            sql = 'insert into '+db_name+'(s_day,order_num,ticket_num,user_num,amount,createtime,updatetime) ' \
                                         'values (%s, %s, %s, %s, %s, now(), now())'
            args = []
            i = 0
            for order in orders:
                i += 1
                arg = [order.s_day,order.order_num,order.ticket_num,order.user_num,order.amount]
                args.append(arg)
                if i%100 == 0 or i == len(orders):
                    self.insert_many(sql, args)
                    args = []
                    self.end()

    def get_order(self,_day):
        # self.__init__()
        sql="select s_day,order_num,ticket_num,user_num,amount from bi_order_statistics where DATE_FORMAT(str_to_date(s_day,'%%Y-%%m-%%d'),'%%Y%%m%%d')=DATE_FORMAT(str_to_date(%s,'%%Y-%%m-%%d'),'%%Y%%m%%d')"
        arg=[_day]
        result=self.get_all(sql,arg)
        orders=[]
        if not result:
            return  False
        for row in result:
            order = gtgj_consumer_old.Order_statistics()
            order.s_day = row['s_day']
            order.order_num = row['order_num']
            order.ticket_num = row['ticket_num']
            order.user_num = row['user_num']
            order.user_num = row['amount']
            orders.append(order)
        return orders
        pass

    def update_orders(self,_orders):
        if (_orders == None):
            pass
        else:
            db_name = 'bi_order_statistics'
            sql="update bi_order_statistics set order_num=%s ,ticket_num=%s ,user_num=%s , amount=%s,updatetime=now()  where  DATE_FORMAT(str_to_date(s_day,'%%Y-%%m-%%d'),'%%Y%%m%%d')=DATE_FORMAT(str_to_date(%s,'%%Y-%%m-%%d'),'%%Y%%m%%d')"
            args = []
            # i = 0
            for order in _orders:
                # i += 1
                arg = [order.order_num,order.ticket_num,order.user_num,order.amount,order.s_day]
                # args.append(arg)
                # if i%100 == 0 or i == len(orders):
                self.update(sql,arg)
                    # args = []
                self.end()

def test_query():
    today1=dateutil.DateUtil.getToday()
    goal=GoaGtgjConsumerDao()
    result=goal.get_order(today1)[0]
    print(result.order_num,result.ticket_num,result.user_num,result.amount,result.s_day)
    pass

def test_insert():
    yes=dateutil.DateUtil.getYestaday()
    goal=GoaGtgjConsumerDao()
    result1=goal.get_order(yes)
    if result1==False:
        order_yes=gtgj_consumer_old.Order_statistics()
        order_yes.s_day=yes
        order_yes.order_num=0
        order_yes.ticket_num=0
        order_yes.user_num=0
        orders = []
        orders.append(order_yes)
        goal.insert_orders(orders)
        print(0)
        return 0
    else:
        print(1)
        return 1

    pass

def test_update():
    order_test1=gtgj_consumer_old.Order_statistics()
    order_test1.s_day='2014-08-09'
    order_test1.order_num=121
    order_test1.ticket_num=121
    order_test1.user_num=121

    order_test2=gtgj_consumer_old.Order_statistics()
    order_test2.s_day='2014-08-10'
    order_test2.order_num=111
    order_test2.ticket_num=111
    order_test2.user_num=111

    orders = []
    orders.append(order_test1)
    orders.append(order_test2)
    test1=GoaGtgjConsumerDao()
    test1.update_orders(orders)
    pass

if __name__ == '__main__':
    test_query()
    # test_insert()
    # print(test_update())
    print("test")
    pass