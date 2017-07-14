## 1. 接口描述

域名：monitor.api.qcloud.com
接口：GetMonitorData

查询文档数据库MongoDB产品监控数据，入参取值如下：
namespace: qce/cmongo
dimensions.0.name=target
dimensions.0.value=视查询维度而定

+++++++++++++++++++改到这里为止+++++++++++

## 2. 输入参数

以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见<a href="/doc/api/405/公共请求参数" title="公共请求参数">公共请求参数</a>页面。其中，此接口的Action字段为GetMonitorData。

### 2.1输入参数

| 参数名称               | 必选   | 类型       | 输入内容       | 描述                                       |
| ------------------ | ---- | -------- | ---------- | ---------------------------------------- |
| namespace          | 是    | String   | qce/cvm    | 命名空间，每个云产品会有一个命名空间，具体名称见输入内容一栏。          |
| metricName         | 是    | String   | 具体的指标名称    | 指标名称，具体名称见2.2                            |
| dimensions.0.name  | 是    | String   | redis_uuid | 入参为redis_uuid                            |
| dimensions.0.value | 是    | String   | 具体的uuid    | 输入Redis实例的具体uuid，如00953d35-f6b7-4c2d-b86e-613b81f4cfcc |
| period             | 否    | Int      | 60/300     | 监控统计周期，绝大部分指标支持60s统计粒度，部分指标仅支持300s统计粒度，统计粒度根据指标的不同而变。输入参数时可参考2.2的指标详情列表。 |
| startTime          | 否    | Datetime | 起始时间       | 起始时间，如"2016-01-01 10:25:00"。 默认时间为当天的”00:00:00” |
| endTime            | 否    | Datetime | 结束时间       | 结束时间，默认为当前时间。 endTime不能小于startTime       |
### 2.2 指标名称

| 指标名称             | 含义          | 单位   | 统计粒度（period） |
| ---------------- | ----------- | ---- | ------------ |
| cache_hit_ratio  | cache命中率    | %    |              |
| cmdstat_get      | get命令数      | 次/分钟 |              |
| cmdstat_getbit   | getbit命令数   | 次/分钟 |              |
| cmdstat_getrange | getrange命令数 | 次/分钟 |              |
| cmdstat_hget     | hget命令数     | 次/分钟 |              |
| cmdstat_hgetall  | hgetall命令数  | 次/分钟 |              |
| cmdstat_hmget    | hmget命令数    | 次/分钟 |              |
| cmdstat_hmset    | hmset命令数    | 次/分钟 |              |
| cmdstat_hset     | hset命令数     | 次/分钟 |              |
| cmdstat_hsetnx   | hsetnx命令数   | 次/分钟 |              |
| cmdstat_lset     | lset命令数     | 次/分钟 |              |
| cmdstat_mget     | mget命令数     | 次/分钟 |              |
| cmdstat_mset     | mset命令数     | 次/分钟 |              |
| cmdstat_msetnx   | msetnx命令数   | 次/分钟 |              |
| cmdstat_set      | set命令数      | 次/分钟 |              |
| cmdstat_setbit   | setbit命令数   | 次/分钟 |              |
| cmdstat_setex    | setex命令数    | 次/分钟 |              |
| cmdstat_setnx    | setnx命令数    | 次/分钟 |              |
| cmdstat_setrange | setrange命令数 | 次/分钟 |              |
| connections      | 外部链接数       | 个    |              |
| cpu_us           | 处理请求数       | 微秒   |              |
| in_flow          | 外部请求包长度     | Mb   |              |
| keys             | 主key量       | 个    |              |
| out_flow         | 外部返回包长度     | Mb   |              |
| stat_get         | 所有get命令数    | 次/分钟 |              |
| stat_set         | 所有set命令数    | 次/分钟 |              |
| storage          | 占用空间        | Mb   |              |
| storage_us       | 占用空间占比      | %    |              |


## 3. 输出参数

| 参数名称       | 类型       | 描述                  |
| ---------- | -------- | ------------------- |
| code       | Int      | 错误码, 0: 成功, 其他值表示失败 |
| message    | String   | 返回信息                |
| startTime  | Datetime | 起始时间                |
| endTime    | Datetime | 结束时间                |
| metricName | String   | 指标名称                |
| period     | Int      | 监控统计周期              |
| dataPoints | Array    | 监控数据列表              |


## 4. 错误码表

| 错误代码 | 错误描述    | 英文描述                                 |
| ---- | ------- | ------------------------------------ |
| -502 | 资源不存在   | OperationDenied.SourceNotExists      |
| -503 | 请求参数有误  | InvalidParameter                     |
| -505 | 参数缺失    | InvalidParameter.MissingParameter    |
| -507 | 超出限制    | OperationDenied.ExceedLimit          |
| -509 | 错误的维度组合 | InvalidParameter.DimensionGroupError |
| -513 | DB操作失败  | InternalError.DBoperationFail        |

## 5. 示例

输入

```
https://monitor.api.qcloud.com/v2/index.php?
&<<a href="https://www.qcloud.com/doc/api/229/6976">公共请求参数</a>>
&namespace=qce/redis
&metricName=cache_hit_ratio
&dimensions.0.name=redis_uuid
&dimensions.0.value=00953d35-f6b7-4c2d-b86e-613b81f4cfcc
&startTime=2016-06-28 14:10:00
&endTime=2016-06-28 14:20:00
```

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
		40，
		30
	]
}
```