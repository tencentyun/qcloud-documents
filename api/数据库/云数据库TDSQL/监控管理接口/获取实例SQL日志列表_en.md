## 1. API Description
This API (CdbTdsqlGetSqlLogList) is used to acquire the SQL log list of an instance.

Domain for API request: tdsql.api.qcloud.com



## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see <a href='/doc/api/309/7016' title='Common Request Parameters'>Common Request Parameters</a>. The Action field for this API is CdbTdsqlGetSqlLogList.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| cdbInstanceId | Yes | Int | Instance ID |
| offset | Yes | Int | SQL entry offset |
| count | Yes | Int | Number of entries fetched each time (value range: 0-1000. 0 indicates fetching the total number information) |


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. 0: Successful; other values: Failed. For more information, please see <a href='https://cloud.tencent.com/doc/api/309/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81' title='Common Error Codes'>Common Error Codes</a> on the Error Codes page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Error description |
| data | Array | Returned data |
| data.totalCount | Int | Number of SQL logs that can be fetched for the instance |
| data.startOffset | Int | Starting offset of the first SQL entry for the instance |
| data.endOffset | Int | Ending offset of the last SQL entry for the instance |
| data.offset | Int | Starting offset of the returned sqlItems |
| data.count | Int | Number of returned sqlItems |
| data.sqlItems | Array | SQL log data | 

"sqlItems" is composed as follows:

| Parameter Name | Type | Description |
|---------|---------|---------|
| offset | Int | Offset | 
| user | String | SQL user | 
| client | String | SQL source IP port | 
| db | String | Database name | 
| sql | String | SQL statement | 
| selectRowNum | Int | Number of rows returned by SQL | 
| affectRowNum | Int | Number of rows affected by SQL | 
| timestamp | Int | Unix time when the SQL was executed | 
| timeCostMs | Int | Time consumed for the SQL execution | 
| resultCode | Int | Error codes returned after the SQL execution | 
## 4. Error Codes

The following are the common error codes for this API. Other error codes not listed here can be found in [TDSQL Error Codes](/doc/api/309/7150).

| Error Code | Description |
|---------|---------|
| DbOperationFailed | DB internal failure |
| InstanceStatusAbnormal | Operation is impossible due to instance status exception (not deleted) |
| ConnectKafkaFailed | KAFKA connection error |
## 5. Example
Input
<pre>
https://tdsql.api.qcloud.com/v2/index.php?Action=CdbTdsqlGetSqlLogList
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
&openid=12345
&openkey=12345
&pf=qzone
&appid=1252014656
&format=json
&userip.0=10.0.0.1
&offset=22593
&count=10
&cdbInstanceId=10369
</pre>
Output
```
{
    "code":"0",
    "message":"",
    "codeDesc":"Success",
    "data":{
        "totalCount":"22615",
        "startOffset":"0",
        "endOffset":"22615",
        "offset":"0",
        "count":"10",
        "sqlItems":[
            {
                "offset":"22593",
                "user":"testandel",
                "client":"10.207.51.41:59945",
                "db":"test",
                "sql":"create table hehe(id int auto_increment primary key)",
                "selectRowNum":"0",
                "affectRowNum":"0",
                "timestamp":"1477898192",
                "timeCostMs":"2",
                "resultCode":"0"
            },
            {
                "offset":"22594",
                "user":"testandel",
                "client":"10.207.51.41:59945",
                "db":"test",
                "sql":"insert into hehe()",
                "selectRowNum":"0",
                "affectRowNum":"0",
                "timestamp":"1477898197",
                "timeCostMs":"0",
                "resultCode":"1064"
            },
            {
                "offset":"22595",
                "user":"testandel",
                "client":"10.207.51.41:59945",
                "db":"test",
                "sql":"insert into hehe",
                "selectRowNum":"0",
                "affectRowNum":"0",
                "timestamp":"1477898200",
                "timeCostMs":"0",
                "resultCode":"1064"
            },
            {
                "offset":"22596",
                "user":"testandel",
                "client":"10.207.51.41:59945",
                "db":"test",
                "sql":"insert into hehe(id)",
                "selectRowNum":"0",
                "affectRowNum":"0",
                "timestamp":"1477898206",
                "timeCostMs":"0",
                "resultCode":"1064"
            },
            {
                "offset":"22597",
                "user":"testandel",
                "client":"10.207.51.41:59945",
                "db":"test",
                "sql":"insert into hehe() values()",
                "selectRowNum":"0",
                "affectRowNum":"1",
                "timestamp":"1477898212",
                "timeCostMs":"1",
                "resultCode":"0"
            },
            {
                "offset":"22598",
                "user":"testandel",
                "client":"10.207.51.41:59945",
                "db":"test",
                "sql":"insert into hehe() values()",
                "selectRowNum":"0",
                "affectRowNum":"1",
                "timestamp":"1477898212",
                "timeCostMs":"0",
                "resultCode":"0"
            },
            {
                "offset":"22599",
                "user":"testandel",
                "client":"10.207.51.41:59945",
                "db":"test",
                "sql":"insert into hehe() values()",
                "selectRowNum":"0",
                "affectRowNum":"1",
                "timestamp":"1477898213",
                "timeCostMs":"0",
                "resultCode":"0"
            },
            {
                "offset":"22600",
                "user":"testandel",
                "client":"10.207.51.41:59945",
                "db":"test",
                "sql":"insert into hehe() values()",
                "selectRowNum":"0",
                "affectRowNum":"1",
                "timestamp":"1477898213",
                "timeCostMs":"0",
                "resultCode":"0"
            },
            {
                "offset":"22601",
                "user":"testandel",
                "client":"10.207.51.41:59945",
                "db":"test",
                "sql":"insert into hehe() values()",
                "selectRowNum":"0",
                "affectRowNum":"1",
                "timestamp":"1477898213",
                "timeCostMs":"0",
                "resultCode":"0"
            },
            {
                "offset":"22602",
                "user":"testandel",
                "client":"10.207.51.41:59945",
                "db":"test",
                "sql":"insert into hehe() values()",
                "selectRowNum":"0",
                "affectRowNum":"1",
                "timestamp":"1477898213",
                "timeCostMs":"0",
                "resultCode":"0"
            }
        ]
    }
}
```


