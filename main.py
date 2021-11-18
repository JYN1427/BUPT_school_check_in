# -*- coding:utf-8 -*-
import requests
import time
import datetime
import threading

from LeetCode.Selenium.myclock import Clock
from LeetCode.Selenium.sendemail import send_email

# ("user", "username", "passwd", "UUkey", "form_data"),
user_list = [
    (["Ning哥", "1073967337@qq.com"], "2020140418", "08194219", "UUkey=795ce530ae3621971b228e92b27e0b47; ", ['ismoved=0&jhfjrq=&jhfjjtgj=&jhfjhbcc=&sfxk=0&xkqq=&szgj=&szcs=&zgfxdq=0&mjry=0&csmjry=0&ymjzxgqk=%E6%97%A9%E9%83%BD%E6%8E%A5%E7%A7%8D%E4%BA%86%EF%BC%8C%E7%BB%9F%E8%AE%A1%E8%AE%A4%E7%9C%9F%E7%82%B9%E8%A1%8C%E5%90%97%EF%BC%9F&xwxgymjzqk=3&tw=2&sfcxtz=0&sfjcbh=0&sfcxzysx=0&qksm=&sfyyjc=0&jcjgqr=0&remark=&address=%E5%8C%97%E4%BA%AC%E5%B8%82%E6%B5%B7%E6%B7%80%E5%8C%BA%E5%8C%97%E5%A4%AA%E5%B9%B3%E5%BA%84%E8%A1%97%E9%81%93%E5%8C%97%E4%BA%AC%E9%82%AE%E7%94%B5%E5%A4%A7%E5%AD%A6%E5%8C%97%E4%BA%AC%E9%82%AE%E7%94%B5%E5%A4%A7%E5%AD%A6%E6%B5%B7%E6%B7%80%E6%A0%A1%E5%8C%BA&geo_api_info=%7B%22type%22%3A%22complete%22%2C%22position%22%3A%7B%22Q%22%3A39.964914822049%2C%22R%22%3A116.357018500435%2C%22lng%22%3A116.357019%2C%22lat%22%3A39.964915%7D%2C%22location_type%22%3A%22html5%22%2C%22message%22%3A%22Get+ipLocation+failed.Get+geolocation+success.Convert+Success.Get+address+success.%22%2C%22accuracy%22%3A20.367%2C%22isConverted%22%3Atrue%2C%22status%22%3A1%2C%22addressComponent%22%3A%7B%22citycode%22%3A%22010%22%2C%22adcode%22%3A%22110108%22%2C%22businessAreas%22%3A%5B%7B%22name%22%3A%22%E5%8C%97%E4%B8%8B%E5%85%B3%22%2C%22id%22%3A%22110108%22%2C%22location%22%3A%7B%22Q%22%3A39.955976%2C%22R%22%3A116.33873%2C%22lng%22%3A116.33873%2C%22lat%22%3A39.955976%7D%7D%2C%7B%22name%22%3A%22%E5%B0%8F%E8%A5%BF%E5%A4%A9%22%2C%22id%22%3A%22110108%22%2C%22location%22%3A%7B%22Q%22%3A39.957147%2C%22R%22%3A116.364058%2C%22lng%22%3A116.364058%2C%22lat%22%3A39.957147%7D%7D%2C%7B%22name%22%3A%22%E8%A5%BF%E7%9B%B4%E9%97%A8%22%2C%22id%22%3A%22110102%22%2C%22location%22%3A%7B%22Q%22%3A39.942856%2C%22R%22%3A116.34666099999998%2C%22lng%22%3A116.346661%2C%22lat%22%3A39.942856%7D%7D%5D%2C%22neighborhoodType%22%3A%22%E7%A7%91%E6%95%99%E6%96%87%E5%8C%96%E6%9C%8D%E5%8A%A1%3B%E5%AD%A6%E6%A0%A1%3B%E9%AB%98%E7%AD%89%E9%99%A2%E6%A0%A1%22%2C%22neighborhood%22%3A%22%E5%8C%97%E4%BA%AC%E9%82%AE%E7%94%B5%E5%A4%A7%E5%AD%A6%22%2C%22building%22%3A%22%22%2C%22buildingType%22%3A%22%22%2C%22street%22%3A%22%E5%B8%88%E5%A4%A7%E5%8C%97%E8%B7%AF%22%2C%22streetNumber%22%3A%227%E5%8F%B7%22%2C%22country%22%3A%22%E4%B8%AD%E5%9B%BD%22%2C%22province%22%3A%22%E5%8C%97%E4%BA%AC%E5%B8%82%22%2C%22city%22%3A%22%22%2C%22district%22%3A%22%E6%B5%B7%E6%B7%80%E5%8C%BA%22%2C%22township%22%3A%22%E5%8C%97%E5%A4%AA%E5%B9%B3%E5%BA%84%E8%A1%97%E9%81%93%22%7D%2C%22formattedAddress%22%3A%22%E5%8C%97%E4%BA%AC%E5%B8%82%E6%B5%B7%E6%B7%80%E5%8C%BA%E5%8C%97%E5%A4%AA%E5%B9%B3%E5%BA%84%E8%A1%97%E9%81%93%E5%8C%97%E4%BA%AC%E9%82%AE%E7%94%B5%E5%A4%A7%E5%AD%A6%E5%8C%97%E4%BA%AC%E9%82%AE%E7%94%B5%E5%A4%A7%E5%AD%A6%E6%B5%B7%E6%B7%80%E6%A0%A1%E5%8C%BA%22%2C%22roads%22%3A%5B%5D%2C%22crosses%22%3A%5B%5D%2C%22pois%22%3A%5B%5D%2C%22info%22%3A%22SUCCESS%22%7D&area=%E5%8C%97%E4%BA%AC%E5%B8%82++%E6%B5%B7%E6%B7%80%E5%8C%BA&province=%E5%8C%97%E4%BA%AC%E5%B8%82&city=%E5%8C%97%E4%BA%AC%E5%B8%82&sfzx=1&sfjcwhry=0&sfjchbry=0&sfcyglq=0&gllx=&glksrq=&jcbhlx=&jcbhrq=&bztcyy=&sftjhb=0&sftjwh=0&sfsfbh=0&xjzd=&jcwhryfs=&jchbryfs=&szsqsfybl=0&sfygtjzzfj=0&gtjzzfjsj=&sfjzxgym=0&sfjzdezxgym=0&jcjg=&date=', '&uid=50442&created=1637031958&jcqzrq=&sfjcqz=&sfsqhzjkk=0&sqhzjkkys=&id=15144357&gwszdd=&sfyqjzgc=&jrsfqzys=&jrsfqzfy=']),
    (["老婆", "1211445287@qq.com"], "2020110538", "06133762", "UUkey=795ce530ae3621971b228e92b27e0b47", [])
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