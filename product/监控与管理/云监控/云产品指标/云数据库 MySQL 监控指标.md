腾讯云云监控为云数据库实例（MySQL）提供以下监控指标：

|       指标英文名                 |                     指标中文名           | 单位                                | 维度        |
| -------------------------------- | ---------------------------------------- | ----------------------------------- | ----------- |
| cpu_user_ate                     | CPU 利用率                                | %                                   | uInstanceId |
| memory_use_rate                  | 内存利用率                               | %                                   | uInstanceId |
| memory_use                       | 内存占用                                 | MB                                  | uInstanceId |
| volume_rate                      | 磁盘使用率                               | %                                   | uInstanceId |
| real_capacity                    | 磁盘使用空间（仅包含数据空间使用量）     | MB                                  | uInstanceId |
| capacity                         | 磁盘占用空间（包含数据及日志空间使用量） | MB                                  | uInstanceId |
| bytes_sent                       | 内网出流量                               | Byte/秒                             | uInstanceId |
| bytes_received                   | 内网入流量                               | Byte/秒                             | uInstanceId |
| qps                              | 每秒执行操作数                           | 次/秒                               | uInstanceId |
| tps                              | 每秒执行事务数                           | 次/秒                               | uInstanceId |
| max_connections                  | 最大连接数                               | 个                                  | uInstanceId |
| threads_connected                | 当前打开连接数                           | 个                                  | uInstanceId |
| connection_use_rate              | 连接数利用率                             | %                                   | uInstanceId |
| slow_queries                     | 慢查询数                                 | 次/分                               | uInstanceId |
| select_scan                      | 全表扫描数                               | 次/秒                               | uInstanceId |
| select_count                     | 查询数                                   | 次/秒                               | uInstanceId |
| com_update                       | 更新数                                   | 次/秒                               | uInstanceId |
| com_delete                       | 删除数                                   | 次/秒                               | uInstanceId |
| com_insert                       | 插入数                                   | 次/秒                               | uInstanceId |
| com_replace                      | 覆盖数                                   | 次/秒                               | uInstanceId |
| queries                          | 总请求数                                 | 次/秒                               | uInstanceId |
| query_rate                       | 查询使用率                               | %                                   | uInstanceId |
| created_tmp_tables               | 临时表数量                               | 次/秒                               | uInstanceId |
| table_locks_waited               | 等待表锁次数                             | 次/秒                               | uInstanceId |
| innodb_cache_use_rate            | innodb 缓存使用率                         | %                                   | uInstanceId |
| innodb_cache_hit_rate            | innodb 缓存命中率                         | %                                   | uInstanceId |
| innodb_os_file_reads             | innodb 读磁盘数量                         | 次/秒                               | uInstanceId |
| innodb_os_file_writes            | innodb 写磁盘数量                         | 次/秒                               | uInstanceId |
| innodb_os_fsyncs                 | innodb fsync 数量                         | 次/秒                               | uInstanceId |
| innodb_num_open_files            | 当前 InnoDB 打开表的数量                   | 个                                  | uInstanceId |
| key_cache_use_rate               | myisam 缓存使用率                         | %                                   | uInstanceId |
| key_cache_hit_rate               | myisam 缓存命中率                         | %                                   | uInstanceId |
| com_commit                       | 提交数                                   | 次/秒                               | uInstanceId |
| com_rollback                     | 回滚数                                   | 次/秒                               | uInstanceId |
| threads_created                  | 已创建的线程数                           | 个                                  | uInstanceId |
| threads_running                  | 运行的线程数                             | 个                                  | uInstanceId |
| created_tmp_disk_tables          | 磁盘临时表数量                           | 次/秒                               | uInstanceId |
| created_tmp_files                | 临时文件数量                             | 次/秒                               | uInstanceId |
| handler_read_rnd_next            | 读下一行请求数                           | 次/秒                               | uInstanceId |
| handler_rollback                 | 内部回滚数                               | 次/秒                               | uInstanceId |
| handler_commit                   | 内部提交数                               | 次/秒                               | uInstanceId |
| innodb_buffer_pool_pages_free    | InnoDB 空页数                             | 个                                  | uInstanceId |
| innodb_buffer_pool_pages_total   | InnoDB 总页数                             | 个                                  | uInstanceId |
| innodb_buffer_pool_read_requests | InnoDB 逻辑读                             | 次/秒                               | uInstanceId |
| innodb_buffer_pool_reads         | InnoDB 物理读                             | 次/秒                               | uInstanceId |
| innodb_data_reads                | InnoDB 总读取量                           | 次/秒                               | uInstanceId |
| innodb_data_read                 | InnoDB 读取量                             | Byte/秒                             | uInstanceId |
| innodb_data_writes               | InnoDB 总写入量                           | 次/秒                               | uInstanceId |
| innodb_data_written              | InnoDB 写入量                             | Byte/秒                             | uInstanceId |
| innodb_rows_deleted              | InnoDB 行删除量                           | 次/秒                               | uInstanceId |
| innodb_rowsinserted              | InnoDB 行插入量                           | 次/秒                               | uInstanceId |
| innodb_rows_updated              | InnoDB 行更新量                           | 次/秒                               | uInstanceId |
| innodb_rows_read                 | InnoDB 行读取量                           | 次/秒                               | uInstanceId |
| innodb_row_lock_time_avg         | InnoDB 平均获取行锁时间                   | 毫秒                                | uInstanceId |
| innodb_row_lock_waits            | InnoDB 等待行锁次数                       | 次/秒                               | uInstanceId |
| key_blocks_unused                | 键缓存内未使用的块数量                   | 个                                  | uInstanceId |
| key_blocks_used                  | 键缓存内使用的块数量                     | 个                                  | uInstanceId |
| key_read_requests                | 键缓存读取数据块次数                     | 次/秒                               | uInstanceId |
| key_reads                        | 硬盘读取数据块次数                       | 次/秒                               | uInstanceId |
| key_write_requests               | 数据块写入键缓冲次数                     | 次/秒                               | uInstanceId |
| key_writes                       | 数据块写入磁盘次数                       | 次/秒                               | uInstanceId |
| opened_tables                    | 已经打开的表数                           | 个                                  | uInstanceId |
| table_locksimmediate             | 立即释放的表锁数                         | 个                                  | uInstanceId |
| open_files                       | 打开文件总数                             | 个                                  | uInstanceId |
| log_capacity                     | 日志使用量                               | MB                                  | uInstanceId |
| slaveio_running                  | IO 线程状态                               | 状态值（0-Yes，1-No，2-Connecting） | uInstanceId |
| slavesql_running                 | SQL 线程状态                              | 状态值（0-Yes，1-No）               | uInstanceId |
| master_slavesync_distance        | 主从延迟距离                             | MB                                  | uInstanceId |
| seconds_behind_master            | 主从延迟时间                             | 秒                                  | uInstanceId |

有关更多如何使用云数据库监控指标的内容，可以查看云监控 API 中的 [云数据库 MySQL 监控接口](https://cloud.tencent.com/document/api/248/11006)。
