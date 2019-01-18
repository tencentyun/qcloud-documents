## 1. API Description
This API (ModifyCdbInstanceAccountPassword) is used to modify the password of the account of a Cloud Database instance.
Domain for API request: <font style="color:red">cdb.api.qcloud.com</font>


## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href='https://intl.cloud.tencent.com/document/product/236/6921' title='Common Request Parameters'>Common Request Parameters</a>. The Action field for this API is ModifyCdbInstanceAccountPassword.

| Parameter Name | Required  | Type | Description |
|---------|---------|---------|---------|
| cdbInstanceId | Yes | String | Instance ID, such as: cdb-c1nl9rpv. It is identical to the instance ID displayed in the Cloud Database console page and can be obtained using the [Query List of Instances](/doc/api/253/1266) API.  |
| user | Yes | String | Account name. Rules: the name should contain 1-16 characters, including upper/lowercase letters, numbers, or underscores; the first character cannot be an underscore |
| host | Yes | String | CVM name. Rules: the name should contain 1-32 characters, including upper/lowercase letters, numbers, or special characters (%. :) |
| password | Yes | String | Password. Rules: the password should contain 8-16 characters, including at least two the followings: uppercase/lowercase letters, numbers, special characters (_+-&=!@#$%^*()) |

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
| 9003 | InvalidParameter | Incorrect parameter |
| 9587 | InvalidParameter | Wrong password |
| 9572 | InstanceNotExists | Instance does not exist |
| 9531 | ConnectRefused | Instance connection is refused |
| 9532 | ConnectErrorUnknown | Instance connection error |
| 9533 | SqlExecFailUnknown  | SQL execution error |
| 9534 | CheckUserExistChangePassword | Cannot find the account whose password is to be changed |


## 5. Example
Input
<pre>
https://cdb.api.qcloud.com/v2/index.php?Action=ModifyCdbInstanceAccountPassword
&<<a href="/document/product/236/6921">Common request parameters</a>>
&cdbInstanceId=cdb-rharasqw
&user=root
&host=localhost
&password=123wewr%24%25
</pre>

Output
```
{
    "code": 0,
    "message": "",
    "codeDesc":"Success",
    "data": []
}
```


