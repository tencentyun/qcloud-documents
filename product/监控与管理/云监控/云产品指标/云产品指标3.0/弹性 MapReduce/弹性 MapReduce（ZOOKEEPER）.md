## 命名空间

Namespace=QCE/TXMR_ZOOKEEPER

## 监控指标

| 指标英文名                                     | 指标中文名                                  | 指标单位              | 指标含义                                | 维度                                             |
| ---------------------------------------------- | ------------------------------------------- | --------------------- | --------------------------------------- | ------------------------------------------------ |
| ZkQmGcUtilGcCountYgc                           | GC 次数_YGC                                 | 次                    | Young GC 次数                           | id4zookeeperzookeeper<br>host4zookeeperzookeeper |
| ZkQmGcUtilGcCountFgc                           | GC 次数_FGC                                 | 次                    | Full GC 次数                            | id4zookeeperzookeeper<br>host4zookeeperzookeeper |
| ZkQmGcUtilGcTimeFgct                           | GC 时间_FGCT                                | s                     | Full GC 消耗时间                        | id4zookeeperzookeeper<br>host4zookeeperzookeeper |
| ZkQmGcUtilGcTimeGct                            | GC 时间_FGCT                                | s                     | 垃圾回收时间消耗                        | id4zookeeperzookeeper<br>host4zookeeperzookeeper |
| ZkQmGcUtilGcTimeYgct                           | GC 时间_YGCT                                | s                     | Young GC 消耗时间                       | id4zookeeperzookeeper<br>host4zookeeperzookeeper |
| ZkQmGcUtilMemoryS0                             | 内存区域占比_S0                             | %                     | Survivor 0区内存使用占比                | id4zookeeperzookeeper<br>host4zookeeperzookeeper |
| ZkQmGcUtilMemoryE                              | 内存区域占比_E                              | %                     | Eden 区内存使用占比                     | id4zookeeperzookeeper<br>host4zookeeperzookeeper |
| ZkQmGcUtilMemoryCcs                            | 内存区域占比_CCS                            | %                     | Compressed class space 区内存使用占比   | id4zookeeperzookeeper<br>host4zookeeperzookeeper |
| ZkQmGcUtilMemoryS1                             | 内存区域占比_S1                             | %                     | Survivor 1区内存使用占比                | id4zookeeperzookeeper<br>host4zookeeperzookeeper |
| ZkQmGcUtilMemoryO                              | 内存区域占比_O                              | %                     | Old 区内存使用占比                      | id4zookeeperzookeeper<br>host4zookeeperzookeeper |
| ZkQmGcUtilMemoryM                              | 内存区域占比_M                              | %                     | Metaspace 区内存使用占比                | id4zookeeperzookeeper<br>host4zookeeperzookeeper |
| ZkQmJvmMemMem<br>nonheapusedm                  | JVM 内存\_MemNonHeapUsedM                   | MB                    | JVM 当前已经使用的 NonHeapMemory 的数量 | id4zookeeperzookeeper<br>host4zookeeperzookeeper |
| ZkQmJvmMemMem<br>nonheapcommittedm             | JVM 内存\_MemNonHeapCommittedM              | MB                    | JVM 当前已经提交的 NonHeapMemory 的数量 | id4zookeeperzookeeper<br>host4zookeeperzookeeper |
| ZkQmJvmMemMem<br>heapusedm                     | JVM 内存\_MemHeapUsedM                      | MB                    | JVM 当前已经使用的 HeapMemory 的数量    | id4zookeeperzookeeper<br>host4zookeeperzookeeper |
| ZkQmJvmMemMem<br>heapcommittedm                | JVM 内存\_MemHeapCommittedM                 | MB                    | JVM 当前已经提交的 HeapMemory 的数量    | id4zookeeperzookeeper<br>host4zookeeperzookeeper |
| ZkQmJvmMem<br>Memheapmaxm                      | JVM 内存\_MemHeapMaxM                       | MB                    | JVM 配置的 HeapMemory 的数量            | id4zookeeperzookeeper<br>host4zookeeperzookeeper |
| ZkQmJvmMem<br>Memheapinitm                     | JVM 内存_MemHeapInitM                       | MB                    | JVM 初始 HeapMem 的数量                 | id4zookeeperzookeeper<br>host4zookeeperzookeeper |
| ZkQmJvmMemMem<br>nonheapinitm                  | JVM 内存_MemNonHeapInitM                    | MB                    | JVM 初始 NonHeapMem 的数量              | id4zookeeperzookeeper<br>host4zookeeperzookeeper |
| ZkQmOsCpuLoad<br>Processcpuload                | CPU 利用率_ProcessCpuLoad                   | %                     | CPU 利用率                              | id4zookeeperzookeeper<br>host4zookeeperzookeeper |
| ZkQmOsFdCountZk<br>MaxFileDescriptorCount      | 文件描述符数\_zk_max_file_descriptor_count  | 个                    | 最大文件描述符数                        | id4zookeeperzookeeper<br>host4zookeeperzookeeper |
| ZkQmOsFdCountZk<br>OpenFileDescriptorCount     | 文件描述符数\_zk_open_file_descriptor_count | 个                    | 已打开文件描述符数                      | id4zookeeperzookeeper<br>host4zookeeperzookeeper |
| ZkQmOsCpuTime<br>Processcputime                | CPU 累计使用时间\_ProcessCpuTime            | ms                    | CPU 累计使用时间                        | id4zookeeperzookeeper<br>host4zookeeperzookeeper |
| ZkQmRtUptimeUptime                             | 进程运行时长_Uptime                         | s                     | 进程运行时长                            | id4zookeeperzookeeper<br>host4zookeeperzookeeper |
| ZkQmThreadCount<br>Daemonthreadcount           | 工作线程数_DaemonThreadCount                | 个                    | Daemon 线程数                           | id4zookeeperzookeeper<br>host4zookeeperzookeeper |
| ZkQmThreadCount<br>Threadcount                 | 工作线程数_ThreadCount                      | 个                    | 总线程数                                | id4zookeeperzookeeper<br>host4zookeeperzookeeper |
| ZkConnectionsNumZk<br>NumAliveConnections      | 连接数\_zk_num_alive_connections            | 个                    | 当前连接数                              | id4zookeeperzookeeper<br>host4zookeeperzookeeper |
| ZkLatencyZkAvgLatency                          | 延迟\_zk_avg_latency                        | ms                    | zk 处理平均延迟                         | id4zookeeperzookeeper<br>host4zookeeperzookeeper |
| ZkLatencyZkMaxLatency                          | 延迟\_zk_max_latency                        | ms                    | zk 处理最大时延                         | id4zookeeperzookeeper<br>host4zookeeperzookeeper |
| ZkLatencyZkMinLatency                          | 延迟\_zk_min_latency                        | ms                    | zk 处理最小时延                         | id4zookeeperzookeeper<br>host4zookeeperzookeeper |
| ZkDataCount<br>ZkWatchCount                    | ZNODE 个数\_zk_watch_count                  | 个                    | zk 的 watch 数目                        | id4zookeeperzookeeper<br>host4zookeeperzookeeper |
| ZkDataCount<br>ZkZnodeCount                    | ZNODE 个数\_zk_znode_count                  | 个                    | zk 的 znode 数量                        | id4zookeeperzookeeper<br>host4zookeeperzookeeper |
| ZkDataCountZk<br>EphemeralsCount               | ZNODE个数\_zk_ephemerals_count              | 个                    | zk 的临时节点数目                       | id4zookeeperzookeeper<br>host4zookeeperzookeeper |
| ZkDataSizeZk<br>ApproximateDataSize            | 数据大小\_zk_approximate_data_size          | Byte                  | zk 存储数据量                           | id4zookeeperzookeeper<br>host4zookeeperzookeeper |
| ZkStateZkServerState                           | 节点状态\_zk_server_state                   | 1：主，0：备，2：单机 | zk 节点类型                             | id4zookeeperzookeeper<br>host4zookeeperzookeeper |
| ZkPacketsZk<br>PacketsReceived                 | 接收发送包量\_zk_packets_received           | 个/s                  | zk 接收的数据包速率                     | id4zookeeperzookeeper<br>host4zookeeperzookeeper |
| ZkPacketsZkPacketsSent                         | 接收发送包量\_zk_packets_sent               | 个/s                  | zk 发送的数据包速率                     | id4zookeeperzookeeper<br>host4zookeeperzookeeper |
| ZkRequestsOutstanding<br>ZkOutstandingRequests | 排队请求数\_zk_outstanding_requests         | 个                    | 排队请求数                              | id4zookeeperzookeeper<br>host4zookeeperzookeeper |

## 各维度对应参数总览

| 参数名称                       | 维度名称                | 维度解释                     | 格式                                                         |
| :----------------------------- | :---------------------- | :--------------------------- | :----------------------------------------------------------- |
| Instances.N.Dimensions.0.Name  | id4zookeeperzookeeper   | EMR 实例 ID 的维度名称       | 输入 String 类型维度名称：id4zookeeperzookeeper              |
| Instances.N.Dimensions.0.Value | id4zookeeperzookeeper   | EMR 实例具体 ID              | 输入 EMR 具体实例 ID，例如：emr-mm8bs222                     |
| Instances.N.Dimensions.1.Name  | host4zookeeperzookeeper | EMR 实例中节点 IP 的维度名称 | 输入 String 类型维度名称：host4zookeeperzookeeper            |
| Instances.N.Dimensions.1.Value | host4zookeeperzookeeper | EMR 实例中具体节点 IP        | 输入具体节点  IP ，可从控制台获取，登录 [腾讯云 MapReduce 控制台](https://console.cloud.tencent.com/emr) > 单击实例 > 集群资源 > 资源管理 > 节点内网 IP。也可通过 [查询节点信息](https://cloud.tencent.com/document/product/589/41707) API 获取。 |

## 入参说明

查询弹性 MapReduce（ZOOKEEPER）监控数据，入参取值如下：

Namespace=QCE/TXMR_ZOOKEEPER
&Instances.N.Dimensions.0.Name=id4zookeeperzookeepe
&Instances.N.Dimensions.0.Value=EMR 实例 ID 
&Instances.N.Dimensions.1.Name=host4zookeeperzookeeper
&Instances.N.Dimensions.1.Value=EMR 实例中具体节点 IP 

