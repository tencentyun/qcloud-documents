## 1. API Description

This API (GetCdnHostsLogStat) is used to query the statistical data on bandwidth produced in logs under specified domain (project) on specified date.

Domain for API request:<font style="color:red">cdn.api.qcloud.com</font>

<font style="color:orange">The data calculated through logs is application layer data and is different from NIC statistical data. This API can adjust the scaling level based on customer's need and billing method. The scaling level will not be raised by default.</font>

**Note:**

+ Query for the detailed bandwidth data of one or multiple domains is supported, with the time granularity being 5 minutes. There are 288 statistical points each day;
+ Query for the detailed bandwidth data of each domain under one or multiple projects is supported;
+ If query is made without specifying domain and project parameters, detailed data of all domains of the user will be returned by default;
+ If a date is specified, 288 statistical points will be returned. The first point is 00:00:00, which represents the bandwidth values between 23:55:00 and 00:00:00;
+ The API has a frequency limit of 100/minutes.

## 2. Input Parameters

The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to [Common Request Parameters](https://www.qcloud.com/doc/api/231/4473). The Action field for this API is GetCdnHostsLogStat.

| Parameter Name    | Required | Type     | Description                                       |
| ------- | ----------- | ------ | -------------------- |
| date     | Yes    | String | The date for which the query is made. Format: yyyy-mm-dd. For example, 2016-09-28                    |
| hosts.n | No | String | Domain. Multiple domains are supported, such as hosts.0=www.test.com&hosts.1=www.test2.com. When you query a domain, you need to enter the project ID. [Click to View](https://console.qcloud.com/project) |
| projects.n | No | String | Project ID. Multiple IDs are supported, such as projects.0=1&projects.1=2  |




## 3. Output Parameters

| Parameter Name     | Type     | Description                                       |
| -------- | ------ | ---------------------------------------- |
| code     | Int    | Common error code; 0: Succeeded; other values: Failed. For more information, refer to [Common Error Codes](https://www.qcloud.com/doc/api/231/5078#1.-.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81) on Error Code page.  |
| message  | String | Module error message description depending on API.                           |
| codeDesc | String | Error message or error code at business side.                           |
| data     | Object | Statistical data                         |


## 4. Example

### 4.1 Input Example

> date: 2016-11-25
> hosts.0: www.test.com
> projects.0: 0

### 4.2 GET Request

For GET request, all the parameters are required to be appended to the URL:

```
https://cdn.api.qcloud.com/v2/index.php?
Action=GetCdnHostsLogStat
&SecretId=XXXXXXXXXXXXXXXXXXXXXX
&Timestamp=1462416887
&Nonce=123456789
&Signature=XXXXXXXXXXXXXXXXXX
&date=2016-11-25
&hosts.0=www.test.com
&projects.0=0
```

### 4.3 POST Request

For POST request, the parameters need to be filled in HTTP Request-body. Request address:

```
https://cdn.api.qcloud.com/v2/index.php
```

Formats such as form-data and x-www-form-urlencoded are supported. The array of parameters is as follows:

```
array (
  'Action' => 'GetCdnHostsLogStat',
  'SecretId' => 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX',
  'Timestamp' => 1462782282,
  'Nonce' => 123456789,
  'Signature' => 'XXXXXXXXXXXXXXXXXXXXXXXX',
  'date' => '2016-11-25',
  'hosts.0' => 'www.test.com',
  'projects.0' => '0'
)

```

### 4.4 Example of Returned Result

```json
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
 		"2016-11-25":{
        	"www.test.com":[
            	1,
                1,
                0,
                ...
            ]
        }
    }
}
```
























