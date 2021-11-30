## 1. API Description
This API (CdbTdsqlSetBackupTime) is used to set custom backup time.

Domain for API request: tdsql.api.qcloud.com



## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see <a href='/doc/api/309/7016' title='Common Request Parameters'>Common Request Parameters</a>. The Action field for this API is CdbTdsqlSetBackupTime.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| cdbInstanceId | Yes | Int | Instance ID |
| sBackupTime | Yes | String | Start time of daily backup time span. Format: mm:ss, such as 22:00 |
| eBackupTime | Yes | String | End time of daily backup time span. Format: mm:ss, such as 23:59 |


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. 0: Successful; other values: Failed. For more information, please see <a href='https://cloud.tencent.com/doc/api/309/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81' title='Common Error Codes'>Common Error Codes</a> on the Error Codes page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Error message |
| data | Array | Returned data |
| data.status | Int | Status. 0: Successful | 
## 4. Error Codes

The following are the common error codes for this API. Other error codes not listed here can be found in [TDSQL Error Codes](/doc/api/309/7150).

| Error Code | Description |
|---------|---------|
| DbOperationFailed | DB internal failure |
| OssOpertaionFailed | OSS internal failure |
| InstanceAlreadyDeleted | Instance has been deleted |
| InstanceStatusAbnormal | Operation is impossible due to instance status exception (not deleted) |
## 5. Example
Input
<pre>
https://tdsql.api.qcloud.com/v2/index.php?Action=CdbTdsqlSetBackupTime
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
&cdbInstanceId=40746
&sBackupTime=00:00
&eBackupTime=23:59
</pre>
Output
```
{
    "code":"0",
    "message":"",
    "codeDesc":"Success",
    "data":{
        "status":"0"
    }
}
```


