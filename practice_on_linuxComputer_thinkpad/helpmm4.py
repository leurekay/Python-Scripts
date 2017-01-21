#_*_coding=utf-8_*_
import urllib
import urllib2
import cookielib
import requests
from bs4 import BeautifulSoup
import re

import smtplib
from email.mime.text import MIMEText
from email.header import Header

import time
import datetime
import random

today=datetime.date.today()
date=today.strftime('%Y/%m/%d')

sender ='2528485257@qq.com'
receiver='1552198088@qq.com'
#receiver='798423285@qq.com'
subject = date
smtpserver = 'smtp.qq.com'
username = '2528485257@qq.com'
password = '3.1415926535'

cookie=cookielib.CookieJar()
hander=urllib2.HTTPCookieProcessor(cookie)
opener=urllib2.build_opener(hander)
urllib2.install_opener(opener)

sites=['30','60','43','106']
items=['0','2221','2220','211','213','215','218','812']

sitess=['gc','ls','nh','jn']
itemss=['AQI','PM2.5','PM10','SO2','NO2','CO','O3','O3(8)']
def sp(x,y):
    url='http://222.190.111.117:8023/Home/GetDataBySiteItem'
    postdata={
            'site':x,
            'item':y
            }  
    postdata=urllib.urlencode(postdata)
    req=urllib2.Request(url,data=postdata)
    login_r=opener.open(req)
    s=str(login_r.read())
    
    a=re.findall(r'\\u003cset value=\\"(.*?)\\" /\\u003e\\r\\n',s)
    b=' '.join(a)
    return b
    print b
    print len(b)
    time.sleep(1.23)

def allnum():
    site_val=['','','','']
    for i in range(0,4):
        site_val[i]=sitess[i]+': \n'
        for j in range(0,8):
           site_val[i]=site_val[i]+itemss[j]+' : '+sp(sites[i],items[j])+'\n'
    last=site_val[0]+'\n'+site_val[1]+'\n'+site_val[2]+'\n'+site_val[3]
    return last
    print last

while 1:
   
    msg = MIMEText(allnum(),'plain','utf-8')#中文需参数‘utf-8’，单字节字符不需要
    msg['Subject'] = Header(subject, 'utf-8')
    smtp = smtplib.SMTP()
    smtp.connect('smtp.qq.com')
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
    time.sleep(3600)
    
