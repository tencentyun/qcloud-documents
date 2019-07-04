## 1. API Description
This API (ExportRedisBackup) is used to export the CRS instance backup.
Domain name for API request: <font style='color:red'>redis.api.qcloud.com </font>

- Export the backup file with a rdb format;
- Only the backup of a cluster instance needs to be exported;
- Only after the backup is exported can it be downloaded by calling the API GetBackupDownloadUrl.
- Only the backup with status 2 can be exported. You can use the API [GetRedisBackupList](/document/product/239/8403) to acquire the backup status.

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see <a href='https://cloud.tencent.com/document/product/213/6976' title='Common Request Parameters'>Common Request Parameters</a> page. The Action field for this API is ExportRedisBackup.

| Parameter Name | Required | Type | Description |
|:---------|---------|---------|---------|
| redisId | Yes | String | ID of instance to work with. This can be obtained from redisId in the returned values of API [DescribeRedis](/document/product/239/1384). |
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
| 11213 | BackupNotExists | No instance backup can be found for the backupId |
| 11214 | OnlyClusterInstanceCanExportBackup | Only the backup of a cluster instance is allowed to be exported |
| 10711 | BackupStatusInvalid | Invalid backup status (for a cluster instance, only the backup with status 2 can be exported) |

## 5. Example
<pre>
https://redis.api.qcloud.com/v2/index.php?Action=ExportRedisBackup
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common Request Parameters</a>>
&redisId=crs-j30wibe7
&backupId=3a07b27e-f744-11e6-babc-525400082493
</pre>
The returned results are as below:
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
	 "data": {
        "requestId": 400151
    }
}
```
