## 1. 接口描述
域名:monitor.api.qcloud.com
接口名:DescribeAlarmRuleObjects

查询告警规则绑定的对象

## 2. 输入参数
| 参数名称 | 必选  | 类型 | 描述 |来源|
|---------|---------|---------|---------|---------|
| Action | 是 | String | 操作接口名|系统规定参数，此处取值：DescribeAlarmRuleObjects|
| alarmRuleId | 是 | String | 规则ID|调用<a href="/doc/api/255/查询告警规则" title="查询告警规则">查询告警规则</a>(DescribeAlarmRuleList)接口查询|
| offset | 否 | int | 偏移，默认0|用户自定义|
| limit | 否 | int	 | 默认30，这里实际获取的是偏移offset开始，取limit 条记录|用户自定义|


## 3. 输出参数
| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 错误码, 0: 成功, 其他值: 失败|
| message | String | 错误信息|
| data | Array | 当有额外的返回信息时，有该字段 |


data内容：

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| ruleBindList | Array | 告警规则绑定的对象列表(每个数组元素是一个具体的对象描述，见示例)|
| total | Int | 数量|




## 4. 示例
输入
<pre>
https://monitor.api.qcloud.com/v2/index.php?Action= DescribeAlarmRuleObjects
& alarmRuleId = policy-f3h1bxvcsb 
&<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>
</pre>
输出
```
{
    "code": 0,
    "message": "",
    "data": {
        "ruleBindList": [
             {"d1":"v1", "d2":"v2"}
        ],
        "total": "1"
    }
}
```

