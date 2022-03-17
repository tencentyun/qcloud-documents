
## 命名空间

Namespace=QCE/CYNOSDB_MYSQL

## 监控指标
| 指标英文名                    | 指标中文名                                                   | 单位  | 维度                  | 统计粒度                     |
| ----------------------------- | ------------------------------------------------------------ | ----- | --------------------- | ---------------------------- |
| BytesSent                     | 内网出流量                                                   | MB/s  | InstanceId            | 5s、60s、300s、3600s、86400s |
| BytesReceived                 | 内网入流量                                                   | MB/s  | InstanceId            | 5s、60s、300s、3600s、86400s |
| Tps                           | 每秒事务数                                                   | 个/秒 | InstanceId            | 5s、60s、300s、3600s、86400s |
| ComDelete                     | 删除数                                                       | 个/秒 | InstanceId            | 5s、60s、300s、3600s、86400s |
| ComInsert                     | 插入数                                                       | 个/秒 | InstanceId            | 5s、60s、300s、3600s、86400s |
| ComUpdate                     | 更新数                                                       | 个/秒 | InstanceId            | 5s、60s、300s、3600s、86400s |
| CpuUsageRate                  | CPU使用率                                                    | %     | InstanceId            | 5s、60s、300s、3600s、86400s |
| MemoryUse                     | 内存占用                                                     | MB    | InstanceId            | 5s、60s、300s、3600s、86400s |
| CacheHits                     | 缓存命中数                                                   | 个    | InstanceId            | 5s、60s、300s、3600s、86400s |
| Qps                           | 请求数                                                       | 个/秒 | InstanceId            | 5s、60s、300s、3600s、86400s |
| StorageUsage                  | 存储使用量                                                   | GB    | InstanceId            | 5s、60s、300s、3600s、86400s |
| ComSelect                     | 查询数                                                       | 个/秒 | InstanceId            | 5s、60s、300s、3600s、86400s |
| DbConnections                 | 连接数                                                       | 个    | InstanceId            | 5s、60s、300s、3600s、86400s |
| MaxConnections                | 最大连接数                                                   | 个    | InstanceId            | 5s、60s、300s、3600s         |
| CacheHitRate                  | 缓存命中率                                                   | %     | InstanceId            | 5s、60s、300s、3600s、86400s |
| DataVolumeAllocate            | 数据表空间分配量                                             | GB    | InstanceId            | 5s、60s、300s、3600s、86400s |
| DataVolumeUsage               | 数据表空间使用量                                             | GB    | InstanceId            | 5s、60s、300s、3600s、86400s |
| TmpVolumeAllocate             | 临时表空间分配量                                             | GB    | InstanceId            | 5s、60s、300s、3600s、86400s |
| TmpVolumeUsage                | 临时表空间使用量                                             | GB    | InstanceId            | 5s、60s、300s、3600s、86400s |
| UndoVolumeAllocate            | undo表空间分配量                                             | GB    | InstanceId            | 5s、60s、300s、3600s、86400s |
| UndoVolumeUsage               | undo表空间使用量                                             | GB    | InstanceId            | 5s、60s、300s、3600s、86400s |
| CreatedTmpTables              | 创建临时表的数量                                             | 个    | InstanceId            | 5s、60s、300s、3600s、86400s |
| InnodbCacheHitRate            | 查询时间超过long_query_time秒的查询个数                      | %     | InstanceId            | 5s、60s、300s、3600s、86400s |
| InnodbCacheUseRate            | InnoDB引擎的缓存使用率                                       | %     | InstanceId            | 5s、60s、300s、3600s、86400s |
| SlowQueries                   | 查询时间超过long_query_time秒的查询个数                      | 个    | InstanceId            | 5s、60s、300s、3600s、86400s |
| ThreadsRunning                | 激活的线程数                                                 | 个    | InstanceId            | 5s、60s、300s、3600s、86400s |
| HandlerRollback               | 每秒事务回滚的次数                                           | 个    | InstanceId            | 5s、60s、300s、3600s、86400s |
| HandlerCommit                 | 每秒事务提交的次数                                           | 个    | InstanceId            | 5s、60s、300s、3600s、86400s |
| InnodbRowsDeleted             | InnoDB引擎每秒删除的行数                                     | 个    | InstanceId            | 5s、60s、300s、3600s、86400s |
| InnodbRowsInserted            | InnoDB引擎每秒插入的行数                                     | 个    | InstanceId            | 5s、60s、300s、3600s、86400s |
| InnodbRowsUpdated             | InnoDB引擎每秒更新的行数                                     | 个    | InstanceId            | 5s、60s、300s、3600s、86400s |
| InnodbRowsRead                | InnoDB引擎每秒读取的行数                                     | 个    | InstanceId            | 5s、60s、300s、3600s、86400s |
| ReplicateLag                  | 备实例 Redo 复制延迟                                         | ms    | InstanceId            | 5s、60s、300s、3600s、86400s |
| ReplicateLsnLag               | 备实例 Redo 复制落后的lsn距离                                | B     | InstanceId            | 5s、60s、300s、3600s、86400s |
| ReplicateStatus               | 备实例的复制状态                                             | -     | InstanceId            | 5s、60s、300s、3600s、86400s |
| InnodbBufferPoolWriteRequests | InnoDB 引擎每秒已完成的逻辑写请求次数                        | 个    | InstanceId            | 5s、60s、300s、3600s、86400s |
| InnodbBufferPoolReadRequests  | InnoDB 引擎每秒已完成的逻辑读请求次数                        | 个    | InstanceId            | 5s、60s、300s、3600s、86400s |
| Memoryuserate                 | 内存使用率                                                   | %     | InstanceId            | 5s、60s、300s、3600s、86400s |
| Volumerate                    | 数据表空间分配率                                             | %     | InstanceId            | 5s、60s、300s、3600s、86400s |
| Logcapacity                   | 日志占用的存储空间                                           | MB    | InstanceId            | 5s、60s、300s、3600s、86400s |
| Capacity                      | 占用的总存储空间                                             | MB    | InstanceId            | 5s、60s、300s、3600s、86400s |
| Comreplace                    | 每秒 replace 数                                              | 个/秒 | InstanceId            | 5s、60s、300s、3600s、86400s |
| Threadscreated                | 创建线程数                                                   | 个    | InstanceId            | 5s、60s、300s、3600s、86400s |
| Selectscan                    | 查询全表扫描数                                               | 个/秒 | InstanceId            | 5s、60s、300s、3600s、86400s |
| LatencyP99                    | 完成时间在统计时间段内的请求，99%的请求执行时间小于或等于该值 | us    | ClusterId、InstanceId | 5s、60s、300s、3600s、86400s |
| LatencyP95                    | 完成时间在统计时间段内的请求，95%的请求执行时间小于或等于该值 | us    | ClusterId、InstanceId | 5s、60s、300s、3600s、86400s |
| LatencyDeleteP95              | 完成时间在统计时间段内的delete请求，95%的请求执行时间小于或等于该值 | us    | ClusterId、InstanceId | 5s、60s、300s、3600s、86400s |
| LatencyDeleteP99              | 完成时间在统计时间段内的delete请求，99%的请求执行时间小于或等于该值 | us    | ClusterId、InstanceId | 5s、60s、300s、3600s、86400s |
| LatencyInsertP95              | 完成时间在统计时间段内的insert请求，95%的请求执行时间小于或等于该值 | us    | ClusterId、InstanceId | 5s、60s、300s、3600s、86400s |
| LatencyInsertP99              | 完成时间在统计时间段内的insert请求，99%的请求执行时间小于或等于该值 | us    | ClusterId、InstanceId | 5s、60s、300s、3600s、86400s |
| LatencyOtherP95               | 完成时间在统计时间段内的other请求，95%的请求执行时间小于或等于该值 | us    | ClusterId、InstanceId | 5s、60s、300s、3600s、86400s |
| LatencyOtherP99               | 完成时间在统计时间段内的other请求，99%的请求执行时间小于或等于该值 | us    | ClusterId、InstanceId | 5s、60s、300s、3600s、86400s |
| LatencyReplaceP95             | 完成时间在统计时间段内的replace请求，95%的请求执行时间小于或等于该值 | us    | ClusterId、InstanceId | 5s、60s、300s、3600s、86400s |
| LatencyReplaceP99             | 完成时间在统计时间段内的replace请求，99%的请求执行时间小于或等于该值 | us    | ClusterId、InstanceId | 5s、60s、300s、3600s、86400s |
| LatencySelectP95              | 完成时间在统计时间段内的select请求，95%的请求执行时间小于或等于该值 | us    | ClusterId、InstanceId | 5s、60s、300s、3600s、86400s |
| LatencySelectP99              | 完成时间在统计时间段内的select请求，99%的请求执行时间小于或等于该值 | us    | ClusterId、InstanceId | 5s、60s、300s、3600s、86400s |
| LatencyUpdateP95              | 完成时间在统计时间段内的update请求，95%的请求执行时间小于或等于该值 | us    | ClusterId、InstanceId | 5s、60s、300s、3600s、86400s |
| LatencyUpdateP99              | 完成时间在统计时间段内的update请求，99%的请求执行时间小于或等于该值 | us    | ClusterId、InstanceId | 5s、60s、300s、3600s、86400s |
> ?每个指标的统计粒度（Period）可取值不一定相同，可通过 [DescribeBaseMetrics](https://cloud.tencent.com/document/product/248/30351) 接口获取每个指标支持的统计粒度信息。

## 各维度对应参数总览

| 参数名称                       | 维度名称   | 维度解释                 | 格式                                             |
| :----------------------------- | :--------- | :----------------------- | :----------------------------------------------- |
| Instances.N.Dimensions.0.Name  | InstanceId | 数据库实例 ID 的维度名称 | 输入String 类型维度名称：InstanceId              |
| Instances.N.Dimensions.0.Value | InstanceId | 数据库的实例具体 ID      | 输入具体实例 ID，例如：cynosdbmysql-ins-12ab34cd |
| Instances.N.Dimensions.1.Name  | ClusterId  | 集群 ID 的维度名称       | 输入String 类型维度名称：ClusterId               |
| Instances.N.Dimensions.1.Value | ClusterId  | 数据库具体的集群 ID      | 输入具体集群 ID，例如：6179109757                |

## 入参说明

**查询云数据库（CynosDB for MySQL）产品监控数据，入参取值如下：**
非时延指标：
&Namespace=QCE/CYNOSDB_MYSQL
&Instances.N.Dimensions.0.Name=InstanceId
&Instances.N.Dimensions.0.Value=CynosDB 数据库中具体实例的 ID

时延相关指标：
&Namespace=QCE/CYNOSDB_MYSQL
&Instances.N.Dimensions.0.Name=InstanceId
&Instances.N.Dimensions.0.Value=CynosDB 数据库中具体实例的 ID
&Instances.N.Dimensions.1.Name=ClusterId 
&Instances.N.Dimensions.1.Value=数据库具体的集群 ID  


