## 1. API Description

This API (GetCdnHostsHyStat) is used to query the back-to-origin bandwidth/traffic data of a domain.

Domain for API request:<font style="color:red">cdn.api.qcloud.com</font>

**Note:**

+ Query by specified date is supported. And query for the real-time data on current date is supported too, with a data latency being about 5 minutes;
+ Query for back-to-origin bandwidth/traffic details of every domain under specified project is supported;
+ Query for back-to-origin bandwidth/traffic details of specified domain is supported.


## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to [Common Request Parameters](https://www.qcloud.com/doc/api/231/4473). The Action field for this API is GetCdnHostsHyStat.

| Parameter Name       | Required | Type     | Description                                       |
| ---------- | ---- | ------ | ---------------------------------------- |
| date       | Yes    | String | Specify the date for which the query is made. Format: yyyy-mm-dd. For example, 2016-10-13.
| projects.n | No    | int    | Specify the project ID for which the query is made. Multiple IDs can be specified, such as projects.0=1&projects.1=2; [Click to View Project ID](https://console.qcloud.com/project) |
| hosts.n    | No    | String | Specify the domain for which the query is made. Multiple domains can be specified, such as hosts.0=www.abc.com&hosts.1=www.def.com. When you enter a domain, you need to enter the project ID of this domain in projects.n parameter. |
| statType   | Yes    | String | Specify statistics type. "Bandwidth" refers to bandwidth, with the returned data measured in bps; "flux" refers to traffic, with the returned data measured in Byte |

**Note:**

+ If both projects.n and hosts.n are not specified for query, the specified statistics type of detailed data for all domains under the user name will be returned by default;
+ The time granularity for statistical data is 5 minutes, and there are 288 statistical points each day;
+ The value at 2016-10-13 00:05:00 is equal to the sum of statistical data values between 00:00:00 and 00:04:59.


## 3. Output Parameters

| Parameter Name     | Type     | Description                                       |
| -------- | ------ | ---------------------------------------- |
| code     | Int    | Common error code; 0: Succeeded; other values: Failed. For more information, refer to [Common Error Codes](https://www.qcloud.com/doc/api/231/5078#1.-.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81) on Error Code page |
| message  | String | Module error message description depending on API                           |
| codeDesc | String | Error message or error code at business side                           |
| data     | Object | Returned result data, including the detailed data array for specified dates and domains                    |


## 4. Example

### 4.1 Input Example

> date: 2016-09-30
> statType: bandwidth

### 4.2 GET Request

For GET request, all the parameters are required to be appended to the URL:

```
https://cdn.api.qcloud.com/v2/index.php?
Action=GetCdnHostsHyStat
&SecretId=XXXXXXXXXXXXXXXXXXXXXXXXXXX
&Timestamp=1462422547
&Nonce=12345678
&Signature=XXXXXXXXXXXXXXXXXXXXXXXXX
&date=2016-09-30
&statType=bandwidth
```

### 4.3 POST Request

For POST request, the parameters need to be filled in HTTP Request-body. Request address:

```
https://cdn.api.qcloud.com/v2/index.php
```

Formats such as form-data and x-www-form-urlencoded are supported for the parameters. The array of parameters is as follows:

```
array (
  'Action' => 'GetCdnHostsHyStat',
  'SecretId' => 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX',
  'Timestamp' => 1462782282,
  'Nonce' => 123456789,
  'Signature' => 'XXXXXXXXXXXXXXXXXXXXXXXX',
  'date' => '2016-09-30',
  'statType' => 'bandwidth'
)
```

### 4.4 Example of Returned Result

```json
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "2016-09-30": {
        	"www.test.com":{
            	1,
                2,
                3,
                ...
            }
		}
    }
}
```


