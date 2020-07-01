## 1. API Description
This API (GetCdbRollbackJob) is used to query rollback task details.
Domain for API request: <font style="color:red">cdb.api.qcloud.com</font>


## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href='/document/product/236/6921' title='Common Request Parameters'>Common Request Parameters</a>. The Action field for this API is GetCdbRollbackJobTask.

| Parameter Name | Required  | Type | Description |
|---------|---------|---------|---------|
| jobId | Yes | Int | Rollback task ID. You can use API [GetCdbRollbackJob](/doc/api/253/4115) to query the task ID |


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please refer to <a href='https://intl.cloud.tencent.com/document/product/236/1743' title='Common Error Codes'>Common Error Codes</a> on the Error Code page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Error description |
| data | Array | Returned data |
Parameter data is composed of the following parameters:

| Parameter Name | Type | Description |
|---------|---------|---------|
| jobInfo | Object | Task information |
| taskDetail | Object | Task details |
Parameter jobInfo is composed as follows:

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | String | Error code. 0: Succeeded, other values: Failed |
| message | String | Error message |
| jobId | Int | Task ID |
| type | Int | Task type. Possible returned value: 10 - Database rollback |
| status | Int | Task status |
| progress | Int | Task progress |
| startTime | String | Start time of the task |
| endTime | String | End time of the task |
| detail | Array | Task details |
Parameter detail is composed as follows:

| Parameter Name | Type | Description |
|---------|---------|---------|
| cdbInstanceId | String | Instance ID |
| cdbInstanceName | String | Instance name |
| rollbackTime | String | Rollback time |
| operator | String | Operator |
| dbs | Array | Database information |
Parameter dbs is composed as follows:

| Parameter Name | Type | Description |
|---------|---------|---------|
| dbname | String | db name |
| newname | String | New name of db |

Parameter taskDetail is composed as follows:

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | int | Error code. Possible returned values include: 0: Succeeded, other values: Failed |
| message | String | Error message |
| status | String | Task status |
| progress | String | Task progress |
| startTime | String | Start time |
| endTime | String | End time |
| taskInfo | Array | Task information |
Parameter taskInfo is composed as follows:

| Parameter Name | Type | Description |
|---------|---------|---------|
| cdbInstanceId | String | Instance ID |
| cdbInstanceName | String | Instance name |
| rollbackTime | String | Rollback time |
| operator | String | Operator UIN |
| dbs | Array | Database |
Parameter dbs is composed as follows:

| Parameter Name | Type | Description |
|---------|---------|---------|
| dbname | String | db name |
| newname | String | New name of db |


## 4. Error Codes
The following error codes only include the business logic error codes for this API.

| Error Code | Error Message | Error Description |
|---------|---------|---------|
| 9003 | InvalidParameter | Incorrect parameter |
| 9006 | InternalError | Database internal error |
| 9013 | InternalError | System internal error |
| 9016 | InternalError | DES system internal error |
| 9590 | InternalFailure | Task database access error |
| 9593 | IncorrectInstanceStatus | Abnormal instance status|


## 5. Example
Input
<pre>
https://cdb.api.qcloud.com/v2/index.php?Action=GetCdbRollbackJobTask
&<<a href="/document/product/236/6921">Common request parameters</a>>
&jobId=12782
</pre>

Output
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "jobInfo": {
            "jobId": "12732",
            "type": "10",
            "status": "2",
            "progress": "100",
            "code": "0",
            "message": "The rollback of all instances is successful",
            "startTime": "2016-03-22 17:26:23",
            "endTime": "2016-03-22 17:28:01",
            "detail": [
                {
                    "cdbInstanceId": "qcdba38e736b015ecad282974cc33e8ffd61",
                    "cdbInstanceName": "cdb153952",
                    "rollbackTime": "2016-03-22 17:26:06",
                    "operator": "909619400",
                    "dbs": [
                        {
                            "dbname": "test",
                            "newname": "test_bak_1"
                        }
                    ]
                }
            ]
        },
        "taskDetail": [
            {
                "taskInfo": {
                    "cdbInstanceId": "62516f24-dc2c-11e5-abea-0819a6d0fc09",
                    "cdbInstanceName": "cdb153952",
                    "rollbackTime": "2016-03-22 17:26:06",
                    "operator": "909619400",
                    "dbs": [
                        {
                            "dbname": "test",
                            "newname": "test_bak_1"
                        }
                    ]
                },
                "status": "2",
                "progress": "100",
                "code": "0",
                "message": "Rollback is successful",
                "startTime": "2016-03-22 17:27:01",
                "endTime": "2016-03-22 17:28:01"
            }
        ]
    }
}
```


