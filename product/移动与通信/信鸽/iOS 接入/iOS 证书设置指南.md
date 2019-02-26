##  iOS 证书命令
#### 证书有效期
```
openssl x509 -in xxx.pem -noout -dates
```
#### 连接 APNS 测试证书是否合法
1. 开发环境：
```
openssl s_client -connect gateway.sandbox.push.apple.com:2195 -cert xxx.pem -key xxx.pem
```
2. 生产环境：
```
openssl s_client -connect gateway.push.apple.com:2195 -cert xxx.pem -key xxx.pem
```

## 指南介绍
本指南用于介绍 iOS 证书如何设置，配置好证书后请前往 iOS SDK 完整接入。
### 设置步骤

**第一步：**登录苹果开发者中心网站。然后单击 Certificates,Identifiers & Profiles
![](//mc.qcloudimg.com/static/img/13a636325558df6da436d28301e907e3/image.jpg)
**第二步：** 单击 Certificates
![](//mc.qcloudimg.com/static/img/13a636325558df6da436d28301e907e3/image.jpg)
**第三步：**选中需要制作 Push 证书的应用，勾选 Push 服务
![](//mc.qcloudimg.com/static/img/47598fc9cf98c77fed1c91aa55c1b88e/image.jpg)
**第四步：**下面以制作开发证书为例演示。
点击 Create Certificate…
![](//mc.qcloudimg.com/static/img/912a8d77242160b02ef102ebb4e3307c/image.png)
![](//mc.qcloudimg.com/static/img/2f8ba124babf0a925c3f0aa96bfd1bdb/image.jpg)
然后打开 Keychain Access 工具
![](//mc.qcloudimg.com/static/img/eee2ebb09a60acfb9509fe30c02b9e2d/image.jpg)
Request a Certificate From a Certificate Authority… 
![](//mc.qcloudimg.com/static/img/66e99c2d806d0d1d59f9fd93d940bc3a/image.jpg)
填写邮件地址，其它留空, 继续。会将证书保存到本地
![](//mc.qcloudimg.com/static/img/61f00eed1371c2ef791dff672545e899/image.png)
返回网站，选择刚才创建的文件上传
![](//mc.qcloudimg.com/static/img/c62bc18cdcb019a62f4ef73cedff8691/image.jpg)
成功后，下载到本地![](//http://developer.qq.com/wiki/xg/imgs/20151118170536_85822.jpg) 

再次打开 Keychain Access。选中 Push 证书导出，选中一行。导出的格式为 p12
![](//mc.qcloudimg.com/static/img/cadb2f416989d37fa517fa27defb21b6/image.jpg)

### 生成 pem 格式的证书
完成上述操作后，打开终端，进入到 p12 文件所在执行以下命令:
```
openssl pkcs12 -in CertificateName.p12 -out CertificateName.pem -nodes
```
则生成了 CertificateName.pem 证书，上传到信鸽则可以进行消息推送。
详细 iOS SDK 相关开发信息请前往 [iOS SDK V2.5.0 完整接入](https://cloud.tencent.com/document/product/548/13270) 或 [iOS SDK V3.0.0 完整接入](https://cloud.tencent.com/document/product/548/13274)。




