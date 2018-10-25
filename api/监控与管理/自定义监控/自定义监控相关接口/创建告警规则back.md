## 1. 接口描述
域名:monitor.api.qcloud.com
接口名:CreateAlarmRule

创建告警规则，此处的statistics和period组合必须在指标statisticsType内部存在。
调用前可以调用DescribeMetric确认内部statisticsType信息。

## 2. 输入参数
| 参数名称 | 必选  | 类型 | 描述 |来源|
|---------|---------|---------|---------|---------|
| Action | 是 | String | 操作接口名|系统规定参数，此处取值：CreateAlarmRule|
| namespace | 是 | String | 命名空间|调用<a href="/doc/api/255/查询命名空间" title="查询命名空间">查询命名空间</a>(DescribeNamespace)接口查询|
| metricName | 是 | String | 指标名|调用<a href="/doc/api/255/查询指标" title="查询指标">查询指标</a>(DescribeMetric)接口查询|
| operatorType | 是 | String | 操作符，取值为(>、< 、>=、 <= 、!=、==), 表示告警规则中的比较方式|用户自定义| 
| threshold | 是 | Int | 触发异常的数目阈值|用户自定义| 
| constancy | 是 | Int | 表明异常持续多少个周期会触发告警，即：当异常持续时间为periodconstancy时，将触发告警|用户自定义| 
| period | 是 | Int | 统计周期,目前只能填写300s|用户自定义| 
| statistics | 是 | Enum | 统计方式，取值为(sum, last, avg, min, max)|调用<a href="/doc/api/255/查询指标" title="查询指标">查询指标</a>(DescribeMetric)接口查询|
| dimensionNames.n | 	是 | 	array | 	维度key的组合|调用<a href="/doc/api/255/查询指标" title="查询指标">查询指标</a>(DescribeMetric)接口查询|
| isWild | 否 | int | 规则是否是通配规则，通配规则适用于该维度key组合下的所有对象，并且不能再绑定到具体的对象上，如不填写则默认为非通配规则|用户自定义|
| receiversId | 否 | string | 告警接收组id，如不填则不绑定任何接收组(即无法收到告警通知)|用户自定义|



## 3. 输出参数
| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 错误码, 0: 成功, 其他值: 失败|
| message | String | 错误信息,当成功时为空|
| data | Array | 当有额外的返回信息时，有该字段 |

data的内容

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
|alarmRuleId| string | 告警规则ID, 用于编辑、删除告警规则时入参| 


## 4. 示例
输入
<pre>
https://monitor.api.qcloud.com/v2/index.phpAction=CreateAlarmRule
&namespace=test
&metricName=m1
&dimensionNames.0=aaa
&dimensionNames.1=bbb
&operatorType=>
&threshold=10
&period=300
&statistics =sum
&constancy=10
&<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>
</pre>
输出
```
{
    "code":"0",
    "message":"",
    "data":{
        "alarmRuleId":"policy-63uiec17"
    }
}
```

