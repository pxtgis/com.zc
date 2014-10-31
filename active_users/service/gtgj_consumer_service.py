#coding=utf-8
__author__ = 'zhangchao'
from db import goal_gtgj_consumers_dao
from db import source_gtgj_consumers_dao
from util import dateutil
from domain import gtgj_consumers


class ConsumerDailyService():
    def __init__(self):
        self.source_dao=source_gtgj_consumers_dao.ConsumersDailyDao()
        self.goal_dao=goal_gtgj_consumers_dao.ConsumersDaily()

    # 从数据源查询过去30天的数据
    def query_data(self):
        today=dateutil.DateUtil.getToday()
        # print(test1._type)
        result=self.source_dao.get_consumers()
        for row in result:
            print(row.s_day,row.consumers,row.consumers_ios,row.consumers_android)
        return  result


    def insert_data(self,_results):
        # goal=goal_order_dao.GoalOrderDao()
        for row in _results:
            sday_result=self.goal_dao.get_user(row.s_day)
            # print(sday_result)
            if sday_result==False:
                consumers_his=gtgj_consumers.Consumers()
                consumers_his.s_day=row.s_day
                consumers_his.consumers=0
                consumers_his.consumers_ios=0
                consumers_his.consumers_android=0
                consumers = []
                consumers.append(consumers_his)
                self.goal_dao.insert_users(consumers)
                print(row.s_day,"insert")
            else:
                pass
                # print(row.s_day,1)

    def update_data(self,_results):
        # goal=goal_order_dao.GoalOrderDao()
        test=self.goal_dao.update_users(_results)
        print(test)

class ConsumerWeeklyService():
    def __init__(self):
        self.source_dao=source_gtgj_consumers_dao.ConsumersWeeklyDao()
        self.goal_dao=goal_gtgj_consumers_dao.ConsumersWeekly()

    # 从数据源查询过去30天的数据
    def query_data(self):
        today=dateutil.DateUtil.getToday()
        # print(test1._type)
        result=self.source_dao.get_consumers()
        for row in result:
            print(row.s_day,row.consumers,row.consumers_ios,row.consumers_android)
        return  result


    def insert_data(self,_results):
        # goal=goal_order_dao.GoalOrderDao()
        for row in _results:
            sday_result=self.goal_dao.get_user(row.s_day)
            # print(sday_result)
            if sday_result==False:
                consumers_his=gtgj_consumers.Consumers()
                consumers_his.s_day=row.s_day
                consumers_his.consumers=0
                consumers_his.consumers_ios=0
                consumers_his.consumers_android=0
                consumers = []
                consumers.append(consumers_his)
                self.goal_dao.insert_users(consumers)
                print(row.s_day,"insert")
            else:
                pass
                # print(row.s_day,1)

    def update_data(self,_results):
        # goal=goal_order_dao.GoalOrderDao()
        test=self.goal_dao.update_users(_results)
        print(test)

class ConsumerMonthlyService():
    def __init__(self):
        self.source_dao=source_gtgj_consumers_dao.ConsumersMonthlyDao()
        self.goal_dao=goal_gtgj_consumers_dao.ConsumersMonthly()
    # 从数据源查询过去30天的数据
    def query_data(self):
        today=dateutil.DateUtil.getToday()
        # print(test1._type)
        result=self.source_dao.get_consumers()
        for row in result:
            print(row.s_day,row.consumers,row.consumers_ios,row.consumers_android)
        return  result


    def insert_data(self,_results):
        # goal=goal_order_dao.GoalOrderDao()
        for row in _results:
            sday_result=self.goal_dao.get_user(row.s_day)
            # print(sday_result)
            if sday_result==False:
                consumers_his=gtgj_consumers.Consumers()
                consumers_his.s_day=row.s_day
                consumers_his.consumers=0
                consumers_his.consumers_ios=0
                consumers_his.consumers_android=0
                consumers = []
                consumers.append(consumers_his)
                self.goal_dao.insert_users(consumers)
                print(row.s_day,"insert")
            else:
                pass
                # print(row.s_day,1)

    def update_data(self,_results):
        # goal=goal_order_dao.GoalOrderDao()
        test=self.goal_dao.update_users(_results)
        print(test)

def DailyMain():
    service=ConsumerDailyService()
    result=service.query_data()
    service.insert_data(result)
    service.update_data(result)

def WeeklyMain():
    service=ConsumerWeeklyService()
    result=service.query_data()
    service.insert_data(result)
    service.update_data(result)

def MonthlyMain():
    service=ConsumerMonthlyService()
    result=service.query_data()
    service.insert_data(result)
    service.update_data(result)

if __name__=="__main__":
    DailyMain()
    WeeklyMain()
    MonthlyMain()
    pass

