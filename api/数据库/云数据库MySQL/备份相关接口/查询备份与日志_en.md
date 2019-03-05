## 1. API Description
This API (GetCdbExportLogUrl) is used to query the download addresses of data and logs of cloud database instances.
Domain for API request: <font style="color:red">cdb.api.qcloud.com</font>


## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href='/doc/api/253/1739' title='Common Request Parameters'>Common Request Parameters</a>. The Action field for this API is GetCdbExportLogUrl.

| Parameter Name | Required  | Type | Description |
|---------|---------|---------|---------|
| cdbInstanceId | Yes | String | Instance ID, such as: cdb-c1nl9rpv. It is identical to the instance ID displayed in the Cloud Database console page and can be obtained using API [Query List of Instances](/doc/api/253/1266). Its value equals to the uInstanceId field value in the output parameter.  |
| type | Yes | String | Log type; passable value: coldbackup (cold backup), binlog (binary log) and slowlog_day (slow query log) |


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please refer to <a href='https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81' title='Common Error Codes'>Common Error Codes</a> on the Error Code page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Error description |
| data | Array | Returned collection of export addresses|
The data parameter is constructed as follows:

| Parameter Name | Type | Description |
|---------|---------|---------|
| data.file_name | String | Name of the backup file | 
| data.size | Int | Size of the backup file in bytes | 
| data.date | String | Backup time of the snapshot, with time format: 2016-03-17 02:10:37 | 
| data.in_url | String | Download address in the private network | 
| data.type | String | Specific type of log; possible values are mysql (logic cold backup), xtrabackup (physical cold backup), binlog (binary log), and slowlog (slow query log) | 


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
https://cdb.api.qcloud.com/v2/index.php?Action=GetCdbExportLogUrl
&<<a href="/document/product/236/6921">Common request parameters</a>>
&cdbInstanceId=cdb-c1nl9rpv
&type=coldbackup
</pre>

Output
```
{
    "code":"0",
    "message":"",
    "codeDesc":"Success",
    "data":[
        {
            "file_name":"%E6%B5%8B%E8%AF%952_backup_2016-03-17",
            "size":"14131139",
            "type":"mysql",
            "date":"2016-03-17 02:10:37",
            "in_url":"http://gz.dl.cdb.tencentyun.com:33003/5822923d304b5083c3e63a916177b9?appid=1251004065&time=1458551053&sign=SbPKB1kKmn2eVZjSzm5sk7zPpnU%3D"
        },
        {
            "file_name":"%E6%B5%8B%E8%AF%952_backup_2016-03-18",
            "size":"14132919",
            "type":"mysql",
            "date":"2016-03-18 02:17:01",
            "in_url":"http://gz.dl.cdb.tencentyun.com:33003/865591074008fe3a04d4d5798b21f3?appid=1251004065&time=1458551053&sign=sPnnfyTq%2BU%2FIbMYKpVLce1c14Mc%3D"
        },
        {
            "file_name":"%E6%B5%8B%E8%AF%952_backup_2016-03-19",
            "size":"14178767",
            "type":"mysql",
            "date":"2016-03-19 02:33:27",
            "in_url":"http://gz.dl.cdb.tencentyun.com:33003/98a1bf8851ecc90f2d68ed150275f1?appid=1251004065&time=1458551053&sign=Q5zlJu0kRhTOr9Vmfpu%2B0MbYDyo%3D"
        },
        {
            "file_name":"%E6%B5%8B%E8%AF%952_backup_2016-03-20",
            "size":"14201855",
            "type":"mysql",
            "date":"2016-03-20 01:58:37",
            "in_url":"http://gz.dl.cdb.tencentyun.com:33003/3e21316c7a4ba8b2cba2748ce89df4?appid=1251004065&time=1458551053&sign=jAwb%2ByBMXcQUggjIiawmwHiSk0w%3D"
        },
        {
            "file_name":"%E6%B5%8B%E8%AF%952_backup_2016-03-21",
            "size":"14213659",
            "type":"mysql",
            "date":"2016-03-21 02:01:23",
            "in_url":"http://gz.dl.cdb.tencentyun.com:33003/31b07c76e8fe83d8b733ae5079bc2c?appid=1251004065&time=1458551053&sign=ij6QVPnU3NBxAWKKz1ROGa%2FO6IU%3D"
        }
    ]
}
```


