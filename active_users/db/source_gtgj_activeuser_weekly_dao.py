__author__ = 'Administrator'
from source_gtgj_mysql import *
import sys
sys.path.append('..')
from domain import gtgj_active_users

class SourceUserDao(Mysql):
    def __init__(self):
        Mysql.__init__(self,dbtype='gtgj')

    def get_users(self):
        sql="SELECT s_day,sum(active_users) active_users FROM global_week_statistics where DATE_FORMAT(str_to_date(s_day, '%Y-%m-%d'),'%Y%m%d')>='20140818' GROUP BY s_day"
        result=self.get_all(sql)
        users=[]
        if not result:
            return False
        for row in result:
            user= gtgj_active_users.Active_users()
            user.s_day = row['s_day']
            user.active_users = row['active_users']
            users.append(user)
        return users
        pass

def test():
    test1=SourceUserDao()
    results=test1.get_users()
    # print(results)
    for row in results:
        print(row.s_day,row.active_users)
    print()

if __name__ == '__main__':
    test()
    # print("OK")
