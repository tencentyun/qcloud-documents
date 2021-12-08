通过 SMTP 的方式发送带附件的邮件的方法，即构建一封 MIME 格式的邮件内容。
## 邮件 mime 格式
了解更多协议相关，请参见 [MIME  协议](https://www.ietf.org/rfc/rfc4021.html)。
>?MIME 消息由消息头和消息体两大部分组成。分别称为 [邮件头](#head)、[邮件体](#body)。
[](id:head)
## 邮件头
包含了发件人、收件人、主题、时间、MIME 版本、邮件内容的类型等重要信息。

>?每条信息称为一个域，由域名后加“: ”和信息内容构成，可以是一行，较长的也可以占用多行。
>- 域的首行必须“顶头”写，即左边不能有空白字符（空格和制表符）。
>- 续行则必须以空白字符打头，且一个空白字符不是信息本身固有的（解码时要过滤掉）。

邮件头中不允许出现空行。有一些邮件不能被邮件客户端软件识别，显示的是原始码，就是因为首行是空行。

例如：
<table style="width: 400px;">
   <tr>
      <th width="50px" >内容</td>
      <th width="50px" >示例 </td>
   </tr>
   <tr>
      <td>Date</td>
      <td>Mon, 29 Jun 2009 18:39:03 +0800</td>
   </tr>
   <tr>
      <td>From</td>
      <td>abc@123.com</td>
   </tr>
   <tr>
      <td>To</td>
      <td>abc1@123.com</td>
   </tr>
   <tr>
      <td>BCC</td>
      <td>abc3@123.com</td>
   </tr>
   <tr>
      <td>Subject</td>
      <td>test</td>
   </tr>
   <tr>
      <td>Message-ID</td>
      <td>123@123.com</td>
   </tr>
   <tr>
      <td>Mime-Version</td>
      <td>1.0</td>
   </tr>
</table>

<table style="width: 400px;">
   <tr>
      <th width="50px" >域名</td>
      <th width="50px" >含义 </td>
   </tr>
   <tr>
      <td>Bcc</td>
      <td>暗送地址</td>
   </tr>
   <tr>
      <td>Cc</td>
      <td>抄送地址</td>
   </tr>
   <tr>
      <td>Content-Transfer-Encoding</td>
      <td>内容的传输编码方式</td>
   </tr>
   <tr>
      <td>Content-Type</td>
      <td>内容的类型</td>
   </tr>
   <tr>
      <td>Date</td>
      <td>日期和时间</td>
   </tr>
   <tr>
      <td>Delivered-To</td>
      <td>发送地址</td>
   </tr>
   <tr>
      <td>From</td>
      <td>发件人地址</td>
   </tr>
   <tr>
      <td>Message-ID</td>
      <td>消息 ID</td>
   </tr>
   <tr>
      <td>MIME-Version</td>
      <td>MIME 版本</td>
   </tr>
   <tr>
      <td>Received</td>
      <td>传输路径</td>
   </tr>
   <tr>
      <td>Reply-To</td>
      <td>回复地址</td>
   </tr>
   <tr>
      <td>Return-Path</td>
      <td>回复地址</td>
   </tr>
   <tr>
      <td>Subject</td>
      <td>主题</td>
   </tr>
   <tr>
      <td>To</td>
      <td>收件人地址</td>
   </tr>
</table>

[](id:body)
## 邮件体
<table style="width: 400px;">
   <tr>
      <th width="50px" >域名</td>
      <th width="50px" >含义 </td>
   </tr>
   <tr>
      <td>Content-ID</td>
      <td>段体的 ID</td>
   </tr>
   <tr>
      <td>Content-Transfer-Encoding</td>
      <td>段体的传输编码方式</td>
   </tr>
   <tr>
      <td>Content-Location</td>
      <td>段体的位置（路径）</td>
   </tr>
   <tr>
      <td>Content-Base</td>
      <td>段体的基位置</td>
   </tr>
   <tr>
      <td>Content-Disposition</td>
      <td>段体的安排方式</td>
   </tr>
   <tr>
      <td>Content-Type</td>
      <td>段体的类型</td>
   </tr>
</table>



有些域除了值之外，还带有参数。值与参数、参数与参数之间以“;”分隔。参数名与参数值之间以“=”分隔。

- 邮件体包含邮件的内容，它的类型由邮件头的`Content-Type`域指出。
>?常见的简单类型有：
>- text/plain（纯文本） 
>- text/html（超文本）。

- multipart 类型，是 MIME 邮件的精髓。邮件体被分为多个段，每个段又包含段头和段体两部分，这两部分之间也以空行分隔。

- 常见的 multipart 类型有三种：
 - multipart/mixed
 - multipart/related
 - multipart/alternative
可从上述名称，得知这些类型各自的含义和用处。它们之间的层次关系可归纳为下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/9f1aac60b3a7964ffbdda28b766b24c6.png)
如果在邮件中要添加附件，必须定义 multipart/mixed 段；如果存在内嵌资源，至少要定义 multipart/related 段；如果纯文本与超文本共存，至少要定义 multipart/alternative 段。
>?附件个数不超过10个，单个附件大小不超过5M，总附件大小不超过10M,具体可参见 [数据结构](https://cloud.tencent.com/document/api/1288/51053#Attachment)。

## 代码示例
<dx-codeblock>
:::  go
package main
import (
	"bytes"
	"crypto/tls"
	"encoding/base64"
	"fmt"
	"io/ioutil"
	"log"
	"mime"
	"net"
	"net/smtp"
	"time"
)

// Test465Attachment  for port 465
func Test465Attachment() error {
	boundary := "GoBoundary"
	host := "smtp.qcloudmail.com"
	port := 465
	email := "abc@cd.com"
	password := "***"
	toEmail := "test@test123.com"
	header := make(map[string]string)
	header["From"] = "test " + "<" + email + ">"
	header["To"] = toEmail
	header["Subject"] = "Test465Attachment"
	header["Content-Type"] = "multipart/mixed;boundary=" + boundary
	//该字段暂时没有用到 ，默认传1.0
	header["Mime-Version"] = "1.0"
	//该字段暂时没有用到
	header["Date"] = time.Now().String()
	bodyHtml := "<!DOCTYPE html>\n<html>\n<head>\n<meta charset=\"utf-8\">\n<title>hello world</title>\n</head>\n<body>\n " +
		"<h1>我的第一个标题</h1>\n    <p>我的第一个段落。</p>\n</body>\n</html>"
	message := ""
	for k, v := range header {
		message += fmt.Sprintf("%s: %s\r\n", k, v)
	}
	buffer := bytes.NewBuffer(nil)
	buffer.WriteString(message)
	contentType := "Content-Type: text/html" + "; charset=UTF-8"
	body := "\r\n--" + boundary + "\r\n"
	body += "Content-Type:" + contentType + "\r\n"
	body += "\r\n" + bodyHtml + "\r\n"
	buffer.WriteString(body)

	attachment := "\r\n--" + boundary + "\r\n"
	attachment += "Content-Transfer-Encoding:base64\r\n"
	attachment += "Content-Disposition:attachment\r\n"
	attachment += "Content-Type:" + "application/octet-stream" + ";name=\"" + mime.BEncoding.Encode("UTF-8",
		"./go.mod") + "\"\r\n"
	buffer.WriteString(attachment)
	writeFile(buffer, "./go.mod")
	//多个附件往后拼接，最多不能超过10个附件，单个附件不能超过5M,所有附件累计不能超过8-9M，消息体过大会返回EOF
	attachment1 := "\r\n--" + boundary + "\r\n"
	attachment1 += "Content-Transfer-Encoding:base64\r\n"
	attachment1 += "Content-Disposition:attachment\r\n"
	attachment1 += "Content-Type:" + "application/octet-stream" + ";name=\"" + mime.BEncoding.Encode("UTF-8",
		"./bbbb.txt") + "\"\r\n"
	buffer.WriteString(attachment1)
	writeFile(buffer, "./bbbb.txt")
	defer func() {
		if err := recover(); err != nil {
			log.Fatalln(err)
		}
	}()

	buffer.WriteString("\r\n--" + boundary + "--")
	message += "\r\n" + body
	auth := smtp.PlainAuth(
		"",
		email,
		password,
		host,
	)
	err := SendMailWithTLS(
		fmt.Sprintf("%s:%d", host, port),
		auth,
		email,
		[]string{toEmail},
		buffer.Bytes(),
	)
	if err != nil {
		fmt.Println("Send email error:", err)
	} else {
		fmt.Println("Send mail success!")
	}
	return err
}

// Dial return a smtp client
func Dial(addr string) (*smtp.Client, error) {
	conn, err := tls.Dial("tcp", addr, nil)
	if err != nil {
		log.Println("tls.Dial Error:", err)
		return nil, err
	}

	host, _, _ := net.SplitHostPort(addr)
	return smtp.NewClient(conn, host)
}

// SendMailWithTLS send email with tls
func SendMailWithTLS(addr string, auth smtp.Auth, from string,
	to []string, msg []byte) (err error) {
	//create smtp client
	c, err := Dial(addr)
	if err != nil {
		log.Println("Create smtp client error:", err)
		return err
	}
	defer c.Close()
	if auth != nil {
		if ok, _ := c.Extension("AUTH"); ok {
			if err = c.Auth(auth); err != nil {
				log.Println("Error during AUTH", err)
				return err
			}
		}
	}
	if err = c.Mail(from); err != nil {
		return err
	}
	for _, addr := range to {
		if err = c.Rcpt(addr); err != nil {
			return err
		}
	}
	w, err := c.Data()
	if err != nil {
		return err
	}
	_, err = w.Write(msg)
	if err != nil {
		return err
	}
	err = w.Close()
	if err != nil {
		return err
	}
	return c.Quit()
}

// writeFile read file to buffer
func writeFile(buffer *bytes.Buffer, fileName string) {
	file, err := ioutil.ReadFile(fileName)
	if err != nil {
		panic(err.Error())
	}
	payload := make([]byte, base64.StdEncoding.EncodedLen(len(file)))
	base64.StdEncoding.Encode(payload, file)
	buffer.WriteString("\r\n")
	for index, line := 0, len(payload); index < line; index++ {
		buffer.WriteByte(payload[index])
		if (index+1)%76 == 0 {
			buffer.WriteString("\r\n")
		}
	}
}

func main() {
	Test465Attachment()
}

:::
</dx-codeblock>
