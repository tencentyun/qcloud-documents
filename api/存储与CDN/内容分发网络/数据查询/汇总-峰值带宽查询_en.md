<font style="color:Brown">The API DescribeCdnHostInfo is used to query peak bandwidth, total traffic, total number of requests, and average hit rate of requests based on the input parameter statType. This document describes how to query peak bandwidth.</font>

## API Description

**DescribeCdnHostInfo** can be used to query the peak bandwidth within a specified time range for a domain name.

Domain name for API request: <font style="color:red">cdn.api.qcloud.com</font>

**Note:**

+ You can submit multiple domain names or projects at a time to query the peak bandwidth for the submitted domain names or the domain names under each project.
+ The statistic value of bandwidth is generated every 5 minutes, and the peak bandwidth is the largest value among the statistic values within the specified time range.
+ Start time is defined as a date. For example, if start time is set to 2017-11-29, the actual start time for query is 2017-11-29 00:00:00; if end time is set to 2017-11-29, the actual end time for query is 2017-11-29 23:55:00.
+ Parameter projectId is required to query the bandwidth for a domain name.
+ You can query the data with a time range of 90 days.
+ The frequency of calling the API is limited to 100/min.

[View the example](https://cloud.tencent.com/document/product/228/1734)

## Input Parameters
The following request parameter list only provides the API request parameters. Common request parameters are required when the API is called. For more information, please see [Common Request Parameters](https://cloud.tencent.com/doc/api/231/4473) page. The Action field for this API is DescribeCdnHostInfo.

| Parameter Name | Required | Type | Description |
| ---------- | ---- | ------ | ---------------------------------------- |
| startDate | Yes | String | Start date for the query, such as 2016-05-03 |
| endDate | Yes | String | End date for the query, such as 2016-05-04 |
| statType | Yes | String | Statistic type<br/>"bandwidth" indicates peak bandwidth |
| projects.n | Yes | String | Project ID. For more information, please see [View Project ID](https://console.cloud.tencent.com/project) |
| hosts.n | No | String | Domain name list |

### The parameters are as follows:

**Sample Parameters**

```
hosts.0=www.test1.com&hosts.1=www.test2.com
```

## Output Parameters

| Parameter Name | Type | Description |
| -------- | ------ | ---------------------------------------- |
| code | Int | Common error code. 0: Successful; other values: Failed.<br/>For more information, please see [Common Error Codes](https://cloud.tencent.com/doc/api/231/5078#1.-.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81) on the Error Codes page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Error message or error code at business side<br/>For more information, please see [Business Error Codes](https://cloud.tencent.com/document/product/228/5078#2.-.E6.A8.A1.E5.9D.97.E9.94.99.E8.AF.AF.E7.A0.81) on the Error Codes page. |
| data | Array | Returned result. For more information, please see the description below |

### "data" is composed as follows:

#### data

| Parameter Name | Type | Description |
| -------------- | ------ | -------------- |
| start_datetime | String | Start date |
| end_datetime | String | End date |
| period | Int | Time interval at which the data is sampled (in minute) |
| detail_data | Array | Summary data. For more information, please see the description below. |

#### detail_data

| Parameter Name | Type | Description |
| ---------- | ------ | ---------------------------------------- |
| host_name | String | Domain name |
| host_type | String | Domain name type<br/>"cname" indicates the domain name accessed to a self-owned origin<br/>"cos" indicates the domain name accessed to a COS origin |
| host_value | Int | Peak bandwidth (in bps) |

## Example

### Sample Parameters

```
startDate: 20160503
endDate: 20160504
projects.0: 0
statType: bandwidth
```

### GET Request

For a GET request, all the parameters are required to be appended to the URL:

```
https://cdn.api.qcloud.com/v2/index.php?
Action=DescribeCdnHostInfo
&SecretId=XXXXXXXXXXXXXXXXXXXXXXXXXXX
&Timestamp=1462781898
&Nonce=123456789
&Signature=XXXXXXXXXXXXXXXXXXXXXXXXXX
&startDate=20160503
&endDate=20160504
&statType=bandwidth
&projects.0=0
```

### POST Request

For a POST request, the parameters are input in HTTP Request-body. The request address is:

```
https://cdn.api.qcloud.com/v2/index.php
```

Formats such as form-data and x-www-form-urlencoded are supported for the parameters. The array of parameters is as follows:

```
array (
  'Action' => 'DescribeCdnHostInfo',
  'SecretId' => 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX',
  'Timestamp' => 1462782282,
  'Nonce' => 123456789,
  'Signature' => 'XXXXXXXXXXXXXXXXXXXXXXXX',
  'startDate' => '20160503',
  'endDate' => '20160504',
  'statType' => 'bandwidth',
  'projects.0' => '0'
)
```


### Example of Result

```json
{
    "retcode": 0,
    "errmsg": "ok",
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "start_datetime": "2016-05-03 00:00:00",
        "end_datetime": "2016-05-04 23:55:00",
        "period": 5,
        "stat_type": "bandwidth",
        "detail_data": [
            {
                "host_id": "www.test.com",
                "host_name": "www.test.com",
                "host_type": "cname",
                "host_value": 123456789
            },
            ...
        ]
    }
}
```
