## 背景信息
集群的统计信息对于集群的使用非常关键，云数据仓库 PostgreSQL 的查询优化器是根据动态计算出来的 cost（代价）来判断如何进行选择。那如何计算代价呢？这里一般是基于代价模型和统计信息，代价模型是否合理，统计信息是否准确都会影响查询优化的效果。

集群的表的空间利用也会影响查询代价，当表有更新操作（包括 INSERT VALUES、UPDATE、DELETE、ALTER TABLE ADD COLUMN 等）时，会在系统表和被更新的数据表中留存不再被使用的垃圾数据，造成系统性能下降，并占用大量磁盘空间，所以也需要定期监测表的数据膨胀情况。

下文就详细介绍统计信息和数据膨胀的定期监控以及维护。

## 统计信息收集
ANALYZE 收集一个数据库中表的内容的统计信息，并且将结果存储在 `pg_statistic` 系统目录中。查询计划器会使用这些统计信息来帮助确定查询最有效的执行计划，统计信息包含表的数据量、索引等信息，一个好的查询计划是基于准确的表统计信息。

### ANALYZE 说明
ANALYZE 是 Greenplum 提供的收集统计信息的命令。ANALYZE 支持三种粒度：列、表、库，具体如下:
```
CREATE TABLE foo (id int NOT NULL, bar text NOT NULL) DISTRIBUTED BY (id); // 创建测试表 foo
ANALYZE foo(bar);  // 只搜集 bar 列的统计信息
ANALYZE foo; // 搜集 foo 表的统计信息
ANALYZE; // 搜集当前库所有表的统计信息，需要有权限才行
```

### ANALYZE 使用限制
ANALYZE 会给目标表加 SHARE UPDATE EXCLUSIVE 锁，即会与 DDL 语句冲突。

### ANALYZE 速度
ANALYZE 是一种采样统计算法，通常不会扫描表中所有的数据，但是对于大表，也仍会消耗一定的时间和计算资源。

### ANALYZE 使用时机
根据上文所述，ANALYZE 会加锁并且也会消耗系统资源，因此运行命令需要选择合适的时机尽可能少的运行。以下4种情况发生后建议运行 ANALYZE。
- 批量加载数据后，例如新表创建导入数据后。
- 创建索引后。
- INSERT、UPDATE、DELETE 大量数据后。
- VACUUM FULL 执行清理后。

### ANALYZE 分区表
只要保持默认值，不去修改系统参数 `optimizer_analyze_root_partition`，那么对于分区表的操作并没有什么不同，直接在 root 表上进行 ANALYZE 即可，系统会自动把所有叶子节点的分区表的统计信息都收集起来。

如果分区表的数目很多，那在 root 表上进行 ANALYZE 可能会非常耗时。分区表通常是带有时间维度的，历史的分区表并不会修改，因此建议单独 ANALYZE 数据会发生变化的分区。

## 数据膨胀
Greenplum 数据库的堆表使用 PostgreSQL 的多版本并发控制（MVCC）存储实现。数据库会逻辑删除被删除或更新的行，但是该行的一个不可见映像将保留在表中，随着操作的进行，表的不可见数据会越来越多，在显著影响存储空间时会导致表操作性能严重下滑，并且膨胀的数据会占用大量的数据空间，因此需要定期对数据库的膨胀进行处理。

### 数据膨胀的监控
gp_toolkit 模式提供了一个 gp_bloat_diag 视图，它通过预计页数和实际页数的比率来确定表膨胀。要使用这个视图，需确定为数据库中所有的表都收集了最新的统计信息。然后运行下面的 SQL：
```
gpadmin=# SELECT * FROM gp_toolkit.gp_bloat_diag;
 bdirelid | bdinspname | bdirelname | bdirelpages | bdiexppages |                bdidiag                
----------+------------+------------+-------------+-------------+---------------------------------------
    21488 | public     | t1         |          97 |           1 | significant amount of bloat suspected
(1 row)
```
其中 bdirelpage 是 t1 表目前实际页面，bdiexppages 为 t1 表期望页面，当膨胀率超过4倍时就会被统计在该表中，没有出现在表中也有可能会有轻度膨胀，也可以对比不同时间的表的空间大小判断是否存在数据膨胀。

### 数据表膨胀的清理

`VACUUM <tablename>` 命令会把过期行加入到共享的空闲空间映射中，这样这些空间能被重用。当在被频繁更新的表上定期运行 VACUUM 时，过期行所占用的空间可以被迅速地重用，从而缓解表膨胀。需根据表更新，删除速度来决定 VACUUM 执行的周期。
>!VACUUM 和 ANALYZE 一样会持有共享更新锁（SHARE UPDATE EXCLUSIVE），该命令可能和 DDL 操作互锁。

当表已经出现明显膨胀时，VACUUM 只能起到延缓继续增长的作用，并不能够立即回收空间，这时需要使用 VACUUM FULL 命令，该命令能够立即回收所有膨胀空间，不过 VACUUM FULL 操作会对操作表加上访问独占（ACCESS EXCLUSIVE），期间该表上其余所有 DDL 和 DML 都将被锁住，并且针对大型表可能会需要很长时间执行，因此需要谨慎操作。

还有一种处理膨胀的方式就是进行表数据重分布：
1. 记录表的分布键。
2. 把该表的分布策略改为随机分布。
```
ALTER TABLE <tablename> SET WITH (REORGANIZE=false) 
                DISTRIBUTED randomly;
```
3. 把分布策略改回初始设置。
```
ALTER TABLE <table_name> SET WITH (REORGANIZE=true) 
DISTRIBUTED BY (<original distribution columns>);
```

### 索引膨胀的处理
VACUUM FULL 命令只会从表中恢复空间。要从索引中恢复空间，需要使用 REINDEX 命令重建它们。
```
REINDEX TABLE <table_name>    --- 重建一个表上所有索引  
REINDEX INDEX <index_name> --- 重建一个指定索引
```
>!REINDEX 和 VACUUM FULL 一样会加上访问独占（ACCESS EXCLUSIVE），因此需要谨慎操作。

## 定期进行集群维护
在使用集群的过程中，需要定期进行数据膨胀消除和统计信息维护，这样才能够让集群的使用性能达到最优。

### 不锁表清理
上文提到 `VACUUM <tablename>` 可以在不锁表的情况下标记可回收的空间，减缓数据膨胀，不锁表清理不会影响数据表读写，只是无法使用 DDL，并且会占用一定 CPU 内存资源。

**建议频率：**
- 大批量实时更新数据，每日多条数据发生变化，建议每天执行一次，每周至少两次。
- 正常情况一周执行一次，或者不频繁更新数据可以每月执行一次。

使用下述脚本可以通过 cron 定时任务清理一张表。
```
#!/bin/bash
export PGHOST=xxx.xxx.x.x
export PGPORT=5436
export PGUSER=test
export PGPASSWORD=test
db="test"
psql -d $db -e -c "VACUUM test_table;"
```

### 锁表全量清理
如果一张表会经常更新删除，那么建议规划一个业务暂停窗口，执行 VACUUM FULL 以及 REINDEX 来回收表的所有膨胀空间，锁表清理会对执行的表加上访问排它锁，期间被清理的表将无法进行任何操作。

1. 执行 `VACUUM FULL <tablename>` 
2. 执行 `REINDEX TABLE <tablename>`（没有索引的表可以不做）  
3. 执行 `ANALYZE <tablename> `

**建议频率：**建议每周执行一次。如果每天会更新几乎所有数据，需要每天做一次。

使用下述脚本可以实现集群表定期清理，建议在周末凌晨非业务期间进行。
```
#!/bin/bash
export PGHOST=xxx.xxx.x.x
export PGPORT=5436
export PGUSER=test
export PGPASSWORD=test
db="test"
psql -d $db -e -c "VACUUM FULL test_table;"
psql -d $db -e -c "REINDEX TABLE test_table;"
psql -d $db -e -c "ANALYZE test_table;"
```
