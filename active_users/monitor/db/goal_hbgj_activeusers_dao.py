__author__ = 'Administrator'
from goal_mysql import *
import sys
sys.path.append('..')
from domain import hbgj_active_users
from util import dateutil

class ActiveusersDaily(Mysql):
    def __init__(self):
        Mysql.__init__(self)

    def get_user(self,_day):
        sql="select s_day,active_users,active_users_ios,active_users_android from hbgj_activeusers_daily where DATE_FORMAT(str_to_date(s_day,'%%Y-%%m-%%d'),'%%Y%%m%%d')=DATE_FORMAT(str_to_date(%s,'%%Y-%%m-%%d'),'%%Y%%m%%d')"
        arg=[_day]
        result=self.get_all(sql,arg)
        users=[]
        if not result:
            return  False
        for row in result:
            user=hbgj_active_users.Active_users()
            user.s_day = row['s_day']
            user.active_users = row['active_users']
            user.active_users_ios = row['active_users_ios']
            user.active_users_android = row['active_users_android']
            users.append(user)
        return users


class ActiveusersWeekly(Mysql):
    def __init__(self):
        Mysql.__init__(self)


    def get_user(self,_day):
        sql="select s_day,active_users,active_users_ios,active_users_android from hbgj_activeusers_weekly where DATE_FORMAT(str_to_date(s_day,'%%Y-%%m-%%d'),'%%Y%%m%%d')=DATE_FORMAT(str_to_date(%s,'%%Y-%%m-%%d'),'%%Y%%m%%d')"
        arg=[_day]
        result=self.get_all(sql,arg)
        users=[]
        if not result:
            return  False
        for row in result:
            user=hbgj_active_users.Active_users()
            user.s_day = row['s_day']
            user.active_users = row['active_users']
            user.active_users_ios = row['active_users_ios']
            user.active_users_android = row['active_users_android']
            users.append(user)
        return users



class ActiveusersMonthly(Mysql):
    def __init__(self):
        Mysql.__init__(self)

    def get_user(self,_day):
        sql="select s_day,active_users,active_users_ios,active_users_android from hbgj_activeusers_monthly where DATE_FORMAT(str_to_date(s_day,'%%Y-%%m-%%d'),'%%Y%%m%%d')=DATE_FORMAT(str_to_date(%s,'%%Y-%%m-%%d'),'%%Y%%m%%d')"
        arg=[_day]
        result=self.get_all(sql,arg)
        users=[]
        if not result:
            return  False
        for row in result:
            user=hbgj_active_users.Active_users()
            user.s_day = row['s_day']
            user.active_users = row['active_users']
            user.active_users_ios = row['active_users_ios']
            user.active_users_android = row['active_users_android']
            users.append(user)
        return users
