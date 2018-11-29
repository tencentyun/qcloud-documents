## 1. API Description
This API (DelCdbDataMigrationTask) is used to delete a data migration task. It can only be performed for the non-running tasks. The relevant statuses include Not Configured (status = 0), Configured (status = 1), Verification Failed (status = 3), Verification Succeeded (status = 4), Migration Failed (status = 8) and Migration Succeeded (status = 9).
Domain for API request: <font style='color:red'>cdb.api.qcloud.com </font>


## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href='/doc/api/372/4153' title='Common Request Parameters'>Common Request Parameters</a>. The Action field for this API is DelCdbDataMigrationTask.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| jobId | Yes | Int | ID of data migration task. Please use API "Query Data Migration Task List" to query the task ID |


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please refer to <a href='https://intl.cloud.tencent.com/document/product/236/1743' title='Common Error Codes'>Common Error Codes</a> on the Error Code page.  |
| message | String | Module error message description depending on API.  |
| codeDesc | String | Error description |
| data | Array | Returned data |


## 4. Example
Input
<pre>
https://cdb.api.qcloud.com/v2/index.php?Action=DelCdbDataMigrationTask
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
&jobId=201
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


