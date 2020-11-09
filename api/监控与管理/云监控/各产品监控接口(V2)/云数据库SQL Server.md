## 1. 接口描述

域名：`monitor.api.qcloud.com`
接口：GetMonitorData

云数据库 SQL Server 是腾讯云基于微软公司推出的 SQL Server 专业打造的云数据库。具体介绍请参见 <a href="/doc/product/238/产品概述" title="产品概述">云数据库 SQL Server</a> 文档。

查询云数据库 SQL Server 产品监控数据，入参取值如下：
namespace：qce/sqlserver
dimensions.0.name=resourceId 
dimensions.0.value 为实例的资源 ID

## 2. 输入参数

以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，详情请参见 <a href="/doc/api/405/公共请求参数" title="公共请求参数">公共请求参数</a> 文档。其中，此接口的 Action 字段为 GetMonitorData。

### 2.1 输入参数

| 参数名称               | 必选   | 类型       | 输入内容       | 描述                                       |
| ------------------ | ---- | -------- | ---------- | ---------------------------------------- |
| namespace          | 是    | String   | qce/cvm    | 命名空间，每个云产品会有一个命名空间，具体名称见输入内容一栏。          |
| metricName         | 是    | String   | 具体的指标名称    | 指标名称，具体名称见2.2                            |
| dimensions.0.name  | 是    | String   | resourceId | 入参必须为 resourceId                              |
| dimensions.0.value | 是    | String   | 实例具体的资源 ID  | 输入实例的具体资源 ID，如 mssql-dh01nvsb              |
| period             | 否    | Int      | 60/300     | 监控统计周期，绝大部分指标支持60s统计粒度，部分指标仅支持300s统计粒度，统计粒度根据指标的不同而变。输入参数时可参考2.2的指标名称列表 |
| startTime          | 否    | Datetime | 起始时间       | 起始时间，如 “2016-01-01 10:25:00”。 默认时间为当天的 “00:00:00” |
| endTime            | 否    | Datetime | 结束时间       | 结束时间，默认为当前时间，endTime 不能小于 startTime       |


### 2.2 指标名称

| 指标名称                   | 含义                    | 单位   |
| ---------------------- | --------------------- | ---- |
| cpu                    | 实例 CPU 消耗的百分比           | %    |
| transactions           | 平均每秒的事务数              | 次/秒  |
| connections            | 平均每秒用户连接数据库的个数        | 个    |
| requests               | 每秒请求次数                | 次/秒  |
| logins                 | 每秒登录次数                | 次/秒  |
| logouts                | 每秒登出次数                | 次/秒  |
| storage                | 实例数据库文件和日志文件占用的空间总和   | GB   |
| in_flow                | 所有连接输入包大小总和           | MB/s |
| out_flow               | 所有连接输出包大小总和           | MB/s |
| iops                   | 磁盘读写次数                | 次/秒  |
| disk_reads             | 每秒读取磁盘次数              | 次/秒  |
| disk_writes            | 每秒写入磁盘次数              | 次/秒  |
| slow_queries           | 运行时间超过1秒的查询数量         | 个    |
| blocked_processes      | 当前阻塞数量                | 个    |
| lock_requests          | 平均每秒锁请求的次数            | 次/秒  |
| user_errors            | 平均每秒错误数               | 次/秒  |
| sql_compilations       | 平均每秒 SQL 编译次数           | 次/秒  |
| sql_recompilations     | 平均每秒 SQL 重编译次数          | 次/秒  |
| full_scans             | 每秒不受限制的完全扫描数          | 次/秒  |
| buffer_cache_hit_ratio | 数据缓存（内存）命中率           | %    |
| latch_waits            | 每秒闩锁等待数量              | 次/秒  |
| lock_waits             | 每个导致等待的锁请求的平均等待时间     | ms   |
| network_io_waits       | 平均网络 IO 延迟时间            | ms   |
| plan_cache_hit_ratio   | 每个 SQL 有一个执行计划，执行计划的命中率 | %    |


## 3. 输出参数

| 参数名称       | 类型       | 描述                  |
| ---------- | -------- | ------------------- |
| code       | Int      | 错误码，0： 成功，其他值表示失败 |
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

#### 输入
<pre>
https://monitor.api.qcloud.com/v2/index.php?
&<a href="/doc/api/405/公共请求参数" title="公共请求参数">公共请求参数</a>
&namespace=qce/sqlserver
&metricName=cpu
&dimensions.0.name=resourceId
&dimensions.0.value=mssql-dh01nvsb
&startTime=2016-06-28 14:10:00
&endTime=2016-06-28 14:20:00
</pre>

#### 输出

```shell
{
	"code": 0,
	"message": "",
	"metricName": "cpu",
	"startTime": "2016-06-28 14:10:00",
	"endTime": "2016-06-28 14:20:00",
	"period": 300,
	"dataPoints": [
		50,
		47,
		44
	]
}
```
