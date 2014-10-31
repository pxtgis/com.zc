__author__ = 'zhangchao'
from db import goal_gtgj_activeusers_dao
from db import source_gtgj_activeuser_dao
from util import dateutil
from domain import gtgj_active_users

class ActiveusersDailyService():
    def __init__(self):
        self.source_dao=source_gtgj_activeuser_dao.ActiveUserDao()
        self.goal_dao=goal_gtgj_activeusers_dao.ActiveusersDaily()

    def query_data(self):
        today=dateutil.DateUtil.getToday()
        # print(test1._type)
        result=self.source_dao.get_users_daily()
        for row in result:
            print(row.s_day,row.active_users,row.active_users_ios,row.active_users_android)
        return  result

    def insert_data(self,_results):

        for row in _results:
            sday_result=self.goal_dao.get_user(row.s_day)
            if sday_result==False:
                user_his=gtgj_active_users.Active_users()
                user_his.s_day=row.s_day
                user_his.active_users=0
                user_his.active_users_ios=0
                user_his.active_users_android=0
                users = []
                users.append(user_his)
                self.goal_dao.insert_users(users)
                print(row.s_day,"insert")
            else:
                # print(row.s_day,1)
                pass

    def update_data(self,_results):
        test=self.goal_dao.update_users(_results)
        print(test)

class ActiveusersWeeklyService():
    def __init__(self):
        self.source_dao=source_gtgj_activeuser_dao.ActiveUserDao()
        self.goal_dao=goal_gtgj_activeusers_dao.ActiveusersWeekly()

    def query_data(self):
        today=dateutil.DateUtil.getToday()
        # print(test1._type)
        result=self.source_dao.get_users_weekly()
        for row in result:
            print(row.s_day,row.active_users,row.active_users_ios,row.active_users_android)
        return  result

    def insert_data(self,_results):

        for row in _results:
            sday_result=self.goal_dao.get_user(row.s_day)
            if sday_result==False:
                user_his=gtgj_active_users.Active_users()
                user_his.s_day=row.s_day
                user_his.active_users=0
                user_his.active_users_ios=0
                user_his.active_users_android=0
                users = []
                users.append(user_his)
                self.goal_dao.insert_users(users)
                print(row.s_day,"insert")
            else:
                # print(row.s_day,1)
                pass

    def update_data(self,_results):
        test=self.goal_dao.update_users(_results)
        print(test)

class ActiveusersMonthlyService():
    def __init__(self):
        self.source_dao=source_gtgj_activeuser_dao.ActiveUserDao()
        self.goal_dao=goal_gtgj_activeusers_dao.ActiveusersMonthly()

    def query_data(self):
        today=dateutil.DateUtil.getToday()
        # print(test1._type)
        result=self.source_dao.get_users_monthly()
        try:
            for row in result:
                print(row.s_day,row.active_users,row.active_users_ios,row.active_users_android)
        except Exception as e:
            print e
        return  result

    def insert_data(self,_results):
        try:
            for row in _results:
                sday_result=self.goal_dao.get_user(row.s_day)
                if sday_result==False:
                    user_his=gtgj_active_users.Active_users()
                    user_his.s_day=row.s_day
                    user_his.active_users=0
                    user_his.active_users_ios=0
                    user_his.active_users_android=0
                    users = []
                    users.append(user_his)
                    self.goal_dao.insert_users(users)
                    print(row.s_day,"insert")
                else:
                    # print(row.s_day,1)
                    pass
        except Exception as e:
            print(e)

    def update_data(self,_results):
        test=self.goal_dao.update_users(_results)
        print(test)

def DailyMain():
    try:
        service=ActiveusersDailyService()
        result=service.query_data()
        service.insert_data(result)
        service.update_data(result)
    except Exception as e:
        print "GtgjActiveDaily",e


def WeeklyMain():
    try:
        service=ActiveusersWeeklyService()
        result=service.query_data()
        service.insert_data(result)
        service.update_data(result)
    except Exception as e:
        print "GtgjActiveWeekly",e

def MonthlyMain():
    try:
        service=ActiveusersMonthlyService()
        result=service.query_data()
        service.insert_data(result)
        service.update_data(result)
    except Exception as e:
        print "GtgjActiveMonth",e

if __name__=="__main__":
    DailyMain()
    WeeklyMain()
    MonthlyMain()
    pass