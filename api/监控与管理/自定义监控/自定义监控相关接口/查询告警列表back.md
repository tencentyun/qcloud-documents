## 1. 接口描述
域名:monitor.api.qcloud.com
接口名:DescribeAlarmList

查询告警列表

## 2. 输入参数
| 参数名称 | 必选  | 类型 | 描述 |来源|
|---------|---------|---------|---------|---------|
| Action | 是 | String | 操作接口名|系统规定参数，此处取值：DescribeAlarmList|
| namespace | 否 | String | 名字空间|调用<a href="/doc/api/255/查询命名空间" title="查询命名空间">查询命名空间</a>(DescribeNamespace)接口查询|
| metricName | 否 | String | 指标名|调用<a href="/doc/api/255/查询指标" title="查询指标">查询指标</a>(DescribeMetric)接口查询|
| dimensions.n.name | 否 | string | 维度组合的key部分，与value共同标识一个具体的对象，若不填则查询所有对象的告警|调用<a href="/doc/api/255/查询指标对象列表" title="查询指标对象列表">查询指标对象列表</a>(DescribeObjects)接口查询|
| dimensions.n.value | 否 | string | 维度组合的value部分|调用<a href="/doc/api/255/查询指标对象列表" title="查询指标对象列表">查询指标对象列表</a>(DescribeObjects)接口查询|
| starttime | 否 | datetime | 起始时间默认时间为当天的00:00|用户自定义|
| endtime | 否 | datetime | 结束时间默认时间为当前时间|用户自定义|
| offset | 否 | int | 偏移，默认0|用户自定义|
| limit | 否 | 	int	 | 默认30,这里实际获取的是偏移offset开始,取limit 条记录 |用户自定义|

填写metricName时，需要填写namespace
其中 dimensions.n.name和dimensions.n.value成对出现，当填写dimensions.n.name和dimensions.n.value时需要填写metricName和namespace
starttime和endtime成对出现。


## 3. 输出参数
| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 错误码, 0: 成功, 其他值: 失败|
| message | String | 错误信息,当成功时为空|
| data | Array | 当有额外的返回信息时，有该字段 |


data的内容：

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| alarmList | Array | 告警列表|
| total | Int |告警的条数|

alarmList的内容：

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
|metricName|	string|	告警相关的指标名|
|namespace|	string	|告警相关的命名空间|
|object|	string	|告警相关的对象字串|
|occurTime| string	|告警发生时间|
|recoverTime| string |	告警恢复时间|
|sendStatus|	int	|告警是否发送成功 0 成功 非0，未成功|
|okStatus|	int |	是否恢复 0.未恢复 1.已恢复 2.超时恢复|
|smsSendCnt|	int |	告警短信的发送条数|
|content|	string	|告警内容|
|alarmRuleId	|string	|告警相关的规则ID|


## 4. 示例
输入
<pre>
https://monitor.api.qcloud.com/v2/index.php?Action= DescribeAlarmList
&namespace=name1
&metricName= metric1
&<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>
</pre>
输出
```
{
    "code": 0,
    "message": "",
    "data": {
        "alarmList": [
            {
                "metricName": "metric1",
                "namespace": " name1",
                "object": "ip=1.2.3.6&name=a1&uuid=abcde",
                "occurTime": "2016-02-23 11:10:00",
                "recoverTime": "2016-02-23 11:13:00",
                "sendStatus": "0",
                "okStatus": "1",
                "smsSendCnt": "1",
				"alarmRuleId": "policy-f3h1bxvcsb",
"content": "xxxx > 30kb "
            },
            {
                "metricName": "metric1",
                "namespace": " name1",
                "object": "ip=1.2.3.6&name=a1&uuid=abcde",
                "occurTime": "2016-02-23 11:10:00",
                "recoverTime": "2016-02-23 11:13:00",
                "sendStatus": "0",
                "okStatus": "1",
                "smsSendCnt": "1"
				"alarmRuleId": " policy-f3h1bxvacd",
"content": "xxxx > 20 count"

            },
        ],
        "total": "2"
    }
}
```

