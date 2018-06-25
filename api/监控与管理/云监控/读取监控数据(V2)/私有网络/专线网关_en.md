## 1. API Description

Domain name: monitor.api.qcloud.com


Direct Connect traffic entry for VPC can have the interconnection with different IDCs by connecting to multiple Direct Connect tunnels.

This API (GetMonitorData) is used to query the monitoring data of direct connect gateway product. The values for input parameters are as follows:
namespace: qce/dcg
dimensions.0.name=directConnectGatewayId
dimensions.0.value is direct connect gateway ID.

## 2. Input Parameters

The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see <a href="/doc/api/405/公共请求参数" title="Common Request Parameters">Common Request Parameters</a> page. The Action field for this API is GetMonitorData.

### 2.1 Input Parameters

| Parameter Name               | Required   | Type       | Input Content                   | Description                                       |
| ------------------ | ---- | -------- | ---------------------- | ---------------------------------------- |
| namespace          | Yes    | String   | qce/cvm    | Namespace. Every Tencent Cloud product has a namespace. For more information, please see Input Content column.           |
| metricName         | Yes    | String   | Specific metric name                | Metric name. For more information, please see 2.2                            |
| dimensions.0.name  | Yes | String   | directConnectGatewayId | Input parameter is direct connect gateway ID                                |
| dimensions.0.value | Yes    | String   | Specific direct connect gateway ID              | Enter specific directConnectGatewayId               |
| period             | No    | Int      | 60/300     | Interval for collecting monitoring data. Most metrics support a statistical granularity of 60s while some metrics only support a statistical granularity of 300s. Statistical granularity varies with metrics. Enter parameters by referring to the list of metric details in section 2.2. |
| startTime          | No    | Datetime | Start time       | Start time, such as "2016-01-01 10:25:00". Default is "00:00:00" of the current day |
| endTime            | No    | Datetime | End time                   | End time. It is the current time by default. endTime cannot be earlier than startTime.       |

### 2.2 Metric Name

| Metric name         | Description    | Unit   | Dimension                     |
| ------------ | ----- | ---- | ---------------------- |
| outbandwidth | Public network outbound bandwidth | Mbps | directConnectGatewayId |
| inbandwidth  | Public network inbound bandwidth | Mbps | directConnectGatewayId |
| outpkg       | Outbound packets   | Packets/sec  | directConnectGatewayId |
| inpkg        | Inbound packets   | Packets/sec  | directConnectGatewayId |


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
&namespace=qce/dcg
&metricName=inpkg
&dimensions.0.name=directConnectGatewayId
&dimensions.0.value=dcg-4d545d
&startTime=2016-06-28 14:10:00
&endTime=2016-06-28 14:20:00
</pre>

Output

```
{
    "code": 0,
    "message": "",
    "metricName": "inpkg",
    "startTime": "2016-06-28 14:10:00",
    "endTime": "2016-06-28 14:20:00",
    "period": 60,
    "dataPoints": [
        30,
        35,
        40
    ]
}
```
