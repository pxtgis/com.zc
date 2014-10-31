#coding=utf-8
__author__ = 'zhangchao'
# 获取每天要更新的数据，为插入数据做准备
from source_gtgj_mysql import *
import sys
sys.path.append('..')
from domain import gtgj_consumers
from util import dateutil


class ConsumersDailyDao(Mysql):
    def __init__(self):
        Mysql.__init__(self,dbtype='gtgj')

    def get_consumers(self):
        # sql需要更改！！！！
        # sql_gtgj102="select CONCAT(YEAR(create_time),'-',MONTH(create_time),'-',  DAY(create_time)) s_day,count(*) order_num,sum(ticket_count) ticket_num,count(DISTINCT uid) user_num,sum(amount) amount from user_order where i_status=3 GROUP BY s_day order by create_time"
        sql="select date_format(create_time,'%Y-%m-%d') s_day,count(DISTINCT uid) consumers," \
            "count(distinct case when p_info LIKE '%ios%' then uid else null end ) consumers_ios," \
            "count(distinct case when p_info LIKE '%android%' then uid else null end ) consumers_android " \
            "from ( " \
            "select create_time,uid,p_info "\
            "from user_order_history "\
            "where i_status=3 and DATE_FORMAT(create_time,'%Y%m%d')>='20140616' "\
            "UNION "\
            "select create_time,uid,p_info "\
            "from user_order "\
            "where i_status=3 "\
            ") as A "\
            "group by s_day "

        # arg = [_today]
        # result = self.get_all(sql, arg)
        result=self.get_all(sql)
        consumers = []
        if not result:
            return False
        for row in result:
            # print row
            consumer = gtgj_consumers.Consumers()
            consumer.s_day = row['s_day']
            consumer.consumers = row['consumers']
            consumer.consumers_ios = row['consumers_ios']
            consumer.consumers_android = row['consumers']-row['consumers_ios']
            consumers.append(consumer)
        return consumers

class ConsumersWeeklyDao(Mysql):
    def __init__(self):
        Mysql.__init__(self,dbtype='gtgj')

    def get_consumers(self):
        # sql需要更改！！！！
        # sql_gtgj102="select CONCAT(YEAR(create_time),'-',MONTH(create_time),'-',  DAY(create_time)) s_day,count(*) order_num,sum(ticket_count) ticket_num,count(DISTINCT uid) user_num,sum(amount) amount from user_order where i_status=3 GROUP BY s_day order by create_time"
        sql="select date_format(subdate(create_time,date_format(create_time,'%w')-1),'%Y-%m-%d') s_day,count(DISTINCT uid) consumers," \
            "count(distinct case when p_info LIKE '%ios%' then uid else null end ) consumers_ios," \
            "count(distinct case when p_info LIKE '%android%' then uid else null end ) consumers_android " \
            "from ( " \
            "select create_time,uid,p_info "\
            "from user_order_history "\
            "where i_status=3 and DATE_FORMAT(create_time,'%Y%m%d')>='20140727' "\
            "UNION "\
            "select create_time,uid,p_info "\
            "from user_order "\
            "where i_status=3 "\
            ") as A "\
            "group by s_day "

        # arg = [_today]
        # result = self.get_all(sql, arg)
        result=self.get_all(sql)
        consumers = []
        if not result:
            return False
        for row in result:
            # print row
            consumer = gtgj_consumers.Consumers()
            consumer.s_day = row['s_day']
            consumer.consumers = row['consumers']
            consumer.consumers_ios = row['consumers_ios']
            consumer.consumers_android = row['consumers']-row['consumers_ios']
            consumers.append(consumer)
        return consumers


class ConsumersMonthlyDao(Mysql):
    def __init__(self):
        Mysql.__init__(self,dbtype='gtgj')

    def get_consumers(self):
        # sql需要更改！！！！
        # sql_gtgj102="select CONCAT(YEAR(create_time),'-',MONTH(create_time),'-',  DAY(create_time)) s_day,count(*) order_num,sum(ticket_count) ticket_num,count(DISTINCT uid) user_num,sum(amount) amount from user_order where i_status=3 GROUP BY s_day order by create_time"
        sql="select DATE_FORMAT(str_to_date(CONCAT(YEAR(create_time),'-',MONTH(create_time),'-01'),'%Y-%m-%d'),'%Y-%m-%d') s_day,count(DISTINCT uid) consumers, " \
            "count(distinct case when p_info LIKE '%ios%' then uid else null end ) consumers_ios," \
            "count(distinct case when p_info LIKE '%android%' then uid else null end ) consumers_android " \
            "from ( " \
            "select create_time,uid,p_info "\
            "from user_order_history "\
            "where i_status=3 and DATE_FORMAT(create_time,'%Y%m%d')>='20140601' "\
            "UNION "\
            "select create_time,uid,p_info "\
            "from user_order "\
            "where i_status=3 "\
            ") as A "\
            "group by s_day "
        # arg = [_today]
        # result = self.get_all(sql, arg)
        result=self.get_all(sql)
        consumers = []
        if not result:
            return False
        for row in result:
            # print row
            consumer = gtgj_consumers.Consumers()
            consumer.s_day = row['s_day']
            consumer.consumers = row['consumers']
            consumer.consumers_ios = row['consumers_ios']
            consumer.consumers_android = row['consumers']-row['consumers_ios']
            consumers.append(consumer)
        return consumers



def test_daily():
    today1=dateutil.DateUtil.getToday()
    test1=ConsumersDailyDao()
    print(test1._type)
    results=test1.get_consumers()
    # print(results)
    for row in results:
        print(row.s_day,row.consumers,row.consumers_ios,row.consumers_android,row.consumers_ios+row.consumers_android)


def test_weekly():
    today1=dateutil.DateUtil.getToday()
    test1=ConsumersWeeklyDao()
    print(test1._type)
    results=test1.get_consumers()
    # print(results)
    for row in results:
        print(row.s_day,row.consumers,row.consumers_ios,row.consumers_android,row.consumers_ios+row.consumers_android)


def test_monthly():
    today1=dateutil.DateUtil.getToday()
    test1=ConsumersMonthlyDao()
    print(test1._type)
    results=test1.get_consumers()
    # print(results)
    for row in results:
        print(row.s_day,row.consumers,row.consumers_ios,row.consumers_android,row.consumers_ios+row.consumers_android)
if __name__ == '__main__':
    test_daily()
    # test_weekly()
    # test_monthly()
    # print("OK")