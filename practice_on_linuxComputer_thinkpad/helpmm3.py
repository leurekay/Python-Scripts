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

sender ='2528485257@qq.com'
receiver ='1552198088@qq.com'
subject = 'hahahaha'
smtpserver = 'smtp.qq.com'
username = '2528485257@qq.com'
password = '3.1415926535'

sites=['30','60','43','106']
items=['0','2221','2220','211','213','215','218','812']

sitess=['gc','ls','nh','jn']


    
    
def getdata():
    value=['','','','']
    for i in range(0,4):      
        value[i]=sitess[i]+':'
        for j in range(0,2):
            cookie=cookielib.CookieJar()
            hander=urllib2.HTTPCookieProcessor(cookie)
            opener=urllib2.build_opener(hander)
            urllib2.install_opener(opener)
       
            url='http://222.190.111.117:8023/Home/GetDataBySiteItem'
            postdata={
            'site':sites[i],
            'item':items[j]
            }  
            postdata=urllib.urlencode(postdata)
            req=urllib2.Request(url,data=postdata)
            login_r=opener.open(req)
            s=str(login_r.read())

            b=re.findall(r'":{"Value":(.*?),"Index":',s)
            time.sleep(1)
            value[i]=value[i]+b[0]+' '
            print value[i]
    

getdata()

        




