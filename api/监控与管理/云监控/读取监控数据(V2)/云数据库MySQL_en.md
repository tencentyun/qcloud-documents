## 1. API Description

Domain name: monitor.api.qcloud.com


Cloud Database for MySQL is a high-performance distributed data storage service created by Tencent Cloud based on the world's most popular open source database MySQL. For more information, please see <a href="/doc/product/236/简介" title="Overview">CDB for MySQL</a> page.

This API (GetMonitorData) is used to query the monitoring data of CDB for MySQL product. The values for input parameters are as follows:
namespace:qce/cdb
dimensions.0.name=uInstanceId
Dimensions.0.value is cdb instance id 

## 2. Input Parameters

The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see <a href="/doc/api/405/公共请求参数" title="Common Request Parameters"> Common Request Parameters</a> page. The Action field for this API is GetMonitorData.

### 2.1 Input Parameters

| Parameter Name               | Required   | Type       | Input Content        | Description                                       |
| ------------------ | ---- | -------- | ----------- | ---------------------------------------- |
| namespace          | Yes    | String   | qce/cdb  | Namespace. Every Tencent Cloud product has a namespace. For more information, please see Input Content column.           |
| metricName         | Yes    | String   | Specific metric name     | Metric name. For more information, please see 2.2                            |
| dimensions.0.name  | Yes    | String   | uInstanceId | Input parameter is CDB instance ID                               |
| dimensions.0.value | Yes    | String   | Specific CDB instance ID  | Enter CDB instance ID, such as cdb-e242adzf               |
| period | No | Int | 60/300 | Interval for collecting monitoring data. Most metrics support a statistical granularity of 60s while some metrics only support a statistical granularity of 300s. Statistical granularity varies with metrics. Enter parameters by referring to the list of metric details in section 2.2. |
| startTime | No | Datetime | Start time | Start time, such as "2016-01-01 10:25:00". Default is "00:00:00" of the current day |
| endTime | No | Datetime | End time| End time. It is the current time by default. endTime cannot be earlier than startTime |
### 2.2 Metric Name

| Metric Name | Description | Unit |
| -------------------------------- | -------------- | ------ |
| slow_queries                     | Number of slow queries           | Counts/min    |
| max_connections                  | Maximum number of connections          | Counts      |
| select_scan                      | Number of full table scans          | Counts/sec    |
| select_count                     | Number of queries            | Counts/sec    |
| com_update                       | Number of updates            | Counts/sec    |
| com_delete                       | Number of deletions            | Counts/sec    |
| com_insert                       | Number of insertions            | Counts/sec    |
| com_replace                      | Number of overwrites            | Counts/sec    |
| queries                          | Number of requests           | Counts/sec    |
| threads_connected                | Number of open connections        | Counts      |
| real_capacity                    | Real disk capacity         | MB     |
| capacity                         | Total disk capacity         | MB     |
| bytes_sent                       | Private network outbound traffic          | Bytes/sec |
| bytes_received                   | Private network inbound traffic          | Bytes/sec |
| qcache_use_rate                  | Cache utilization          | %      |
| qcache_hit_rate                  | Cache hit rate          | %      |
| table_locks_waited               | Number of table lock waits         | Counts/sec    |
| created_tmp_tables               | Number of temporary tables          | Counts/sec    |
| innodb_cache_use_rate            | innodb cache utilization    | %      |
| innodb_cache_hit_rate            | innodb cache hit rate    | %      |
| innodb_os_file_reads             | Number of innodb's disk reads    | Counts/sec    |
| innodb_os_file_writes            | Number of innodb's disk writes    | Counts/sec    |
| innodb_os_fsyncs                 | Number of innodb fsync | Counts/sec    |
| key_cache_use_rate               | myisam cache utilization    | %      |
| key_cache_hit_rate               | myisam cache hit rate    | %      |
| volume_rate                      | Volume rate          | %      |
| query_rate                       | Query rate          | %      |
| qps                              | Operations per second        | Counts/sec    |
| tps                              | Transactions per second        | Counts/sec    |
| cpu_use_rate                     | CPU proportion          | %      |
| memory_use                       | Memory usage           | MB     |
| key_write_requests               | Number of data blocks written into keyboard cache     | Counts/sec    |
| key_writes                       | Number of data blocks written into disks      | Counts/sec    |
| com_commit                       | Number of submissions            | Counts/sec    |
| handler_commit                   | Number of internal submissions          | Counts/sec    |
| innodb_rows_read                 | Number of rows read from InnoDB     | Counts/sec    |
| innodb_row_lock_time_avg         | Average Lock Time of InnoDB's Acquiring Rows | millisecond     |
| threads_created                  | Number of created threads        | Counts      |
| opened_tables                    | Number of opened tables        | Counts      |
| threads_running                  | Number of running threads         | Counts      |
| innodb_data_reads                | Number of InnoDB reads     | Counts/sec    |
| com_rollback                     | Number of rollbacks            | Counts/sec    |
| key_blocks_unused                | Number of unused blocks in keyboard cache    | Counts      |
| innodb_data_writes               | Number of InnoDB writes     | Counts/sec    |
| innodb_buffer_pool_pages_free    | Number of empty pages in InnoDB      | Counts      |
| innodb_rows_inserted             | Number of rows inserted in InnoDB     | Counts/sec    |
| created_tmp_files                | Number of temporary files         | Counts/sec    |
| innodb_data_read                 | Number of InnoDB reads      | Bytes/sec |
| innodb_row_lock_waits            | Number of InnoDB row lock waits   | Counts/sec    |
| innodb_buffer_pool_read_requests | Number of InnoDB logical reads      | Counts/sec    |
| handler_rollback                 | Number of internal rollbacks          | Counts/sec    |
| master_slave_sync_distance       | Distance between the unsynchronized master and slave        | MB     |
| handler_read_rnd_next            | Number of requests of reading the next line        | Counts/sec    |
| innodb_rows_updated              | Number of rows updated in InnoDB     | Counts/sec    |
| innodb_rows_deleted              | Number of rows deleted in InnoDB     | Counts/sec    |
| innodb_buffer_pool_pages_total   | Number of empty pages in InnoDB      | Counts      |
| key_blocks_used                  | Number of used blocks in keyboard cache     | Counts      |
| innodb_data_written              | Number of InnoDB writes      | Bytes/sec |
| key_read_requests                | Number of data blocks read by keyboard cache     | Counts/sec    |
| innodb_buffer_pool_reads         | Number of InnoDB physical reads      | Counts/sec    |
| created_tmp_disk_tables          | Number of temporary tables in the disk        | Counts/sec    |
| key_reads                        | Number of data blocks read by disks      | Counts/sec    |




## 3. Output Parameters

| Parameter Name       | Type       | Description                  |
| ---------- | -------- | ------------------- |
| code       | Int      | Error code. 0: Successful; other values: Failed |
| message    | String   | Error message                |
| startTime  | Datetime | Start time                |
| endTime    | Datetime | End time                |
| metricName | String   | Metric name                |
| period     | Int      | Interval for collecting monitoring data              |
| dataPoints | Array    | Monitoring data list              |


## 4. Error Codes

| Error Code | Error Description    | Error Message                                 |
| ---- | ------- | ------------------------------------ |
| -502 | Resource does not exist   | OperationDenied.SourceNotExists      |
| -503 | Incorrect request parameter  | InvalidParameter                     |
| -505 | Parameter is missing    | InvalidParameter.MissingParameter    |
| -507 | Limit is exceeded    | OperationDenied.ExceedLimit          |
| -509 | Incorrect dimension group | InvalidParameter.DimensionGroupError |
| -513 | DB operation failed  | InternalError.DBoperationFail        |

## 5. Example

Input

<pre>
https://monitor.api.qcloud.com/v2/index.php?
&<a href="/doc/api/405/公共请求参数" title="Common Request Parameters">Common Request Parameters</a>
&namespace=qce/cdb
&metricName=slow_queries
&dimensions.0.name=uInstanceId
&dimensions.0.value=cdb-e242adzf
&startTime=2016-06-28 14:10:00
&endTime=2016-06-28 14:20:00
</pre>

Output

```
{
	"code": 0,
	"message": "",
	"metricName": "slow_queries",
	"startTime": "2016-06-28 14:10:00",
	"endTime": "2016-06-28 14:20:00",
	"period": 300,
	"dataPoints": [
		55,
		46,
		33
	]
}
```
