## 性能监控
为方便用户查看和掌握实例的运行信息，云数据库 MySQL 提供了丰富的性能监控项，用户可登录 [腾讯云控制台][1]，单击导航条【关系型数据库】，进入[云数据库控制台][2]，【管理】>【实例监控】查看。

## 支持监控的实例类型

腾讯云 MySQL 支持云数据库主实例及只读实例的监控，并为每个实例提供独立的监控视图供查询。

## 监控指标

腾讯云云监控为云数据库实例（MySQL）提供以下监控指标：

| 指标中文名 | 指标英文名 | 单位 |维度|指标说明|
|---------|---------|---------|---------|
|每秒执行操作数|QPS|次/秒|实例维度|数据库每秒执行的 SQL 数（含 insert、select、update、delete、replace），QPS 指标主要体现 CDB 实例的实际处理能力|
|慢查询数|slow_queries|次/秒|实例维度|[查看 MySQL 官方指导][3]|
|全表扫描数|select_scan|次/秒|实例维度|[查看 MySQL 官方指导][3]|
|查询数|select_count|次/秒|实例维度|Com_select 值|
|更新数|com_update|次/秒|实例维度|[查看 MySQL 官方指导][3]|
|删除数|com_delete|次/秒|实例维度|[查看 MySQL 官方指导][3]|
|插入数|com_insert|次/秒|实例维度|[查看 MySQL 官方指导][3]|
|覆盖数|com_replace|次/秒|实例维度|[查看 MySQL 官方指导][3]|
|总请求数|queries|次/秒|实例维度|所有执行的 SQL 语句，包括 set，show 等|
|当前打开连接数|threads_connected|个|实例维度|[查看 MySQL 官方指导][3]|
|查询使用率|query_rate|%|实例维度|每秒执行操作数 QPS / 推荐每秒操作数|
|磁盘使用空间|real_capacity|MB|实例维度|仅包括 MySQL 数据目录，不含 binlog、relaylog、undolog、errorlog、slowlog 日志空间|
|磁盘占用空间|capacity|MB|实例维度|包括 MySQL 数据目录和 binlog、relaylog、undolog、errorlog、slowlog 日志空间|
|发送数据量|bytes_sent|MB/秒|实例维度|[查看 MySQL 官方指导][3]|
|接收数据量|bytes_received|MB/秒|实例维度|[查看 MySQL 官方指导][3]|
|容量使用率|volume_rate|%|实例维度|磁盘使用空间/实例购买空间|
|查询缓存命中率|qcache_hit_rate|%|实例维度|[查看 MySQL 官方指导][3]|
|查询缓存使用率|qcache_use_rate|%|实例维度|[查看 MySQL 官方指导][3]|
|等待表锁次数|table_locks_waited|次/秒|实例维度|[查看 MySQL 官方指导][3]|
|临时表数量|created_tmp_tables|次/秒|实例维度|[查看 MySQL 官方指导][3]|
|innodb 缓存命中率|innodb_cache_hit_rate|%|实例维度|[查看 MySQL 官方指导][3]|
|innodb 缓存使用率|innodb_cache_use_rate|%|实例维度|[查看 MySQL 官方指导][3]|
|innodb 读磁盘数量|innodb_os_file_reads|次/秒|实例维度|[查看 MySQL 官方指导][3]|
|innodb 写磁盘数量|innodb_os_file_writes|次/秒|实例维度|[查看 MySQL 官方指导][3]|
|innodb fsync 数量|innodb_os_fsyncs|次/秒|实例维度|[查看 MySQL 官方指导][3]|
|myisam 缓存命中率|key_cache_hit_rate|%|实例维度|[查看 MySQL 官方指导][3]|
|myisam 缓存使用率|key_cache_use_rate|%|实例维度|[查看 MySQL 官方指导][3]|
|CPU 占比|cpu_use_rate|%|实例维度|允许宿主机闲时超用，可能大于 100%|
|内存占用|memory_use|MB|实例维度|允许宿主机闲时超用，可能大于购买容量|
|临时文件数量|created_tmp_files|次/秒|实例维度|[查看 MySQL 官方指导][3]|
|内存临时表数量|created_tmp_tables|次/秒|实例维度|[查看 MySQL 官方指导][3]|
|已经打开的表数|opened_tables|个|实例维度|[查看 MySQL 官方指导][3]|
|需要等待的表锁数|table_locks_waited|次/秒|实例维度|[查看 MySQL 官方指导][3]|
|提交数|com_commit|次/秒|实例维度|[查看 MySQL 官方指导][3]|
|回滚数|com_rollback|次/秒|实例维度|[查看 MySQL 官方指导][3]|
|已创建的线程数|threads_created|个|实例维度|[查看 MySQL 官方指导][3]|
|运行的线程数|threads_running|个|实例维度|[查看 MySQL 官方指导][3]|
|最大连接数|max_connections|个|实例维度|[查看 MySQL 官方指导][3]|
|磁盘临时表数量|created_tmp_disk_tables|次/秒|实例维度|[查看 MySQL 官方指导][3]|
|读下一行请求数|handler_read_rnd_next|次/秒|实例维度|[查看 MySQL 官方指导][3]|
|内部回滚数|handler_rollback|次/秒|实例维度|[查看 MySQL 官方指导][3]|
|内部提交数|handler_commit|次/秒|实例维度|[查看 MySQL 官方指导][3]|
|InnoDB 空页数|innodb_buffer_pool_pages_free|个|实例维度|[查看 MySQL 官方指导][3]|
|InnoDB 空页数|innodb_buffer_pool_pages_total|个|实例维度|[查看 MySQL 官方指导][3]|
|InnoDB 逻辑读|innodb_buffer_pool_read_requests|次/秒|实例维度|[查看 MySQL 官方指导][3]|
|InnoDB 物理读|innodb_buffer_pool_reads|次/秒|实例维度|[查看 MySQL 官方指导][3]|
|InnoDB 读取量|innodb_data_read|Byte/秒|实例维度|[查看 MySQL 官方指导][3]|
|InnoDB 总读取量|innodb_data_reads|次/秒|实例维度|[查看 MySQL 官方指导][3]|
|InnoDB 总写入量|innodb_data_writes|次/秒|实例维度|[查看 MySQL 官方指导][3]|
|InnoDB 写入量|innodb_data_written|Byte/秒|实例维度|[查看 MySQL 官方指导][3]|
|InnoDB 行删除量|innodb_rows_deleted|次/秒|实例维度| [查看 MySQL 官方指导][3]|
|InnoDB 行插入量|innodb_rows_inserted|次/秒|实例维度|[查看 MySQL 官方指导][3]|
|InnoDB 行更新量|innodb_rows_updated|次/秒|实例维度|[查看 MySQL 官方指导][3]|
|InnoDB 行读取量|innodb_rows_read|次/秒|实例维度|[查看 MySQL 官方指导][3]|
|InnoDB 平均获取行锁时间|innodb_row_lock_time_avg|毫秒|实例维度|[查看 MySQL 官方指导][3]|
|InnoDB 等待行锁次数|innodb_row_lock_waits|次/秒|实例维度|[查看 MySQL 官方指导][3]|
|键缓存内未使用的块数量|key_blocks_unused|个|实例维度|[查看 MySQL 官方指导][3]|
|键缓存内使用的块数量|key_blocks_used|个|实例维度|[查看 MySQL 官方指导][3]|
|键缓存读取数据块次数|key_read_requests|次/秒|实例维度|[查看 MySQL 官方指导][3]|
|硬盘读取数据块次数|key_reads|次/秒|实例维度|[查看 MySQL 官方指导][3]|
|数据块写入键缓冲次数|key_write_requests|次/秒|实例维度|[查看 MySQL 官方指导][3]|
|数据块写入磁盘次数|key_writes|次/秒|实例维度|[查看 MySQL 官方指导][3]|
|打开文件总数|open_files|个|实例维度|[查看 MySQL 官方指导][3]|
|日志使用量|log_capacity|MB|实例维度|[查看 MySQL 官方指导][3]|
|主从不同步距离|master_slave_sync_distance|MB|实例维度|主从 binlog 差距|
|Slave 下 IO 线程状态|slave_io_running|0-Yes，1-No，2-Connecting|实例维度|[查看 MySQL 官方指导][3]|
|Slave 下 SQL 线程状态|slave_sql_running|0-Yes，1-No|实例维度|[查看 MySQL 官方指导][3]|
|主从差距时间|seconds_behind_master|秒|实例维度|[查看 MySQL 官方指导][3]|


有关更多如何使用云数据库监控指标的内容，可以查看云监控 API 中的 [读取监控数据接口](https://cloud.tencent.com/doc/api/405/4667)。

**更多监控指标，敬请期待。**

[1]:	https://console.cloud.tencent.com/
[2]:	https://console.cloud.tencent.com/cdb/ "云数据库控制台"
[3]:	https://dev.mysql.com/doc/refman/5.6/en/ "查看 MySQL 官方指导"

