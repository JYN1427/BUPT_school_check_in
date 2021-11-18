# -*- coding:utf-8 -*-
import requests
import time
import datetime
import threading

from LeetCode.Selenium.myclock import Clock
from LeetCode.Selenium.sendemail import send_email

# ("user", "username", "passwd", "UUkey", "form_data"),
user_list = [
    (["张三", "...@qq.com"], "...", "...", "UUkey=...; ", ['ismoved=0&jhfjr......ym=0&sfjzdezxgym=0&jcjg=&date=', '&uid=.....jrsfqzfy=']),
    (["李四", "...@qq.com"], "...", "...", "UUkey=...; ", [])
]

def task(u, us, ps, ww, fd):
    print(u[0] + "! 该打卡了！")
    c = Clock(us, ps, ww, fd)
    if c.start():
        send_email(u[1])
        print(u[0] + "，您已打卡完毕：")
        print(datetime.datetime.now())
        print('-----------------------------\n')



def multi_clock():
    for u, us, ps, ww, fd in user_list[:1]:
        t = threading.Thread(target=task, args=(u, us, ps, ww, fd))
        t.start()

if __name__ == '__main__':
    multi_clock()