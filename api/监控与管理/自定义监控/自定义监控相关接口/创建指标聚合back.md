## 1. 接口描述
域名:monitor.api.qcloud.com
接口名:CreateMetricAggeration

添加指标聚合，将该指标下的指定维度聚合起来，以实现统计指标下部分维度的信息的功能以及查询指标下部分维度信息的功能。
说明：当其他接口内出现维度入参时，假如没有聚合指定维度，需要填写该指标的所有维度。聚合指定维度之后，可以填写部分维度。
例如指标a  有维度dimensionNames.0=d1  dimensionNames.1=d2 dimensionNames.1=d3
将维度dimensionNames.0=d1  dimensionNames.1=d2聚合起来，调用添加统计类型接口时，才可以只指定维度d1,d2。
当没有聚合部分维度，添加统计类型时，参数若只指定部分维度时，无法统计。

## 2. 输入参数
| 参数名称 | 必选  | 类型 | 描述 |来源|
|---------|---------|---------|---------|---------|
| Action | 是 | String | 操作接口名|系统规定参数，此处取值：CreateMetricAggeration|
| namespace | 是 | String | 名字空间|名字空间|调用<a href="/doc/api/255/查询命名空间" title="查询命名空间">查询命名空间</a>(DescribeNamespace)接口查询|
| metricName | 是 | String | 指标名|调用<a href="/doc/api/255/查询指标" title="查询指标">查询指标</a>(DescribeMetric)接口查询|
| dimensionNames.n | 是 | String | 需要聚合的维度名称|用户自定义| 
| statisticsType.m.statistics | 否 | Enum | 统计方式，包括max、min、last、sum、avg等|用户自定义| 
| statisticsType.m.period| 否 | Int | 统计周期目前只能填写300秒|目前只支持300s| 
statisticsType.n.statistics 和  statisticsType.n.period 填写时，为该聚合下的所有维度添加统计类型

## 3. 输出参数
| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 错误码, 0: 成功, 其他值: 失败|
| message | String | 错误信息|


## 4. 示例
输入
<pre>
https://monitor.api.qcloud.com/v2/index.phpAction=CreateMetricAggeration
&namespace=name1
&metricName=zqmetric1
&dimensionNames.0=d1
&dimensionNames.1=d2
&<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>
</pre>
输出
```
{
    "code":"0",
    "message":""
}
```

## 5. 错误码

| 返回值 | 说明 |
|---------|---------|
|-503 | 参数错误 | 
|-509 | 指定的配置(namespace/metricName/dimensionNames)不存在 | 
|-513 | DB操作失败 | 
|-514 | 统计方式/聚合的dimension已存在 | 