本文介绍使用 DTS 数据迁移功能，从通过 MySQL 迁移数据至物联网 SaaS 托管 MySQL 节点的操作指导。

## 前提条件

- 已 [创建物联网 SaaS 托管 MySQL 节点](https://cloud.tencent.com/document/product/1081/62046)。
- 源数据库和目标数据库符合迁移功能和版本要求，请参见 [数据迁移支持的数据库](https://cloud.tencent.com/document/product/571/58686) 进行核对。
- 已完成 [准备工作](https://cloud.tencent.com/document/product/571/59968)。
- 需要您在源端自建 MySQL 中创建迁移帐号，需要的帐号权限如下：
```
CREATE USER '迁移帐号'@'%' IDENTIFIED BY '迁移密码';  
GRANT RELOAD,LOCK TABLES,REPLICATION CLIENT,REPLICATION SLAVE,SHOW
DATABASES,SHOW VIEW,PROCESS ON *.* TO '迁移帐号'@'%';  
GRANT ALL PRIVILEGES ON `__tencentdb__`.* TO '迁移帐号'@'%';  
GRANT SELECT ON `mysql`.* TO '迁移帐号'@'%';
```
- 部分库表迁移：`GRANT SELECT ON 待迁移的库.* TO '迁移帐号';`
- 全实例迁移：`GRANT SELECT ON *.* TO '迁移帐号';`
- 需要具备目标数据库的权限：ALTER, ALTER ROUTINE, CREATE, CREATE ROUTINE, CREATE TEMPORARY TABLES, CREATE USER, CREATE VIEW, DELETE, DROP, EVENT, EXECUTE, INDEX, INSERT, LOCK TABLES, PROCESS, REFERENCES, RELOAD, SELECT, SHOW DATABASES, SHOW VIEW, TRIGGER, UPDATE。
- 源端账号遵循最小权限原则，仅需要必要的权限。若用户迁移中使用的帐号超出 DTS 迁移所需的权限，DTS 会给出警告，且迁移无法开始。

## 注意事项

- DTS 在执行全量数据迁移时，会占用一定源端实例资源可能会导致源实例负载上升，增加数据库自身压力。如果您数据库配置过低，建议您在业务低峰期进行。
- 源端 MySQL 中待迁移的表支持没有主键或唯一索引，并且不会导致目标数据库中出现重复数据。在全量迁移过程通过有锁迁移来实现，锁表过程中会短暂阻塞写入操作。

## 应用限制

- 只支持迁移基础表和视图，不支持迁移函数、触发器、存储过程等对象。
- 不支持迁移系统库表和用户信息，包括 `information_schema`， `sys`， `performance_schema`，`__cdb_recycle_bin__`， `__recycle_bin__`， `__tencentdb__`， `mysql`。迁移完成后，如果需要调用目标库的视图、存储过程或函数，则要对调用者授予读写权限。 
- 在导出视图结构时，DTS 会检查源库中 `DEFINER` 对应的 user1（ [DEFINER = user1]）和迁移目标的 user2 是否一致，如果不一致，则会修改 user1 在目标库中的 `SQL SECURITY` 属性，由 `DEFINER` 转换为 `INVOKER`（ [INVOKER = user1]），同时设置目标库中 `DEFINER` 为迁移目标的 user2（[DEFINER = 迁移目标 user2]）。
- 源端如果是非 GTID 实例，DTS 不支持源端 HA 切换，一旦源端 MySQL 发生切换可能会导致 DTS 增量同步中断。
- 只支持迁移 InnoDB、MySIAM、TokuDB 三种数据库引擎，如果存在这三种以外的数据引擎表则默认跳过不进行迁移。
- 相互关联的数据对象需要同时迁移，否则会导致迁移失败。常见的关联关系：视图引用表、视图引用视图、存储过程/函数/触发器引用视图/表、主外键关联表等。
- 增量迁移过程中，若源库存在分布式事务或者产生了类型为 `STATEMENT` 格式的 Binlog 语句，则会导致迁移失败。
- 无锁迁移场景（源库为阿里云 MySQL 5.6，阿里云 PolarDB MySQL 5.6，AWS MySQL，目标库为腾讯云 MySQL 数据库的场景），全量阶段不支持 DDL 操作。

## 操作限制

- 迁移过程中请勿进行如下操作，否则会导致迁移任务失败。
  - 请勿修改、删除源数据库和目标数据库中用户信息（包括用户名、密码和权限）和端口号。
  - 请勿在源库上执行分布式事务。
  - 请勿在源库写入 Binlog 格式为 `STATEMENT` 的数据。
  - 请勿在源库上执行清除 Binlog 的操作。
  - 在库表结构迁移和全量迁移阶段，请勿执行库或表结构变更的 DDL 操作。
  - 在增量迁移阶段，请勿删除系统库表 `__tencentdb__`。 
- 如果仅执行全量数据迁移，请勿在迁移过程中向源实例中写入新的数据，否则会导致源和目标数据不一致。针对有数据写入的场景，为实时保持数据一致性，建议选择全量 + 增量数据迁移。

## 支持的 SQL 操作

| 操作类型 | 支持同步的 SQL 操作                                            |
| -------- | ------------------------------------------------------------ |
| DML      | INSERT、UPDATE、DELETE、REPLACE                              |
| DDL      | TABLE：CREATE TABLE、ALTER TABLE、DROP TABLE、TRUNCATE TABLE、RENAEM TABLE <br>VIEW：CREATE VIEW、ALTER VIEW、DROP VIEW<br>INDEX：CREATE INDEX、DROP INDEX <br>DATABASE：CREATE DATABASE、ALTER DATABASE、DROP DATABASE |

## 环境要求

> ?如下环境要求，系统会在启动迁移任务前自动进行校验，不符合要求的系统会报错。如果用户能够识别出来，可以参考 [校验项检查要求](https://cloud.tencent.com/document/product/571/58685) 自行修改，如果不能则等系统校验完成，按照报错提示修改。

<table>
<tr><th width="20%">类型</th><th width="80%">环境要求</th></tr>
<tr>
<td>源数据库要求</td>
<td>
<li>源库和目标库网络能够连通。</li>
<ul>
<li>实例参数要求：
<ul>
<li>table_row_format 不能设置为 Fixed。</li>
<li>源库和目标库 lower_case_table_names 变量必须一致。</li>
<li>检查目标端 max_allowed_packet 参数，至少为4M。</li>
<li>源库变量 connect_timeout 必须大于10。</li></ul></li>
<li>Binlog 参数要求：
<ul>
<li>源端 binlog_format 变量必须为 ROW。</li>
<li>源端 log_bin 变量必须为 ON。</li>
<li>源端 binlog_row_image 变量必须为 FULL。</li>
<li>源端 gtid_mode 变量在5.6及以上版本不为 ON 时，会报 WARNING，建议用户打开 gtid_mode。</li>
<li>不允许设置 do_db, ignore_db。</li>
<li>对于源实例为从库的情况，log_slave_updates 变量必须为 ON。</li></ul></li>
<li>外键依赖：
<ul>
<li>外键依赖只能是 no action 和 restrict 两种类型。</li>
<li>部分库表迁移时，有外键依赖的表必须齐全。</li></ul></li></td></tr>
<tr> 
<td>目标数据库要求</td>
<td>
<li>目标库的版本必须大于等于源库的版本。</li>
<li>目标库的空间大小须是源库待迁移库表空间的1.2倍以上。</li>
<li>目标库不能有和源库冲突的库表。</li></td></tr>
<tr> 
<td>其他要求</td>
<td>环境变量 innodb_stats_on_metadata 需要设置为 OFF。</td></tr> 
</table>

## 操作步骤

不同接入类型的数据迁移步骤基本一致，本场景以“公网”接入方式为例进行介绍。

1. 登录 [DTS 控制台](https://console.cloud.tencent.com/dts/migration)，在左侧导航选择**数据迁移**页，单击**新建迁移任务**，进入新建迁移任务页面。
2. 在新建迁移任务页面，选择迁移的目标实例所属地域，单击**0元购买**，目前 DTS 数据迁移功能免费使用。
3. 在设置源和目标数据库页面，完成任务设置、源库设置和目标库设置，测试源库和目标库连通性通过后，单击**新建**。
>?如果连通性测试失败，请根据提示和 [修复指导](https://cloud.tencent.com/document/product/571/58685) 进行排查和解决，然后再次重试。
<table>
<thead><tr><th>设置类型</th><th>配置项</th><th>说明</th></tr></thead>
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
<td rowspan=8>源库设置</td>
<td>源库类型</td><td>选择“MySQL”。</td></tr>
<tr>
<td>服务提供商</td><td>选择“普通”。</td></tr>
<tr>
<td>接入类型</td><td>选择“公网”。</td></tr>
<tr>
<td>所属地域</td><td>源库所属地域为 DTS 服务出口地域，请选择离自建 MySQL 最近的一个地域即可。</td></tr>
<tr>
<td>主机地址</td><td>源库 MySQL 访问 IP 地址或域名。</td></tr>
<tr>
<td>端口</td><td>源库 MySQL 访问端口。</td></tr>
<tr>
<td>帐号</td><td>源库 MySQL 的数据库帐号，帐号权限需要满足要求。</td></tr>
<tr>
<td>密码</td><td>源库 MySQL 的数据库帐号的密码。</td></tr>
<tr>
<td rowspan=6>目标库设置</td>
<td>目标库类型</td><td>选择“TDSQL-C MySQL 版”。</td></tr>
<tr>
<td>接入类型</td><td>选择“云数据库”。</td></tr>
<tr>
<td>所属地域</td><td>上一步中已选择的地域。</td></tr>
<tr>
<td>数据库实例</td><td>选择目标端 MySQL 集群 ID。</td></tr>
<tr>
<td>帐号</td><td>目标端 MySQL 集群的数据库帐号，帐号权限需要满足要求。</td></tr>
<tr>
<td>密码</td><td>目标端 MySQL 集群的数据库帐号的密码。</td></tr>
</tbody></table>
4. 在设置迁移选项及选择迁移对象页面，设置迁移类型、对象，单击**保存**。
<table>
<thead><tr><th>配置项</th><th>说明</th></tr></thead>
<tbody><tr>
<td>迁移类型</td>
<td>如果只进行结构迁移，请选择结构迁移。<br>如果只进行数据全量迁移，请选择全量迁移。<br>如果需要不停机平滑迁移，请选择全量 + 增量迁移。</td></tr>
<tr>
<td>迁移对象</td>
<td>如果需要整个实例迁移，请选择整个实例，不包括系统库，如 information_schema、mysql、performance_schema、sys。 <br>如果需要指定库表迁移，请选择指定对象。</td></tr>
<tr>
<td>指定对象</td>
<td>在源库对象中选择待迁移的对象，然后将其移到已选对象框中。</td></tr>
</tbody></table>
<img src="https://main.qcloudimg.com/raw/51d26749a5a208f84c3750e9afc9ea32.png"  style="margin:0;">
5. 在校验任务页面，进行校验，校验任务通过后，单击**启动任务**。
 -  校验任务通过后，根据选择的运行模式启动迁移任务。
 -  如果校验任务不通过，可以查看具体检查项和失败原因，待问题解决后重新发起校验任务。
![](https://main.qcloudimg.com/raw/0a206c0f8f0c26da17ecb3b983c2ee52.png)
6. 返回数据迁移任务列表，任务进入创建中状态，运行1分钟 - 2分钟后，数据迁移任务开始正式启动。
 -  选择**结构迁移**或者**全量迁移**：任务完成后会自动结束，不需要手动结束。
 -  选择**全量 + 增量迁移**：全量迁移完成后会自动进入增量数据同步阶段，增量数据同步不会自动结束，需要您手动单击**完成**结束增量数据同步。
    - 请选择合适时间手动完成增量数据同步，并完成业务切换。
    - 观察迁移阶段为增量同步，并显示无延迟状态，将源库停写几分钟。
    - 目标与源库数据差距为0MB及目标与源库时间延迟为0秒时，手动完成增量同步。
    ![](https://main.qcloudimg.com/raw/e2b9ed2f2a63a0fdf28a557aa5f7aaf2.png)
7. （可选）如果您需要进行查看任务、删除任务等操作，请单击对应的任务，在**操作**列进行操作，详情可参考 [任务管理](https://cloud.tencent.com/document/product/571/58674)。
8. 当迁移任务状态变为**任务成功**时，即可对业务进行正式割接，更多详情可参考 [割接说明](https://cloud.tencent.com/document/product/571/58660)。
