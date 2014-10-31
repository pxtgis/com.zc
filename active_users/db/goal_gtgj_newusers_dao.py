__author__ = 'Administrator'
from goal_mysql import *
import sys
sys.path.append('..')
from domain import gtgj_newusers
from util import dateutil

class GoalGtgjNewusersDao(Mysql):
    def __init__(self):
        Mysql.__init__(self)

    def insert_users(self,_users):
        if (_users==None) or (len(_users)<=0):
            pass
        else:
            db_name='gtgj_newusers_daily'
            sql='insert into '+db_name+' (s_day,new_users,new_users_ios,new_users_android,createtime,updatetime)'\
                                         'values (%s, %s, %s, %s, now(), now())'
            args = []
            i = 0
            for user in _users:
                i += 1
                arg = [user.s_day,user.new_users,user.new_users_ios,user.new_users_android]
                args.append(arg)
                if i%100 == 0 or i == len(_users):
                    self.insert_many(sql, args)
                    args = []
                    self.end()

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


    def update_users(self,_users):
        if (_users == None):
            pass
        else:
            db_name = 'gtgj_newusers_daily'
            sql="update gtgj_newusers_daily set new_users=%s, new_users_ios=%s , new_users_android=%s , updatetime=now() where  DATE_FORMAT(str_to_date(s_day,'%%Y-%%m-%%d'),'%%Y%%m%%d')=DATE_FORMAT(str_to_date(%s,'%%Y-%%m-%%d'),'%%Y%%m%%d')"
            args = []
            # i = 0
            for user in _users:
                # i += 1
                arg = [user.new_users,user.new_users_ios,user.new_users_android,user.s_day]
                # args.append(arg)
                # if i%100 == 0 or i == len(orders):
                self.update(sql,arg)
                    # args = []
                self.end()



