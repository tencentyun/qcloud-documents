## 1. API Description
This API (StopCdbImportJob) is used to terminate the file import task.
Domain for API request: <font style='color:red'>cdb.api.qcloud.com </font>


## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href='/document/product/236/6921' title='Common Request Parameters'>Common Request Parameters</a>. The Action field for this API is StopCdbImportJob.

| Parameter Name | Required  | Type | Description |
|---------|---------|---------|---------|
| jobId | Yes | Int | Task ID |


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
| 9520 | InternalError | Import task does not exist |
| 9590 | InternalFailure | File import internal error |


## 5. Example
Input
<pre>
https://cdb.api.qcloud.com/v2/index.php?Action=StopCdbImportJob
&<<a href="/document/product/236/6921">Common request parameters</a>>
&jobId=18302
</pre>

Output
```
{
    "code":"0",
    "message":"",
    "codeDesc":"Success"
}
```


