## 1. 接口描述
域名:monitor.api.qcloud.com
接口名:GetMonitorRealtimeData

获取指标实时监控数据，返回最近的period（300s内），监控的指标的指定维度的数据。


## 2. 输入参数
| 参数名称 | 必选  | 类型 | 描述 |来源|
|---------|---------|---------|---------|---------|
| Action | 是 | String | 操作接口名|系统规定参数，此处取值：GetMonitorRealtimeData|
| namespace | 是 | String | 命名空间 |调用<a href="/doc/api/255/查询命名空间" title="查询命名空间">查询命名空间</a>(DescribeNamespace)接口查询|
| metricName | 是 |String | 指标名|调用<a href="/doc/api/255/查询指标" title="查询指标">查询指标</a>(DescribeMetric)接口查询|
| dimensions.N.name | 是  | String |  dimension组合的key部分，最多30个k/v组合|调用<a href="/doc/api/255/查询指标" title="查询指标">查询指标</a>(DescribeMetric)接口查询|
| dimensions.N.value | 是  | String |  dimension组合的value部分|调用<a href="/doc/api/255/查询指标对象列表" title="查询指标对象列表">查询指标对象列表</a>(DescribeObjects)接口查询|
| statistics | 是 | Enum | 统计方式，包括max、min、last、sum、avg等|用户自定义| 
| period	| 是 |	int | 统计周期，目前只能填写300|用户自定义| 



## 3. 输出参数
| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 错误码, 0: 成功, 其他值: 失败|
| message | String | 错误信息|
| data | array | 对象具体信息|

其中data的具体信息：

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| dimensions.name&dimensions.value | String | 由维度和其对应的值用&连接起来的字符串|
| value | Int | 返回数据|
| updateTime | datetime | 时间|




## 4. 示例
输入
<pre>
https://monitor.api.qcloud.com/v2/index.phpAction=GetMonitorRealtimeData
&namespace=name1
&metricName=metric1
&period=300
&statistics=last
&dimensions.0.name=d0
&dimensions.1.name=d1
&dimensions.2.name=d2
&dimensions.0.value=v0
&dimensions.1.value=v1
&dimensions.2.value=v2
&<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>
</pre>
输出
```
成功返回
{
		'code': 0,
		'message': “”,
		“data”:{
	     "d0=v0&d1=v1&d2=v2":{"value":1234, "updateTime":"2016-03-01 23:05:09"}
			}
}

注：如果查询的对象不存，则返回data字段内容为空
```

## 5. 错误码
| 返回值 | 说明 |
|---------|---------|
|-500  | 内部错误，从hbase拉数据失败 | 
|-513  | 访问DB时失败 | 
