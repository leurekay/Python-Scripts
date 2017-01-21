
import urllib
from bs4 import BeautifulSoup
import re

num=''

while 1:
    
    url='http://www.heibanke.com/lesson/crawler_ex00/'
    html=urllib.urlopen(url+num)
    bs_obj=BeautifulSoup(html,"html.parser")
    e=str(bs_obj.h3)
    p=re.compile('\d+')
    list1=p.findall(e)
    num=list1[1]
    print num








