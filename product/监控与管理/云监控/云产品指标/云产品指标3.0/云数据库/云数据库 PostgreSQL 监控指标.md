## 命名空间

Namespace=QCE/POSTGRES

## 监控指标


| 指标英文名                  | 指标中文名|指标含义           |单位           |维度|
| --------------------- | ------------ | ---- |---- | --------------------- |
| Connections   | 连接数     | 实例的活跃连接历史变化趋势 | 个   |resourceId|
| Cpu | CPU 利用率 | 实例 CPU 使用率，由于在闲时采用灵活的 CPU 限制策略，CPU 利用率可能大于100% | %   |resourceId|
| HitPercent          | 缓冲区缓存命中率   | 数据缓存命中率 | %  |resourceId|
| InFlow            | 输入流量   | 实例读写输入的流量 | KB/秒  |resourceId|
| OutFlow         | 	输出流量       | 实例读写输出的流量 | KB/秒   |resourceId|
| Iops          | 	磁盘 IOPS  | 实例的 IOPS（每秒的请求次数) | 次/秒  |resourceId|
| Memory          | 内存占用   | 实例占用磁盘的可用空间 | KB  |resourceId|
| OtherCalls          | 	其他请求数   | 除了读和写以外的请求总数（例如 Drop），按分钟累加 | 次/分钟  |resourceId|
| Qps             | 	每秒查询数       | 每秒查询次数 | 次/秒  |resourceId|
| WriteCalls        | 	写请求数       | 写请求每分钟总数 | 次/分钟    |resourceId|
| ReadCalls           | 读请求数       |读请求每分钟总数  |次/分钟  |resourceId|
| ReadWriteCalls          | 读写请求数          | 读写（增删改查）请求每分钟总数 | 次/分钟  |resourceId|
| RemainXid    | 	剩余XID数量     | 剩余的 Transaction Id 数量，Transaction Id 最大有2^32个，小于1000000建议手工执行 vacuum full | 个    |resourceId|
| SqlRuntimeAvg        | 平均执行时延       | 所有 SQL 请求的平均执行时间，不包含事务里面的 SQL | Ms    |resourceId|
| SqlRuntimeMax        | 最长TOP10执行时延       | 执行时间最长的 TOP10 的 SQL 的平均值 | Ms    |resourceId|
| SqlRuntimeMin        | 	最短TOP10执行时延       | 执行时间最短的 TOP10 的 SQL 的平均值 | Ms    |resourceId|
| Storage        | 已用存储空间       | 实例使用储存容量 | GB    |resourceId|
| XlogDiff        | 		主备 XLOG 同步差异     | 每分钟采样，主备 XLOG 的同步的大小差异，代表着同步的延迟，越小越好 | Byte   |resourceId|
| SlowQueryCnt | 慢查询数量 | 查询时间超过规定时间内（默认为1s）的查询的个数 | 次 |resourceId|
| StorageRate | 存储空间使用率 | 实例储存空间使用率 | % |resourceId|

> ?每个指标的统计粒度（Period）可取值不一定相同，可通过 [DescribeBaseMetrics](https://cloud.tencent.com/document/product/248/30351) 接口获取每个指标支持的统计粒度。

## 各维度对应参数总览

| 参数名称               | 维度名称             | 维度解释          | 格式                            |
| ------------------ | ---------------- | ------------- | ----------------------------- |
| Instances.N.Dimensions.0.Name  | resourceId              | resourceId 维度名称   | 输入 String 类型维度名称：resourceId         |
| Instances.N.Dimensions.0.Value | resourceId              | 实例具体的 resourceId       | 输入实例的具体 resourceId，例如：postgres-123456       |


## 入参说明

查询 PostgreSQL 监控数据，入参取值如下：
&Namespace=QCE/POSTGRES
&Instances.N.Dimensions.0.Name=resourceId
&Instances.N.Dimensions.0.Value 为实例的 resourceId 
