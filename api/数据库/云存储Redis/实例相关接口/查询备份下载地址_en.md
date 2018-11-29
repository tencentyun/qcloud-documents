## 1. API Description
This API (GetBackupDownloadUrl) is used to query the download URL of CRS instance backup.
Domain name for API request: <font style='color:red'>redis.api.qcloud.com </font>

1. Private network and local download URLs are valid for 12 hours, and need to be re-obtained upon expiration;
2. Quotation marks must be used around URL when wget is used for downloading;

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see <a href='https://cloud.tencent.com/document/product/213/6976' title='Common Request Parameters'>Common Request Parameters</a>. The Action field for this API is GetBackupDownloadUrl.

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
| data | Object | Download URL of backup |

Parameter data represents the download URL of backup, and is composed as follows:

| Parameter Name | Type | Description |
|:---------|---------|---------|
| data.intranet | URL in private network | The download URL in private network, which can only be obtained on CVM. It is valid for 12 hours, and needs to be re-obtained upon expiration |
| data.extranet | URL in public network | The download URL in public network, which is valid for 12 hours and needs to be re-obtained upon expiration |

## 4. Error Codes
The following error codes include the business logic error codes for this API.

| Error Code | Error Message | Error Description |
|---------|---------|---------|
| 11201 | InvalidParameter | Incorrect business parameter |
| 10701 | InstanceNotExists | No instance can be found for the serialId |
| 10711 | BackupStatusAbnormal | The operation is impossible due to an abnormal backup status |
| 11213 | BackupNotExists | No instance backup can be found for the backupId |

## 5. Example
<pre>
https://redis.api.qcloud.com/v2/index.php?Action=GetBackupDownloadUrl
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
&redisId=crs-c7xq4kqu
&backupId=fb8d2cd6-f6ee-11e6-ac36-525400394272
</pre>
The returned results are as below:
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "intranet": "http://10.66.183.31:5500/download/dump.rdb?NuRTyoDugir/5bQ3o46lHIVXtwJKTEtotpngKa5R4A4AytZn+XjX7ywuP5QTV+ayfvQR3BIJRA12ECRSSGOzIM7qsLQ6TkjFVSkuoLqNJ0jCdm721qkJpQ==",
        "extranet": "http://203.195.128.115:9097/download/dump.rdb?NuRTyoDugir/5bQ3o46lHIVXtwJKTEtotpngKa5R4A4AytZn+XjX7ywuP5QTV+ayfvQR3BIJRA12ECRSSGOzIM7qsLQ6TkjFVSkuoLqNJ0jCdm721qkJpQ=="
    }
}
```
