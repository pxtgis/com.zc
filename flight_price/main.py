#
#coding=utf-8
__author__ = 'Administrator'

import pymongo

import conf
import flight_price_model
import goal_flight_price_dao


def mongodb_con(dbtype='local'):
    ##连接mongodb,获取查询结果,返回flight_price_model结构体的列表
    if dbtype=='local':
        con_local=pymongo.Connection(host="localhost",port=27017)
        db = con_local.test
        flight=db.flight.find()

    elif dbtype=='225':
        con_225=pymongo.Connection(host="182.92.194.225",port=27017)
        db = con_225.collectdata
        db.authenticate("readonly","read@hl123")
        flight=db.flight_price_percent.find()
    else:
        return None

    results=[]
    for i in flight:
        result=flight_price_model.Flight_price()
        result.flightnum=int(i['flightnum'])
        result.airlineno=str(i['airlineno'])
        result.hbgj_percent=int(i['hbgj_percent'])
        result.xc_percent=int(i['xc_percent'])
        result.qunar_percent=int(i['qunar_percent'])
        result.datatime=i['datatime']
        results.append(result)
    return results


def data_insert(_data):
    #插入数据
    t=goal_flight_price_dao.FlightPriceUpdate()
    t.insert_data(_data)

    pass


if __name__=="__main__":
    data=mongodb_con(dbtype="225")
    data_insert(data)
    # print t

    pass


