Tencent Cloud Cloud Monitor provides the following monitoring metrics for Cloud Database instance (MySQL):

| Metric Name | Description | Unit | Dimension |
|---------|---------|---------|---------|
| Slow Queries | slow_queries | Counts per second | uInstanceId |
| scan | select_scan | Counts per second | uInstanceId |
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
| Key Cache Hit Rate | key_cache_hit_rate | % | uInstanceId |
| Key Cache Use Rate | key_cache_use_rate | % | uInstanceId |

For more information about the monitoring metrics of Cloud Database, please see [Read Monitoring Data API](https://www.qcloud.com/doc/api/405/4667) in the Cloud Monitor API.

