from bs4 import BeautifulSoup
import requests
import urllib

url='http://fanyi.youdao.com/'
html=urllib.urlopen(url)
bs_obj=BeautifulSoup(html)
e=str(bs_obj)
print e

    
    
