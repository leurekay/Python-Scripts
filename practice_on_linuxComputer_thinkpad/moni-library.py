#_*_coding=utf-8_*_
import urllib
import urllib2
import cookielib
import requests
from bs4 import BeautifulSoup
import re

#cookie
cookie=cookielib.CookieJar()
hander=urllib2.HTTPCookieProcessor(cookie)
opener=urllib2.build_opener(hander)
urllib2.install_opener(opener)


url='http://book.njulib.cn/smarty_lib/control/controller.php?control=control_log&action=user_login&user_id=MG1422005&us'
postdata={}
#data['control']='control_log'
#data['action']='user_login'
postdata['user_id']='MG1422099'
postdata['user_pwd']='MG1422099'
#data['rand']='0.077178061008453'
postdata=urllib.urlencode(postdata)

req=urllib2.Request(url,data=postdata)
login_r=opener.open(req)
print login_r.read()
print '##########################'


url2='http://book.njulib.cn/book_lst.php'
result=opener.open(url2)
aa=result.read()
b=re.findall(r'[0-9]" target="_self">(.*?)</a></li>',aa)
num=len(b)
for i in range(0,(num)):
    
    print b[i].decode('utf-8')

   
