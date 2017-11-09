无法使用 TCP 25 端口连接外部地址。例如，运行`Telnet smtp.***.com 25`，该命令执行失败，但是安全组并没有禁止该端口。

**原因：**为了提升腾讯云 IP 地址发邮件的质量，将默认限制云主机 TCP 25 端口连接外部地址 。

**解封方法：**登录腾讯云控制台，鼠标移动到账号，即见 **25 端口解封** 入口，每个客户在每个地域默认可解封 5 个云服务器。

![](https://mc.qcloudimg.com/static/img/fa9add630c9defc5b005cd0d820d4824/Image.png)
25 端口主要用于 SMTP 邮件服务器的架设，如果您没有在云上部署邮件服务，则本次端口封堵不会对您的服务造成影响；如果您在云主机中使用 25 端口部署了邮件服务，则您的邮件服务将受到影响而暂时不可用。

我们诚挚地推荐您使用腾讯企业邮箱（exmail.qq.com）代替云上的 SMTP 邮件服务，来提高业务的整体安全性。如果您一定要保留云上的 SMTP 服务，请优先在云主机内安装相关安全工具，如 [云镜](https://cloud.tencent.com/document/product/296/9927)，进行相风险控制。
> **注意：**
如果您发起解封申请，腾讯云将默认您已确认并承诺：保证 TCP 25 端口仅用来连接第三方的 SMTP 服务器，并从第三方的 SMTP 服务器向外发邮件。如发现您使用申请的 IP 直接通过 SMTP 发送邮件，腾讯云有权永久性封禁 TCP 25 端口，并不再提供解封服务，如有其它问题，请提 [工单申请](https://console.cloud.tencent.com/workorder/category/create?level1_id=6&level2_id=7&level1_name=%E8%AE%A1%E7%AE%97%E4%B8%8E%E7%BD%91%E7%BB%9C&level2_name=%E4%BA%91%E6%9C%8D%E5%8A%A1%E5%99%A8%20CVM)。
