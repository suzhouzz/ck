import os
import smtplib
from email.mime.multipart import MIMEMultipart
import datetime
from email.mime.text import MIMEText
from random import *


def send_report():
    port = randint(10000, 90000)
    # 用浏览器打开报告
    os.popen("allure serve " + "D:\\Desktop\\login\SZZX\\report" + " -h 192.168.3.60 -p " + str(port))
    # 格式化成我们想要的日期
    rq = datetime.datetime.now().strftime('%Y-%m-%d')
    sender = "17302154925@163.com"                              # 发送人邮箱
    receiver = ['17302154925@163.com']      # 抄送人邮箱
    message = MIMEMultipart()
    message['Subject'] = "%s 测试报告" % rq    # 邮件标题
    message['From'] = sender
    message['To'] = ','.join(receiver)

    message.attach(MIMEText('测试报告地址：http://desktop-ls6pof1:%s/index.html' % port, 'html', 'utf-8'))
    # 端口465或994
    server = smtplib.SMTP_SSL('smtp.163.com', 465)

    server.login(sender, 'JQHEPXXRKHSJBESN')
    server.sendmail(sender, receiver, message.as_string())

    server.quit()
