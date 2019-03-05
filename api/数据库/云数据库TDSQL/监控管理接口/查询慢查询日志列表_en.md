## 1. API Description
This API (CdbTdsqlGetSlowLogList) is used to query the list of slow logs.

Domain for API request: tdsql.api.qcloud.com



## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see [Common Request Parameters](https://cloud.tencent.com/document/api/213/6976
). The Action field for this API is CdbTdsqlGetSlowLogList.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| cdbInstanceId | Yes | Int | Instance ID |
| start | Yes | Int | Starting offset of the first data entry of the returned results |
| num | Yes | Int | Number of results to be returned |
| startTime | No | datetime | Start time for the query, such as: 2016-07-23 14:55:20 |
| endTime | No | datetime | End time for the query, such as: 2016-08-22 14:55:20 |
| db | No | String | Name of the database to be queried |
| orderBy | No | String | Sorting field (query_time_sum or query_count) |
| orderByType | No | String | Sorting type (desc or asc) |


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. 0: Successful; other values: Failed. For more information, please see <a href='https://cloud.tencent.com/doc/api/309/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81' title='Common Error Codes'>Common Error Codes</a> on the Error Codes page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Error description |
| data | Array | Returned data |
| data.data | Array | Data | 
| data.data.checksum | String | Statement checksum used for querying details | 
| data.data.db | String | Database name | 
| data.data.fingerprint | String | Abstract SQL statement | 
| data.data.lock_time_avg | String | Average lock time | 
| data.data.lock_time_max | String | Maximum lock time | 
| data.data.lock_time_min | String | Minimum lock time | 
| data.data.lock_time_sum | String | Total lock time | 
| data.data.query_count | String | Count of queries | 
| data.data.query_time_avg | String | Average query time | 
| data.data.query_time_max | String | Maximum query time | 
| data.data.query_time_min | String | Minimum query time | 
| data.data.query_time_sum | String | Total query time | 
| data.data.rows_examined_sum | String | Number of rows examined | 
| data.data.rows_sent_sum | String | Number of rows sent | 
| data.data.ts_max | String | Time of first execution | 
| data.data.ts_min | String | Time of last execution | 
| data.data.user | String | Account | 
| data.lock_time_sum | Int | Total lock time for all statements | 
| data.query_count | Int | Total count of queries for all statements | 
| data.query_time_sum | String | Total query time for all statements | 
| data.total | Int | Total number of logs | 
## 4. Error Codes

The following are the common error codes for this API. Other error codes not listed here can be found in [TDSQL Error Codes](/doc/api/309/7150).

| Error Code | Description |
|---------|---------|
| IllegalTime | Invalid time parameter |
| DbOperationFailed | DB internal failure |
| EINSTANCEDELETED | Instance has been deleted |
| InstanceStatusAbnormal | Operation is impossible due to instance status exception (not deleted) |
| GetInstanceInfoFailed | Failed to acquire instance information |
| LogDBFailed | logDB API error |
## 5. Example
Input
<pre>
https://tdsql.api.qcloud.com/v2/index.php?Action=CdbTdsqlGetSlowLogList
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
&cdbInstanceId=10338
&start=0
&num=20
&begin=2016-08-10
&end=2016-08-23
</pre>
Output
```
{
    "code":"0",
    "message":"",
    "codeDesc":"Success",
    "data":{
        "data":[
            {
                "checksum":"14090621765287179955",
                "db":"",
                "fingerprint":"replace into sysdb.statustable set ts = from_unixtime(?),ip=?,port=?",
                "lock_time_avg":"0.00",
                "lock_time_max":"0.00",
                "lock_time_min":"0.00",
                "lock_time_sum":"0.00",
                "query_count":"1",
                "query_time_avg":"1.13",
                "query_time_max":"1.13",
                "query_time_min":"1.13",
                "query_time_sum":"1.13",
                "rows_examined_sum":"0.00",
                "rows_sent_sum":"0.00",
                "ts_max":"2016-08-06 11:32:10",
                "ts_min":"2016-08-06 11:32:10",
                "user":"agent"
            }
        ],
        "lock_time_sum":"0",
        "query_count":"1",
        "query_time_sum":"1.13",
        "total":"1"
    }
}
```


