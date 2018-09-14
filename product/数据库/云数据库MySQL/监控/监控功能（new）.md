## 性能监控
为方便用户查看和掌握实例的运行信息，云数据库 MySQL 提供了丰富的性能监控项与便捷的监控功能（自定义视图、时间对比、合并监控项等）。用户可登录[腾讯云控制台][1]，单击导航条【关系型数据库】，进入[云数据库控制台][2]，【管理】-【实例监控】查看。

同时，可以在云监控中[MySQL监控数据接口](https://cloud.tencent.com/document/api/248/11006)通过云API来获取CDB实例的监控指标。

<span  id = "jiankonglidu"></span>
## 监控粒度
自2018年08月11起，云数据库 MySQL 监控粒度实行自适应策略，暂不支持监控粒度的自定义选择。届时，云数据库 MySQL 的实例同时支持 5 秒粒度监控，敬请体验。此阶段 5 秒监控免费使用，具体收费时间另行通知。以下为监控粒度自适应策略：

| 时间跨度 | 监控粒度 | 说明 |
|:-------|:--------|:----|
| (0, 4h] | 5s | 时间跨度在4小时内，监控粒度为5秒 |
| (4h, 2d] | 1min | 时间跨度超过4小时，但在2天内，监控粒度调整为1分钟 |
| (2d, 10d] | 5min | 时间跨度超过2天，但在10天内，监控粒度调整为5分钟 |
| (10d, 30d] | 1h | 时间跨度超过10天，但在30天内，监控粒度调整为1小时 |

> **注意**
> 
> 目前云数据库 MySQL 最长支持查看30天内的监控数据

## 支持监控的实例类型

腾讯云 MySQL 支持云数据库主实例、只读实例和灾备实例的监控，并为每个实例提供独立的监控视图供查询。

## 监控指标

腾讯云云监控为云数据库实例（MySQL）提供以下监控指标：

| 指标中文名 | 指标英文名 | 单位 |维度|指标说明|
|---------|---------|---------|---------|
|每秒执行操作数|qps|次/秒|实例维度|数据库每秒执行的SQL数（含insert、select、update、delete、replace），QPS指标主要体现CDB实例的实际处理能力|
|慢查询数|slow_queries|次/分|实例维度|查询时间超过long_query_time秒的查询的个数|
|全表扫描数|select_scan|次/秒|实例维度|执行全表搜索查询的数量|
|查询数|select_count|次/秒|实例维度|每秒查询数|
|更新数|com_update|次/秒|实例维度|每秒更新数|
|删除数|com_delete|次/秒|实例维度|每秒删除数|
|插入数|com_insert|次/秒|实例维度|每秒插入数|
|覆盖数|com_replace|次/秒|实例维度|每秒覆盖数|
|总请求数|queries|次/秒|实例维度|所有执行的SQL语句，包括set，show等|
|当前打开连接数|threads_connected|个|实例维度|当前打开的连接的数量|
|查询使用率|query_rate|%|实例维度|每秒执行操作数QPS/推荐每秒操作数|
|磁盘使用空间|real_capacity|MB|实例维度|仅包括MySQL数据目录，不含binlog、relaylog、undolog、errorlog、slowlog日志空间|
|磁盘占用空间|capacity|MB|实例维度|包括MySQL数据目录和binlog、relaylog、undolog、errorlog、slowlog日志空间|
|发送数据量|bytes_sent|MB/秒|实例维度|每秒发送的字节数|
|接收数据量|bytes_received|MB/秒|实例维度|每秒接受的字节数|
|容量使用率|volume_rate|%|实例维度|磁盘使用空间/实例购买空间|
|查询缓存命中率|qcache_hit_rate|%|实例维度|查询缓存命中率|
|查询缓存使用率|qcache_use_rate|%|实例维度|查询缓存使用率|
|等待表锁次数|table_locks_waited|次/秒|实例维度|不能立即获得的表的锁的次数|
|临时表数量|created_tmp_tables|次/秒|实例维度|创建临时表的数量|
|innodb缓存命中率|innodb_cache_hit_rate|%|实例维度|Innodb引擎的缓存命中率|
|innodb缓存使用率|innodb_cache_use_rate|%|实例维度|Innodb引擎的缓存使用率|
|innodb读磁盘数量|innodb_os_file_reads|次/秒|实例维度|Innodb引擎每秒读磁盘文件的次数|
|innodb写磁盘数量|innodb_os_file_writes|次/秒|实例维度|Innodb引擎每秒写磁盘文件的次数|
|innodb fsync数量|innodb_os_fsyncs|次/秒|实例维度|Innodb引擎每秒调用fsync函数次数|
|myisam缓存命中率|key_cache_hit_rate|%|实例维度|myisam引擎的缓存命中率|
|myisam缓存使用率|key_cache_use_rate|%|实例维度|myisam引擎的缓存使用率|
|CPU占比|cpu_use_rate|%|实例维度|允许宿主机闲时超用，可能大于100%|
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
|InnoDB空页数|innodb_buffer_pool_pages_free|个|实例维度|Innodb引擎内存空页个数|
|InnoDB总页数|innodb_buffer_pool_pages_total|个|实例维度|Innodb引擎占用内存总页数|
|InnoDB逻辑读|innodb_buffer_pool_read_requests|次/秒|实例维度|Innodb引擎每秒已经完成的逻辑读请求次数|
|InnoDB物理读|innodb_buffer_pool_reads|次/秒|实例维度|Innodb引擎每秒已经完成的物理读请求次数|
|InnoDB读取量|innodb_data_read|Byte/秒|实例维度|Innodb引擎每秒已经完成读取数据的字节数|
|InnoDB总读取量|innodb_data_reads|次/秒|实例维度|Innodb引擎每秒已经完成读取数据的次数|
|InnoDB总写入量|innodb_data_writes|次/秒|实例维度|Innodb引擎每秒已经完成写数据的次数|
|InnoDB写入量|innodb_data_written|Byte/秒|实例维度|Innodb引擎每秒已经完成写数据的字节数|
|InnoDB行删除量|innodb_rows_deleted|次/秒|实例维度|Innodb引擎每秒删除的行数|
|InnoDB行插入量|innodb_rows_inserted|次/秒|实例维度|Innodb引擎每秒插入的行数|
|InnoDB行更新量|innodb_rows_updated|次/秒|实例维度|Innodb引擎每秒更新的行数|
|InnoDB行读取量|innodb_rows_read|次/秒|实例维度|Innodb引擎每秒读取的行数|
|InnoDB平均获取行锁时间|innodb_row_lock_time_avg|毫秒|实例维度|Innodb引擎行锁定的平均时长|
|InnoDB等待行锁次数|innodb_row_lock_waits|次/秒|实例维度|Innodb引擎每秒等待行锁定的次数|
|键缓存内未使用的块数量|key_blocks_unused|个|实例维度|myisam引擎未使用键缓存块的个数|
|键缓存内使用的块数量|key_blocks_used|个|实例维度|myisam引擎已使用键缓存块的个数|
|键缓存读取数据块次数|key_read_requests|次/秒|实例维度|myisam引擎每秒读取键缓存块的次数|
|硬盘读取数据块次数|key_reads|次/秒|实例维度|myisam引擎每秒读取硬盘数据块的次数|
|数据块写入键缓冲次数|key_write_requests|次/秒|实例维度|myisam引擎每秒写键缓存块的次数|
|数据块写入磁盘次数|key_writes|次/秒|实例维度|myisam引擎每秒写硬盘数据块的次数|
|主从不同步距离|master_slave_sync_distance|MB|实例维度|主从binlog差距|


有关更多如何使用云数据库监控指标的内容，可以查看云监控 API 中的[读取监控数据接口](https://cloud.tencent.com/document/api/248/11006)。

> 更多监控指标，敬请期待。

[1]:	https://console.cloud.tencent.com/
[2]:	https://console.cloud.tencent.com/cdb/ "云数据库控制台"

