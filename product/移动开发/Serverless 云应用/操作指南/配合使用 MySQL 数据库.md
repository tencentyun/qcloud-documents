本文分为两部分，分别介绍：

- 已有业务迁移至云托管时，如何继续使用现有的云数据库 MySQL 实例。
- 使用云托管从零搭建新服务时，如何申请并使用新的云数据库 MySQL 实例。

## 基本概念

云托管的开通以环境为维度，在开通时您需要指定当前环境绑定的 VPC 和子网。同一环境下可创建最多5个服务，这些服务都将部署在当前环境所绑定的 VPC 内。

当您的 MySQL 实例与云托管中的某个服务处于同一 VPC 内时，该服务即可连接使用这个 MySQL 实例。

>!暂不支持开通后，再次更改云托管所在环境绑定的 VPC 和子网。



## 已有业务迁移-复用云数据库 MySQL 实例

### 操作场景

1. 应用当前未部署在云托管上，希望迁移到云托管。
2. 业务的数据存储在云数据库 MySQL 实例中，希望应用迁移到云托管后，还能继续使用原有的腾讯云数据库 MySQL 实例，无需重新搭建数据库。

### 前提条件

1. 暂未开通云托管。
2. 已购买腾讯云数据库 MySQL 实例。
3. 应用与腾讯云数据库 MySQL 实例之间，采用内网连接方式。
> ?什么是内网连接方式，请参见 [连接 MySQL 实例](https://cloud.tencent.com/document/product/236/3130) 文档。

### 操作步骤

#### 步骤1：查询 MySQL 实例所在 VPC

1. 登录 [云数据库 MySQL 控制台](https://console.cloud.tencent.com/cdb)，找到您希望复用的 MySQL 实例。
2. 在左侧菜单中，单击【实例列表】，进入实例列表。单击实例名进入详情页，进入【实例详情】选项卡，在基本信息版块中，查找到**所属网络**信息。
![](https://main.qcloudimg.com/raw/587ff2bf466ce705cd1b559d36d48cf8.jpg)

#### 步骤2：进入云托管控制台


1. 开通云托管之前，您需要先登录 [云开发控制台](https://console.cloud.tencent.com/tcb) 并选择一个**按量计费**的环境。如果您还未开通**按量计费**类型的环境，或还未开通云开发，请先根据云开发文档 [开通环境](https://cloud.tencent.com/document/product/876/41391)。
![](https://main.qcloudimg.com/raw/2a3d2731646d326d773e2fd534c31002.png)
2. 在左侧菜单中，单击【云托管】，进入云托管控制台。
![](https://main.qcloudimg.com/raw/38110b543ebe9c38b0e25370b1dfaf3a.png)


#### 步骤3：开通云托管

1. 单击【立即开通】。
![](https://main.qcloudimg.com/raw/b7a1394679586c41045b93067e647d7e.png)
2. 在**云托管网络**中选择【自定义配置】。
3. 下拉选择步骤1中查询到 MySQL 实例所在的 VPC 和子网。
![](https://main.qcloudimg.com/raw/0a0d75d92a19a9abbd66ec318d3af591.png)



#### 步骤4：开通成功

单击【提交】，状态将变为**开通中**，请等待数秒。
![](https://main.qcloudimg.com/raw/031cf80d0314c6c5207beabb5f576978.png)

开通成功后，您将自动跳转到云托管的服务列表页面。当前您还没有创建任何服务，列表为空。
至此您已经成功开通后**云托管**服务，您可以单击【新建服务】开始新建您的第一个服务。

您在该环境下创建的所有服务，都可以访问您选定的 MySQL 实例，以及同 VPC 下其他 MySQL 实例。
![](https://main.qcloudimg.com/raw/6b5051cc990cafee831e002416b5e67e.png)

### 特殊情况

- 若您需要复用多个不在同一 VPC 下的 MySQL 实例，可在多个云开发环境开通云托管分别对应不同 VPC，或打通多个 VPC。如何打通多个 VPC，请参见 [连接其它 VPC](https://cloud.tencent.com/document/product/215/36698) 文档。
- 若您已开通云托管，误选了和 MySQL 实例不相同的 VPC，可选择打通多个 VPC，或 [提交工单](https://console.cloud.tencent.com/workorder/category) 申请销毁当前环境的云托管后，重新开通并选择正确的网络配置。
- 云托管暂时仅支持上海地域。若您的 MySQL 实例不在上海地域则无法复用。更多地域将陆续开放，敬请期待。



## 搭建新服务-新建MySQL实例

### 操作场景

使用云托管从零搭建服务，并配套使用云数据库 MySQL。

### 操作步骤

#### 步骤1：进入云托管控制台

1. 开通云托管之前，您需要先登录 [云开发控制台](https://console.cloud.tencent.com/tcb) 并选择一个**按量计费**的环境。如果您还未开通**按量计费**类型的环境，或还未开通云开发，请先根据云开发文档 [开通环境](https://cloud.tencent.com/document/product/876/41391)。
![](https://main.qcloudimg.com/raw/2a3d2731646d326d773e2fd534c31002.png)
2. 在左侧菜单中，单击【云托管】，进入云托管控制台。
![](https://main.qcloudimg.com/raw/38110b543ebe9c38b0e25370b1dfaf3a.png)



#### 步骤2：进入云托管控制台


1. 开通云托管之前，您需要先登录 [云开发控制台](https://console.cloud.tencent.com/tcb) 并选择一个**按量计费**的环境。如果您还未开通**按量计费**类型的环境，或还未开通云开发，请先根据云开发文档 [开通环境](https://cloud.tencent.com/document/product/876/41391)。
![](https://main.qcloudimg.com/raw/2a3d2731646d326d773e2fd534c31002.png)
2. 在左侧菜单中，单击【云托管】，进入云托管控制台。
![](https://main.qcloudimg.com/raw/38110b543ebe9c38b0e25370b1dfaf3a.png)


#### 步骤3：开通成功

单击【提交】，状态将变为**开通中**，请等待数秒。
![](https://main.qcloudimg.com/raw/031cf80d0314c6c5207beabb5f576978.png)

开通成功后，您将自动跳转到云托管的服务列表页面。当前您还没有创建任何服务，列表为空。
至此您已经成功开通后**云托管**服务，您可以单击【新建服务】开始新建您的第一个服务了。
![](https://main.qcloudimg.com/raw/f78b6f7f84562c0ea0455bcacb5c8ec8.png)

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

