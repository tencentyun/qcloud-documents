腾讯云云监控为云数据库实例（MySQL）提供以下监控指标：

| 指标中文名              | 指标英文名                       | 单位                                | 维度        |
| ----------------------- | -------------------------------- | ----------------------------------- | ----------- |
| 慢查询数                | slow_queries                     | 次/分                               | uInstanceId |
| 全表扫描数              | select_scan                      | 次/秒                               | uInstanceId |
| 查询数                  | select_count                     | 次/秒                               | uInstanceId |
| 更新数                  | com_update                       | 次/秒                               | uInstanceId |
| 删除数                  | com_delete                       | 次/秒                               | uInstanceId |
| 插入数                  | com_insert                       | 次/秒                               | uInstanceId |
| 覆盖数                  | com_replace                      | 次/秒                               | uInstanceId |
| 总请求数                | queries                          | 次/秒                               | uInstanceId |
| 当前打开连接数          | threads_connected                | 个                                  | uInstanceId |
| 查询使用率              | query_rate                       | %                                   | uInstanceId |
| 磁盘使用空间            | real_capacity                    | MB                                  | uInstanceId |
| 磁盘占用空间            | capacity                         | MB                                  | uInstanceId |
| 发送数据量              | bytes_sent                       | MB/秒                               | uInstanceId |
| 接收数据量              | bytes_received                   | MB/秒                               | uInstanceId |
| 磁盘利用率              | volume_rate                      | %                                   | uInstanceId |
| 查询缓存命中率          | qcache_hit_rate                  | %                                   | uInstanceId |
| 查询缓存使用率          | qcache_use_rate                  | %                                   | uInstanceId |
| 等待表锁次数            | table_locks_waited               | 次/秒                               | uInstanceId |
| 临时表数量              | created_tmp_tables               | 次/秒                               | uInstanceId |
| innodb 缓存命中率       | innodb_cache_hit_rate            | %                                   | uInstanceId |
| innodb 缓存使用率       | innodb_cache_use_rate            | %                                   | uInstanceId |
| innodb 读磁盘数量       | innodb_os_file_reads             | 次/秒                               | uInstanceId |
| innodb 写磁盘数量       | innodb_os_file_writes            | 次/秒                               | uInstanceId |
| innodb fsync 数量       | innodb_os_fsyncs                 | 次/秒                               | uInstanceId |
| myisam 缓存命中率       | key_cache_hit_rate               | %                                   | uInstanceId |
| myisam 缓存使用率       | key_cache_use_rate               | %                                   | uInstanceId |
| CPU 利用率              | cpu_use_rate                     | %                                   | uInstanceId |
| 内存利用率              | memory use rate                  | %                                   | uInstanceId |
| 内存占用                | memory_use                       | MB                                  | uInstanceId |
| 临时文件数量            | created_tmp_files                | 次/秒                               | uInstanceId |
| 内存临时表数量          | created_tmp_tables               | 次/秒                               | uInstanceId |
| 已经打开的表数          | opened_tables                    | 个                                  | uInstanceId |
| 需要等待的表锁数        | table_locks_waited               | 次/秒                               | uInstanceId |
| 提交数                  | com_commit                       | 次/秒                               | uInstanceId |
| 回滚数                  | com_rollback                     | 次/秒                               | uInstanceId |
| 已创建的线程数          | threads_created                  | 个                                  | uInstanceId |
| 运行的线程数            | threads_running                  | 个                                  | uInstanceId |
| 最大连接数              | max_connections                  | 个                                  | uInstanceId |
| 磁盘临时表数量          | created_tmp_disk_tables          | 次/秒                               | uInstanceId |
| 读下一行请求数          | handler_read_rnd_next            | 次/秒                               | uInstanceId |
| 内部回滚数              | handler_rollback                 | 次/秒                               | uInstanceId |
| 内部提交数              | handler_commit                   | 次/秒                               | uInstanceId |
| InnoDB 空页数           | innodb_buffer_pool_pages_free    | 个                                  | uInstanceId |
| InnoDB 空页数           | innodb_buffer_pool_pages_total   | 个                                  | uInstanceId |
| InnoDB 逻辑读           | innodb_buffer_pool_read_requests | 次/秒                               | uInstanceId |
| InnoDB 物理读           | innodb_buffer_pool_reads         | 次/秒                               | uInstanceId |
| InnoDB 读取量           | innodb_data_read                 | Byte/秒                             | uInstanceId |
| InnoDB 总读取量         | innodb_data_reads                | 次/秒                               | uInstanceId |
| InnoDB 总写入量         | innodb_data_writes               | 次/秒                               | uInstanceId |
| InnoDB 写入量           | innodb_data_written              | Byte/秒                             | uInstanceId |
| InnoDB 行删除量         | innodb_rows_deleted              | 次/秒                               | uInstanceId |
| InnoDB 行插入量         | innodb_rows_inserted             | 次/秒                               | uInstanceId |
| InnoDB 行更新量         | innodb_rows_updated              | 次/秒                               | uInstanceId |
| InnoDB 行读取量         | innodb_rows_read                 | 次/秒                               | uInstanceId |
| InnoDB 平均获取行锁时间 | innodb_row_lock_time_avg         | 毫秒                                | uInstanceId |
| InnoDB 等待行锁次数     | innodb_row_lock_waits            | 次/秒                               | uInstanceId |
| 键缓存内未使用的块数量  | key_blocks_unused                | 个                                  | uInstanceId |
| 键缓存内使用的块数量    | key_blocks_used                  | 个                                  | uInstanceId |
| 键缓存读取数据块次数    | key_read_requests                | 次/秒                               | uInstanceId |
| 硬盘读取数据块次数      | key_reads                        | 次/秒                               | uInstanceId |
| 数据块写入键缓冲次数    | key_write_requests               | 次/秒                               | uInstanceId |
| 数据块写入磁盘次数      | key_writes                       | 次/秒                               | uInstanceId |
| 主从延迟距离            | master_slave_sync_distance       | MB                                  | uInstanceId |
| 主从延迟时间            | seconds_behind_master            | 秒                                  | uInstanceId |
| IO 线程状态             | slave_io_running                 | 状态值（0-Yes，1-No，2-Connecting） | uInstanceId |
| SQL 线程状态            | slave_sql_running                | 状态值（0-Yes，1-No）               | uInstanceId |

有关更多如何使用云数据库监控指标的内容，可以查看云监控 API 中的 [读取监控数据接口](https://cloud.tencent.com/document/api/248/11006)。
