当选择部署 Hive 组件时，Hive 元数据库提供了两种存储方式：第一种集群默认，Hive 元数据存储于集群独立购买 MetaDB；第二种是关联外部 Hive 元数据库，可选择关联 EMR-MetaDB 或自建 MySQL 数据库，元数据将存储于关联的数据库中，不随集群销毁而销毁。

集群默认是独立自动购买一个 MetaDB 云数据库实例存储单元作为元数据存储地，与其余组件元数据一起存储，并随集群销毁而销毁 MetaDB 云数据库，若需保存元数据，需提前在云数据库中手动保存元数据。
>!
>1. Hive 元数据与 Druid、Superset、Hue、Ranger、Oozie、Presto 组件元数据一起存储。  
>2. 集群需要单独购买一个 MetaDB 作为元数据存储单元。
>3. MetaDB 随集群销毁而销毁，即元数据随集群而销毁。

## 关联 EMR-MetaDB 共享 Hive 元数据
集群创建时系统会拉取云上可用的 MetaDB，用于新集群 Hive 组件存储元数据，无需单独购买 MetaDB 存储 Hive 元数据节约成本；并且 Hive 元数据不会随当前集群的销毁而销毁。
> !
>1. 可用 MetaDB 实例 ID 为同一账号下 EMR 集群中已有的 MetaDB。
>2. 当选择 Hue、Ranger、Oozie、Druid、Superset 一个或多个组件时系统会自动购买一个 MetaDB 用于除 Hive 外的组件元数据存储。
>3. 要销毁关联的 EMR-MetaDB 需前往云数据库销毁，销毁后 Hive 元数据库将无法恢复。
>4. 需保持关联的 EMR-MetaDB 网络与当前新建集群在同一网络环境下。
>
1. 新建集群并选择 Hive 组件后，单击**下一步**并选择关联的 EMR-MetaDB：
![](https://qcloudimg.tencent-cloud.cn/raw/15b3d819da3ce791f6985a954eaa1e59.png)
2. 未安装 Hive 组件的集群，在新增 Hive 组件时，选择关联的 EMR-MetaDB：
![](https://qcloudimg.tencent-cloud.cn/raw/dd2b64c1610783c3f94f31fa5f5d568d.png)

## 关联自建 MySQL 共享 Hive 元数据
关联自己本地自建 MySQL 数据库作为 Hive 元数据存储，也无需单独购买 MetaDB 存储 Hive 元数据节约成本，需准确填写输入以“jdbc:mysql://开头”的本地址、数据库名字、数据库登录密码，并确保网络与当前集群网络打通。
> !
>1. 请确保自建数据库与 EMR 集群在同一网络下。
>2. 准确填写数据库用户名和数据库密码。
>3. 当选择 Hue、Ranger、Oozie、Druid、Superset 一个或多个组件时系统会自动购买一个 MetaDB 用于除 Hive 外的元数据存储。
>4. 需保证自定义数据库中的 Hive 元数据版本大于等于新集群中的 Hive 版本。
>
1. 新建集群并选择 Hive 组件后，单击**下一步**并关联自建的 Mysql 数据库：
![](https://qcloudimg.tencent-cloud.cn/raw/5bcdf5307bc9947625f20fed37f6c7e9.png)
2. 未安装 Hive 组件的集群，在新增 Hive 组件时，关联自建的 Mysql 数据库：
![](https://qcloudimg.tencent-cloud.cn/raw/a56663f50ae4be468959b13cce74f809.png)

## HIVE 关联自建元数据异常修复方法
由于在创建 EMR 集群时选用了关联自建 MySQL，且自建 MySQL 无 HIVE 的元数据，这会导致 HIVE 进程异常。
### 问题复现
![](https://qcloudimg.tencent-cloud.cn/raw/57fcc9dd9eb72464c196243de3104421.png)
### 解决方案
对于无数据的 hive 元数据操作步骤如下：
>? 操作时替换成用户实际的 ${ip}、${port}、${database}。
>
1. 控制台将 HIVE 的 hs2 和 metastore 停掉。
2. hive 组件修改 hive-site.xml proto-hive-site.xml 下发。
配置项：javax.jdo.option.ConnectionURL
```
jdbc:mysql://${ip}:${port}/${database}?useSSL=false&amp;createDatabaseIfNotExist=true&amp;characterEncodin
g=UTF-8
```
3. CDB 数据库里删除库操作：
```
drop database ${database};
```
4. hadoop 用户执行如下命令：
```
/usr/local/service/hive/bin/schematool -dbType mysql -initSchema
```
5. 控制台 HIVE 启动 hs2和 metastore。
6. 访问 hive 是否异常。
如果有字符异常，CDB 再执行如下命令：
```
alter database ${database} character set latin1；
flush privileges；
```
