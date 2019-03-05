## 1. 接口描述

域名：catapi.api.qcloud.com
接口：DescribeCatTaskList



查询拨测任务列表

## 2. 输入参数

以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见<a href="/doc/api/405/公共请求参数" title="公共请求参数">公共请求参数</a>页面。其中，此接口的Action字段为DescribeCatTaskList。

### 2.1输入参数

| 参数名称   | 必选   | 类型   | 输入内容 | 描述                    |
| ------ | ---- | ---- | ---- | --------------------- |
| offset | 否    | Int  | 起始条数 | 从第offset 条开始查询。缺省值为0  |
| limit  | 否    | Int  | 一批条数 | 本批次查询limit 条记录。缺省值为20 |
#### 

## 3. 输出参数

| 参数名称    | 类型     | 描述                  |
| ------- | ------ | ------------------- |
| code    | Int    | 错误码, 0: 成功, 其他值表示失败 |
| message | String | 返回信息                |
| data    | Array  | 结果数据                |

### 3.1 data 的结构

| 参数名称  | 类型    | 描述          |
| ----- | ----- | ----------- |
| total | Int   | 当前用户总的拨测任务数 |
| tasks | Array | 本批拨测任务列表    |

#### 3.1.1 拨测任务  的结构  

| 参数名称               | 类型     | 描述                               |
| ------------------ | ------ | -------------------------------- |
| taskId             | Int    | 任务id                             |
| taskName           | String | 任务名称                             |
| period             | Int    | 任务周期                             |
| catTypeName        | String | 拨测类型                             |
| status             | Int    | 任务状态  1 暂停, 2 激活                 |
| cgiUrl             | String | 拨测地址                             |
| addTime            | String | 任务创建的时间  格式如：2017-05-16 10:00:00 |
| availRatioThres    | Int    | 告警的可用率门限                         |
| availRatioInterval | Int    | 告警的可用率持续时间                       |
| receiverGroupId    | Int    | 告警接收组                            |

##### 

## 4. 错误码表

| 错误代码  | 错误描述                                | 英文描述                          |
| ----- | ----------------------------------- | ----------------------------- |
| 10001 | 输入参数错误。可能是达到最大拨测分组数限制。结合message一起看。 | InvalidParameter              |
| 11000 | DB操作失败                              | InternalError.DBoperationFail |

## 5. 示例

输入

```
https://catapi.api.qcloud.com/v2/index.php?
& <<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>
&Action=DescribeCatTaskList
&offset=0
&limit=20
```

输出

```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "total": 18,
    "tasks": [
        {
            "taskId": 24418,
            "taskName": "keke_test_pop3",
            "period": 5,
            "catTypeName": "pop3",
            "status": 2,
            "cgiUrl": "pop.qq.com",
            "addTime": "2017-05-10 17:29:15",
            "receiverGroupId": 9063,
            "availRatioThres": 90,
            "availRatioInterval": 15
        },
        {
            "taskId": 24420,
            "taskName": "test_ftp_keke2",
            "period": 5,
            "catTypeName": "ftp",
            "status": 2,
            "cgiUrl": "115.159.142.79",
            "addTime": "2017-05-11 14:38:38",
            "receiverGroupId": null,
            "availRatioThres": null,
            "availRatioInterval": null
        },
        ......
    ]
}
```