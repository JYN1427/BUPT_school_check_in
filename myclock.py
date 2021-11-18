# -*- coding:utf-8 -*-
import requests
import time
import datetime

class Clock:
    def __init__(self, user, passwd, UUkey, save_datas):
        self.user = user
        self.passwd = passwd
        self.UUkey = UUkey
        self.eai_sess = ''
        self.save_datas = save_datas

    def get_eai_sess(self):
        # 获取cookie，可以去掉后缀?redirect=https%3A%2F%2Fapp.bupt.edu.cn%2Fncov%2Fwap%2Fdefault%2Findex
        url = "https://app.bupt.edu.cn/uc/wap/login"
        resp = requests.get(url)
        # print(resp.headers)
        # print(resp.text)
        self.eai_sess = resp.headers['Set-Cookie'].split(';')[0] # 形如eai-sess=k733fvre6h3hg8dklq5t5nc121
        return resp

    def log_in(self):
        # Login
        url2 = "https://app.bupt.edu.cn/uc/wap/login/check"
        data = "username="+self.user+"&password="+self.passwd
        headers = {
            "Host":"app.bupt.edu.cn",
            "Connection": "keep-alive",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "X-Requested-With": "XMLHttpRequest",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
            "Origin":"https://app.bupt.edu.cn",
            "Referer":"https://app.bupt.edu.cn/uc/wap/login",
            "Cookie":self.UUkey + self.eai_sess
        }
        resp = requests.post(url2,data=data,headers=headers)
        return resp

    def save_data(self):
        now = time.strftime("%Y%m%d", time.localtime())
        data = self.save_datas[0] + now + self.save_datas[1]
        url = "https://app.bupt.edu.cn/ncov/wap/default/save"
        headers = {
                "Host": "app.bupt.edu.cn",
                "Connection": "keep-alive",
                "Accept": "application/json, text/javascript, */*; q=0.01",
                "Accept-Language": "zh-CN,zh;q=0.9",
                "Accept-Encoding": "gzip, deflate, br",
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "X-Requested-With": "XMLHttpRequest",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
                "Origin": "https://app.bupt.edu.cn",
                "Content-Length": "3157",
                "Referer": "https://app.bupt.edu.cn/ncov/wap/default/index",
                "Cookie":self.UUkey + self.eai_sess
                }
        resp = requests.post(url=url, headers=headers, data=data)
        return resp

    def start(self):
        print("尝试获取Cookie：")
        print(datetime.datetime.now())
        code = self.get_eai_sess().status_code
        # print(type(code))
        if code != 200:
            print("获取失败")
            return

        print("尝试登录账号：")
        print(datetime.datetime.now())
        code = self.log_in().status_code
        if code != 200:
            print("登录失败")
            return

        print("提交打卡：")
        print(datetime.datetime.now())
        r = self.save_data()
        if r.status_code != 200:
            print("提交失败")
            return
        print("提交结果：")
        print(r.text)
        return True
