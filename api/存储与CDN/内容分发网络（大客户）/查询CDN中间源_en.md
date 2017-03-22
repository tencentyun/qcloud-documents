## 1. API Description

This API (GetCdnMiddleSourceList) is used to query the list of all IPs of CDN intermediate nodes.

Domain for API request:<font style="color:red">cdn.api.qcloud.com</font>

## 2. Input Parameters

No input parameters are needed for this API



## 3. Output Parameters

| Parameter Name     | Type     | Description                                       |
| -------- | ------ | ---------------------------------------- |
| code     | Int    | Common error code; 0: Succeeded; other values: Failed. For more information, refer to [Common Error Codes](https://www.qcloud.com/doc/api/231/5078#1.-.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81) on Error Code page.  |
| message  | String | Module error message description depending on API.                           |
| codeDesc | String | Error message or error code at business side.                           |
| data     | Array  | Returned results; For details, refer to the description later.                          |

#### data Field Description

| Parameter Name               | Type    | Description      |
| ------------------ | ----- | ------- |
| middle_source_list | Array | List of IPs of intermediate nodes |



## 4. Example

### 4.1 GET Request

For GET request, all the parameters are required to be appended to the URL:

```
https://cdn.api.qcloud.com/v2/index.php?
Action=GetCdnMiddleSourceList
&SecretId=XXXXXXXXXXXXXXXXXXXXXX
&Timestamp=1462431364
&Nonce=123465789
&Signature=XXXXXXXXXXXXXXXXXX
```

### 4.2 POST Request

For POST request, the parameters need to be filled in HTTP Request-body. Request address:

```
https://cdn.api.qcloud.com/v2/index.php
```

Formats such as form-data and x-www-form-urlencoded are supported. The array of parameters is as follows:

```
array (
  'Action' => 'GetCdnMiddleSourceList',
  'SecretId' => 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
  'Timestamp' => 1462866050,
  'Nonce' => 1130670281,
  'Signature' => 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
)
```





### 4.3 Example of Returned Result

```json
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "middle_source_list": [
		"1.1.1.1",
        "2.2.2.2",
        ...
        ]
    }
}
```






