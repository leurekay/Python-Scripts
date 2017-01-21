#coding: utf-8
import smtplib
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.header import Header
import time
 
sender ='2528485257@qq.com'
receiver ='1447981848@qq.com'
subject = '不为人知的秘密．．．．'
smtpserver = 'smtp.qq.com'
username = '2528485257@qq.com'
password = '3.1415926535'
 
msg = MIMEText('hehehheheheh','plain','utf-8')#中文需参数‘utf-8’，单字节字符不需要
with open('/home/gates/test/help.txt', 'rb') as f:
    # 设置附件的MIME和文件名，这里是png类型:
    mime = MIMEBase('image', 'txt', filename='help.txt')
    # 加上必要的头信息:
    mime.add_header('Content-Disposition', 'attachment', filename='test.png')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来:
    mime.set_payload(f.read())
    # 用Base64编码:
    #encoders.encode_base64(mime)
    # 添加到MIMEMultipart:
    msg.attach(mime)
msg['Subject'] = Header(subject, 'utf-8')

    
smtp = smtplib.SMTP()
smtp.connect('smtp.qq.com')
smtp.login(username, password)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()
time.sleep(1)
