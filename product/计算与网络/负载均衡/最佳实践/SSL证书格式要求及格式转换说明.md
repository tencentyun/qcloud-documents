## 1. 证书格式要求
- 用户要申请的证书为：Linux 环境下 pem 格式的证书。负载均衡不支持其他格式的证书，如是其它格式的证书请参考本文 “负载均衡支持的证书格式及转换方式” 部分内容。
- 如果是通过 root CA 机构颁发的证书，您拿到的证书为唯一的一份，不需要额外的证书，配置的站点即可被浏览器等访问设备认为可信。
- 如果是通过中级 CA 机构颁发的证书，您拿到的证书文件包含多份证书，需要人为的将服务器证书与中间证书合并在一起上传。
- 当您的证书有证书链时，请将证书链内容，转化为 PEM 格式内容，与证书内容合并上传。
- 拼接规则为：服务器证书放第一份，中间证书放第二份，中间不要有空行。
>!一般情况下，机构在颁发证书的时候会有对应说明，请注意规则说明。

以下为证书格式和证书链格式范例，请确认格式正确后上传：
1. root CA 机构颁发的证书：证书格式为 Linux 环境下 pem 格式。样例如下：
![](//mccdn.qcloud.com/static/img/b5eb2ee933723e3171d48377f354bc95/image.jpg)
证书规则为：
 - [——-BEGIN CERTIFICATE——-, ——-END CERTIFICATE——-] 开头和结尾；请将这些内容一并上传。
 - 每行64字符，最后一行不超过64字符。
2. 中级机构颁发的证书链：
——-BEGIN CERTIFICATE——-
——-END CERTIFICATE——-
——-BEGIN CERTIFICATE——-
——-END CERTIFICATE——-
——-BEGIN CERTIFICATE——-
——-END CERTIFICATE——-

证书链规则：
- 证书之间不能有空行。
- 每一份证书遵守第一点关于证书的格式说明。

## 2. RSA 私钥格式要求

样例如下：
![](//mccdn.qcloud.com/static/img/6fd4309a24b9f969cd76950712fe8868/image.jpg)
rsa 私钥可以包括所有私钥（RSA 和 DSA）、公钥（RSA 和 DSA）和 (x509) 证书。它存储用 Base64 编码的 DER 格式数据，用 ascii 报头包围，因此适合系统之间的文本模式传输。

rsa私钥规则：
- [——-BEGIN RSA PRIVATE KEY——-, ——-END RSA PRIVATE KEY——-] 开头结尾，请将这些内容一并上传。
- 每行64字符，最后一行长度可以不足64字符。

如果您不是按照上述方案生成私钥，得到[——-BEGIN PRIVATE KEY——-, ——-END PRIVATE KEY——-] 这种样式的私钥，您可以按照如下方式转换：
```
openssl rsa -in old_server_key.pem -out new_server_key.pem
```
然后将 new_server_key.pem 的内容与证书一起上传。

## 3. 证书转换为 PEM 格式说明

目前负载均衡只支持 PEM 格式的证书，其他格式的证书需要转换成 PEM 格式后才能上传到负载均衡中，建议通过 openssl  工具进行转换。下面是几种比较流行的证书格式转换为 PEM 格式的方法。

### 3.1 DER 格式证书转换为 PEM 格式

DER 格式一般出现在 Java 平台中。

证书转换：```openssl x509 -inform der -in certificate.cer -out certificate.pem```

私钥转换：```openssl rsa -inform DER -outform PEM -in privatekey.der -out privatekey.pem```
 
### 3.2 P7B 格式证书转换为 PEM 格式

P7B 格式一般出现在 Windows Server 和 tomcat 中。

证书转换：```openssl pkcs7 -print_certs -in incertificat.p7b -out outcertificate.cer```

获取 outcertificat.cer 里面 [——-BEGIN CERTIFICATE——-， ——-END CERTIFICATE——-] 的内容作为证书上传。

私钥转换：私钥一般在 IIS 服务器里可导出。

### 3.3 PFX 格式证书转换为 PEM 格式

PFX 格式一般出现在 Windows Server 中。

证书转换：```openssl pkcs12 -in certname.pfx -nokeys -out cert.pem```

私钥转换：```openssl pkcs12 -in certname.pfx -nocerts -out key.pem -nodes```	

### 3.4 CER/CRT 格式证书转换为 PEM 格式

对于 CER/CRT 格式的证书，您可通过直接修改证书文件扩展名的方式进行转换。例如，将 “servertest.crt” 证书文件直接重命名为 “servertest.pem” 即可。
