## 1. 接口描述

域名：catapi.api.qcloud.com
接口：GetCatReturnCodeHistory



查询拨测任务的历史返回码信息

## 2. 输入参数

以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见<a href="/doc/api/405/公共请求参数" title="公共请求参数">公共请求参数</a>页面。其中，此接口的Action字段为GetCatReturnCodeHistory。

### 2.1输入参数

| 参数名称      | 必选   | 类型     | 输入内容    | 描述                                       |
| --------- | ---- | ------ | ------- | ---------------------------------------- |
| taskId    | 是    | Int    | 拨测任务id  | 正整数。验证成功的拨测任务id                          |
| beginTime | 是    | String | 告警的起始时间 | 格式如：2017-05-09 00:00:00                  |
| endTime   | 是    | String | 告警的截至时间 | 格式如：2017-05-10 00:00:00                  |
| province  | 否    | String | 省份      | 取值范围，参见下表1 中的province 列。province, 应属于taskId 对应的agentGroup 里的运营商集合所在的省份。参见接口：DescribeCatAgentGroup |
#### 

## 3. 输出参数

| 参数名称    | 类型     | 描述                  |
| ------- | ------ | ------------------- |
| code    | Int    | 错误码, 0: 成功, 其他值表示失败 |
| message | String | 返回信息                |
| data    | Array  | 结果数据                |

### 3.1 data 的结构

| 参数名称    | 类型    | 描述    |
| ------- | ----- | ----- |
| details | Array | 返回码信息 |

#### 3.1.1 各运营商的返回码  的结构  

| 参数名称         | 类型     | 描述                                 |
| ------------ | ------ | ---------------------------------- |
| ispName      | String | 运营商名称                              |
| province     | String | 省份                                 |
| provinceName | String | 省份中文                               |
| serverIp     | String | 服务端ip                              |
| resultCount  | String | 失败次数                               |
| errorReason  | String | 失败原因                               |
| resultCode   | Int    | 返回码                                |
| startTime    | String | 错误发生，起始时间  格式如：2017-05-11 02:08:00 |
| endTime      | String | 错误发生，截至时间  格式如：2017-05-11 02:08:00 |



## 4. 错误码表

| 错误代码  | 错误描述                                | 英文描述                          |
| ----- | ----------------------------------- | ----------------------------- |
| 10001 | 输入参数错误。可能是达到最大拨测分组数限制。结合message一起看。 | InvalidParameter              |
| 11000 | DB操作失败                              | InternalError.DBoperationFail |

## 5. 示例

输入

```
offset=0&limit=5 AخA https://catapi.api.qcloud.com/v2/index.php?& <<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>&Action=GetCatReturnCodeHistory
&taskId=126531
&beginTime=2017-05-25 00:00
&endTime=2017-05-25 08:10
&province=jiangxi
```

输出

```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "detail": [
            {
                "ispName": "移动",
                "province": "jiangxi",
                "provinceName": "江西",
                "mapKey": "jiangXi",
                "serverIp": "119.28.20.246",
                "resultCount": 982,
                "resultCode": 10016,
                "errorReason": "Ping超时"
            }
        ],
        "summary": [
            {
                "resultCount": 982,
                "errorReason": "Ping超时",
                "resultCode": 10016
            }
        ],
        "startTime": "2017-05-25 00:00:00",
        "endTime": "2017-05-25 08:10:00"
    }
}
```