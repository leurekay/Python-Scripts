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

url='https://passport.meituan.com/account/unitivelogin?service=www&continue=http%3A%2F%2Fwww.meituan.com%2Faccount%2Fsettoken%3Fcontinue%3Dhttp%253A%252F%252Fnj.meituan.com%252F'
data0={
'email':'15251897539',
'password':'313313',
'origin':'account-login',
'fingerprint':'0-6-1-4wp%7Cbo%7Cjl%7Cbx%7Ch5%7C6n%7C6e%7C6k%7C18u%7Ce2%7C5z%7C1km%7Cv%7C1j%7C8b%7C1',
'csrf':'rAv0g0si-u_m6weQxNV3j5e8-OIqRfSYpkDk'
}
postdata=urllib.urlencode(data0)

head={
'Host':'passport.meituan.com',
'Origin':'https://passport.meituan.com',
'Referer':'https://passport.meituan.com/account/unitivelogin?service=www&continue=http%3A%2F%2Fwww.meituan.com%2Faccount%2Fsettoken%3Fcontinue%3Dhttp%253A%252F%252Fnj.meituan.com%252F&mtt=1.index%2Ffloornew.0.0.ifmk658m',
'User-Agent':'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/45.0.2454.85 Chrome/45.0.2454.85 Safari/537.36',
'X-Authorization':'MWS mtpassport:U+YqF0fHZfgywayWqXhaqo+JrDPo7fZOJxXA8rZ8Tag=',
'X-Client':'javascript',
'X-CSRF-Token':'rAv0g0si-u_m6weQxNV3j5e8-OIqRfSYpkDk',

    }
#head=urllib.urlencode(head)

req=urllib2.Request(url,data=postdata,headers=head)
login_r=opener.open(req)
print login_r.read()

url2='http://www.meituan.com/rates/list/torate?mtt=1.rates%2Flist.0.0.ifmjoh9b'
ww=opener.open(url2)
#print ww.read()
