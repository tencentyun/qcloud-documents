## iOS 证书命令

证书有效期
```
openssl x509 -in xxx.pem -noout -dates
```
连接 APNS 测试证书是否合法

1. 开发环境
```
openssl s_client -connect gateway.sandbox.push.apple.com:2195 -cert xxx.pem -key xxx.pem
```
2. 生产环境
```
openssl s_client -connect gateway.push.apple.com:2195 -cert xxx.pem -key xxx.pem
```
## 指南介绍

本指南用于介绍 iOS 证书如何设置

配置好证书后请前往 iOS SDK 完整接入



### 设置步骤

首先，登录 [苹果开发者中心网站](https://Developer.apple.com/account)。然后点击 Certificates,Identifiers & Profiles
![开发者网站](http://developer.qq.com/wiki/xg/imgs/20151118164839_43490.jpg)


然后点击 Certificates
![Certificates](http://developer.qq.com/wiki/xg/imgs/20151118164854_57803.jpg)


选中需要制作 Push 证书的应用，勾选 Push 服务

![制作证书](http://developer.qq.com/wiki/xg/imgs/20151118165407_29483.jpg)

下面以制作开发证书为例演示。点击 Create Certificate…
![Create Certificate](http://developer.qq.com/wiki/xg/imgs/20151110192434_69196.png)
![create certificate2](http://developer.qq.com/wiki/xg/imgs/20151118170034_31723.jpg)


然后打开 Keychain Access 工具
![Keychain Access](http://developer.qq.com/wiki/xg/imgs/20151118170223_56259.jpg)

 选择 Request a Certificate From a Certificate Authority…
 ![Request a certificate From a certificate authority](http://developer.qq.com/wiki/xg/imgs/20151118170327_87514.jpg)

填写邮件地址，其它留空，继续，证书将保存到本地
![Fill email address](http://developer.qq.com/wiki/xg/imgs/20151110193013_44930.png)


返回网站，选择刚才创建的文件上传

![Upload Certificate](http://developer.qq.com/wiki/xg/imgs/20151118170443_25583.jpg)

成功后，下载到本地
![Download Certificate](http://developer.qq.com/wiki/xg/imgs/20151118170536_85822.jpg)

再次打开Keychain Access。选中 Push 证书导出，选中一行，导出的格式为 p12

![Keychain Access export p12](http://developer.qq.com/wiki/xg/imgs/20151118170642_42628.jpg)

### 生成 pem 格式的证书

完成上述操作后，打开终端，进入到 p12 文件所在执行以下命令:
```
openssl pkcs12 -in CertificateName.p12 -out CertificateName.pem -nodes
```
则生成了 CertificateName.pem 证书，上传到移动开发平台（MobileLine）控制台则可以进行消息推送。
