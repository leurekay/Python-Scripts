#_*_coding=utf-8_*_
import urllib
import requests
import re
from bs4 import BeautifulSoup


def h(x):
    if x>=0 :
        return 1
    else:
        return 0

    
url='http://222.190.111.117:8023/Home/GetDataBySiteItem'
data={
'site':'106',
'item':'812'
}

r=requests.post(url,data)

t=r.text

print t
b0=re.findall(r'003ccategory name=\\"(.*?)\\" /\\',t)
a0=re.findall(r'\\u003cset value=\\"(.*?)\\" /\\u003e\\r\\n',t)


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
print a0

dic=dict(zip(t2,a0))
d=dic.items()
print d
e=(d[2])[0]
print c

