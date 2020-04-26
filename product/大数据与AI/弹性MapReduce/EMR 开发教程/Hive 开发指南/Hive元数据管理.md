当选择部署 Hive 组件时，Hive 元数据库提供了两种存储方式；第一种集群默认， Hive 元数据存储于集群独立购买 MetaDB；第二种是关联外部 Hive 元数据库 ，可选择关联 EMR-MetaDB 或自建 MySQL 数据库，元数据将存储于关联的数据库中，不随集群销毁而销毁。
集群默认是独立自动购买一个 MetaDB 云数据库实例存储单元作为元数据存储地，与其余组件元数据一起存储，并随集群销毁而销毁 MetaDB 云数据库，若需保存元数据，需提前前往云数据库中手动保存元数据。

>!
>1. Hive 元数据与 Sqoop、Hue、Ranger、Oozie、Presto 组件元数据一起存储。
>2. 集群需要单独购买一个 MetaDB 作为元数据存储单元。
>3. MetaDB 随集群销毁而销毁，即元数据随集群而销毁。

## 关联 EMR-MetaDB 共享 Hive 元数据
集群创建时系统会拉取云上可用的 MetaDB，用于新集群 Hive 组件存储元数据，无需单独购买 MetaDB 存储 Hive 元数据节约成本；并且 Hive 元数据不会随当前集群的销毁而销毁。
> !
>1. 可用 MetaDB 实例 ID 为同一账号下 EMR 集群中已有的 MetaDB。
>2. 当选择 Sqoop、Hue、Ranger、Oozie、Presto 一个或多个组件时系统会自动购买一个 MetaDB 用于除 Hive 外的组件元数据存储。
>3. 要销毁关联的 EMR-MetaDB 需前往云数据库销毁，销毁后 Hive 元数据库将无法恢复。
>4. 需保持关联的 EMR-MetaDB 网络与当前新建集群在同一网络环境下。
>
![](https://main.qcloudimg.com/raw/5c58a791c3a4fe0d6f854b44c92c2b13.png)
![](https://main.qcloudimg.com/raw/56837d31dfe5ebf11ef2cf7737bd1bcf.png)

## 关联自建 MySQL 共享 Hive 元数据
关联自己本地自建 MySQL 数据库作为 Hive 元数据存储，也无需单独购买 MetaDB存储 Hive 元数据节约成本，需准确填写输入以 “jdbc:mysql://开头” 的本地址、数据库名字、数据库登录密码，并确保网络与当前集群网络打通。
> !
>1. 请确保自建数据库与 EMR 集群在同一网络下。
>2. 准确填写数据库用户名和数据库密码。
>3. 当选择 Sqoop、Hue、Ranger、Oozie、Presto 一个或多个组件时系统会自动购买一个 MetaDB 用于除 Hive 外的元数据存储。
>4. 需保证自定义数据库中的 Hive 元数据版本大于等于新集群中的 Hive 版本。
>
![](https://main.qcloudimg.com/raw/1cd32465eb0c50eef2811d047d98245f.png)
![](https://main.qcloudimg.com/raw/9482f426e38b9471cc17f89d301cfbfb.png)


