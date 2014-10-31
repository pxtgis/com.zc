__author__ = 'Administrator'
from goal_mysql import *
import sys
sys.path.append('..')
from domain import hbgj_active_users
from util import dateutil

class ActiveusersDaily(Mysql):
    def __init__(self):
        Mysql.__init__(self)

    def insert_users(self,_users):
        if (_users==None) or (len(_users)<=0):
            pass
        else:
            db_name='hbgj_activeusers_daily'
            sql='insert into '+db_name+' (s_day,active_users,active_users_ios,active_users_android,createtime,updatetime)'\
                                         'values (%s, %s, %s, %s, now(), now())'
            args = []
            i = 0
            for user in _users:
                i += 1
                arg = [user.s_day,user.active_users,user.active_users_ios,user.active_users_android]
                args.append(arg)
                if i%100 == 0 or i == len(_users):
                    self.insert_many(sql, args)
                    args = []
                    self.end()

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


    def update_users(self,_users):
        if (_users == None):
            pass
        else:
            db_name = 'hbgj_activeusers_daily'
            sql="update hbgj_activeusers_daily set active_users=%s,active_users_ios=%s,active_users_android=%s,updatetime=now() where  DATE_FORMAT(str_to_date(s_day,'%%Y-%%m-%%d'),'%%Y%%m%%d')=DATE_FORMAT(str_to_date(%s,'%%Y-%%m-%%d'),'%%Y%%m%%d')"
            args = []
            for user in _users:
                arg = [user.active_users,user.active_users_ios,user.active_users_android,user.s_day]
                self.update(sql,arg)
                self.end()

class ActiveusersWeekly(Mysql):
    def __init__(self):
        Mysql.__init__(self)

    def insert_users(self,_users):
        if (_users==None) or (len(_users)<=0):
            pass
        else:
            db_name='hbgj_activeusers_weekly'
            sql='insert into '+db_name+' (s_day,active_users,active_users_ios,active_users_android,createtime,updatetime)'\
                                         'values (%s, %s, %s, %s,now(), now())'
            args = []
            i = 0
            for user in _users:
                i += 1
                arg = [user.s_day,user.active_users,user.active_users_ios,user.active_users_android]
                args.append(arg)
                if i%100 == 0 or i == len(_users):
                    self.insert_many(sql, args)
                    args = []
                    self.end()

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


    def update_users(self,_users):
        if (_users == None):
            pass
        else:
            db_name = 'hbgj_activeusers_weekly'
            sql="update hbgj_activeusers_weekly set active_users=%s,active_users_ios=%s,active_users_android=%s,updatetime=now() where  DATE_FORMAT(str_to_date(s_day,'%%Y-%%m-%%d'),'%%Y%%m%%d')=DATE_FORMAT(str_to_date(%s,'%%Y-%%m-%%d'),'%%Y%%m%%d')"
            args = []
            for user in _users:
                arg = [user.active_users,user.active_users_ios,user.active_users_android,user.s_day]
                self.update(sql,arg)
                self.end()

class ActiveusersMonthly(Mysql):
    def __init__(self):
        Mysql.__init__(self)

    def insert_users(self,_users):
        if (_users==None) or (len(_users)<=0):
            pass
        else:
            db_name='hbgj_activeusers_monthly'
            sql='insert into '+db_name+' (s_day,active_users,active_users_ios,active_users_android,createtime,updatetime)'\
                                         'values (%s, %s, %s, %s,now(), now())'
            args = []
            i = 0
            for user in _users:
                i += 1
                arg = [user.s_day,user.active_users,user.active_users_ios,user.active_users_android]
                args.append(arg)
                if i%100 == 0 or i == len(_users):
                    self.insert_many(sql, args)
                    args = []
                    self.end()

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


    def update_users(self,_users):
        if (_users == None):
            pass
        else:
            db_name = 'hbgj_activeusers_monthly'
            sql="update hbgj_activeusers_monthly set active_users=%s,active_users_ios=%s,active_users_android=%s,updatetime=now() where  DATE_FORMAT(str_to_date(s_day,'%%Y-%%m-%%d'),'%%Y%%m%%d')=DATE_FORMAT(str_to_date(%s,'%%Y-%%m-%%d'),'%%Y%%m%%d')"
            args = []
            for user in _users:
                arg = [user.active_users,user.active_users_ios,user.active_users_android,user.s_day]
                self.update(sql,arg)
                self.end()