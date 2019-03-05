## 1. 接口描述
 
域名：monitor.api.qcloud.com
接口名: DescribeMetric

查询自定义指标。

 

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
<td>系统规定参数，此处取值：DescribeMetric
<tr>
<td> namespace
<td>是
<td> String
<td> 查询该命名空间下的指标
<td> 	调用<a href="/doc/api/255/查询命名空间" title="查询命名空间">查询命名空间</a>(DescribeNamespace)接口查询
<tr>
<td> metricName
<td>否
<td> String
<td> 按指标名称筛选，不指定时返回本命名空间下所有指标信息
<td> 依据用户定义的指标名填入
</tbody></table>

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
<tr>
<td> data
<td> Array
<td> 返回的数组
<tr>
</tbody></table>


其中data返回的每个指标中的内容的含义
<table class="t"><tbody><tr>
<th><b>参数名称</b></th>
<th><b>类型</b></th>
<th><b>描述</b></th>
<tr>
<td> namespace
<td> String
<td> 本指标所在的命名空间
<tr>
<td> metricName
<td> String
<td> 本指标名称
<tr>
<td> metricCname
<td> String
<td> 本指标中文名称
<tr>
<td> dimension
<td> String
<td> 指标维度
<tr>
<td> unit
<td> String
<td>单位
<tr>
<td> statisticsType
<td> Array
<td> 统计类型
</tbody></table>

其中statisticsType的含义：
<table class="t"><tbody><tr>
<th><b>参数名称</b></th>
<th><b>类型</b></th>
<th><b>描述</b></th>
<tr>
<td> period
<td> Int
<td> 统计周期
<tr>
<td> statistics
<td> String
<td> 统计方法函数
</tbody></table>


## 4. 示例
 
输入

<pre>
 https://domain/v2/index.php?Action=DescribeMetric
 &namespace=name1
 &<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>
</pre>

输出
```
{
    "code": 0,
    "message": "",
    "data": {
        "name1": {//命名空间
            "metric1": {//指标metric1的具体信息
                "namespace": "name1",
                "metricName": "metric1",
                "unit": "",
                "metricCname": "中文名称",
                "dimension": "d1,d2",
                "statisticsType": null
            },
            "metric4": {//指标metric4的具体信息
                "namespace": "name1",
                "metricName": "metric4",
                "unit": "kb",
                "metricCname": "metric_cn",
                "dimension": "d1,d2,d3",
                "statisticsType": [
                    {
                        "period": "300",
                        "statistics": "last"
                    }
                ]
            }
        }
    }
}
```

## 5. 错误码

| 返回值 | 说明 |
|---------|---------|
|-513 | DB操作失败 | 