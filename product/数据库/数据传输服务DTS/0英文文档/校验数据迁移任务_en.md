## 1. API Description
This API (CheckCdbDataMigrationTask) is used to check a data migration task. It can only be performed for the tasks with a status of "Configured" (status = 1).
Domain for API request: <font style='color:red'>cdb.api.qcloud.com </font>


## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href='/doc/api/372/4153' title='Common Request Parameters'>Common Request Parameters</a>. The Action field for this API is CheckCdbDataMigrationTask.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| jobId | Yes | Int | ID of data migration task. Please use API "Query Data Migration Task List" to query the task ID |


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please refer to <a href='https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81' title='Common Error Codes'>Common Error Codes</a> on the Error Code page.  |
| message | String | Module error message description depending on API.  |
| codeDesc | String | Error description |


## 4. Error Codes
The following error codes only include the business logic error codes for this API.

| Error Code | Error Message | Error Description |
|---------|---------|---------|
| 9003 | InvalidParameter | Incorrect parameter |
| 9013 | InternalError | System internal error |
| 9634 | OperationDenied | Self-built migration operation is not allowed |
| 9570 | OperationDenied | Process conflict. The task is not allowed |
| 9572 | InstanceNotExists | Instance does not exist |
| 9589 | InternalError | Task data error |
| 9591 | TaskNotExist | Task does not exist |
| 9592 | OperationDenied | Source MySQL or destination instance already has a running task |
| 9631 | OperationDenied | Task data error |


## 5. Example
Input
<pre>
https://cdb.api.qcloud.com/v2/index.php?Action=CheckCdbDataMigrationTask
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
&jobId=146
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


