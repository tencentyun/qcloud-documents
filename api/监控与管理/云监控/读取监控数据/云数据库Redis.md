## 1. 接口描述


云存储Redis（Cloud Redis Store，以下简称CRS）是腾讯云基于分布式缓存领域多年技术沉淀和Redis类业务运营的需求，打造的一款高可用、高可靠的Redis服务平台。具体介绍请参考<a href="/doc/product/239/产品介绍" title="产品介绍">云存储Redis简介</a>页面。
查询云存储Redis产品监控数据，入参取值如下：

namespace: qce/redis
维度名称取值：redis_uuid
dimensions.0.name=redis_uuid
dimensions.0.value为实例的uuid

## 2. 输入参数

以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见<a href="/doc/api/405/公共请求参数" title="公共请求参数">公共请求参数</a>页面。其中，此接口的Action字段为GetMonitorData。


<table class="t"><tbody><tr>
<th><b>参数名称</b></th>
<th><b>必选</b></th>
<th><b>类型</b></th>
<th><b>描述</b></th>
<tr>
<td> namespace
<td> 是
<td> String
<td> 命名空间，参见第一小节
<tr>
<td> metricName
<td> 是
<td> String
<td> 指标名称，具体名称见第5小节
<tr>
<td> dimensions.n.name
<td> 是
<td> String
<td> 维度的名称，具体维度名称见第5小节各产品监控指标列表，与dimensions.n.value配合使用。
<tr>
<td> dimensions.n.value
<td> 是
<td> String
<td> 对应的维度的值，具体维度名称见第5小节各产品监控指标列表，与dimensions.n.name配合使用。
<tr>
<td> period
<td> 否
<td> Int
<td> 监控统计周期。默认为取值为300，单位为s。目前CVM支持60s、300s粒度，其他产品支持仅300s。后续将逐步支持更多产品。
<tr>
<td> startTime
<td> 否
<td> Datetime
<td> 起始时间，如”2016-01-01 10:25:00”。 默认时间为当天的”00:00:00”
<tr>
<td> endTime
<td> 否
<td> Datetime
<td> 结束时间，默认为当前时间。 endTime不能小于startTime
</tbody></table>



## 3. 输出参数

<table class="t"><tbody><tr>
<th><b>参数名称</b></th>
<th><b>类型</b></th>
<th><b>描述</b></th>
<tr>
<td> code
<td> Int
<td> 错误码, 0: 成功, 其他值表示失败
<tr>
<td> message
<td> String
<td> 返回信息
<tr>
<td> startTime
<td> Datetime
<td> 起始时间
<tr>
<td> endTime
<td> Datetime
<td> 结束时间
<tr>
<td> metricName
<td> String
<td> 指标名称
<tr>
<td> period
<td> Int
<td> 监控统计周期，单位为s
<tr>
<td> dataPoints
<td> Array
<td> 监控数据列表
</tbody></table>


## 4. 错误码表

| 错误代码 | 错误描述    | 英文描述                                 |
| ---- | ------- | ------------------------------------ |
| -502 | 资源不存在   | OperationDenied.SourceNotExists      |
| -503 | 请求参数有误  | InvalidParameter                     |
| -505 | 参数缺失    | InvalidParameter.MissingParameter    |
| -507 | 超出限制    | OperationDenied.ExceedLimit          |
| -509 | 错误的维度组合 | InvalidParameter.DimensionGroupError |
| -513 | DB操作失败  | InternalError.DBoperationFail        |


## 5. 指标列表

**metricName可选取值范围**

| 指标名称             | 含义          | 单位   | 维度         |
| ---------------- | ----------- | ---- | ---------- |
| cache_hit_ratio  | cache命中率    | %    | redis_uuid |
| cmdstat_get      | get命令数      | 次/分钟 | redis_uuid |
| cmdstat_getbit   | getbit命令数   | 次/分钟 | redis_uuid |
| cmdstat_getrange | getrange命令数 | 次/分钟 | redis_uuid |
| cmdstat_hget     | hget命令数     | 次/分钟 | redis_uuid |
| cmdstat_hgetall  | hgetall命令数  | 次/分钟 | redis_uuid |
| cmdstat_hmget    | hmget命令数    | 次/分钟 | redis_uuid |
| cmdstat_hmset    | hmset命令数    | 次/分钟 | redis_uuid |
| cmdstat_hset     | hset命令数     | 次/分钟 | redis_uuid |
| cmdstat_hsetnx   | hsetnx命令数   | 次/分钟 | redis_uuid |
| cmdstat_lset     | lset命令数     | 次/分钟 | redis_uuid |
| cmdstat_mget     | mget命令数     | 次/分钟 | redis_uuid |
| cmdstat_mset     | mset命令数     | 次/分钟 | redis_uuid |
| cmdstat_msetnx   | msetnx命令数   | 次/分钟 | redis_uuid |
| cmdstat_set      | set命令数      | 次/分钟 | redis_uuid |
| cmdstat_setbit   | setbit命令数   | 次/分钟 | redis_uuid |
| cmdstat_setex    | setex命令数    | 次/分钟 | redis_uuid |
| cmdstat_setnx    | setnx命令数    | 次/分钟 | redis_uuid |
| cmdstat_setrange | setrange命令数 | 次/分钟 | redis_uuid |
| connections      | 外部链接数       | 个    | redis_uuid |
| cpu_us           | 处理请求数       | 微秒   | redis_uuid |
| in_flow          | 外部请求包长度     | Mb   | redis_uuid |
| keys             | 主key量       | 个    | redis_uuid |
| out_flow         | 外部返回包长度     | Mb   | redis_uuid |
| stat_get         | 所有get命令数    | 次/分钟 | redis_uuid |
| stat_set         | 所有set命令数    | 次/分钟 | redis_uuid |
| storage          | 占用空间        | Mb   | redis_uuid |
| storage_us       | 占用空间占比      | %    | redis_uuid |

## 6. 示例

**读取云存储Redis监控指标示例**

输入

<pre>
https://monitor.api.qcloud.com/v2/index.php?Action=GetMonitorData
&<<a href="https://www.qcloud.com/doc/api/229/6976">公共请求参数</a>>
&namespace=qce/redis
&metricName=cache_hit_ratio
&dimensions.0.name=redis_uuid
&dimensions.0.value=00953d35-f6b7-4c2d-b86e-613b81f4cfcc
&startTime=2016-06-28 14:10:00
&endTime=2016-06-28 14:20:00
</pre>

输出

```
{
	"code": 0,
	"message": "",
	"metricName": "cache_hit_ratio",
	"startTime": "2016-06-28 14:10:00",
	"endTime": "2016-06-28 14:20:00",
	"period": 300,
	"dataPoints": [
		50,
		30
	]
}
```
```