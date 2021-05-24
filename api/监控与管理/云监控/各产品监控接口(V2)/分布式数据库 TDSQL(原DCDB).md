## 1. 接口描述

域名：monitor.api.qcloud.com
接口：GetMonitorData

分布式数据库 TDSQL（ TencentDB for TDSQL，TDSQL）（曾用名：分布式数据库 DCDB）是部署在腾讯云公有云上的一种支持自动水平拆分的 share nothing 架构的分布式数据库。分布式数据库即业务获取是完整的逻辑库表，后端却将库表均匀的拆分到多个物理分片节点。目前，TDSQL 默认部署主备架构且提供了容灾、备份、恢复、监控、迁移等方面的全套解决方案，适用于 TB 或 PB 级的海量数据库场景。具体介绍请参见 [分布式数据库 TDSQL](https://cloud.tencent.com/document/product/557/7700)。

查询分布式数据库监控数据，入参取值如下：
namespace：qce/dcdb

维度名称取值：instanceId,topicId
dimensions.0.name=uuid
dimensions.0.value=实例 ID
dimensions.1.name=shardId
dimensions.1.value=实例下具体的分片 ID


## 2. 输入参数

以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见 <a href="/doc/api/405/公共请求参数" title="公共请求参数">公共请求参数</a> 页面。其中，此接口的 Action 字段为 GetMonitorData。

### 2.1 输入参数

| 参数名称               | 必选   | 类型       | 输入内容      | 描述                                       |
| ------------------ | ---- | -------- | --------- | ---------------------------------------- |
| namespace          | 是    | String   | qce/dcdb   | 命名空间，每个云产品会有一个命名空间，具体名称见输入内容一栏。          |
| metricName         | 是    | String   | 具体的指标名称   | 指标名称，具体名称见2.2                            |
| dimensions.0.name  | 是    | String   | uuid      | 入参为实例的 uuid                               |
| dimensions.0.value | 是    | String   | 实例具体的 uuid | 输入实例的具体 uuid，如 dcdbt-0gfryg60              |
| dimensions.1.name  | 否    | String   | shardId | 入参为实例具体的分片 ID，在需要查询分片的监控数据时传递，不传则查询汇总的实例监控数据     |
| dimensions.1.value | 否    | String   | 实例具体的分片 ID | 输入实例的具体分片 ID，如 shard-0mzlzl89    |
| period             | 否    | Int      | 60/300    | 监控统计周期，绝大部分指标支持60s统计粒度，部分指标仅支持300s统计粒度，统计粒度根据指标的不同而变。输入参数时可参考2.2的指标详情列表。 |
| startTime          | 否    | Datetime | 起始时间      | 起始时间，如 “2016-01-01 10:25:00”。 默认时间为当天的 “00:00:00” |
| endTime            | 否    | Datetime | 结束时间      | 结束时间，默认为当前时间。 endTime 不能小于 startTime       |

### 2.2 指标名称

| 指标名称                  | 含义           | 单位   | 统计粒度（period）|
| --------------------- | ------------ | ---- |-------|
| cpu_usage_rate        | CPU 使用率       | %    | 60s、300s |
| mem_hit_rate          | 缓存命中率      | % | 60s、300s |
| data_disk_used_rate   | 磁盘空间利用率  | % | 60s、300s |
| mem_available         | 可用缓存空间       | GB   | 60s、300s |
| data_disk_available         | 可用磁盘空间       | GB   | 60s、300s |
| binlog_used_disk         | 已用日志磁盘空间       | GB   | 60s、300s |
| disk_iops         | IO 利用率       | %   | 60s、300s |
| conn_active           | 总连接数       | 次/秒  | 60s、300s |
| conn_running          | 活跃连接数          | 次/秒  | 60s、300s |
|  total_orig_sql  | SQL 总数  | 次/秒 | 60s、300s |
|  total_error_sql  | SQL 错误数  | 次/秒 | 60s、300s |
|  total_success_sql  | SQL 成功数  | 次/秒 | 60s、300s |
|  long_query  | 慢查询数  | 次/秒 | 60s、300s |
|  time_range_0  | 耗时(1~5ms)请求数  | 次/秒 | 60s、300s |
|  time_range_1  | 耗时(5~20ms)请求数  | 次/秒 | 60s、300s |
|  time_range_2  | 耗时(20~30ms)请求数  | 次/秒 | 60s、300s |
|  time_range_3  | 耗时(大于30ms)请求数  | 次/秒 | 60s、300s |
|  request_total  | 总请求数(QPS)  | 次/秒 | 60s、300s |
|  select_total  | 查询数  | 次/秒 | 60s、300s |
|  update_total  | 更新数  | 次/秒 | 60s、300s |
|  insert_total  | 插入数  | 次/秒 | 60s、300s |
|  replace_total  |  覆盖数 | 次/秒 | 60s、300s |
|  delete_total  |  删除数 | 次/秒 | 60s、300s |
|  master_switched_total  |  主从切换 | 次/秒 | 60s、300s |
|  slave_delay  | 主从延迟  | ms | 60s、300s |
|  innodb_buffer_pool_reads | innodb 磁盘读页次数  | 次/秒 | 60s、300s |
|  innodb_buffer_pool_read_requests | innodb 缓冲池读页次数  | 次/秒 | 60s、300s |
|  innodb_buffer_pool_read_ahead | innodb 缓冲池预读页次数  | 次/秒 | 60s、300s |
|  innodb_rows_deleted | innodb 执行 DELETE 行数  | 次/秒 | 60s、300s |
|  innodb_rows_inserted | innodb 执行 INSERT 行数  | 次/秒 | 60s、300s |
|  innodb_rows_read | innodb 执行 UPDATE 行数  | 次/秒 | 60s、300s |
|  innodb_rows_updated | innodb 执行 UPDATE 行数  | 次/秒 | 60s、300s |

## 3. 输出参数

| 参数名称       | 类型       | 描述                  |
| ---------- | -------- | ------------------- |
| code       | Int      | 错误码，0: 成功, 其他值表示失败 |
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

### 5.1 查询实例汇总监控数据

#### 输入

<pre>
https://monitor.api.qcloud.com/v2/index.php?
&<a href="/doc/api/405/公共请求参数" title="公共请求参数">公共请求参数</a>
&namespace=qce/dcdb
&metricName=cpu_usage_rate
&dimensions.0.name=uuid
&dimensions.0.value=dcdbt-52s53yyh
&startTime=2018-05-23 17:00:00
&endTime=2018-05-23 17:20:00
</pre>

#### 输出

```
{
    "code": 0,
    "message": "",
    "metricName": "cpu_usage_rate",
    "startTime": "2018-05-23 17:00:00",
    "endTime": "2018-05-23 17:20:00",
    "period": 300,
    "dataPoints": [
        3,
        3,
        3,
        3,
        3
    ]
}
```

### 5.2 查询实例分片监控数据
#### 输入

<pre>
https://monitor.api.qcloud.com/v2/index.php?
&<a href="/doc/api/405/公共请求参数" title="公共请求参数">公共请求参数</a>
&namespace=qce/dcdb
&metricName=cpu_usage_rate
&dimensions.0.name=uuid
&dimensions.0.value=dcdbt-52s53yyh
&dimensions.1.name=shardId
&dimensions.1.value=shard-n8f80yrv
&startTime=2018-05-23 17:00:00
&endTime=2018-05-23 17:20:00
</pre>

#### 输出

```
{
    "code": 0,
    "message": "",
    "metricName": "cpu_usage_rate",
    "startTime": "2018-05-23 17:00:00",
    "endTime": "2018-05-23 17:20:00",
    "period": 300,
    "dataPoints": [
        3,
        2,
        3,
        2,
        2
    ]
}
```
