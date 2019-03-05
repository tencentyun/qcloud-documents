## API Description
This API (**OfflineHost**) is used to disable the acceleration service for a specified domain name.

Domain name for API request: <font style="color:red">cdn.api.qcloud.com</font>

**Notes:** 

+ Only one CDN domain name can be disabled at a time
+ After the domain name is disabled, a 404 error is returned from CDN node. Make sure that the resolved IP has been moved away from CDN before the domain name is disabled.
+ You can only disable an "Enabled" domain name.
+ The frequency of calling the API is limited to 100/min.

[View the example](https://cloud.tencent.com/document/product/228/1734)

## Input Parameters
The following request parameter list only provides the API request parameters. Common request parameters are required when the API is called. For more information, please see [Common Request Parameters](https://cloud.tencent.com/doc/api/231/4473) page. The Action field for this API is OfflineHost.

| Parameter Name | Required | Type | Description |
| ------ | ---- | ------ | ---------- |
| hostId | No | Int | ID of the domain name to be disabled |
| host | No | String | Accelerated domain to be disabled |

### Notes

+  You can use APIs [Query Domain Name Information by Domain Name](https://cloud.tencent.com/doc/api/231/3938) and [Query Domain Name Information](https://cloud.tencent.com/doc/api/231/3937) to obtain the ID of the host.
+  Either host or hostId must be specified for query.


## Output Parameters


| Parameter Name | Type | Description |
| -------- | ------ | ---------------------------------------- |
| code | Int | Common error code. 0: Successful; other values: Failed.<br/>For more information, please see [Common Error Codes](https://cloud.tencent.com/doc/api/231/5078#1.-.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81) on the Error Codes page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Error message or error code at business side.<br/>For more information, please see [Business Error Codes](https://cloud.tencent.com/document/product/228/5078#2.-.E6.A8.A1.E5.9D.97.E9.94.99.E8.AF.AF.E7.A0.81) on the Error Codes page. |

## Example

### Sample Parameters

```
hostId: 1234
```

### GET Request

For a GET request, all the parameters are required to be appended to the URL:

```
https://cdn.api.qcloud.com/v2/index.php?
Action=OfflineHost
&SecretId=XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
&Timestamp=1462436277
&Nonce=123456789
&Signature=XXXXXXXXXXXXXXXXXXXXX
&hostId=1234
```

### POST Request

For a POST request, the parameters are input in HTTP Request-body. The request address is:

```
https://cdn.api.qcloud.com/v2/index.php
```

Formats such as form-data and x-www-form-urlencoded are supported for the parameters. The array of parameters is as follows:

```
array (
  'Action' => 'OfflineHost',
  'SecretId' => 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX',
  'Timestamp' => 1462782282,
  'Nonce' => 123456789,
  'Signature' => 'XXXXXXXXXXXXXXXXXXXXXXXX',
  'hostId' => 1234
)
```

### Example of Result

```json
{
    "code": 0,
    "message": "",
    "codeDesc": "Success"
}
```

```json
{
    "code": 4000,
    "message": "(9175) Deploying status cdn host in progress[host in progress]",
    "codeDesc": 9175
}
```




