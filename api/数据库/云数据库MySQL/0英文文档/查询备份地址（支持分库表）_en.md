## 1. API Description
This API (GetExportBackupUrl) is used to query the download address of a backup, and supports obtaining the download address of a backup through a specified database table.
Domain for API request: <font style='color:red'>cdb.api.qcloud.com </font>

1. Addresses for downloading in private networks and local download addresses have a validity period of 12 hours, and need to be reacquired in case of expiration;
2. English quotation marks need to be added to URL when wget is used for downloading;
3. It supports the downloading of only database table structures and data contents, and temporarily you cannot download views, storage procedures, user-defined functions or triggers etc.


## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters are also needed when API is called. For more information, please refer to <a href='/document/product/236/6921' title='Common Request Parameters'>Common Request Parameters</a>. The Action field for this API is GetExportBackupUrl.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| cdbInstanceId | Yes | String | Instance ID, such as: cdb-c1nl9rpv. It is identical to the instance ID displayed in the Cloud Database console page and can be obtained using API [Query List of Instances](/doc/api/253/1266). Its value equals to the uInstanceId field value in the output parameter.  |
| date | Yes | String |Backup time, with the time format: 2015-11-05 02:18:23; it can be obtained through [Query Backups and Logs](/doc/api/253/4691) API |
| dbTableList | Yes | Array | Database table content; array is converted to JSON string, with format such as [{"dbname":"test1","tableList":[]},{"dbname":"mysql","tableList":["general_log","slow_log"]}] |

The dbTableList parameter is constucted as follows: 

| Parameter Name | Type | Description |
|---------|---------|---------|
| dbname | String | Database name | 
| tableList | Array | Database table | 


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please refer to <a href='https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81' title='Common Error Codes'>Common Error Codes</a> on the Error Code page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Error code description|
| data | Array | Backup data |

The data parameter is constructed as follows:

| Parameter Name | Type | Description |
|---------|---------|---------|
| file_name | String | Name of the backup file | 
| size | Int | Size of the backup file in bytes | 
| date | String | Backup time of the snapshot, with time format: 2016-07-06 01:04:54 | 
| in_url | String | Download address in the private network; only obtaining it on CVM is supported; its validity period is 12 hours, and reacquisition is needed in case of expiration |
| type | String | Specific type of log; possible values are mysql (logic cold backup), xtrabackup (physical cold backup), binlog (binary log), and slowlog (slow query log) | 


## 4. Error Codes
The following error codes only include the business logic error codes for this API.

| Error Code | Error Message | Error Description |
|---------|---------|---------|
| 9000 | SystemError | System internal error |
| 9003 | InvalidParameter | Incorrect parameter |
| 9006 | InternalError | Database internal error |
| 9013 | InternalError | System internal error |
| 9016 | InternalError | DES system internal error |
| 9544 | OperationDenied | Instance does not exist |
| 9572 | InstanceNotExists | Instance does not exist |
| 9576 | OperationDenied | Unable to operate because the instance is not running |
| 9593 | IncorrectInstanceStatus | Abnormal instance status|


## 5. Example
Input
<pre>
https://cdb.api.qcloud.com/v2/index.php?Action=GetExportBackupUrl
&<<a href="/document/product/236/6921">Common request parameters</a>>
&cdbInstanceId=cdb-c1nl9rpv
&date=2016-07-06 01:04:54
&dbTableList=[{"dbname":"test1","tableList":[]},{"dbname":"mysql","tableList":["general_log","slow_log"]}]
</pre>

Output
```
{
    "code":"0",
    "message":"",
    "codeDesc":"Success",
    "data":[
        {
            "file_name":"cdb154153_backup_2016-07-06 01:04:54",
            "size":"671224",
			"type":"mysql",
            "date":"2016-07-06 01:04:54",
            "in_url":"http://gz.dl.cdb.tencentyun.com/**?appid=1351000042&time=1467971011&sign=ChupJ1dMt8W%2BcYHLlYGAE6ccEnk%3D&dbtbcode=272"
        }
    ]
}
```


