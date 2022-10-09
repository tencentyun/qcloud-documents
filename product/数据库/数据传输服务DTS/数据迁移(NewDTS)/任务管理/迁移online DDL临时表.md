
## 操作场景
使用 gh-ost、pt-online-schema-change（下文简称 pt-osc ）工具对源库中的表执行 Online DDL 操作，需要将 Online DDL 变更产生的临时表迁移到目标库。
DTS 支持在选择迁移对象时，提前关联对象表的临时表名，在后续源库产生临时表时一并进行迁移。  

- 使用 gh-ost 工具对表 `表名` 做 Online DDL，DTS 支持迁移临时表 `_表名_ghc`、`_表名_gho`、`_表名_del` 到目标库。 
- 使用 pt-osc 工具对表 `表名` 做 Online DDL，DTS 支持迁移临时表 `_表名_new`、  `_表名_old` 到目标库。

## 适用范围
 MySQL、MariaDB、Percona、TDSQL-C MySQL 之间的数据迁移。

## 约束限制

表映射（表重命名）功能与迁移 Online DDL 临时表功能冲突，只能选择一个功能使用。

## 操作步骤

1. 登录 [DTS 控制台](https://console.cloud.tencent.com/dts/migration)，在左侧导航选择**数据迁移**页，创建迁移任务。
2. 在“设置迁移选项及选择迁移对象”步骤中，勾选**是否同步 Online DDL 临时表**，和 **Online DDL 工具**。
 - 勾选 gh-ost，DTS 会将 gh-ost 工具产生的临时表名（`_表名_ghc`、`_表名_gho`、`_表名_del`）迁移到目标库。 
 - 勾选 pt-osc， DTS 会将 pt-osc 工具产生的临时表名（`_表名_new`、 `_表名_old`）迁移到目标库。
使用迁移临时表功能后，已选对象的表名前会显示![](https://qcloudimg.tencent-cloud.cn/raw/dfacb477b4cf9ba2d1046c5ccff9e463.png)，鼠标悬浮后可以显示已选择的临时表名。
>?如果源库中已存在与临时表名 `_表名_new` 、`_表名_old` 相同的表名，则 pt-osc 会产生其他临时表，由于 pt-osc 产生的其他临时表名并非固定，DTS 无法迁移其他临时表。这种情况**迁移对象**不能仅选择这个表，需要选择这个表所在的整个库（或者整个实例），否则无法迁移 Online DDL 变更产生的临时表数据到目标数据库。
>
![](https://qcloudimg.tencent-cloud.cn/raw/293c5f5bb7c84659d537487b1063ccc3.png)

