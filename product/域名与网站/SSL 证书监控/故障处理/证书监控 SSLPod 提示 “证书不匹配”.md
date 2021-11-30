

## 现象描述
在证书监控 SSLPod 中添加站点后提示 “证书不匹配”。如下图所示：
![](https://main.qcloudimg.com/raw/077156d7a1aa45694b83ef504697993a.png)


## 可能原因
您添加的站点与证书监控 SSLPod 监控到的 SSL 证书不匹配。例如：您添加的站点为 `bbs.dnspod.cn`，但证书监控 SSLPod 监控到的 SSL 证书为 `cloud.dnspod.cn`。

## 解决思路

检查站点绑定的 SSL 证书是否正确。若您添加的监控类型为 `HTTPS`，您可参考以下步骤进行检查：

1. 使用浏览器访问您的站点并单击<span ><img src="https://main.qcloudimg.com/raw/fd45b838ed9e4b11c9d02f8bc66e6625.png" style="margin-bottom:-3px;"/></span> 。如下图所示：
![](https://main.qcloudimg.com/raw/205cd42ecc99285a127197ab3807a4a6.png)
2. 在展开的信息框中，单击**证书**。如下图所示：
![](https://main.qcloudimg.com/raw/9301bb174a945857f85bbba760f6ed3d.png)
3. 在弹出的 “证书” 窗口中，查看**颁发给**显示的域名是否与站点一致。如下图所示：
![](https://main.qcloudimg.com/raw/84bbf3d1b59348cde3927817e176c450.png)
 - 若显示不一致，请将您网站的 SSL 证书安装部署为正确的 SSL 证书。SSL 证书安装部署操作请参考 [如何选择 SSL 证书安装部署类型？](https://cloud.tencent.com/document/product/400/4143)
 - 若显示一致，您可通过 [联系我们](https://cloud.tencent.com/document/product/1084/59538) 寻求帮助。

>?监控类型非 `HTTPS`，请根据监控类型排查对应的应用端 SSL 证书是否安装正确。一般情况下 SMTP、IMAP、POP3、TLS 监控类型应用于电子邮件，您可检查您的电子邮件 SSL 服务是否设置正确，具体详情请咨询您的电子邮件商。











