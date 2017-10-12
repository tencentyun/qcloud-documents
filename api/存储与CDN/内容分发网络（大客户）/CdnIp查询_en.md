## 1. API Description
This API (QueryCdnIp) is used to query whether specified IP is a CDN node.

Domain for API request:<font style="color:red">cdn.api.qcloud.com</font>

**Note:**
+ Query for multiple IPs is supported, and a maximum of 20 IPs are allowed to be queried at a time;


## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters are required when the API is called. For more information, refer to [Common Request Parameters](https://cloud.tencent.com/doc/api/231/4473). The Action field for this API is QueryCdnI.

| Parameter Name | Required | Type     | Description |
| ---- | ---- | ------ | ----------------- |
| ips  | Yes    | String | IP to be queried. You may query one or more IPs |


**Note:**

+ For the query for multiple IPs, the IPs need to be separated with commas, as shown below:
```
ips=1.1.1.1,2.2.2.2
```

## 3. Output Parameters
| Parameter Name     | Type     | Description                                       |
| -------- | ------ | ---------------------------------------- |
| code     | Int    | Common error code; 0: Succeeded; other values: Failed. For more information, refer to [Common Error Codes](https://cloud.tencent.com/doc/api/231/5078#1.-.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81) on Error Code page.  |
| message  | String | Module error message description depending on API.                           |
| codeDesc | String | Error message or error code at business side.                           |
| data     | Object | Returned data result                                   |

**data Field Description**

| Parameter Name             | Type   | Description |
| ---------------- | ----- | -------------- |
| last_update_time | int   | The last update time for Unix |
| list             | Array | The array of query results         |

**list Field Description**

| Parameter Name      | Type     | Description                            |
| --------- | ------ | ----------------------------- |
| ip        | String | IP to be queried                         |
| platform  | String | Whether it is a CDN node. The value is "yes" or "no" |
| prov_name | String | The province in which the node resides                        |
| isp_name  | String | The ISP of node                         |

## 4. Example
### 4.1 Input Example
> ips: 1.1.1.1,2.2.2.2

### 4.2 GET Request
For GET request, all the parameters are required to be appended to the URL (commas are transcoded):
```
https://cdn.api.qcloud.com/v2/index.php?
Action=QueryCdnIp
&SecretId=XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
&Timestamp=1462436277
&Nonce=123456789
&Signature=XXXXXXXXXXXXXXXXXXXXX
&ips=1.1.1.1%2C2.2.2.2
```

### 4.2 POST Request
For POST request, the parameters are filled in HTTP Requestbody. The request address is:
```
https://cdn.api.qcloud.com/v2/index.php
```
Such formats as formdata and xwwwformurlencoded are supported for the parameters. The array of parameters is as follows:

```
array (
	'Action' => 'QueryCdnIp',
	'SecretId' => 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX',
	'Timestamp' => 1462782282,
	'Nonce' => 123456789,
	'Signature' => 'XXXXXXXXXXXXXXXXXXXXXXXX',
	'ips' => '1.1.1.1,2.2.2.2'
)
```

### 4.3 Response Example
Note: IP in the example is only for reference.
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "last_update_time": 1477987948,
        "list": [
            {
                "ip": "2.2.2.2",
                "platform": "yes",
                "prov_name": "Guangdong",
                "isp_name": "China Telecom"
            },
            {
                "ip": "1.1.1.1",
                "platform": "no",
                "prov_name": "Unknown",
                "isp_name": "Unknown"
            }
        ]
    }
}
```



