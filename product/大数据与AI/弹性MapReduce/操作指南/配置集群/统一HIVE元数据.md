## 功能介绍
当新建 EMR 集群部署可选组件 Hive 时，系统提供了两种 Hive 元数据存储方式，从而达到 Hive 元数据统一管理；第一种集群默认，Hive 元数据存储于集群独立购买的 MetaDB；第二种是关联外部 Hive 元数据库，可选择关联 EMR-MetaDB 或自建 MySQL 数据库，元数据将存储于关联的数据库中，不随集群销毁而销毁。
## 前提条件
- 集群默认：是独立自动购买一个 MetaDB 云数据库实例存储单元作为元数据存储地，与其余组件元数据一起存储，并随集群销毁而销毁 MetaDB 云数据库，若需保存元数据，需提前前往云数据库中手动保存元数据。
 - Hive 元数据与 Hue、Ranger、Oozie、Presto、Druid、Superset 组件元数据一起存储。
 - 集群需要单独购买一个 MetaDB 作为元数据存储单元。
 - MetaDB 随集群销毁而销毁，即元数据随集群而销毁。
- 关联 EMR-MetaDB：集群创建时系统会拉取云上可用的 MetaDB，用于新集群 Hive 组件存储元数据，无需单独购买 MetaDB 存储 Hive 元数据节约成本；并且 Hive 元数据不会随当前集群的销毁而销毁。
 - 可用 MetaDB 实例 ID 为同一账号下 EMR 集群中已有的 MetaDB。
 - 当选择 Hue、Ranger、Oozie、Druid、Superset 一个或多个组件时系统会自动购买一个 MetaDB 用于除 Hive 外的组件元数据存储。
 - 要销毁关联的 EMR-MetaDB 需前往云数据库销毁，销毁后 Hive 元数据库将无法恢复。
 - 需保持关联的 EMR-MetaDB 网络与当前新建集群在同一网络环境下。
- 关联自建 MySQL 数据库：关联自己本地自建 MySQL 数据库作为 Hive 元数据存储，也无需单独购买 MetaDB 存储 Hive 元数据节约成本，需准确填写输入以“jdbc:mysql://开头”的本地址、数据库名字、数据库登录密码，并确保网络与当前集群网络打通。
 - 请确保自建数据库与 EMR 集群在同一网络下。
 - 准确填写数据库用户名和数据库密码。
 - 当选择 Hue、Ranger、Oozie、Druid、Superset 一个或多个组件时系统会自动购买一个 MetaDB 用于除 Hive 外的元数据存储。
 - 需保证自定义数据库中的 Hive 元数据版本大于等于新集群中的 Hive 版本。

## 操作步骤
### 新建集群
1. 登录 [腾讯云账号](https://console.cloud.tencent.com/emr)，单击产品介绍页【[立即选购](https://buy.cloud.tencent.com/emapreduce#/)】在“可用区与软件配置”页的【可选组件】中，选择 Hive 组件。
![](https://qcloudimg.tencent-cloud.cn/raw/90c7f8e5a26a6bc9330f0354cbd8c3a2.png)2. 在 hive 元数据库存储方式上可根据情况选择，集群默认 EMR-MetaDB 或自建 MySQL 数据库。
3. 根据选择情况与上述限制条件一致配置即可。

### 后安装 HIVE 组件
1. 集群创建成功后，登录 [EMR 控制台](https://console.cloud.tencent.com/emr)，进入【集群列表】页面单击需要管理的集群【ID/名称】。
2. 选择【集群服务】中的【新增组件】并安装 hive 组件。
![](https://main.qcloudimg.com/raw/040a8ab7a58a7743a1a0698997151a56.png)
3. 在 hive 元数据库存储方式上可根据情况选择，集群默认 EMR-MetaDB 或自建 MySQL 数据库。
4. 根据选择情况与上述限制条件一致配置即可。
