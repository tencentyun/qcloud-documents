## 1. 接口描述
域名:monitor.api.qcloud.com
接口名:DescribeAlarmRuleByObject

查询指定对象绑定的告警规则

## 2. 输入参数
| 参数名称 | 必选  | 类型 | 描述 |来源|
|---------|---------|---------|---------|---------|
| Action | 是 | String | 操作接口名|系统规定参数，此处取值：DescribeAlarmRuleByObject|
| namespace | 是 | string | 命名空间|调用<a href="/doc/api/255/查询命名空间" title="查询命名空间">查询命名空间</a>(DescribeNamespace)接口查询|
| metricName | 是 | String | 指标名|调用<a href="/doc/api/255/查询指标" title="查询指标">查询指标</a>(DescribeMetric)接口查询|
| dimensions.n.name | 是 | array | 维度组合的key|调用<a href="/doc/api/255/查询指标对象列表" title="查询指标对象列表">查询指标对象列表</a>(DescribeObjects)接口查询|
| dimensions.n.value | 是 | array | 维度组合的value|调用<a href="/doc/api/255/查询指标对象列表" title="查询指标对象列表">查询指标对象列表</a>(DescribeObjects)接口查询|
| offset | 否 | int | 偏移，默认0 |用户自定义|
| limit	 | 否 | int | 默认30，这里实际获取的是偏移offset开始，取limit 条记录 |用户自定义|

## 3. 输出参数
| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 错误码, 0: 成功, 其他值: 失败|
| message | String | 错误信息|
| data | Array | 返回结果 |

data内容：

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
|ruleList | Array | 告警规则绑定的对象列表(每个数组元素是一个具体的对象描述，见示例)| 
|total|Int|返回的ruleList条数|

ruleList内容：

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| alarmRuleId | String | 告警规则id|
| namespace | String | 命名空间|
| metricName | String | 指标名|
| dimensionGroup | String|维度组合名称|
| operatorType| String | 操作符| 
| threshold | Int | 触发异常的数目阈值|
| constancy | Int | 表明异常持续多少个周期会触发告警| 
| period | Int | 统计周期,目前只能填写300s|
| statistics | Enum | 统计方式，取值为(sum, last, avg, min, max)|
| receiversId | string | 告警接收组id|

## 4. 示例
输入
<pre>
https://monitor.api.qcloud.com/v2/index.php?Action=DescribeAlarmRuleByObject
&namespace=name1
&metricName=metric0
&dimensions.0.name=name
&dimensions.0.value=a1
&<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>
</pre>
输出
```
{
    "code": 0,
    "message": "",
    "data": {
        "ruleList": [
            {
                "alarmRuleId": "policy-1qiq3aibqz",
                "namespace": "name1",
                "metricName": "metric0",
                "dimensionGroup": "name",
                "operatorType": ">",
                "threshold": "20",
                "constancy": "2",
                "period": "300",
                "statistics": "sum",
                "receiversId": "9758"
            },
            {
                "alarmRuleId": "policy-koprfomozb",
                "namespace": "name1",
                "metricName": "metric0",
                "dimensionGroup": "name",
                "operatorType": ">",
                "threshold": "50",
                "constancy": "2",
                "period": "300",
                "statistics": "sum",
                "receiversId": "0"
            }
        ],
        "total": "2"
    }
}
```

