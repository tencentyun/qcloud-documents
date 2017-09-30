## 1. API Description
This API is used to acquire function log according to the configured query conditions.    

Domain name for API access: scf.api.qcloud.com
## 2. Request Parameter
The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see [Common Request Parameters](/doc/api/244/4183). The Action field for this API is GetFunctionLogs.

| Parameter Name | Required | Type | Description |
|-----------|--------|----------|----------|
| functionName | No | String | Function name. |
| offset | No | Int | Data offset. Default: 0. |
| limit | No | Int | Length of returned data. Default: 20. |
| order | No | String | Whether the logs are sorted in ascending order or descending order. Available values: desc, asc. |
| orderby | No | String | This determines the field based on which the logs are sorted. Available fields: start_time, function_name, request_id, duration, mem_usage. |
| requestId | No | String | The generated request_id when the trigger is called. |

## 3. Response Parameters
| Parameter Name | Type | Description |
|-------|---|---------------|
| code | Int | Common error code. 0: Successful; other values: Failed. |
| message | String | Module error message description depending on API |
| codeDesc | String | Error code. For a successful operation, "Success" will be returned. For a failed operation, a message describing the failure will be returned. |
| total | Int | Total number of logs. |
| data | Array | List of log information returned. |

The data structures of returned log entries are as follows:

| Parameter Name | Type | Description |
|-------|---|---------------|
| function_name | String | Name of the corresponding function for this log. |
| ret_msg | String | Returned value when function execution was finished. |
| request_id | String | Corresponding request_id when the function was executed. |
| start_time | String | The time when function execution started. |
| ret_code | Int | Function execution result. 0: Successful; other values: Failed. |
| duration | Float | Function execution time cost (in ms). |
| bill_duration | Int | Billable duration for the function, rounded up to the latest 100 ms based on "duration" (in ms). |
| mem_usage | Int | Actual memory used during function execution (in bytes). |
| log | String | Log output during function execution. |

## 4. Example
Input
```
https://scf.api.qcloud.com/v2/index.php?Action=GetFunctionLogs
&<Common request parameters>
&offset=1
&limit=2
&orderby=duration
&functionName=helljin89
```
Output

```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "total": 189,
    "data": [
        {
            "functionName": "helljin89",
            "retMsg": "'module' object has no attribute 'lambda_handler'",
            "requestId": "b684ef85-250a-11e7-839d-5254007d2563",
            "startTime": "2017-04-19 22:16:00",
            "retCode": 1,
            "duration": 0.241,
            "billDuration": 100,
            "memUsage": 131072,
            "log": ""
        },
        {
            "functionName": "helljin89",
            "retMsg": "'module' object has no attribute 'lambda_handler'",
            "requestId": "b6842e1a-250a-11e7-aaa8-525400edfec1",
            "startTime": "2017-04-19 22:16:00",
            "retCode": 1,
            "duration": 0.269,
            "billDuration": 100,
            "memUsage": 131072,
            "log": ""
        }
    ]
}

```

