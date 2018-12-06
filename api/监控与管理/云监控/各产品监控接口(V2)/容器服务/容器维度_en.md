## 1. API Description

Domain name: monitor.api.qcloud.com


Tencent CCS is a solution that helps users build, operate and manage container clusters. It connects Tencent Cloud's computing, network, storage, monitoring, security capabilities in a seamless manner, and helps users upgrade development mode, change how applications are delivered and reconfigure data management method. It also helps enterprises migrate their business into the cloud quickly, accelerate application deployment, and simplify cluster management. For more information, please see <a href="https://cloud.tencent.com/document/product/457/6759">CCS Overview</a>.

This API (GetMonitorData) is used to query the monitoring data of CCS - Container dimension. The values for input parameters are as follows:
namespace: qce/docker
dimensions.0.name=clusterId
dimensions.0.value is cluster ID
dimensions.1.name=serviceName
dimensions.1.value is service name
dimensions.2.name=namespace
dimensions.2.value is namespace name
dimensions.3.name=podName
dimensions.3.value is Pod name
dimensions.4.name=containerId
dimensions.4.value is container ID

| Name   | Description                                     |
| ----------- | ---------------------------------------- |
| clusterId   | Enter "clusterId" (Cluster Id) returned when calling the API [Query Cluster List](https://cloud.tencent.com/document/api/457/9448) |
| serviceName | Enter "serviceName" (Service name) returned when calling the API [Query Service List](https://cloud.tencent.com/document/api/457/9440) |
| namespace   | Enter "namespace" (Namespace) returned when calling the API [Query Service List](https://cloud.tencent.com/document/api/457/9440) |
| podName     | Enter "name" (Pod name) returned when calling the API [Query Service Pod List](https://cloud.tencent.com/document/api/457/9433) |
| containerId | Enter "contianerId" (Container Id) returned when calling the API Query Service Pod List.<font style="color:red"><strong> Note: Container Id only takes the first 12 digits</strong></font> |

## 2. Input Parameters

The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see <a href="/doc/api/405/公共请求参数" title="Common Request Parameters"> Common Request Parameters</a> page. The Action field for this API is GetMonitorData.

### 2.1 Input Parameters

| Parameter Name               | Required   | Type       | Input Content    | Description                                       |
| ------------------ | ---- | -------- | ------- | ---------------------------------------- |
| namespace          | Yes    | String   | qce/cvm  | Namespace. Every Tencent Cloud product has a namespace. For more information, please see Input Content column.           |
| metricName         | Yes    | String   | Specific metric name | Metric name. For more information, please see 2.2                            |
| dimensions.n.name  | Yes    | String   | Dimension name   | Dimension name, which is used in combination with dimensions.n.value. For more information, please see section 1. |
| dimensions.n.value | Yes    | String   | Dimension value | Dimension value, which is used in combination with dimensions.n.name. For more information, please see section 1. |
| period             | No    | Int      | 60/300  | Interval for collecting monitoring data. Most metrics support a statistical granularity of 60s while some metrics only support a statistical granularity of 300s. Statistical granularity varies with metrics. Enter parameters by referring to the list of metric details in section 2.2. |
| startTime          | No    | Datetime | Start time    | Start time, such as "2016-01-01 10:25:00". Default is "00:00:00" of the current day |
| endTime            | No    | Datetime | End time    | End time. It is the current time by default. endTime cannot be earlier than startTime       |

### 2.2 Metric Name
| Monitoring Item                | Metric Name                            | Unit    | Description              |
| ------------------ | ------------------------------- | ----- | --------------- |
| Container CPU Usage          | container_cpu_used              | Core     | CPU usage of the container        |
| Container CPU utilization (for CVM)      | container_cpu_usage_for_node    | %     | Ratio of container CPU utilization to CVM      |
| Container CPU utilization (for Request) | container_cpu_usage_for_request | %     | Ratio of container CPU utilization to Request |
| Container CPU utilization (for Limit)   | container_cpu_usage_for_limit   | %     | Ratio of container CPU utilization to Limit   |
| Container memory usage           | container_mem_used              | MiB   | Amount of container memory used         |
| Container memory utilization (for CVM)       | container_mem_usage_for_node    | %     | Ratio of container memory utilization to CVM       |
| Container memory utilization (for Request)  | container_mem_usage_for_request | %     | Ratio of container memory utilization to Request  |
| Container memory utilization (for Limit)    | container_mem_usage_for_limit   | %     | Ratio of container memory utilization to Limit    |
| Container disk read traffic            | container_disk_read_traffic     | KB/sec  | Disk read traffic when container reads from the disk        |
| Container disk write traffic            | container_disk_write_traffic    | KB/sec  | Disk write traffic when container writes to the disk        |
| Container disk read IOPS          | container_disk_read             | count | Read IOPS when container reads from the disk      |
| Container disk write IOPS          | container_disk_write            | count | Write IOPS when container writes to the disk      |
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
&namespace=qce/docker
&metricName=container_cpu_used
&dimensions.0.name=clusterId
&dimensions.0.value=cls-xxxxx
&dimensions.1.name=serviceName
&dimensions.1.value=test
&dimensions.2.name=namespace
&dimensions.2.value=default
&dimensions.3.name=podName
&dimensions.3.value=test-3488000495-nj6s9
&dimensions.4.name=containerId
&dimensions.4.value=01c5509d2b39
&startTime=2017-03-28 14:10:00
&endTime=2016-03-28 15:10:00
&period=60
</pre>

Output

```
{
	"code": 0,
	"message": "",
	"metricName": "container_cpu_used",
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
