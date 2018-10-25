## 1. 接口描述
域名:monitor.api.qcloud.com
接口名:ModifyAlarmRule

更改告警规则

## 2. 输入参数
| 参数名称 | 必选  | 类型 | 描述 |来源|
|---------|---------|---------|---------|---------|
| Action | 是 | String | 操作接口名|系统规定参数，此处取值：ModifyAlarmRule|
| alarmRuleId | 是 | String | 告警规则ID|调用<a href="/doc/api/255/查询告警规则" title="查询告警规则">查询告警规则</a>(DescribeAlarmRuleList)接口查询|
| operatorType | 否 | String | 比较类型|用户自定义| 
| threshold | 否 | Int | 告警阈值|用户自定义| 
| constancy | 否 | Int | 持续时间|用户自定义| 
| receiversId | 否 | Int | 告警接收分组ID|用户自定义| 


## 3. 输出参数
| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 错误码, 0: 成功, 其他值: 失败|
| message | String | 错误信息|


## 4. 示例
输入
<pre>
https://monitor.api.qcloud.com/v2/index.php?Action=ModifyAlarmRule
&alarmRuleId=policy-eqzqq79naz
&receiversId=8888
&<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>
</pre>
输出
```
{
    "code":"0",
    "message":""
}
```

