以下代码示例，Python 语言（版本 >= 3.6即可）通过 SMTP 发送邮件：

``` python
# -*- coding:utf-8 -*-
import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr


def send_mail(sender, sender_alias, sender_pwd, recipient_list, subject, body, host="smtp.qcloudmail.com", port=465,
              is_use_ssl=True):
    try:
        message = MIMEMultipart('alternative')
        message['Subject'] = Header(subject, 'UTF-8')
        message['From'] = formataddr([sender_alias, sender])
        message['To'] = ",".join(recipient_list)
        to_addr_list = recipient_list

        mime_text = MIMEText(body, _subtype='html', _charset='UTF-8')
        message.attach(mime_text)

        if is_use_ssl:
            client = smtplib.SMTP_SSL(host, port)
        else:
            client = smtplib.SMTP(host, port)

        client.login(sender, sender_pwd)
        client.sendmail(sender, to_addr_list, message.as_string())
        client.quit()

        print('Send email success!')
    except smtplib.SMTPConnectError as e:
        print('Send email failed,connection error:', e.smtp_code, e.smtp_error)
    except smtplib.SMTPAuthenticationError as e:
        print('Send email failed,smtp authentication error:', e.smtp_code, e.smtp_error)
    except smtplib.SMTPSenderRefused as e:
        print('Send email failed,sender refused:', e.smtp_code, e.smtp_error)
    except smtplib.SMTPRecipientsRefused as e:
        print('Send email failed,recipients refused:', e.recipients)
    except smtplib.SMTPDataError as e:
        print('Send email failed,smtp data error:', e.smtp_code, e.smtp_error)
    except smtplib.SMTPException as e:
        print('Send email failed,smtp exception:', str(e))
    except Exception as e:
        print('Send email failed,other error:', str(e))


if __name__ == '__main__':
    # 将下面xxx之类替换为自己的地址，直接运行就可以成功发送邮件了，python版本>=3.6即可
    # 控制台创建的发信人地址
    from_email = "xxx@xxxx"
    # 控制台发信地址对应设置的SMTP密码
    from_email_pwd = "xxx"
    # 接收人地址列表
    to_email_list = ["xxx@xxx1", "xxx@xxx2"]

    # 发信人地址别名
    from_alias = "测试别名"
    # 邮件主题
    subject_txt = "[测试主题]"
    # 邮件内容
    body_content = (
        "<!DOCTYPE html>\n<html>\n<head>\n<meta charset=\"utf-8\">\n<title>hello world</title>\n</head>\n<body>\n "
        "<h1>我的第一个标题</h1>\n    <p>我的第一个段落。</p>\n</body>\n</html>")

    # 默认使用ssl发邮件，端口可以为 465或587
    is_using_ssl = True
    # smtp服务地址, 香港=smtp.qcloudmail.com,新加坡=sg-smtp.qcloudmail.com,广州=gz-smtp.qcloudmail.com
    smtp_host = "smtp.qcloudmail.com"
    # smtp端口号, 465和587使用ssl加密，25使用tls
    smtp_port = 465

    # 使用25端口发邮件
    # is_using_ssl = False
    # smtp_host = "smtp.qcloudmail.com"
    # smtp_port = 25
    send_mail(from_email, from_alias, from_email_pwd, to_email_list, subject_txt, body_content,
              smtp_host, smtp_port, is_using_ssl)

```
