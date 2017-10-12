## 1. 接口描述
 
域名：monitor.api.qcloud.com
接口名: DeleteMetricStatisticsType

删除指定指标下的统计类型。

 

## 2. 输入参数
 
<table class="t"><tbody><tr>
<th><b>参数名称</b></th>
<th><b>必选</b></th>
<th><b>类型</b></th>
<th><b>描述</b></th>
<th><b>来源</b></th>
<tr>
<td> Action
<td> 是
<td> String
<td>操作接口名
<td>系统规定参数，此处取值：DeleteMetricStatisticsType
<tr>
<td> namespace
<td>是
<td> String
<td> 为该命名空间下的指标删除统计类型
<td> 	调用<a href="/doc/api/255/查询命名空间" title="查询命名空间">查询命名空间</a>(DescribeNamespace)接口查询
<tr>
<td> metricName
<td>是
<td> String
<td> 为该指标删除统计类型
<td> 	调用<a href="/doc/api/255/查询指标" title="查询指标">查询指标</a>(DescribeMetric)接口查询
<tr>
<td> dimensionNames.n
<td> 是
<td> Array
<td> 维度名称,和添加统计类型相同，必须填写所有维度名称
<td> 	调用<a href="/doc/api/255/查询指标" title="查询指标">查询指标</a>(DescribeMetric)接口查询
<tr>
<td> statisticsType.m.statistics
<td> 是
<td> Enum
<td>  m为statisticsType数字下标，statistics统计方式，包括max、min、last、sum、avg等
<td> 用户自定义
<tr>
<td> statisticsType.m.period
<td> 是
<td> Int
<td>  统计周期，目前只能填写300s
<td> 用户自定义
</tbody></table>



## 3.输出参数
 
<table class="t"><tbody><tr>
<th><b>参数名称</b></th>
<th><b>类型</b></th>
<th><b>描述</b></th>
<tr>
<td> code
<td> Int
<td> 错误码, 0: 成功, 其他值: 失败
<tr>
<td> message
<td> String
<td> 错误信息
</tbody></table>

## 4. 示例
 
输入

<pre>
 https://monitor.api.qcloud.com/v2/index.php?Action=CreateMetricStatisticsType
 &namespace=name1
 &metricName=zqmetric1
 &dimensionNames.0=d1
 &statisticsType.0.period=300
 &statisticsType.0.statistics=last
 &<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>
</pre>

输出
```
{
  'code': 0,
  'message': ''
}
```

## 5. 错误码

| 返回值 | 说明 |
|---------|---------|
|-503 | 参数错误 | 
|-509 | 指定的配置(namespace/metricName/dimensionNames)不存在 |
|-513 | DB操作失败 | 
|-514 |  统计方式已存在 | 