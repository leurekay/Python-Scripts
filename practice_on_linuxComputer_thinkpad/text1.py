import requests
url='http://www.heibanke.com/lesson/crawler_ex01/'
    
params={'username':'heibanke','password':25}
r=requests.post(url,data=params)
print r.text

