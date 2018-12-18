## 性能监控
为方便用户查看和掌握实例的运行信息，云数据库 MySQL 提供了丰富的性能监控项与便捷的监控功能（自定义视图、时间对比、合并监控项等）。用户可登录 [腾讯云控制台][1]，单击导航条【关系型数据库】，进入[云数据库控制台][2]，【管理】-【实例监控】查看。

同时，可以在云监控中 [MySQL监控数据接口](https://cloud.tencent.com/document/api/248/11006) 通过云 API 来获取 TencentDB 实例的监控指标。

<span  id = "jiankonglidu"></span>
## 监控粒度
自 2018 年 08 月 11 起，云数据库 MySQL 监控粒度实行自适应策略，暂不支持监控粒度的自定义选择。另外，云数据库 MySQL 的实例同时支持 5 秒粒度监控。此阶段 5 秒监控免费使用，具体收费时间另行通知。以下为监控粒度自适应策略：

| 时间跨度 | 监控粒度 | 自适应说明 | 保留时长 |
|:-------|:--------|:----|:-----|
| (0, 4h] | 5s | 时间跨度在 4 小时内，监控粒度为 5 秒 | 1天 |
| (4h, 2d] | 1min | 时间跨度超过 4 小时，但在 2 天内，监控粒度调整为 1 分钟 | 15天 |
| (2d, 10d] | 5min | 时间跨度超过 2 天，但在 10 天内，监控粒度调整为 5 分钟 | 31天 |
| (10d, 30d] | 1h | 时间跨度超过 10 天，但在 30 天内，监控粒度调整为 1 小时 | 62天 |

> **注意：**
> 目前云数据库 MySQL 最长支持查看 30 天内的监控数据。

## 支持监控的实例类型

腾讯云 MySQL 支持云数据库主实例、只读实例和灾备实例的监控，并为每个实例提供独立的监控视图供查询。

## 监控指标

腾讯云云监控为云数据库实例（MySQL）提供以下监控指标：

| 指标中文名 | 指标英文名 | 单位 |维度|指标说明|
|---------|---------|---------|---------|----|
|每秒执行操作数|qps|次/秒|实例维度|数据库每秒执行的 SQL 数（含 insert、select、update、delete、replace），QPS 指标主要体现 TencentDB 实例的实际处理能力|
|慢查询数|slow_queries|次|实例维度|查询时间超过 long_query_time 秒的查询的个数|
|全表扫描数|select_scan|次/秒|实例维度|执行全表搜索查询的数量|
|查询数|select_count|次/秒|实例维度|每秒查询数|
|更新数|com_update|次/秒|实例维度|每秒更新数|
|删除数|com_delete|次/秒|实例维度|每秒删除数|
|插入数|com_insert|次/秒|实例维度|每秒插入数|
|覆盖数|com_replace|次/秒|实例维度|每秒覆盖数|
|总请求数|queries|次/秒|实例维度|所有执行的 SQL 语句，包括 set，show 等|
|当前打开连接数|threads_connected|个|实例维度|当前打开的连接的数量|
|查询使用率|query_rate|%|实例维度|每秒执行操作数 QPS/推荐每秒操作数|
|磁盘使用空间|real_capacity|MB|实例维度|仅包括 MySQL 数据目录，不含 binlog、relaylog、undolog、errorlog、slowlog 日志空间|
|磁盘占用空间|capacity|MB|实例维度|包括 MySQL 数据目录和 binlog、relaylog、undolog、errorlog、slowlog 日志空间|
|发送数据量|bytes_sent|MB/秒|实例维度|每秒发送的字节数|
|接收数据量|bytes_received|MB/秒|实例维度|每秒接受的字节数|
|容量使用率|volume_rate|%|实例维度|磁盘使用空间/实例购买空间|
|查询缓存命中率|qcache_hit_rate|%|实例维度|查询缓存命中率|
|查询缓存使用率|qcache_use_rate|%|实例维度|查询缓存使用率|
|等待表锁次数|table_locks_waited|次/秒|实例维度|不能立即获得的表的锁的次数|
|临时表数量|created_tmp_tables|次/秒|实例维度|创建临时表的数量|
|innodb 缓存命中率|innodb_cache_hit_rate|%|实例维度|Innodb 引擎的缓存命中率|
|innodb 缓存使用率|innodb_cache_use_rate|%|实例维度|Innodb 引擎的缓存使用率|
|innodb 读磁盘数量|innodb_os_file_reads|次/秒|实例维度|Innodb 引擎每秒读磁盘文件的次数|
|innodb 写磁盘数量|innodb_os_file_writes|次/秒|实例维度|Innodb 引擎每秒写磁盘文件的次数|
|innodb fsync 数量|innodb_os_fsyncs|次/秒|实例维度|Innodb 引擎每秒调用 fsync 函数次数|
|myisam 缓存命中率|key_cache_hit_rate|%|实例维度|myisam 引擎的缓存命中率|
|myisam 缓存使用率|key_cache_use_rate|%|实例维度|myisam 引擎的缓存使用率|
|CPU 占比|cpu_use_rate|%|实例维度|允许宿主机闲时超用，可能大于 100%|
|内存占用|memory_use|MB|实例维度|允许宿主机闲时超用，可能大于购买容量|
|临时文件数量|created_tmp_files|次/秒|实例维度|每秒创建临时文件的次数|
|已经打开的表数|opened_tables|个|实例维度|已打开表的个数|
|提交数|com_commit|次/秒|实例维度|每秒提交次数|
|回滚数|com_rollback|次/秒|实例维度|每秒回滚次数|
|已创建的线程数|threads_created|个|实例维度|创建用来处理连接的线程数|
|运行的线程数|threads_running|个|实例维度|激活的（非睡眠状态）线程数|
|最大连接数|max_connections|个|实例维度|最大连接数|
|磁盘临时表数量|created_tmp_disk_tables|次/秒|实例维度|每秒创建磁盘临时表的次数|
|读下一行请求数|handler_read_rnd_next|次/秒|实例维度|每秒读取下一行的请求次数|
|内部回滚数|handler_rollback|次/秒|实例维度|每秒事务被回滚的次数|
|内部提交数|handler_commit|次/秒|实例维度|每秒事务提交的次数|
|InnoDB 空页数|innodb_buffer_pool_pages_free|个|实例维度|Innodb 引擎内存空页个数|
|InnoDB 总页数|innodb_buffer_pool_pages_total|个|实例维度|Innodb 引擎占用内存总页数|
|InnoDB 逻辑读|innodb_buffer_pool_read_requests|次/秒|实例维度|Innodb 引擎每秒已经完成的逻辑读请求次数|
|InnoDB 物理读|innodb_buffer_pool_reads|次/秒|实例维度|Innodb 引擎每秒已经完成的物理读请求次数|
|InnoDB 读取量|innodb_data_read|Byte/秒|实例维度|Innodb 引擎每秒已经完成读取数据的字节数|
|InnoDB 总读取量|innodb_data_reads|次/秒|实例维度|Innodb 引擎每秒已经完成读取数据的次数|
|InnoDB 总写入量|innodb_data_writes|次/秒|实例维度|Innodb 引擎每秒已经完成写数据的次数|
|InnoDB 写入量|innodb_data_written|Byte/秒|实例维度|Innodb 引擎每秒已经完成写数据的字节数|
|InnoDB 行删除量|innodb_rows_deleted|次/秒|实例维度|Innodb 引擎每秒删除的行数|
|InnoDB 行插入量|innodb_rows_inserted|次/秒|实例维度|Innodb 引擎每秒插入的行数|
|InnoDB 行更新量|innodb_rows_updated|次/秒|实例维度|Innodb 引擎每秒更新的行数|
|InnoDB 行读取量|innodb_rows_read|次/秒|实例维度|Innodb 引擎每秒读取的行数|
|InnoDB 平均获取行锁时间|innodb_row_lock_time_avg|毫秒|实例维度|Innodb 引擎行锁定的平均时长|
|InnoDB 等待行锁次数|innodb_row_lock_waits|次/秒|实例维度|Innodb 引擎每秒等待行锁定的次数|
|键缓存内未使用的块数量|key_blocks_unused|个|实例维度|myisam 引擎未使用键缓存块的个数|
|键缓存内使用的块数量|key_blocks_used|个|实例维度|myisam 引擎已使用键缓存块的个数|
|键缓存读取数据块次数|key_read_requests|次/秒|实例维度|myisam 引擎每秒读取键缓存块的次数|
|硬盘读取数据块次数|key_reads|次/秒|实例维度|myisam 引擎每秒读取硬盘数据块的次数|
|数据块写入键缓冲次数|key_write_requests|次/秒|实例维度|myisam 引擎每秒写键缓存块的次数|
|数据块写入磁盘次数|key_writes|次/秒|实例维度|myisam 引擎每秒写硬盘数据块的次数|
|主从不同步距离|master_slave_sync_distance|MB|实例维度|主从 binlog 差距|
|主从差距时间|	seconds_behind_master|	秒|	实例维度|	主从延迟时间|
|Slave 下 IO 线程状态|	slave_io_running|	状态值（0-Yes，1-No，2-Connecting）|	实例维度|	IO 线程运行状态|
|Slave 下 SQL 线程状态|	slave_sql_running|	状态值（0-Yes，1-No）|	实例维度|	SQL 线程运行状态|


有关更多如何使用云数据库监控指标的内容，可以查看云监控 API 中的 [云数据库 MySQL 接口](https://cloud.tencent.com/document/product/248/11006)。


[1]:	https://console.cloud.tencent.com/
[2]:	https://console.cloud.tencent.com/cdb/ "云数据库控制台"

