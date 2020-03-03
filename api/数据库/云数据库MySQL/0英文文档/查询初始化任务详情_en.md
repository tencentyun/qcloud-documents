## 1. API Description
This API (GetCdbInitInfo) is used to query details of initialization task.
Domain for API request: <font style='color:red'>cdb.api.qcloud.com </font>


## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters are also needed when API is called. For more information, please refer to <a href='/document/product/236/6921' title='Common Request Parameters'>Common Request Parameters</a>. The Action field for this API is GetCdbInitInfo.

| Parameter Name | Required  | Type | Description |
|---------|---------|---------|---------|
| jobId | Yes | Int | Initialization task ID, which is the task ID that was returned when executing [Initialize Instance](/document/product/236/5335). |


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please refer to <a href='https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81' title='Common Error Codes'>Common Error Codes</a> on the Error Code page. |
| message | String | Module error message description depending on API.  |
| codeDesc | String | Error description |
| data | Array | Task details |
Parameter data is composed of the following parameters:

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | String | Task error code; 0: Succeeded; other values: Failed.  |
| message | String | Task message. An error message will be returned if the task fails.  |
| jobId | Int | Task ID |
| type | Int | Task type, possible return value: 6 - initialize instance |
| status | Int | Task status. Possible returned values include: 0 - running; 2 - execution succeeded; 3 - execution failed; 4 - terminated; 5 - deleted; 6- terminating.  |
| progress | Int | Task progress. Value range: [0-100]; where 0 means the task starts and 100 indicates that the task is completed.  |
| startTime | String | Task start time. Format: 2017-02-05 18:19:08 |
| endTime | String | Task end time. Format: 2017-02-05 18:19:08 |
| detail | Object | Task information |
Parameter detail is composed of the following parameters:

| Parameter Name | Type | Description |
|---------|---------|---------|
| cdbInstanceId | String | Instance ID, such as: cdb-c1nl9rpv. It is identical to the instance ID displayed in the Cloud Database console page and can be obtained using API [Query Instance List](/doc/api/253/1266). Its value equals the uInstanceId field value in the output parameter.  |


## 4. Error Codes
The following error codes only include the business logic error codes for this API.

| Error Code | Error Message | Error Description |
|---------|---------|---------|
| 9003 | InvalidParameter | Incorrect parameter |
| 9006 | InternalError | Database internal error |
| 9590 | InternalFailure | Task database access error |


## 5. Example
Input
<pre>
https://cdb.api.qcloud.com/v2/index.php?Action=GetCdbInitInfo
&<<a href="/document/product/236/6921">Common request parameters</a>>
&jobId=9
</pre>

Output
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "code": "0",
        "message": "success",
        "jobId": "47197",
        "type": "6",
        "status": "2",
        "progress": "100",
        "startTime": "2017-02-13 01:16:53",
        "endTime": "2017-02-13 01:17:56",
        "detail": [
            {
                "cdbInstanceId": "qcdbcb931d7017291f2a0431dd659f1005bf"
            }
        ]
    }
}
```


