__author__ = 'zhangchao'
from db import goal_gtgj_newusers_dao
from db import source_gtgj_newuser_dao
from util import dateutil
from domain import gtgj_newusers

class NewuserService():
    def __init__(self):
        self.source_dao=source_gtgj_newuser_dao.SourceUserDao()
        self.goal_dao=goal_gtgj_newusers_dao.GoalGtgjNewusersDao()

    def query_data(self):
        today=dateutil.DateUtil.getToday()
        # print(test1._type)
        result=self.source_dao.get_users()
        for row in result:
            print(row.s_day,row.new_users,row.new_users_ios,row.new_users_android)
        return  result

    def insert_data(self,_results):

        for row in _results:
            sday_result=self.goal_dao.get_user(row.s_day)
            if sday_result==False:
                user_his=gtgj_newusers.User_statistics()
                user_his.s_day=row.s_day
                user_his.new_users=0
                user_his.new_users_ios=0
                user_his.new_users_android=0
                users = []
                users.append(user_his)
                self.goal_dao.insert_users(users)
                print(row.s_day,"insert")
            else:
                pass
                # print(row.s_day,1)

    def update_data(self,_results):
        # goal=goal_order_dao.GoalOrderDao()
        test=self.goal_dao.update_users(_results)
        print(test)

def main():
    service=NewuserService()
    result=service.query_data()
    service.insert_data(result)
    service.update_data(result)

if __name__=="__main__":
    main()
    pass