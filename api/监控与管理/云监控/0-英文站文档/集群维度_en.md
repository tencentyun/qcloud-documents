## 1. API Description

Domain name: monitor.api.qcloud.com


Tencent CCS is a solution that helps users build, operate and manage container clusters. It connects Tencent Cloud's computing, network, storage, monitoring, security capabilities in a seamless manner, and helps users upgrade development mode, change how applications are delivered and reconfigure data management method. It also helps enterprises migrate their business into the cloud quickly, accelerate application deployment, and simplify cluster management. For more information, please see <a href="https://cloud.tencent.com/document/product/457/6759">CCS Overview</a>.

This API (GetMonitorData) is used to query the monitoring data of CCS - Cluster dimension. The values for input parameters are as follows:
namespace: qce/cvm
dimensions.0.name=docker_clusterid
dimensions.0.value is cluster ID

| Name   | Description                                     |
| ---------------- | ---------------------------------------- |
| docker_clusterid | Enter "clusterId" (Cluster Id) returned when calling the API [Query Cluster List](https://cloud.tencent.com/document/api/457/9448) |

## 2. Input Parameters

The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see <a href="/doc/api/405/公共请求参数" title="Common Request Parameters"> Common Request Parameters</a> page. The Action field for this API is GetMonitorData.

### 2.1 Input Parameters

| Parameter Name               | Required   | Type       | Input Content             | Description                                       |
| ------------------ | ---- | -------- | ---------------- | ---------------------------------------- |
| namespace          | Yes    | String   | qce/cvm   | Namespace. Every Tencent Cloud product has a namespace. For more information, please see Input Content column.           |
| metricName         | Yes    | String   | Specific metric name          | Metric name. For more information, please see 2.2                            |
| dimensions.0.name  | Yes    | String   | docker_clusterid | Input parameter is the cluster ID                                  |
| dimensions.0.value | Yes    | String   | Specific cluster ID          | Enter specific docker_clusterid                     |
| period             | No    | Int      | 60/300       | Interval for collecting monitoring data. Most metrics support a statistical granularity of 60s while some metrics only support a statistical granularity of 300s. Statistical granularity varies with metrics. Enter parameters by referring to the list of metric details in section 2.2. |
| startTime          | No    | Datetime | Start time             | Start time, such as "2016-01-01 10:25:00". Default time is "00:00:00" of the current day |
| endTime            | No    | Datetime | End time                | End time. It is the current time by default. endTime cannot be earlier than startTime       |

### 2.2 Metric Name
| Monitoring Item      | Metric Name         | Unit   | Description             |
| -------- | ------------ | ---- | -------------- |
| Cluster CPU utilization | dc_cpu_usage | %    | Average CPU utilization of the nodes in the cluster |
| Cluster memory utilization  | dc_mem_usage | %    | Average memory utilization of the nodes in the cluster  |


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
| -507 | Limit is exceeded       | OperationDenied.ExceedLimit          |
| -509 | Incorrect dimension group | InvalidParameter.DimensionGroupError |
| -513 | DB operation failed  | InternalError.DBoperationFail        |

## 5. Example

Input

<pre>
https://monitor.api.qcloud.com/v2/index.php?
&<a href="/doc/api/405/公共请求参数" title="Common Request Parameters">Common Request Parameters</a>
&namespace=qce/cvm
&metricName=dc_cpu_usage
&dimensions.0.name=docker_clusterid
&dimensions.0.value=cls-xxxxx
&startTime=2017-03-28 14:10:00
&endTime=2016-03-28 15:10:00
&period=60
</pre>

Output

```
{
    "code": 0,
	"message": "",
	"metricName": "dc_cpu_usage",
	"startTime": "2017-03-28 14:10:00",
	"endTime": "2016-03-28 15:10:00",
	"period": 60,
    "dataPoints": [
        30,
        35,
        40
    ]
}
```
