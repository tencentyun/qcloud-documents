## 1. API Description
This API (GetCdbModifyParamsJobTask) is used to query the details of a parameter modification task.
Domain for API request: <font style='color:red'>cdb.api.qcloud.com </font>


## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href='https://intl.cloud.tencent.com/document/product/236/6921' title='Common Request Parameters'>Common Request Parameters</a>. The Action field for this API is GetCdbModifyParamsJobTask.

| Parameter Name | Required  | Type | Description |
|---------|---------|---------|---------|
| jobId | Yes | Int | ID of parameter modification task, which is the task ID that was returned when executing [Modify Parameter](/document/product/236/6368) |


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please refer to <a href='https://intl.cloud.tencent.com/document/product/236/1743' title='Common Error Codes'>Common Error Codes</a> on the Error Code page.
| message | String | Module error message description depending on API |
| codeDesc | String | Error description |
| data | Array | Returned data |
Parameter data is composed of the following parameters:

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | String | Error code. 0: Succeeded; other values: Failed |
| message | String | Error code message |
| jobId | Int | Task ID |
| type | Int | Task type. Possible returned value: 5-to modify the parameter |
| status | Int | Task status. Possible returned values include: 0-Initializing; 1-Running; 2-Succeeded; 3-Failed; 4-Terminated; 5-Deleted |
| progress | Int | Task progress, expressed as a percentage, 100 means completed |
| startTime | String | Task start time. Format: yyyy-mm-dd hh:mm:ss |
|endTime | String | Task end time. Format: yyyy-mm-dd hh:mm:ss |
| detail | Object | Task information |
Parameter detail is composed of the following parameters:

| Parameter Name | Type | Description |
|---------|---------|---------|
| cdbInstanceId | String | Instance ID, such as: cdb-c1nl9rpv. It is identical to the instance ID displayed in the Cloud Database console page and can be obtained using API [Query List of Instances](/doc/api/253/1266). Its value equals to the uInstanceId field value in the output parameter.  |
| paramList | Object | Modified parameter list |
Parameter paramList is composed of the following parameters:

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | String | Error code. 0: Succeeded; other values: Failed |
| message | String | Error code message |
| name | String | Modified parameter name |
| cur_value | String | Parameter value after modification |
| old_value | String | Parameter value before modification |


## 4. Error Codes
The following error codes only include the business logic error codes for this API.

| Error Code | Error Message | Error Description |
|---------|---------|---------|
| 9003 | InvalidParameter | Incorrect parameter |
| 9613 | InternalError | Database query error |


## 5. Example
Input
<pre>
https://cdb.api.qcloud.com/v2/index.php?Action=GetCdbModifyParamsJobTask
&<<a href="/document/product/236/6921">Common request parameters</a>>
&jobId=7
</pre>

Output
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "code": 0,
        "message": "Parameter Configuration Succeeded",
        "jobId": 129,
        "type": 5,
        "status": 2,
        "progress": 100,
        "startTime": "2016-12-25 19:55:48",
        "endTime": "2016-12-25 19:56:29",
        "detail": [
            {
                "cdbInstanceId": "qcdbd392646a080c1f373f189d018f266c27",
                "paramList": [
                    {
                        "code": 0,
                        "message": "ok",
                        "name": "lower_case_table_names",
                        "cur_value": "1",
                        "old_value": "0"
                    },
                    {
                        "code": 0,
                        "message": "Same value",
                        "name": "character_set_server",
                        "cur_value": "utf8",
                        "old_value": "utf8"
                    }
                ]
            }
        ]
    }
}
```


