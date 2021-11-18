# -*- coding:utf-8 -*-
import smtplib
import time
from email.mime.text import MIMEText

def send_email(receiver):
    # 126 SMTP 邮箱服务器地址
    mail_host = 'smtp.126.com'

    # 126用户名和密码
    mail_user = 'jialaolao'
    # 密码(部分邮箱为授权码)
    mail_pass = 'WIZEJWMDVVEBKFVM'

    # 邮件发送方邮箱地址，接收方就是receiver
    sender = 'jialaolao@126.com'

    # 邮件内容设置
    now = time.strftime("%Y-%m-%d", time.localtime())
    content = '您于' + now + '已经完成打卡'
    message = MIMEText(_text=content, _subtype='plain', _charset='utf-8')

    # 邮件主题
    message['Subject'] = '打卡完成通告'

    # 发送方信息
    message['From'] = sender

    # 接受方信息
    message['To'] = receiver

    # 登录并发送邮件
    try:
        smtp_obj = smtplib.SMTP()
        # 连接到服务器, port25
        smtp_obj.connect(mail_host, 25)
        # 登录到服务器
        smtp_obj.login(mail_user, mail_pass)
        # 发送
        smtp_obj.sendmail(sender, receiver, message.as_string())
        print(message.as_string())
        # 退出
        smtp_obj.quit()
        print('success')
    except smtplib.SMTPException as e:
        print('error',e) # 打印错误
