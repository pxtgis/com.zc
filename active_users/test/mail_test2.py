# -*- coding: utf-8 -*-
#导入smtplib和MIMEText
import smtplib
from email.mime.text import MIMEText
#要发给谁
mail_to="744996162@qq.com"
def send_mail(to_list,sub,content):
    #############
    #to_list为收件人
    #sub为邮件标题
    #content为邮件内容
    ###############
    #设置服务器，用户名、口令以及邮箱的后缀
    mail_host="smtp.qq.com"
    mail_user="744996162"
    mail_pass=""
    mail_postfix="qq.com"
    me=mail_user+"<"+mail_user+"@"+mail_postfix+">"
    msg = MIMEText(content)
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = to_list
    try:
        s = smtplib.SMTP()
        s.connect(mail_host)
        s.login(mail_user,mail_pass)
        s.sendmail(me, to_list, msg.as_string())
        s.close()
        return True
    except Exception as e:
        print(2)
        return False

def send_mail_admin(to_list,sub,content):
    #############
    #to_list为收件人
    #sub为邮件标题
    #content为邮件内容
    ###############
    #设置服务器，用户名、口令以及邮箱的后缀
    mail_host="smtp.qq.com"
    mail_user="744996162"
    mail_pass=""
    mail_postfix="qq.com"
    me=mail_user+"<"+mail_user+"@"+mail_postfix+">"
    msg = MIMEText(content)
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = to_list
    try:
        s = smtplib.SMTP()
        s.connect(mail_host)
        s.login(mail_user,mail_pass)
        s.sendmail(me, to_list, msg.as_string())
        s.close()
        return True
    except Exception as e:
        print(2)
        return False
if __name__ == "__main__":
    if send_mail(mail_to,"hello","this is python sent"):
        print("发送成功")
    else:
        send_mail_admin(mail_to,"邮件发送失败","邮件发送失败！！！")
        print("发送失败")

