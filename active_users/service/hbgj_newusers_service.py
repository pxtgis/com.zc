__author__ = 'zhangchao'
from db import goal_hbgj_newusers_dao
from db import source_hbgj_dao
from util import dateutil
from domain import hbgj_new_users


class NewusersDailyService():
    def __init__(self):
        # self.source_dao=source_hbgj_dao.hbgj_active_user_daily()
        # self.goal_dao=goal_hbgj_activeusers_dao.ActiveusersDaily()
        self.goal_dao=goal_hbgj_newusers_dao.NewusersDaily()

    def query_data(self):
        result=source_hbgj_dao.hbgj_new_user()
        # result=self.source_dao.get_users()
        for row in result:
            print(row.s_day,row.new_users,row.new_users_ios,row.new_users_android)
        return  result
    pass

    def insert_data(self,_results):
        for row in _results:
            sday_result=self.goal_dao.get_user(row.s_day)
            if sday_result==False:
                user_his=hbgj_new_users.New_users()
                user_his.s_day=row.s_day
                user_his.new_users=0
                user_his.new_users_ios=0
                user_his.new_users_android=0
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



def DailyMain():
    try:
        service=NewusersDailyService()
        result=service.query_data()
        service.insert_data(result)
        service.update_data(result)
    except Exception as e:
        print "HbgjNewDaily",e


if __name__=="__main__":
    DailyMain()

    pass