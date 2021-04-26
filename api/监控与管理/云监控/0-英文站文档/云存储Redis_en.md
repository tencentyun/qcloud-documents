## 1. API Description

Domain name: monitor.api.qcloud.com


Cloud Redis Store (CRS) is a highly available and reliable Redis service platform, which is built on Tencent Cloud's years of technical expertise in distributed cache. It is designed to meet demands for Redis business operations. For more information, please see <a href="/doc/product/239/产品介绍" title="Product Overview">Cloud Redis Introduction</a> page.

This API (GetMonitorData) is used to query the monitoring data of CRS product. The values for input parameters are as follows:
namespace: qce/redis
dimensions.0.name=redis_uuid
Dimensions.0.value is instance uuid

## 2. Input Parameters

The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see <a href="/doc/api/405/公共请求参数" title="Common Request Parameters"> Common Request Parameters</a> page. The Action field for this API is GetMonitorData.

### 2.1 Input Parameters

| Parameter Name               | Required   | Type       | Input Content       | Description                                       |
| ------------------ | ---- | -------- | ---------- | ---------------------------------------- |
| namespace          | Yes    | String   | qce/redis  | Namespace. Every cloud product has a namespace. For more information, please see Input Content column.           |
| metricName         | Yes    | String   | Specific metric name    | Metric name. For more information, please see 2.2                            |
| dimensions.0.name  | Yes    | String   | redis_uuid | Input parameter must be redis_uuid                          |
| dimensions.0.value | Yes    | String   | Specific uuid    | Enter Redis instance id, i.e. instance ID, such as crs-ifmymj41. It can be queried with the API [Query CRS Instance List](http://cloud.tencent.com/doc/api/260/1384) |
| period             | No    | Int      | 60/300     | Interval for collecting monitoring data. Most metrics support a statistical granularity of 60s while some metrics only support a statistical granularity of 300s. Statistical granularity varies with metrics. Enter parameters by referring to the list of metric details in section 2.2. |
| startTime          | No    | Datetime | Start time       | Start time, such as "2016-01-01 10:25:00". Default is "00:00:00" of the current day |
| endTime            | No    | Datetime | End time       | End time. It is the current time by default. endTime cannot be earlier than startTime       |
### 2.2 Metric Name
| Metric       | Name            | Metric Collecting Method (Meaning in Linux)                         | Metric Statistical Method                    | Unit    |
| ----------- | ---------------- | ---------------------------------------- | ------------------------- | ----- |
| cache hit rate    | cache_hit_ratio  | Obtain keyspace_misses, keyspace_hits within 1 minute and get the result by calculating as follows: (1 - keyspace_misses/keyspace_hits) * 100%. The metric is no longer maintained | Data is collected every minute. The granularity of 5 minutes is the average over the last 5 minutes  | %     |
| Number of get commands      | cmdstat_get      | Number of get command requests within 1 minute                           | Data is collected every minute. The granularity of 5 minutes is the summation over the last 5 minutes   | times/min  |
| Number of getbit commands   | cmdstat_getbit   | Number of getbit command requests within 1 minute                        | Data is collected every minute. The granularity of 5 minutes is the summation over the last 5 minutes   | times/min  |
| Number of getrange commands | cmdstat_getrange | Number of getrange command requests within 1 minute                      | Data is collected every minute. The granularity of 5 minutes is the summation over the last 5 minutes   | times/min  |
| Number of hget commands     | cmdstat_hget     | Number of hget command requests within 1 minute                          | Data is collected every minute. The granularity of 5 minutes is the summation over the last 5 minutes   | times/min  |
| Number of hgetall commands  | cmdstat_hgetall  | Number of hgetall command requests within 1 minute                       | Data is collected every minute. The granularity of 5 minutes is the summation over the last 5 minutes   | times/min  |
| Number of hmget commands    | cmdstat_hmget    | Number of hmget command requests within 1 minute                         | Data is collected every minute. The granularity of 5 minutes in the summation over the last 5 minutes   | times/min  |
| Number of hmset commands    | cmdstat_hmset    | Number of hmset command requests within 1 minute                         | Data is collected every minute. The granularity of 5 minutes is the summation over the last 5 minutes   | times/min  |
| Number of hset commands     | cmdstat_hset     | Number of hset command requests within 1 minute                          | Data is collected every minute. The granularity of 5 minutes is the summation over the last 5 minutes   | times/min  |
| Number of hsetnx commands   | cmdstat_hsetnx   | Number of hsetnx command requests within 1 minute                        | Data is collected every minute. The granularity of 5 minutes is the summation over the last 5 minutes   | times/min  |
| Number of lset commands     | cmdstat_lset     | Number of lset command requests within 1 minute                          | Data is collected every minute. The granularity of 5 minutes is the summation over the last 5 minutes   | times/min  |
| Number of mget commands     | cmdstat_mget     | Number of mget command requests within 1 minute                          | Data is collected every minute. The granularity of 5 minutes is the summation over the last 5 minutes   | times/min  |
| Number of mset commands     | cmdstat_mset     | Number of mset command requests within 1 minute                          | Data is collected every minute. The granularity of 5 minutes is the summation over the last 5 minutes   | times/min  |
| Number of msetnx commands   | cmdstat_msetnx   | Number of msetnx command requests within 1 minute                         | Data is collected every minute. The granularity of 5 minutes is the summation over the last 5 minutes   | times/min  |
| Number of set commands      | cmdstat_set      | Number of set command requests within 1 minute                         | Data is collected every minute. The granularity of 5 minutes is the summation over the last 5 minutes   | times/min  |
| Number of setbit commands    | cmdstat_setbit    | Number of setbit command requests within 1 minute                         | Data is collected every minute. The granularity of 5 minutes is the summation over the last 5 minutes   | times/min  |
| Number of setex commands    | cmdstat_setex    | Number of setex command requests within 1 minute                         | Data is collected every minute. The granularity of 5 minutes is the summation over the last 5 minutes   | times/min  |
| Number of setnx commands    | cmdstat_setnx    | Number of setnx command requests within 1 minute                         | Data is collected every minute. The granularity of 5 minutes is the summation over the last 5 minutes   | times/min  |
| Number of setrange commands | cmdstat_setrange | Number of setrange command requests within 1 minute                      | Data is collected every minute. The granularity of 5 minutes is the summation over the last 5 minutes   | times/min  |
| Number of commands executed per second     | qps              | Total number of commands within 1 minute divided by 60                             | Data is collected every minute. The granularity of 5 minutes is the average over the last 5 minutes | times/min  |
| Number of connections         | connections      | Total number of connections within 1 minute                                | Data is collected every minute. The granularity of 5 minutes is the summation over the last 5 minutes   | times     |
| cpu utilization      | cpu_us           | Percentage of time during which the CPU is occupied, which is calculated by obtaining data /proc/stat         | Data is collected every minute. The granularity of 5 minutes is the average over the last 5 minute | %     |
| Private network inbound traffic        | in_flow          | Summation of inbound traffic within 1 minute                                | Data is collected every minute. The granularity of 5 minutes is the summation over the last 5 minutes   | MB/min |
| Total number of keys       | keys             | Maximum number of keys within 1 minute                            | Data is collected every minute. The granularity of 5 minutes is the maximum value over the last 5 minutes | keys     |
| Private network outbound traffic       | out_flow         | Summation of outbound traffic within 1 minute                                | Data is collected every minute. The granularity of 5 minutes is the summation over the last 5 minutes   | MB/min |
| Total number of get commands    | stat_get         | Number of get/hget/hgetall/hmget/mget/getbit/getrange command requests within 1 minute | Data is collected every minute. The granularity of 5 minutes is the summation over the last 5 minutes   | times/min  |
| Total number of set commands    | stat_set         | Number of set/hset/hmset/hsetnx/lset/mset/msetnx/setbit/setex/setrange/setnx command requests within 1 minute | Data is collected every minute. The granularity of 5 minutes is the summation over the last 5 minutes   | times/min  |
| Occupied capacity       | storage          | Maximum value of the occupied capacity within 1 minute                            | Data is collected every minute. The granularity of 5 minutes is the maximum value over the last 5 minutes | MB/min |
| Capacity usage       | storage_us       | Maximum percentage of the occupied capacity within 1 minute                         | Data is collected every minute. The granularity of 5 minutes is the maximum value over the last 5 minutes | %     |


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
&namespace=qce/redis
&metricName=cache_hit_ratio
&dimensions.0.name=redis_uuid
&dimensions.0.value=crs-ifmymj41
&startTime=2016-06-28 14:10:00
&endTime=2016-06-28 14:20:00
</pre>

Output

```
{
	"code": 0,
	"message": "",
	"metricName": "cache_hit_ratio",
	"startTime": "2016-06-28 14:10:00",
	"endTime": "2016-06-28 14:20:00",
	"period": 300,
	"dataPoints": [
		50,
		40,
		30
	]
}
```
