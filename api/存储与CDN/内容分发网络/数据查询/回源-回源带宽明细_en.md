<font style="color:Brown">The API GetCdnOriginStat is used to query origin-pull bandwidth, origin-pull traffic, the number of origin-pull requests, the number of failed origin-pull requests, and origin-pull failure rate based on the input parameter statType. This document describes how to query the details of origin-pull bandwidth.</font>

## API Description

**GetCdnOriginStat** is used to query the details of origin-pull bandwidth within a specified time period for a domain name.

Domain name for API request: <font style="color:red">cdn.api.qcloud.com</font>

**Notes:**

+ You can submit a maximum of 20 domain names at a time to query the real-time origin-pull bandwidth for each domain name.
+ The statistic value of the origin-pull bandwidth is generated at an interval of 5 minutes, with the delay of real-time data being 5-10 minutes.
+ You can query the data with a time range of 60 days between a start and end time (inclusive).
+ By default, the data granularity is 5 minutes for the data within a time range of 3 days, 1 hour for the data within 4-7 days (peak bandwidth), and 1 day for the data within 8 or more days (daily peak bandwidth).
+ The frequency of calling the API is limited to 100/min.


[View the example](https://cloud.tencent.com/document/product/228/1734)

## Input Parameters
The following request parameter list only provides the API request parameters. Common request parameters are required when the API is called. For more information, please see [Common Request Parameters](https://cloud.tencent.com/doc/api/231/4473) page. The Action field for this API is GetCdnOriginStat.

| Parameter Name | Required | Type | Description |
| --------- | ---- | ------ | ---------------------------------------- |
| startTime | Yes | String | Start time for the query |
| endTime | Yes | String | End time for the query |
| hosts.n | No | String | Domain name |
| statType | Yes | String | Statistical type <br/>"bandwidth": origin-pull bandwidth |
| detail | No | String | Time granularity <br/>"1": data with a granularity of 5 minutes is returned<br/> Other: data is returned according to the default rule |

## Output Parameters

| Parameter Name | Type | Description |
| -------- | ------ | ---------------------------------------- |
| code | Int | Common error code. 0: Successful; other values: Failed.<br/>For more information, please see [Common Error Codes](https://cloud.tencent.com/doc/api/231/5078#1.-.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81) on the Error Codes page. |
| message  | String | Module error message description depending on API                           |
| codeDesc | String | Error message or error code at business side.<br/>For more information, please see [Business Error Codes](https://cloud.tencent.com/document/product/228/5078#2.-.E6.A8.A1.E5.9D.97.E9.94.99.E8.AF.AF.E7.A0.81) on the Error Codes page. |
| data | Array | Returned result. For more information, please see the description below |

### "data" is composed as follows:

#### data

| Name | Type | Description |
| -------------- | ------ | ---------------- |
| start_datetime | String | Start time |
| end_datetime | String | End time |
| period | String | Time granularity |
| bandwidth | Array | Details of origin-pull bandwidth, in bps |

## Example

### Sample Parameters

```
startTime: 2017-10-28 00:00:00
endTime: 2017-10-28 01:05:00
hosts.0: www.test.com
statType: bandwidth
```

### GET Request

For a GET request, all the parameters are required to be appended to the URL:

```
https://cdn.api.qcloud.com/v2/index.php?
Action=GetCdnOriginStat
&SecretId=XXXXXXXXXXXXXXXXXXXXXXXXXXX
&Timestamp=1462422547
&Nonce=12345678
&Signature=XXXXXXXXXXXXXXXXXXXXXXXXX
&startTime=2017-10-28+00%3A00%3A00
&endDate=2017-10-28+00%3A05%3A00
&hosts.0=www.test.com
&statType=bandwidth
```

### POST Request

For a POST request, the parameters are input in HTTP Request-body. The request address is:

```
https://cdn.api.qcloud.com/v2/index.php
```

Formats such as form-data and x-www-form-urlencoded are supported for the parameters. The array of parameters is as follows:

```
array (
  'Action' => 'GetCdnOriginStat',
  'SecretId' => 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX',
  'Timestamp' => 1462782282,
  'Nonce' => 123456789,
  'Signature' => 'XXXXXXXXXXXXXXXXXXXXXXXX',
  'startTime' => '2017-10-28 00:00:00',
  'endTime' => '2017-10-28 00:05:00',
  'hosts.0' => 'www.test.com',
  'statType' => 'bandwidth'
)
```

### Example of Result

```json
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "period": 5,
        "start_datetime": "2017-10-28 00:00:00",
        "end_datetime": "2017-10-28 00:05:00",
        "bandwidth": {
            "www.test.com": [
                1234567,
                7605898
            ]
        }
    }
}
```


