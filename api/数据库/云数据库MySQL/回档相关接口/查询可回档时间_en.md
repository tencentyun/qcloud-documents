## 1. API Description
This API (QueryCdbRollbackRangeTime) is used to query the time range available for the rollback of CDB instances.
Domain for API request: <font style='color:red'>cdb.api.qcloud.com </font>


## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href='/document/product/236/6921' title='Common Request Parameters'>Common Request Parameters</a>. The Action field for this API is QueryCdbRollbackRangeTime.

| Parameter Name | Required  | Type | Description |
|---------|---------|---------|---------|
| cdbInstanceIds.n | Yes | String | One or more instance IDs (n represents array subscript starting with 0). Instance ID, such as: cdb-c1nl9rpv. It is identical to the instance ID displayed in the Cloud Database console page and can be obtained using API [Query List of Instances](/doc/api/253/1266). Its value equals to the uInstanceId field value in the output parameter.  |


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please refer to <a href='https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81' title='Common Error Codes'>Common Error Codes</a> on the Error Code page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Error description |
| data | Array | Returned data message |
Parameter data is composed as follows:

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code returned for database query |
| message | String | Error message returned for database query | 
| cdbInstanceId | String | Instance ID |
| times | Array | Time range available for rollback | 
| times.begin | String | Start time available for rollback of the instance, such as: 2016-10-29 01:06:04 |
| times.end | String | End time available for rollback of the instance, such as: 2016-11-02 11:44:47 |


## 4. Error Codes
The following error codes only include the business logic error codes for this API.

| Error Code | Error Message | Error Description |
|---------|---------|---------|
| 9003 | InvalidParameter | Incorrect parameter |
| 9006 | InternalError | Database internal error |
| 11041 | InternalError.CDBNotExist | CDB instance does not exist |


## 5. Example
Input
<pre>
https://cdb.api.qcloud.com/v2/index.php?Action=QueryCdbRollbackRangeTime
&<<a href="/document/product/236/6921">Common request parameters</a>>
&cdbInstanceIds.0=cdb-mo64xu70
</pre>

Output
```
{
    "code":"0",
    "message":"",
    "codeDesc":"Success",
    "data":[
        {
            "code":"0",
            "message":"ok",
            "cdbInstanceId":"cdb-mo64xu70",
            "times":[
                {
                    "begin":"2016-10-29 01:06:04",
                    "end":"2016-11-02 11:44:47"
                }
            ]
        }
    ]
}
```


