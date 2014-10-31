-- 查询订单数和订票数
SELECT (
case
when '${time_state}'='1' then CONCAT(MONTH(TICKET_ORDERDETAIL.createtime),".",DAY(TICKET_ORDERDETAIL.createtime),',',case WHEN DAYOFWEEK
(createtime)=1 THEN 'Sun'
WHEN DAYOFWEEK(createtime)=2 THEN  'Mon'
WHEN DAYOFWEEK(createtime)=3  THEN 'Tue'
WHEN DAYOFWEEK(createtime)=4 THEN  'Wed'
WHEN DAYOFWEEK(createtime)=5  THEN 'Thur'
WHEN DAYOFWEEK(createtime)=6 THEN  'Fri'
else 'Sat' END,',',YEAR(TICKET_ORDERDETAIL.createtime))
when '${time_state}'='2' then CONCAT(case
when DAYOFWEEK(TICKET_ORDERDETAIL.createtime)=1 then DATE_FORMAT((DATE_SUB(TICKET_ORDERDETAIL.createtime,INTERVAL 6 DAY)),'%m.%d,Mon,%Y')
when DAYOFWEEK(TICKET_ORDERDETAIL.createtime)=2 then DATE_FORMAT((DATE_SUB(TICKET_ORDERDETAIL.createtime,INTERVAL 0 DAY)),'%m.%d,Mon,%Y')
when DAYOFWEEK(TICKET_ORDERDETAIL.createtime)=3 then DATE_FORMAT((DATE_SUB(TICKET_ORDERDETAIL.createtime,INTERVAL 1 DAY)),'%m.%d,Mon,%Y')
when DAYOFWEEK(TICKET_ORDERDETAIL.createtime)=4 then DATE_FORMAT((DATE_SUB(TICKET_ORDERDETAIL.createtime,INTERVAL 2 DAY)),'%m.%d,Mon,%Y')
when DAYOFWEEK(TICKET_ORDERDETAIL.createtime)=5 then DATE_FORMAT((DATE_SUB(TICKET_ORDERDETAIL.createtime,INTERVAL 3 DAY)),'%m.%d,Mon,%Y')
when DAYOFWEEK(TICKET_ORDERDETAIL.createtime)=6 then DATE_FORMAT((DATE_SUB(TICKET_ORDERDETAIL.createtime,INTERVAL 4 DAY)),'%m.%d,Mon,%Y')
when DAYOFWEEK(TICKET_ORDERDETAIL.createtime)=7 then DATE_FORMAT((DATE_SUB(TICKET_ORDERDETAIL.createtime,INTERVAL 5 DAY)),'%m.%d,Mon,%Y')
end)
when '${time_state}'='3' then CONCAT(MONTH(TICKET_ORDERDETAIL.createtime),',',YEAR(TICKET_ORDERDETAIL.createtime))
when '${time_state}'='4' then  CONCAT('Q',QUARTER(TICKET_ORDERDETAIL.createtime),',',YEAR(TICKET_ORDERDETAIL.createtime))
END) time,
count(ORDERID) ticket_num,
count(distinct ORDERID) order_num

from TICKET_ORDERDETAIL
where  ORDERID in
(
select ORDERID
from TICKET_ORDER
where
ORDERSTATUE not in (2,12,21,51,75)
and DATE_FORMAT(TICKET_ORDER.createtime,'%Y%m%d')>=DATE_FORMAT('${start_time}','%Y%m%d')
and DATE_FORMAT(TICKET_ORDER.createtime,'%Y%m%d')<=DATE_FORMAT('${end_time}','%Y%m%d')
and p LIKE '%gtgj%'
)

GROUP BY  time
order BY TICKET_ORDERDETAIL.createtime;
