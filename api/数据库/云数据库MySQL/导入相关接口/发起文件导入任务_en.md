## 1. API Description
This API (StartCdbImportJob) is used to initiate a file import task.
Domain for API request: <font style='color:red'>cdb.api.qcloud.com </font>


## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href='/document/product/236/6921' title='Common Request Parameters'>Common Request Parameters</a>. The Action field for this API is StartCdbImportJob.

| Parameter Name | Required  | Type | Description |
|---------|---------|---------|---------|
| uInstanceId | Yes | Int | ID of the instance on which an import will be performed, such as: cdb-c1nl9rpv. It is identical to the instance ID displayed in the Cloud Database console page and can be obtained using API [Query List of Instances](/doc/api/253/1266). Its value equals to the uInstanceId field value in the output parameter.  |
| dbName | No | Int | Name of the destination database to which the files are imported. If the parameter is not passed, it means not specifying a database |
| rootPassword | Yes | Int | root password of the instance |
| fileName | Yes | Int | Names of files to be imported, which can be obtained via the API for querying the list of files to be imported |


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please refer to <a href='https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81' title='Common Error Codes'>Common Error Codes</a> on the Error Code page.  |
| message | String | Module error message description depending on API.  |
| codeDesc | String | Error description |
| data | Object | Import task details |
Parameter data is composed as follows:

| Parameter Name | Type | Description |
|---------|---------|---------|
| jobId | Int | Task ID, which can be used to terminate the task |


## 4. Error Codes
The following error codes only include the business logic error codes for this API.

| Error Code | Error Message | Error Description |
|---------|---------|---------|
| 9003 | InvalidParameter | Incorrect parameter |
| 9520 | InternalError | File import internal error |
| 9541 | Import.FileSize  | File content cannot be empty |
| 9572 | InstanceNotExists | Instance does not exist |
| 9576 | OperationDenied | Instance is not running, or is executing other operations |
| 9587 | InvalidParameter | Wrong password |
| 9590 | InternalFailure | File import internal error |


## 5. Example
Input
<pre>
https://cdb.api.qcloud.com/v2/index.php?Action=StartCdbImportJob
&<<a href="/document/product/236/6921">Common request parameters</a>>
&uInstanceId=cdb-2d9mgksg
&rootPassword=xxxxxxxx
&fileName=test.sql
</pre>

Output
```
{
    "code":"0",
    "message":"",
    "codeDesc":"Success",
    "data":{
        "jobId": "18302"
     }
}
```


