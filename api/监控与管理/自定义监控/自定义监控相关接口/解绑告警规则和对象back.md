## 1. 接口描述
域名:monitor.api.qcloud.com
接口名:UnbindAlarmRuleObjects

将对象与告警规则解绑

## 2. 输入参数
| 参数名称 | 必选  | 类型 | 描述 |来源|
|---------|---------|---------|---------|---------|
| Action | 是 | String | 操作接口名|系统规定参数，此处取值：UnbindAlarmRuleObjects|
| alarmRuleId | 是 | String | 规则ID|调用<a href="/doc/api/255/查询告警规则" title="查询告警规则">查询告警规则</a>(DescribeAlarmRuleList)接口查询|
| dimensions.n.name | 是 | String | 维度组合的key|调用<a href="/doc/api/255/查询告警规则绑定的对象" title="查询告警规则绑定的对象">查询告警规则绑定的对象</a>(DescribeObjects)接口查询|
| dimensions.n.value | 是 | string |	维度组合的value|调用<a href="/doc/api/255/查询告警规则绑定的对象" title="查询告警规则绑定的对象">查询告警规则绑定的对象</a>(DescribeObjects)接口查询|

## 3. 输出参数
| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 错误码, 0: 成功, 其他值: 失败|
| message | String | 错误信息|


## 4. 示例
输入
<pre>
https://monitor.api.qcloud.com/v2/index.php?Action=UnbindAlarmRuleObjects
& alarmRuleId = policy-f3h1bxvcsb 
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

