本文为您介绍使用数据传输服务 DTS 从 MySQL、MariaDB、Percona 数据库同步数据至腾讯云数据库 MariaDB 的过程。

源数据库支持的部署类型如下：

- 自建 MySQL、腾讯云数据库 MySQL。
- 自建 MariaDB、腾讯云数据库 MariaDB。
- 自建 Percona。

因为 MySQL、MariaDB、Percona 同步至腾讯云数据库 MariaDB，三种场景的同步要求和操作步骤基本一致，本章节仅以 MariaDB 到 MariaDB 的数据同步为例进行介绍，其他场景请参考相关内容。

## 注意事项
- DTS 在执行全量数据同步时，会占用一定源端实例资源，可能会导致源实例负载上升，增加数据库自身压力。如果您数据库配置过低，建议您在业务低峰期进行。
- 为了避免数据重复，请确保需要同步的表具有主键或者非空唯一键。
- 默认采用无锁方式，同步过程中对源库不加全局锁（FTWRL），仅对无主键的表加表锁，其他不加锁。
- 数据同步时，DTS 会使用执行同步任务的账号在源库中写入系统库`__tencentdb__`，用于记录同步任务过程中的数据对比信息。
  - 为保证后续数据对比问题可定位，同步任务结束后不会删除源库中的`__tencentdb__`。
  - `__tencentdb__`系统库占用空间非常小，约为源库存储空间的千分之一到万分之一（例如源库为50GB，则`__tencentdb__`系统库约为5MB - 50MB），并且采用单线程，等待连接机制，所以对源库的性能几乎无影响，也不会抢占资源。 

## [前提条件](id:qttj)
- 源数据库和目标数据库符合同步功能和版本要求，请参考 [数据同步支持的数据库](https://cloud.tencent.com/document/product/571/58672) 进行核对。
- 需要具备源数据库的权限如下：
```sql
GRANT RELOAD,LOCK TABLES,REPLICATION CLIENT,REPLICATION SLAVE,SHOW VIEW,PROCESS,SELECT ON *.* TO '帐号'@'%' IDENTIFIED BY '密码';
GRANT ALL PRIVILEGES ON `__tencentdb__`.* TO '帐号'@'%'; 
FLUSH PRIVILEGES;
```
- 需要具备目标数据库的权限：ALTER, ALTER ROUTINE, CREATE, CREATE ROUTINE, CREATE TEMPORARY TABLES, CREATE USER, CREATE VIEW, DELETE, DROP, EVENT, EXECUTE, INDEX, INSERT, LOCK TABLES, PROCESS, REFERENCES, RELOAD, SELECT, SHOW DATABASES, SHOW VIEW, TRIGGER, UPDATE。

## 应用限制
- 只支持同步基础表、视图、存储过程和函数。 
- 在同步视图、存储过程和函数时，DTS 会检查源库中 `DEFINER` 对应的 user1（ [DEFINER = user1]）和同步账号 user2 是否一致，如果不一致，同步后 DTS 会修改 user1 在目标库中的 `SQL SECURITY` 属性，由 `DEFINER` 转换为 `INVOKER`（ [INVOKER = user1]），同时设置目标库中 `DEFINER` 为同步账号 user2（[DEFINER = 同步账号 user2]）。如果源库中视图定义过于复杂，可能会导致任务失败。
- 源端如果是非 GTID 实例，DTS 不支持源端 HA 切换，一旦源端 MySQL 发生切换可能会导致 DTS 增量同步中断。
- 只支持同步 InnoDB、MyISAM、TokuDB 三种数据库引擎，如果存在这三种以外的数据引擎表则默认跳过不进行同步。
- 相互关联的数据对象需要一起同步，否则会导致同步失败。常见的关联关系：视图引用表、视图引用视图、主外键关联表等。
- 增量同步过程中，若源库存在分布式事务或者产生了类型为 `STATEMENT` 格式的 Binlog 语句，则会导致同步失败。
- 源数据库为阿里云 MySQL，则阿里云 MySQL 5.6 版本待同步表不能存在无主键表，MySQL 5.7 及以后版本不限制。源数据库为 AWS MySQL，则 AWS MySQL 待同步表不能存在无主键表。
- 源数据库 Binlog 的 GTID 如果存在空洞，可能会影响同步任务的性能并导致任务失败。
- 不支持同时包含 DML 和 DDL 语句在一个事务的场景，遇到该情况任务会报错。
- 不支持 Geometry 相关的数据类型，遇到该类型数据任务报错。
- 不支持 `ALTER VIEW` 语句，遇到该语句任务跳过不同步。

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
| DDL      | CREATE DATABASE、DROP DATABASE、ALTER DATABASE、CREATE TABLE、ALTER TABLE、DROP TABLE、TRUNCATE TABLE、RENAEM TABLE、CREATE VIEW、DROP VIEW、CREATE INDEX、DROP INDEX<br><dx-alert infotype="explain" title="说明">不支持同步涉及分区（Partition）的 DDL。</dx-alert> |

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
<li>源库变量 connect_timeout设置数值必须大于10。</li></ul></li>
<li>Binlog 参数要求：
<ul>
<li>源端 log_bin 变量必须设置为 ON。</li>
<li>源端 binlog_format 变量必须设置为 ROW。</li>
<li>源端 binlog_row_image 变量必须设置为 FULL。</li>
<li>MySQL 5.6 及以上版本 gtid_mode 变量不为 ON 时会报警告，建议打开 gtid_mode。</li>
<li>不允许设置 do_db, ignore_db。</li>
<li>源实例为从库时，log_slave_updates 变量必须设置为 ON。</li>
   <li>建议源库 Binlog 日志至少保留3天及以上，否则可能会因任务暂停/中断时间大于 Binlog 日志保留时间，造成任务无法续传，进而导致任务失败。</li>
  </ul></li>
<li>外键依赖：
<ul>
<li>外键依赖只能设置为 NO ACTION，RESTRICT 两种类型。</li>
<li>部分库表同步时，有外键依赖的表必须齐全。</li></ul></li>
  <li>环境变量 innodb_stats_on_metadata 必须设置为 OFF。</li></td></tr>
<tr> 
<td>目标数据库要求</td>
<td>
<li>目标库的版本必须大于等于源库的版本。</li>
<li>目标库需要有足够的存储空间，如果初始类型选择“全量数据初始化”，则目标库的空间大小须是源库待同步库表空间的1.2倍以上。</li>
<li>目标库不能有和源库同名的表、视图等同步对象。</li>
<li>目标库 max_allowed_packet 参数设置数值至少为4M。</li></td></tr>
</table>

## 操作步骤
本场景操作步骤与 [MySQL 数据同步至 MySQL](https://cloud.tencent.com/document/product/571/56516) 的一致，请参考 MySQL 同步场景的操作步骤。
