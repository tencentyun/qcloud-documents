## 一键 HTTPS 套餐即将到期如何处理？
若您需继续使用一键 HTTPS 功能，您可前往腾讯云 [SSL 证书管理控制台](https://console.cloud.tencent.com/https) 进行续费升级操作。详情请参见 [一键 HTTPS 续费流程](https://cloud.tencent.com/document/product/400/67311)。

若您不再继续使用，建议您在一键 HTTPS 套餐到期前将接入域名解析切换至源站，避免套餐到期后影响正常访问。若您的接入域名在 DNSPod 进行解析，您可参考以下步骤进行操作：

1. 登录 [DNSPod DNS 解析管理控制台](https://console.dnspod.cn/dns/list)。
2. 单击您在一键 HTTPS 接入的**域名**，进入 “记录管理” 页面。
3. 查找接入域名的 CNAME 记录类型，并将记录值修改为您的源站地址。如下图所示：
>!若您的源站地址为 IP 地址，请将记录类型修改为 A 记录并在记录值处填写您的源站 IP 地址。
>
![](https://qcloudimg.tencent-cloud.cn/raw/e5dba6791502ba152b4a95b2e047e181.png)
3. 单击**确认**，即可完成设置。





