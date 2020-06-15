## 命名空间

Namespace=QCE/TXMR_ZOOKEEPER

## 监控指标

| 指标英文名                                     | 指标中文名                                 | 指标单位              | 指标含义                                | 维度                                             |
| ---------------------------------------------- | ------------------------------------------ | --------------------- | --------------------------------------- | ------------------------------------------------ |
| ZkQmGcUtilGcCountYgc                           | GC次数_YGC                                 | 次                    | Young GC 次数                           | id4zookeeperzookeeper<br>host4zookeeperzookeeper |
| ZkQmGcUtilGcCountFgc                           | GC次数_FGC                                 | 次                    | Full GC 次数                            | id4zookeeperzookeeper<br>host4zookeeperzookeeper |
| ZkQmGcUtilGcTimeFgct                           | GC时间_FGCT                                | s                     | Full GC 消耗时间                        | id4zookeeperzookeeper<br>host4zookeeperzookeeper |
| ZkQmGcUtilGcTimeGct                            | GC时间_FGCT                                | s                     | 垃圾回收时间消耗                        | id4zookeeperzookeeper<br>host4zookeeperzookeeper |
| ZkQmGcUtilGcTimeYgct                           | GC时间_YGCT                                | s                     | Young GC 消耗时间                       | id4zookeeperzookeeper<br>host4zookeeperzookeeper |
| ZkQmGcUtilMemoryS0                             | 内存区域占比_S0                            | %                     | Survivor 0区内存使用占比                | id4zookeeperzookeeper<br>host4zookeeperzookeeper |
| ZkQmGcUtilMemoryE                              | 连接数_zk_num_alive_connections            | %                     | Eden 区内存使用占比                     | id4zookeeperzookeeper<br>host4zookeeperzookeeper |
| ZkQmGcUtilMemoryCcs                            | 内存区域占比_CCS                           | %                     | Compressed class space 区内存使用占比   | id4zookeeperzookeeper<br>host4zookeeperzookeeper |
| ZkQmGcUtilMemoryS1                             | 内存区域占比_S1                            | %                     | Survivor 1区内存使用占比                | id4zookeeperzookeeper<br>host4zookeeperzookeeper |
| ZkQmGcUtilMemoryO                              | 连接数_zk_num_alive_connections            | %                     | Old 区内存使用占比                      | id4zookeeperzookeeper<br>host4zookeeperzookeeper |
| ZkQmGcUtilMemoryM                              | 连接数_zk_num_alive_connections            | %                     | Metaspace 区内存使用占比                | id4zookeeperzookeeper<br>host4zookeeperzookeeper |
| ZkQmJvmMemMem<br>nonheapusedm                  | JVM内存_MemNonHeapUsedM                    | MB                    | JVM 当前已经使用的 NonHeapMemory 的数量 | id4zookeeperzookeeper<br>host4zookeeperzookeeper |
| ZkQmJvmMemMem<br>nonheapcommittedm             | JVM内存_MemNonHeapCommittedM               | MB                    | JVM 当前已经提交的 NonHeapMemory 的数量 | id4zookeeperzookeeper<br>host4zookeeperzookeeper |
| ZkQmJvmMemMem<br>heapusedm                     | JVM内存_MemHeapUsedM                       | MB                    | JVM 当前已经使用的 HeapMemory 的数量    | id4zookeeperzookeeper<br>host4zookeeperzookeeper |
| ZkQmJvmMemMem<br>heapcommittedm                | JVM内存_MemHeapCommittedM                  | MB                    | JVM 当前已经提交的 HeapMemory 的数量    | id4zookeeperzookeeper<br>host4zookeeperzookeeper |
| ZkQmJvmMem<br>Memheapmaxm                      | JVM内存_MemHeapMaxM                        | MB                    | JVM 配置的 HeapMemory 的数量            | id4zookeeperzookeeper<br>host4zookeeperzookeeper |
| ZkQmJvmMem<br>Memheapinitm                     | JVM内存_MemHeapInitM                       | MB                    | JVM 初始 HeapMem 的数量                 | id4zookeeperzookeeper<br>host4zookeeperzookeeper |
| ZkQmJvmMemMem<br>nonheapinitm                  | JVM内存_MemNonHeapInitM                    | MB                    | JVM 初始 NonHeapMem 的数量              | id4zookeeperzookeeper<br>host4zookeeperzookeeper |
| ZkQmOsCpuLoad<br>Processcpuload                | CPU利用率_ProcessCpuLoad                   | %                     | CPU 利用率                              | id4zookeeperzookeeper<br>host4zookeeperzookeeper |
| ZkQmOsFdCountZk<br>MaxFileDescriptorCount      | 文件描述符数_zk_max_file_descriptor_count  | 个                    | 最大文件描述符数                        | id4zookeeperzookeeper<br>host4zookeeperzookeeper |
| ZkQmOsFdCountZk<br>OpenFileDescriptorCount     | 文件描述符数_zk_open_file_descriptor_count | 个                    | 已打开文件描述符数                      | id4zookeeperzookeeper<br>host4zookeeperzookeeper |
| ZkQmOsCpuTime<br>Processcputime                | CPU累计使用时间_ProcessCpuTime             | ms                    | CPU 累计使用时间                        | id4zookeeperzookeeper<br>host4zookeeperzookeeper |
| ZkQmRtUptimeUptime                             | 进程运行时长_Uptime                        | s                     | 进程运行时长                            | id4zookeeperzookeeper<br>host4zookeeperzookeeper |
| ZkQmThreadCount<br>Daemonthreadcount           | 工作线程数_DaemonThreadCount               | 个                    | Daemon 线程数                           | id4zookeeperzookeeper<br>host4zookeeperzookeeper |
| ZkQmThreadCount<br>Threadcount                 | 工作线程数_ThreadCount                     | 个                    | 总线程数                                | id4zookeeperzookeeper<br>host4zookeeperzookeeper |
| ZkConnectionsNumZk<br>NumAliveConnections      | 连接数_zk_num_alive_connections            | 个                    | 当前连接数                              | id4zookeeperzookeeper<br>host4zookeeperzookeeper |
| ZkLatencyZkAvgLatency                          | 延迟_zk_avg_latency                        | ms                    | zk 处理平均延迟                         | id4zookeeperzookeeper<br>host4zookeeperzookeeper |
| ZkLatencyZkMaxLatency                          | 延迟_zk_max_latency                        | ms                    | zk 处理最大时延                         | id4zookeeperzookeeper<br>host4zookeeperzookeeper |
| ZkLatencyZkMinLatency                          | 延迟_zk_min_latency                        | ms                    | zk 处理最小时延                         | id4zookeeperzookeeper<br>host4zookeeperzookeeper |
| ZkDataCount<br>ZkWatchCount                    | ZNODE个数_zk_watch_count                   | 个                    | zk 的 watch 数目                        | id4zookeeperzookeeper<br>host4zookeeperzookeeper |
| ZkDataCount<br>ZkZnodeCount                    | ZNODE个数_zk_znode_count                   | 个                    | zk 的 znode 数量                        | id4zookeeperzookeeper<br>host4zookeeperzookeeper |
| ZkDataCountZk<br>EphemeralsCount               | ZNODE个数_zk_ephemerals_count              | 个                    | zk 的临时节点数目                       | id4zookeeperzookeeper<br>host4zookeeperzookeeper |
| ZkDataSizeZk<br>ApproximateDataSize            | 数据大小_zk_approximate_data_size          | Byte                  | zk 存储数据量                           | id4zookeeperzookeeper<br>host4zookeeperzookeeper |
| ZkStateZkServerState                           | 节点状态_zk_server_state                   | 1：主，0：备，2：单机 | zk 节点类型                             | id4zookeeperzookeeper<br>host4zookeeperzookeeper |
| ZkPacketsZk<br>PacketsReceived                 | 接收发送包量_zk_packets_received           | 个/s                  | zk 接收的数据包速率                     | id4zookeeperzookeeper<br>host4zookeeperzookeeper |
| ZkPacketsZkPacketsSent                         | 接收发送包量_zk_packets_sent               | 个/s                  | zk 发送的数据包速率                     | id4zookeeperzookeeper<br>host4zookeeperzookeeper |
| ZkRequestsOutstanding<br>ZkOutstandingRequests | 排队请求数_zk_outstanding_requests         | 个                    | 排队请求数                              | id4zookeeperzookeeper<br>host4zookeeperzookeeper |

## 各维度对应参数总览

| 参数名称                       | 维度名称                | 维度解释                     | 格式                                             |
| :----------------------------- | :---------------------- | :--------------------------- | :----------------------------------------------- |
| Instances.N.Dimensions.0.Name  | id4zookeeperzookeeper   | EMR 实例 ID 的维度名称       | 输入 String 类型维度名称：id4zookeeperzookeeper  |
| Instances.N.Dimensions.0.Value | id4zookeeperzookeeper   | EMR 实例具体 ID              | 输入 EMR 具体实例 ID，例如 ：emr-mm8bs222        |
| Instances.N.Dimensions.1.Name  | host4zookeeperzookeeper | EMR 实例中节点 IP 的维度名称 | 输入String 类型维度名称：host4zookeeperzookeeper |
| Instances.N.Dimensions.1.Value | host4zookeeperzookeeper | EMR 实例中具体节点 IP        | 输入具体节点 IP ，例如：1.1.1.1                  |

## 入参说明

查询弹性 MapReduce（ZOOKEEPER）监控数据，入参取值如下：

Namespace=QCE/TXMR_ZOOKEEPER<br>
&Instances.N.Dimensions.0.Name=id4zookeeperzookeeper<br>
&Instances.N.Dimensions.0.Value为 EMR 实例ID <br>
&Instances.N.Dimensions.1.Name=host4zookeeperzookeeper<br>
&Instances.N.Dimensions.1.Value EMR实例中具体节点IP <br>
