## 常用证书申请流程

- 本地生成私钥：openssl genrsa -out privateKey.pem 2048 其中privateKey.pem为您的私钥文件，请妥善保管
- 生成证书请求文件：openssl req -new -key privateKey.pem -out server.csr 其中server.csr是您的证书请求文件，可用其去申请证书
- 获取请求文件中的内容前往CA等机构站点申请证书

## 证书格式要求

- 用户要申请的证书为：linux环境下pem格式的证书。负载均衡不支持其他格式的证书，如是其它格式的证书请参考本文 “负载均衡支持的证书格式及转换方式” 部分内容。

- 如果是通过root CA机构颁发的证书， 您拿到的证书为唯一的一份，不需要额外的证书，配置的站点即可被浏览器等访问设备认为可信。

- 如果是通过中级CA机构颁发的证书，您拿到的证书文件包含多份证书，需要人为的将服务器证书与中间证书合并在一起上传。

- 当您的证书有证书链时，请将证书链内容，转化为PEM格式内容，与证书内容合并上传。

- 拼接规则为：服务器证书放第一份，中间证书放第二份，中间不要有空行。注：一般情况下，机构在颁发证书的时候会有对应说明， 请注意规则说明。

以下为证书格式和证书链格式范例，请确认格式正确后上传：

1、root CA机构颁发的证书：证书格式为linux环境下pem格式。样例如下：

![](//mccdn.qcloud.com/static/img/b5eb2ee933723e3171d48377f354bc95/image.jpg)

证书规则为：
- [——-BEGIN CERTIFICATE——-, ——-END CERTIFICATE——-] 开头和结尾；请将这些内容一并上传；
- 每行64字符，最后一行不超过64字符；

2、中级机构颁发的证书链：
——-BEGIN CERTIFICATE——-
——-END CERTIFICATE——-
——-BEGIN CERTIFICATE——-
——-END CERTIFICATE——-
——-BEGIN CERTIFICATE——-
——-END CERTIFICATE——-

证书链规则：
- 证书之间不能有空行；
- 每一份证书遵守第一点关于证书的格式说明；

## RSA私钥格式要求

样例如下：

![](//mccdn.qcloud.com/static/img/6fd4309a24b9f969cd76950712fe8868/image.jpg)

rsa私钥可以包括所有私钥（RSA 和 DSA）、公钥（RSA 和 DSA）和 (x509) 证书。它存储用 Base64 编码的 DER 格式数据，用 ascii 报头包围，因此适合系统之间的文本模式传输。

rsa私钥规则：
- [——-BEGIN RSA PRIVATE KEY——-, ——-END RSA PRIVATE KEY——-] 开头结尾；请将这些内容一并上传；
- 每行64字符，最后一行长度可以不足64字符。

如果您不是按照上述方案生成私钥，得到[——-BEGIN PRIVATE KEY——-, ——-END PRIVATE KEY——-] 这种样式的私钥，您可以按照如下方式转换：
```
openssl rsa -in old_server_key.pem -out new_server_key.pem
```
然后将new_server_key.pem的内容与证书一起上传。

## 证书转换为PEM格式说明

目前负载均衡只支持PEM格式的证书，其他格式的证书需要转换成PEM格式后才能上传到负载均衡中，建议通过openssl 工具进行转换。下面是几种比较流行的证书格式转换为PEM格式的方法。

### DER转换为PEM

DER格式一般出现在java平台中。

证书转换：```openssl x509 -inform der -in certificate.cer -out certificate.pem```

私钥转换：```openssl rsa -inform DER -outform PEM -in privatekey.der -out privatekey.pem```

### P7B转换为PEM

P7B格式一般出现在windows server和tomcat中。

证书转换：```openssl pkcs7 -print_certs -in incertificat.p7b -out outcertificate.cer```

获取outcertificat.cer里面 [——-BEGIN CERTIFICATE——-， ——-END CERTIFICATE——-] 的内容作为证书上传。

私钥转换：无私钥

### PFX转换为PEM

PFX格式一般出现在windows server中。

证书转换：```openssl pkcs12 -in certname.pfx -nokeys -out cert.pem```

私钥转换：```openssl pkcs12 -in certname.pfx -nocerts -out key.pem -nodes```	
