## 1. API Description

Domain name: monitor.api.qcloud.com


This API (GetMonitorData) is used to query the monitoring data of BM EIP. The values for input parameters are as follows:
namespace: qce/bm_lb
dimensions.0.name=vip
dimensions.0.value (address of EIP to be queried)

| Name   | Description                                     |
| ---- | ---------------------------------------- |
| vip | EIP address. The list of EIPs applied by your account can be viewed using the API [DescribeEipBm](https://cloud.tencent.com/document/product/386/6671) for querying EIP list |

## 2. Input Parameters

The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see <a href="/doc/api/405/公共请求参数" title="Common Request Parameters"> Common Request Parameters</a> page. The Action field for this API is GetMonitorData.

### 2.1 Input Parameters

| Parameter Name               | Required   | Type       | Input Content           | Description                                       |
| ------------------ | ---- | -------- | -------------- | ---------------------------------------- |
| namespace          | Yes    | String   | qce/bm_lb        | Namespace. Every Tencent Cloud product has a namespace. For more information, please see Input Content column.           |
| metricName         | Yes    | String   | Specific metric name        | Metric name. For more information, please see 2.2                            |
| dimensions.0.name  | Yes   | String   | vip            | Input parameter is the address of EIP to be queried                          |
| dimensions.0.value | Yes    | String   | Address of EIP to be queried | Enter specific vip                                  |
| period             | No    | Int      | 60/300         | Interval for collecting monitoring data. Most metrics support a statistical granularity of 60s while some metrics only support a statistical granularity of 300s. Statistical granularity varies with metrics. Enter parameters by referring to the list of metric details in section 2.2. |
| startTime          | No    | Datetime | Start time           | Start time, such as "2016-01-01 10:25:00". Default is "00:00:00" of the current day |
| endTime            | No    | Datetime | End time           | End time. It is the current time by default. endTime cannot be earlier than startTime       |

### 2.2 Metric Name
> For now, the statistical period (the parameter "period") for BM EIP monitoring dimension is 300 seconds. Data collection with a finer granularity is not supported.

| Metric Name           | Description    | Unit   | Dimension   |
| -------------- | ----- | ---- | ---- |
| eip_outtraffic | Public network outbound bandwidth | Mbps | vip  |
| eip_intraffic  | Public network inbound bandwidth | Mbps | vip  |
| eip_outpkg     | Public network outbound packets | pck/sec  | vip |
| eip_inpkg      | Public network outbound packets | pck/sec  | vip  |


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
&metricName=eip_outpkg
&dimensions.0.name=vip
&dimensions.0.value=115.115.115.115
&startTime=2016-06-28 14:10:00
&endTime=2016-06-28 14:20:00
&period=300
</pre>

Output

```
{
    "code": 0,
    "message": "",
    "metricName": "eip_outpkg",
    "startTime": "2016-06-28 14:10:00",
    "endTime": "2016-06-28 14:20:00",
    "period": 300,
    "dataPoints": [
        30,
        35,
        40
    ]
}
```
