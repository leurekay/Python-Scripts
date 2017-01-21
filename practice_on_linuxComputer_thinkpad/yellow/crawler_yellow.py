import urllib
from bs4 import BeautifulSoup
import re
import os
num=224499
while(num):
    os.mkdir(str(num))
    url='http://www.46lb.com/html/article/'+str(num)+'.html'
    html=urllib.urlopen(url)
    bs_obj=BeautifulSoup(html,"html.parser")
    e=str(bs_obj)
    b=re.findall('http://img(.*?)jpg',e)
    num=num-1
    for i in range(0,len(b)):
        b[i]='http://img'+b[i]+'jpg'
        #print i,'',b[i],'\n' '\n'
        urllib.urlretrieve(b[i],str(num+1)+'_'+str(i))
        #shutil.move("oldpos","newpos")
