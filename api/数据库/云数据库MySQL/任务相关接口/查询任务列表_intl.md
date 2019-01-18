## 1. API Description
This API (GetCdbJobList) is used to query the task list of cloud database.
Domain for API request: <font style='color:red'>cdb.api.qcloud.com </font>


## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters are also needed when API is called. For more information, please refer to <a href='/document/product/236/6921' title='Common Request Parameters'>Common Request Parameters</a>. The Action field for this API is GetCdbJobList.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| jobId | No | Int | Task ID, the jobId returned by executing CDB related operations |
| taskTypeList | No | Array | Task type. All task types are queried if no value is passed. Possible return values include: 2 - SQL operation; 3 - data import; 5 - parameter configuration; 6 - initialization; 7 - restart; 8 - enable GTID; 9 - read-only instance upgrade; 10 - database rollback; 11 - master instance upgrade; 12 - delete database list; 13 - switch to master instance; |
| taskStatusList | No | Int | Task status. All task status are queried if no value is passed; possible return values include: 0 - running; 2 - execution succeeded; 3 - execution failed; 4 - terminated; 5 - deleted; 6- terminating |
| startTimeBegin | No | String | Task start time. Format: Y-m-d |
| StartTimeEnd | No | String | Task end time. Format: Y-m-d |
| offset | No | Int | Record offset; default is 0 |
| limit | No | Int | Number of records returned for a single request; default is 20; maximum is 100 |


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please refer to <a href='https://intl.cloud.tencent.com/document/product/236/1743' title='Common Error Codes'>Common Error Codes</a> on the Error Code page. |
| message | String | Module error message description depending on API |
| codeDesc | String | Error code description|
| data | Array | Returned job status data |
data is composed of the following parameters:

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | String | Task error code; 0: Succeeded; other values: Failed.  |
| message | String | Task message. An error message will be returned if the task fails.  |
| jobId | Int | Task ID |
| type | Int | Task type. Possible returned values include: 2 - SQL operation; 3 - data import; 5 - parameter configuration; 6 - initialization; 7 - restart; 8 - enable GTID; 9 - read-only instance upgrade; 11 - master instance upgrade; 12 - delete database list; 13 - switch to master instance |
| status | Int | Task status, possible return values include: 0 - running; 2 - execution succeeded; 3 - execution failed; 4 - terminated; 5 - deleted; 6- terminating |
| progress | Int | Task progress, value range is [0-100]; where 0 means the task starts and 100 indicates that the task is completed.  |
| startTime | String | Task start time. Format: 2017-02-05 18:19:08 |
| endTime | String | Task end time. Format: 2017-02-05 18:19:08 |
| detail | Object | Task details |


## 4. Error Codes
The following error codes only include the business logic error codes for this API.

| Error Code | Error Message | Error Description |
|---------|---------|---------|
| 9000 | SystemError | System internal error |
| 9003 | InvalidParameter | Incorrect parameter |
| 9006 | InternalError | Database internal error |
| 9013 | InternalError | System internal error |
| 9016 | InternalError | System internal error |
| 9544 | OperationDenied | Instance does not exist |
| 9572 | InstanceNotExists | Instance does not exist |
| 9576 | OperationDenied | Unable to operate because the instance is not running |
| 9593 | IncorrectInstanceStatus | Abnormal instance status |

## 5. Example
Input
<pre>
https://cdb.api.qcloud.com/v2/index.php?Action=GetCdbJobList
&<<a href="/document/product/236/6921">Common request parameters</a>>
</pre>

Output
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "totalCount": "1",
    "data": [
        {
            "code": "0",
            "message": "Parameter Configuration Succeeded",
            "jobId": "132",
            "type": "5",
            "status": "2",
            "progress": "100",
            "startTime": "2017-02-13 17:21:23",
            "endTime": "2017-02-13 17:25:27",
            "detail": [
                {
                    "code": 0,
                    "message": "Parameter Configuration Succeeded",
                    "progress": 100,
                    "startTime": "2017-02-13 17:25:25",
                    "endTime": "2017-02-13 17:25:27",
                    "cdbInstanceId": "qcdb6bfd419f2e054beb210b8fa12b68fc15",
                    "paramList": [
                        {
                            "code": 0,
                            "message": "ok",
                            "name": "auto_increment_increment",
                            "cur_value": "5",
                            "old_value": "4"
                        }
                    ]
                }
            ]
        }
    ]
}
```


