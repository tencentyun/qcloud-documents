## 1. 接口描述

域名：catapi.api.qcloud.com
接口：DescirbeCatAlarmList



查询拨测告警列表

## 2. 输入参数

以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见<a href="/doc/api/405/公共请求参数" title="公共请求参数">公共请求参数</a>页面。其中，此接口的Action字段为DescirbeCatAlarmList。

### 2.1输入参数

| 参数名称      | 必选   | 类型     | 输入内容    | 描述                                      |
| --------- | ---- | ------ | ------- | --------------------------------------- |
| beginTime | 否    | String | 告警的起始时间 | 格式如：2017-05-09 00:00:00  缺省为7天前0点       |
| endTime   | 否    | String | 告警的截至时间 | 格式如：2017-05-10 00:00:00  缺省为明天0点        |
| offset    | 否    | Int    | 偏移量     | 从第offset 条开始查询。缺省值为0                    |
| limit     | 否    | Int    | 每页多少条   | 本批次查询limit 条记录。缺省值为20                   |
| status    | 否    | Int    | 告警状态    | 0 全部, 1 已恢复, 2 未恢复  默认为0。其他值，视为0 查全部状态。 |
#### 

## 3. 输出参数

| 参数名称    | 类型     | 描述                  |
| ------- | ------ | ------------------- |
| code    | Int    | 错误码, 0: 成功, 其他值表示失败 |
| message | String | 返回信息                |
| data    | Array  | 结果数据                |

### 3.1 data 的结构

| 参数名称      | 类型    | 描述       |
| --------- | ----- | -------- |
| total     | Int   | 总共的接收组数目 |
| alarmInfo | Array | 告警列表     |

#### 3.1.1 告警接收组  的结构  

| 参数名称           | 类型     | 描述                         |
| -------------- | ------ | -------------------------- |
| firstOccurTime | String | 告警发生时间                     |
| objName        | String | 告警对象                       |
| lastOccurTime  | String | 告警结束时间（如果和告警发生时间相同，表示尚未结束） |
| okStatus       | Int    | 1 表示已恢复。0 表示未恢复            |
| content        | String | 告警的内容                      |



## 4. 错误码表

| 错误代码  | 错误描述                                | 英文描述                          |
| ----- | ----------------------------------- | ----------------------------- |
| 10001 | 输入参数错误。可能是达到最大拨测分组数限制。结合message一起看。 | InvalidParameter              |
| 11000 | DB操作失败                              | InternalError.DBoperationFail |

## 5. 示例

输入

```
offset=0&limit=5 AخA https://catapi.api.qcloud.com/v2/index.php?& <<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>&Action=DescirbeCatAlarmList
&offset=0
&limit=5
```

输出

```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "total": 10,
    "alarmInfo": [
        {
            "firstOccurTime": "2017-05-24 16:57:00",
            "objName": "keke_test_hk",
            "lastOccurTime": "2017-05-24 17:00:00",
            "okStatus": 1,
            "content": "当前可用率0.0%,请检查您的服务是否正常"
        },
        {
            "firstOccurTime": "2017-05-24 19:46:00",
            "objName": "keke_test_hk",
            "lastOccurTime": "2017-05-24 19:48:00",
            "okStatus": 1,
            "content": "当前可用率72.73%,共有6个拨测点低于平均值,最低(江西移动:0.0%)"
        }
    ]
}
```