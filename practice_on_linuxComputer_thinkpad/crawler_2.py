import requests
url='http://www.heibanke.com/lesson/crawler_ex01/'
for i in range(1,30):
    
    params={'username':'heibanke','password':i}
    r=requests.post(url,data=params)
    
    end=r.text.find('/h3')
    start=r.text.find('h3')
    print end-start
    if (end-start)==19 :
        print i, 'no'
    else:
        print i, 'yes'
        print r.text
        break
    
