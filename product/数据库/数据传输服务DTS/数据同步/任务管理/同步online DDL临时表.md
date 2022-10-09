
## 操作场景
使用 gh-ost、 pt-online-schema-change（下文简称 pt-osc ）等工具对源库中的表做 Online DDL，需要将 Online DDL 变更产生的临时表同步到目标库。
DTS 支持在选择同步对象时，提前关联对象表的临时表名，在后续源库产生临时表时一并进行同步。  
- 使用 gh-ost 工具对表 `表名` 做 Online DDL，DTS 支持同步临时表 `_表名_ghc`、`_表名_gho`、`_表名_del` 到目标库。 
- 使用 pt-osc 工具对表 `表名` 做 Online DDL，DTS 支持同步临时表 `_表名_new`、  `_表名_old` 到目标库。

## 适用范围
 MySQL、MariaDB、Percona、TDSQL-C MySQL 之间的数据同步。

## 约束限制

表映射（表重命名）功能与迁移 Online DDL 临时表功能冲突，只能选择一个功能使用。

## 操作步骤

1. 登录 [DTS 控制台](https://console.cloud.tencent.com/dts/replication)，在左侧导航选择**数据同步**页，创建同步任务。
2. 在“设置同步选项和同步对象”步骤中，勾选**是否同步 Online DDL 临时表**，和 **Online DDL 工具**。
 - 勾选 gh-ost，DTS 会将 gh-ost 工具产生的临时表名（`_表名_ghc`、`_表名_gho`、`_表名_del`）迁移到目标库。 
 - 勾选 pt-osc， DTS 会将 pt-osc 工具产生的临时表名（`_表名_new`、 `_表名_old`）迁移到目标库。
使用同步临时表功能后，已选对象的表名前会显示![](https://qcloudimg.tencent-cloud.cn/raw/dfacb477b4cf9ba2d1046c5ccff9e463.png)，鼠标悬浮后可以显示已选择的临时表名。
>?如果源库中已存在与临时表名 `_表名_new` 、`_表名_old` 相同的表名，则 pt-osc 会产生其他临时表，由于 pt-osc 产生的其他临时表名并非固定，DTS 无法同步其他临时表。这种情况**同步对象**不能仅选择这个表，需要选择这个表所在的整个库（或者整个实例），否则无法同步 Online DDL 变更产生的临时表数据到目标数据库。
>
![](https://qcloudimg.tencent-cloud.cn/raw/07f7410678b23d500c3fd4c934b896d8.png)
