<font style="color:Brown">The API GetCdnStatTop is used to query the TOP provinces, TOP operators and TOP URLs by traffic/number of requests based on the input parameter statType. This document describes the TOP query by number of requests.</font>

## API Description

**GetCdnStatTop** is used to query the TOP 100 URLs, TOP provinces and TOP operators of domain names/projects by number of requests within the specified time period.

Domain name for API request: <font style="color:red">cdn.api.qcloud.com</font>

**Notes:**

+ You can submit multiple domain names at a time to query the rankings of TOP 100 URLs, TOP provinces and TOP operators by number of requests. projectId is required.
+ You can submit multiple projects at a time to query the rankings of TOP 100 URLs, TOP provinces and TOP operators by the total number of requests.
+ The TOP data is calculated and obtained from logs with a latency of about 30 minutes.
+ You can query the TOP data within 90 days.
+ The frequency of calling the API is limited to 100/min.

[View the example](https://cloud.tencent.com/document/product/228/1734)

## Input Parameters
The following request parameter list only provides the API request parameters. Common request parameters are required when the API is called. For more information, please see [Common Request Parameters](https://cloud.tencent.com/doc/api/231/4473) page. The Action field for this API is GetCdnStatTop.

| Parameter Name | Required | Type | Description |
| ---------- | ---- | ------ | ---------------------------------------- |
| startDate  | Yes    | String | Start time (day) of the query                              |
| endDate    | Yes    | String | End time (day) of the query                                |
| projects.n | Yes | String | Project ID. [View Project ID](https://console.cloud.tencent.com/project) |
| hosts.n | No | String | Domain name |
| statType | Yes | String | "requests" indicates that it is sorted by the number of requests |


## Output Parameters

| Parameter Name | Type | Description |
| -------- | ------ | ---------------------------------------- |
| code | Int | Common error code. 0: Successful; other values: Failed.<br/>For more information, please see [Common Error Codes](https://cloud.tencent.com/doc/api/231/5078#1.-.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81) on the Error Codes page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Error message or error code at business side.<br/>For more information, please see [Business Error Codes](https://cloud.tencent.com/document/product/228/5078#2.-.E6.A8.A1.E5.9D.97.E9.94.99.E8.AF.AF.E7.A0.81) on the Error Codes page. |
| data | Array | Returned result. For more information, please see the description below |

### "data" is composed as follows:

#### data

| Name | Type | Description |
| -------------- | ------ | ---------------- |
| province_data | Array | Ranking of provinces. Structure is described below |
| isp_data | Array | Ranking of operators. Structure is described below |
| url_data | Array | Ranking of URLs. Structure is described below |
| start_datetime | String | Start date |
| end_datetime | String | End date |
| statType | String | "requests" refers to the ranking of the number of requests |
| period | Int | Time granularity |

#### province_data

| Name | Type | Description |
| ----- | ------ | ------------ |
| id | Int | Province ID |
| name | String | Province name, such as "Jilin" |
| value | Int | The number of requests, unit is count |

#### isp_data

| Name | Type | Description |
| ----- | ------ | ------------- |
| id | Int | Operator ID |
| name | String | Operator name, such as "China Mobile" |
| value | Int | The number of requests, unit is count |

#### url_data

| Name | Type | Description |
| ----- | ------ | ------------ |
| name | String | URL |
| value | Int | The number of requests |

## Example

### Sample Parameters

```
startDate: 20160503
endDate: 20160504
projects.0: 0
hosts.0: www.test.com
statType: requests
```

### GET Request

For a GET request, all the parameters are required to be appended to the URL:

```
https://cdn.api.qcloud.com/v2/index.php?
Action=GetCdnStatTop
&SecretId=XXXXXXXXXXXXXXXXXXXXXXXXX
&Timestamp=1462421433
&Nonce=123456789
&Signature=XXXXXXXXXXXXXXXXXXXXXXXX
&startDate=20160503
&endDate=20160504
&hosts.0=www.test.com
&projects.0=0
&statType=requests
```

### POST Request

For a POST request, the parameters are input in HTTP Request-body. The request address is:

```
https://cdn.api.qcloud.com/v2/index.php
```

Formats such as form-data and x-www-form-urlencoded are supported for the parameters. The array of parameters is as follows:

```
array (
  'Action' => 'GetCdnStatTop',
  'SecretId' => 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX',
  'Timestamp' => 1462782282,
  'Nonce' => 123456789,
  'Signature' => 'XXXXXXXXXXXXXXXXXXXXXXXX',
  'startDate' => '20160503',
  'endDate' => '20160504',
  'projects.0' => '0',
  'hosts.0' => 'www.test.com',
  'statType' => 'requests'
)
```

### Example of Result

```json
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "start_datetime": "2016-05-03",
        "end_datetime": "2016-05-04",
        "stat_type": "requests",
        "period": 5,
        "province_data": [
            {
                "id": 1051,
                "name": "Chongqing",
                "value": 207
            }
          ...
        ],
        "isp_data": [
            {
                "id": 2,
                "name": "China Telecom",
                "value": 207
            }
          ...
        ],
        "url_data": [
            {
                "name": "www.test.com/robots.txt",
                "value": 212
            },
            {
                "name": "www.test.com/",
                "value": 207
            }
        ]
    }
}
```


