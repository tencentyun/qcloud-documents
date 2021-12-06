本文介绍使用 DTS 数据迁移功能，从 TDSQL MySQL 迁移数据至腾讯云分布式数据库 TDSQL MySQL 的操作指导。

如下场景的迁移要求与 TDSQL MySQL 到 TDSQL MySQL 的迁移要求一致，可参考本场景相关内容。

- TDSQL MySQL 到腾讯云数据库 MariaDB 的数据迁移
- TDSQL MySQL 到腾讯云数据库 MySQL 的数据迁移

>?如需体验本章节中 TDSQL MySQL 的迁移功能时，请 [提交工单](https://console.cloud.tencent.com/workorder/category) 进行申请。

## 注意事项
DTS 在执行全量数据迁移时，会占用一定源端实例资源可能会导致源实例负载上升，增加数据库自身压力。如果您数据库配置过低，建议您在业务低峰期进行。

## 前提条件
- 已 [创建分布式数据库 TDSQL MySQL版](https://cloud.tencent.com/document/product/557/10236)。
- 源数据库和目标数据库符合迁移功能和版本要求，请参见 [数据迁移支持的数据库](https://cloud.tencent.com/document/product/571/58686) 进行核对。
- 已完成 [准备工作](https://cloud.tencent.com/document/product/571/59968)。
- 需要您在源端 TDSQL MySQL 中提前创建好数据库：`__tencentdb__`。
- 需要具备源数据库的权限。
  - “整个实例”迁移，需要的帐号权限如下：
```
CREATE USER '迁移帐号'@'%' IDENTIFIED BY '迁移密码';  
GRANT RELOAD,LOCK TABLES,REPLICATION CLIENT,REPLICATION SLAVE,SHOW DATABASES,SHOW VIEW,PROCESS ON *.* TO '迁移帐号'@'%';  
GRANT INSERT, UPDATE, DELETE, DROP, SELECT, INDEX, ALTER, CREATE ON `__tencentdb__`.* TO '迁移帐号'@'%'; //如果源端为腾讯云数据库需要授予`__tencentdb__`权限
GRANT SELECT ON *.* TO '迁移帐号';
```
  - “指定对象”迁移，需要的帐号权限如下：
```
CREATE USER '迁移帐号'@'%' IDENTIFIED BY '迁移密码';  
GRANT RELOAD,LOCK TABLES,REPLICATION CLIENT,REPLICATION SLAVE,SHOW DATABASES,SHOW VIEW,PROCESS ON *.* TO '迁移帐号'@'%';  
GRANT INSERT, UPDATE, DELETE, DROP, SELECT, INDEX, ALTER, CREATE ON `__tencentdb__`.* TO '迁移帐号'@'%'; //如果源端为腾讯云数据库需要授予`__tencentdb__`权限
GRANT SELECT ON `mysql`.* TO '迁移帐号'@'%';
GRANT SELECT ON 待迁移的库.* TO '迁移帐号';
```
- 需要具备目标数据库的权限：ALTER, ALTER ROUTINE, CREATE, CREATE ROUTINE, CREATE TEMPORARY TABLES, CREATE USER, CREATE VIEW, DELETE, DROP, EVENT, EXECUTE, INDEX, INSERT, LOCK TABLES, PROCESS, REFERENCES, RELOAD, SELECT, SHOW DATABASES, SHOW VIEW, TRIGGER, UPDATE。

## 应用限制
- 只支持迁移基础表，不支持迁移视图、函数、触发器、存储过程等对象。

- 不支持迁移系统库表和用户信息，包括 `information_schema`， `sysdb`，`test`，`sys`， `performance_schema`， `__tencentdb__`， `mysql`。迁移完成后，如果需要调用目标库的视图、存储过程或函数，则要对调用者授予读写权限。 

- 只支持迁移 InnoDB 数据库引擎，如果存在其他的数据引擎表则默认跳过不进行迁移。

- 相互关联的数据对象需要同时迁移，否则会导致迁移失败。

- 增量迁移过程中，若源库存在分布式事务或者产生了类型为 `STATEMENT` 格式的 Binlog 语句，则会导致迁移失败。

- 不支持迁移 [二级分区](https://cloud.tencent.com/document/product/557/58907) 表，如果迁移的库表中包含二级分区表，存量数据会跳过二级分区表的迁移；如果选择整库或全实例迁移，增量过程中遇到二级分区表任务报错暂停。

## 操作限制
- 迁移过程中请勿进行如下操作，否则会导致迁移任务失败。
  - 请勿修改、删除源数据库和目标数据库中用户信息（包括用户名、密码和权限）和端口号。
  - 请勿在源库上执行分布式事务。
  - 请勿在源库写入 Binlog 格式为 `STATEMENT` 的数据。
  - 请勿在源库上执行清除 Binlog 的操作。
  - 在增量迁移阶段，请勿删除系统库表 `__tencentdb__`。 
- 如果仅执行全量数据迁移，请勿在迁移过程中向源实例中写入新的数据，否则会导致源和目标数据不一致。针对有数据写入的场景，为实时保持数据一致性，建议选择全量 + 增量数据迁移。
- 增量迁移过程中，不支持源库新增分片、调整分片规格，否则迁移任务不会同步新增分片的数据或是任务报错暂停，如果需要长期保持增量同步并且支持源库的新增分片、调整分片操作，请使用 [TDSQL 数据同步](https://cloud.tencent.com/document/product/571/63736) 来进行同步。

## 支持的 SQL 操作
| 操作类型 | 支持同步的 SQL 操作                                          |
| -------- | ------------------------------------------------------------ |
| DML      | INSERT、UPDATE、DELETE、REPLACE                              |
| DDL      | TABLE：CREATE TABLE、ALTER TABLE、DROP TABLE、TRUNCATE TABLE<br>VIEW：CREATE VIEW、DROP VIEW<br>INDEX：CREATE INDEX、DROP INDEX<br>DATABASE：CREATE DATABASE、ALTER DATABASE、DROP DATABASE |

## 环境要求
>?如下环境要求，系统会在启动迁移任务前自动进行校验，不符合要求的系统会报错。如果用户能够识别出来，可以参考 [校验项检查要求](https://cloud.tencent.com/document/product/571/58685) 自行修改，如果不能则等系统校验完成，按照报错提示修改。

<table>
<tr><th width="20%">类型</th><th width="80%">环境要求</th></tr>
<tr>
<td>源数据库要求</td>
<td>
<li>源库和目标库网络能够连通。</li>
<ul>
<li>实例参数要求：
<ul>
<li>table_row_format 不能设置为 FIXED。</li>
<li>源库和目标库 lower_case_table_names 变量必须设置一致。</li>
<li>检查目标端 max_allowed_packet 参数，至少设置 4M。</li>
<li>源库变量 connect_timeout 设置数值必须大于10。</li></ul></li>
<li>Binlog参数要求：
<ul>
<li>源端 binlog_format 变量必须设置为 ROW。</li>
<li>源端 log_bin 变量必须设置为 ON。</li>
<li>源端 binlog_row_image 变量必须设置为 FULL。</li>
<li>源端 gtid_mode 变量在5.6及以上版本不为 ON 时，会报 WARNING，建议用户打开 gtid_mode。</li>
<li>不允许设置 do_db, ignore_db。</li>
<li>对于源实例为从库的情况，log_slave_updates 变量必须设置为 ON。</li></ul></li>
<li>外键依赖：
<ul>
<li>外键依赖只能设置为 no action 和 restrict 两种类型。</li>
<li>部分库表迁移时，有外键依赖的表必须齐全。</li></ul></li></td></tr>
<tr> 
<td>目标数据库要求</td>
<td>
<li>目标库为分布式数据库时，推荐提前手动创建分表，并规划 shardkey，否则 DTS 会按照源库的表样式来在目标库创建表，如果源库为单机实例，则目标库会创建为单表。</li>
<li>目标库的版本必须大于等于源库的版本。</li>
<li>目标库的空间大小须是源库待迁移库表空间的1.2倍以上。</li>
<li>目标库不能有和源库冲突的库表。</li> 
</td></tr>
<tr> 
<td>其他要求</td>
<td>环境变量 innodb_stats_on_metadata 必须设置为 off。</td></tr>
</table>

## 操作步骤
1. 登录 [DTS 控制台](https://console.cloud.tencent.com/dts/migration)，在左侧导航选择**数据迁移**页，单击**新建迁移任务**，进入新建迁移任务页面。
2. 在新建迁移任务页面，选择迁移的目标实例所属地域，单击**0元购买**，目前 DTS 数据迁移功能免费使用。
3. 在设置源和目标数据库页面，完成任务设置、源库设置和目标库设置，测试源库和目标库连通性通过后，单击**新建**。
>?如果连通性测试失败，请根据提示和 [修复指导](https://cloud.tencent.com/document/product/571/58685) 进行排查和解决，然后再次重试。
<table>
<thead><tr><th width="15%">设置类型</th><th width="15%">配置项</th><th width="70%">说明</th></tr></thead>
<tbody><tr>
<td rowspan=3>任务设置</td>
<td>任务名称</td>
<td>设置一个具有业务意义的名称，便于任务识别。</td></tr>
<tr>
<td>运行模式</td>
<td>支持立即执行和定时执行：立即执行，则完成任务校验通过后立即启动任务；定时执行，需要配置一个任务执行时间则到时间后启动任务。</td></tr>
<tr>
<td>标签</td>
<td>标签用于从不同维度对资源分类管理。如现有标签不符合您的要求，请前往控制台管理标签。</td></tr>
<tr>
<td rowspan=6>源库设置</td>
<td>源库类型</td><td>选择“TDSQL MySQL”。</td></tr>
<tr>
<td>服务提供商</td><td>选择“普通”。</td></tr>
<tr>
<td>接入类型</td><td>选择“云数据库”。</td></tr>
<tr>
<td>所属地域</td><td>源库所属地域为 DTS 服务出口地域，选择离自建实例最近的一个地域即可。</td></tr>
<tr>
<td>帐号</td><td>源库 TDSQL MySQL 的数据库帐号，帐号权限需要满足要求。</td></tr>
<tr>
<td>密码</td><td>源库 TDSQL MySQL 的数据库帐号的密码。</td></tr>
<tr>
<td rowspan=6>目标库设置</td>
<td>目标库类型</td><td>选择“TDSQL MySQL版”。</td></tr>
<tr>
<td>接入类型</td><td>选择“云数据库”。</td></tr>
<tr>
<td>所属地域</td><td>上一步中已选择的地域。</td></tr>
<tr>
<td>数据库实例</td><td>选择目标端 TDSQL MySQL版 实例 ID。</td></tr>
<tr>
<td>帐号</td><td>目标端 TDSQL MySQL版 的数据库帐号，帐号权限需要满足要求。</td></tr>
<tr>
<td>密码</td><td>目标端 TDSQL MySQL版 的数据库帐号的密码。</td></tr>
</tbody></table>
4. 在设置迁移选项及选择迁移对象页面，设置迁移类型、对象，单击**保存**。
> ?
>- 如果用户在迁移过程中确定会使用 gh-ost、pt-osc 等工具对某张表做 Online DDL，则**迁移对象**需要选择这个表所在的整个库（或者整个实例），不能仅选择这个表，否则无法迁移 Online DDL 变更产生的临时表数据到目标数据库。
>- 如果用户在迁移过程中确定会对某张表使用 rename 操作（例如将 table A rename 为 table B），则**迁移对象**需要选择 table A 所在的整个库（或者整个实例），不能仅选择 table A，否则系统会报错。
>
<img src="https://qcloudimg.tencent-cloud.cn/raw/a595cd8f101830bd7a93604685de1547.png" style="zoom:80%;" />
<table>
<thead><tr><th>配置项</th><th>说明</th></tr></thead>
<tbody><tr>
<td>迁移类型</td>
<td>请根据您的场景选择。<ul><li>结构迁移：迁移数据库中的库、表等结构化的数据。</li><li>全量迁移：迁移整个数据库。</li><li>全量 + 增量迁移：迁移整个数据库和后续增量数据，如果迁移过程中有数据写入，需要不停机平滑迁移，请选择此场景。</li></ul></td></tr>
<tr>
<td>迁移对象</td>
<td><ul><li>整个实例：迁移整个实例，但不包括系统库，如information_schema、mysql、performance_schema、sys。</li>
<li>指定对象：迁移指定对象。</li></ul> </td></tr>
<tr>
<td>指定对象</td>
<td>在源库对象中选择待迁移的对象，然后将其移到已选对象框中。</td></tr>
</tbody></table>
5. 在校验任务页面，进行校验，校验任务通过后，单击**启动任务**。
如果校验任务不通过，可以参考 [校验不通过处理方法](https://cloud.tencent.com/document/product/571/58685) 修复问题后重新发起校验任务。
 - 失败：表示校验项检查未通过，任务阻断，需要修复问题后重新执行校验任务。
 - 警告：表示检验项检查不完全符合要求，可以继续任务，但对业务有一定的影响，用户需要根据提示自行评估是忽略警告项还是修复问题再继续。
<img src="https://qcloudimg.tencent-cloud.cn/raw/44e791fc319cd223e8e288e6376695a1.png" style="zoom:90%;" />
6. 返回数据迁移任务列表，任务进入创建中状态，运行1分钟 - 2分钟后，数据迁移任务开始正式启动。
   -  选择**结构迁移**或者**全量迁移**：任务完成后会自动结束，不需要手动结束。
   -  选择**全量 + 增量迁移**：全量迁移完成后会自动进入增量数据同步阶段，增量数据同步不会自动结束，需要您手动单击**完成**结束增量数据同步。
      - 请选择合适时间手动完成增量数据同步，并完成业务切换。
      - 观察迁移阶段为增量同步，并显示无延迟状态，将源库停写几分钟。
      - 目标与源库数据差距为0MB及目标与源库时间延迟为0秒时，手动完成增量同步。      
      ![](https://qcloudimg.tencent-cloud.cn/raw/c792a492834e2e9598d08d1e324d9c3f.png)
7. （可选）如果您需要进行查看任务、删除任务等操作，请单击对应的任务，在**操作**列进行操作，详情可参考 [任务管理](https://cloud.tencent.com/document/product/571/58674)。
8. 当迁移任务状态变为**任务成功**时，即可对业务进行正式割接，更多详情可参考 [割接说明](https://cloud.tencent.com/document/product/571/58660)。

