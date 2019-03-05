## 1. 接口描述
域名:monitor.api.qcloud.com
接口名:DescribeAlarmRuleList

查询告警规则列表

## 2. 输入参数
| 参数名称 | 必选  | 类型 | 描述 |来源|
|---------|---------|---------|---------|---------|
| Action | 是 | String | 操作接口名|系统规定参数，此处取值：DescribeAlarmRuleList|
| namespace | 是 | String | 名字空间|调用<a href="/doc/api/255/查询命名空间" title="查询命名空间">查询命名空间</a>(DescribeNamespace)接口查询|
| metricName | 否 | string	| 指标名，不填则返回这个命名空间下所有的规则|调用<a href="/doc/api/255/查询指标" title="查询指标">查询指标</a>(DescribeMetric)接口查询|
| offset | 否 | Int | 分页偏移，默认0|用户自定义|
| rows | 否 | Int | 默认30，这里实际获取的是偏移offset开始，取limit 条记录|用户自定义|



## 3. 输出参数
| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 错误码, 0: 成功, 其他值: 失败|
| message | String | 错误信息|
| data | Array | 当有额外的返回信息时，有该字段 |

data字段的内容：

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| ruleList | Array | 具体告警规则内容|
| total | Int | 规则条数|

ruleList字段的内容：

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| policyId | String | 告警规则Id|
| namespace | String | 命名空间|
| metricName | String | 命名空间|
| dimensionKeys | String | 命名空间|
| operatorType | String | 操作符|
| threshold | Int | 阈值|
| period | Int | 统计周期|
| receiversId | Int | 告警接收组Id |
| isWild | Int | 是否为通配规则|


## 4. 示例
输入
<pre>
https://monitor.api.qcloud.com/v2/index.php?Action= DescribeAlarmRuleList
&namespace=name1
&<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>
</pre>
输出
```
{
    "code":"0",
    "message":"",
    "data":{
        "ruleList":[
            {
							“policyId”: “policy-f3h1bxvcsb”, 			//告警规则Id
							“namespace”:”name1”, 					//命名空间
							“metricName”:”metric1”,					//指标名
							“dimensionKeys”:”xxx”,					//dimensionKey组合
							“operatorType”:”>”, 					//操作符
							“threshold”: 10,    					//阈值
							“constancy”:2,						//告警周期
							“period”:300,							//统计周期
							“receiversId”: “123”, 					//告警接收组Id 
							“isWild”: 0 							//是否为通配规则
            }
        ],
        "total":"1"
    }
}
```

