import urllib
import requests
import re
while 1:
    name=raw_input('enter:')
    url='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null'
    data={
'type':'AUTO',
'i':name,
'doctype':'json',
'xmlVersion':'1.8',
'keyfrom':'fanyi.web',
'ue':'UTF-8',
'action':'FY_BY_CLICKBUTTON',
'typoResult':'true'
}

    r=requests.post(url,data)
    print r.text
