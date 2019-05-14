## 1. API Description
This API (RestoreInstance) is used to restore a CRS instance.
Domain name for API request: <font style='color:red'>redis.api.qcloud.com </font>

- The target instance can only be restored to its own backup, instead of that of another instance.

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see <a href='https://cloud.tencent.com/document/product/213/6976' title='Common Request Parameters'>Common Request Parameters</a> page. The Action field for this API is RestoreInstance.

| Parameter Name | Required | Type | Description |
|:---------|---------|---------|---------|
| redisId | Yes | String | ID of instance to work with. This can be obtained from redisId in the returned values of API [DescribeRedis](/document/product/239/1384). |
| password | Yes | String | Password for the instance. It needs to be verified when the instance is restored. |
| backupId | Yes | String | Backup ID, which can be obtained from backupId in the returned values of API [GetRedisBackupList](/document/product/239/1384).  |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please see <a href='https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81' title='Common Error Codes'>Common Error Codes</a> on the Error Codes page. |
| message | String | Error message description. A null value indicates a success |
| codeDesc | String | Description of error code at business side. For a successful operation, "Success" will be returned. In case of an error, a message describing the reason for the error will be returned.  |
| data | Object | Task ID |

Parameter data indicates the task ID, and is composed as follows:

| Parameter Name | Type | Description |
|:---------|---------|---------|
| data.requestId | Task ID | Task ID. You can use the API [DescribeTaskInfo](/document/product/239/1387) to query the task execution status |

## 4. Error Codes
The following error codes include the business logic error codes for this API.

| Error Code | Error Message | Error Description |
|---------|---------|---------|
| 11201 | InvalidParameter | Incorrect business parameter |
| 10701 | InstanceNotExists | No instance can be found for the serialId |
| 10707 | InstanceLockedError | The operation is impossible because the instance is locked |
| 10702 | InstanceStatusAbnormal | The operation is impossible due to an abnormal instance status. For example, the instance has a status of "in process" or "isolated" or "deleted" |
| 10711 | BackupStatusAbnormal | The operation is impossible due to an abnormal backup status | The backup may be expired or deleted |
| 10710 | BackupLockedError | The operation is impossible because the instance is locked by another task |
| 10712 | PasswordError | Incorrect instance password |
| 11213 | BackupNotExists | No instance backup can be found for the backupId |

## 5. Example
<pre>
https://redis.api.qcloud.com/v2/index.php?Action=RestoreInstance
&<<a href="https://cloud.tencent.com/doc/api/229/6976">common request parameters</a>>
&redisId=crs-izbob1wh
&password=12D3E@!r5ed
&backupId=e824aecc-ef5e-11e6-a2c7-525400082493
</pre>
The returned results are as below:
```
{
    "code": 0,
    "message": "",
	"codeDesc": "Success",
	"data": {
        "requestId": 375074
    }
}
```
