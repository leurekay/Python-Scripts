import urllib
from bs4 import BeautifulSoup
import re
num=99
while(num):
    url='http://tieba.baidu.com/p/18054339'+str(num)
    html=urllib.urlopen(url)
    bs_obj=BeautifulSoup(html,"html.parser")
    e=str(bs_obj)
    b=re.findall('http://imgsrc.baidu.com/forum/w%(.*?)jpg',e)
    num=num-1
    for i in range(0,len(b)):
        b[i]='http://imgsrc.baidu.com/forum/w%'+b[i]+'jpg'
        #print i,'',b[i],'\n' '\n'
        urllib.urlretrieve(b[i],str(num+1)+'_'+str(i))
        

