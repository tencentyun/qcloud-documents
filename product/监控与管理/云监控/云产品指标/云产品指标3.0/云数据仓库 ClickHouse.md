## 命名空间

Namespace=QCE/CDWCH

## 监控指标

### 节点指标

| 指标英文名                    | 指标中文名                 | 单位  | 维度           |
| ----------------------------- | -------------------------- | ----- | -------------- |
| Zookeeperrequest              | zk 请求数                  | 个    | InstanceId、IP |
| Zookeepersession              | 当前 zk session 个数       | 个    | InstanceId、IP |
| Zookeeperwatch                | zkwatch 个数               | 个    | InstanceId、IP |
| Fileopen                      | 文件打开数                 | 个    | InstanceId、IP |
| NodeLoad1                     | 节点一分钟负载             | -     | InstanceId、IP |
| NodeLoad5                     | 5分钟负载                  | -     | InstanceId、IP |
| NodeLoad15                    | 15分钟负载                 | -     | InstanceId、IP |
| CpuLoadRate                   | CPU 负载比率               | %     | InstanceId、IP |
| DiskUsage                     | 数据盘使用率               | %     | InstanceId、IP |
| NodeNetworkReceiveBytesTotal  | 节点接收流量               | MB/s  | InstanceId、IP |
| NodeNetworkTransmitBytesTotal | 节点流出流量               | MB/s  | InstanceId、IP |
| MemUsage                      | 内存使用率                 | %     | InstanceId、IP |
| CpuUsage                      | CPU 使用率                 | %     | InstanceId、IP |
| CpuUsageAvg                   | CPU 平均使用率             | %     | InstanceId、IP |
| Contextlockwait               | 上下文锁等待               | -     | InstanceId、IP |
| Httpconnection                | HTTP 连接数                | 个    | InstanceId、IP |
| Mergestimemilliseconds        | merge 所消耗的时间（速率） | ms    | InstanceId、IP |
| Mysqlconnection               | mysql 方式的连接数         | 个    | InstanceId、IP |
| Querythread                   | 查询线程数                 | 个    | InstanceId、IP |
| Replicatedpartmerges          | 单位时间内的副本块合并个数 | 个/秒 | InstanceId、IP |
| Replicatedpartmutations       | 单位时间内的副本块修改数   | 个/秒 | InstanceId、IP |
| Tcpconnection                 | TCP 连接数                 | 个    | InstanceId、IP |
| Merge                         | 合并数                     | 个    | InstanceId、IP |
| Uptime                        | 启动时间                   | s     | InstanceId、IP |
| CkUp                          | 1-存活，0-失活             | -     | InstanceId、IP |
| Failedinsertquery             | 插入失败数                 | 个/秒 | InstanceId、IP |
| Failedselectquery             | 查询失败数                 | 个/秒 | InstanceId、IP |
| Query                         | 包含增删改查的 query 个数  | 个/秒 | InstanceId、IP |
| Insertquery                   | 单位时间的 insert 执行次数 | 次    | InstanceId、IP |

### ZK 指标

| 指标英文名                    | 指标中文名         | 单位  | 维度           |
| ----------------------------- | ------------------ | ----- | -------------- |
| NodeLoad1                     | 节点一分钟负载     | -     | InstanceId、IP |
| NodeLoad5                     | 5分钟负载          | -     | InstanceId、IP |
| NodeLoad15                    | 15分钟负载         | -     | InstanceId、IP |
| NodeNetworkReceiveBytesTotal  | 节点接收流量       | MB/s  | InstanceId、IP |
| DiskUsage                     | 数据盘使用率       | %     | InstanceId、IP |
| CpuUsage                      | CPU 使用率         | %     | InstanceId、IP |
| NodeNetworkTransmitBytesTotal | 节点流出流量       | MB/s  | InstanceId、IP |
| MemUsage                      | 内存使用率         | %     | InstanceId、IP |
| PacketsSent                   | 发包个数           | 个    | InstanceId、IP |
| ZkUp                          | zk 进程存活        | -     | InstanceId、IP |
| GlobalSessions                | 全局 session 个数  | 个    | InstanceId、IP |
| ConnectionRejected            | 拒绝链接个数       | 个    | InstanceId、IP |
| JvmMemoryPoolBytesUsed        | jvm 内存池使用     | MB    | InstanceId、IP |
| PacketsReceived               | 接收传输包的速率   | 个/秒 | InstanceId、IP|
| RequestCommitQueued           | 请求提交队列个数   | 个    | InstanceId、IP |
| PrepProcessorQueueTimeMs      | 预处理队列等待时间 | ms    | InstanceId、IP |
| WatchCount                    | zk_watch 个数      | 个    | InstanceId、IP |
| PrepProcessTime               | 预处理时间         | ms    | InstanceId、IP |

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
| Instances.N.Dimensions.1.Name  | IP         | 节点 IP 的维度名称 | 输入 String 类型维度名称：IP          |
| Instances.N.Dimensions.1.Value | IP         | 具体节点 IP        | 输入具体节点 IP，例如：10.0.0.0       |

## 入参说明

**查询节点指标和 ZK 指标监控数据，入参取值如下：**
&Namespace=QCE/CDWCH
&Instances.N.Dimensions.0.Name=InstanceId
&Instances.N.Dimensions.0.Value=具体集群 ID
&Instances.N.Dimensions.1.Name=IP
&Instances.N.Dimensions.1.Value=具体节点 IP

**查询集群指标监控数据，入参取值如下：**
&Namespace=QCE/CDWCH
&Instances.N.Dimensions.0.Name=InstanceId
&Instances.N.Dimensions.0.Value=具体集群 ID
