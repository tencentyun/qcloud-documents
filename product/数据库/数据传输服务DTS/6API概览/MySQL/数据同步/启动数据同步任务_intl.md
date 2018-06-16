## API Description
This API (StartCdbDataSyncTask) is used to start a data synchronization task. It can only be performed on the tasks with a status of "Verification Successful" (status=4).
Domain name for API request: <font style='color:red'>cdb.api.qcloud.com </font>


## Input Parameters
The following request parameter list only provides API request parameters. Common request parameters are required when the API is called. For more information, please see <a href='/doc/api/372/4153' title='Common Request Parameters'>Common Request Parameters</a> page. The Action field for this API is StartCdbDataSyncTask.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| jobId | Yes | Int | ID of data synchronization task. You can use the API "Query Data Synchronization Task List" to query the task ID. |


## Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. 0: Successful; other values: Failed. For more information, please see <a href='https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81' title='Common Error Codes'>Common Error Codes</a> on the Error Codes page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Error description |
| data | Array | Returned data |


## Example
Input
<pre>
https://cdb.api.qcloud.com/v2/index.php?Action=StartCdbDataSyncTask
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
&jobId=148
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


