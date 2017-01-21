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
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import time
import datetime
import random
import xlwt


sender = '2528485257@qq.com'#发件人地址
receiver = '798423285@qq.com'#收件人地址
smtpserver = 'smtp.qq.com'#邮件服务器
username = '2528485257@qq.com'#用户名
password = '3.1415926535'#密码
smtp = smtplib.SMTP()

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

def h(x):
    if x>=0 :
        return 1
    else:
        return 0
    
def getnow():
    url='http://222.190.111.117:8023/Home/GetDataBySiteItem'
    data={
    'site':'106',
    'item':'812'
            }
    r=requests.post(url,data)
    t=r.text
    b0=re.findall(r'003ccategory name=\\"(.*?)\\" /\\',t)
    a0=re.findall(r'\\u003cset value=\\"(.*?)\\" /\\u003e\\r\\n',t)
    b1=' '.join(b0)
    b2=b1.encode('utf-8')
    b=b2.split(':00')
    b.remove('')
    t1=[]
    for i in range(len(b)):
        t1=t1+[int(b[i])]
    c=t1[len(t1)-1]
    return c

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
    a0=re.findall(r'\\u003cset value=\\"(.*?)\\" /\\u003e\\r\\n',s)
    b0=re.findall(r'003ccategory name=\\"(.*?)\\" /\\',s)
    c0=re.findall(r'DateTime":"(.*?)","Value":',s)
    b1=' '.join(b0)
    b2=b1.encode('utf-8')
    b=b2.split(':00')
    b.remove('')
    t1=[]
    for i in range(len(b)):
        t1=t1+[int(b[i])]
    print t1
    c=t1[len(t1)-1]
    t2=[]
    for i in range(len(t1)):
        w=h((c-t1[i]))*(t1[i]+24-c)+h((t1[i]-c))*(t1[i]-c)
        t2=t2+[w]
    print t2  
    a=a0
    print len(a)
    dic=dict(zip(t2,a0))
    return dic

def wrcol(m,n):
    d=(sp(m,n)).items()
    if n==0:
        for r in range(24):
            table.write((1+r+m*24),1,sitess[m].decode('utf-8'))
            table.write((1+r+m*24),0,str(getnow()-24+r+1)+':00')
    for r in range(len(d)):
        table.write(24*m+(d[r])[0],n+2,(d[r])[1])
  
def send_email(msg,file_name):
    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = file_name#邮件标题，这里我把标题设成了你所发的附件名
    msgText = MIMEText('%s'%msg,'html','utf-8')#你所发的文字信息将以html形式呈现
    msgRoot.attach(msgText)
    att = MIMEText(open('%s'%file_name, 'rb').read(), 'base64', 'utf-8')#添加附件
    att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"] = 'attachment; filename="%s"'%file_name
    msgRoot.attach(att)
    while 1:#持续尝试发送，直到发送成功
        try:
            smtp.sendmail(sender, receiver, msgRoot.as_string())#发送邮件 
            break
        except:
            try:
                smtp.connect(smtpserver)#连接至邮件服务器
                smtp.login(username, password)#登录邮件服务器
            except:
                print "failed to login to smtp server"#登录失败
                 
f=xlwt.Workbook()
table=f.add_sheet('001')
for i in range(len(itemss)):
    table.write(0,i+2,itemss[i])   
for i in range(4):
    for j in range(8):
        wrcol(i,j)       
f.save(date+'.xls')
time.sleep(10)
MSG="good-night"#要发送的文字
FILE="/root/airlinux/"+date+".xls"#要发送的文件
send_email(MSG,FILE)
