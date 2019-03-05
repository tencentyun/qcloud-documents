## 1. 接口描述
域名:monitor.api.qcloud.com
接口名:BindAlarmRuleObjects

将对象绑定到告警规则
当用户上传数据之后会产生对象：
例如：d1=v1&d2=v2&d3=v3确定对象。

## 2. 输入参数
| 参数名称 | 必选  | 类型 | 描述 |来源|
|---------|---------|---------|---------|---------|
| Action | 是 | String | 操作接口名|系统规定参数，此处取值：BindAlarmRuleObjects|
| alarmRuleId | 是 | String | 规则ID|调用<a href="/doc/api/255/查询告警规则" title="查询告警规则">查询告警规则</a>(DescribeAlarmRuleList)接口查询|
| dimensions.n.name | 是 | String | 维度组合的key|调用<a href="/doc/api/255/查询指标对象列表" title="查询指标对象列表">查询指标对象列表</a>(DescribeObjects)接口查询|
| dimensions.n.value | 是 | string | 维度组合的value|调用<a href="/doc/api/255/查询指标对象列表" title="查询指标对象列表">查询指标对象列表</a>(DescribeObjects)接口查询|
此处的维度信息必须和创建告警规则时的维度信息一致。

## 3. 输出参数
| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 错误码, 0: 成功, 其他值: 失败|
| message | String | 错误信息|


## 4. 示例
输入
<pre>
https://monitor.api.qcloud.com/v2/index.php?Action= BindAlarmRuleObjects
&alarmRuleId = policy-f3h1bxvcsb 
&dimensions.0.name=name
&dimensions.0.value=a1
&<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>
</pre>
输出
```
{
    "code":"0",
    "message":""
}
```

