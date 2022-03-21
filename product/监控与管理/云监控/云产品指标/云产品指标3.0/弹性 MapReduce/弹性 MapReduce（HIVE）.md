## 命名空间

Namespace=QCE/TXMR_HIVE

## 监控指标

### HIVE-HiveMetaStore

| 指标英文名                                    | 指标中文名                           | 单位 | 指标含义                                | 维度                                     |
| --------------------------------------------- | ------------------------------------ | ---- | --------------------------------------- | ---------------------------------------- |
| HiveHmsGcUtilMemoryE                          | 内存区域占比_E                       | %    | Eden 区内存使用占比                     | id4hivemetastore、<br>host4hivemetastore |
| HiveHmsGcUtilGcCountFgc                       | GC次数_FGC                           | 次   | Full GC 次数                            | id4hivemetastore、<br>host4hivemetastore |
| HiveHmsGcUtilGcTimeYgct                       | GC时间_YGCT                          | s    | Young GC 次数                           | id4hivemetastore、<br>host4hivemetastore |
| HiveHmsGcUtilMemoryS1                         | 内存区域占比_S1                      | %    | Survivor 1区内存使用占比                | id4hivemetastore、<br>host4hivemetastore |
| HiveHmsGcUtilMemoryM                          | 内存区域占比_M                       | %    | Metaspace 区内存使用占比                | id4hivemetastore、<br>host4hivemetastore |
| HiveHmsGcUtilMemoryO                          | 内存区域占比_O                       | %    | Old 区内存使用占比                      | id4hivemetastore、<br>host4hivemetastore |
| HiveHmsGcUtilGcTimeGct                        | GC时间_GCT                           | s    | 垃圾回收时间消耗                        | id4hivemetastore、<br>host4hivemetastore |
| HiveHmsGcUtilGcCountYgc                       | GC次数_YGC                           | 次   | Young GC 次数                           | id4hivemetastore、<br>host4hivemetastore |
| HiveHmsGcUtilGcTimeFgct                       | GC时间_FGCT                          | s    | Full GC 消耗时间                        | id4hivemetastore、<br>host4hivemetastore |
| HiveHmsGcUtilMemoryS0                         | 内存区域占比_S0                      | %    | Survivor 0区内存使用占比                | id4hivemetastore、<br>host4hivemetastore |
| HiveHmsGcUtilMemoryCcs                        | 内存区域占比_CCS                     | %    | Compressed class space 区内存使用占比   | id4hivemetastore、<br>host4hivemetastore |
| HiveHmsJvmMemMem<br/>heapcommittedm           | JVM内存_MemHeapCommittedM            | MB   | JVM 已经提交的 HeapMemory 的数量        | id4hivemetastore、<br>host4hivemetastore |
| HiveHmsJvmMem<br/>Memheapinitm                | JVM内存_MemHeapInitM                 | MB   | JVM 初始 HeapMem 的数量                 | id4hivemetastore、<br>host4hivemetastore |
| HiveHmsJvmMem<br/>Memheapmaxm                 | JVM内存_MemHeapMaxM                  | MB   | JVM 配置的 HeapMemory 的数量            | id4hivemetastore、<br>host4hivemetastore |
| HiveHmsJvmMem<br/>Memheapusedm                | JVM内存_MemHeapUsedM                 | MB   | JVM 当前已经使用的 HeapMemory 的数量    | id4hivemetastore、<br>host4hivemetastore |
| HiveHmsJvmMem<br/>Memnonheapcommittedm        | JVM内存_MemNonHeapCommittedM         | MB   | JVM 当前已经使用的 NonHeapMemory 的数量 | id4hivemetastore、<br>host4hivemetastore |
| HiveHmsJvmMem<br/>Memnonheapinitm             | JVM内存_MemNonHeapInitM              | MB   | JVM 初始 NonHeapMem 的数量              | id4hivemetastore、<br>host4hivemetastore |
| HiveHmsJvmMem<br/>Memnonheapusedm             | JVM内存_MemNonHeapUsedM              | MB   | JVM 当前已使用NonHeapMem 的数量         | id4hivemetastore、<br>host4hivemetastore |
| HiveHmsJvmPause<br/>Extrasleeptime            | GC额外每秒睡眠时间_ExtraSleepTime    | ms   | GC 额外睡眠时间                         | id4hivemetastore、<br>host4hivemetastore |
| HiveHmsOpenConnections<br/>Numopenconnections | 进程打开连接数_NumOpenConnections    | 个   | 进程打开连接数                          | id4hivemetastore、<br>host4hivemetastore |
| HiveHmsOsCpuLoad<br/>Processcpuload           | CPU利用率_ProcessCpuLoad             | %    | 进程 CPU 利用率                         | id4hivemetastore、<br>host4hivemetastore |
| HiveHmsOsCpuLoad<br/>Systemcpuload            | CPU利用率_SystemCpuLoad              | %    | 系统 CPU 利用率                         | id4hivemetastore、<br>host4hivemetastore |
| HiveHmsOsCpuTime<br/>Processcputime           | CPU累计使用时间_ProcessCpuTime       | ms   | CPU累计使用时间                         | id4hivemetastore、<br>host4hivemetastore |
| HiveHmsRtUptimeUptime                         | 进程运行时长_Uptime                  | s    | 进程运行时长                            | id4hivemetastore、<br>host4hivemetastore |
| HiveHmsThreadCount<br/>Daemonthreadcount      | 工作线程数_DaemonThreadCount         | 个   | 守护线程数                              | id4hivemetastore、<br>host4hivemetastore |
| HiveHmsThreadCount<br/>Threadcount            | 工作线程数_ThreadCount               | 个   | 线程总数                                | id4hivemetastore、<br>host4hivemetastore |
| HiveHmsOsFdCount<br/>Maxfiledescriptorcount   | 文件描述符数_MaxFileDescriptorCount  | 个   | 最大文件描述符数                        | id4hivemetastore、<br>host4hivemetastore |
| HiveHmsOsFdCountOpen<br/>filedescriptorcount  | 文件描述符数_OpenFileDescriptorCount | 个   | 已打开文件描述符数量                    | id4hivemetastore、<br>host4hivemetastore |
| HiveHmsOsCpuUsedCpurate                       | 每秒CPU使用时间_CPURATE              | s    | 每秒CPU使用时间                         | id4hivemetastore、<br>host4hivemetastore |



### HIVE-HiveServer2

| frontMetricNameV3                            |                                      | frontMetricUnit | 指标含义                                | 维度                                         |
| -------------------------------------------- | ------------------------------------ | --------------- | --------------------------------------- | -------------------------------------------- |
| HiveH2ThreadCountThreadcount                 | 工作线程数_ThreadCount               | 个              | 总线程数                                | host4hivehiveserver2、<br>id4hivehiveserver2 |
| HiveH2ThreadCount<br/>Daemonthreadcount      | 工作线程数_DaemonThreadCount         | 个              | Daemon  线程数                          | host4hivehiveserver2、<br>id4hivehiveserver2 |
| HiveH2RtUptimeUptime                         | 进程运行时长_Uptime                  | s               | 进程运行时长                            | host4hivehiveserver2、<br>id4hivehiveserver2 |
| HiveH2OsFdCountOpen<br/>filedescriptorcount  | 文件描述符数_OpenFileDescriptorCount | 个              | 已打开文件描述符数                      | host4hivehiveserver2、<br>id4hivehiveserver2 |
| HiveH2OsFdCountMax<br/>filedescriptorcount   | 文件描述符数_MaxFileDescriptorCount  | 个              | 最大文件描述符数                        | host4hivehiveserver2、<br>id4hivehiveserver2 |
| HiveH2OsCpuUsedCpurate                       | 每秒CPU使用时间_CPURate              | s               | 每秒CPU使用时间                         | host4hivehiveserver2、<br>id4hivehiveserver2 |
| HiveH2OsCpuTime<br/>Processcputime           | CPU累计使用时间_ProcessCpuTime       | ms              | CPU累计使用时间                         | host4hivehiveserver2、<br>id4hivehiveserver2 |
| HiveH2OsCpuLoad<br/>Processcpuload           | CPU利用率_ProcessCpuLoad             | %               | CPU利用率                               | host4hivehiveserver2、<br>id4hivehiveserver2 |
| HiveH2OpenConnections<br>Numopenconnections  | 进程打开连接数_NumOpenConnections    | 个              | 进程打开连接数                          | host4hivehiveserver2、<br>id4hivehiveserver2 |
| HiveH2JvmPause<br/>Extrasleeptime            | GC额外每秒睡眠时间_ExtraSleepTime    | ms              | GC额外每秒睡眠时间                      | host4hivehiveserver2、<br>id4hivehiveserver2 |
| HiveH2JvmMemStatUsed<br>RatioMemheapusedrate | JVM堆内存使用率_MemHeapUsedRate      | %               |                                         | host4hivehiveserver2、<br>id4hivehiveserver2 |
| HiveH2JvmMem<br/>Memnonheapusedm             | JVM内存_MemNonHeapUsedM              | MB              | JVM 当前已经使用的 NonHeapMemory 的数量 | host4hivehiveserver2、<br>id4hivehiveserver2 |
| HiveH2JvmMem<br/>Memnonheapinitm             | JVM内存_MemNonHeapInitM              | MB              | JVM 初始 NonHeapMem 的数量              | host4hivehiveserver2、<br>id4hivehiveserver2 |
| HiveH2JvmMemMemnon<br/>heapcommittedm        | JVM内存_MemNonHeapCommittedM         | MB              | JVM 当前已经提交的 NonHeapMemory 的数量 | host4hivehiveserver2、<br>id4hivehiveserver2 |
| HiveH2JvmMem<br/>Memheapusedm                | JVM内存_MemHeapUsedM                 | MB              | JVM 当前已经使用的 HeapMemory 的数量    | host4hivehiveserver2、<br>id4hivehiveserver2 |
| HiveH2JvmMem<br/>Memheapmaxm                 | JVM内存_MemHeapMaxM                  | MB              | JVM 配置的 HeapMemory 的数量            | host4hivehiveserver2、<br>id4hivehiveserver2 |
| HiveH2JvmMem<br/>Memheapinitm                | JVM内存_MemHeapInitM                 | MB              | JVM 初始 HeapMem 的数量                 | host4hivehiveserver2、<br>id4hivehiveserver2 |
| HiveH2JvmMemMem<br/>heapcommittedm           | JVM内存_MemHeapCommittedM            | MB              | JVM 当前已经提交的 HeapMemory 的数量    | host4hivehiveserver2、<br>id4hivehiveserver2 |
| HiveH2GcUtilMemoryS1                         | 内存区域占比_S1                      | %               | Survivor 1区内存使用占比                | host4hivehiveserver2、<br>id4hivehiveserver2 |
| HiveH2GcUtilMemoryS0                         | 内存区域占比_S0                      | %               | Survivor 0区内存使用占比                | host4hivehiveserver2、<br>id4hivehiveserver2 |
| HiveH2GcUtilMemoryO                          | 内存区域占比_O                       | %               | Old 区内存使用占比                      | host4hivehiveserver2、<br>id4hivehiveserver2 |
| HiveH2GcUtilMemoryM                          | 内存区域占比_M                       | %               | Metaspace 区内存使用占比                | host4hivehiveserver2、<br>id4hivehiveserver2 |
| HiveH2GcUtilMemoryE                          | 内存区域占比_E                       | %               | Eden 区内存使用占比                     | host4hivehiveserver2、<br>id4hivehiveserver2 |
| HiveH2GcUtilMemoryCcs                        | 内存区域占比_CCS                     | %               | Compressed class space 区内存使用占比   | host4hivehiveserver2、<br>id4hivehiveserver2 |
| HiveH2GcUtilGcTimeYgct                       | GC时间_YGCT                          | s               | Young GC 消耗时间                       | host4hivehiveserver2、<br>id4hivehiveserver2 |
| HiveH2GcUtilGcTimeGct                        | GC时间_GCT                           | s               | 垃圾回收时间消耗                        | host4hivehiveserver2、<br>id4hivehiveserver2 |
| HiveH2GcUtilGcTimeFgct                       | GC时间_FGCT                          | s               | Full GC 消耗时间                        | host4hivehiveserver2、<br>id4hivehiveserver2 |
| HiveH2GcUtilGcCountYgc                       | GC次数_YGC                           | 次              | Young GC 次数                           | host4hivehiveserver2、<br>id4hivehiveserver2 |
| HiveH2GcUtilGcCountFgc                       | GC次数_FGC                           | 次              | Full GC 次数                            | host4hivehiveserver2、<br>id4hivehiveserver2 |
| HiveH2ExecAsync<br/>QueueSizeQueuesize       | hs2异步操作队列大小_QueueSize        | 个              | hs2 异步操作队列当前大小                | host4hivehiveserver2、<br>id4hivehiveserver2 |
| HiveH2ExecAsync<br/>PoolSizePoolsize         | hs2异步线程池大小_PoolSize           | 个              | hs2异步线程池当前大小                   | host4hivehiveserver2、<br>id4hivehiveserver2 |
| HiveH2Completed<br/>OperationFinished        | 完成的操作数量_Finished              | 个/秒           | 完成的操作数量                          | host4hivehiveserver2、<br>id4hivehiveserver2 |
| HiveH2Completed<br/>OperationError           | 出错的操作数量_Error                 | 个/秒           | 出错的操作数量                          | host4hivehiveserver2、<br>id4hivehiveserver2 |
| HiveH2Completed<br/>OperationClosed          | 关闭的操作数量_Closed                | 个/秒           | 关闭的操作数量                          | host4hivehiveserver2、<br>id4hivehiveserver2 |
| HiveH2Completed<br/>OperationCanceled        | 取消的操作数量_Canceled              | 个/秒           | 取消的操作数量                          | host4hivehiveserver2、<br>id4hivehiveserver2 |
| HiveH2ApiDriverRunAvg                        | Driver执行时延_Avg                   | ms              | Driver 执行平均执行时延                 | host4hivehiveserver2、<br>id4hivehiveserver2 |
| HiveH2ApiDriver<br/>Run99thPercentile        | Driver执行时延_99th_percentile       | ms              | Driver 执行99%的时延                    | host4hivehiveserver2、<br>id4hivehiveserver2 |

### HIVE-HiveWebHcat

| 指标英文名             | 指标名称 | 指标中文名       | 指标单位 | 指标含义                              | 维度                                          |
| ---------------------- | -------- | ---------------- | -------- | ------------------------------------- | --------------------------------------------- |
| HiveHcGcUtilGcCountYgc | YGC      | GC 次数\_YGC     | 次       | Young GC 次数                         | host4hivehivewebhcat、<br>id4hivehivewebhcat  |
| HiveHcGcUtilGcCountFgc | FGC      | GC 次数_FGC      | 次       | Full GC 次数                          | host4hivehivewebhcat、<br>id4hivehivewebhcat  |
| HiveHcGcUtilGcTimeFgct | FGCT     | GC 时间_FGCT     | s        | Full GC 消耗时间                      | host4hivehivewebhcat、<br>id4hivehivewebhcat  |
| HiveHcGcUtilGcTimeGct  | GCT      | GC 时间_FGCT     | s        | 垃圾回收时间消耗                      | host4hivehivewebhcat、<br/>id4hivehivewebhca  |
| HiveHcGcUtilGcTimeYgct | YGCT     | GC 时间_YGCT     | s        | Young GC 消耗时间                     | host4hivehivewebhcat、<br/>id4hivehivewebhca  |
| HiveHcGcUtilMemoryS0   | S0       | 内存区域占比_S0  | %        | Survivor 0 区内存使用占比             | host4hivehivewebhcat、<br/>id4hivehivewebhca  |
| HiveHcGcUtilMemoryE    | E        | 内存区域占比_E   | %        | Eden 区内存使用占比                   | host4hivehivewebhcat、<br/>id4hivehivewebhca  |
| HiveHcGcUtilMemoryCcs  | CCS      | 内存区域占比_CCS | %        | Compressed class space 区内存使用占比 | host4hivehivewebhcat、<br/>id4hivehivewebhca  |
| HiveHcGcUtilMemoryS1   | S1       | 内存区域占比_S1  | %        | Survivor 1 区内存使用占比             | host4hivehivewebhcat、<br/>id4hivehivewebhca  |
| HiveHcGcUtilMemoryO    | O        | 内存区域占比_O   | %        | Old 区内存使用占比                    | host4hivehivewebhcat、<br/>id4hivehivewebhcat |
| HiveHcGcUtilMemoryM    | M        | 内存区域占比_M   | %        | Metaspace 区内存使用占比              | host4hivehivewebhcat、<br/>id4hivehivewebhcat |

## 各维度对应参数总览

| 参数名称                       | 维度名称             | 维度解释                     | 格式                                                         |
| :----------------------------- | :------------------- | :--------------------------- | :----------------------------------------------------------- |
| Instances.N.Dimensions.0.Name  | id4hivemetastore     | EMR 实例 ID 的维度名称       | 输入 String 类型维度名称：id4hivemetastore                   |
| Instances.N.Dimensions.0.Value | id4hivemetastore     | EMR 实例具体 ID              | 输入 EMR 具体实例 ID，例如 ：emr-mm8bs222                    |
| Instances.N.Dimensions.1.Name  | host4hivemetastore   | EMR 实例中节点 IP 的维度名称 | 输入String 类型维度名称：host4hivemetastore                  |
| Instances.N.Dimensions.1.Value | host4hivemetastore   | EMR 实例中具体节点 IP        | 输入具体节点  IP ，可从控制台获取，登录 [腾讯云 MapReduce 控制台](https://console.cloud.tencent.com/emr) > 单击实例 > 集群资源 > 资源管理 > 节点内网 IP。也可通过 [查询节点信息](https://cloud.tencent.com/document/product/589/41707) API 获取。 |
| Instances.N.Dimensions.0.Name  | id4hivehiveserver2   | EMR 实例 ID 的维度名称       | 输入 String 类型维度名称：id4hivehiveserver2                 |
| Instances.N.Dimensions.0.Value | id4hivehiveserver2   | EMR 实例具体 ID              | 输入 EMR 具体实例 ID，例如 ：emr-mm8bs222                    |
| Instances.N.Dimensions.1.Name  | host4hivehiveserver2 | EMR 实例中节点 IP 的维度名称 | 输入String 类型维度名称：host4hivehiveserver2                |
| Instances.N.Dimensions.1.Value | host4hivehiveserver2 | EMR 实例中具体节点 IP        | 输入具体节点  IP ，可从控制台获取，登录 [腾讯云 MapReduce 控制台](https://console.cloud.tencent.com/emr) > 单击实例 > 集群资源 > 资源管理 > 节点内网 IP。也可通过 [查询节点信息](https://cloud.tencent.com/document/product/589/41707) API 获取。 |
| Instances.N.Dimensions.0.Name  | id4hivehivewebhcat   | EMR 实例 ID 的维度名称       | 输入 String 类型维度名称：id4hivehivewebhcat                 |
| Instances.N.Dimensions.0.Value | id4hivehivewebhcat   | EMR 实例具体 ID              | 输入 EMR 具体实例 ID，例如 ：emr-mm8bs222                    |
| Instances.N.Dimensions.1.Name  | host4hivehivewebhcat | EMR 实例中节点 IP 的维度名称 | 输入String 类型维度名称：host4hivehivewebhcat                |
| Instances.N.Dimensions.1.Value | host4hivehivewebhcat | EMR 实例中具体节点 IP        | 输入具体节点  IP ，可从控制台获取，登录 [腾讯云 MapReduce 控制台](https://console.cloud.tencent.com/emr) > 单击实例 > 集群资源 > 资源管理 > 节点内网 IP。也可通过 [查询节点信息](https://cloud.tencent.com/document/product/589/41707) API 获取。 |

## 入参说明

弹性 MapReduce（HIVE）支持以下三种维度组合的查询方式，三种入参取值如下： 

**1. 查询  HIVE-HiveMetaStore  的指标监控数据，入参取值如下：**
&Namespace=QCE/TXMR_HIVE
&Instances.N.Dimensions.0.Name=id4hivemetastore
&Instances.N.Dimensions.0.Value=EMR 实例 ID 
&Instances.N.Dimensions.1.Name=host4hivemetastore
&Instances.N.Dimensions.1.Value=EMR 实例中具体节点 IP 

**2. 查询 HIVE-HiveServer2  的指标监控数据，入参取值如下：**
&Namespace=QCE/TXMR_HIVE
&Instances.N.Dimensions.0.Name=id4hivehiveserver2
&Instances.N.Dimensions.0.Value=EMR 实例 ID
&Instances.N.Dimensions.1.Name=host4hivehiveserver2
&Instances.N.Dimensions.1.Value=EMR 实例中具体节点IP 

**3. 查询  HIVE-HiveWebHcat 的指标监控数据，入参取值如下：**
&Namespace=QCE/TXMR_HIVE
&Instances.N.Dimensions.0.Name=id4hivehivewebhcat
&Instances.N.Dimensions.0.Value=EMR 实例 ID
&Instances.N.Dimensions.1.Name=host4hivehivewebhcat
&Instances.N.Dimensions.1.Value=EMR实例中具体节点 IP 
