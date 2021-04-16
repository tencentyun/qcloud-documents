
## 操作场景
自定义 DNS Host，是指使用当前域名创建 DNS 服务器，即可由您创建的 DNS 服务器提供 DNS 解析服务。本文将指导您如何添加 DNS Host。

>?
>- 如果使用 DNS Host 来解析域名，必须在对应域名服务器上添加对应 A 记录（IP 地址保持一致）。
>- 一个域名下，最多创建 10 个 DNS Host。
>- 创建 DNS Host 时，至少需要填写1个 IP 地址，最多可填写13个 IP 地址。
>- 创建 DNS Host 成功后，不允许修改名称，只能删除后新建。


## 操作指南
1. 登录 [腾讯云域名注册管理控制台](https://console.cloud.tencent.com/domain)，单击您需要设置自定义 DNS Host 的域名，即可进入 “域名信息” 页面。
2. 在 “域名信息” 页面，选择【自定义 DNS Host】页签。
3. 在 “自定义 DNS Host” 中， 您可以通过以下两种方式添加自定义 DNS Host。如下图所示：
![](https://main.qcloudimg.com/raw/c6ac5a3090919bd81c9d0dfef4719cf9.png)
 - **添加 DNS Host**：可通过手动输入方式进行添加。
 - **同步 DNS Host**：将注册局已有的 DNS Host （在其他注册商平台填写过）同步至腾讯云控制台。

### 添加 DNS Host
1. 单击【添加 DNS Host】，在弹出的 “创建 DNS Host 窗口” 中，填写相关信息。
![](https://main.qcloudimg.com/raw/7e73f40ef884485831b46a0a7cfdaaa2.png)
 - DNS Host：请输入 DNS Host 的子域名称。
 - IP 地址：请输入您的服务器 IP 地址。
2. 填写完成后，单击【提交】，即可完成添加。
>!为了使添加的 DNS Host 生效，请在对应设置 DNS Host 的域名添加 A 记录。详情请查看 [A 记录](https://cloud.tencent.com/document/product/302/3449)。

### 同步 DNS Host
如您在其他注册商平台填写过 DNS Host 地址，单击【同步 DNS Host】，即可将注册局已有的 DNS Host 同步到腾讯云控制台。
![](https://main.qcloudimg.com/raw/a0fea451386a96eaf5916cc445b935c7.png)
