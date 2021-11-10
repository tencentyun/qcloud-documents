云托管服务可以通过其所在的 VPC（私有网络）访问您在腾讯云上的 TDSQL- C 数据库。

## 背景知识
- 了解什么是 TDSQL-C 及如何使用，请参见 [云原生数据库 TDSQL-C](https://cloud.tencent.com/document/product/1003)。
- 单击服务所在私有网络的名称，可以跳转到私有网络控制台查看该私有网络内您有哪些TDSQL-C 数据库资源，可以与此服务配合使用。

## 前置条件
您的云托管服务和 TDSQL-C 数据库集群处于同一 VPC 内。

## 操作步骤

### 步骤1：查询 TDSQL-C 数据库所在 VPC[](id:step1)

1. 登录 [云原生数据库 TDSQL-C 控制台](https://console.cloud.tencent.com/cynosdb)，找到您的 TDSQL-C 集群。
2. 在左侧菜单中，单击**集群列表**。单击集群名进入详情页，进入**集群详情**选项卡，在基本信息版块中，查找到**所属网络**信息：
![](https://main.qcloudimg.com/raw/0354d81a152424863c51b74b4a4e61f9.png)

### 步骤2：新建云托管服务

具体流程请参见 [新建服务](https://cloud.tencent.com/document/product/1243/46126)。
创建时，在“云托管网络”中选择**已有私有网络**，下拉选择 [步骤1](#step1) 中查询到 TDSQL-C 集群所在的 VPC 和子网。

### 步骤3：部署服务
具体流程请参见 [部署服务](https://cloud.tencent.com/document/product/1243/46127)。
服务部署完成后，该服务将可以访问您选定的 TDSQL- C 数据库，以及同 VPC 下其他 TDSQL-C 数据库。

## 说明

- 已有云托管服务不支持修改所在 VPC。若您已部署好了服务，误选了和 TDSQL- C 数据库不相同的 VPC，可选择：
   - 重新在正确 VPC 部署服务，删除部署错误的服务。
   - [打通多个 VPC](https://cloud.tencent.com/document/product/215/36698)。
- 云托管暂时仅支持上海、广州、北京地域。若您的 TDSQL-C 数据库不在上述地域则无法复用。更多地域将陆续开放，敬请期待。
- 如果 TDSQL-C 集群使用的是 Serverless 的计费模式，且连接 TDSQL-C 的云托管服务采用的是高可用模式（即便无流量也保持实例常驻），则与 TDSQL-C 的连接也将被一直保持，导致 TDSQL-C 持续产生计算费用。建议云托管服务采用低成本模式（无流量时缩容到0）配合 TDSQL-C 的 Serverless 计费模式使用。
