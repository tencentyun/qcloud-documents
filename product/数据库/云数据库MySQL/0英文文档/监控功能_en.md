## Performance Monitor
Cloud Database for MySQL provides various performance monitoring items to make it easy for users to view and obtain the operation information of instances. You can log in to [Tencent Cloud Console][1], click "Relational Database" in the navigation bar to enter [Cloud Database Console][2] to view these items through "Management" - "Instance Monitoring".

At the same time, the monitored metrics of CDB instances can be obtained at [MySQL Monitored Data Interface](https://cloud.tencent.com/document/api/248/11006) through cloud APIs.

## Instance Types That Can Be Monitored

Tencent Cloud's CDB for MySQL can monitor master instances and read-only instances, and provides an independent monitoring view for each instance for query.

## Monitoring Metrics

Tencent Cloud Monitor provides the following monitored metrics for CDB instances (MySQL):

| Metric | Code Name | Unit | Dimension | Description |
|---------|---------|---------|---------|
| Operations per Second | qps | Count/s | Instance Dimension | The number of SQLs executed by the database per second (including insert, select, update, delete and replace), and QPS metric mainly represents the actual processing capability of CDB instances |
| Number of Slow Queries | slow_queries | Count/Min | Instance Dimension | [View MySQL's Official Guide][3] |
| Number of Full Table Scans | select_scan | Count/s | Instance Dimension | [View MySQL's Official Guide][3] |
| Number of Queries | select_count | Count/s | Instance Dimension | Com_select value |
| Number of Updates | com_update | Count/s | Instance Dimension | [View MySQL's Official Guide][3] |
| Number of Deletions | com_delete | Count/s | Instance Dimension | [View MySQL's Official Guide][3] |
| Number of Insertions | com_insert | Count/s | Instance Dimension | [View MySQL's Official Guide][3] |
| Number of Overwrites | com_replace | Count/s | Instance Dimension | [View MySQL's Official Guide][3] |
| Total Number of Requests | queries | Count/s | Instance Dimension | All the executed SQL statements, including set, show, etc. |
| Number of Currently Opened Connections | threads_connected | Count | Instance Dimension | [View MySQL's Official Guide][3] |
| Query Rate | query_rate | % | Instance Dimension | Operations per second (QPS)/Operations per second are recommended |
| Real Disk Capacity | real_capacity | MB | Instance Dimension | Only include MySQL's data directory, rather than log space, such as binlog, relaylog, undolog, errorlog and slowlog. |
| Total Disk Capacity | capacity | MB | Instance Dimension | Include MySQL's data directory and log space, such as binlog, relaylog, undolog, errorlog and slowlog. |
| Delivered Data Volume | bytes_sent | MB/s | Instance Dimension | [View MySQL's Official Guide][3] |
| Received Data Volume | bytes_received | MB/s | Instance Dimension | [View MySQL's Official Guide][3] |
| Capacity Usage | volume_rate | % | Instance Dimension | Real Disk Capacity/Purchased Instance Space |
| Query Cache Hit Rate | qcache_hit_rate | % | Instance Dimension | [View MySQL's Official Guide][3] |
| Query Cache Usage | qcache_use_rate | % | Instance Dimension | [View MySQL's Official Guide][3] |
| Number of Table Lock Waits | table_locks_waited | Count/s | Instance Dimension | [View MySQL's Official Guide][3] |
| Number of Temporary Tables | created_tmp_tables | Count/s | Instance Dimension | [View MySQL's Official Guide][3] |
| innodb Cache Hit Rate | innodb_cache_hit_rate | % | Instance Dimension | [View MySQL's Official Guide][3] |
| innodb Cache Usage | innodb_cache_use_rate | % | Instance Dimension | [View MySQL's Official Guide][3] |
| Number of innodb's Disk Reads | innodb_os_file_reads | Count/s | Instance Dimension | [View MySQL's Official Guide][3] |
| Number of innodb's Disk Writes | innodb_os_file_writes | Count/s | Instance Dimension | [View MySQL's Official Guide][3] |
| Number of innodb fsync | innodb_os_fsyncs | Count/s | Instance Dimension | [View MySQL's Official Guide][3] |
| myisam Cache Hit Rate | key_cache_hit_rate | % | Instance Dimension | [View MySQL's Official Guide][3] |
| myisam Cache Usage | key_cache_use_rate | % | Instance Dimension | [View MySQL's Official Guide][3] |
| CPU Proportion | cpu_use_rate |% | Instance Dimension | Off-peak traffic of the host can be over used and may be over 100% |
| Memory Usage | memory_use | MB | Instance Dimension | Off-peak traffic of the host can be over used and may be over 100% |
| Number of Temporary Files | created_tmp_files | Count/s | Instance Dimension | [View MySQL's Official Guide][3] |
| Number of Opened Tables | opened_tables | Count | Instance Dimension | [View MySQL's Official Guide][3] |
| Number of Submission | com_commit | Count/s | Instance Dimension | [View MySQL's Official Guide][3] |
| Number of Rollbacks | com_rollback | Count/s | Instance Dimension | [View MySQL's Official Guide][3] |
| Number of Created Threads | threads_created | Count | Instance Dimension | | [View MySQL's Official Guide][3] |
| Number of Running Threads | threads_running | Count | Instance Dimension | | [View MySQL's Official Guide][3] |
| Max. Number of Connections | max_connections | Count | Instance Dimension | | [View MySQL's Official Guide][3] |
| Number of Temporary Tables in the Disk | created_tmp_disk_tables | Count/s | Instance Dimension | [View MySQL's Official Guide][3] |
| Number of Requests of Reading the Next Line | handler_read_rnd_next | Count/s | Instance Dimension | [View MySQL's Official Guide][3] |
| Number of Internal Rollbacks | handler_rollback | Count/s | Instance Dimension | [View MySQL's Official Guide][3] |
| Number of Internal Submission | handler_commit | Count/s | Instance Dimension | [View MySQL's Official Guide][3] |
| Number of InnoDB Blank Pages | innodb_buffer_pool_pages_free | Count | Instance Dimension | [View MySQL's Official Guide][3] |
| Number of InnoDB Blank Pages | innodb_buffer_pool_pages_total | Count | Instance Dimension | [View MySQL's Official Guide][3] |
| InnoDB Logic Read | innodb_buffer_pool_read_requests | Count/s | Instance Dimension | [View MySQL's Official Guide][3] |
| InnoDB Physical Read | innodb_buffer_pool_reads | Count/s | Instance Dimension | [View MySQL's Official Guide][3] |
| InnoDB Read Volume | innodb_data_read | Byte/s | Instance Dimension | [View MySQL's Official Guide][3] |
| Total InnoDB Read Volume | innodb_data_reads | Count/s | Instance Dimension | [View MySQL's Official Guide][3] |
| Total InnoDB Write Volume | innodb_data_writes | Count/s | Instance Dimension | [View MySQL's Official Guide][3] |
| InnoDB Write Volume | innodb_data_written | Byte/s | Instance Dimension | [View MySQL's Official Guide][3] |
| Number of InnoDB Deleted Rows | innodb_rows_deleted | Count/s | Instance Dimension | [View MySQL's Official Guide][3] |
| Number of InnoDB Inserted Rows | innodb_rows_inserted | Count/s | Instance Dimension | [View MySQL's Official Guide][3] |
| Number of InnoDB Upgraded Rows | innodb_rows_updated | Count/s | Instance Dimension | [View MySQL's Official Guide][3] |
| Number of InnoDB Read Rows | innodb_rows_read | Count/s | Instance Dimension | [View MySQL's Official Guide][3] |
| Average Lock Time of InnoDB's Acquiring Rows | innodb_row_lock_time_avg | Count/s | Instance Dimension | [View MySQL's Official Guide][3] |
| Number of InnoDB's Row Lock Waits | innodb_row_lock_waits | Count/s | Instance Dimension | [View MySQL's Official Guide][3] |
| Number of Unused Blocks in Keyboard Cache | key_blocks_unused | Count | Instance Dimension | [View MySQL's Official Guide][3] |
| Number of Used Blocks in Keyboard Cache | key_blocks_used | Count | Instance Dimension | [View MySQL's Official Guide][3] |
| Number of Data Blocks Read by Keyboard Cache | key_read_requests | Count/s | Instance Dimension | [View MySQL's Official Guide][3] |
| Number of Data Blocks Read by Hard Disks | key_reads | Count/s | Instance Dimension | [View MySQL's Official Guide][3] |
| Number of Data Block Written into Keyboard Cache | key_write_requests | Count/s | Instance Dimension | [View MySQL's Official Guide][3] |
| Number of Data Block Written into Hard Disks | key_writes | Count/s | Instance Dimension | [View MySQL's Official Guide][3] |
| Distance between the Unsynchronized Master and Slave | master_slave_sync_distance | MB | Instance Dimension | [View MySQL's Official Guide][3] |


For more information about how to use the monitoring metrics in the database, please see [Interface of Reading Monitored Data](https://cloud.tencent.com/document/api/248/11006) in the Cloud Monitor API.

> More monitoring metrics will be available in the future.

[1]:	https://console.cloud.tencent.com/
[2]:	https://console.cloud.tencent.com/cdb/ "Cloud Database Console"
[3]:	https://dev.mysql.com/doc/refman/5.6/en/ "View MySQL's Official Guide"


