## 1. API Description
This API (CloseCdbExtranetAccess) is used to disable the public network access of a Cloud Database instance. After the public network access is disabled, the public network addresses cannot be accessed. The information of the public network domain and port of corresponding instances will not be returned via the API [Query List of Instances](/doc/api/253/1266).
Domain for API request: <font style='color:red'>cdb.api.qcloud.com </font>


## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href='/document/product/236/6921' title='Common Request Parameters'>Common Request Parameters</a>. The Action field for this API is CloseCdbExtranetAccess.

| Parameter Name | Required  | Type | Description |
|---------|---------|---------|---------|
| cdbInstanceId | Yes | String | Instance ID, such as: cdb-c1nl9rpv. It is identical to the instance ID displayed in the Cloud Database console page and can be obtained using API [Query List of Instances](/doc/api/253/1266). Its value equals to the uInstanceId field value in the output parameter.  |


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please refer to <a href='https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81' title='Common Error Codes'>Common Error Codes</a> on the Error Code page. |
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


## 5. Example
Input
<pre>
https://cdb.api.qcloud.com/v2/index.php?Action=CloseCdbExtranetAccess
&<<a href="/document/product/236/6921">Common request parameters</a>>
&cdbInstanceId=cdb-c1nl9rpv
</pre>

Output
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "jobId": 168138
    }
}
```


