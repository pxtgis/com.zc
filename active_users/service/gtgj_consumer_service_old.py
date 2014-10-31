#coding=utf-8
__author__ = 'zhangchao'
from db import goal_gtgj_consumer_dao_old
from db import source_gtgj_userorder
from util import dateutil
from domain import gtgj_consumer_old

class ConsumerService():
    def __init__(self):
        self.source_dao=source_gtgj_userorder.SourceOrderDao()
        self.goal_dao=goal_gtgj_consumer_dao_old.GoaGtgjConsumerDao()

    # 从数据源查询过去30天的数据
    def query_data(self):
        today=dateutil.DateUtil.getToday()
        # print(test1._type)
        result=self.source_dao.get_orders(today)
        for row in result:
            print(row.s_day,row.order_num,row.ticket_num,row.user_num,row.amount)

        return  result


    def insert_data(self,_results):
        # goal=goal_order_dao.GoalOrderDao()
        for row in _results:
            sday_result=self.goal_dao.get_order(row.s_day)
            # print(sday_result)
            if sday_result==False:
                order_his=gtgj_consumer_old.Order_statistics()
                order_his.s_day=row.s_day
                order_his.order_num=0
                order_his.ticket_num=0
                order_his.user_num=0
                order_his.amount=0
                orders = []
                orders.append(order_his)
                self.goal_dao.insert_orders(orders)
                print(row.s_day,0)
            else:
                print(row.s_day,1)

    def update_data(self,_results):
        # goal=goal_order_dao.GoalOrderDao()
        test=self.goal_dao.update_orders(_results)
        print(test)

def main():
    service=ConsumerService()
    result=service.query_data()
    service.insert_data(result)
    service.update_data(result)

    pass

if __name__=="__main__":
    main()
    pass

