__author__ = 'Administrator'
from goal_mysql import *
import sys
sys.path.append('..')
import flight_price_model
import datetime

class FlightPriceUpdate(Mysql):
    def __init__(self):
        Mysql.__init__(self)

    def insert_data(self,_data):
        if (_data==None) or (len(_data)<=0):
            pass
        else:
            db_name='filght_price_percent'
            sql='insert into '+db_name+' (flightnum,airlineno,hbgj_percent,xc_percent,qunar_percent,datatime)'\
                                         'values (%s, %s,%s,%s, %s, %s)'
            args = []
            i = 0
            for data in _data:
                i += 1
                arg = [data.flightnum,data.airlineno,data.hbgj_percent,data.xc_percent,data.qunar_percent,data.datatime]
                args.append(arg)
                if i%100 == 0 or i == len(_data):
                    self.insert_many(sql, args)
                    args = []
                    self.end()

    def get_data(self,_day):
        sql="select flightnum,airlineno,hbgj_percent,xc_percent,qunar_percent,datatime from filght_price_percent where DATE_FORMAT(str_to_date(s_day,'%%Y-%%m-%%d'),'%%Y%%m%%d')=DATE_FORMAT(str_to_date(%s,'%%Y-%%m-%%d'),'%%Y%%m%%d')"
        arg=[_day]
        result=self.get_all(sql,arg)
        datas=[]
        if not result:
            return  False
        for row in result:
            data=flight_price_model.Flight_price()

            data.flightnum = row['flightnum']
            data.airlineno = row['airlineno']
            data.hbgj_percent = row['hbgj_percent']
            data.xc_percent = row['xc_percent']
            data.qunar_percent = row['qunar_percent']
            data.datatime = row['datatime']
            datas.append(data)
        return datas



