import smtplib  

from email.mime.text import MIMEText  

to_list=["798423285@qq.com"] 

host="smtp.qq.com"

username="2528485257@qq.com"

password="3.1415926535"

postfix="xxx"

  

def send_plain_mail(send_list,title,content):

    me="<"+username+"@"+postfix+">"  

    msg = MIMEText(content,_subtype='plain',_charset='gb2312')  

    msg['Subject'] = title 

    msg['From'] = me  

    msg['To'] = ";".join(to_list)

  

    try:  

        server = smtplib.SMTP()

        server.connect(host)

        server.login(username,password)  

        server.sendmail(me, to_list, msg.as_string())

        server.close()

        return True

  

    except Exception, e:  

        print str(e)  

        return False

if __name__ == '__main__':

    email_title = "title::"

    email_content = "content::"

    if send_plain_mail(to_list,email_title,email_content):

        print "send success !"

    else:  

        print "send failed !"




