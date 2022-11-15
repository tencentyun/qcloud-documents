TXRocks 是腾讯 TXSQL 团队基于 RocksDB 开发的事务型存储引擎，兼具更加节省存储空间和写⼊放⼤更低的优势。

## 产品介绍
TXRocks 是腾讯 TXSQL 团队基于 RocksDB 的事务型存储引擎，得益于 RocksDB LSM Tree 存储结构，既减少了 InnoDB ⻚⾯半满和碎⽚浪费，⼜可以使⽤紧凑格式存储，因此 TXRocks 在保持与 InnoDB 接近的性能的前提下，存储空间相⽐ InnoDB 可以节省⼀半甚⾄更多，⾮常适合对事务读写性能有要求，且数据存储量⼤的业务。

## 前提条件
数据库版本须为 MySQL 5.7、8.0，架构为双节点。

## 购买云数据库 MySQL 实例（RocksDB 引擎）
您可以在云数据库 MySQL [购买页](https://buy.cloud.tencent.com/cdb) 购买实例时，选择引擎为 RocksDB，其他参数项可参考 [创建 MySQL 实例](https://cloud.tencent.com/document/product/236/46433)。
![](https://qcloudimg.tencent-cloud.cn/raw/de5305050da41ff4df8f7d1538784850.png)
>?RocksDB 是 key-value 存储引擎，以高效写入能力与高压缩存储著称，目前暂时仅支持 MySQL 5.7、8.0 版本可选择引擎为 RocksDB。

## 创建 RocksDB 表
如果创建实例时设置了默认引擎为 RocksDB，则建表时默认引擎就是 RocksDB。您可以通过如下命令查看默认引擎：
```
show variables like '%default_storage_engine%';
```
![](https://qcloudimg.tencent-cloud.cn/raw/3bb1550d5995cece7cec2712ad62c5d0.png)
当默认引擎是 RocksDB 时，建表语句不许指定存储引擎。
![](https://qcloudimg.tencent-cloud.cn/raw/f4cb2efa27e236fb26a78971a8725cbd.png)
表创建成功后，后续的使用方法与 InnoDB一样，数据会存储在 RocksDB 引擎。

## 引擎功能限制
TXRocks 在引擎功能上有一些限制，具体如下表所示：
<table>
<thead><tr><th>功能分类</th><th>功能项</th><th>TXRocks 限制</th></tr></thead>
<tbody>
<tr>
<td>DDL</td><td>Online DDL</td><td>不⽀持，例如不⽀持 ALTER TABLE ... ALOGRITHM=INSTANT 功能，Partition 管理操作仅⽀持 COPY 算法</td></tr>
<tr>
<td rowspan="5">SQL 功能</td>
<td>外键</td><td>不⽀持外键（Foreign Key）</td></tr>
<td>分区表</td><td>不⽀持分区表 （Partition）</td></tr>
<td>⽣成列</td><td>不⽀持⽣成列 （Generated Columns）</td></tr>
<td>显式 Default 表达式</td><td>不支持，如 CREATE TABLE t1（c1 FLOAT DEFAULT(RAND())）ENGINE=ROCKSDB; 会失败，报错 'Specited storage engine' is not supported for default value expressions.</td></tr>
<td>加密表</td><td>不⽀持加密表</td></tr>
<tr> 
<td rowspan="3">索引</td>
<td>空间索引</td><td>不⽀持空间索引（Spatial Index）、空间数据类型（如 GEOMETRY、POINT等）</td></tr>
<tr> 
<td>全⽂索引</td><td>不⽀持全⽂索引（Fulltext Index）</td></tr>
<td>多值索引</td><td>不⽀持多值索引（multi-valued index）</td></tr>
<tr>
<td rowspan="4">复制</td>
<td>组复制</td><td>不⽀持组复制（Group Replication）</td></tr>
<td>binlog 格式</td><td>仅⽀持 ROW 格式，不⽀持 stmt 或者 mixed 格式</td></tr>
<td>克隆插件</td><td>不⽀持克隆插件（Clone Plugin）</td></tr>
<td>可传输表空间</td><td>不⽀持可传输表空间（Transportable Tablespace）</td></tr>
<tr>
<td rowspan="5">事务与锁</td>
<td>LOCK NOWAIT 和 SKIP LOCKED</td><td>不⽀持 LOCK NOWAIT 和 SKIP LOCKED</td></tr>
<td>间隙锁</td><td>不⽀持间隙锁（Gap Lock）</td></tr>
<td>Savepoint</td><td>不⽀持 Savepoint</td></tr>
<td>部分更新 LOB 字段</td><td>不⽀持部分更新 LOB 字段</td></tr>
<td>XA 事务</td><td>不建议使⽤</td></tr>
</tbody></table>	

## 参数说明
>?在创建云数据库 MySQL 实例时，可以选择 RocksDB 为默认存储引擎，也可以根据下表的参数说明调整参数模板以便适应自身业务。

#### MySQL 5.7 相关参数列表

| 参数名称 | 是否需要重启 | 默认值 | 允许值 | 描述 |
|---------|---------|---------|---------|---------|
| rocksdb_use_direct_io_for_flush_and_compaction | 是 | ON | ON/OFF | compaction 时是否使用 DIO。 |
| rocksdb_flush_log_at_trx_commit | 否 | 1 | 0/1/2 | 控制何时将日志写入磁盘。<br>类似于 innodb_flush_log_at_trx_commit，事务提交时是否进行同步。<li>等于0时，事务提交时不同步；<li>等于1时，每次事务提交时都同步；<li>等于2时，每1秒同步一次。</li>  |
| rocksdb_lock_wait_timeout | 否 | 1 | 1-1073741824 | 锁等待超时时间，单位秒。 |
| rocksdb_deadlock_detect | 否 | ON | ON/OFF | 死锁检测开关，开启后，有关所有死锁的信息将记录在 mysqld 错误日志中。 |
| rocksdb_manual_wal_flush | 是 | ON | ON/OFF | rocksdb_max_total_wal_size，WAL 超过这个大小，RocksDB 会开始强制列族落盘，以保证删除最老的 WAL 文件。 |

#### MySQL 8.0 相关参数列表

| 参数名称 | 是否需要重启 | 默认值 | 允许值 | 描述 |
|---------|---------|---------|---------|---------|
| rocksdb_flush_log_at_trx_commit | 否 | 1 | 0/1/2 | 控制何时将日志写入磁盘。<br>类似于 innodb_flush_log_at_trx_commit，事务提交时是否进行同步。<li>等于0时，事务提交时不同步；<li>等于1时，每次事务提交时都同步；<li>等于2时，每1秒同步一次。 </li>|
| rocksdb_lock_wait_timeout | 否 | 1 | 1-1073741824 | 锁等待超时时间，单位秒。 |
| rocksdb_merge_buf_size | 否 | 524288(=512K) | 100-18446744073709551615 | 创建二级索引过程中用到的 merge-sort buffer 大小。 |
| rocksdb_merge_combine_read_size | 否 | 8388608 (=8M) | 524288(=512K)-18446744073709551615 | 创建二级索引过程中用到的多路归并过程使用的内存大小。 |
| rocksdb_deadlock_detect | 否 | ON | ON/OFF | 死锁检测开关。 |
| rocksdb_manual_wal_flush | 是 | ON | ON/OFF | rocksdb_max_total_wal_size，WAL 超过这个大小，RocksDB 会开始强制列族落盘，以保证删除最老的 WAL 文件。 |

## RocksDB 引擎监控项
下表为 RocksDB 的引擎监控指标。

| 指标 | 描述 | 
|---------|---------|
| rocksdb_bytes_read | 读磁盘量 |
| rocksdb_bytes_written | 写磁盘量 |
| rocksdb_block_cache_bytes_read | 读数据块数 |
| rocksdb_block_cache_bytes_write | 写数据块数 |
| rocksdb_wal_log_capacity | 写 WAL 日志大小 |

