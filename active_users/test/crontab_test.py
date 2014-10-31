__author__ = 'Administrator'
import datetime
now_time = str(datetime.datetime.now())

print now_time
# fout=open("test.txt","wt")
output_txt=open("test.txt",'a')
output_txt.write(now_time+ '\n')
output_txt.close()

