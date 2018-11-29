In this section, you will create a function to implement the sendEmail program, and test the function through the console or by calling APIs.

## Creating a sendEmail SCF
1. Log in to the [Serverless Cloud Function Console](https://console.cloud.tencent.com/scf). Select **Guangzhou** from the region list and click **Create**.

2. In the  **Function configuration** section, enter `sendEmail` as the function name and keep default settings for the other options, and then click **Next**.

3. In the **Function code** section, enter `index.main_handler` as the execution method and paste the following codes into the code window, and then click **Next**.

```
# -*- coding: utf8 -*-
import json
import smtplib
from email.mime.text import MIMEText
from email.header import Header

#Third-party SMTP service
mail_host="smtp.qq.com"         #SMTP server
mail_user="3473058547@qq.com"     #User name
mail_pass="xxxxxxx"        #Password 
mail_port=465                   # SMTP service port

def sendEmail(fromAddr,toAddr,subject,content):
    sender = fromAddr
    receivers = [toAddr]  # To receive emails. You can set it as your QQ mailbox or other mailbox.
     
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

4. In the **Triggering method** section, you need to test the function manually, so no trigger method is added currently. Click **Complete**.


**Note**
You must configure the `mail_host, mail_user, mail_pass, and mail_port` parameters based on the mailbox or mail server you use to receive emails. For example, you can view [here](http://service.mail.qq.com/cgi-bin/help?subtype=1&&no=166&&id=28) to learn about how to enable the SMTP feature of QQ Mail. After it is enabled, the relevant parameters are as follows:
- mail_host: SMTP server "smtp.qq.com"
- mail_user: Your email address as the login user name, such as `3473058547@qq.com`
- mail_pass: The password you specified when you enable the SMTP feature.
- mail_port: The server login port. Since you can only log in to your QQ mailbox using SSL, the port must always be 465. Use `smtplib.SMTP_SSL` in codes to build SSL SMTP connection.


## Testing the sendEmail SCF

When a function is created, it is generally tested through the console or API, to ensure the function output meets the expectation, and then you can bind it to a trigger for practical application.

1) In the details page of the sendEmail function you just created, click **Test**.

2) Enter the following in the test template:

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

You can modify both `fromAddr` and `toAddr` in the `msgBody` field to your email address. In this way, you can send an email from and to the same email address to test the validity of email sending. Here, we use `3473058547@qq.com` to test.

3) Click **Run** to view the results. This program is running normally if "send email success" is displayed in both the returned value and the log.

![](https://main.qcloudimg.com/raw/d9d40307e078d3f625b72b5a4c2a06d2.png)



4) Go to the mailbox you specified to check whether the email is received. Open the email to check whether configured information is displayed.
![](https://main.qcloudimg.com/raw/399d00ece487f97afb8d3acdf93ee955.png)

