本文为您介绍物联网 SaaS 托管 MySQL 节点的新建集群流程。

## 前提条件
已完成 [开通 SaaS 托管](https://cloud.tencent.com/document/product/1081/50043)。

## 操作步骤
1. 登录 [物联网开发平台控制台](https://console.cloud.tencent.com/iotexplorer) ，选择**公共实例**或您购买的**标准企业实例**。
2. 单击**项目 ID** 进入项目详情页面，单击**物联使能** > **SaaS服务**进入 SaaS 列表页面，选择对应的 SaaS 进入 SaaS 详情页，单击 **MySQL 节点**进入 MySQL 节点页。
3. 单击**新建集群**，进入物联使能 MySQL 节点购买页。
4. 选择所要部署的地域、可用区以及数据库规格等配置，单击**立即购买**进入付费页。
 - **计费模式**：支持包年包月模式。
 - **网络**：出于性能安全考虑，目前仅支持私有网络（VPC），自研节点或云服务器需要与 MySQL 节点在同一 [VPC](https://cloud.tencent.com/document/product/215) 下方可通信。
 - **兼容数据库**：支持 MySQL 5.7、8.0。
 - **实例规格**：数据库规格和价格请参见 [计费概述](https://cloud.tencent.com/document/product/1081/50075)。
 - **存储计费**：支持包年包月，即预购存储空间，未使用部分仍然计费。
>?当集群存储数据量超过最大存储空间时，集群仅能读取数据不能写入，用户可以选择删除冗余数据或者升级规格。
>
5. 购买成功后，返回 MySQL 节点页的集群列表，待集群状态显示为**运行中**，即可正常使用。

## 后续操作
购买 MySQL 集群后，可通过集群内外网地址或数据管理平台连接 MySQL 集群，请参见 [连接 MySQL 集群](https://cloud.tencent.com/document/product/1003/37907)。
