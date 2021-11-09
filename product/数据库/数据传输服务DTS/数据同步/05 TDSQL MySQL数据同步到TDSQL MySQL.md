本文为您介绍使用数据传输服务 DTS 从 TDSQL MySQL 数据库同步数据至 TDSQL MySQL 数据库的过程。

如下场景的同步要求与 TDSQL MySQL 到 TDSQL MySQL 的同步要求一致，可参考本场景相关内容。
- TDSQL MySQL 到腾讯云数据库 MariaDB 的数据同步
- TDSQL MySQL 到腾讯云数据库 MariaDB（Percona）的数据同步
- TDSQL MySQL 到腾讯云数据库 MySQL 的数据同步 
- MariaDB 到 TDSQL MySQL（MariaDB）的数据同步
- MariaDB（Percona）到 TDSQL MySQL（Percona）的数据同步
- MySQL 到 TDSQL MySQL 的数据同步
>?如需体验本章节中 TDSQL MySQL 的同步功能，请先 [提交工单](https://console.cloud.tencent.com/workorder/category) 进行申请。
>

## 注意事项
- DTS 在执行全量数据同步时，会占用一定源端实例资源，可能会导致源实例负载上升，增加数据库自身压力。如果您数据库配置过低，建议您在业务低峰期进行。
- 为了避免数据重复，请确保需要同步的表具有主键或者非空唯一键。

## [前提条件](id:qttj)
- 源数据库和目标数据库符合同步功能和版本要求，请参考 [数据同步支持的数据库](https://cloud.tencent.com/document/product/571/58672) 进行核对。
- 需要具备源数据库的权限如下：
```sql
GRANT RELOAD,LOCK TABLES,REPLICATION CLIENT,REPLICATION SLAVE,SELECT ON *.* TO '迁移帐号'@'%' IDENTIFIED BY '迁移密码';
GRANT ALL PRIVILEGES ON `__tencentdb__`.* TO '迁移帐号'@'%'; //如果源端为腾讯云数据库需要授予`__tencentdb__`权限
FLUSH PRIVILEGES;
```
- 需要具备目标数据库的权限：ALTER, ALTER ROUTINE, CREATE, CREATE ROUTINE, CREATE TEMPORARY TABLES, CREATE USER, CREATE VIEW, DELETE, DROP, EVENT, EXECUTE, INDEX, INSERT, LOCK TABLES, PROCESS, REFERENCES, RELOAD, SELECT, SHOW DATABASES, SHOW VIEW, TRIGGER, UPDATE。

## 应用限制
- 只支持同步基础表，不支持同步视图、函数、触发器、存储过程等对象。 
- 源端如果是非 GTID 实例，DTS 不支持源端 HA 切换，一旦源端 MySQL 发生切换可能会导致 DTS 增量同步中断。
- 只支持同步 InnoDB 数据库引擎，如果存在其他数据引擎表则任务校验时会报错。
- 相互关联的数据对象需要同时同步，否则会导致同步失败。
- 增量同步过程中，若源库存在分布式事务或者产生了类型为 `STATEMENT` 格式的 Binlog 语句，则会导致同步失败。
- 不支持同步 [二级分区](https://cloud.tencent.com/document/product/557/58907) 表，如果同步的库表中包含二级分区表，则任务会报错暂停。
- TDSQL MySQL（MariaDB）作为源或者目标库时，不支持双向同步。
- TDSQL 同步功能为了提高增量阶段的同步速度，采用了行级并发策略。因此在增量同步过程中，可能会在极短的时间内在目标库观察到事务的中间值，但最终源库和目标库数据会保持一致。 
- 目前主键冲突处理策略只支持冲突覆盖，对于增量阶段的主键数据冲突，会直接进行冲突覆盖。但对于全量数据初始化阶段的冲突，任务会报错。

## 操作限制
同步过程中请勿进行如下操作，否则会导致同步任务失败。
- 请勿修改、删除源数据库和目标数据库中用户信息（包括用户名、密码和权限）和端口号。
- 请勿在源库上执行分布式事务。
- 请勿在源库写入 Binlog 格式为 `STATEMENT` 的数据。
- 请勿在源库上执行清除 Binlog 的操作。
- 在同步增量阶段，请勿删除系统库表 `__tencentdb__`。 

## 支持同步的 SQL 操作
| 操作类型 | SQL 操作语句                                                 |
| -------- | ------------------------------------------------------------ |
| DML      | INSERT、UPDATE、DELETE                                       |
| DDL      | CREATE DATABASE、DROP DATABASE、ALTER DATABASE、CREATE TABLE、ALTER TABLE、DROP TABLE、TRUNCATE TABLE、RENAEM TABLE、CREATE INDEX、DROP INDEX |

## 环境要求
<table>
<tr><th width="20%">类型</th><th width="80%">环境要求</th></tr>
<tr>
<td>源数据库要求</td>
<td>
<li>源库和目标库网络能够连通。</li>
<ul>
<li>实例参数要求：
<ul>
<li>源库 server_id 参数需要手动设置，且值不能设置为0。</li>
<li>源库表的 row_format 不能设置为 FIXED。</li>
<li>源库和目标库 lower_case_table_names 变量必须设置一致。</li>
<li>源库变量 connect_timeout 设置数值必须大于10。</li></ul></li>
<li>Binlog 参数要求：
<ul>
<li>源端 log_bin 变量必须设置为 ON。</li>
<li>源端 binlog_format 变量必须设置为 ROW。</li>
<li>源端 binlog_row_image 变量必须设置为 FULL。</li>
<li>MySQL 5.6 及以上版本 gtid_mode 变量不为 ON 时会报警告，建议打开 gtid_mode。</li>
<li>不允许设置 do_db, ignore_db。</li>
<li>源实例为从库时，log_slave_updates 变量必须设置为 ON。</li></ul></li>
<li>外键依赖：
<ul>
<li>外键依赖只能设置为 NO ACTION，RESTRICT 两种类型。</li>
<li>部分库表同步时，有外键依赖的表必须齐全。</li>
</ul>
</li>
</td></tr>
<tr> 
<td>目标数据库要求</td>
<td>
<li>目标库为分布式数据库时，推荐提前手动创建分表，并规划 shardkey，否则 DTS 会按照源库的表样式来在目标库创建表，如果源库为单机实例，则目标库会创建为单表。</li>
<li>目标库的版本必须大于等于源库的版本。</li>
<li>目标库需要有足够的存储空间，如果初始类型选择“全量数据初始化”，则目标库的空间大小须是源库待同步库表空间的1.2倍以上。</li>
<li>目标库 max_allowed_packet 参数设置数值至少为4M。</li></td></tr>
<tr> 
<td>其他要求</td>
<td>环境变量 innodb_stats_on_metadata 必须设置为 OFF。</td></tr>
</table>

## 操作步骤
1. 登录 [数据同步购买页](https://buy.cloud.tencent.com/dts)，选择相应配置，单击**立即购买**。
<table>
<thead><tr><th>参数</th><th>描述</th></tr></thead>
<tbody><tr>
<td>计费模式</td><td>支持包年包月和按量计费。目前免费，将来开始计费前1个月会通过邮件和站内信方式提前通知用户。</td></tr>
<tr>
<td>源实例类型</td><td>选择 TDSQL MySQL。</td></tr>
<tr>
<td>源实例地域</td><td>选择源实例所在地域。</td></tr>
<tr>
<td>目的实例类型</td><td>选择 TDSQL MySQL。</td></tr>
<tr>
<td>目的实例地域</td><td>选择目的实例所在地域。</td></tr>
<tr>
<td>同步任务规格</td><td>目前只支持标准版。</td></tr>
</tbody></table>
2. 购买完成后，返回 [数据同步列表](https://console.cloud.tencent.com/dts/replication)，可看到刚创建的数据同步任务，刚创建的同步任务需要进行配置后才可以使用。
3. 在数据同步列表，单击**操作**列的**配置**，进入配置同步任务页面。
![](https://qcloudimg.tencent-cloud.cn/raw/593ce1e644f0717809760c4ba84bb840.png)
4. 在配置同步任务页面，配置源端实例、帐号密码，配置目标端实例、帐号和密码，测试连通性后，单击**下一步**。
![](https://qcloudimg.tencent-cloud.cn/raw/4e09c5e94a31ae02012db00bcfadbd87.png)
<table>
<thead><tr><th width="10%">设置项</th><th width="15%">参数</th><th width="75%">描述</th></tr></thead>
<tbody><tr>
<td rowspan=2 >任务设置</td>
<td>任务名称</td>
<td>DTS 会自动生成一个任务名称，用户可以根据实际情况进行设置。</td></tr>
<tr>
<td>运行模式</td><td>支持立即执行和定时执行两种模式。</td></tr>
<tr>
<td rowspan=6 >源实例设置</td>
<td>源实例类型</td>
<td>购买时所选择的云数据库实例类型，不可修改。</td></tr>
<tr>
<td>源实例地域</td>
<td>购买时选择的云数据库实例所在地域，不可修改。</td></tr>
<tr>
<td>接入类型</td>
<td>选择“云数据库”，表示源实例属于腾讯云数据库实例。</td></tr>
<tr>
<td>实例 ID</td>
<td>源实例 ID。</td></tr>
<tr>
<td>帐号</td>
<td>源实例帐号。</td></tr>
<tr>
<td>密码</td>
<td>源实例密码。</td></tr>
<tr>
<td rowspan=6 >目标实例设置</td>
<td>目标实例类型</td><td>所选择的目标实例类型，不可修改。</td></tr>
<tr>
<td>目标实例地域</td><td>选择的目标实例所在地域，不可修改。</td></tr>
<tr>
<td>接入类型</td><td>选择目标数据库类型。</td></tr>
<tr>
<td>实例 ID</td><td>目标实例 ID。</td></tr>
<tr>
<td>帐号</td><td>目标实例帐号。</td></tr>
<tr>
<td>密码</td><td>目标实例密码。</td></tr>
</tbody></table>
5. 在设置同步选项和同步对象页面，将对数据初始化选项、数据同步选项、同步对象选项进行设置，在设置完成后单击**保存并下一步**。
>?
>- 如果用户在同步过程中确定会使用 gh-ost、pt-osc 等工具对某张表做 Online DDL，则**同步对象**需要选择这个表所在的整个库（或者整个实例），不能仅选择这个表，否则无法同步 Online DDL 变更产生的临时表数据到目标数据库。
>- 如果用户在同步过程中确定会对某张表使用 rename 操作（例如将 table A rename 为 table B），则**同步对象**需要选择 table A 所在的整个库（或者整个实例），不能仅选择 table A，否则系统会报错。
>
![](https://qcloudimg.tencent-cloud.cn/raw/367d16f2af9fd6b08e9b81632a2951b8.png)
<strong>库表映射</strong>：在已选对象中，鼠标放在右侧将出现编辑按钮，单击后可在弹窗中填写映射名。
<img src="https://qcloudimg.tencent-cloud.cn/raw/7d8260ec27667ef8fadcf32ae9e41e3e.png" style="zoom:70%;" />
<table>
<thead><tr><th>设置项</th><th>参数</th><th>描述</th></tr></thead>
<tbody>
<tr>
<td rowspan=2>数据初始化选项</td>
<td>初始化类型</td>
<td><ul><li>结构初始化：同步任务执行时会先将源实例中表结构初始化到目标实例中。</li><li>全量数据初始化：同步任务执行时会先将源实例中数据初始化到目标实例中。</li></ul>默认两者都勾上，可根据实际情况取消。仅选择“全量数据初始化”时，用户需要提前在目标库创建好表结构。
</ul></td></tr>
<tr>
<td>已存在同名表</td>
<td><ul><li>前置校验并报错：存在同名表则报错，流程不再继续。<li>忽略并继续执行：全量数据和增量数据直接追加目标实例的表中。</td></tr>
<tr>
<td rowspan=2>数据同步选项</td>
<td>冲突处理机制</td>
<td>冲突覆盖：在同步时发现表主键冲突，用源库主键记录覆盖目标库主键记录。</td></tr>
<tr>
<td>同步操作类型</td><td>支持操作：Insert、Update、Delete、DDL。</td></tr>
<tr>
<td rowspan=2>同步对象选项</td>
<td>源实例库表对象</td><td>选择待同步的对象，支持库级别和表级别。</td></tr>
<tr>
<td>已选对象</td><td>展示已选择的同步对象，支持库表映射。</td></tr>
</tbody></table>
6. 在校验任务页面，完成校验并全部校验项通过后，单击**启动任务**。
    如果校验任务不通过，可以参考 [校验不通过处理方法](https://cloud.tencent.com/document/product/571/58685) 修复问题后重新发起校验任务。
 - 失败：表示校验项检查未通过，任务阻断，需要修复问题后重新执行校验任务。
 - 警告：表示检验项检查不完全符合要求，可以继续任务，但对业务有一定的影响，用户需要根据提示自行评估是忽略警告项还是修复问题再继续。
![](https://qcloudimg.tencent-cloud.cn/raw/99e53691dc68b1a987424a3a91ada555.png)
7. 返回数据同步任务列表，任务开始进入**运行中**状态。
>?选择**操作**列的**更多** > **结束**可关闭同步任务，请您确保数据同步完成后再关闭任务。
>
![](https://qcloudimg.tencent-cloud.cn/raw/a14d84281ab739bfba84a61b2e09fa79.png)
8. （可选）您可以单击任务 ID，进入任务详情页，查看任务初始化状态和监控数据。

