
## 命名空间

Namespace=QCE/CYNOSDB_MYSQL

## 监控指标

| 指标英文名                   | 指标中文名             | 单位     | 维度 |
| ----------------------------- | -------------- | ------ | ------ |
|BytesReceived|内网入流量|MB/%| InstanceId |
|BytesSent|内网出流量|MB/%| InstanceId |
|ComDelete|删除数|次/秒| InstanceId |
|ComInsert|插入数|次/秒| InstanceId |
|ComSelect|查询数|次/秒| InstanceId |
|ComUpdate|更新数|次/秒| InstanceId |
|CpuUsageRate|CPU 使用率|%| InstanceId |
|DbConnections|连接数|个| InstanceId |
|MemoryUse|内存占用|MB| InstanceId |
|Qps|请求数|次/秒| InstanceId |
|StorageUsage|存储使用量|GB| InstanceId |
|Tps|每秒事务数|次/秒| InstanceId |
|CacheHitRate|缓存命中率|%| InstanceId |
|CacheHits|缓存命中数|次| InstanceId |
|DataVolumeUsage|数据表空间使用量|GB| InstanceId |
|DataVolumeAllocate|数据表空间分配量|GB| InstanceId |
|MaxConnections|最大连接数|次| InstanceId |
|UndoVolumeAllocate| undo 表空间分配量 |GB| InstanceId |
|UndoVolumeUsage| undo 表空间使用量 |GB| InstanceId |
|TmpVolumeAllocate|临时表空间分配量|GB| InstanceId |
|TmpVolumeUsage|临时表空间使用量|GB| InstanceId |

> ?每个指标的统计粒度（Period）可取值不一定相同，可通过 [DescribeBaseMetrics](https://cloud.tencent.com/document/product/248/30351) 接口获取每个指标支持的统计粒度信息。

## 各维度对应参数总览

| 参数名称               | 维度名称             | 维度解释          | 格式                            |
| ------------------ | ---------------- | ------------- | ----------------------------- |
| Instances.N.Dimensions.0.Name  | InstanceId              | 数据库实例 ID 的维度名称 | 输入String 类型维度名称：InstanceId              |
| Instances.N.Dimensions.0.Value | InstanceId              | 数据库的实例具体 ID  | 输入具体实例 ID，例如：cynosdbmysql-ins-12ab34cd |

## 入参说明

查询云数据库（CynosDB for MySQL）产品监控数据，入参取值如下：
&Namespace=QCE/CYNOSDB_MYSQL
&Instances.N.Dimensions.0.Name=InstanceId
&Instances.N.Dimensions.0.Value=CynosDB 数据库中具体实例的 ID 

