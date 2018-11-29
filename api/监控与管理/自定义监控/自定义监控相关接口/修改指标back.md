## 1. 接口描述
域名:monitor.api.qcloud.com
接口名:ModifyMetric

修改指标，只能修改指标的unit或者metricCname

## 2. 输入参数
| 参数名称 | 必选  | 类型 | 描述 |来源|
|---------|---------|---------|---------|---------|
| Action | 是 | String | 操作接口名|系统规定参数，此处取值：ModifyMetric|
| namespace | 是 | String | 名字空间|调用<a href="/doc/api/255/查询命名空间" title="查询命名空间">查询命名空间</a>(DescribeNamespace)接口查询|
| metricName | 是 | String | 指标名|调用<a href="/doc/api/255/查询指标" title="查询指标">查询指标</a>(DescribeMetric)接口查询|
| metricCname | 是  | String | 指标中文名|用户自定义| 
| unit | 否 | String | 数据上报的单位|用户自定义| 



## 3. 输出参数
| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 错误码, 0: 成功, 其他值: 失败|
| message | String | 错误信息|


## 4. 示例
输入
<pre>
https://monitor.api.qcloud.com/v2/index.php?Action=ModifyMetric
&namespace=nm1
&metricName=secret0
&metricCname=修改后的指标
&unit=兆
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

