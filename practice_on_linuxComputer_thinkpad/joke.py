#coding=utf-8
import urllib
from bs4 import BeautifulSoup
import re
import random

url='http://www.qiushibaike.com/textnew'
html=urllib.urlopen(url)
bs_obj=BeautifulSoup(html,"html.parser")
st=str(bs_obj)
print st

#rand=random.randrange(0,10)
aqi=re.findall('<br/>   3.(.*?)</div>',st)
#print aqi[0].decode('utf-8')


