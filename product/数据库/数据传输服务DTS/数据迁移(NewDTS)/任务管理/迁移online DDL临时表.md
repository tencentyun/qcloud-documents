
## 操作场景
使用 gh-ost、  pt-online-schema-change 工具对源库中的表做 Online DDL，需要将 Online DDL 变更产生的临时表迁移到目标库。

- 使用 gh-ost 工具对表 `表名` 做 Online DDL，DTS 支持迁移临时表 `_表名_ghc`、`_表名_gho`、`_表名_del` 到目标库。 
- 使用 pt-online-schema-change  工具对表 `表名` 做 Online DDL，DTS 支持迁移临时表 `_表名_new`、  `_表名_old` 到目标库。

## 适用范围
 MySQL、MariaDB、Percona、TDSQL-C MySQL 之间的数据迁移。

## 操作步骤
1. 登录 [DTS 控制台](https://console.cloud.tencent.com/dts/migration)，在左侧导航选择**数据迁移**页，创建迁移任务。
2. 在“设置迁移选项及选择迁移对象”步骤中，在选择迁移对象右侧“已选对象”中，将鼠标悬浮在需要修改的对象上，即可显示编辑按钮。
![](https://qcloudimg.tencent-cloud.cn/raw/6eda98abf0900849b8b4c02551268d66.png)
3. 在弹出的对话框，选择**迁移临时表**，勾选需要迁移的表名后，单击**确定**。
 - 使用 gh-ost 工具做 Online DDL，勾选临时表名 `_表名_ghc`、`_表名_gho`、`_表名_del` 。 
 - 使用 pt-online-schema-change 工具做 Online DDL，勾选临时表名 `_表名_new`、`_表名_old`。
使用迁移临时表功能后，已选对象的表名前会显示![](https://qcloudimg.tencent-cloud.cn/raw/dfacb477b4cf9ba2d1046c5ccff9e463.png)，鼠标悬浮后可以显示已选择的临时表名。
>?
> - 如果源库中已存在与临时表名 `_表名_new` 、`_表名_old` 相同的表名，则 pt-osc 会产生其他临时表，由于 pt-osc 产生的其他临时表名并非固定，DTS 无法迁移其他临时表。这种情况**迁移对象**不能仅选择这个表，需要选择这个表所在的整个库（或者整个实例），否则无法迁移 Online DDL 变更产生的临时表数据到目标数据库。
> - 表映射（表重命名）功能与迁移临时表功能冲突，只能选择一个功能使用。
> 
![](https://qcloudimg.tencent-cloud.cn/raw/6d31f10be315c59d1af822f5c809cdd9.png)

