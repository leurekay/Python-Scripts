# -*- coding: utf-8 -*-
from email.mime.text import MIMEText
msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
import smtplib
from_addr = '2528485257@qq.com'
password = '3.1415926535'
smtp_server = '798423285@qq.com'
to_addr = 'smtp.qq.com'

import smtplib
server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25

server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
