## 1. API Description
This API (CdbTdsqlGetBackupTime) is used to obtain custom backup time.
Domain for API request: tdsql.api.qcloud.com



## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see <a href='/doc/api/309/7016' title='Common Request Parameters'>Common Request Parameters</a>. The Action field for this API is CdbTdsqlGetBackupTime.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| cdbInstanceIds.n (cdbInstanceIds is an array. The input parameters here are the array parameters) | Yes | String | Instance IDs to be fetched, with n starting with 0 |


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. 0: Successful; other values: Failed. For more information, please see <a href='https://cloud.tencent.com/doc/api/309/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81' title='Common Error Codes'>Common Error Codes</a> on the Error Codes page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Error message |
| data | Array | Returned data |
| data.instances | Array | Returned instance list | 
| data.instances.id | Int | Instance ID | 
| data.instances.uuid | String | Instance UUID | 
| data.instances.sbackuptime | String | Start time of daily backup time span. The actual start time may be slightly different from this value. | 
| data.instances.ebackuptime | String |End time of daily backup time span. The actual end time may be slightly different from this value | 
## 4. Error Codes

The following are the common error codes for this API. Other error codes not listed here can be found in [TDSQL Error Codes](/doc/api/309/7150).

| Error Code | Description |
|---------|---------|
| DbOperationFailed | DB internal failure |
| OssOpertaionFailed | OSS internal failure |
| OSSGetInstanceError | Error occurs while OSS is obtaining instance information |
| InnerSystemError | Internal system error (unrelated to service) |
## 5. Example
Input
<pre>
https://tdsql.api.qcloud.com/v2/index.php?Action=CdbTdsqlGetBackupTime
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
&cdbInstanceIds.0=40746
</pre>
Output
```
{
    "code":"0",
    "message":"",
    "codeDesc":"Success",
    "data":{
        "totalCnt":"1",
        "instances":[
            {
                "id":"40746",
                "uuid":"tdsql-33y5ai5p",
                "sbackuptime":"00:00",
                "ebackuptime":"23:59"
            }
        ]
    }
}
```


