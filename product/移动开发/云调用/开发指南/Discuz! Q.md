

云开发支持一键部署 [Discuz!Q](https://discuz.com/) 应用。通过云托管结合静态网站托管、共享文件存储 CFS、云数据库 CynosDB for Mysql 等各项云计算资源能力，为您提供高性能、高可靠性、可弹性扩缩容的的应用体验。

|方案特性|介绍	|
|--| -- | 
|省钱|云托管没有流量可缩容到0；存储按实际存储容量计费。无需为闲时资源买单。按量付费，无需预先支出|
|省心|Serverless 无服务器化，架构弹性可自动扩缩容，无需担心网站崩溃|
|更快	|用户发帖上传的图片与附件，享受 CDN 节点就近加速分发|
|更便捷	|自带三级域名可以快速访问，无需通过 IP 访问|


## 适用场景

- 不具备专业的运维开发人员的个人站长，无需预估业务规模，可自动扩缩容。
- 访问流量不稳定，无流量时，云托管将自动缩容到0，减少成本。
- 对数据安全要求敏感的行业，数据独立存储在专业的云数据库 CynosDB for Mysql 中。

## 部署架构配置

|资源	|架构	|
|--| -- | 
|[云托管](https://cloud.tencent.com/document/product/1243)	|默认配置0.25核0.5G内存的容器，伸缩范围0 - 4个实例，遇到 CPU 负载大于60将会进行扩容。无流量则会缩容到0，不产生费用 |
|[静态网站托管](https://cloud.tencent.com/document/product/1210)	| 按照实际容量与流量付费|
|[共享文件存储（Cloud File Storage，CFS）](https://cloud.tencent.com/document/product/582)|按照实际容量付费，DAU 1000的站点预估消耗量在5GB以下|
|[云数据库 CynosDB for Mysql](https://cloud.tencent.com/document/product/1003)|数据库1C1G，存储按照容量计费|

安装 Discuz! Q 资源配置架构图如下：
![架构图](https://main.qcloudimg.com/raw/441da6affa73b708ebafa0b7eb26efdd.png)


## 常见问题
#### 小程序部署

小程序的部署需要单独提审，安装完本扩展应用后，需要参考 [构建/发布Discuz! Q小程序与 H5 前端](https://discuz.com/docs/uniapp_hbuilderx.html#%E4%BD%BF%E7%94%A8%E6%96%B9%E6%B3%95) 进行构建发布小程序端的代码。

#### 公众号白名单 IP 配置

公众号登录开通时，需要将服务的 IP 添加到公众号的 IP 白名单中，详情请参见 [第三方登录设置](https://discuz.com/manual-admin/2.html#_2-3-%E7%AC%AC%E4%B8%89%E6%96%B9%E7%99%BB%E5%BD%95%E8%AE%BE%E7%BD%AE)。

1. 在扩展应用详情页页 API 和资源模块中，单击云托管的服务详情。
![查看云托管服务](https://main.qcloudimg.com/raw/e210b5f23304867805926e3c3a4bb07e.png)
2. 单击【服务配置】，查看服务的出口 NAT IP。
![NAT IP](https://main.qcloudimg.com/raw/e9b4724b662b52230b7ce5ca5ff270db.png)

#### 版本升级

云开发会定期跟踪 Discuz! Q 的版本更新，为您推送版本升级，可一键完成升级操作。

#### 复用已有 CynosDB 集群

本应用会选取当前环境所处地域下的集群名为 DiscuzCynosDB 的集群，如果不存在，则会创建新的集群。如果希望复用已有 CynosDB 集群，可变更集群名。

同理，CFS 也会创建名称为 DiscuzCfs 的一块磁盘。

## 其他
### 程序配置信息

您可以通过以下配置参数：
* 环境 ID：选择需要部署的环境，在哪个环境下使用。
* 管理员用户名：Discuz! Q 后台管理系统的管理员用户名，默认为 admin。
* 管理员密码：Discuz! Q 后台管理系统的管理员密码，第一次安装时，会设置并加密存储在数据库内，之后变更请前往管理系统的用户管理面板重置密码，详情请参见 [用户管理](https://discuz.com/manual-admin/3.html#_3-1-%E7%94%A8%E6%88%B7%E7%AE%A1%E7%90%86)。
* 数据库用户名：默认为 root，当前不可修改。
* 数据库密码：root 账号的密码，初次安装时设置后将作为初始化的密码创建 CynosDB。后续修改密码请前往 CynosDB 控制台的账号管理页面，修改密码后，请同步修改此处的密码，以保证数据库的正常使用。

### 计费

此能力使用云开发与其他腾讯云服务，可能会产生相关费用。云开发与云上其他资源分开计费，您可以在 [费用中心](https://console.cloud.tencent.com/expense/overview) 查看具体信息。

1. 云托管（[产品定价](https://cloud.tencent.com/document/product/1003/30493) 及 [使用明细](https://console.cloud.tencent.com/tcb)）。
2. 静态网站托管（[产品定价](https://cloud.tencent.com/document/product/876/39095) 及 [使用明细](https://console.cloud.tencent.com/tcb)）。
3. 文件存储（Cloud File Storage，CFS）（[产品定价](https://cloud.tencent.com/document/product/582/47378) 及 [使用明细](https://console.cloud.tencent.com/cfs/overview)）。
4. 云数据库 CynosDB for MySQL（[产品定价](https://cloud.tencent.com/document/product/1003/30493) 及 [使用明细](https://console.cloud.tencent.com/cynosdb)）。
