## 1. API Description

Domain name: monitor.api.qcloud.com


BM provides load balance capacity.

This API (GetMonitorData) is used to query the monitoring data of BM load balancer listeners in public network. The values for input parameters are as follows:
namespace: qce/bm_lb
dimensions.0.name=protocol
dimensions.0.value (protocol value, such as tcp, udp)
dimensions.1.name=vip
dimensions.1.value (load balancer vip)
dimensions.2.name=vport
dimensions.2.value (load balancer port)

| Name       | Description    |
| -------- | ------- |
| protocol | Protocol      |
| vip      | Load balancer VIP |
| vport    | Load balancer port  |

## 2. Input Parameters

The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see <a href="/doc/api/405/公共请求参数" title="Common Request Parameters"> Common Request Parameters</a> page. The Action field for this API is GetMonitorData.

### 2.1 Input Parameters

| Parameter Name               | Required   | Type       | Input Content    | Description                                       |
| ------------------ | ---- | -------- | ------- | ---------------------------------------- |
| namespace          | Yes    | String   | qce/bm_lb  | Namespace. Every Tencent Cloud product has a namespace. For more information, please see Input Content column.           |
| metricName         | Yes    | String   | Specific metric name | Metric name. For more information, please see 2.2                            |
| dimensions.n.name  | Yes    | String   | Dimension name   | Dimension name, which is used in combination with dimensions.n.value. For more information, please see section 1. |
| dimensions.n.value | Yes    | String   | Dimension value   | Dimension value, which is used in combination with dimensions.n.name. For more information, please see section 1. |
| period             | No    | Int      | 60/300  | Interval for collecting monitoring data. Most metrics support a statistical granularity of 60s while some metrics only support a statistical granularity of 300s. Statistical granularity varies with metrics. Enter parameters by referring to the list of metric details in section 2.2. |
| startTime          | No    | Datetime | Start time    | Start time, such as "2016-01-01 10:25:00". Default is "00:00:00" of the current day |
| endTime            | No    | Datetime | End time    | End time. It is the current time by default. endTime cannot be earlier than startTime       |
### 2.2 Metric Name

| Metric Name                | Description   | Unit   | Dimension                 |
| ------------------- | ---- | ---- | ------------------ |
| listener_inpkg      | Inbound packets  | pck/sec  | protocol, vip, vport |
| listener_outpkg     | Outbound packets  | pck/sec  | protocol, vip, vport |
| listener_intraffic  | Inbound bandwidth  | Mbps | protocol, vip, vport |
| listener_outtraffic | Outbound bandwidth  | Mbps | protocol, vip, vport |

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
&namespace=qce/bm_lb
&metricName=listener_inpkg
&dimensions.0.name=protocol
&dimensions.0.value=tcp
&dimensions.1.name=vip
&dimensions.1.value=1.2.3.4
&dimensions.2.name=vport
&dimensions.2.value=80
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
    "period": 300,
    "dataPoints": [
        20,
        30,
        40
    ]
}
```

