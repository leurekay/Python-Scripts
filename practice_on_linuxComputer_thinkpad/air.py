#coding=utf-8
import urllib
from bs4 import BeautifulSoup
import re

url='http://www.zq12369.com/?city=%E5%8D%97%E4%BA%AC&tab=city'
html=urllib.urlopen(url)
bs_obj=BeautifulSoup(html,"html.parser")
st=str(bs_obj)

aqi=re.findall('<div class="aqi">(.*?)</div>',st)
first=re.findall('div class="pdate">(.*?)</div>',st)
a=re.findall('<div class="item bglevel[0-9]">(.*?)</div>',st)
b=re.findall('"value">(.*?)</div>',st)


print first[0].decode('utf-8')
print 'aqi:',aqi[0]
for i in range(0,6):
    print a[i],':',b[i]
    

