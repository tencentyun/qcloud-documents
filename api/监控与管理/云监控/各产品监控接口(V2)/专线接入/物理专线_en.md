## 1. API Description

Domain name: monitor.api.qcloud.com
API: GetMonitorData

Physical direct connect is a physical line used to connect Tencent Cloud with local IDCs.

This API (GetMonitorData) is used to query the monitoring data of physical direct connect. The values for input parameters are as follows:

namespace: qce/dc

dimensions.0.name=directConnectId

dimensions.0.value (direct connect ID)

## 2. Input Parameters

The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see <a href="/doc/api/405/公共请求参数" title="Common Request Parameters">Common Request Parameters</a> page. The Action field for this API is GetMonitorData.

### 2.1 Input Parameters

| Parameter Name | Required | Type | Input Content | Description |
| ------------------ | ---- | -------- | --------------- | ---------------------------------------- |
| namespace | Yes | String | qce/dc | Namespace. Every Tencent Cloud product has a namespace. For more information, please see Input Content column. |
| metricName | Yes | String | Specific metric name | Metric name. For more information, please see 2.2 |
| dimensions.0.name | Yes | String | directConnectId | Input parameter is direct connect ID |
| dimensions.0.value | Yes | String | The ID of direct connect | The field unInstanceId obtained by calling the API [DescribeInstances](http://cloud.tencent.com/doc/api/229/%E6%9F%A5%E7%9C%8B%E5%AE%9E%E4%BE%8B%E5%88%97%E8%A1%A8) |
| period | No | Int | 60/300 | Interval for collecting monitoring data. A statistical granularity of 60s is supported. |
| startTime | No | Datetime | Start time | Start time, such as "2016-01-01 10:25:00". Default is "00:00:00" of the current day |
| endTime | No | Datetime | End time | End time. It is the current time by default. endTime cannot be earlier than startTime |
### 2.2 Metric Name

| Metric Name (metricName) | Description | Unit | Statistical Granularity (period) |
| ---------------- | ---- | ---- | ------------ |
| inbandwidth | Inbound bandwidth | bps | 60s |
| outbandwidth | Outbound bandwidth | bps | 60s |


## 3. Output Parameters

| Parameter Name | Type | Description |
| ---------- | -------- | ------------------- |
| code | Int | Error code. 0: Successful; other values: Failed |
| message | String | Error message |
| startTime | Datetime | Start time |
| endTime | Datetime | End time |
| metricName | String | Metric name |
| period | Int | Interval for collecting monitoring data |
| dataPoints | Array | Monitoring data list |


## 4. Error Codes

| Error Code | Error Description | Error Message |
| ---- | ------- | ------------------------------------ |
| -502 | Resource does not exist | OperationDenied.SourceNotExists |
| -503 | Incorrect request parameter | InvalidParameter |
| -505 | Parameter is missing | InvalidParameter.MissingParameter |
| -507 | Limit is exceeded | OperationDenied.ExceedLimit |
| -509 | Incorrect dimension group | InvalidParameter.DimensionGroupError |
| -513 | DB operation failed | InternalError.DBoperationFail |

## 5. Example

Input

<pre>
https://monitor.api.qcloud.com/v2/index.php?
&<a href="/doc/api/405/公共请求参数" title="Common Request Parameters">Common Request Parameters</a>
&namespace=qce/dc
&metricName=inbandwidth
&dimensions.0.name=directConnectId
&dimensions.0.value=dc-e6p0gw5f
&startTime=2016-06-28 14:10:00
&endTime=2016-06-28 14:20:00
</pre>

Output

```
{
	"code": 0,
	"message": "",
	"metricName": "inbandwidth",
	"startTime": "2016-06-28 14:10:00",
	"endTime": "2016-06-28 14:20:00",
	"period": 300,
	"dataPoints": [
		15.6,
		17.9
		20.3
	]
}
```

