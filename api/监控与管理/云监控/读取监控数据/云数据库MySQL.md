## 1. 接口描述

域名：monitor.api.qcloud.com
接口：GetMonitorData

云数据库MySQL（Cloud Database for MySQL）是腾讯云基于全球最受欢迎的开源数据库MySQL专业打造的高性能分布式数据存储服务。具体介绍请参考<a href="/doc/product/236/简介" title="简介">云数据库MySQL</a>页面。

查询云数据库（MySQL）产品监控数据，入参取值如下：
namespace：qce/cdb
dimensions.0.name=unInstanceId
dimensions.0.value为cdb实例id

## 2. 输入参数

以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见<a href="/doc/api/405/公共请求参数" title="公共请求参数">公共请求参数</a>页面。其中，此接口的Action字段为GetMonitorData。

### 2.1输入参数

| 参数名称               | 必选   | 类型       | 输入内容         | 描述                                       |
| ------------------ | ---- | -------- | ------------ | ---------------------------------------- |
| namespace          | 是    | String   | qce/cvm      | 命名空间，每个云产品会有一个命名空间，具体名称见输入内容一栏。          |
| metricName         | 是    | String   | 具体的指标名称      | 指标名称，具体名称见2.2                            |
| dimensions.0.name  | 是    | String   | unInstanceId | 入参为cdb实例Id                               |
| dimensions.0.value | 是    | String   | CDB实例的具体Id   | 输入CDB实例的具体Id，如cdb-e242adzf               |
| period             | 否    | Int      | 60/300       | 监控统计周期，绝大部分指标支持60s统计粒度，部分指标仅支持300s统计粒度，统计粒度根据指标的不同而变。输入参数时可参考2.2的指标详情列表。 |
| startTime          | 否    | Datetime | 起始时间         | 起始时间，如"2016-01-01 10:25:00"。 默认时间为当天的”00:00:00” |
| endTime            | 否    | Datetime | 结束时间         | 结束时间，默认为当前时间。 endTime不能小于startTime       |
### 2.2 指标名称

| 指标名称                  | 含义             | 单位     | 统计粒度（period） |
| --------------------- | -------------- | ------ | ------------ |
| slow_queries          | 慢查询数           | 次/秒    |              |
| max_connections       | 最大连接数          | 个      |              |
| select_scan           | 全表扫描数          | 次/秒    |              |
| select_count          | 查询数            | 次/秒    |              |
| com_update            | 更新数            | 次/秒    |              |
| com_delete            | 删除数            | 次/秒    |              |
| com_insert            | 插入数            | 次/秒    |              |
| com_replace           | 覆盖数            | 次/秒    |              |
| queries               | 总请求数           | 次/秒    |              |
| threads_connected     | 当前打开连接数        | 个      |              |
| real_capacity         | 磁盘使用空间         | MB     |              |
| capacity              | 磁盘占用空间         | MB     |              |
| bytes_sent            | 内网出流量          | Byte/秒 |              |
| bytes_received        | 内网入流量          | Byte/秒 |              |
| qcache_use_rate       | 缓存使用率          | %      |              |
| qcache_hit_rate       | 缓存命中率          | %      |              |
| table_locks_waited    | 等待表锁次数         | 次/秒    |              |
| created_tmp_tables    | 临时表数量          | 次/秒    |              |
| innodb_cache_use_rate | innodb缓存使用率    | %      |              |
| innodb_cache_hit_rate | innodb缓存命中率    | %      |              |
| innodb_os_file_reads  | innodb读磁盘数量    | 次/秒    |              |
| innodb_os_file_writes | innodb写磁盘数量    | 次/秒    |              |
| innodb_os_fsyncs      | innodb fsync数量 | 次/秒    |              |
| key_cache_use_rate    | myisam缓存使用率    | %      |              |
| key_cache_hit_rate    | myisam缓存命中率    | %      |              |
| volume_rate           | 容量使用率          | %      |              |
| query_rate            | 查询使用率          | %      |              |
| qps                   | 每秒执行操作数        | 次/秒    |              |
| tps                   | 每秒执行事务数        | 次/秒    |              |
| cpu_use_rate          | CPU占比          | %      |              |
| memory_use            | 内存占用           | MB     |              |


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
&namespace=qce/cdb
&metricName=slow_queries
&dimensions.0.name=uInstanceId
&dimensions.0.value=cdb-e242adzf
&startTime=2016-06-28 14:10:00
&endTime=2016-06-28 14:20:00
```

输出

```
{
	"code": 0,
	"message": "",
	"metricName": "slow_queries",
	"startTime": "2016-06-28 14:10:00",
	"endTime": "2016-06-28 14:20:00",
	"period": 300,
	"dataPoints": [
		55,
		46，
		33
	]
}
```