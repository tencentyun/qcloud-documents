## 1. API Description

This API (GetCdnHostsDetailStat) is used to query the bandwidth consumption details of every domain under specified project on a specified date (288 statistical points per day), or the bandwidth consumption details of specified domain. Query for the bandwidth consumption details of edge nodes or intermediate nodes is supported.

Domain for API request:<font style="color:red">cdn.api.qcloud.com</font>


## 2. Input Parameters

The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to [Common Request Parameters](https://www.qcloud.com/doc/api/231/4473). The Action field for this API is GetCdnHostsDetailStat.

| Parameter Name    | Required | Type     | Description                                       |
| ------- | ---- | ------ | ---------------------------------------- |
| date     | Yes    | String | The date for which the query is made. Format: yyyy-mm-dd. For example, 2016-09-28                    |
| projects.n | No | String | Project ID for which the query is made. [Click to VIew Project ID](https://console.qcloud.com/project) |
| hosts.n | No    | String | Domain for which the query is made. |
| sources.n  | No    | String | Network layer for which the query is made. |

**Note:**

- date: This is the date for which the query is made. The query only applies to the data within the last 90 days. For example, if the date is set to 2016-05-03, the data between 2016-05-03 00:00:00 and 2016-05-03 23:55:00 will be queried.
- projects.n: Used to specify project ID. Multiple IDs can be specified, for example, projects.0=123&projects.1=456. The default project ID is 0, which means the consumption details of all domains under the specified project will be returned;
- hosts.n: Used to specify domain. Multiple domains can be specified, for example, hosts.0=www.test1.com&hosts.1=www.test2.com. The returned result is the bandwidth consumption details of each specified domain on specified date. The time granularity is 5 minutes, and there are a total of 288 statistical points each day (measured in bps). When you enter a domain name, you need to specify the project ID of this domain;
- If both projects.n and hosts.n are left empty, the query results will be the bandwidth consumption details of all the domains;
- sources.n: The data source. oc refers to edge node, and middle refers to intermediate node. It can be either oc or middle, or both. The default is oc.


## 3. Output Parameters

| Parameter Name     | Type     | Description                                       |
| -------- | ------ | ---------------------------------------- |
| code     | Int    | Common error code; 0: Succeeded; other values: Failed. For more information, refer to [Common Error Codes](https://www.qcloud.com/doc/api/231/5078#1.-.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81) on the Error Code page.  |
| message  | String | Module error message description depending on API.                           |
| codeDesc | String | Error message or error code at business side.                           |
| data     | Object | Data result. For details, refer to the description later.                            |

## 4. Example

### 4.1 Input Example

> date: 2016-09-28
> projects.0:0
> hosts.0: www.test.com

### 4.2 GET Request

For GET request, all the parameters are required to be appended to the URL:

```
https://cdn.api.qcloud.com/v2/index.php?
Action=GetCdnHostsDetailStat
&SecretId=XXXXXXXXXXXXXXXXXXXXXX
&Timestamp=1462416887
&Nonce=123456789
&Signature=XXXXXXXXXXXXXXXXXX
&date=2016-09-28
&projects.0=0
&hosts.0=www.test.com
```

### 4.3 POST Request

For POST request, the parameters need to be filled in the HTTP Request-body. Request address:

```
https://cdn.api.qcloud.com/v2/index.php
```

Formats such as form-data and x-www-form-urlencoded are supported for the parameters. The array of parameters is as follows:

```
array (
  'Action' => 'GetCdnHostsDetailStat',
  'SecretId' => 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX',
  'Timestamp' => 1462782282,
  'Nonce' => 123456789,
  'Signature' => 'XXXXXXXXXXXXXXXXXXXXXXXX',
  'date' => '2016-09-28',
  'projects.0' => '0',
  'hosts.0' => 'www.test.com'
)

```

### 4.4 Example of Returned Result

```json
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data":{
        "2016-09-28":{
            "www.test.com":[
            	0,
            	0,
            	...
            	0
            ]
        }
    }
}
```
























