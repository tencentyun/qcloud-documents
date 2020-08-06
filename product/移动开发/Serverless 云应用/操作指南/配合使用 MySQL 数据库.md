本文分为两部分，分别介绍：

- 已有业务迁移至 Serverless 云应用时，如何继续使用现有的云数据库 MySQL 实例。
- 在 Serverless 云应用从零搭建新服务时，如何申请并使用新的云数据库 MySQL 实例。

## 基本概念

Serverless 云应用的开通以环境为维度，在开通时您需要指定当前环境绑定的 VPC 和子网。同一环境下可创建最多5个服务，这些服务都将部署在当前环境所绑定的 VPC 内。

当您的 MySQL 实例与 Serverless 云应用中的某个服务处于同一 VPC 内时，该服务即可连接使用这个 MySQL 实例。

>!暂不支持开通后，再次更改 Serverless 云应用所在环境绑定的 VPC 和子网。



## 已有业务迁移 • 复用云数据库 MySQL 实例

### 操作场景

1. 应用当前未部署在 Serverless 云应用上，希望迁移到 Serverless 云应用。
2. 业务的数据存储在云数据库 MySQL 实例中，希望应用迁移到 Serverless 云应用后，还能继续使用原有的腾讯云数据库 MySQL 实例，无需重新搭建数据库。

### 前提条件

1. 暂未开通 Serverless 云应用。
2. 已购买腾讯云数据库 MySQL 实例。
3. 应用与腾讯云数据库 MySQL 实例之间，采用内网连接方式。
> ?什么是内网连接方式，请参见 [连接 MySQL 实例](https://cloud.tencent.com/document/product/236/3130) 文档。

### 操作步骤

#### 步骤1：查询 MySQL 实例所在 VPC

1. 登录 [云数据库 MySQL 控制台](https://console.cloud.tencent.com/cdb)，找到您希望复用的 MySQL 实例。
2. 在左侧菜单中，单击【实例列表】，进入实例列表。单击实例名进入详情页，进入【实例详情】选项卡，在基本信息版块中，查找到**所属网络**信息。
![](https://main.qcloudimg.com/raw/587ff2bf466ce705cd1b559d36d48cf8.jpg)

#### 步骤2：进入 Serverless 云应用控制台


1. 开通 Serverless 云应用之前，您需要先登录 [云开发控制台](https://console.cloud.tencent.com/tcb) 并选择一个**按量计费**的环境。如果您还未开通**按量计费**类型的环境，或还未开通云开发，请先根据云开发文档 [开通环境](https://cloud.tencent.com/document/product/876/41391)。
![](https://main.qcloudimg.com/raw/2a3d2731646d326d773e2fd534c31002.png)
2. 在左侧菜单中，单击【Serverless 云应用】，进入 Serverless 云应用。
![](https://main.qcloudimg.com/raw/2b47f79763be8b5ae32e2bf3900d1106.jpg)
>?Serverless 云应用公测期间，需要先 [申请开通](https://cloud.tencent.com/apply/p/y5uji0g6a7p)，审核通过后，云开发控制台的左侧菜单将展示 【Serverless 云应用】入口，否则入口将不可见。公测结束后，**Serverless 云应用**的入口将对所有云开发用户开放。



#### 步骤4：开通 Serverless 云应用

1. 单击【立即开通】。
![](https://main.qcloudimg.com/raw/c28dbbabd53906f84db237156b8ac850.png)
2. 在**Serverless 云应用网络**中选择【自定义配置】。
3. 下拉选择步骤1中查询到 MySQL 实例所在的 VPC 和子网。
![](https://main.qcloudimg.com/raw/5443e7ad6e871c112f69dacd53c52f75.png)



#### 步骤5：开通成功

单击【提交】，状态将变为**开通中**，请等待数秒。
![](https://main.qcloudimg.com/raw/fa0de696760aab0ef690e079d68973d7.png)

开通成功后，您将自动跳转到 Serverless 云应用的服务列表页面。当前您还没有创建任何服务，列表为空。
至此您已经成功开通后 **Serverlesss 云应用**服务，您可以单击【新建服务】开始新建您的第一个服务。

您在该环境下创建的所有服务，都可以访问您选定的 MySQL 实例，以及同 VPC 下其他 MySQL 实例。
![](https://main.qcloudimg.com/raw/993711f6a2f0a8e704da6a581efc43ad.png)

### 特殊情况

- 若您需要复用多个不在同一 VPC 下的 MySQL 实例，可在多个云开发环境开通 Serverless 云应用分别对应不同 VPC，或打通多个 VPC。如何打通多个 VPC，请参见 [连接其它 VPC](https://cloud.tencent.com/document/product/215/36698) 文档。
- 若您已开通 Serverless 云应用，误选了和 MySQL 实例不相同的 VPC，可选择打通多个 VPC，或 [提交工单](https://console.cloud.tencent.com/workorder/category) 申请销毁当前环境的 Serverless 云应用后，重新开通并选择正确的网络配置。
- 公测期间 Serverless 云应用仅支持上海地域。若您的 MySQL 实例不在上海地域则无法复用。



## 搭建新服务 • 新建MySQL实例

### 操作场景

使用 Serverless 云应用从零搭建服务，并配套使用云数据库 MySQL。

### 操作步骤

#### 步骤1：进入 Serverless 云应用控制台

1. 开通 Serverless 云应用之前，您需要先登录 [云开发控制台](https://console.cloud.tencent.com/tcb) 并选择一个**按量计费**的环境。如果您还未开通**按量计费**类型的环境，或还未开通云开发，请先根据云开发文档 [开通环境](https://cloud.tencent.com/document/product/876/41391)。
![](https://main.qcloudimg.com/raw/2a3d2731646d326d773e2fd534c31002.png)
2. 在左侧菜单中，单击【Serverless 云应用】，进入 Serverless 云应用。
![](https://main.qcloudimg.com/raw/2b47f79763be8b5ae32e2bf3900d1106.jpg)
>?Serverless 云应用公测期间，需要先 [申请开通](https://cloud.tencent.com/apply/p/y5uji0g6a7p)，审核通过后，云开发控制台的左侧菜单将展示 【Serverless 云应用】入口，否则入口将不可见。公测结束后，**Serverless 云应用**的入口将对所有云开发用户开放。



#### 步骤2：开通 Serverless 云应用

1. 单击【立即开通】。
![](https://main.qcloudimg.com/raw/c28dbbabd53906f84db237156b8ac850.png)
2. 在**Serverless 云应用网络**中选择【系统默认配置】。
![](https://main.qcloudimg.com/raw/f5399f62887a62973ef88a4384c48437.png)


#### 步骤3：开通成功

单击【提交】，状态变为**开通中**，请等待数秒。
![](https://main.qcloudimg.com/raw/fa0de696760aab0ef690e079d68973d7.png)

开通成功后，您将自动跳转到 Serverless 云应用的服务列表页面。当前您还没有创建任何服务，列表为空。
至此您已经成功开通后 **Serverlesss 云应用**服务，您可以单击【新建服务】开始新建您的第一个服务了。
![](https://main.qcloudimg.com/raw/993711f6a2f0a8e704da6a581efc43ad.png)

#### 步骤4：查询服务所在网络

1. 选择您需要配合使用 MySQL 的服务，单击服务名称进入服务详情页面。
![](https://main.qcloudimg.com/raw/0549eee11a609f62ef5a95f77e6d969b.png)
2. 单击【服务配置】选项卡，查看服务所在私有网络信息。
![](https://main.qcloudimg.com/raw/e6c356fdf7cb744d182f80cd7ebed10e.png)

#### 步骤5：购买云数据库 MySQL 实例

具体步骤请参见云数据库 MySQL [购买指南](https://cloud.tencent.com/document/product/236/5160) 文档。购买时网络配置，请选择上一步中查询到的服务所在网络信息。

#### 步骤6：开始使用数据库

购买并配置完 MySQL 实例后，您的服务就可以使用此数据库实例，以及后续同一个 VPC 下所有的 MySQL 实例了。



## 相关操作

- [新建服务](https://cloud.tencent.com/document/product/1243/46126)
- [部署服务](https://cloud.tencent.com/document/product/1243/46127)

