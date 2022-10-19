## 命名空间

Namespace=QCE/CYNOSDB_POSTGRES

## 监控指标

| 指标英文名      | 指标中文名   | 单位  | 维度       | 统计粒度                       |
| --------------- | ------------ | ----- | ---------- | --------------------------------- |
| CacheHitRate    | 缓存命中率   | %     | InstanceId | 5s、10s、60s、300s、3600s、86400s |
| Memoryusagerate | 内存使用率   | %     | InstanceId | 5s、60s、300s、3600ss、86400s     |
| ReadWriteCalls  | 总请求数     | 个/秒 | InstanceId | 5s、10s、60s、300s、3600s、86400s |
| ReadCalls       | 读请求数     | 个/秒 | InstanceId | 5s、10s、60s、300s、3600s、86400s |
| SqlRuntimeAvg   | 平均执行时延 | ms    | InstanceId | 5s、10s、60s、300s、3600s、86400s |
| StorageUsage    | 存储使用量   | GB    | InstanceId | 5s、60s、300s、3600s、86400s      |
| WriteCalls      | 写请求数     | 个/秒 | InstanceId | 5s、10s、60s、300s、3600s、86400s |
| DbConnections   | 总连接数     | 个    | InstanceId | 5s、60s、300s、3600s、86400s      |
| CpuUsageRate    | CPU利用率    | %     | InstanceId | 5s、60s、300s、3600s、86400s      |

## 各维度对应参数总览

| 参数名称                       | 维度名称   | 维度解释                     | 格式                                                         |
| :----------------------------- | :--------- | :--------------------------- | :----------------------------------------------------------- |
| Instances.N.Dimensions.0.Name  | InstanceId | TDSQL-C PostgreSQL  实例 ID  | 输入 String 类型维度名称：InstanceId                         |
| Instances.N.Dimensions.0.Value | InstanceId | TDSQL-C PostgreSQL 的实例 ID | 输入具体实例 ID，例如：tdcpg-ins-1abc2df3，可通过 [DescribeClusterInstances](https://cloud.tencent.com/document/product/1556/70688) 查询 |

## 入参说明

**查询 TDSQL-C PostgreSQL 版监控数据，入参取值如下：**
&Namespace=QCE/CYNOSDB_POSTGRES
&Instances.N.Dimensions.0.Name=InstanceId
&Instances.N.Dimensions.0.Value= TDSQL-C PostgreSQL 的实例 ID
