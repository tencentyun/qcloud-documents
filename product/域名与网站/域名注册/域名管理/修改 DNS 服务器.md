## 操作场景
若您注册的域名需添加解析，则需将域名的托管至 DNS 解析商后才可正常解析。本文将指导您如何通过修改 DNS 服务器地址方式指定对应的 DNS 服务解析商。

>? 您在腾讯云新注册的域名 DNS 服务器地址默认为 DNSPod 免费套餐对应的 DNS 服务器地址，若您不需要升级套餐，则无需调整 DNS 服务器地址。

## 操作步骤
如果域名在腾讯云注册，或者已转入腾讯云，可以通过以下步骤修改 DNS 服务器：
1. 登录 [腾讯云域名注册控制台](https://console.cloud.tencent.com/domain/)，进入 “我的域名” 页面。
2. 选择待修改 DNS 的域名，单击**管理**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/cec42b283df9cbb37f1855db914f7bb6.png)
3. 在 “基本信息” 栏中，单击 “DNS 服务器” 的**修改**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/46f554f0f1c6a0299b2acf9860774253.png)
4. 在弹出的 “修改 DNS 服务器” 窗口中，选择您需要修改域名 DNS 服务器方式。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/d5eb5e4e76abc8dd0c5c00c128c688a7.png)
 - **使用 DNSPod**：自动为该域名匹配 DNSPod 服务器的 DNS 地址。
 - **自定义 DNS**： 填写您需要设置的 DNS 服务器地址。
>? 
>- 自定义的 DNS 服务器域名不能是私建的 DNS 服务器域名，必须是解析商的权威 DNS 服务器域名。
>- 需要在腾讯云进行解析的域名，修改 DNS 服务器地址请参考 [各个套餐对应的 DNS 服务器地址](https://cloud.tencent.com/document/product/302/9070)。
