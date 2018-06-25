## 1. 接口描述
域名:monitor.api.qcloud.com
接口名:DeleteMetricAggeration

删除指标聚合，需要指定聚合的维度的名称。

## 2. 输入参数
| 参数名称 | 必选  | 类型 | 描述 |来源|
|---------|---------|---------|---------|---------|
| Action | 是 | String | 操作接口名|系统规定参数，此处取值：DeleteMetricAggeration|
| namespace | 是 | String | 名字空间|调用<a href="/doc/api/255/查询命名空间" title="查询命名空间">查询命名空间</a>(DescribeNamespace)接口查询|
| metricName | 是 | String | 指标名|调用<a href="/doc/api/255/查询指标" title="查询指标">查询指标</a>(DescribeMetric)接口查询|
| dimensionNames.n | 是 | Array | 维度名称，dimensionNames 为数组，此处入参需要填写数组元素|用户定义过的维度名称组合|


## 3. 输出参数
| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 错误码, 0: 成功, 其他值: 失败|
| message | String | 错误信息|


## 4. 示例
输入
<pre>
https://monitor.api.qcloud.com/v2/index.php?Action=DeleteMetricAggeration
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
|-509 | 指定的配置(Aggeration)不存在 | 

