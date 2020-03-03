## 1. API Description
This API (OpenCdbExtranetAccess) is used to enable the public network access of a Cloud Database instance. After enabling the public network access, you can access instances using the public network domain and port. You can use API [Query List of Instances](/doc/api/253/1266) to acquire the information of the public network domain and port.
Domain for API request: <font style='color:red'>cdb.api.qcloud.com </font>


## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href='/document/product/236/6921' title='Common Request Parameters'>Common Request Parameters</a>. The Action field for this API is OpenCdbExtranetAccess.

| Parameter Name | Required  | Type | Description |
|---------|---------|---------|---------|
| cdbInstanceId | Yes | String | Instance ID, such as: cdb-c1nl9rpv. It is identical to the instance ID displayed in the Cloud Database console page and can be obtained using API [Query List of Instances](/doc/api/253/1266). Its value equals to the uInstanceId field value in the output parameter.  |
| password | Yes | String | Public network access password, which should be a combination of 8-16 characters comprised of at least two of the following types: letters, numbers, special characters (_, +, -, &, =, !, @, #, $, %, ^, *, ()) |


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please refer to <a href='https://intl.cloud.tencent.com/document/product/236/1743' title='Common Error Codes'>Common Error Codes</a> on the Error Code page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Error description |
| data | Array | Returned task data |
Parameter data is composed of the following parameters:

| Parameter Name | Type | Description |
|---------|---------|---------|
| jobId | String | Task ID |


## 4. Error Codes
The following error codes only include the business logic error codes for this API.

| Error Code | Error Message | Error Description |
|---------|---------|---------|
| 9572 | InstanceNotExists | Instance does not exist |
| 9573 | OperationDenied | The public network permission is enabled |
| 9574 | OperationDenied | The public network permission is not enabled |
| 9575 | OperationDenied | The public network permission is being processed |
| 9576 | OperationDenied | Unable to operate because the instance is not running |
| 9587 | InvalidParameter | Wrong password |


## 5. Example
Input
<pre>
https://cdb.api.qcloud.com/v2/index.php?Action=OpenCdbExtranetAccess
&<<a href="/document/product/236/6921">Common request parameters</a>>
&cdbInstanceId=cdb-8qrg9t04
&password=abc123456
</pre>

Output
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "jobId": 168137
    }
}
```


