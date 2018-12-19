## 1. API Description
This API (SetCdbAutoRenew) is used to set or cancel the auto renewal for instances (including master instances and read-only instances).
Domain for API request: <font style="color:red">cdb.api.qcloud.com</font>

1. Any instance marked "Auto Renewal" will be automatically renewed for one month whenever it expires.
2. Before using this API, please make ensure that there is sufficient balance in user's account.
3. Auto renewal is not required for instances with pay by usage mode.

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href='/document/product/236/6921' title='Common Request Parameters'>Common Request Parameters</a>. The Action field for this API is SetCdbAutoRenew.

| Parameter Name | Required  | Type | Description |
|---------|---------|---------|---------|
| cdbInstanceId | Yes | String | Instance ID, such as: cdb-c1nl9rpv. It is identical to the instance ID displayed in the Cloud Database console page and can be obtained using API [Query List of Instances](/doc/api/253/1266). Its value equals to the uInstanceId field value in the output parameter.  |
| isAutoRenew | Yes | String | Whether auto renewal is enabled. Values include: Y - Yes, N - No |


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please refer to <a href='https://intl.cloud.tencent.com/document/product/236/1743' title='Common Error Codes'>Common Error Codes</a> on the Error Code page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Error description |
| data | Array | Data |


## 4. Error Codes
The following error codes only include the business logic error codes for this API.

| Error Code | Error Message | Error Description |
|---------|---------|---------|
| 9572 | InstanceNotExists | Instance does not exist |
| 9006 | InternalError | Database internal error |


## 5. Example
Input
<pre>
https://cdb.api.qcloud.com/v2/index.php?Action=SetCdbAutoRenew
&<<a href="/document/product/236/6921">Common request parameters</a>>
&cdbInstanceId=cdb-c1nl9rpv
&isAutoRenew=Y
</pre>

Output
```
{
    "code":"0",
    "message":"",
    "codeDesc":"Success",
    "data":[]
}
```


