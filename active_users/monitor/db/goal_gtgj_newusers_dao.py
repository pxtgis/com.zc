__author__ = 'Administrator'
from goal_mysql import *
import sys
sys.path.append('..')
from domain import gtgj_newusers
from util import dateutil

class GoalGtgjNewusersDao(Mysql):
    def __init__(self):
        Mysql.__init__(self)



    def get_user(self,_day):
        sql="select s_day,new_users,new_users_ios,new_users_android from gtgj_newusers_daily where DATE_FORMAT(str_to_date(s_day,'%%Y-%%m-%%d'),'%%Y%%m%%d')=DATE_FORMAT(str_to_date(%s,'%%Y-%%m-%%d'),'%%Y%%m%%d')"
        arg=[_day]
        result=self.get_all(sql,arg)
        users=[]
        if not result:
            return  False
        for row in result:
            user= gtgj_newusers.User_statistics()
            user.s_day = row['s_day']
            user.new_users = row['new_users']
            user.new_users_ios = row['new_users_ios']
            user.new_users_android = row['new_users_android']

            users.append(user)
        return users



