## 1. 接口描述
本接口(CdbTdsqlGetSqlLogList)用于获取实例SQL日志列表。
接口请求域名：<font style='color:red'>tdsql.api.qcloud.com </font>



## 2. 输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见<a href='/doc/api/309/7016' title='公共请求参数'>公共请求参数</a>页面。其中，此接口的Action字段为CdbTdsqlGetSqlLogList。

| 参数名称 | 是否必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| cdbInstanceId | 是 | Int | 实例ID|
| offset | 是 | Int | sql条目偏移量|
| count | 是 | Int | 每次拉取条目数（0-1000，为0时拉取总数信息）|


## 3. 输出参数
| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 公共错误码, 0表示成功，其他值表示失败。详见错误码页面的<a href='https://cloud.tencent.com/doc/api/309/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81' title='公共错误码'>公共错误码</a>。|
| message | String | 模块错误信息描述，与接口相关。|
| codeDesc | String | 英文错误描述 |
| data | Array | 返回数据 |
| data.totalCount | Int | 实例可拉取的sql日志数量 |
| data.startOffset | Int | 实例第一条sql的起始offset |
| data.endOffset | Int | 实例最后一条sql的结束offset |
| data.offset | Int | 返回的sqlItems的起始偏移量 |
| data.count | Int | 返回的sqlItems的数量 |
| data.sqlItems | Array | sql日志数据| 

其中sqlItems包含如下字段：

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| offset | Int | 偏移量| 
| user | String | sql用户| 
| client | String | sql来源IP端口| 
| db | String | 数据库名称| 
| sql | String | sql语句| 
| selectRowNum | Int |  sql返回的行数| 
| affectRowNum | Int |  sql影响的行数| 
| timestamp | Int | sql执行的unix时间| 
| timeCostMs | Int | sql执行的时间耗时| 
| resultCode | Int |  sql执行的返回码| 

## 4. 错误码表

以下是本接口常见的错误码，如果有不在此列的错误请查阅[TDSQL错误码表](/doc/api/309/7150)

| 错误码 | 描述 |
|---------|---------|
| DbOperationFailed | DB内部失败 |
| InstanceStatusAbnormal | 实例状态异常(非删除), 不能进行操作 |
| ConnectKafkaFailed | 链接KAFKA错误 |

## 5. 示例
输入
<pre>
https://tdsql.api.qcloud.com/v2/index.php?Action=CdbTdsqlGetSqlLogList
&<<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>
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
输出
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

