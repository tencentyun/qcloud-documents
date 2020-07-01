## 1. API Description
This API (ModifyCdbBackupInfo) is used to modify backup information, for example, to modify the name of a backup.
Domain for API request: <font style='color:red'>cdb.api.qcloud.com </font>


## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters are also needed when API is called. For more information, please refer to <a href='/document/product/236/6921' title='Common Request Parameters'>Common Request Parameters</a>. The Action field for this API is ModifyCdbBackupInfo.

| Parameter Name | Required  | Type | Description |
|---------|---------|---------|---------|
| cdbInstanceIds | Yes | String | One or more instance IDs (n represents array subscript starting with 0). Instance ID, such as: cdb-c1nl9rpv. It is identical to the instance ID displayed in the Cloud Database console page and can be obtained using API [Query List of Instances](/doc/api/253/1266). Its value equals to the uInstanceId field value in the output parameter.  |
| backupMethod | Yes | String | Target backup method, with optional values: logic cold backup "mysql", or physical cold backup "xtrabackup"|


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please refer to <a href='https://intl.cloud.tencent.com/document/product/236/1743' title='Common Error Codes'>Common Error Codes</a> on the Error Code page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Error description |
| data | Array | Returned data. Array being empty indicates success.


## 4. Error Codes
The following error codes only include the business logic error codes for this API.

| Error Code | Error Message | Error Description |
|---------|---------|---------|
| 9003 | InvalidParameter | Incorrect parameter |
| 9013 | InternalError | System internal error |
| 9544 | OperationDenied | Instance does not exist |
| 9572 | InstanceNotExists | Instance does not exist |


## 5. Example
Input
<pre>
https://cdb.api.qcloud.com/v2/index.php?Action=ModifyCdbBackupInfo
&<<a href="/document/product/236/6921">Common request parameters</a>>
&cdbInstanceIds.0=cdb-0ty37vfg
&backupMethod=mysql
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


