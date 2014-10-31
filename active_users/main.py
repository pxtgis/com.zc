#coding=utf-8
###本程序每天定时运行
# 用来更新高铁管家的活跃用户数、新增用户数、订单数、订票数、交易额等数据

__author__ = 'zhangchao'
from service import hbgj_activeusers_service
from service import hbgj_newusers_service
from service import gtgj_activeusers_service
from service import gtgj_consumer_service
from service import gtgj_newusers_service
import sys
import datetime
sys.path.append('..')

def main():

    try:
        print("hbgj_activeusers_daily")
        hbgj_activeusers_service.DailyMain()
    except Exception as e:
        print e

    try:
        print("hbgj_activeusers_weekly")
        hbgj_activeusers_service.WeeklyMain()
        pass
    except Exception as e:
        print e

    try:
        print("hbgj_activeusers_Monthly")
        hbgj_activeusers_service.MonthlyMain()
        pass
    except Exception as e:
        print e

    try:
        print("hbgj_newusers_Daily")
        hbgj_newusers_service.DailyMain()
        pass
    except Exception as e:
        print e

    try:
        print("gtgj_activeusers_Daily")
        gtgj_activeusers_service.DailyMain()
        pass
    except Exception as e:
        print e

    try:
        print("gtgj_activeusers_Weekly")
        gtgj_activeusers_service.WeeklyMain()
        pass
    except Exception as e:
        print e

    try:
        print("gtgj_activeusers_Monthly")
        gtgj_activeusers_service.MonthlyMain()
        pass
    except Exception as e:
        print e

    try:
        print("gtgj_consumer_Daily")
        gtgj_consumer_service.DailyMain()
        pass
    except Exception as e:
        print e

    try:
        print("gtgj_consumer_Weekly")
        gtgj_consumer_service.WeeklyMain()
        pass
    except Exception as e:
        print e

    try:
        print("gtgj_consumer_Monthly")
        gtgj_consumer_service.MonthlyMain()
        pass
    except Exception as e:
        print e
        return 1

    try:
        print("gtgj_newusers_Daily")
        gtgj_newusers_service.main()
        pass
    except Exception as e:
        print e
        return 1

main()


