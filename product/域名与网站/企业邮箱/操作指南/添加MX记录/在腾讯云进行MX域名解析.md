## 操作场景
为让您邮箱能收到邮件，请添加 MX 记录。本文档指导您如何添加 MX 记录。

## 操作步骤
1. 登录 [腾讯云 DNS 解析控制台](https://console.cloud.tencent.com/cns)。
2. 在 “域名解析列表” 中，选择需要进行 MX 记录转发的域名，单击操作栏的**解析**，进入该域名的**记录管理**页面。如下图所示：
![](https://main.qcloudimg.com/raw/bae548136e4d3090a675ecb8597573f6.png)
3. 单击**添加记录**，填写以下记录信息。
 - 主机记录：填写子域名，通常选择 “@” 或 “mail”。例如，如果 “主机记录” 选择 “@”，邮箱地址是` xxx@123.com`。如果 “主机记录” 选择 “mail”，邮箱地址会变为 ` xxx@mail.123.com`。
 - 记录类型：选择 “MX”。
 - 线路类型：选择 “默认” 类型，否则会导致部分用户无法解析，邮件无法收取；MX 一般不需要做智能解析，直接默认即可。
 - 记录值：可以是域名，也可以是一个 IP 地址。通常为邮件服务器域名或邮件服务器 IP。例如腾讯企业邮 mxbiz1.qq.com 和 mxbiz2.qq.com 。
 - TTL：为缓存时间，数值越小，修改记录各地生效时间越快，默认为600秒。
 - MX 优先级：数值越低，优先级别就越高。
    - 邮件会先尝试发送到 MX 优先级为5的 `mxbiz1.qq.com`。
![](https://main.qcloudimg.com/raw/1aa0c9695cb90dcb00f8afd8cc4837f1.png)
    - 如果尝试失败，邮件会发送到 MX 优先级为10的 `mxbiz2.qq.com`。
![](https://main.qcloudimg.com/raw/9afc6671fb9e9e4c3a3e31db65ba7fc3.png)
4. 单击**保存**，完成添加。
