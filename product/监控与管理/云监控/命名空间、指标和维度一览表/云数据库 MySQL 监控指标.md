腾讯云云监控为云数据库实例（MySQL）提供以下监控指标：

| 指标中文名 | 指标英文名 | 单位 |维度|
|---------|---------|---------|---------|
|慢查询数|slow_queries|次/秒|uInstanceId|
|全表扫描数|select_scan|次/秒|uInstanceId|
|查询数|select_count|次/秒|uInstanceId|
|更新数|com_update|次/秒|uInstanceId|
|删除数|com_delete|次/秒|uInstanceId|
|插入数|com_insert|次/秒|uInstanceId|
|覆盖数|com_replace|次/秒|uInstanceId|
|总请求数|queries|次/秒|uInstanceId|
|当前连接数|threads_connected|个|uInstanceId|
|查询使用率|query_rate|%|uInstanceId|
|磁盘使用空间|real_capacity|MB|uInstanceId|
|磁盘占用空间|capacity|MB|uInstanceId|
|发送数据量|bytes_sent|MB/秒|uInstanceId|
|接收数据量|bytes_received|MB/秒|uInstanceId|
|容量使用率|volume_rate|%|uInstanceId|
|缓存命中率|qcache_hit_rate|%|uInstanceId|
|缓存使用率|qcache_use_rate|%|uInstanceId|
|等待表锁次数|table_locks_waited|次/秒|uInstanceId|
|临时表数量|created_tmp_tables|次/秒|uInstanceId|
|innodb缓存命中率|innodb_cache_hit_rate|%|uInstanceId|
|innodb缓存使用率|innodb_cache_use_rate|%|uInstanceId|
|innodb读磁盘数量|innodb_os_file_reads|次/秒|uInstanceId|
|innodb写磁盘数量|innodb_os_file_writes|次/秒|uInstanceId|
|innodb fsync数量|innodb_os_fsyncs|次/秒|uInstanceId|
|myisam缓存命中率|key_cache_hit_rate|%|uInstanceId|
|myisam缓存使用率|key_cache_use_rate|%|uInstanceId|

有关更多如何使用云数据库监控指标的内容，可以查看云监控 API 中的[读取监控数据接口](https://www.qcloud.com/doc/api/405/4667)。
