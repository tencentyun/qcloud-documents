云开发支持一键部署 [Discuz! Q](https://discuz.com/) 应用。通过云托管结合静态网站托管、共享文件存储 CFS、云数据库 CynosDB for MySQL 等各项云计算资源能力，为您提供高性能、高可靠性、可弹性扩缩容的的应用体验。

| 方案特性 | 介绍                                                                                         |
| -------- | -------------------------------------------------------------------------------------------- |
| 省钱     | 云托管没有流量可缩容到 0；存储按实际存储容量计费。无需为闲时资源买单。按量付费，无需预先支出 |
| 省心     | Serverless 无服务器化，架构弹性可自动扩缩容，无需担心网站崩溃                                |
| 更快     | 用户发帖上传的图片与附件，享受 CDN 节点就近加速分发                                          |
| 更便捷   | 自带三级域名可以快速访问，无需通过 IP 访问                                                   |

## 适用场景

- 不具备专业的运维开发人员的个人站长，无需预估业务规模，可自动扩缩容。
- 访问流量不稳定，无流量时，云托管将自动缩容到 0，减少成本。
- 对数据安全要求敏感的行业，数据独立存储在专业的云数据库 CynosDB for MySQL 中。

## 部署架构配置

| 资源                                                                                      | 架构                                                                                                                       |
| ----------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| [云托管](https://cloud.tencent.com/document/product/1243)                                 | 默认配置 0.25 核 0.5G 内存的容器，伸缩范围 0 - 4 个实例，遇到 CPU 负载大于 60 将会进行扩容。无流量则会缩容到 0，不产生费用 |
| [静态网站托管](https://cloud.tencent.com/document/product/1210)                           | 按照实际容量与流量付费                                                                                                     |
| [文件存储（Cloud File Storage，CFS）](https://cloud.tencent.com/document/product/582) | 按照实际容量付费，DAU 1000 的站点预估消耗量在 5GB 以下                                                                     |
| [云数据库 CynosDB for MySQL](https://cloud.tencent.com/document/product/1003)             | 数据库 1C1G，存储按照容量计费                                                                                              |

安装 Discuz! Q 资源配置架构图如下：
![架构图](https://main.qcloudimg.com/raw/441da6affa73b708ebafa0b7eb26efdd.png)

## 安装流程

1. 登录 [云开发控制台](https://console.cloud.tencent.com/tcb/env/index)。
2. 单击**新建环境**，新建一个**按量计费**环境，详情可参见 [开通环境](https://cloud.tencent.com/document/product/876/41391) 文档。
3. 环境创建完后，单击**环境卡片**，进入环境管理页面。
4. 单击左侧导航栏底部的 **[扩展应用](https://console.cloud.tencent.com/tcb/extensions/index)**，在更多扩展能力中，可以看到 Discuz! Q 应用。
   ![disucz入口](https://main.qcloudimg.com/raw/69482ddda7cc18bf2fbc15d559417578.png)
5. 在 Discuz! Q 应用中，单击**安装**，进入扩展安装流程。
   - 确认应用相关资源
   - 授予云开发相关资源的操作权限
   - 扩展云资源准备，声明会依赖的 2 个资源(文件存储、云数据库)
   - 扩展程序配置，请勿长期使用默认的密码，注意**修改密码**，避免管理后台被他人登录
     ![disucz安装](https://main.qcloudimg.com/raw/81bb3905d3972d4f298b9c1fbc551944.png)
6. 已安装列表里显示 Discuz! Q 应用正在安装中，安装完成后单击可进入详情页。
7. 详情页内，可以查看 Discuz! Q 的访问地址。
   ![discuz详情页](https://main.qcloudimg.com/raw/009a5504f4f2f439f53ee5ae2478be1c.png)

## 部署异常

安装过程中可能遇到一些异常，请根据异常提示查看以下解决方案进行解决。如果遇到无法解决的问题，请 [提交工单](https://console.cloud.tencent.com/workorder/category) 联系我们，我们将协助您解决。
![安装异常](https://main.qcloudimg.com/raw/1e8022496f7c221a6f84fa02ddd5859e.png)

### 账户余额不足

Discuz! Q 应用创建时，会一同创建云数据库 CynosDB for MySQL。创建数据库资源会预先扣 1 个小时的费用，为了保证服务的可用，推荐先 [充值腾讯云账户](https://console.cloud.tencent.com/expense/recharge) 5 元钱。

### HTTP 访问服务 “/” 路径已经被占用

Discuz! Q 将会占用 “/” 路径，如果当前环境的 “/” 已经被占用，推荐再创建一个按量计费环境进行安装。

### CynosDB 被隔离

错误信息 `queryClusterDetail failed, err=DescribeClusters invalid response.detail.status[isolated]`，代表 CynosDB 集群被隔离，请前往[回收站](https://console.cloud.tencent.com/cynosdb/recycle)将该集群恢复或者直接删除。

### 共享文件存储 CFS 资源售罄

错误信息：”参数值错误：该地域无法提供服务“，代表 共享文件存储 CFS 该地域可用区售罄。我们将及时补货，请耐心等待。

### 部署异常后，但是资源已经创建

Discuz! Q 涉及资源较多，过程中可能产生异常。顺序为先创建 CFS、CynosDB for MySQL 资源，再开通云托管。
CFS 是按照存储量计费，没有存储数据则不产生费用。
CynosDB for MySQL 与服务器类似，是按照使用时间计费，即使没有调用也会计费。请开发者注意该项资源的计费方式。

## 其他

### 程序配置信息

您可以通过以下配置参数：

- 环境 ID：选择需要部署的环境，在哪个环境下使用。
- 管理员用户名：Discuz! Q 后台管理系统的管理员用户名，默认为 admin。
- 管理员密码：Discuz! Q 后台管理系统的管理员密码，第一次安装时，会设置并加密存储在数据库内，之后变更请前往管理系统的用户管理面板重置密码，详情请参见 [用户管理](https://discuz.com/manual-admin/3.html#_3-1-%E7%94%A8%E6%88%B7%E7%AE%A1%E7%90%86)。
- 数据库用户名：默认为 root，当前不可修改。
- 数据库密码：root 账号的密码，初次安装时设置后将作为初始化的密码创建 CynosDB。后续修改密码请前往 CynosDB 控制台的账号管理页面，修改密码后，请同步修改此处的密码，以保证数据库的正常使用。

### 计费

此能力使用云开发与其他腾讯云服务，可能会产生相关费用。云开发与云上其他资源分开计费，您可以在 [费用中心](https://console.cloud.tencent.com/expense/overview) 查看具体信息。

#### 云托管
[产品定价](https://cloud.tencent.com/document/product/1243/47823) 及 [使用明细](https://console.cloud.tencent.com/tcb)。
![云托管与静态网站托管用量查询](https://main.qcloudimg.com/raw/3135c5ef7c19be7a86156f10dc0a8749.png)

#### 静态网站托管
[产品定价](https://cloud.tencent.com/document/product/1210/42854) 及 [使用明细](https://console.cloud.tencent.com/tcb)。


#### 文件存储（Cloud File Storage，CFS）
[产品定价](https://cloud.tencent.com/document/product/582/47378) 及 [使用明细](https://console.cloud.tencent.com/cfs/overview)。
 ![CFS用量](https://main.qcloudimg.com/raw/4022e36a8b69a450e5c36c78353c1b82.png)

#### 云数据库 CynosDB for MySQL
[产品定价](https://cloud.tencent.com/document/product/1003/30493) 及 [使用明细](https://console.cloud.tencent.com/cynosdb)。
 ![数据库存储用量](https://main.qcloudimg.com/raw/d486a7bb304ea1bff2738e213ce4c9e2.png)
