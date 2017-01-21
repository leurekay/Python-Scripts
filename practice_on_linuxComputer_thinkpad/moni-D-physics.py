#_*_coding=utf-8_*_
import urllib
import urllib2
import requests
from bs4 import BeautifulSoup
import cookielib
import re

#cookie
cookie=cookielib.CookieJar()
hander=urllib2.HTTPCookieProcessor(cookie)
opener=urllib2.build_opener(hander)
urllib2.install_opener(opener)

url='http://graphy.nju.edu.cn/user/user_check.asp?redirectto='
data0={}
data0['user_account']='MG1422005'
data0['user_pwd']='313313'
postdata=urllib.urlencode(data0)


req=urllib2.Request(url,data=postdata)
login_r=opener.open(req)
#print result
print login_r.read()

url2='http://graphy.nju.edu.cn/user/course_sel.asp'
ww=opener.open(url2)
#print ww.read()
