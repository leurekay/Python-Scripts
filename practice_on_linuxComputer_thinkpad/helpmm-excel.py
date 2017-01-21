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
import xlwt

cookie=cookielib.CookieJar()
hander=urllib2.HTTPCookieProcessor(cookie)
opener=urllib2.build_opener(hander)
urllib2.install_opener(opener)

sites=['30','60','43','106']
items=['0','2221','2220','211','213','215','218','812']
sitess=['高淳','溧水','六合','江宁']
itemss=['AQI','PM2.5','PM10','SO2','NO2','CO','O3','O3(8)']

g=time.localtime()
now=g.tm_hour
date=str(g.tm_mon)+'-'+str(g.tm_mday)+'-'+str(g.tm_hour)+'-'+str(g.tm_min)

def sp(x,y):
    url='http://222.190.111.117:8023/Home/GetDataBySiteItem'
    postdata={
            'site':sites[x],
            'item':items[y]
            }  
    postdata=urllib.urlencode(postdata)
    req=urllib2.Request(url,data=postdata)
    login_r=opener.open(req)
    s=str(login_r.read())
    a=re.findall(r'\\u003cset value=\\"(.*?)\\" /\\u003e\\r\\n',s)
    b=' '.join(a)
    #print a
    
    a=[itemss[y]]+a
    print len(a)
    return a
    time.sleep(1.23)


def wrcol(m,n):
    num=sp(m,n)
    for r in range(len(num)):       
        table.write((r+m*len(num)),j+2,num[r])
        if n==0 :         
            if r>0 :
                table.write((r+m*len(num)),j+1,sitess[m].decode('utf-8'))
                table.write((r+m*len(num)),j,str(now-len(num)+r+1)+':00')
            
f=xlwt.Workbook()
table=f.add_sheet('001')

for i in range(4):
    for j in range(8):
        wrcol(i,j)
        
f.save(date+'.xls')
    
        
    
