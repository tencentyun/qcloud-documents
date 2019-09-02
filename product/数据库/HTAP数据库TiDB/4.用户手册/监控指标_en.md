

**Cluster Metric**

| Metric | ID | Unit |
|---------|---------|---------|
| Cluster storage usage | cluster_storage_size | Bytes |

**TiDB Metric**

| Metric | ID | Unit |
|---------|---------|---------|
| Total number of query requests | tidb_server_query_total | Count |
| Number of active connections of database | tidb_server_connection | Count |
| Memory usage | tidb_go_memstats_heap_inuse_bytes | Bytes | 
| Average CPU utilization | tidb_process_cpu_seconds_total_avg |  |
| INSERT statement statistics | tidb_executor_statement_node_total_insert | Count |
| DELETE statement statistics | tidb_executor_statement_node_total_delete | Count |
| UPDATE statement statistics | tidb_executor_statement_node_total_update | Count |
| SELECT statement statistics | tidb_executor_statement_node_total_select | Count |

**TiKV Metric**

| Metric | ID | Unit |
|---------|---------|---------|
| Key usage | tikv_region_written_keys_count | Count |
| Average CPU utilization | tikv_process_cpu_seconds_total_avg |  |
| Storage usage | tikv_region_written_bytes_count | Bytes |
