## 1. 接口描述
 
域名：monitor.api.qcloud.com
接口名: CreateMetricStatisticsType

为指标下的指定维度添加统计类型，只有添加统计类型之后，才能查询得到数据。

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
<td>系统规定参数，此处取值：CreateMetricStatisticsType
<tr>
<td> namespace
<td>是
<td> String
<td> 为该命名空间下的指标添加统计类型
<td>调用<a href="/doc/api/255/查询命名空间" title="查询命名空间">查询命名空间</a>(DescribeNamespace)接口查询
<tr>
<td> metricName
<td>是
<td> String
<td> 为该指标添加统计类型
<td>调用<a href="/doc/api/255/查询指标" title="查询指标">查询指标</a>(DescribeMetric)接口查询
<tr>
<td> dimensionNames.n
<td> 是
<td> Array
<td> 该指标的所有维度名称
<td>调用<a href="/doc/api/255/查询指标" title="查询指标">查询指标</a>(DescribeMetric)接口查询
<tr>
<td> statisticsType.m.statistics
<td> 是
<td> Enum
<td>  统计方式，包括max、min、last、sum、avg等
<td>用户自定义
<tr>
<td> statisticsType.m.period
<td> 是
<td> Int
<td> 统计周期，以秒为单位，目前必须填写300s暂不支持其他值
<td>目前必须填写300s
</tbody></table>

dimensionNames.n，此处的下标n，表示该指标的维度的下标
此处可以调用 DescribeMetric接口来获得该指标的所有维度信息。
在没有调用创建指标聚合的情形下，此处必须填写该指标下的所有维度名称。
例如：当指标name1有两个维度时，应该填写：dimensionNames.0=d1&dimensionNames.1=d2

若创建了指标聚合，此处可以填写指定聚合的维度。

statisticsType.m.statistics和statisticsType.m.period成对出现，可以对该指标的维度添加多组统计类型。
此处的下标m表示不同的统计类型数字下标
例如：   statisticsType.0.statistics=max  statisticsType.0.period=300s
              statisticsType.1.statistics=min  statisticsType.1.period=300s

## 3. 输出参数
 
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
|-513 | DB操作失败 | 
|-509 | 配置(指标/统计方式)不存在 | 