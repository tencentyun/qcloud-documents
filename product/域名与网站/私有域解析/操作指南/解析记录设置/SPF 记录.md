## 操作场景
SPF 记录用于指定发送邮件的服务器，是一种高效的反垃圾邮件解决方案。本文档指导您如何添加 SPF 记录。

## 前提条件
已创建对应的私有域。详情请查看 [创建私有域](https://cloud.tencent.com/document/product/1338/50532)。

## 操作步骤
1. 登录私有域解析 [Private DNS 管理控制台](https://console.cloud.tencent.com/privatedns/)，并单击左侧导航栏的**私有域列表**，即可进入私有域列表。
2. 在 “私有域列表” 中，单击您需要添加 SPF 记录的私有域名称或**解析**。如下图所示：
![](https://main.qcloudimg.com/raw/965b35507b9de90112d57608a95d6405.png)
3. 在**解析记录**页签中，单击**添加记录**并填写相关记录值信息。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/26e7e57467802ae9becc9dabaf685278.png)
 - **主机记录**：填写子域名。例如，添加 `www.123.com` 的 SPF 记录，您在 “主机记录” 处选择 “www” 即可。如果只是想添加 `123.com` 的 SPF 记录，您在 “主机记录” 处选择 “@” 即可。
 - **记录类型**：选择 “SPF”。
 - **记录值**：例如 `v=spf1 include:spf.mail.qq.com ~all`，表示只有这个域名的 A 记录和 MX 记录中的 IP 地址有权限使用这个域名发送邮件。
 - **权重**：不需要填写。 
 - **MX 优先级**：不需要填写。 
 - **TTL**：为缓存时间，数值越小，修改记录生效时间越快，默认设置为300，支持自定义1 - 86400区间的整数。
4. 单击**保存**，完成添加。

>?操作过程中如果出现问题，请您 [联系我们](https://cloud.tencent.com/act/event/connect-service)。




