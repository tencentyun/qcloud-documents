## 命名空间

Namespace=QCE/CDWCH

## 监控指标

### 节点指标

| 指标英文名                    | 指标中文名                 | 单位  | 维度           |
| ----------------------------- | -------------------------- | ----- | -------------- |
| Zookeeperrequest              | zk 请求数                  | 个    | InstanceId、ip |
| Zookeepersession              | 当前 zk session 个数       | 个    | InstanceId、ip |
| Zookeeperwatch                | zkwatch 个数               | 个    | InstanceId、ip |
| Fileopen                      | 文件打开数                 | 个    | InstanceId、ip |
| NodeLoad1                     | 节点一分钟负载             | -     | InstanceId、ip |
| NodeLoad5                     | 5分钟负载                  | -     | InstanceId、ip |
| NodeLoad15                    | 15分钟负载                 | -     | InstanceId、ip |
| CpuLoadRate                   | CPU 负载比率               | %     | InstanceId、ip |
| DiskUsage                     | 数据盘使用率               | %     | InstanceId、ip |
| NodeNetworkReceiveBytesTotal  | 节点接收流量               | MB/s  | InstanceId、ip |
| NodeNetworkTransmitBytesTotal | 节点流出流量               | MB/s  | InstanceId、ip |
| MemUsage                      | 内存使用率                 | %     | InstanceId、ip |
| CpuUsage                      | CPU 使用率                 | %     | InstanceId、ip |
| CpuUsageAvg                   | CPU 平均使用率             | %     | InstanceId、ip |
| Contextlockwait               | 上下文锁等待               | -     | InstanceId、ip |
| Httpconnection                | HTTP 连接数                | 个    | InstanceId、ip |
| Mergestimemilliseconds        | merge 所消耗的时间（速率） | ms    | InstanceId、ip |
| Mysqlconnection               | mysql 方式的连接数         | 个    | InstanceId、ip |
| Querythread                   | 查询线程数                 | 个    | InstanceId、ip |
| Replicatedpartmerges          | 单位时间内的副本块合并个数 | 个/秒 | InstanceId、ip |
| Replicatedpartmutations       | 单位时间内的副本块修改数   | 个/秒 | InstanceId、ip |
| Tcpconnection                 | TCP 连接数                 | 个    | InstanceId、ip |
| Merge                         | 合并数                     | 个    | InstanceId、ip |
| Uptime                        | 启动时间                   | s     | InstanceId、ip |
| CkUp                          | 1-存活，0-失活             | -     | InstanceId、ip |
| Failedinsertquery             | 插入失败数                 | 个/秒 | InstanceId、ip |
| Failedselectquery             | 查询失败数                 | 个/秒 | InstanceId、ip |
| Query                         | 包含增删改查的 query 个数  | 个/秒 | InstanceId、ip |
| Insertquery                   | 单位时间的 insert 执行次数 | 次    | InstanceId、ip |

### ZK 指标

| 指标英文名                    | 指标中文名         | 单位  | 维度           |
| ----------------------------- | ------------------ | ----- | -------------- |
| NodeLoad1                     | 节点一分钟负载     | -     | InstanceId、ip |
| NodeLoad5                     | 5分钟负载          | -     | InstanceId、ip |
| NodeLoad15                    | 15分钟负载         | -     | InstanceId、ip |
| NodeNetworkReceiveBytesTotal  | 节点接收流量       | MB/s  | InstanceId、ip |
| DiskUsage                     | 数据盘使用率       | %     | InstanceId、ip |
| CpuUsage                      | CPU 使用率         | %     | InstanceId、ip |
| NodeNetworkTransmitBytesTotal | 节点流出流量       | MB/s  | InstanceId、ip |
| MemUsage                      | 内存使用率         | %     | InstanceId、ip |
| PacketsSent                   | 发包个数           | 个    | InstanceId、ip |
| ZkUp                          | zk 进程存活        | -     | InstanceId、ip |
| GlobalSessions                | 全局 session 个数  | 个    | InstanceId、ip |
| ConnectionRejected            | 拒绝链接个数       | 个    | InstanceId、ip |
| JvmMemoryPoolBytesUsed        | jvm 内存池使用     | MB    | InstanceId、ip |
| PacketsReceived               | 接收传输包的速率   | 个/秒 | InstanceId、ip |
| RequestCommitQueued           | 请求提交队列个数   | 个    | InstanceId、ip |
| PrepProcessorQueueTimeMs      | 预处理队列等待时间 | ms    | InstanceId、ip |
| WatchCount                    | zk_watch 个数      | 个    | InstanceId、ip |
| PrepProcessTime               | 预处理时间         | ms    | InstanceId、ip |

### 集群指标

| 指标英文名                       | 指标中文名   | 单位  | 维度       |
| -------------------------------- | ------------ | ----- | ---------- |
| SumCkUp                          | 集群节点数   | None  | InstanceId |
| SumCpuUsage                      | CPU 使用率   | %     | InstanceId |
| SumDiskUsage                     | 数据盘使用率 | %     | InstanceId |
| SumMemUsage                      | 内存使用率   | %     | InstanceId |
| SumNodeNetworkReceiveBytesTotal  | 节点接收流量 | MB    | InstanceId |
| SumNodeNetworkTransmitBytesTotal | 节点发送流量 | MB    | InstanceId |
| SumQuery                         | 总查询数     | None  | InstanceId |
| SumInsertquery                   | 插入数       | 个/秒 | InstanceId |
| SumFailedinsertquery             | 插入失败数   | 个/秒 | InstanceId |
| SumFailedselectquery             | 查询失败数   | 个/秒 | InstanceId |

## 各维度对应参数总览

| 参数名称                       | 维度名称   | 维度解释           | 格式                                  |
| :----------------------------- | :--------- | :----------------- | :------------------------------------ |
| Instances.N.Dimensions.0.Name  | InstanceId | 集群 ID 的维度名称 | 输入 String 类型维度名称：InstanceId  |
| Instances.N.Dimensions.0.Value | InstanceId | 具体集群 ID        | 输入具体集群 ID，例如：cdwch-89d5vlvd |
| Instances.N.Dimensions.1.Name  | ip         | 节点 ip 的维度名称 | 输入 String 类型维度名称：ip          |
| Instances.N.Dimensions.1.Value | ip         | 具体节点 ip        | 输入具体节点 ip，例如：10.0.0.0       |

## 入参说明

**查询节点指标和 ZK 指标监控数据，入参取值如下：**
&Namespace=QCE/CDWCH
&Instances.N.Dimensions.0.Name=InstanceId
&Instances.N.Dimensions.0.Value=具体集群 ID
&Instances.N.Dimensions.1.Name=ip
&Instances.N.Dimensions.1.Value=具体节点 ip

**查询集群指标监控数据，入参取值如下：**
&Namespace=QCE/CDWCH
&Instances.N.Dimensions.0.Name=InstanceId
&Instances.N.Dimensions.0.Value=具体集群 ID
