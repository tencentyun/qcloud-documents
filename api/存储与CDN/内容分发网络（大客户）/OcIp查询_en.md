## 1. API Description
This API (GetCdnIps) is used to query all the edge node IPs of specified domain on the Tencent Cloud CDN resource platform.

Domain for API request:<font style="color:red">cdn.api.qcloud.com</font>

<font color="orange">This is a highly data-sensitive API. Please ensure the data security.</font>

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to [Common Request Parameters](https://www.qcloud.com/doc/api/231/4473). The Action field for this API is GetCdnIps.

| Parameter Name | Required | Type     | Description |
| ---- | ---- | ------ | ----------------- |
| host  | Yes    | String | Domain to be queried|

**Note**

+ The resource platform for each domain varies, so the edge node IPs that are pulled may be inconsistent.

## 3. Output Parameters
| Parameter Name     | Type     | Description                                       |
| -------- | ------ | ---------------------------------------- |
| code     | Int    | Common error code; 0: Succeeded; other values: Failed. For more information, refer to [Common Error Codes](https://www.qcloud.com/doc/api/231/5078#1.-.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81) on Error Code page.  |
| message  | String | Module error message description depending on API.                           |
| codeDesc | String | Error message or error code at business side.                           |
| data     | Object | Returned data result; IP list                               |


## 4. Example
### 4.1 Input Example
> host=www.test.com

### 4.2 GET Request
For GET request, all the parameters are required to be appended to the URL (commas are transcoded):
```
https://cdn.api.qcloud.com/v2/index.php?
Action=GetCdnIps
&SecretId=XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
&Timestamp=1462436277
&Nonce=123456789
&Signature=XXXXXXXXXXXXXXXXXXXXX
&host=www.test.com
```

### 4.2 POST Request
For POST request, the parameters are filled in HTTP Requestbody. The request address is:
```
https://cdn.api.qcloud.com/v2/index.php
```
Such formats as formdata and xwwwformurlencoded are supported for the parameters. The array of parameters is as follows:

```
array (
	'Action' => 'GetCdnIps',
	'SecretId' => 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX',
	'Timestamp' => 1462782282,
	'Nonce' => 123456789,
	'Signature' => 'XXXXXXXXXXXXXXXXXXXXXXXX',
	'host' => ''www.test.com
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
        "oc_ips": [
			1.1.1.1,
			2.2.2.2,
			...
        ]
    }
}
```



