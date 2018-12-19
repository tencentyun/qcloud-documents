在此部分中，用户将创建一个函数来实现发送邮件程序，并通过控制台/API调用来测试函数。

## 创建 sendEmail 云函数
1. 登录[无服务器云函数控制台](https://console.cloud.tencent.com/scf)，在【广州】地域下单击【新建】按钮。

2. 进入函数配置部分，函数名称填写`sendEmail`，剩余项保持默认，单击【下一步】。

3. 进入函数代码部分，执行方法填写`index.main_handler`，代码窗口内贴入如下代码，单击【下一步】。

```
# -*- coding: utf8 -*-
import json
import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
mail_host="smtp.qq.com"         #SMTP服务器
mail_user="3473058547@qq.com"     #用户名
mail_pass="xxxxxxx"        #口令 
mail_port=465                   #SMTP服务端口

def sendEmail(fromAddr,toAddr,subject,content):
    sender = fromAddr
    receivers = [toAddr]  # 接收邮件，可设置为您的QQ邮箱或者其他邮箱
     
    message = MIMEText(content, 'plain', 'utf-8')
    message['From'] = Header(fromAddr, 'utf-8')
    message['To'] =  Header(toAddr, 'utf-8')
    message['Subject'] = Header(subject, 'utf-8')
     
    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, mail_port) 
        smtpObj.login(mail_user,mail_pass)  
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("send success") 
    except smtplib.SMTPException as e:
        print(e)
        print("Error: send fail") 

def main_handler(event, context):
    cmqMsg = None
    if event is not None and "Records" in event.keys():
        if len(event["Records"]) >= 1 and "CMQ" in event["Records"][0].keys():
            cmqMsgStr = event["Records"][0]["CMQ"]["msgBody"]
            cmqMsg = json.loads(cmqMsgStr)
    print cmqMsg
    sendEmail(cmqMsg['fromAddr'], cmqMsg['toAddr'], cmqMsg['title'], cmqMsg['body'])
    return "send email success"

```

4) 进入触发方式部分，此时由于需要先手动测试函数，暂时不添加任何触发方式，单击【完成】按钮。


**说明**
请特别注意，参数 `mail_host, mail_user, mail_pass, mail_port` 需要您根据所期望发送的邮箱或邮件服务器来配置，这里我们以 QQ 邮箱为例，您可以从 [这里](http://service.mail.qq.com/cgi-bin/help?subtype=1&&no=166&&id=28) 了解到如何开启 QQ 邮箱的 SMTP 功能。QQ 邮箱的 SMTP 功能开启后，相应的参数如下。
- mail_host SMTP服务器地址为 "smtp.qq.com"
- mail_user 登录用户名为您的邮箱地址，例如 `3473058547@qq.com`
- mail_pass 为您在开启 SMTP 功能时设置的密码
- mail_port 为服务器登录端口，由于 QQ 邮箱强制要求SSL登录，端口固定为 465，同时代码中使用 `smtplib.SMTP_SSL` 创建 SSL 的 SMTP 连接


## 测试 sendEmail 云函数

在创建函数时，通常会使用控制台或 API 先进行测试，确保函数输出符合预期后再绑定触发器进行实际应用。

1) 在刚刚创建的 sendEmail 函数详情页中，单击【测试】按钮；

2) 在测试模版内输入如下内容：

```
{
  "Records": [
    {
      "CMQ": {
        "type": "topic",
        "topicOwner":1253970226,
        "topicName": "sendEmailQueue",
        "subscriptionName":"sendEmailFunction",
        "publishTime": "2017-09-25T06:34:00.000Z",
        "msgId": "123345346",
        "requestId":"123345346",
        "msgBody": "{\"fromAddr\":\"3473058547@qq.com\",\"toAddr\":\"3473058547@qq.com\",\"title\":\"hello from scf & cmq\",\"body\":\"email content to send\"}",
        "msgTag": []
      }
    }
  ]
}
```

其中 `msgBody` 字段内， `fromAddr`，`toAddr`内的字段，可以根据您自身邮箱地址进行修改，建议可以修改为相同地址，自身邮箱向自身邮箱内发送邮件，以便测试邮件发送的正确性。我们在这里使用了 `3473058547@qq.com` 这个邮箱来进行测试。

3) 单击【运行】按钮，观察运行结果。如果在结果中发现返回值和日志中均显示 "send email success"，则此程序运行正常。
![](https://mc.qcloudimg.com/static/img/2f660ce173162212ac1fc1bf4aaf1b09/function+test.png)

4) 前往个人配置的接收邮箱，查收是否收取到邮件。打开邮件，查看邮件内容是否为配置的内容。
![](https://mc.qcloudimg.com/static/img/a6f6b9c368e208f795e0700f597363c6/email+confirm.png)
