## 1. API Description

Domain name: monitor.api.qcloud.com


Tencent Cloud Message Queue (CMQ) is a distributed message queuing service that provides a reliable message-based asynchronous communication between distributed applications or components of an application. Messages are stored in highly available and reliable CMQ queues. Multiple processes can read/write from/to a queue at the same time without interfering with each other.
CMQ provides two modes: queue and topic

This API (GetMonitorData) is used to query the monitoring data of CMQ Topic product. The values for input parameters are as follows:
namespace: qce/cmqtopic
Value of dimension name: qtopicId, subscriptionId
dimensions.0.name=topicId
dimensions.0.value is CMQ topic instance id
dimensions.1.name=subscriptionId
dimensions.1.value is CMQ subscription instance id

## 2. Input Parameters

The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see <a href="/doc/api/405/公共请求参数" title="Common Request Parameters">Common Request Parameters</a> page. The Action field for this API is GetMonitorData.

### 2.1 Input Parameters

| Parameter Name               | Required   | Type       | Input Content           | Description                                       |
| ------------------ | ---- | -------- | -------------- | ---------------------------------------- |
| namespace          | Yes    | String   | qce/cvm | Namespace. Every cloud product has a namespace. For more information, please see Input Content column.          |
| metricName         | Yes    | String   | Specific metric name        | Metric name. For more information, please see 2.2                            |
| dimensions.0.name  | Yes    | String   | topicId        | Input parameter is CMQ topic instance id                            |
| dimensions.0.value | Yes    | String   | Specific CMQ topic instance id  | Enter specific qtopicId, such as topic-i4p4k0u0            |
| dimensions.1.name  | Yes    | String   | subscriptionId | Input parameter is CMQ subscription instance id                            |
| dimensions.1.value | Yes    | String   | Specific CMQ subscription instance id  | Enter specific subscriptionId, such as test1               |
| period             | No    | Int      | 60/300       | Interval for collecting monitoring data. Most metrics support a statistical granularity of 60s while some metrics only support a statistical granularity of 300s. Statistical granularity varies with metrics. Enter parameters by referring to the list of metric details in section 2.2. |
| startTime          | No    | Datetime | Start time           | Start time, such as "2016-01-01 10:25:00". Default is "00:00:00" of the current day |
| endTime            | No    | Datetime | End time           | End time. It is the current time by default. endTime cannot be earlier than startTime       |

### 2.2 Metric Name

| Metric Name                     | Description          | Unit   | Dimension                     |
| ------------------------ | ----------- | ---- | ---------------------- |
| NumOfMsgPublished        | Number of published messages    | -    | topicId                |
| NumOfMsgBatchPublished   | Number of messages published in batches  | -    | topicId                |
| CountOfMsgPublished      | Number of requests for publishing messages   | -    | topicId                |
| CountOfMsgBatchPublished | Number of requests for batch publishing of messages | -    | topicId                |
| PublishSize              | Size of published messages    | MB   | topicId                |
| BatchPublishSize         | Size of messages published in batches  | MB   | topicId                |
| NumOfNotify              | Total number of delivered messages    | -    | topicId, subscriptionId |
| NumOfSuccNotify          | Total number of messages delivered successfully   | -    | topicId, subscriptionId |


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
&namespace=qce/cmqtopic
&metricName=NumOfMsgPublished
&dimensions.0.name=topicId
&dimensions.0.value=topic-06c1jrku
&startTime=2016-06-28 14:10:00
&endTime=2016-06-28 14:20:00
</pre>

Output

```
{
    "code": 0,
    "message": "",
    "metricName": "NumOfMsgPublished",
    "startTime": "2016-06-28 14:10:00",
    "endTime": "2016-06-28 14:20:00",
    "period": 300,
    "dataPoints": [
        50,
        35,
        20
    ]
}
```
