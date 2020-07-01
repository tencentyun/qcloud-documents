## 1. API Description
This API (CreateBackup) is used to create a backup.
Domain for API request: sqlserver.api.qcloud.com


## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see<a href='https://cloud.tencent.com/document/api/238/7328
' title='Common Request Parameters'>Common Request Parameters</a>. The Action field for this API is CreateBackup.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| resourceId | Yes | String | Instance ID |
| strategy | No | Int | Backup strategy (0: Instance backup. 1: Multi-database backup) |
| dbList.n ( dbList is an array. The input parameters here are the array elements) | No | string | List of names of the databases to be backed up (for multi-database backup only)


## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. 0: Successful; other values: Failed. For more information, please see <a href='https://cloud.tencent.com/doc/api/238/7334#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81' title='Common Error Codes'>Common Error Codes</a> on the Error Codes page. |
| message | String | Module error message description depending on API. |
| data | Array | Returned data |

Parameter data is composed as follows:

| Parameter Name | Type | Description |
|---------|---------|---------|
| flowId | Int | Flow ID |

## 4. Error Codes

| Error Code | Error Message | Error Description |
|---------|---------|---------|
| 50 | InstanceNotFound | Instance does not exist |
| 51 | AbnormalInstanceStatus | Instance status exception |
| 1000 | SystemError | System error. Contact customer service. |
| 1002 | DBConnectError | Database connection error |
| 1005 | CreateFlowFailed | Failed to create task flow |

## 5. Example
Input
<pre>
https://sqlserver.api.qcloud.com/v2/index.php?Action=CreateBackup
&<<a href="https://cloud.tencent.com/document/api/238/7328">Common request parameters</a>>
&resourceId=mssql-q6g71pcf
&strategy=1
&dbList.0=test1
&dbList.1=test2
</pre>
Output
```
{
    "code":"0",
    "message":"",
    "data":{
        "flowId":5293
    }
}
```


