#coding: utf-8
import urllib
from bs4 import BeautifulSoup
import re

import time
import random

import smtplib
from email.mime.text import MIMEText
from email.header import Header
 
sender ='2528485257@qq.com'
receiver ='798423285@qq.com'
subject = '神秘数字．．．．'
smtpserver = 'smtp.qq.com'
username = '2528485257@qq.com'
password = '3.1415926535'

def getdata():
    url='http://www.zq12369.com/?city=%E5%8D%97%E4%BA%AC&tab=city'
    html=urllib.urlopen(url)
    bs_obj=BeautifulSoup(html,"html.parser")
    st=str(bs_obj)
    aqi=re.findall('<div class="aqi">(.*?)</div>',st)
    first=re.findall('div class="pdate">(.*?)</div>',st)
    a=re.findall('<div class="item bglevel[0-9]">(.*?)</div>',st)
    b=re.findall('"value">(.*?)</div>',st)
    return first[0].decode('utf-8')+str(b)
def send():
    smtp = smtplib.SMTP()
    smtp.connect('smtp.qq.com')
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()

while 1:
    delay=random.randrange(45,60)
    msg = MIMEText(getdata()+'\n'+'\n'+str(delay)+u'分钟后，你将再次收到提示', 'plain', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    send()
    time.sleep(delay)
