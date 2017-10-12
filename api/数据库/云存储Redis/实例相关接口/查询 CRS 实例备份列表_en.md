## 1. API Description
 
This API (GetRedisBackupList) is used to query the backup list of a CRS instance.
Domain name for API request: <font style='color:red'>redis.api.qcloud.com </font>

- Currently, backups can only be retained for 7 days, so you can just query the backups for the last 7 days, including the manual backups initiated by users and the backups initiated by the system in the early morning.

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see <a href='https://cloud.tencent.com/document/product/213/6976' title='Common Request Parameters'>Common Request Parameters</a>. The Action field for this API is GetRedisBackupList.

| Parameter Name | Required | Type | Description |
|:---------|---------|---------|---------|
| limit | Yes | Int | Length of a page. |  |
| offset | Yes | Int | Current page number. Default is 0.  For query APIs, a maximum number of returned records is generally set for a single query by default. To traverse all the resources, you need to use "limit" and "offset" for a paged query; For example, to query the 40 records between 110 and 149, you can set offset = 110 and limit = 40.  |
| redisId | Yes | String | ID of instance to work with. This can be obtained from redisId in the returned values of API [DescribeRedis](/document/product/239/1384). |
| beginTime | No | String | Start time, such as: 2017-02-08 16:46:34. Query the list of instance backups initiated within the time period of [beginTime, endTime].  |
| endTime | No | String | End time, such as: 2017-02-08 19:09:26. Query the list of instance backups initiated within the time period of [beginTime, endTime].  |

## 3. Output Parameters

| Parameter Name | Type | Description |
|:---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please see <a href='https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81' title='Common Error Codes'>Common Error Codes</a> on the Error Codes page. |
| message | String | Error message description. A null value indicates a success |
| codeDesc | String | Description of error code at business side. For a successful operation, "Success" will be returned. In case of an error, a message describing the reason for the error will be returned.  |
| totalCount | Int | Total number of backups |
| data | Object | Details of instance backup list |


Parameter data indicates the details of instance backup list, and is composed as follows:

| Parameter Name | Type | Description |
|:---------|---------|---------|
| data.redisBackupSet | Array | Array of instance backups |

Parameter redisBackupSet indicates the array of instance backups, and is composed as follows:

| Parameter Name | Type | Description |
|:---------|---------|---------|
| startTime | String | The time when the backup starts |
| backupId | String | Backup ID |
| backupType | String | Backup type. <br>manualBackupInstance: Manual backup initiated by the user; <br>systemBackupInstance: Backup initiated by the system in the early morning |
| status | Int | Backup status.  <br>1: "Backup is locked by another process"; <br>2: "Backup is normal without being locked by any process"; <br>-1: "Backup expired"; <br>3:"Backup is being exported"; <br>4:"Backup has been exported successfully" |
| remark | String | Remarks of backup |
| locked | Int | Whether the backup is locked. 0: Not Locked; 1: Locked |

## 4. Error Codes
The following error codes include the business logic error codes for this API.

| Error Code | Error Message | Error Description |
|---------|---------|---------|
| 11201 | InvalidParameter | Incorrect business parameter |

## 5. Example
<pre>
https://redis.api.qcloud.com/v2/index.php?Action=GetRedisBackupList
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
&limit=10
&offset=0
&redisId=crs-izbob1wh
&beginTime=2017-02-08 16:46:34
&endTime=2017-02-08 19:09:26
</pre>
The returned results are as below:
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "totalCount": 2,
    "data": {
        "redisBackupSet": [
            {
                "startTime": "2017-02-08 16:46:34",
                "backupId": "19266626-eddb-11e6-890a-525400394272",
                "backupType": "manualBackupInstance",
                "status": 2,
                "remark": "testAPI",
                "locked": 0
            },
            {
                "startTime": "2017-02-08 19:09:26",
                "backupId": "0f87ffc6-edef-11e6-b88e-525400394272",
                "backupType": "systemBackupInstance",
                "status": 2,
                "remark": "",
                "locked": 0
            }
        ]
    }
}

```
