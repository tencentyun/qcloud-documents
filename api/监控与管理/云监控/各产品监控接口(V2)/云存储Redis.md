## 1. 接口描述

域名：monitor.api.qcloud.com
接口：GetMonitorData

云存储 Redis（Cloud Redis Store，以下简称 CRS）是腾讯云基于分布式缓存领域多年技术沉淀和 Redis 类业务运营的需求，打造的一款高可用、高可靠的 Redis 服务平台。具体介绍请参考 <a href="/doc/product/239/产品介绍" title="产品介绍">云存储 Redis 简介</a> 页面。

查询云存储 Redis 产品监控数据，入参取值如下：
namespace: qce/redis
dimensions.0.name=redis_uuid
dimensions.0.value 为实例的 uuid

## 2. 输入参数

以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见 <a href="/doc/api/405/公共请求参数" title="公共请求参数">公共请求参数</a> 页面。其中，此接口的 Action 字段为 GetMonitorData。

### 2.1 输入参数

| 参数名称               | 必选   | 类型       | 输入内容       | 描述                                       |
| ------------------ | ---- | -------- | ---------- | ---------------------------------------- |
| namespace          | 是    | String   | qce/redis  | 命名空间，每个云产品会有一个命名空间，具体名称见输入内容一栏。          |
| metricName         | 是    | String   | 具体的指标名称    | 指标名称，具体名称见2.2                            |
| dimensions.0.name  | 是    | String   | redis_uuid | 入参必须是 redis_uuid                          |
| dimensions.0.value | 是    | String   | 具体的 uuid    | 输入 redis 实例 ID，也即是实例串号，如 crs-ifmymj41，可通过 [查询 CRS 实例列表接口](http://cloud.tencent.com/doc/api/260/1384) 查询 |
| period             | 否    | Int      | 60/300     | 监控统计周期，绝大部分指标支持60s统计粒度，部分指标仅支持300s统计粒度，统计粒度根据指标的不同而变。输入参数时可参考2.2的指标详情列表。 |
| startTime          | 否    | Datetime | 起始时间       | 起始时间，如 “2016-01-01 10:25:00”。 默认时间为当天的 “00:00:00” |
| endTime            | 否    | Datetime | 结束时间       | 结束时间，默认为当前时间。 endTime 不能小于 startTime       |


### 2.2 指标名称

| 指标中文名       | 指标英文名            | 指标采集方式（Linux 下含义）                         | 指标统计方式                    | 单位    |
| ----------- | ---------------- | ---------------------------------------- | ------------------------- | ----- |
| cache 命中率    | cache_hit_ratio  | 1分钟取内取 keyspace_misses、keyspace_hits 通过如下计算 （1- keyspace_misses/keyspace_hits）* 100% 得出。不再维护该指标 |每分钟采集，5分钟粒度数据是按最近5分钟内平均值  | %     |
| get 命令数      | cmdstat_get      | 1分钟内 get 命令请求数                           | 每分钟采集，5分钟粒度数据是按最近5分钟内求和   | 次/分钟  |
| getbit 命令数   | cmdstat_getbit   | 1分钟内 getbit 命令请求数                        | 每分钟采集，5分钟粒度数据是按最近5分钟内求和   | 次/分钟  |
| getrange 命令数 | cmdstat_getrange | 1分钟内 getrange 命令请求数                      | 每分钟采集，5分钟粒度数据是按最近5分钟内求和   | 次/分钟  |
| hget 命令数     | cmdstat_hget     | 1分钟内 hget 命令请求数                          | 每分钟采集，5分钟粒度数据是按最近5分钟内求和   | 次/分钟  |
| hgetall 命令数  | cmdstat_hgetall  | 1分钟内 hgetall 命令请求数                       | 每分钟采集，5分钟粒度数据是按最近5分钟内求和   | 次/分钟  |
| hmget 命令数    | cmdstat_hmget    | 1分钟内 hmget 命令请求数                         | 每分钟采集，5分钟粒度数据是按最近5分钟内求和   | 次/分钟  |
| hmset命令数    | cmdstat_hmset    | 1分钟内 hmset 命令请求数                         | 每分钟采集，5分钟粒度数据是按最近5分钟内求和   | 次/分钟  |
| hset 命令数     | cmdstat_hset     | 1分钟内 hset 命令请求数                          | 每分钟采集，5分钟粒度数据是按最近5分钟内求和   | 次/分钟  |
| hsetnx 命令数   | cmdstat_hsetnx   | 1分钟内 hsetnx 命令请求数                        | 每分钟采集，5分钟粒度数据是按最近5分钟内求和   | 次/分钟  |
| lset 命令数     | cmdstat_lset     | 1分钟内 lset 命令请求数                          | 每分钟采集，5分钟粒度数据是按最近5分钟内求和   | 次/分钟  |
| mget 命令数     | cmdstat_mget     | 1分钟内 mget 命令请求数                          | 每分钟采集，5分钟粒度数据是按最近5分钟内求和   | 次/分钟  |
| mset 命令数     | cmdstat_mset     | 1分钟内 mset 命令请求数                          | 每分钟采集，5分钟粒度数据是按最近5分钟内求和   | 次/分钟  |
| msetnx 命令数   | cmdstat_msetnx   | 1分钟内 msetnx 命令请求数                        | 每分钟采集，5分钟粒度数据是按最近5分钟内求和   | 次/分钟  |
| set 命令数      | cmdstat_set      | 1分钟内 set 命令请求数                           | 每分钟采集，5分钟粒度数据是按最近5分钟内求和   | 次/分钟  |
| setbit 命令数   | cmdstat_setbit   | 1分钟内 setbit 命令请求数                        | 每分钟采集，5分钟粒度数据是按最近5分钟内求和   | 次/分钟  |
| setex 命令数    | cmdstat_setex    | 1分钟内 setex 命令请求数                         | 每分钟采集，5分钟粒度数据是按最近5分钟内求和   | 次/分钟  |
| setnx 命令数    | cmdstat_setnx    | 1分钟内 setnx 命令请求数                         | 每分钟采集，5分钟粒度数据是按最近5分钟内求和   | 次/分钟  |
| setrange 命令数 | cmdstat_setrange | 1分钟内 setrange 命令请求数                      | 每分钟采集，5分钟粒度数据是按最近5分钟内求和   | 次/分钟  |
| 每秒执行命令数     | qps              | 1分钟内命令总数除以60                             | 每分钟采集，5分钟粒度数据是按最近5分钟内求平均值 | 次/秒钟  |
| 连接数         | connections      | 1分钟内连接数总和                                | 每分钟采集，5分钟粒度数据是按最近5分钟内求和   | 个     |
| cpu 利用率      | cpu_us           | CPU 处于非空闲状态的百分比，取 /proc/stat 数据计算得出         | 每分钟采集，5分钟粒度数据是按最近5分钟内求平均值 | %     |
| 内网入流量       | in_flow          | 1分钟内入流量总和                                | 每分钟采集，5分钟粒度数据是按最近5分钟内求和   | Mb/分钟 |
| key总数       | keys             | 1分钟内 key 数量的最大值                            | 每分钟采集，5分钟粒度数据是按最近5分钟内求最大值 | 个     |
| 内网出流量       | out_flow         | 1分钟内出流量总和                                | 每分钟采集，5分钟粒度数据是按最近5分钟内求和   | Mb/分钟 |
| 所有 get 命令数    | stat_get         | 1分钟内 get, hget, hgetall, hmget, mget, getbit, getrange 命令请求数 | 每分钟采集，5分钟粒度数据是按最近5分钟内求和   | 次/分钟  |
| 所有 set 命令数    | stat_set         | 1分钟内 set, hset, hmset, hsetnx, lset, mset, msetnx, setbit, setex, setrange, setnx 命令请求数 | 每分钟采集，5分钟粒度数据是按最近5分钟内求和   | 次/分钟  |
| 已使用容量       | storage          | 1分钟内已使用容量的最大值                            | 每分钟采集，5分钟粒度数据是按最近5分钟内求最大值 | MB/分钟 |
| 容量使用率       | storage_us       | 1分钟内已使用容量的百分比最大值                         | 每分钟采集，5分钟粒度数据是按最近5分钟内求最大值 | %     |


## 3. 输出参数

| 参数名称       | 类型       | 描述                  |
| ---------- | -------- | ------------------- |
| code       | Int      | 错误码， 0： 成功，其他值表示失败 |
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
| -513 | DB 操作失败  | InternalError.DBoperationFail        |

## 5. 示例

输入

<pre>
https://monitor.api.qcloud.com/v2/index.php?
&<a href="/doc/api/405/公共请求参数" title="公共请求参数">公共请求参数</a>
&namespace=qce/redis
&metricName=cache_hit_ratio
&dimensions.0.name=redis_uuid
&dimensions.0.value=crs-ifmymj41
&startTime=2016-06-28 14:10:00
&endTime=2016-06-28 14:20:00
</pre>

输出

```shell
{
	"code": 0,
	"message": "",
	"metricName": "cache_hit_ratio",
	"startTime": "2016-06-28 14:10:00",
	"endTime": "2016-06-28 14:20:00",
	"period": 300,
	"dataPoints": [
		50,
		40,
		30
	]
}
```
