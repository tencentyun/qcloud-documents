## 1. API Description
This API (GetCdbRollbackJob) is used to query the list of rollback tasks.
Domain for API request: <font style="color:red">cdb.api.qcloud.com</font>

1. The list of Cloud Database instance rollback tasks can be queried based on the CDB instance ID;
2. A maximum of 100 task records can be returned for each request.

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href='/document/product/236/6921' title='Common Request Parameters'>Common Request Parameters</a>. The Action field for this API is GetCdbRollbackJob.

| Parameter Name | Required  | Type | Description |
|---------|---------|---------|---------|
| cdbInstanceId | Yes | String | Instance ID, such as: cdb-c1nl9rpv. It is identical to the instance ID displayed in the Cloud Database console page and can be obtained using API [Query List of Instances](/doc/api/253/1266). Its value equals to the uInstanceId field value in the output parameter.  |
| offset | No | Int | Offset; default is 0 |
| limit | No | Int | Number of returned tasks. The default value is 50, and the maximum is 100 |

## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please refer to <a href='https://intl.cloud.tencent.com/document/product/236/1743' title='Common Error Codes'>Common Error Codes</a> on the Error Code page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Error description |
| data | Array | Returned list of rollback tasks |
Parameter data is composed of the following parameters:

| Parameter Name | Type | Description |
|---------|---------|---------|
| taskCount | Int | Total number of rollback tasks |
| taskList | Array | List of rollback tasks |

Parameter taskList is composed of the following parameters:

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | String | Error code |
| message | String | Rollback error message |
| jobId | String | Task ID |
| startTime | String | Start time |
| endTime | String | End time |
| name | String | Database table to be rolled back |
| newName | String | Database table after rollback |
| progress | String | Rollback progress |
| status | Int | Rollback status |
| taskMessage | String | Task execution results |
| taskProgress | String | Task execution progress |
| taskStatus | String | Task execution status |
| type | String | Task type. Possible returned values include: 1 - Database rollback; 10 - Batch database rollback |
| taskContext | Array | Task details |
Parameter taskContext is composed as follows:

| Parameter Name | Type | Description |
|---------|---------|---------|
| data | Array | Task details |
| data.operator | String | Operator UIN |
| data.rollbackTime | String | Rollback time |
| data.dbs | Array | Rollback database details |
| data.dbs.dbname | String | Database name to be rolled back |
| data.dbs.newname | String | Database name after rollback |


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
https://cdb.api.qcloud.com/v2/index.php?Action=GetCdbRollbackJob
&<<a href="/document/product/236/6921">Common request parameters</a>>
&cdbInstanceId=cdb-c1nl9rpv
</pre>

Output
```
{
    "code":"0",
    "message":"",
    "codeDesc":"Success",
    "data":{
        "taskCount":"1",
        "taskList":[
            {
                "code":"0",
                "message":"",
                "jobId":"1343",
                "startTime":"2016-01-25 17:32:59",
                "endTime":"2016-01-25 17:35:02",
                "name":"test, test_bak",
                "newName":"test_bakee, test_bak_bak",
                "progress":"100",
                "status":"2",
                "taskMessage":"Rollback is successful",
                "taskProgress":"100",
                "taskStatus":"2",
                "type":"10",
                "taskContext":{
                    "data":{
                        "operator":"231323",
                        "rollbackTime":"2016-01-25 17:32:39",
                        "dbs":[
                            {
                                "dbname":"test",
                                "newname":"test_bakee"
                            },
                            {
                                "dbname":"test_bak",
                                "newname":"test_bak_bak"
                            }
                        ]
                    }
                }
            }
        ]
    }
}
```

