## API Description
### Description

This API (GetMonitorData) is used to obtain monitoring data of serverless cloud functions. Monitoring data can be obtained based on the function name specified by the user.

### Domain name for API
Domain name for API request: `monitor.api.qcloud.com`

## Request
Syntax:
```
GET https://monitor.api.qcloud.com/v2/index.php?Action=GetMonitorData
    &<Common request parameters>
    &namespace=qce/scf
    &metricName=duration
    &dimensions.0.name=functionName
    &dimensions.0.value=test
    &startTime=2017-07-24 14:00:00
    &endTime=2017-07-24 14:05:00
    &period=300
```

### Input Parameters
The following request parameter list only provides the API request parameters. Common request parameters are required when the API is called. For more information, see [Common Request Parameters](/doc/api/244/4183). The Action field for this API is GetMonitorData.

| Parameter | Description | Type | Required | 
|-----------|--------|----------|----------|
| namespace | Namespace. Every Tencent Cloud product has a namespace. The namespace of the serverless cloud function is `qce/scf`. | String | Yes |
| metricName | Metric name. The specific monitor metrics to be obtained, such as duration for the run time, and invocation for the number of calls | String | Yes |
| dimensions.n.name | Dimension name. The serverless cloud function has only one dimension: functionName, which is used in combination with dimensions.n.value. | String | Yes | 
| dimensions.n.value | The corresponding value of a dimension name. | String | Yes |
| startTime | Start time, such as "2017-01-01 00:00:00". Default is "00:00:00" of the current day. | Datetime | No | 
| endTime | End time, such as "2017-01-01 10:00:00". Default is the current time. <br>**Note: startTime must be earlier than endTime. It is recommended that endTime and startTime be on the same day. | Datetime | No |
| period | Interval for collecting monitoring data. The supported granularities are 60s and 300s. Default is 300s if it is not specified. | Int | No |

`metricName` list for the serverless cloud function is as follows:

| Metric name | Description | Unit |
|---------|---------|---------|
| duration | Run time | Milliseconds (ms) |
| invocation | The number of calls | - |
| error | The number of error calls | - |

The serverless cloud function only supports the dimension of cloud function name, as described below:
This dimension reflects the monitoring metric of a cloud function. The dimension (dimensions.n.name) to be specified is as follows:

| Dimension | Description | Format |
|---------|---------|---------|
| functionName | The name of a serverless cloud function | string |

If you want to query the monitoring data of a cloud function named "test" in a specified run time (duration), see the following API request example:
```
GET https://monitor.api.qcloud.com/v2/index.php?Action=GetMonitorData
    &<Common request parameters>
    &namespace=qce/scf
    &metricName=duration
    &dimensions.0.name=functionName
    &dimensions.0.value=test
```

## Response
Response Example:
```
{
    "code": 0,
    "message": "",
    "metricName": "duration",
    "startTime": "2017-07-24 14:00:00",
    "endTime": "2017-07-24 14:05:00",
    "period": 300,
    "dataPoints":  [
        0.65213,
        0.5586
    ]
}
```

## Response Parameters

| Parameter | Description | Type |
| --- | --- | --- |
| code | Common error code. 0: Successful; other values: Failed. For more information, please see [Common Error Codes](https://cloud.tencent.com/doc/api/244/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81) on the Error Codes page. | Int | 
| codeDesc | Description | String |
| message | Error message details | String |
| startTime | Start time | Datetime | 
| endTime | End Time | Datetime | 
| metricName | Metric name | String |
| period | Interval for collecting monitoring data | Int | 
| dataPoints | Monitoring data list. Each element of the array stands for the data read at the monitoring time point. | Object |

## Practical Case

### Request
```
GET https://monitor.api.qcloud.com/v2/index.php?
    Action=GetMonitorData
    &SecretId=AKIDutrojKl3CKQZNAr763UXks05898Lmciu
    &Nonce=62089
    &Timestamp=1505804102
    &Region=gz
    &Signature=LWI%2BdudHPe56OYcsvKWiXImdO5s%3D
    &namespace=qce%2Fscf
    &metricName=duration
    &dimensions.0.name=functionName
    &dimensions.0.value=test5
    &startTime=2017-09-19+12%3A00%3A00
    &endTime=2017-09-19+14%3A05%3A00
    &period=300

```
### Response
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "metricName": "duration",
    "startTime": "2017-09-19 12:00:00",
    "endTime": "2017-09-19 14:05:00",
    "period": "300",
    "dataPoints": [
        2.983,
        1.131,
        0.732,
        0.773,
        0.921,
        0.901,
        0.775,
        0.931,
        0.812,
        0.757,
        1.06,
        0.805,
        0.834,
        0.812,
        0.881,
        0.807,
        0.831,
        0.992,
        0.793,
        1.968,
        0.868,
        0.93,
        6.365,
        0.732,
        0.836,
        1.433
    ]
}
```
