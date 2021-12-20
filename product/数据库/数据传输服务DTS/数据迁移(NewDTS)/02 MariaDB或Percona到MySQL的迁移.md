本文介绍使用 DTS 数据迁移功能从 MariaDB 或者 Percona 迁移数据至腾讯云数据库 MySQL 的操作指导。

 如下场景的迁移要求与迁移与 MariaDB 或者 Percona 迁移到 MySQL 的要求基本一致，请参考本场景相关内容。

- MariaDB 到 MariaDB 的数据迁移

- MariaDB 到 TDSQL-C 的数据迁移

- Percona 到 TDSQL-C 的数据迁移

- Percona 到 MariaDB 的数据迁移

- MySQL 到 MariaDB 的数据迁移

> ?腾讯云数据库 MariaDB 支持三种内核 MariaDB、Percona 和 MySQL，用户在使用时不需要区分哪种内核，如果源数据库为腾讯云 MariaDB，不论源数据库的内核是 MariaDB、Percona 还是 MySQL，在设置源数据库或目标数据库的类型时，都选择 MariaDB。

## 注意事项 
- DTS 在执行全量数据迁移时，会占用一定源端实例资源，可能会导致源实例负载上升，增加数据库自身压力。如果您的数据库配置过低，建议您在业务低峰期进行迁移。
- 全量迁移过程通过有锁（备份锁）迁移来实现，锁表过程中会短暂（秒级）阻塞写入操作。

## 前提条件
- 已 [创建云数据库 MySQL](https://cloud.tencent.com/document/product/236/46433)。
- 源数据库和目标数据库符合迁移功能和版本要求，请参见 [数据迁移支持的数据库](https://cloud.tencent.com/document/product/571/58686) 进行核对。
- 已完成 [准备工作](https://cloud.tencent.com/document/product/571/59968)。
- 源数据库需要具备的权限如下：
  - “整个实例”迁移：
```
CREATE USER '迁移帐号'@'%' IDENTIFIED BY '迁移密码';  
GRANT RELOAD,LOCK TABLES,REPLICATION CLIENT,REPLICATION SLAVE,SHOW DATABASES,SHOW VIEW,PROCESS ON *.* TO '迁移帐号'@'%';  
GRANT ALL PRIVILEGES ON `__tencentdb__`.* TO '迁移帐号'@'%';  //如果源端为腾讯云数据库需要授予`__tencentdb__`权限
GRANT SELECT ON *.* TO '迁移帐号';
```
  - “指定对象”迁移：
```
CREATE USER '迁移帐号'@'%' IDENTIFIED BY '迁移密码';  
GRANT RELOAD,LOCK TABLES,REPLICATION CLIENT,REPLICATION SLAVE,SHOW DATABASES,SHOW VIEW, RELOAD, PROCESS ON *.* TO '迁移帐号'@'%';  //源端若为腾讯云 MariaDB 数据库，需要提交工单进行 RELOAD 授权，其他场景请用户参照代码授权
GRANT ALL PRIVILEGES ON `__tencentdb__`.* TO '迁移帐号'@'%';  //如果源端为腾讯云数据库需要授予`__tencentdb__`权限
GRANT SELECT ON `mysql`.* TO '迁移帐号'@'%';
GRANT SELECT ON 待迁移的库.* TO '迁移帐号';
```
 - 源数据库为 MariaDB 10.5、10.6 版本时，还需要 SLAVE MONITOR 的权限才能执行 show slave status。
- 目标数据库需要具备的权限：ALTER, ALTER ROUTINE, CREATE,  CREATE ROUTINE, CREATE TEMPORARY TABLES,  CREATE USER,  CREATE VIEW,  DELETE,  DROP,  EVENT,  EXECUTE,  INDEX,  INSERT,  LOCK TABLES,  PROCESS,  REFERENCES,  RELOAD,  SELECT,  SHOW DATABASES,  SHOW VIEW,  TRIGGER,  UPDATE（如果目标库为腾讯云 MariaDB 数据库，需要 [提交工单](https://console.cloud.tencent.com/workorder/category) 进行 RELOAD 授权）。

## 异构迁移兼容性说明
MariaDB 迁移到 MySQL，由于不同的数据库类型之间功能有略微差异，会存在以下兼容性问题。
1. 由于 MariaDB 自身的功能特性，部分 SQL 执行语句与 SHOW CREATE TABLE 不一致，可能导致目标端同步的 DDL 语句有差别。
   - MariaDB 中的 blob 类型不指定默认值，创建表后 SHOW CREATE TABLE 会显示有默认值 DEFAULT NULL。   
   - datetime 类型 DDL 语句在源数据为 `datetime NOT NULL ON UPDATE CURRENT_TIMESTAMP`，创建表后 SHOW CREATE TABLE 显示 `datetime NOT NULL DEFAULT '0000-00-00 00:00:00' ON UPDATE current_timestamp()`，在目标端 MySQL 解析的 DDL 为：`datetime NOT NULL ON UPDATE CURRENT_TIMESTAMP`。

2. 一些仅 MariaDB 支持的语法（例如 CREATE OR REPLACE TABLE/PERIOD FOR/WITHOUT OVERLAPS 等），在全量阶段可能导致迁移任务报错，在增量阶段会忽略这些语句。 
   - 对于 PERIOD FOR/WITHOUT OVERLAPS 语句，在迁移任务启动前，或者在任务进行中的全量阶段（源库导出和数据导入步骤）有执行该语句，则迁移任务失败；在同步增量阶段执行该语句，则目标端会忽略，数据无法同步到目标端。
   - 对于 CREATE OR REPLACE TABLE 语句， 由于在全量迁移阶段，不能执行库或表结构变更的 DDL 操作，所以全量阶段执行该语句，迁移任务会失败；在同步增量阶段执行该语句，则目标端会忽略，数据无法同步到目标端。 

3. MariaDB 允许 blob/text 等有默认值，但 MySQL 不允许，如果有这种类型的 SQL 会导致迁移任务报错。  

## 应用限制
- 只支持迁移基础表和视图，不支持迁移函数、触发器、存储过程等对象。
- 不支持迁移系统库表和用户信息，包括 `information_schema`， `sys`，`sysdb`、 `performance_schema`，`__cdb_recycle_bin__`， `__recycle_bin__`， `__tencentdb__`， `mysql`。迁移完成后，如果需要调用目标库的视图、存储过程或函数，则要对调用者授予读写权限。 
- 在导出视图结构时，DTS 会检查源库中 `DEFINER` 对应的 user1（ [DEFINER = user1]）和迁移目标的 user2 是否一致，如果不一致，则会修改 user1 在目标库中的 `SQL SECURITY` 属性，由 `DEFINER` 转换为 `INVOKER`（ [INVOKER = user1]），同时设置目标库中 `DEFINER` 为迁移目标的 user2（[DEFINER = 迁移目标 user2]）。
- 源端如果是非 GTID 实例，DTS 不支持源端 HA 切换，一旦源端 MySQL 发生切换可能会导致 DTS 增量同步中断。
- 只支持迁移 InnoDB、MySIAM、TokuDB 三种数据库引擎，如果存在这三种以外的数据引擎表则默认跳过不进行迁移。
- 相互关联的数据对象需要同时迁移，否则会导致迁移失败。常见的关联关系：视图引用表、视图引用视图、存储过程/函数/触发器引用视图/表、主外键关联表等。
- 增量迁移过程中，若源库存在分布式事务或者产生了类型为 `STATEMENT` 格式的 Binlog 语句，则会导致迁移失败。
- 源数据库为腾讯云 MariaDB 时，应用限制如下。
   - DTS 迁移任务要求源库、目标库的 `lower_case_tame_name` 参数（表名大小敏感）保持一致，如果源数据库为腾讯云数据库 MariaDB，由于云数据库 MariaDB 只能在创建实例时修改 `lower_case_tame_name` 参数，所以用户需要在创建源库实例时确定大小写敏感规则，并在参数校验不一致时，修改目标库的 `lower_case_tame_name` 参数。
   - 源数据库为腾讯云数据库 MariaDB 10.4 版本时，在迁移任务配置中，**接入类型**不支持选择**云数据库**，需要选择**公网**或者其他方式。//待确认

## 操作限制
- 迁移过程中请勿进行如下操作，否则会导致迁移任务失败。
  - 请勿修改、删除源数据库和目标数据库中用户信息（包括用户名、密码和权限）和端口号。
  - 请勿在源库上执行分布式事务。
  - 请勿在源库写入 Binlog 格式为 `STATEMENT` 的数据。
  - 请勿在源库上执行清除 Binlog 的操作。
  - 在库表结构迁移和全量迁移阶段，请勿执行库或表结构变更的 DDL 操作。
  - 在增量迁移阶段，请勿删除系统库表 `__tencentdb__`。 
  - 对于 MariaDB 的特有语法，如 CREATE OR REPLACE TABLE/PERIOD FOR/WITHOUT OVERLAPS，在全量阶段可能导致迁移任务报错，在增量阶段会忽略这些语句。
- 如果仅执行全量数据迁移，请勿在迁移过程中向源实例中写入新的数据，否则会导致源和目标数据不一致。针对有数据写入的场景，为实时保持数据一致性，建议选择全量+增量数据迁移。

## 支持的 SQL 操作
| 操作类型 | 支持的 SQL 操作                                              |
| -------- | ------------------------------------------------------------ |
| DML      | INSERT、UPDATE、DELETE、REPLACE                              |
| DDL      | TABLE：CREATE TABLE、ALTER TABLE、DROP TABLE、TRUNCATE TABLE、RENAEM TABLE <br>VIEW：CREATE VIEW、DROP VIEW<br>INDEX：CREATE INDEX、DROP INDEX <br>DATABASE：CREATE DATABASE、ALTER DATABASE、DROP DATABASE |

## 环境要求
>?如下环境要求，系统会在启动迁移任务前自动进行校验，不符合要求的系统会报错。如果用户能够识别出来，可以参考 [校验项检查要求](https://cloud.tencent.com/document/product/571/58685) 自行修改，如果不能则等系统校验完成，按照报错提示修改。

<table>
<tr><th width="20%">类型</th><th width="80%">环境要求</th></tr>
<tr>
<td>源数据库要求</td>
<td>
<ul>
<li>源库和目标库网络能够连通。</li>
<li>源库所在的服务器需具备足够的出口带宽，否则将影响迁移速率。</li>
<li>实例参数要求：
<ul>
<li>源库 server_id 参数需要手动设置，且值不能设置为0。</li>
<li>源库表的 row_format 不能设置为 FIXED。</li>
<li>源库和目标库 lower_case_table_names 变量必须设置为一致。</li>
<li>源库变量 connect_timeout 设置数值必须大于10。</li>
<li>建议开启 skip-name-resolve，减少连接超时的可能性。</li></ul></li>
<li>Binlog 参数要求：
<ul>
<li>源库 log_bin 变量必须设置为 ON。</li>
<li>源库 binlog_format 变量必须设置为 ROW。</li>
<li>源库 binlog_row_image 变量必须设置为 FULL。</li>
<li>MariaDB 10.2 及以上版本，Percona 5.6 及以上版本 gtid_mode 变量不为 ON 时会报警告，建议打开 gtid_mode。</li>
<li>不允许设置 do_db, ignore_db 过滤条件。</li>
<li>源实例为从库时，log_slave_updates 变量必须设置为 ON。</li>
</ul></li>
<li>外键依赖：
<ul>
<li>外键依赖只能设置为 NO ACTION，RESTRICT 两种类型。</li>
<li>部分库表迁移时，有外键依赖的表必须齐全。</li>
</ul></li>
<li>DTS 对数据类型为 FLOAT 的迁移精度为38位，对数据类型为 DOUBLE 的迁移精度为308位，需要确认是否符合预期。</li></ul></td></tr>
<tr> 
<td>目标数据库要求</td>
<td>
<li>目标库的版本必须大于等于源库的版本。</li>
<li>目标库的空间大小须是源库待迁移库表空间的1.2倍以上。（全量数据迁移会并发执行 INSERT 操作，导致目标数据库的表产生碎片，因此全量迁移完成后目标数据库的表存储空间很可能会比源实例的表存储空间大）</li>
<li>目标库不能有和源库同名的表、视图等迁移对象。</li>
<li>目标库 max_allowed_packet 参数设置数值至少为4M。</li></td></tr>
<tr> 
<td>其他要求</td>
<td>环境变量 innodb_stats_on_metadataw 必须设置为 OFF。</td></tr>
</table>

## 操作步骤
MariaDB 到 MySQL 的迁移、Percona 到 MySQL 的迁移，与 MySQL 到 MySQL 的迁移操作步骤一致，请参考 [MySQL 到 MySQL 的迁移](https://cloud.tencent.com/document/product/571/58688#.E6.93.8D.E4.BD.9C.E6.AD.A5.E9.AA.A4) 进行配置。
