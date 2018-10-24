 Cloud Monitor of Tencent Cloud provides the following monitoring metrics for Cloud Database instance (MySQL):

| Metric Name | Description | Unit | Dimension |
|---------|---------|---------|---------|
| Slow Queries | slow_queries | Counts per second | uInstanceId |
| Table Scan | select_scan | Counts per second | uInstanceId |
| Queries | select_count | Counts per second | uInstanceId |
| Updates | com_update | Counts per second | uInstanceId |
| Deletions | com_delete | Counts per second | uInstanceId |
| Insertions | com_insert | Counts per second | uInstanceId |
| Replacements | com_replace | Counts per second | uInstanceId |
| Total Requests | queries | Counts per second | uInstanceId |
| Connections | threads_connected | Count | uInstanceId |
| Query Usage | query_rate | % | uInstanceId |
| Used Capacity | real_capacity | MB | uInstanceId |
| Occupied Capacity | capacity | MB | uInstanceId |
| Sent Volume | bytes_sent | MB/s | uInstanceId |
| Received Volume | bytes_received | MB/s | uInstanceId |
| Volume Usage | volume_rate | % | uInstanceId |
| Cache Hit Rate | qcache_hit_rate | % | uInstanceId |
| Cache Use Rate | qcache_use_rate | % | uInstanceId |
| Waited Table Locks | table_locks_waited | Counts per second | uInstanceId |
| Creating Temp Table Rate| created_tmp_tables | Counts per second | uInstanceId |
| Innodb Cache Hit Rate | innodb_cache_hit_rate | % | uInstanceId |
| innodb Cache Use Rate | innodb_cache_use_rate | % | uInstanceId |
| Read Innodb File | innodb_os_file_reads | Counts per second | uInstanceId |
| Write Innodb File | innodb_os_file_writes | Counts per second | uInstanceId |
| Innodb Fsyncs Number | innodb_os_fsyncs | Counts per second | uInstanceId |
|myisam Cache Hit Rate|key_cache_hit_rate|%|uInstanceId|
|Myisam Memory Use Rate |key_cache_use_rate|%|uInstanceId|
|CPU Use Rate|cpu_use_rate|%|uInstanceId|
|Memory Used|memory_use|MB|uInstanceId|
|Temp File Number|created_tmp_files|count/s|uInstanceId|
|Memory Temp Table Number|created_tmp_tables|count/s|uInstanceId|
|Opend Tables|opened_tables|count|uInstanceId|
|Waited Table Locks |table_locks_waited|count/s|uInstanceId|
|Commit Numbers|com_commit|count/s|uInstanceId|
|Rollback Numbers|com_rollback|count/s|uInstanceId|
|Created threads|threads_created|count|uInstanceId|
|Running Threads|threads_running|count|uInstanceId|
|Maximum Connections|max_connections|count|uInstanceId|
|Disk Temp Tables |created_tmp_disk_tables|count/s|uInstanceId|
|Read Next Line Queries|handler_read_rnd_next|count/s|uInstanceId|
|Internal Rollback|handler_rollback|count/s|uInstanceId|
|Internal Commits|handler_commit|count/s|uInstanceId|
|InnoDB Free Pages|innodb_buffer_pool_pages_free|count|uInstanceId|
|InnoDB Free Pages|innodb_buffer_pool_pages_total|count|uInstanceId|
|InnoDB Logic Read Requests|innodb_buffer_pool_reads|count/s|uInstanceId|
|InnoDB Physical Reads|innodb_buffer_pool_reads|count/s|uInstanceId|
|InnoDB Reads|innodb_data_read|Byte/s|uInstanceId|
|InnoDB Total Reads|innodb_data_reads|count/s|uInstanceId|
|InnoDB Total Writes|innodb_data_writes|count/s|uInstanceId|
|InnoDB Writes|innodb_data_written|Byte/s|uInstanceId|
|InnoDB Rows Deleted|innodb_rows_deleted|count/s|uInstanceId| 
|InnoDB Rows Inserted|innodb_rows_inserted|count/s|uInstanceId|
|InnoDB Rows Updates|innodb_rows_updated|count/s|uInstanceId|
|InnoDB Rows Reads|innodb_rows_read|count/s|uInstanceId|
|InnoDB Average Row Lock Time|innodb_row_lock_time_avg|ms|uInstanceId|
|InnoDB Waited Row Locks|innodb_row_lock_waits|count/s|uInstanceId|
|Key Memory Unused Blocks|key_blocks_unused|count|uInstanceId|
|Key Memory Used Locks|key_blocks_used|count|uInstanceId|
|Key Memory Read Data Requests|key_read_requests|count/s|uInstanceId|
|Disk Read Data Blocks|key_reads|count/s|uInstanceId|
|Data Block Write Key Buffers|key_write_requests|count/s|uInstanceId|
|Data Block Writes|key_writes|count/s|uInstanceId|
 
For more information about the monitoring metrics of Cloud Database, please see [Read Monitoring Data API](https://cloud.tencent.com/doc/api/405/4667) in the Cloud Monitor API.

