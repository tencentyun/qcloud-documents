## 命名空间

Namespace=QCE/CES

## 监控指标

| 指标英文名                         | 指标中文名                 | 计算方式                                                 | 指标含义                             | 单位    |       维度      | 统计粒度（period） |
| ---------------------------------- | -------------------------- | -------------------------------------------------------- | ------------------------------------ | ------- | ----------- | ------------------ |
| Status                             | 集群健康状态               | ES 集群在统计周期内的最新值                               | 集群健康状态:0:Green,1:Yellow,2:Red  | -       | uInstanceId | 60s、300s          |
| DiskUsageAvg                       | 平均磁盘使用率             | ES 集群在统计周期内各节点磁盘使用率的平均值               | ES 集群各节点磁盘使用率的平均值      | %       | uInstanceId | 60s、300s          |
| DiskUsageMax                       | 最大磁盘使用率             | ES 集群在统计周期内各节点磁盘使用率的最大值               | ES 集群各节点磁盘使用率的最大值       | %       | uInstanceId | 60s、300s          |
| JvmMemUsageAvg                     | 平均 JVM 内存使用率          | ES 集群在统计周期内各节点 JVM 内存使用率的平均值            | ES 集群各节点 JVM 内存使用率的平均值    | %       | uInstanceId | 60s、300s          |
| JvmMemUsageMax                     | 最大 JVM 内存使用率          | ES 集群在统计周期内各节点 JVM 内存使用率的最大值            | ES 集群各节点 JVM 内存使用率的最大值    | %       | uInstanceId | 60s、300s          |
| JvmOldMemUsageAvg | 平均 JVM old 区内存使用率 |ES 集群在统计周期内各节点 JVM old 区内存使用率的平均值 | ES 集群各节点 JVM old 区的平均内存使用率 | %        | uInstanceId | 60s、300s          |
| JvmOldMemUsageMax | 最大 JVM old 区内存使用率 | ES 集群在统计周期内各节点 JVM old 区内存使用率的最大值 | ES 集群各节点 JVM old 区的最大内存使用率 | %        | uInstanceId | 60s、300s          |
| CpuUsageAvg                        | 平均 CPU 使用率              | ES 集群在统计周期内各节点 CPU 使用率的平均值                | ES集群各节点 CPU使用率的平均值        | %       | uInstanceId | 60s、300s          |
| CpuUsageMax                        | 最大 CPU 使用率              | ES 集群在统计周期内各节点 CPU 使用率的最大值                | ES集群各节点 CPU使用率的最大值        | %       | uInstanceId | 60s、300s          |
| CpuLoad1minAvg                     | 集群1分钟 CPU 平均负载       | ES 集群在统计周期内各节点1分钟 CPU 负载的平均值             | ES集群各节点 CPU 1分钟CPU负载的平均值 | -       | uInstanceId | 60s、300s          |
| CpuLoad1minMax                     | 集群1分钟 CPU 最大负载       | ES 集群在统计周期内各节点1分钟 CPU 负载的最大值             | ES集群各节点 CPU 1分钟负载的最大值    | -       | uInstanceId | 60s、300s          |
| IndexLatencyAvg                    | 平均写入延迟               | ES 集群在统计周期内写入延迟的平均值                       | ES 集群写入延迟的平均值               | ms      | uInstanceId | 60s、300s          |
| IndexLatencyMax                    | 最大写入延迟               | ES 集群在统计周期内写入延迟的最大值                       | ES 集群写入延迟的最大值               | ms      | uInstanceId | 60s、300s          |
| SearchLatencyAvg                   | 平均查询延迟               | ES 集群在统计周期内查询延迟的平均值                       | ES 集群查询延迟的平均值               | ms      | uInstanceId | 60s、300s          |
| SearchLatencyMax                   | 最大查询延迟               | ES 集群在统计周期内查询延迟的最大值                       | ES 集群查询延迟的最大值               | ms      | uInstanceId | 60s、300s          |
| IndexSpeed                         | 写入速度                   | ES 集群单周期内写入速度的平均值                           | ES 集群每秒完成写入操作次数           | count/s | uInstanceId | 60s、300s          |
| SearchCompletedSpeed               | 查询速度                   | ES 集群单周期内查询速度的平均值                           | ES 集群每秒完成查询操作次数           | count/s | uInstanceId | 60s、300s          |
| BulkRejected<br>CompletedPercent   | bulk拒绝率                 | ES 集群在统计周期内 bulk 操作被拒绝次数占 bulk 总次数的百分比 | bulk 操作被拒绝次数占总次数的百分比   | %       | uInstanceId | 60s、300s          |
| SearchRejected<br>CompletedPercent | 查询拒绝率                 | ES 集群在统计周期内查询操作被拒绝次数占查询总次数的百分比 | 查询操作被拒绝次数占总次数的百分比   | %       | uInstanceId | 60s, 300s          |
| IndexDocs                          | 文档总数                   | ES 集群在统计周期内文档总数的平均值                       | ES 集群中的文档总数                   | count   | uInstanceId | 60s、300s          |
| AutoSnapshotStatus                 | ES 集群自动备份任务执行状态 | ES 集群在统计周期内最后一次执行自动备份任务的状态         | ES 集群自动备份任务的执行状态         | -       | uInstanceId | 300s               |

>?每个指标对应的统计粒度（Period）可取值不一定相同，可通过 [DescribeBaseMetrics](https://cloud.tencent.com/document/product/248/30351) 接口获取每个指标支持的统计粒度。

##  各维度对应参数总览

| 参数名称                       | 维度名称    | 维度解释            | 格式                                |
| ------------------------------ | ----------- | ------------------- | ----------------------------------- |
| Instances.N.Dimensions.0.Name  | uInstanceId | ES 实例 ID 的维度名称 | 输入 String 类型维度名称：uInstanceId |
| Instances.N.Dimensions.0.Value | uInstanceId | ES 具体实例 ID       | 输入实例具体 ID，例如：es-example     |

## 入参说明

查询 Elasticsearch Service 监控数据，入参取值如下：
&Namespace=QCE/CES
&Instances.N.Dimensions.0.Name=uInstanceId
&Instances.N.Dimensions.0.Value=ES 具体实例 ID
