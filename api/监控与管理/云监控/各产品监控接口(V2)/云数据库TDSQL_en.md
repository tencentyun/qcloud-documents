## 1. API Description

Domain name: monitor.api.qcloud.com


Especially designed for OLTP scenarios, Tencent CDB for TDSQL is a high-security enterprise-level cloud database used in Tencent billing services for over ten years. TDSQL is compatible with MySQL syntax, and has advanced features such as thread pool, audit and remote disaster recovery. In addition, it is highly scalable, easy to use, and cost-effective just like other cloud databases. For more information, please see <a href="/doc/product/237/产品概述" title="Product Overview">CDB for TDSQL Introduction</a> page.

This API (GetMonitorData) is used to query the monitoring data of CDB for TDSQL product. The values for input parameters are as follows:
namespace:qce/tdsql
dimensions.0.name=uuid
Dimensions.0.value is instance uuid

## 2. Input Parameters

The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see <a href="/doc/api/405/公共请求参数" title="Common Request Parameters"> Common Request Parameters</a> page. The Action field for this API is GetMonitorData.

### 2.1 Input Parameters

| Parameter Name               | Required   | Type       | Input Content      | Description                                       |
| ------------------ | ---- | -------- | --------- | ---------------------------------------- |
| namespace          | Yes    | String   | qce/cvm   | Namespace. Every Tencent Cloud product has a namespace. For more information, please see Input Content column.           |
| metricName         | Yes    | String   | Specific metric name   | Metric name. For more information, please see 2.2                            |
| dimensions.0.name  | Yes    | String   | uuid      | Input parameter is the instance uuid                               |
| dimensions.0.value | Yes    | String   | Specific instance uuid | Enter a specific instance uuid, such as tdsql-0gfryg60              |
| period             | No    | Int      | 60/300    | Interval for collecting monitoring data. Most metrics support a statistical granularity of 60s while some metrics only support a statistical granularity of 300s. Statistical granularity varies with metrics. Enter parameters by referring to the list of metric details in section 2.2. |
| startTime          | No    | Datetime | Start time      | Start time, such as "2016-01-01 10:25:00". Default is "00:00:00" of the current day |
| endTime            | No    | Datetime | End time     | End time. It is the current time by default. endTime cannot be earlier than startTime       |
### 2.2 Metric Name

| Metric Name | Description | Unit |
| --------------------- | ------------ | ---- |
| data_disk_available   | Available size of data disk     | MB   |
| binlog_disk_available | Available size of BINLOG disk | MB   |
| select_total          | Number of SELECT requests   | Counts/sec  |
| long_query            | Number of SELECT slow queries   | Counts/sec  |
| update_total          | Number of UPDATE requests   | Counts/sec  |
| insert_total          | Number of INSERT requests   | Counts/sec  |
| delete_total          | Number of DELETE requests   | Counts/sec  |
| mem_available         | Available size of memory       | GB   |
| disk_iops             | Disk IOPS       | Counts/sec  |
| conn_active           | Number of connections       | Counts/sec  |
| conn_running          | Number of active connections          | Counts/sec  |
| is_master_switched    | Whether the monitor switches between master and slave     | None    |
| cpu_usage_rate        | CPU utilization       | %    |


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
&namespace=qce/tdsql
&metricName=data_disk_available
&dimensions.0.name=uuid
&dimensions.0.value=tdsql-0gfryg60
&startTime=2016-06-28 14:10:00
&endTime=2016-06-28 14:20:00
</pre>

Output

```
{
	"code": 0,
	"message": "",
	"metricName": "data_disk_available",
	"startTime": "2016-06-28 14:10:00",
	"endTime": "2016-06-28 14:20:00",
	"period": 300,
	"dataPoints": [
		28.3,
        28.3,
		28.3
	]
}
```

