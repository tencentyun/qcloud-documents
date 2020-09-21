## 1. API Description
This API (CdbMysqlInit) is used to initialize Cloud Database instances, during which the character set, port, case sensitivity and the password of root account can be set. The instance is available after the initialization.
Domain for API request: <font style='color:red'>cdb.api.qcloud.com </font>


## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href='/document/product/236/6921' title='Common Request Parameters'>Common Request Parameters</a>. The Action field for this API is CdbMysqlInit.

| Parameter Name | Required  | Type | Description |
|---------|---------|---------|---------|
| cdbInstanceId | Yes | String | Instance ID, such as: cdb-c1nl9rpv. It is identical to the instance ID displayed in the Cloud Database console page and can be obtained using API [Query List of Instances](/doc/api/253/1266). Its value equals to the uInstanceId field value in the output parameter.  |
| charset | Yes | String | Character set; possible values include: [latin1, utf8, gbk, utf8mb4] |
| port | Yes | Int | Custom port, value range: [1024-65535] |
| lowerCaseTableNames | Yes | Int | Whether the table name only be saved in lowercase. Possible returned values: 1 - Only saved in lowercase; 0 - Case-sensitive |
| password | Yes | String | Password of root account, which should be a combination of 8-16 characters comprised of at least two of the following types: letters, numbers, special characters (!, @, #, $, %, ^, *, ()) |


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please refer to <a href='https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81' title='Common Error Codes'>Common Error Codes</a> on the Error Code page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Error description |
| jobId | Int | Task ID. You can use API [Query Asynchronous Tasks Initialization Details](/doc/api/253/5334) to query the task details.  |


## 4. Error Codes
The following error codes only include the business logic error codes for this API.

| Error Code | Error Message | Error Description |
|---------|---------|---------|
| 9003 | InvalidParameter | Incorrect parameter |
| 9006 | InternalError | Database internal error |
| 9587 | InvalidParameter | Wrong password |
| 9590 | InternalFailure | Task database access error |
| 9593 | IncorrectInstanceStatus | Abnormal instance status |


## 5. Example
Input
<pre>
https://cdb.api.qcloud.com/v2/index.php?Action=CdbMysqlInit
&<<a href="/document/product/236/6921">Common request parameters</a>>
&cdbInstanceId=cdb-c1nl9rpv
&charset=utf8
&port=3306
&password=cloud123456
&lowerCaseTableNames=0
</pre>

Output
```
{
    "code":"0",
    "message":"",
    "codeDesc":"Success",
    "jobId":"12894"
}
```


