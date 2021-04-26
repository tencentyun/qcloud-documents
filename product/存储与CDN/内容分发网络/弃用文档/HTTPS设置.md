HTTPS 是指超文本传输安全协议（Hypertext Transfer Protocol Secure），是一种在 HTTP 协议基础上进行传输加密的安全协议，能够有效保障数据传输安全。配置 HTTPS 时，需要您提供域名对应的证书，将其部署在全网 CDN 节点，实现全网数据加密传输功能。

>?
> - **对象存储**或**万象优图**服务开启 CDN 加速后，默认的`.file.myqcloud.com`后缀域名，或`.image.myqcloud.com`后缀域名，可直接支持 HTTPS 请求，无需配置证书。
> - 腾讯云 CDN 目前针对 HTTP2.0 协议支持已经全面公测，可直接开启使用。

## 配置指引
腾讯云 CDN 目前支持两种方式部署证书。
- 自有证书：将自有证书、私钥内容上传至 CDN 进行部署，全程加密传输，证书不落地，保障您的证书安全。
- 腾讯云托管证书：您可以通过 [SSL 证书管理](https://console.cloud.tencent.com/ssl)，将已有证书托管至腾讯云，以用于多个云产品，您也可以在该平台申请由亚洲诚信免费提供的第三方证书，将其直接部署至 CDN。


1. 登录 [CDN 控制台](https://console.cloud.tencent.com/cdn)，单击左侧目录的【域名管理】，进入管理页面，在列表中找到您需要编辑的域名所在行，单击操作栏的【管理】。
![img](https://main.qcloudimg.com/raw/f7f2871e66214431430af7c4e508e29a.png)
2. 单击【高级配置】，找到 **HTTPS 配置**模块。单击【前往配置】，跳转至**证书管理**页面配置证书。配置流程请参见 [证书管理](https://cloud.tencent.com/document/product/228/6303)。
![img](https://main.qcloudimg.com/raw/5c11cea6df9309c96856c352c3b94d23.png)
3. 证书**配置成功**后，会出现【强制跳转 HTTPS】开关，默认情况下，强制跳转 HTTPS为关闭状态。
![img](https://main.qcloudimg.com/raw/1de2e0e330cc65ced62bd5d351379d43.png)
4. 开启【强制跳转 HTTPS】后，即使用户发起 HTTP 请求，也会强制跳转为 HTTPS 请求进行访问。默认情况下，跳转方式为302。
![image](https://main.qcloudimg.com/raw/9d5fb1d152c3aa781b0f1eaca1f3211a.png)
可单击【编辑】修改跳转方式：
![image](https://main.qcloudimg.com/raw/cbd93a57a01478d44f9a6ec067e91e83.png)

## HTTP2.0 配置

在成功为域名配置了 HTTPS 证书后，可以开启 HTTP2.0。
![img](https://main.qcloudimg.com/raw/e55814078f908119c2876cd545c62b4d.png)
了解更多 HTTP2.0 相关特性，请参见 [HTTP2.0 的新特性](https://cloud.tencent.com/community/article/541321)。

## OCSP 装订配置
**功能说明**
OCSP 装订（OCSP Stapling，TLS 证书状态查询扩展）。OCSP Stapling 服务器在 TLS 握手时可将已经缓存好的 OCSP 查询结果发送给客户端，供用户验证，而不用让客户端自己向 CA 发送请求。OCSP 装订极大地提高了 TLS 握手效率，节省了用户验证时间。

在成功为域名配置了 HTTPS 证书后，可以开启 OCSP 装订。
![image](https://main.qcloudimg.com/raw/fcaee8ad06ea02f5fcdb7ad1d39b0bff.png)


## HTTPS 回源支持的算法

目前 HTTPS 回源可支持的算法如下表所示（顺序无先后之分）：

| ECDHE-RSA-AES256-SHA   | ECDHE-RSA-AES256-SHA384   | ECDHE-RSA-AES256-GCM-SHA384   |
| ---------------------- | ------------------------- | ----------------------------- |
| ECDHE-ECDSA-AES256-SHA | ECDHE-ECDSA-AES256-SHA384 | ECDHE-ECDSA-AES256-GCM-SHA384 |
| SRP-AES-256-CBC-SHA    | SRP-RSA-AES-256-CBC-SHA   | SRP-DSS-AES-256-CBC-SHA       |
| DH-RSA-AES256-SHA      | DH-RSA-AES256-SHA256      | DH-RSA-AES256-GCM-SHA384      |
| DH-DSS-AES256-SHA      | DH-DSS-AES256-SHA256      | DH-DSS-AES256-GCM-SHA384      |
| DHE-RSA-AES256-SHA     | DHE-RSA-AES256-SHA256     | DHE-RSA-AES256-GCM-SHA384     |
| DHE-DSS-AES256-SHA     | DHE-DSS-AES256-SHA256     | DHE-DSS-AES256-GCM-SHA384     |
| CAMELLIA256-SHA        | DH-RSA-CAMELLIA256-SHA    | DHE-RSA-CAMELLIA256-SHA       |
| PSK-3DES-EDE-CBC-SHA   | DH-DSS-CAMELLIA256-SHA    | DHE-DSS-CAMELLIA256-SHA       |
| ECDH-RSA-AES256-SHA    | ECDH-RSA-AES256-SHA384    | ECDH-RSA-AES256-GCM-SHA384    |
| ECDH-ECDSA-AES256-SHA  | ECDH-ECDSA-AES256-SHA384  | ECDH-ECDSA-AES256-GCM-SHA384  |
| AES256-SHA             | AES256-SHA256             | AES256-GCM-SHA384             |
| ECDHE-RSA-AES128-SHA   | ECDHE-RSA-AES128-SHA256   | ECDHE-RSA-AES128-GCM-SHA256   |
| ECDHE-ECDSA-AES128-SHA | ECDHE-ECDSA-AES128-SHA256 | ECDHE-ECDSA-AES128-GCM-SHA256 |
| SRP-AES-128-CBC-SHA    | SRP-RSA-AES-128-CBC-SHA   | SRP-DSS-AES-128-CBC-SHA       |
| DH-RSA-AES128-SHA      | DH-RSA-AES128-SHA256      | DH-RSA-AES128-GCM-SHA256      |
| DH-DSS-AES128-SHA      | DH-DSS-AES128-SHA256      | DH-DSS-AES128-GCM-SHA256      |
| DHE-RSA-AES128-SHA     | DHE-RSA-AES128-SHA256     | DHE-RSA-AES128-GCM-SHA256     |
| DHE-DSS-AES128-SHA     | DHE-DSS-AES128-SHA256     | DHE-DSS-AES128-GCM-SHA256     |
| ECDH-RSA-AES128-SHA    | ECDH-RSA-AES128-SHA256    | ECDH-RSA-AES128-GCM-SHA256    |
| ECDH-ECDSA-AES128-SHA  | ECDH-ECDSA-AES128-SHA256  | ECDH-ECDSA-AES128-GCM-SHA256  |
| CAMELLIA128-SHA        | DH-RSA-CAMELLIA128-SHA    | DHE-RSA-CAMELLIA128-SHA       |
| PSK-RC4-SHA            | DH-DSS-CAMELLIA128-SHA    | DHE-DSS-CAMELLIA128-SHA       |
| AES128-SHA             | AES128-SHA256             | AES128-GCM-SHA256             |
| SEED-SHA               | DH-RSA-SEED-SHA           | DH-DSS-SEED-SHA               |
| DES-CBC3-SHA           | DHE-RSA-SEED-SHA          | DHE-DSS-SEED-SHA              |
| IDEA-CBC-SHA           | PSK-AES256-CBC-SHA        | PSK-AES128-CBC-SHA            |
| EDH-RSA-DES-CBC3-SHA   | ECDH-RSA-DES-CBC3-SHA     | ECDHE-RSA-DES-CBC3-SHA        |
| EDH-DSS-DES-CBC3-SHA   | ECDH-ECDSA-DES-CBC3-SHA   | ECDHE-ECDSA-DES-CBC3-SHA      |
| RC4-SHA                | ECDH-RSA-RC4-SHA          | ECDHE-RSA-RC4-SHA             |
| RC4-MD5                | ECDH-ECDSA-RC4-SHA        | ECDHE-ECDSA-RC4-SHA           |
| SRP-3DES-EDE-CBC-SHA   | SRP-RSA-3DES-EDE-CBC-SHA  | SRP-DSS-3DES-EDE-CBC-SHA      |
| DH-DSS-DES-CBC3-SHA    | DH-RSA-DES-CBC3-SHA       | -                             |
