以下代码示例，是 Demo 使用 JDK 1.8：
```
package org.example;

import javax.mail.*;
import javax.mail.internet.InternetAddress;
import javax.mail.internet.MimeMessage;
import java.io.UnsupportedEncodingException;
import java.nio.charset.StandardCharsets;
import java.util.Properties;

public class SampleMail {
    private static final String SMTP_HOST = "smtp.qcloudmail.com";
    private static final String SMTP_PORT = "465";

    public static void main(String[] args) {
        // 配置发送邮件的环境属性
        final Properties props = new Properties();
        // 表示SMTP发送邮件，需要进行身份验证
        props.put("mail.smtp.auth", "true");
        props.put("mail.smtp.host", SMTP_HOST);
        // 如果使用ssl，则去掉使用25端口的配置，进行如下配置,
        props.put("mail.smtp.socketFactory.class", "javax.net.ssl.SSLSocketFactory");
        props.put("mail.smtp.socketFactory.port", SMTP_PORT);
        props.put("mail.smtp.port", SMTP_PORT);
        // 发件人的账号，填写控制台配置的发信地址,比如xxx@xxx.com
        props.put("mail.user", "xxx@xxx.com");
        // 访问SMTP服务时需要提供的密码(在控制台选择发信地址进行设置)
        props.put("mail.password", "XXXX");
        props.setProperty("mail.smtp.socketFactory.fallback", "false");
        props.put("mail.smtp.ssl.enable", "true");
        //props.put("mail.smtp.starttls.enable","true");
        // 构建授权信息，用于进行SMTP进行身份验证
        Authenticator authenticator = new Authenticator() {
            @Override
            protected PasswordAuthentication getPasswordAuthentication() {
                // 用户名、密码
                String userName = props.getProperty("mail.user");
                String password = props.getProperty("mail.password");
                return new PasswordAuthentication(userName, password);
            }
        };
        // 使用环境属性和授权信息，创建邮件会话
        Session mailSession = Session.getInstance(props, authenticator);
//        mailSession.setDebug(true);
        //UUID uuid = UUID.randomUUID();
        //final String messageIDValue = "<" + uuid.toString() + ">";
        // 创建邮件消息
        MimeMessage message = new MimeMessage(mailSession) {
            //@Override
            //protected void updateMessageID() throws MessagingException {
            //设置自定义Message-ID值
            //setHeader("Message-ID", messageIDValue);
            //}
        };
        try {
            // 设置发件人邮件地址和名称。填写控制台配置的发信地址,比如xxx@xxx.com。和上面的mail.user保持一致。名称用户可以自定义填写。
            InternetAddress from = new InternetAddress("xxx@xxx.com", "test");
            message.setFrom(from);
            //可选。设置回信地址
//            Address[] a = new Address[1];
//            a[0] = new InternetAddress("***");
//            message.setReplyTo(a);
            // 设置收件人邮件地址，比如yyy@yyy.com
            InternetAddress to = new InternetAddress("xxx@xxx.com");
            message.setRecipient(MimeMessage.RecipientType.TO, to);
            //如果同时发给多人，才将上面两行替换为如下（因为部分收信系统的一些限制，尽量每次投递给一个人；同时我们限制单次允许发送的人数是50人）：
            //InternetAddress[] adds = new InternetAddress[2];
            //adds[0] = new InternetAddress("xxx@xxx.com");
            //adds[1] = new InternetAddress("xxx@xxx.com");
            //message.setRecipients(Message.RecipientType.TO, adds);

            // 设置邮件标题
            message.setSubject("测试邮件");
            message.setHeader("Content-Transfer-Encoding", "base64");
            // 设置邮件的内容体 type: text/plain（纯文本）text/html（HTML 文档）
            message.setContent("<!DOCTYPE html>\n<html>\n<head>\n<meta charset=\"utf-8\">\n<title>hello world</title>\n</head>\n<body>\n " +
                    "<h1>我的第一个标题</h1>\n    <p>我的第一个段落。</p>\n</body>\n</html>", "text/html;charset=UTF-8");
            //发送邮件
            Transport.send(message);
        } catch (MessagingException | UnsupportedEncodingException e) {
            String err = e.getMessage();
            err = new String(err.getBytes(StandardCharsets.ISO_8859_1), StandardCharsets.UTF_8);
            System.out.println(err);
        }
    }

}
```

## 发送附件
```
package org.example;

import javax.activation.DataHandler;
import javax.activation.FileDataSource;
import javax.mail.*;
import javax.mail.internet.*;
import java.io.UnsupportedEncodingException;
import java.nio.charset.StandardCharsets;
import java.util.Properties;
import java.util.UUID;

public class SampleMailAttach {
    private static final String ALIDM_SMTP_HOST = "smtp.qcloudmail.com";
    private static final String ALIDM_SMTP_PORT = "465";

    public static void main(String[] args) {
        // 配置发送邮件的环境属性
        final Properties props = new Properties();
        // 表示SMTP发送邮件，需要进行身份验证
        props.put("mail.smtp.auth", "true");
        props.put("mail.smtp.host", ALIDM_SMTP_HOST);
        // 如果使用ssl，则去掉使用25端口的配置，进行如下配置,
        props.put("mail.smtp.socketFactory.class", "javax.net.ssl.SSLSocketFactory");
        props.put("mail.smtp.socketFactory.port", ALIDM_SMTP_PORT);
        props.put("mail.smtp.port", ALIDM_SMTP_PORT);
        // 发件人的账号，填写控制台配置的发信地址,比如xxx@xxx.com
        props.put("mail.user", "xxx@xxx.com");
        // 访问SMTP服务时需要提供的密码(在控制台选择发信地址进行设置)
        props.put("mail.password", "XXXX");
        props.setProperty("mail.smtp.socketFactory.fallback", "false");
        props.put("mail.smtp.ssl.enable", "true");
        //props.put("mail.smtp.starttls.enable","true");
        // 构建授权信息，用于进行SMTP进行身份验证
        Authenticator authenticator = new Authenticator() {
            @Override
            protected PasswordAuthentication getPasswordAuthentication() {
                // 用户名、密码
                String userName = props.getProperty("mail.user");
                String password = props.getProperty("mail.password");
                return new PasswordAuthentication(userName, password);
            }
        };
        // 使用环境属性和授权信息，创建邮件会话
        Session mailSession = Session.getInstance(props, authenticator);

        UUID uuid = UUID.randomUUID();
        final String messageIDValue = "<" + uuid.toString() + ">";
        //创建邮件消息
        MimeMessage message = new MimeMessage(mailSession) {
            @Override
            protected void updateMessageID() throws MessagingException {
                //设置自定义Message-ID值
                setHeader("Message-ID", messageIDValue);
            }
        };
        try {
            // 设置发件人邮件地址和名称。填写控制台配置的发信地址,和mail.user保持一致。发信别名可以自定义，如test。
            InternetAddress from = new InternetAddress("xxx@xxx.com", "test");
            message.setFrom(from);
            //可选。设置回信地址
            Address[] a = new Address[1];
            a[0] = new InternetAddress("xxx@xxx.com");
            message.setReplyTo(a);
            //设置收件人邮件地址，比如yyy@yyy.com
            InternetAddress to = new InternetAddress("xxx@xxx.com");
            message.setRecipient(MimeMessage.RecipientType.TO, to);
            //如果同时发给多人，才将上面两行替换为如下（因为部分收信系统的一些限制，尽量每次投递给一个人；同时我们限制单次允许发送的人数是50人）：
            /*InternetAddress[] adds = new InternetAddress[2];
            adds[0] = new InternetAddress("xxx@xxx.com");
            adds[1] = new InternetAddress("xxx@xxx.com");
            message.setRecipients(Message.RecipientType.TO, adds);*/

            // 设置邮件标题
            message.setSubject("测试邮件");
            //发送附件，总的邮件大小不超过10M，创建消息部分
            BodyPart messageBodyPart = new MimeBodyPart();
            //消息 text/plain（纯文本）text/html（HTML 文档）
            messageBodyPart.setText("<!DOCTYPE html>\n<html>\n<head>\n<meta charset=\"utf-8\">\n<title>hello world</title>\n</head>\n<body>\n " +
                    "<h1>我的第一个标题</h1>\n    <p>我的第一个段落。</p>\n</body>\n</html>");
            messageBodyPart.setHeader("Content-Type", "text/plain;charset=utf-8");
            //创建多重消息
            Multipart multipart = new MimeMultipart();
            //设置文本消息部分
            multipart.addBodyPart(messageBodyPart);
            //附件部分
            messageBodyPart = new MimeBodyPart();
            //设置要发送附件的文件路径
            String filename = "/Users/aaa/bbb/a.txt";
            FileDataSource source = new FileDataSource(filename);
            messageBodyPart.setDataHandler(new DataHandler(source));
            //处理附件名称中文（附带文件路径）乱码问题
            String filenameEncode = MimeUtility.encodeText(filename, "UTF-8", "base64");
            messageBodyPart.setFileName(filenameEncode);
            messageBodyPart.setHeader("Content-Transfer-Encoding", "base64");
            messageBodyPart.setHeader("Content-Disposition", "attachment");
            messageBodyPart.setHeader("Content-Type", "application/octet-stream;name=\"" + filenameEncode + "\"");
            multipart.addBodyPart(messageBodyPart);

            //附件部分,多个附件，分为多个part
            BodyPart messageBodyPart1 = new MimeBodyPart();
            //设置要发送附件的文件路径
            String filename1 = "/Users/aaa/bbb/b.txt";
            FileDataSource source1 = new FileDataSource(filename1);
            messageBodyPart1.setDataHandler(new DataHandler(source1));
            //处理附件名称中文（附带文件路径）乱码问题
            String filenameEncode1 = MimeUtility.encodeText(filename1, "UTF-8", "base64");
            messageBodyPart1.setHeader("Content-Transfer-Encoding", "base64");
            messageBodyPart1.setHeader("Content-Disposition", "attachment");
            messageBodyPart1.setHeader("Content-Type", "application/octet-stream;name=\"" + filenameEncode1 + "\"");
            multipart.addBodyPart(messageBodyPart1);

            //发送含有附件的完整消息
            message.setContent(multipart);
            //发送附件代码，结束
            //发送邮件
            Transport.send(message);
        } catch (MessagingException | UnsupportedEncodingException e) {
            String err = e.getMessage();
            err = new String(err.getBytes(StandardCharsets.ISO_8859_1), StandardCharsets.UTF_8);
            System.out.println(err);
        }
    }
}


```
## 常见问题
### 遇到报错：“No appropriate protocol (protocol is disabled or cipher suites are inappropriate)”，如何处理？
找到 `jdk/jre/lib/security/java.security` 文件进行修改：
![](https://qcloudimg.tencent-cloud.cn/raw/d05f0478d608849a10f61290777a2689.png)