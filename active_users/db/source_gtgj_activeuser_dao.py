__author__ = 'Administrator'
from source_gtgj_mysql import *
import sys
sys.path.append('..')
from active_users.domain import gtgj_active_users

class ActiveUserDao(Mysql):
    def __init__(self):
        Mysql.__init__(self,dbtype='gtgj')

    def get_users_daily(self):
        sql="SELECT s_day,sum(active_users) active_users FROM global_statistics where DATE_FORMAT(str_to_date(s_day, '%Y-%m-%d'),'%Y%m%d')>='20140801' GROUP BY s_day"
        sql_os="SELECT s_day,sum(active_users) active_users,sum(case when source LIKE '%91ZS%' or source LIKE '%appstore%' or source LIKE '%juwan%' or source LIKE '%91PGZS%' or source LIKE '%kuaiyong%' or source LIKE '%TBT%' or source LIKE '%PPZS%' then active_users else 0 end) active_users_ios FROM global_statistics where DATE_FORMAT(str_to_date(s_day, '%Y-%m-%d'),'%Y%m%d')>='20140917' GROUP BY s_day"
        result=self.get_all(sql_os)
        users=[]
        if not result:
            return False
        for row in result:
            user= gtgj_active_users.Active_users()
            user.s_day = row['s_day']
            user.active_users = row['active_users']
            user.active_users_ios=row['active_users_ios']
            user.active_users_android=row['active_users']-row['active_users_ios']
            users.append(user)
        return users

    def get_users_weekly(self):
        sql="SELECT s_day,sum(active_users) active_users FROM global_week_statistics where DATE_FORMAT(str_to_date(s_day, '%Y-%m-%d'),'%Y%m%d')>='20140818' GROUP BY s_day"
        sql_os="SELECT s_day,sum(active_users) active_users,sum(case when source LIKE '%91ZS%' or source LIKE '%appstore%' or source LIKE '%juwan%' or source LIKE '%91PGZS%' or source LIKE '%kuaiyong%' or source LIKE '%TBT%' or source LIKE '%PPZS%' then active_users else 0 end) active_users_ios FROM global_week_statistics where DATE_FORMAT(str_to_date(s_day, '%Y-%m-%d'),'%Y%m%d')>='20140818' GROUP BY s_day"
        result=self.get_all(sql_os)
        users=[]
        if not result:
            return False
            pass
        for row in result:
            user= gtgj_active_users.Active_users()
            user.s_day = row['s_day']
            user.active_users = row['active_users']
            user.active_users_ios=row['active_users_ios']
            user.active_users_android=row['active_users']-row['active_users_ios']
            users.append(user)
        return users

    def get_users_monthly(self):
        sql="SELECT s_day,sum(active_users) active_users FROM global_month_statistics where DATE_FORMAT(str_to_date(s_day, '%Y-%m-%d'),'%Y%m%d')>='20140818' GROUP BY s_day"
        sql_os="SELECT s_day,sum(active_users) active_users,sum(case when source LIKE '%91ZS%' or source LIKE '%appstore%' or source LIKE '%juwan%' or source LIKE '%91PGZS%' or source LIKE '%kuaiyong%' or source LIKE '%TBT%' or source LIKE '%PPZS%' then active_users else 0 end) active_users_ios FROM global_month_statistics where DATE_FORMAT(str_to_date(s_day, '%Y-%m-%d'),'%Y%m%d')>='20140801' GROUP BY s_day"
        result=self.get_all(sql_os)
        users=[]
        if not result:
            return False
        for row in result:
            user= gtgj_active_users.Active_users()
            user.s_day = row['s_day']
            user.active_users = row['active_users']
            user.active_users_ios=row['active_users_ios']
            user.active_users_android=row['active_users']-row['active_users_ios']
            users.append(user)
        return users

def test():
    test1=ActiveUserDao()
    # results=test1.get_users_daily()
    results=test1.get_users_weekly()
    # results=test1.get_users_monthly()
    print(results)
    for row in results:
        print(row.s_day,row.active_users,row.active_users_ios,row.active_users_android)
    print()

if __name__ == '__main__':
    test()
    # print("OK")
