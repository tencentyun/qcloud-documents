本文介绍使用 DTS 数据迁移功能，从 MySQL 迁移数据至腾讯云数据库 MariaDB（Percona）的操作指导。

如下场景的迁移要求与 MySQL 到 MariaDB（Percona）的迁移要求一致，可参考本场景相关内容。

- MariaDB 到腾讯云数据库 MariaDB 的数据迁移
- MariaDB（Percona）到腾讯云数据库 MariaDB（Percona）的数据迁移

## 注意事项

- DTS 在执行全量数据迁移时，会占用一定源端实例资源可能会导致源实例负载上升，增加数据库自身压力。如果您数据库配置过低，建议您在业务低峰期进行。
- 在全量迁移过程通过有锁迁移来实现，锁表过程中会短暂阻塞写入操作。

## 前提条件

- 已 [创建云数据库 MariaDB](https://cloud.tencent.com/document/product/237/7051)。
- 源数据库和目标数据库符合迁移功能和版本要求，请参见 [数据迁移支持的数据库](https://cloud.tencent.com/document/product/571/58686) 进行核对。
- 已完成 [准备工作](https://cloud.tencent.com/document/product/571/59968)。
- 需要您在源端 MySQL 中提前创建好数据库：`__tencentdb__`。
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

- 只支持迁移基础表和视图，不支持迁移函数、触发器、存储过程等对象。
- 不支持迁移系统库表和用户信息，包括 `information_schema`， `sys`， `performance_schema`， `__tencentdb__`， `mysql`。迁移完成后，如果需要调用目标库的视图、存储过程或函数，则要对调用者授予读写权限。 
- 在导出视图结构时，DTS 会检查源库中 `DEFINER` 对应的 user1（ [DEFINER = user1]）和迁移目标的 user2 是否一致，如果不一致，则会修改 user1 在目标库中的 `SQL SECURITY` 属性，由 `DEFINER` 转换为 `INVOKER`（ [INVOKER = user1]），同时设置目标库中 `DEFINER` 为迁移目标的 user2（[DEFINER = 迁移目标 user2]）。
- 只支持迁移 InnoDB 数据库引擎，如果存在其他的数据引擎表则默认跳过不进行迁移。
- 相互关联的数据对象需要同时迁移，否则会导致迁移失败。
- 增量迁移过程中，若源库存在分布式事务或者产生了类型为 `STATEMENT` 格式的 Binlog 语句，则会导致迁移失败。

## 操作限制

- 迁移过程中请勿进行如下操作，否则会导致迁移任务失败。
  - 请勿修改、删除源数据库和目标数据库中用户信息（包括用户名、密码和权限）和端口号。
  - 请勿在源库上执行分布式事务。
  - 请勿在源库写入 Binlog 格式为 `STATEMENT` 的数据。
  - 请勿在源库上执行清除 Binlog 的操作。
  - 在增量迁移阶段，请勿删除系统库表 `__tencentdb__`。 
- 如果仅执行全量数据迁移，请勿在迁移过程中向源实例中写入新的数据，否则会导致源和目标数据不一致。针对有数据写入的场景，为实时保持数据一致性，建议选择全量 + 增量数据迁移。

## 支持的 SQL 操作

| 操作类型 | 支持同步的 SQL 操作                                          |
| -------- | ------------------------------------------------------------ |
| DML      | INSERT、UPDATE、DELETE、REPLACE                              |
| DDL      | TABLE：CREATE TABLE、ALTER TABLE、DROP TABLE、TRUNCATE TABLE<br>VIEW：CREATE VIEW、DROP VIEW<br>INDEX：CREATE INDEX、DROP INDEX <br>DATABASE：CREATE DATABASE、ALTER DATABASE、DROP DATABASE |

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
<li>table_row_format 不能设置为 FIXED。</li>
<li>源库和目标库 lower_case_table_names 变量必须设置一致。</li>
<li>检查目标端 max_allowed_packet 参数，至少设置4M。</li>
<li>源库变量 connect_timeout 设置数值必须大于10。</li></ul></li>
<li>Binlog 参数要求：
<ul>
<li>源端 binlog_format 变量必须设置为 ROW。</li>
<li>源端 log_bin 变量必须设置为 ON。</li>
<li>源端 binlog_row_image 变量必须设置为FULL。</li>
<li>源端 gtid_mode 变量在5.6及以上版本不为 ON 时，会报 WARNING，建议用户打开 gtid_mode。</li>
<li>不允许设置 do_db，ignore_db。</li>
<li>对于源实例为从库的情况，log_slave_updates 变量必须设置为 ON。</li></ul></li>
<li>外键依赖：
<ul>
<li>外键依赖只能设置为 no action 和 restrict 两种类型。</li>
<li>部分库表迁移时，有外键依赖的表必须齐全。</li></ul></li></td></tr>
<tr> 
<td>目标数据库要求</td>
<td>
<li>目标库的版本必须大于等于源库的版本。</li>
<li>目标库的空间大小须是源库待迁移库表空间的1.2倍以上。</li>
<li>目标库不能有和源库冲突的库表。</li>
<li>源数据库实例为分布式数据库时，需要提前在目标库建立分表，否则这些表被迁移后都将是单表。</li></td></tr>
<tr> 
<td>其他要求</td>
<td>环境变量 innodb_stats_on_metadata 必须设置为 OFF。</td></tr>
</table>

## 操作步骤
不同场景的数据迁移步骤基本一致，请参考 [MySQL 到 TDSQL MySQL 的迁移](https://cloud.tencent.com/document/product/571/59971) 进行操作。

