本文为您介绍从腾讯云数据库 MySQL 同步数据至腾讯云数据仓库 PostgreSQL（CDWPG）的过程。

CDWPG 是腾讯云大数据数据仓库产品，通过 DTS 实现云数据库 MySQL 到 CDWPG 的数据实时同步，可以帮助您完成 TP（在线事务）数据库到 AP（在线分析）数据库的数据闭环。

## 前提条件
- 已 [创建云数据库 MySQL](https://cloud.tencent.com/document/product/236/46433)，支持的 MySQL 版本：MySQL 5.6、MySQL 5.7。
- 需要您在源端 MySQL 实例中创建迁移帐号，需要的帐号权限如下：
```
GRANT RELOAD,LOCK TABLE,REPLICATION CLIENT,REPLICATION SLAVE,SELECT ON *.* TO "迁移帐号"@"%" IDENTIFIED BY "迁移密码";
GRANT ALL PRIVILEGES ON `__tencentdb__`.* TO "迁移帐号"@"%";
FLUSH PRIVILEGES;
```
- 已 [创建 CDWPG](https://cloud.tencent.com/document/product/878/31447)，支持的 CDWPG 版本：1.0.0。
- 需要您在目标端 CDWPG 实例中创建迁移帐号，需要的帐号权限如下：
```
Delete
Truncate
Insert
References
Select
Update
TRIGGER
```
- 配置云数据库 MySQL 到 CDWPG 数据同步任务，在任务启动前，需要进行前置检查，主要检查内容和检查点如下：

| 检查内容                            | 检查点                                             |
| ------------------------------ | ------------------------------------------- |
| 校验目标数据库 schema 和 table是否存在 | schema 和 table 必须提前创建好，如果没有创建好，则会报错 |
| 校验当前用户是否拥有目标数据表权限 | 针对要同步的表，首先判断当前用户是否是该表的 owner（owner 拥有所有权限），如果不是，则查看 information_schema.table_privilege 表中的授权信息，必须保证拥有：Delete、Truncate、Insert、References、Select、Update、TRIGGER 的授权权限，否则会报错 |
| 校验目标端磁盘空间是否充足 | 目标库的可用空间和源端需要的空间进行对比 |
| 校验源端数据库权限 | 对源实例检查是否有权限：Reload、LockTable、ReplClient、ReplSlave、Select、REPLICATION CLIENT |
| 校验源端 MySQL connect_timeout 参数 | 校验 MySQL 侧的 connect_timeout 参数是否小于10，如果小于则会报错 | 
| 校验源端和目标端数据库连接 | 校验 MySQL 和 CDWPG 是否能正确连接 |
| 校验源端数据库版本	| MySQL 版本须是 MySQL 5.6或 MySQL 5.7 |
| 校验源端优化参数 | innodb_stats_on_metadata 指标需要关闭 |
| 校验源端 binlog 参数 |	binlog_format 须为 ROW；binlog_row_image 须为 FULL；log_bin 须为 ON；gtid_mode 须为ON |
| 校验主键约束 |	源端需要同步的表必须有主键 |
| 校验源数据库编码	| 源端必须是 utf8 或 utf8mb4 |
| 校验 MySQL 表名大小写配置是否配置正确	| 校验 lower_case_table_names 参数是否为0，如果为0则配置不正确 |
| 校验 MySQL 数据库表名和列名是否含有`"`	| CDWPG 不支持`"`作为列名 |

## 注意事项
- DTS 在执行全量数据迁移时，会占用一定源端实例资源，可能会导致源实例负载上升，增加数据库自身压力。如果您数据库配置过低，建议您在业务低峰期进行。
- 云数据库 MySQL 需要同步的表必须具有主键。

## 支持同步的 SQL 操作
支持源端数据库同步表的 DML 操作，包括 INSERT、UPDATE、DELETE、REPLACE。

## 支持同步的架构
- 支持1对1单向同步。
- 支持1对多单向同步。
- 支持多对1单向同步。

## 操作步骤
1. 登录 [数据同步购买页](https://buy.cloud.tencent.com/dts)，选择相应配置，单击【立即购买】。
 - 计费模式：支持包年包月和按量计费，目前免费，后续计费会通过邮件和站内信方式提前1个月通知用户。
 - 源实例类型：目前仅支持 MySQL。
 - 源实例地域：选择后不支持再次修改，请选择源实例所在的地域。
 - 目标实例类型：目前仅 CDWPG。
 - 目标实例地域：选择后不支持再次修改，请选择目标实例所在的地域。
 - 同步任务规格：目前只支持标准版。
![](https://main.qcloudimg.com/raw/38e4ed88b4ec409ad213f991bc0f0274.png)
2. 在弹出的对话框，确认无误后，单击【立即购买】，返回数据同步列表，可看到刚创建的数据同步任务，刚创建的同步任务需要进行配置后才可以使用。
![](https://main.qcloudimg.com/raw/edcdb7fc6c76f9ce77f49757ba7c760d.png)
3. 在 [数据同步列表](https://console.cloud.tencent.com/dts/replication)，单击“操作”列的【配置】，进入配置同步任务页面。
4. 在配置同步任务页面，配置源端实例、帐号密码，配置目标端实例、帐号和密码，测试连通性后，单击【下一步】。
 - 任务名称：DTS 会自动生成一个任务名称，用户可以根据实际情况进行设置。
 - 运行模式：支持立即执行和定时执行。
 - 源实例类型：选择的云数据库实例类型，不可修改。
 - 源实例地域：选择的云数据库实例所在地域，不可修改。
 - 接入类型：目前支持云数据库。
 - 实例 ID：选择源实例 ID。
 - 源实例数据库帐号和密码：填入实际 [数据库帐号和密码](https://cloud.tencent.com/document/product/236/10305)，并单击【测试连通性】。
 - 目标实例类型：选择的目标实例类型，不可修改。
 - 目标实例地域：选择的目标实例所在地域，不可修改。
 - 接入类型：目前支持 CDWPG。
 - 实例 ID：选择目标实例 ID。
 - 数据库名称：同步到 CDWPG 所在的数据名称。
 - 目标实例数据库帐号和密码：填入实际 [数据库帐号和密码](https://console.cloud.tencent.com/cdwpg)，并单击【测试连通性】。
![](https://main.qcloudimg.com/raw/5fb32bc78048e1df3c309953b29f5781.png)
5. 在设置同步选项和同步对象页面，选择相应配置，单击【保存并下一步】。
 - 同步初始化：目前只支持全量数据初始化。
 - 已存在同名表：支持删除并重新初始化和忽略并继续执行两个策略。
    - 删除并重新初始化：如果目标端存在同名表会先删除同名表中数据并重新初始化。
    - 忽略并继续执行：全量数据初始化会全量追加数据，适用多张表汇聚到一张表中。
 - 同步操作类型：目前只支持 DML 操作。
 - 同步对象：在源库中选择待同步的表对象。
![](https://main.qcloudimg.com/raw/c1780105f32fdb299e213447881eba92.png)
6. 在校验任务页面，完成校验并全部校验项通过后，单击【启动任务】。
![](https://main.qcloudimg.com/raw/ad39b4d36b88f65afade0dec9a1afc48.png)
7. 返回数据同步任务列表，任务开始进入“运行中”状态。
 - 暂停任务，则同步数据暂停，单击【启动】后继续进行数据同步。
 - 停止任务，则直接关闭任务，请您确保数据同步完成后再关闭任务。
 - 在暂停状态下，可以对该任务进行重置，重置任务后该同步信息不再保留，请谨慎操作。
![](https://main.qcloudimg.com/raw/ef30c9b250284c6e6184fc479228184f.png)
8. （可选）您可以单击任务名，进入任务详情页，查看任务初始化状态和监控数据。
![](https://main.qcloudimg.com/raw/b7c0d14e5309f2756c56fcfee3834700.png)

