## 证书监控 SSLPod 提示“证书不匹配”

### 故障描述
在证书监控 SSLPod 中添加站点后提示提示“证书不匹配”。如下图所示：

![](https://main.qcloudimg.com/raw/077156d7a1aa45694b83ef504697993a.png)


### 故障原因
您添加的站点与证书监控 SSLPod 监控到的SSL 证书与添加的站点不匹配。如：您添加的站点为 `bbs.dnspod.cn`。证书监控 SSLPod 监控到的 SSL 证书为 `cloud.dnspod.cn`。

### 排查思路

排查站点绑定的 SSL 证书是否正确。若您添加的监控类型为 `HTTPS`，您可参考以下步骤进行检查：

1. 使用浏览器访问您的站点并单击 ![](https://main.qcloudimg.com/raw/84291e4afb4141381733e73e8fb6495d.png) 图标。

![](https://main.qcloudimg.com/raw/205cd42ecc99285a127197ab3807a4a6.png)

2. 在展开的信息框中，单击**证书**。

![](https://main.qcloudimg.com/raw/9301bb174a945857f85bbba760f6ed3d.png)

3. 打开的“证书”窗口中，查看**颁发给**字段与站点是否一致。

![](https://main.qcloudimg.com/raw/84bbf3d1b59348cde3927817e176c450.png)

4. 若不一致，请将您网站的 SSL 证书安装部署为正确的 SSL 证书。SSL 证书安装部署操作您可参考：[如何选择 SSL 证书安装部署类型？](https://cloud.tencent.com/document/product/400/4143)

>? 若一致您可通过 [技术支持](链接) 联系我们寻求帮助。

监控类型非为 `HTTPS`，请根据您的监控类型排查对应应用端 SSL 证书是否安装正确。一般情况下 SMTP、IMAP、POP3、TLS 监控类型应用于电子邮件。您可检查您的电子邮件 SSL 服务是否设置正确，具体详情您可咨询您的电子邮件商。











