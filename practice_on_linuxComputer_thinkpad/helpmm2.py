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
 
sender ='2528485257@qq.com'
receiver ='1552198088@qq.com'
subject = 'hahahaha'
smtpserver = 'smtp.qq.com'
username = '2528485257@qq.com'
password = '3.1415926535'
 


cookie=cookielib.CookieJar()
hander=urllib2.HTTPCookieProcessor(cookie)
opener=urllib2.build_opener(hander)
urllib2.install_opener(opener)
    
    
    
url='http://222.190.111.117:8023/Home/GetDataBySiteItem'
postdata={
'site':'106',
'item':'812'
}  
postdata=urllib.urlencode(postdata)
req=urllib2.Request(url,data=postdata)
login_r=opener.open(req)
s=str(login_r.read())
b=re.findall(r'"CalcIndex":{"Value":(.*?),"Index":',s)
print b[0]
msg = MIMEText(str(b[0]),'plain','utf-8')#中文需参数‘utf-8’，单字节字符不需要
msg['Subject'] = Header(subject, 'utf-8')


while 1:
    
    smtp = smtplib.SMTP()
    smtp.connect('smtp.qq.com')
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
    time.sleep(20)

  

   
