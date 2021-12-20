## 命名空间

Namespace=QCE/SQLSERVER


## 监控指标

### 常见指标

| 指标英文名           | 指标中文名          | 含义  | 单位 | 维度 |
|---------|---------|---------|---------|---------|
| Cpu                 | CPU 利用率 |实例 CPU 消耗的百分比                     | %     | resourceId |
| Transactions        | 事务数 | 平均每秒的事务数                          | 次/秒 |resourceId |
| Connections         | 连接数 |平均每秒用户连接数据库的个数              | 个    |resourceId |
| Requests            |  请求数  |每秒请求次数                              | 次/秒 | resourceId |
| Logins              | 登录次数 | 每秒登录次数                              | 次/秒 | resourceId |
| Logouts             | 登出次数  | 每秒登出次数                              | 次/秒 | resourceId |
| Storage             | 已用存储空间 |实例数据库文件和日志文件占用的空间总和    | GB    |resourceId |
| InFlow              | 输入流量|所有连接输入包大小总和                    | KB/s  |resourceId |
| OutFlow             | 输出流量|所有连接输出包大小总和                    | KB/s  |resourceId |
| Iops                | 磁盘 IOPS|每秒磁盘读写次数                              | 次/秒 |resourceId |
| DiskReads           |读取磁盘次数 |每秒读取磁盘次数                          | 次/秒 |resourceId |
| DiskWrites          | 写入磁盘次数 |每秒写入磁盘次数                          | 次/秒 | resourceId |
|ServerMemory|内存占用|  	实际内存消耗量 | MB | resourceId |

### 性能优化指标

| 指标英文名           | 指标中文名          | 含义  | 单位 | 维度 |
|---------|---------|---------|---------|---------|
| SlowQueries         |  慢查询 |  运行时间超过1秒的查询数量                 | 个    | resourceId |
| BlockedProcesses    | 阻塞数 | 当前阻塞数量                              | 个    | resourceId |
| LockRequests        | 锁请求次数 |平均每秒锁请求的次数                      | 次/秒 | resourceId |
| UserErrors          | 用户错误数|平均每秒错误数   | 次/秒 | resourceId |
| SqlCompilations     |  SQL 编译数 |平均每秒 SQL 编译次数                     | 次/秒 | resourceId |
| SqlRecompilations   | SQL 重编译数 |平均每秒 SQL 重编译次数                   | 次/秒 |resourceId |
| FullScans           | 每秒钟 SQL 做全表扫描数目 |每秒不受限制的完全扫描数 | 次/秒 |resourceId |
| BufferCacheHitRatio | 缓冲区缓存命中率 |数据缓存（内存）命中率                    | %     | resourceId |
| LatchWaits          | 闩锁等待数量 |每秒闩锁等待数量                          | 次/秒 | resourceId |
| LockWaits           | 平均锁等待延迟 |每个导致等待的锁请求的平均等待时间       | Ms    | resourceId |
| NetworkIoWaits  |  IO 延迟时间|平均网络 IO 延迟时间                      | Ms    | resourceId |
| PlanCacheHitRatio   | 执行缓存缓存命中率  |每个 SQL 有一个执行计划，执行计划的命中率 | %     | resourceId |
|FreeStorage| 硬盘剩余容量 | 硬盘剩余容量百分比 |  %  | resourceId |

> ?每个指标的统计粒度（Period）可取值不一定相同，可通过 [DescribeBaseMetrics](https://cloud.tencent.com/document/product/248/30351) 接口获取每个指标支持的统计粒度。

## 各维度对应参数总览

| 参数名称                       | 维度名称   | 维度解释             | 格式                                            |
| ------------------------------ | ---------- | -------------------- | ----------------------------------------------- |
| Instances.N.Dimensions.0.Name  | resourceId | 实例资源 ID 的维度名称 | 输入 String 类型维度名称：resourceId              |
| Instances.N.Dimensions.0.Value | resourceId | 实例具体的资源 ID    | 输入实例的具体 resourceId，例如：mssql-dh0123456 |

## 入参说明

查询云数据库 SQL Server监控数据，入参取值如下：
&Namespace=QCE/SQLSERVER
&Instances.N.Dimensions.0.Name=resourceId
&Instances.N.Dimensions.0.Value 为实例的资源 ID 



