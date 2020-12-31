## 命名空间
Namespace=QCE/DCDB

## 监控指标
| 指标英文名                   | 指标中文名              | 单位  | 维度          |
| ---------------------------- | ----------------------- | ----- | ------------- |
| CpuUsageRate                 | CPU 使用率              | %     | uuid、shardId |
| MemHitRate                   | 缓存命中率              | %     | uuid、shardId |
| DataDiskUsedRate             | 磁盘空间利用率          | %     | uuid、shardId |
| MemAvailable                 | 可用缓存空间            | GB    | uuid、shardId |
| DataDiskAvailable            | 可用磁盘空间            | GB    | uuid、shardId |
| BinlogUsedDisk               | 已用日志磁盘空间        | GB    | uuid、shardId |
| DiskIops                     | IO 利用率               | %     | uuid、shardId |
| ConnActive                   | 总连接数                | 次/秒 | uuid、shardId |
| ConnRunning                  | 活跃连接数              | 次/秒 | uuid、shardId |
| TotalOrigSql                 | SQL 总数                | 次/秒 | uuid、shardId |
| TotalErrorSql                | SQL 错误数              | 次/秒 | uuid、shardId |
| TotalSuccessSql              | SQL 成功数              | 次/秒 | uuid、shardId |
| LongQuery                    | 慢查询数                | 次/秒 | uuid、shardId |
| TimeRange0                   | 耗时（1 - 5ms）请求数       | 次/秒 | uuid、shardId |
| TimeRange1                   | 耗时（5 - 20ms）请求数      | 次/秒 | uuid、shardId |
| TimeRange2                   | 耗时（20 - 30ms）请求数     | 次/秒 | uuid、shardId |
| TimeRange3                   | 耗时（大于30ms）请求数    | 次/秒 | uuid、shardId |
| RequestTotal                 | 总请求数（QPS）           | 次/秒 | uuid、shardId |
| SelectTotal                  | 查询数                  | 次/秒 | uuid、shardId |
| UpdateTotal                  | 更新数                  | 次/秒 | uuid、shardId |
| InsertTotal                  | 插入数                  | 次/秒 | uuid、shardId |
| ReplaceTotal                 | 覆盖数                  | 次/秒 | uuid、shardId |
| DeleteTotal                  | 删除数                  | 次/秒 | uuid、shardId |
| MasterSwitchedTotal          | 主从切换                | 次/秒 | uuid、shardId |
| SlaveDelay                   | 主从延迟                | Ms    | uuid、shardId |
| InnodbBufferPoolReads        | innodb 磁盘读页次数     | 次/秒 | uuid、shardId |
| InnodbBufferPoolReadRequests | innodb 缓冲池读页次数   | 次/秒 | uuid、shardId |
| InnodbBufferPoolReadAhead    | innodb 缓冲池预读页次数 | 次/秒 | uuid、shardId |
| InnodbRowsDeleted            | innodb 执行 DELETE 行数 | 次/秒 | uuid、shardId |
| InnodbRowsInserted           | innodb 执行 INSERT 行数 | 次/秒 | uuid、shardId |
| InnodbRowsRead               | innodb 执行 READ 行数 | 次/秒 | uuid、shardId |
| InnodbRowsUpdated            | innodb 执行 UPDATE 行数 | 次/秒 | uuid、shardId |

>? 分布式数据库所有指标的统计粒度可取值60s 、300s 。 每个指标的统计粒度（Period）可取值不一定相同，可通过 [DescribeBaseMetrics](https://cloud.tencent.com/document/product/248/30351) 接口获取每个指标支持的统计粒度。

##  各维度对应参数总览

| 参数名称                       | 维度名称 | 维度解释                                                     | 格式                                      |
| ------------------------------ | -------- | ------------------------------------------------------------ | ----------------------------------------- |
| Instances.N.Dimensions.0.Name  | uuid     | 数据库实例的维度名称                                         | 输入 String 类型维度名称：uuId             |
| Instances.N.Dimensions.0.Value | uuid     | 实例具体的 uuid                                              | 输入实例具体 uuid，例如：dcdbt-0gfryg60    |
| Instances.N.Dimensions.1.Name  | shardId  | 实例分片 ID 的维度名称，在需要查询分片的监控数据时传递，不传则查询汇总的实例监控数据 | 输入String 类型维度名称：shardId          |
| Instances.N.Dimensions.1.Value | shardId  | 实例具体的 shardId                                           | 输入实例具体分片 ID，例如：shard-0mzlzl89 |

## 入参说明

**查询分布式数据库 DCDB V3 监控数据，入参取值如下：**
&Namespace=QCE/DCDB
&Instances.N.Dimensions.0.Name=uuid
&Instances.N.Dimensions.0.Value=实例具体的 uuid
