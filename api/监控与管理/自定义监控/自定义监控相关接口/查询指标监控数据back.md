## 1. 接口描述
域名:monitor.api.qcloud.com
接口名:GetMonitorData

获取监控数据，此接口获取指标下指定维度的在startTime和endTime之间的多组数据
（每组数据的统计周期为period ，目前为300s）

## 2. 输入参数
| 参数名称 | 必选  | 类型 | 描述 |来源|
|---------|---------|---------|---------|---------|
| Action | 是 | String | 操作接口名|系统规定参数，此处取值：GetMonitorData|
| namespace | 是 | String | 名字空间|调用<a href="/doc/api/255/查询命名空间" title="查询命名空间">查询命名空间</a>(DescribeNamespace)接口查询|
| metricName | 是 | String | 指标名称|调用<a href="/doc/api/255/查询指标" title="查询指标">查询指标</a>(DescribeMetric)接口查询|
| statistics  | 是 | Enum | 统计方式，包括max、min、last、sum、avg等|用户自定义| 
| dimensions.n.name| 是| String | 纬度字段的名称，dimensions.n.name 为数组，此处入参需要填写数组元素 |调用<a href="/doc/api/255/查询指标" title="查询指标">查询指标</a>(DescribeMetric)接口查询|
| dimensions.n.value | 是 | String | 纬度字段的值，dimensions.n.value 为数组，此处入参需要填写数组元素| 调用<a href="/doc/api/255/查询指标对象列表" title="查询指标对象列表">查询指标对象列表</a>(DescribeObjects)接口查询|
| period | 否 | Int | 监控数据统计粒度，目前只能填写300|用户自定义| 
| startTime | 否 | datetime | Y-m-d H:M:S 起始时间，当不填写时，起始时间默认为当天的00:00:00|用户自定义| 
| endTime | 否 | datetime | 结束时间,不填写时，默认为当前时间|用户自定义| 

此处的dimensions.n.name为您需要查询的维度。
当指标下的维度没有创建指标聚合时，此处必须填写该指标下所有维度。
当为特定维度创建聚合之后，此处才可以只填写聚合的部分维度。

dimensions.n.value和dimensions.n.name的值对应，dimensions.n.value可由查询指标对象列表接口获得


## 3. 输出参数
| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 错误码, 0: 成功, 其他值: 失败|
| message | String | 错误信息|
| data | Array | 数据信息 |

其中data对应为metricName和统计的个维度对应的结果数值。

## 4. 示例
输入
<pre>
https://monitor.api.qcloud.com/v2/index.php?Action=GetMonitorData
&namespace=name1
&metricName=metric1
&dimensions.0.name=d1
&dimensions.1.name=d2
&dimensions.2.name=d3
&dimensions.0.value=v1
&dimensions.1.value=v2
&dimensions.2.value=v3
&period=300
&statistics=last
&<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>
</pre>
输出
```
{
			'code': 0,
			'message': “”,
			“data”:{
		         “{metric1}”:[10,15,11...]
			}
}
```

