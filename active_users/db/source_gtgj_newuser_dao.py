__author__ = 'zhangchao'
from source_gtgj_mysql import *
import sys
sys.path.append('..')
from domain import gtgj_newusers
from util import dateutil

class SourceUserDao(Mysql):
    def __init__(self):
        Mysql.__init__(self,dbtype='gtgj')

    def get_users(self):
        sql="SELECT s_day,sum(new_users) new_users,sum(active_users) active_users FROM global_statistics where DATE_FORMAT(str_to_date(s_day, '%Y-%m-%d'),'%Y%m%d')>='20140801' GROUP BY s_day"
        sql_os="SELECT s_day,sum(new_users) new_users,sum(case when source LIKE '%91ZS%' or source LIKE '%appstore%' or source LIKE '%juwan%' or source LIKE '%91PGZS%' or source LIKE '%kuaiyong%' or source LIKE '%TBT%' or source LIKE '%PPZS%' then new_users else 0 end) new_users_ios FROM global_statistics where DATE_FORMAT(str_to_date(s_day, '%Y-%m-%d'),'%Y%m%d')>='20140801' GROUP BY s_day"
        result=self.get_all(sql_os)
        users=[]
        if not result:
            return False
        for row in result:
            user= gtgj_newusers.User_statistics()
            user.s_day = row['s_day']
            user.new_users = row['new_users']
            user.new_users_ios=row['new_users_ios']
            user.new_users_android = row['new_users']-row['new_users_ios']
            users.append(user)
        return users
        pass

def test():
    test1=SourceUserDao()
    results=test1.get_users()
    # print(results)
    for row in results:
        print(row.s_day,row.new_users,row.new_users_ios,row.new_users_android)
    print()

if __name__ == '__main__':
    test()
    print("OK")



