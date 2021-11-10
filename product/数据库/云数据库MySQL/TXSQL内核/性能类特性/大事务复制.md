## 功能介绍
在 row 模式下，单个语句更新多行的大事务每行生成1个 event，一方面产生大量 binlog，另一方面复制时备库 apply 的时候也比较慢，导致备库复制延迟。
腾讯云内核团队通过对大事务复制场景的分析和优化，开发了该能力，大事务复制优化功能将自动识别大事务，并将 row 模式的 binlog 转化为 statement 格式的 binlog，从而减少 binlog 并提升复制效率。

## 支持版本
- 内核版本 MySQL 5.6 20210630 及以上
- 内核版本 MySQL 5.7 20200630 及以上
- 内核版本 MySQL 8.0 20200830 及以上

## 适用场景
- 该功能主要提升 row 模式下无主键表的大事务回放速度，在确定是由无主键回放慢导致延迟时可以打开。
- 该功能主要针对 row 模式下存在大事务，出现复制较慢的场景。

## 性能数据
update 场景复制时间减少85%，insert 场景减少约30%。

## 使用说明
大事务复制优化功能是基于 SQL 历史执行的统计情况去判断它是否有可能是大事务； 当识别为大事务时并且有可能被优化时，会自动将它的隔离级别提升至 RR（可重复读）的级别，将 binlog 落成 Statement 格式，以达到缩短大事务备库执行的时间。 其中：
- cdb_optimize_large_trans_binlog 为该功能的开关。
- cdb_sql_statistics 为 SQL 运行情况进行统计的开关。
- cdb_optimize_large_trans_binlog_last_affected_rows_threshold 和 cdb_optimize_large_trans_binlog_aver_affected_rows_threshold 共同组成了大事务的阈值条件。
- cdb_sql_statistics_info_threshold 为内存中保持中的历史统计数据条数。

为了更好的监控事务运行情况，还增加了 information_schema 库下的表 CDB_SQL_STATISTICS 用于查询当前事务的统计情况。

#### 新增参数

| 名称                                                         | 状态 | 类型      | 默认 | 说明                                      |
| :----------------------------------------------------------- | :------ | :-------- | :------ | :----------------------------------------------- |
| cdb_optimize_large_trans_binlog                              | true    | bool      | false   | binlog 大事务优化的开关                           |
| cdb_optimize_large_trans_binlog_last_affected_rows_threshold | true    | ulonglong | 10000   | 大事务优化的条件：上次影响行数的阈值              |
| cdb_optimize_large_trans_binlog_aver_affected_rows_threshold | true    | ulonglong | 10000   | 大事务优化的条件：平均影响行数的阈值              |
| cdb_sql_statistics                                           | true    | bool      | false   | 是否开始对 SQL 运行情况进行统计的开关            |
| cdb_sql_statistics_info_threshold                            | true    | ulonglong | 10000   | CDB_SQL_STATISTICS 的 map 里保存最多的统计的 SQL 个数 |

#### 新增 information_schema.CDB_SQL_STATISTICS 表

| 名称                           | 类型                | 说明                                             |
| :----------------------------- | :------------------ | :------------------------------------------------------ |
| DIGEST_MD5                     | MYSQL_TYPE_STRING   | 该条 SQL 的 digest 换算出来的 MD5                            |
| DIGEST_TEXT                    | MYSQL_TYPE_STRING   | SQL 的 digest 文本格式                                   |
| SQL_COMMAND                    | MYSQL_TYPE_STRING   | SQL 命令的类型                                           |
| FIRST_UPDATE_TIMESTAMP         | MYSQL_TYPE_DATETIME | 该条统计信息第一次产生的时间                            |
| LAST_UPDATE_TIMESTAMP          | MYSQL_TYPE_DATETIME | 该条统计息上一次更新的时间                              |
| LAST_ACCESS_TIMESTAMP          | MYSQL_TYPE_DATETIME | 该条统计信息上一次被访问的时间                          |
| EXECUTE_COUNT                  | MYSQL_TYPE_LONGLONG | 这类 SQL 被执行次数                                       |
| TOTAL_AFFECTED_ROWS            | MYSQL_TYPE_LONGLONG | 总影响的行数                                            |
| AVER_AFFECTED_ROWS             | MYSQL_TYPE_LONGLONG | 平均影响的行数                                          |
| LAST_AFFECTED_ROWS             | MYSQL_TYPE_LONGLONG | 上次影响的行数                                          |
| STMT_BINLOG_FORMAT_IF_POSSIBLE | MYSQL_TYPE_STRING   | 这类 SQL 是否可以落成 statement 格式的 binlog，TRUE 或者 FALSE |

