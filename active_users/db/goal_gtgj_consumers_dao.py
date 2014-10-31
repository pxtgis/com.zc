__author__ = 'Administrator'
from goal_mysql import *
import sys
sys.path.append('..')
from domain import gtgj_consumers
from util import dateutil

class ConsumersDaily(Mysql):
    def __init__(self):
        Mysql.__init__(self)

    def insert_users(self,_users):
        if (_users==None) or (len(_users)<=0):
            pass
        else:
            db_name='gtgj_consumers_daily'
            sql='insert into '+db_name+' (s_day,consumers,consumers_ios,consumers_android,createtime,updatetime)'\
                                         'values (%s, %s, %s, %s, now(), now())'
            args = []
            i = 0
            for user in _users:
                i += 1
                arg = [user.s_day,user.consumers,user.consumers_ios,user.consumers_android]
                args.append(arg)
                if i%100 == 0 or i == len(_users):
                    self.insert_many(sql, args)
                    args = []
                    self.end()

    def get_user(self,_day):
        sql="select s_day,consumers,consumers_ios,consumers_android from gtgj_consumers_daily where DATE_FORMAT(str_to_date(s_day,'%%Y-%%m-%%d'),'%%Y%%m%%d')=DATE_FORMAT(str_to_date(%s,'%%Y-%%m-%%d'),'%%Y%%m%%d')"
        arg=[_day]
        result=self.get_all(sql,arg)
        users=[]
        if not result:
            return  False
        for row in result:
            user=gtgj_consumers.Consumers()
            user.s_day = row['s_day']
            user.consumers = row['consumers']
            user.consumers_ios = row['consumers_ios']
            user.consumers_android = row['consumers_android']
            users.append(user)
        return users


    def update_users(self,_users):
        if (_users == None):
            pass
        else:
            db_name = 'gtgj_consumers_daily'
            sql="update gtgj_consumers_daily set consumers=%s,consumers_ios=%s,consumers_android=%s,updatetime=now() where  DATE_FORMAT(str_to_date(s_day,'%%Y-%%m-%%d'),'%%Y%%m%%d')=DATE_FORMAT(str_to_date(%s,'%%Y-%%m-%%d'),'%%Y%%m%%d')"
            args = []
            for user in _users:
                arg = [user.consumers,user.consumers_ios,user.consumers_android,user.s_day]
                self.update(sql,arg)
                self.end()

class ConsumersWeekly(Mysql):
    def __init__(self):
        Mysql.__init__(self)

    def insert_users(self,_users):
        if (_users==None) or (len(_users)<=0):
            pass
        else:
            db_name='gtgj_consumers_weekly'
            sql='insert into '+db_name+' (s_day,consumers,consumers_ios,consumers_android,createtime,updatetime)'\
                                         'values (%s, %s, %s, %s, now(), now())'
            args = []
            i = 0
            for user in _users:
                i += 1
                arg = [user.s_day,user.consumers,user.consumers_ios,user.consumers_android]
                args.append(arg)
                if i%100 == 0 or i == len(_users):
                    self.insert_many(sql, args)
                    args = []
                    self.end()

    def get_user(self,_day):
        sql="select s_day,consumers,consumers_ios,consumers_android from gtgj_consumers_weekly where DATE_FORMAT(str_to_date(s_day,'%%Y-%%m-%%d'),'%%Y%%m%%d')=DATE_FORMAT(str_to_date(%s,'%%Y-%%m-%%d'),'%%Y%%m%%d')"
        arg=[_day]
        result=self.get_all(sql,arg)
        users=[]
        if not result:
            return  False
        for row in result:
            user=gtgj_consumers.Consumers()
            user.s_day = row['s_day']
            user.consumers = row['consumers']
            user.consumers_ios = row['consumers_ios']
            user.consumers_android = row['consumers_android']
            users.append(user)
        return users


    def update_users(self,_users):
        if (_users == None):
            pass
        else:
            db_name = 'gtgj_consumers_weekly'
            sql="update gtgj_consumers_weekly set consumers=%s,consumers_ios=%s,consumers_android=%s,updatetime=now() where  DATE_FORMAT(str_to_date(s_day,'%%Y-%%m-%%d'),'%%Y%%m%%d')=DATE_FORMAT(str_to_date(%s,'%%Y-%%m-%%d'),'%%Y%%m%%d')"
            args = []
            for user in _users:
                arg = [user.consumers,user.consumers_ios,user.consumers_android,user.s_day]
                self.update(sql,arg)
                self.end()

class ConsumersMonthly(Mysql):
    def __init__(self):
        Mysql.__init__(self)

    def insert_users(self,_users):
        if (_users==None) or (len(_users)<=0):
            pass
        else:
            db_name='gtgj_consumers_monthly'
            sql='insert into '+db_name+' (s_day,consumers,consumers_ios,consumers_android,createtime,updatetime)'\
                                         'values (%s, %s, %s, %s, now(), now())'
            args = []
            i = 0
            for user in _users:
                i += 1
                arg = [user.s_day,user.consumers,user.consumers_ios,user.consumers_android]
                args.append(arg)
                if i%100 == 0 or i == len(_users):
                    self.insert_many(sql, args)
                    args = []
                    self.end()

    def get_user(self,_day):
        sql="select s_day,consumers,consumers_ios,consumers_android from gtgj_consumers_monthly where DATE_FORMAT(str_to_date(s_day,'%%Y-%%m-%%d'),'%%Y%%m%%d')=DATE_FORMAT(str_to_date(%s,'%%Y-%%m-%%d'),'%%Y%%m%%d')"
        arg=[_day]
        result=self.get_all(sql,arg)
        users=[]
        if not result:
            return  False
        for row in result:
            user=gtgj_consumers.Consumers()
            user.s_day = row['s_day']
            user.consumers = row['consumers']
            user.consumers_ios = row['consumers_ios']
            user.consumers_android = row['consumers_android']
            users.append(user)
        return users


    def update_users(self,_users):
        if (_users == None):
            pass
        else:
            db_name = 'gtgj_consumers_monthly'
            sql="update gtgj_consumers_monthly set consumers=%s,consumers_ios=%s,consumers_android=%s,updatetime=now() where  DATE_FORMAT(str_to_date(s_day,'%%Y-%%m-%%d'),'%%Y%%m%%d')=DATE_FORMAT(str_to_date(%s,'%%Y-%%m-%%d'),'%%Y%%m%%d')"
            args = []
            for user in _users:
                arg = [user.consumers,user.consumers_ios,user.consumers_android,user.s_day]
                self.update(sql,arg)
                self.end()


