## 1. API Description
This API (GetCdbImportSQLFileHistory) is used to query the recent record of file import.
Domain for API request: <font style='color:red'>cdb.api.qcloud.com </font>


## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href='/document/product/236/6921' title='Common Request Parameters'>Common Request Parameters</a>. The Action field for this API is GetCdbImportSQLFileHistory.

| Parameter Name | Required  | Type | Description |
|---------|---------|---------|---------|
| cdbInstanceId | Yes | String | Instance ID, such as: cdb-c1nl9rpv. It is identical to the instance ID displayed in the Cloud Database console page and can be obtained using API [Query List of Instances](/doc/api/253/1266). Its value equals to the uInstanceId field value in the output parameter.  |
| startTime | No | String | Start time, such as: 2016-01-01 00:00:01 |
| endTime | No | String | End time, such as: 2016-01-01 23:59:59 |
| offset | No | Int | Record offset; default is 0 |
| Limit | No | Int | Number of returned results upon a single request; default is 20 |


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please refer to <a href='https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81' title='Common Error Codes'>Common Error Codes</a> on the Error Code page.  |
| message | String | Module error message description depending on API.  |
| codeDesc | String | Error description |
| totalCount | Int | Total number of import records |
| data | Array | Returned data |
Parameter data is composed as follows:

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | String | Import task error code; 0: Succeeded; other values: Failed.  |
| message | String | Import task message. An error message will be returned if the task fails.  |
| jobId | Int | Task ID |
| status | Int | Task status. Possible returned values: -1 (Import failed), 0 (Import succeeded), 1 (Importing), 1000 (The task is being created), 9529 (The task is terminated).  |
| cdbInstanceId | Int | Instance ID |
| fileName | String | File name |
| fileSize | Int | File size (in bytes) |
| dbName | String | Name of the destination database to which the files are imported |
| process | Int | Import progress |
| costTime | String | Time spent on the import (in seconds) |
| createTime | String | Creation time of import task |


## 4. Error Codes
The following error codes only include the business logic error codes for this API.

| Error Code | Error Message | Error Description |
|---------|---------|---------|
| 9003 | InvalidParameter | Incorrect parameter |


## 5. Example
Input
<pre>
https://cdb.api.qcloud.com/v2/index.php?Action=GetCdbImportSQLFileHistory
&<<a href="/document/product/236/6921">Common request parameters</a>>
cdbInstanceId=cdb-0pzitle8
</pre>

Output
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "totalCount": "0",
    "data": []
}
```


