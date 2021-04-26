## 1. API Description

Domain name: monitor.api.qcloud.com


CDB for SQL Server is a cloud database created by Tencent Cloud based on the Microsoft SQL Server. For more information, please see <a href="/doc/product/238/产品概述" title="Product Overview">CDB for SQL Server</a> page.

This API (GetMonitorData) is used to query the monitoring data of CDB for SQL Server product. The values for input parameters are as follows:
namespace:qce/sqlserver
dimensions.0.name=resourceId 
Dimensions.0.value is instance resource Id

## 2. Input Parameters

The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see <a href="/doc/api/405/公共请求参数" title="Common Request Parameters"> Common Request Parameters</a> page. The Action field for this API is GetMonitorData.

### 2.1 Input Parameters

| Parameter Name               | Required   | Type       | Input Content       | Description                                       |
| ------------------ | ---- | -------- | ---------- | ---------------------------------------- |
| namespace          | Yes    | String   | qce/cvm    | Namespace. Every cloud product has a namespace. For more information, please see Input Content column.           |
| metricName         | Yes    | String   | Specific metric name    | Metric name. For more information, please see 2.2                            |
| dimensions.0.name  | Yes    | String   | resourceId | Input parameter is the instance resource ID                               |
| dimensions.0.value | Yes    | String   | Specific instance resource Id  | Enter a specific instance resource ID, such asmssql-dh01nvsb              |
| period             | No    | Int      | 60/300     | Interval for collecting monitoring data. Most metrics support a statistical granularity of 60s while some metrics only support a statistical granularity of 300s. Statistical granularity varies with metrics. Enter parameters by referring to the list of metric details in section 2.2. |
| startTime          | No    | Datetime | Start time       | Start time, such as "2016-01-01 10:25:00". Default is "00:00:00" of the current day |
| endTime            | No    | Datetime | End time       | End time. It is the current time by default. endTime cannot be earlier than startTime       |
### 2.2 Metric Name

| Metric Name | Description | Unit |
| ---------------------- | --------------------- | ---- |
| cpu                    | Percentage of instance CPU consumption           | %    |
| transactions           | Average number of transactions per second              | Counts/sec  |
| connections            | Average number of users connected to the database per second        | Counts    |
| requests               | Number of requests per second                | Counts/sec  |
| logins                 | Number of logins per second                | Counts/sec  |
| logouts                | Number of logouts per second                | Counts/sec  |
| storage                | Total amount of storage occupied by instance database files and log files   | GB   |
| in_flow                | Total size of all connected input packages           | MB/sec |
| out_flow               | Total size of all connected output packages           | MB/sec |
| iops                   | Number of disk reads and writes                | Counts/sec  |
| disk_reads             | Number of disk reads per second              | Counts/sec  |
| disk_writes            | Number of disk writes per second              | Counts/sec  |
| slow_queries           | Number of queries for which the execution time exceeds 1 second         | Counts    |
| blocked_processes      | Number of current blocks                | Counts    |
| lock_requests          | Average number of lock requests per second            | Counts/sec  |
| user_errors            | Average number of errors per second               | Counts/sec  |
| sql_compilations       | Average number of SQL compilations per second           | Counts/sec  |
| sql_recompilations     | Average number of SQL recompilations per second          | Counts/sec  |
| full_scans             | Number of unlimited full scans per second          | Counts/sec  |
| buffer_cache_hit_ratio | Data cache (memory) hit rate           | %    |
| latch_waits            | Number of latch waits per second              | Counts/sec  |
| lock_waits             | Average waiting time for each lock request that causes waiting     | ms   |
| network_io_waits       | Average delay time of network IO            | ms   |
| plan_cache_hit_ratio   | Hit rate of an execution plan (each SQL has an execution plan) | %    |


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
&namespace=qce/sqlserver
&metricName=cpu
&dimensions.0.name=resourceId
&dimensions.0.value=mssql-dh01nvsb
&startTime=2016-06-28 14:10:00
&endTime=2016-06-28 14:20:00
</pre>

Output

```
{
	"code": 0,
	"message": "",
	"metricName": "cpu",
	"startTime": "2016-06-28 14:10:00",
	"endTime": "2016-06-28 14:20:00",
	"period": 300,
	"dataPoints": [
		50,
		47,
		44
	]
}
```
