## 1. 接口描述
域名:monitor.api.qcloud.com
接口名:DescribeObjects

查询指标对象列表，当上报数据之后，会产生各个维度对应的对象。

## 2. 输入参数
| 参数名称 | 必选  | 类型 | 描述 |来源|
|---------|---------|---------|---------|---------|
| Action | 是 | String | 操作接口名|系统规定参数，此处取值：DescribeObjects|
| namespace | 是 | String | 命名空间|调用<a href="/doc/api/255/查询命名空间" title="查询命名空间">查询命名空间</a>(DescribeNamespace)接口查询|
| metricName | 是 | String | 指标名|调用<a href="/doc/api/255/查询指标" title="查询指标">查询指标</a>(DescribeMetric)接口查询|
| dimensionNames.n | 是 | array | dimension组合的key部分|调用<a href="/doc/api/255/查询指标" title="查询指标">查询指标</a>(DescribeMetric)接口查询|
| offset | 否 | Int | 偏移,默认0|用户自定义|
| limit | 否 | Int | 每页显示的记录数,默认30，这里实际获取的是偏移offset开始，取limit 条记录|用户自定义|

此处的dimensionNames.n为您需要查询的维度。
当指标下的维度没有创建指标聚合时，此处必须填写该指标下所有维度。
当为特定维度创建聚合之后，此处才可以只填写聚合的部分维度。


## 3. 输出参数
| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 错误码, 0: 成功, 其他值: 失败|
| message | String | 错误信息|
| data | array | 对象具体信息|
| total | Int | data数量|

其中data对应的array的内容为维度名称和维度对应的数值


## 4. 示例
输入
<pre>
https://monitor.api.qcloud.com/v2/index.phpAction=DescribeObjects
&namespace=name1
&metricName=zqmetric1
&dimensionNames.0=d1
&dimensionNames.1=d2
&dimensionNames.2=d3
&<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>
</pre>
输出
```
{
		'code': 0,
		'message': “”,
     “data”:{
	                “records”:[{ “d1”: “v1”, “d2”:”v2”, ...},...]
						     },
			"total":1
}
```

## 5. 错误码
| 返回值 | 说明 |
|---------|---------|
|-500  | 内部错误，从hbase拉数据失败 | 
|-513  | 访问DB时失败 | 
