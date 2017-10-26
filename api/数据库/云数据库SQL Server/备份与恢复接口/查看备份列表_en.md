## 1. API Description
This API (ListBackup) is used to view backup list.
Domain for API request: sqlserver.api.qcloud.com



## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see<a href='https://cloud.tencent.com/document/api/238/7328
' title='Common Request Parameters'>Common Request Parameters</a>. The Action field for this API is ListBackup.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| resourceId | Yes | String | Instance ID |
| startTime | Yes | String | Start time (yyyy-MM-dd HH:mm:ss) |
| endTime | Yes | String | End time (yyyy-MM-dd HH:mm:ss) |
| pageSize | No | Int | Page size |
| pageNo | No | Int | Page number |


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. 0: Successful; other values: Failed. For more information, please see <a href='https://cloud.tencent.com/doc/api/238/7334#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81' title='Common Error Codes'>Common Error Codes</a> on the Error Codes page. |
| message | String | Module error message description depending on API. |
| data | Array | Returned data |

Parameter data is composed as follows:

| Parameter Name | Type | Description |
|---------|---------|---------|
| totalCount | Int | Total number of backups |
| backupList | Array | Details of backup list |

Parameter backupList is composed as follows:

| Parameter Name | Type | Description |
|---------|---------|---------|
| fileName | String | File name | 
| size | Int | File size (in KB) | 
| startTime | String | Start time of the backup | 
| endTime | String | End time of the backup | 
| internalAddr | String | Download address in the private network | 
| externalAddr | String | Download address in the public network | 
 
## 4. Error Codes

| Error Code | Error Message | Error Description |
|---------|---------|---------|
| 50 | InstanceNotFound | Instance does not exist |
| 1000 | SystemError | System error. Contact customer service. |
| 1002 | DBConnectError | Database connection error |
| 1005 | CreateFlowFailed | Failed to create task flow |

## 5. Example
Input
<pre>
https://sqlserver.api.qcloud.com/v2/index.php?Action=ListBackup
&<<a href="https://cloud.tencent.com/document/api/238/7328">Common request parameters</a>>
&resourceId=mssql-q6g71pcf
&startTime=2016-09-27 00:00:00
&endTime=2016-09-28 00:00:00
&pageSize=10
&pageNo=0
</pre>
Output
```
{
    "code":"0",
    "message":"",
    "data":{
        "backupList":[
            {
                "fileName":"backup_540316.tar",
                "size":"1440",
                "startTime":"2016-09-27 02:03:15",
                "endTime":"2016-09-27 02:21:45",
                "internalAddr":"http://10.66.185.141:58366/download/backup_540316.tar?YJW3gzNLKt2LCrywP9JslJXZo6TXiqprJ6x+tRJfDqzPsYYttIeozrDQeh2yfY/Dq/8OltqtK/+Bg3+plnNy5TzRhaYuCh+DpYehlAXVPBHPARU+zHUfxGkimTw+RxB5BBmgF/TTvwQXHfyjCr2DnQ==",
                "externalAddr":"http://119.29.47.51:9097/download/backup_540316.tar?YJW3gzNLKt2LCrywP9JslJXZo6TXiqprJ6x+tRJfDqzPsYYttIeozrDQeh2yfY/Dq/8OltqtK/+Bg3+plnNy5TzRhaYuCh+DpYehlAXVPBHPARU+zHUfxGkimTw+RxB5BBmgF/TTvwQXHfyjCr2DnQ=="
            }
        ],
        "totalCount":"1"
    }
}
```


