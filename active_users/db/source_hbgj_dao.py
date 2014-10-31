__author__ = 'Administrator'
import cx_Oracle
from domain import hbgj_new_users
from domain import hbgj_active_users
def oracle_con():
    ip = '58.83.130.79'
    port = 1521
    SID = 'ora9i'
    dsn_tns = cx_Oracle.makedsn(ip, port, SID)
    db = cx_Oracle.connect('et', 'atet501', dsn_tns)
    cursor = db.cursor()
    return cursor


def hbgj_new_user():
    # sql="select distinct to_char(createtime,'yyyy-mm-dd') s_day,count(distinct md5) user_num from DEVICE_USER_LOG group by to_char(createtime,'yyyy-mm-dd') order by to_char(createtime,'yyyy-mm-dd')"

    sql2="select distinct to_char(USER_LOGINDATE,'yyyy-mm-dd') s_day,count(distinct user_id) from HBZJ_USER where USER_LOGINDATE>=to_date('2014-09-04', 'yyyy-mm-dd') group by to_char(USER_LOGINDATE,'yyyy-mm-dd')"
    sql_os="select distinct to_char(USER_LOGINDATE,'yyyy-mm-dd') s_day,count(distinct user_id),sum(case when USER_CHANNEL LIKE '%91ZS%' or USER_CHANNEL LIKE '%appstore%' or USER_CHANNEL LIKE '%juwan%' or USER_CHANNEL LIKE '%91PGZS%' or USER_CHANNEL LIKE '%kuaiyong%' or USER_CHANNEL LIKE '%TBT%' or USER_CHANNEL LIKE '%PPZS%' then 1 else 0 end ) ios_activeusers from HBZJ_USER where USER_LOGINDATE>=to_date('2014-08-14', 'yyyy-mm-dd') group by to_char(USER_LOGINDATE,'yyyy-mm-dd')"
    cursor = oracle_con()
    cursor.execute(sql_os)
    result=cursor.fetchall()
    users=[]
    if not result:
        return  False
    for row in result:
        user = hbgj_new_users.New_users()
        user.s_day = row[0]
        user.new_users = row[1]
        user.new_users_ios = row[2]
        # t=row[1]-row[2]
        user.new_users_android=row[1]-row[2]
        users.append(user)
        # print user.s_day,user.new_users
    return users

def hbgj_active_user_daily():
    sql="select distinct to_char(createtime,'yyyy-mm-dd') s_day,count(distinct md5) from ACTIVE_USER_LOG where createtime>=to_date('2014-09-04', 'yyyy-mm-dd') group by to_char(createtime,'yyyy-mm-dd') order by  to_char(createtime,'yyyy-mm-dd')"
    sql_os="select distinct to_char(createtime,'yyyy-mm-dd') s_day,count(distinct md5),sum(case when p LIKE '%91ZS%' or p LIKE '%appstore%' or p LIKE '%juwan%' or p LIKE '%91PGZS%' or p LIKE '%kuaiyong%' or p LIKE '%TBT%' or p LIKE '%PPZS%' then 1 else 0 end ) ios_activeusers from ACTIVE_USER_LOG where createtime>=to_date('2014-08-18', 'yyyy-mm-dd') group by to_char(createtime,'yyyy-mm-dd') order by  to_char(createtime,'yyyy-mm-dd')"
    cursor = oracle_con()
    cursor.execute(sql_os)
    result=cursor.fetchall()
    users=[]
    if not result:
        return  False
    for row in result:
        user = hbgj_active_users.Active_users()
        user.s_day = row[0]
        user.active_users = row[1]
        user.active_users_ios=row[2]
        user.active_users_android=row[1]-row[2]
        users.append(user)
    return users

def hbgj_active_user_weekly():
    sql="select to_char(TRUNC(createtime,'IW'),'yyyy-mm-dd') s_day,count(distinct userid) active_users from ACTIVE_USER_LOG where createtime>=to_date('2014-08-18', 'yyyy-mm-dd') group by to_char(TRUNC(createtime,'IW'),'yyyy-mm-dd')"
    sql_os="select to_char(TRUNC(createtime,'IW'),'yyyy-mm-dd') s_day,count(distinct userid) active_users,count(distinct case when p LIKE '%91ZS%' or p LIKE '%appstore%' or p LIKE '%juwan%' or p LIKE '%91PGZS%' or p LIKE '%kuaiyong%' or p LIKE '%TBT%' or p LIKE '%PPZS%' then userid else null end ) active_users_ios from ACTIVE_USER_LOG where createtime>=to_date('2014-08-18', 'yyyy-mm-dd') group by to_char(TRUNC(createtime,'IW'),'yyyy-mm-dd')"
    cursor = oracle_con()
    cursor.execute(sql_os)
    result=cursor.fetchall()
    users=[]
    if not result:
        return  False
    for row in result:
        user = hbgj_active_users.Active_users()
        user.s_day = row[0]
        user.active_users = row[1]
        user.active_users_ios = row[2]
        user.active_users_android = row[1]-row[2]
        users.append(user)
    return users

def hbgj_active_user_monthly():
    sql="select to_char(trunc(createtime,'mm'),'yyyy-mm-dd') s_day,count(distinct userid) active_users from ACTIVE_USER_LOG where createtime>=to_date('2014-09-01', 'yyyy-mm-dd') group by to_char(trunc(createtime,'mm'),'yyyy-mm-dd')"
    sql_os="select to_char(trunc(createtime,'mm'),'yyyy-mm-dd') s_day,count(distinct userid) active_users,count(distinct case when p LIKE '%91ZS%' or p LIKE '%appstore%' or p LIKE '%juwan%' or p LIKE '%91PGZS%' or p LIKE '%kuaiyong%' or p LIKE '%TBT%' or p LIKE '%PPZS%' then userid else null end ) active_users_ios from ACTIVE_USER_LOG where createtime>=to_date('2014-09-01', 'yyyy-mm-dd') group by to_char(trunc(createtime,'mm'),'yyyy-mm-dd')"
    cursor = oracle_con()
    cursor.execute(sql_os)
    result=cursor.fetchall()
    users=[]
    if not result:
        return  False
    for row in result:
        user = hbgj_active_users.Active_users()
        user.s_day = row[0]
        user.active_users = row[1]
        user.active_users_ios = row[2]
        user.active_users_android = row[1]-row[2]
        users.append(user)
    return users
    pass


def test():
    # new_users=hbgj_new_user()
    # for user in new_users:
    #     print user.s_day,user.new_users,user.new_users_ios,user.new_users_android

    # active_users=hbgj_active_user_daily()
    # active_users=hbgj_active_user_weekly()
    active_users=hbgj_active_user_monthly()
    for user in active_users:
        print user.s_day,user.active_users,user.active_users_ios,user.active_users_android

    # new_users=hbgj_new_user()
    # for user in new_users:
    #     print user.s_day,user.new_users
# test()





