## 1. 接口描述
 
域名：monitor.api.qcloud.com
接口名: CreateMetric

创建指标。

 

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
<td>系统规定参数，此处取值：CreateMetric
<tr>
<td> namespace
<td>是
<td> String
<td> 要创建指标的命名空间
<td> 	调用<a href="/doc/api/255/查询伸缩组列表" title="查询命名空间">查询命名空间</a>(DescribeNamespace)接口查询
<tr>
<td> metricName
<td>是
<td> String
<td> 指标名称，支持英文、数字和下划线
<td>用户自定义
<tr>
<td>  dimensionNames.n
<td>是
<td> String
<td> 该指标的统计维度名称
<td>用户自定义
<tr>
<td> metricCname
<td>是
<td> String
<td> 指标中文名称信息
<td>用户自定义
<tr>
<td> unit
<td>否
<td> String
<td> 此单位只作显示使用，不做任何计算的转换，可为任意字符串
<td>用户自定义
<tr>
<td> statisticsType.m.statistics
<td>否
<td> Enum
<td> 统计方式，包括max、min、sum、avg、last(最后一个数值)等
<td>用户自定义
<tr>
<td> statisticsType.m.period
<td>否
<td> Int
<td> 收集数据时间间隔，目前指定为300s，暂时不支持修改为其它值
<td>系统目前指定为300s
</tbody></table>

statisticsType.m.statistics 和  statisticsType.m.period 填写时，为该指标下的所有维度添加统计类型



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
 https://monitor.api.qcloud.com/v2/index.php?Action=CreateMetric
 &namespace=name1
 &metricName=metric1
 &metricCname=metric_cn
 &dimensionNames.0=d1
 &dimensionNames.1=d2
 &dimensionNames.2=d3
 &unit=kb
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
| -503 | 参数错误 | 
|-513 | DB操作失败 | 
|-514 | 指标已存在 | 
|-507 | dimensions维度数量超出限制 | 