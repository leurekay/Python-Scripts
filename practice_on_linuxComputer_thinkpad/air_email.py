# -*- coding: utf-8 -*-
import urllib
from bs4 import BeautifulSoup
import re

import time

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

from_addr ='2528485257@qq.com'
password = '3.1415926535'
to_addr ='798423285@qq.com'
smtp_server = 'smtp.qq.com'

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

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(( \
        Header(name, 'utf-8').encode(), \
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))
while 1:

    msg = MIMEText(getdata(), 'plain', 'utf-8')
    msg['From'] = _format_addr(u'雷锋 <%s>' % from_addr)
    msg['To'] = _format_addr(u'管理员 <%s>' % to_addr)
    msg['Subject'] = Header(u'神秘数字的背后，隐藏着不为人知的秘密．．．．', 'utf-8').encode()

    server = smtplib.SMTP(smtp_server, 25)
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()

    time.sleep(10)

