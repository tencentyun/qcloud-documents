## 1. 接口描述

域名：catapi.api.qcloud.com
接口：GetCatRespTimeTrend



查询拨测任务的统计数据

## 2. 输入参数

以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见<a href="/doc/api/405/公共请求参数" title="公共请求参数">公共请求参数</a>页面。其中，此接口的Action字段为GetCatRespTimeTrend。

### 2.1输入参数

| 参数名称               | 必选   | 类型     | 输入内容   | 描述                                       |
| ------------------ | ---- | ------ | ------ | ---------------------------------------- |
| taskId             | 是    | Int    | 拨测任务id | 正整数。验证成功的拨测任务id                          |
| date               | 是    | String | 日期     | 统计数据的发生日期。格式如：2017-05-09。1分钟粒度，数据保留最近14天。5、15、30分钟粒度最近30天 |
| dimentions.0.name  | 否    | String | 纬度名称   | 可为 isp 或 province                        |
| dimentions.0.value | 否    | String | 纬度值    | 可为 province的值参见后面的表一，isp 参见表二。province, isp 组合值，应属于taskId 对应的agentGroup 里的运营商集合。参见接口：DescribeCatAgentGroup |
| period             | 是    | Int    | 拨测周期   | 拨测周期。取值可为1,5,15,30之一, 单位：分钟。             |
| metricName         | 否    | String | 指标名    | 可为totalTime, parseTime, connectTime, sendTime, waitTime, receiveTime。缺省为 totalTime |
#### 

## 3. 输出参数

| 参数名称    | 类型     | 描述                  |
| ------- | ------ | ------------------- |
| code    | Int    | 错误码, 0: 成功, 其他值表示失败 |
| message | String | 返回信息                |
| data    | Array  | 结果数据                |

### 3.1 data数据元素 的结构

| 参数名称      | 类型     | 描述                                       |
| --------- | ------ | ---------------------------------------- |
| logTime   | String | 统计时间点。格式：2017-06-16 00:00:00             |
| totalTime | String | 总响应时间。单位: ms。备注：根据metricName 不同，这里的参数名 和输入参数里的metricName 会是一致的。 |



## 4. 错误码表

| 错误代码  | 错误描述                                | 英文描述                          |
| ----- | ----------------------------------- | ----------------------------- |
| 10001 | 输入参数错误。可能是达到最大拨测分组数限制。结合message一起看。 | InvalidParameter              |
| 11000 | DB操作失败                              | InternalError.DBoperationFail |

## 5. 示例

输入

```
taskId=126395&period=5&date=2017-05-24&dimentions.0.province=&dimentions.0.isp=&metricName=totalTime AخA offset=0&limit=5 AخA https://catapi.api.qcloud.com/v2/index.php?& <<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>&Action=GetCatRespTimeTrend
&taskId=126395
&period=5
&date=2017-05-24
&dimentions.0.province=
&dimentions.0.isp=
&metricName=connectTime
```

输出

```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": [
        {
            "logTime": "2017-05-24 00:00:00",
            "connectTime": "66.2000"
        },
        {
            "logTime": "2017-05-24 00:05:00",
            "connectTime": "54.4000"
        },
        ......
    }
}
```