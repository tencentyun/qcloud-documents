## 命名空间

Namespace=QCE/TXMR_TRINO



## 监控指标

### TRINO-概览

| 指标英文名                             | 指标中文名                                   | 指标含义           | 单位            | 维度             |
| -------------------------------------- | -------------------------------------------- | ------------------ | --------------- | ---------------- |
| TrinoMNodesActive                      | 节点数量_Active                              | 活跃节点数量       | 次数总和(Count) | id4trinooverview |
| TrinoMNodesTotal                       | 节点数量_Total                               | 总节点数量         | 次数总和(Count) | id4trinooverview |
| TrinoMNodesFailed                      | 节点数量_Failed                              | 失败节点数量       | 次数总和(Count) | id4trinooverview |
| TrinoMQueriesRunningqueries            | 查询_RunningQueries                          | 正在运行的查询总数 | 次数总和(Count) | id4trinooverview |
| TrinoMQueriesQueuedqueries             | 查询_QueuedQueries                           | 等待状态的查询总数 | 次数总和(Count) | id4trinooverview |
| TrinoMQueriesOneMinuteFailedqueries    | 查询频度_FailedQueries                       | 失败的查询总数     | 次数总和(Count) | id4trinooverview |
| TrinoMQueriesOneMinuteAbandonedqueries | 查询频度_AbandonedQueries                    | 放弃的查询总数     | 次数总和(Count) | id4trinooverview |
| TrinoMQueriesOneMinuteCanceledqueries  | 查询频度_CanceledQueries                     | 取消的查询总数     | 次数总和(Count) | id4trinooverview |
| TrinoMQueriesOneMinuteCompletedqueries | 查询频度_CompletedQueries                    | 完成的查询总数     | 次数总和(Count) | id4trinooverview |
| TrinoMQueriesOneMinuteStartedqueries   | 查询频度_StartedQueries                      | 已启动的查询总数   | 次数总和(Count) | id4trinooverview |
| TrinoMDataRateInputdatasizeoneminute   | 每分钟数据输入输出量_InputDataSizeOneMinute  | 输入数据速率       | GB              | id4trinooverview |
| TrinoMDataRateOutputdatasizeoneminute  | 每分钟数据输出输出量_OutputDataSizeOneMinute | 输出数据速率       | GB              | id4trinooverview |



###  TRINO-WORKER

| 指标英文名                             | 指标中文名                               | 指标含义                                | 单位            | 维度                                       |
| -------------------------------------- | ---------------------------------------- | --------------------------------------- | --------------- | ------------------------------------------ |
| TrinoWDataRateInputdatasizeoneminute   | 数据输入输出速率_InputDataSizeOneMinute  | 输入数据速率                            | GBytes          | host4trinotrinoworker、id4trinotrinoworker |
| TrinoWDataRateOutputdatasizeoneminute  | 数据输入输出速率_OutputDataSizeOneMinute | 输出数据速率                            | GBytes          | host4trinotrinoworker、id4trinotrinoworker |
| TrinoWGcUtilGcCountFgc                 | GC次数_FGC                               | Full GC 次数                            | 次数总和(Count) | host4trinotrinoworker、id4trinotrinoworker |
| TrinoWGcUtilGcCountYgc                 | GC次数_YGC                               | Young GC 次数                           | 次数总和(Count) | host4trinotrinoworker、id4trinotrinoworker |
| TrinoWGcUtilGcTimeFgct                 | GC时间_FGCT                              | Full GC 消耗时间                        | 秒(s)           | host4trinotrinoworker、id4trinotrinoworker |
| TrinoWGcUtilGcTimeGct                  | GC时间_GCT                               | 垃圾回收时间消耗                        | 秒(s)           | host4trinotrinoworker、id4trinotrinoworker |
| TrinoWGcUtilGcTimeYgct                 | GC时间_YGCT                              | Young GC 消耗时间                       | 秒(s)           | host4trinotrinoworker、id4trinotrinoworker |
| TrinoWGcUtilMemoryCcs                  | 内存区域占比_CCS                         | Compressed class space 区内存使用占比   | %               | host4trinotrinoworker、id4trinotrinoworker |
| TrinoWGcUtilMemoryE                    | 内存区域占比_E                           | Eden 区内存使用占比                     | %               | host4trinotrinoworker、id4trinotrinoworker |
| TrinoWGcUtilMemoryM                    | 内存区域占比_M                           | Metaspace 区内存使用占比                | %               | host4trinotrinoworker、id4trinotrinoworker |
| TrinoWGcUtilMemoryO                    | 内存区域占比_O                           | Old 区内存使用占比                      | %               | host4trinotrinoworker、id4trinotrinoworker |
| TrinoWGcUtilMemoryS0                   | 内存区域占比_S0                          | Survivor 0区内存使用占比                | %               | host4trinotrinoworker、id4trinotrinoworker |
| TrinoWGcUtilMemoryS1                   | 内存区域占比_S1                          | Survivor 1区内存使用占比                | %               | host4trinotrinoworker、id4trinotrinoworker |
| TrinoWJvmMemMemheapcommittedm          | JVM内存_MemHeapCommittedM                | JVM 已经提交的 HeapMemory 的数量        | MBytes          | host4trinotrinoworker、id4trinotrinoworker |
| TrinoWJvmMemMemheapinitm               | JVM内存_MemHeapInitM                     | JVM 初始 HeapMem 的数量                 | MBytes          | host4trinotrinoworker、id4trinotrinoworker |
| TrinoWJvmMemMemheapmaxm                | JVM内存_MemHeapMaxM                      | JVM 配置的 HeapMemory 的数量            | MBytes          | host4trinotrinoworker、id4trinotrinoworker |
| TrinoWJvmMemMemheapusedm               | JVM内存_MemHeapUsedM                     | JVM 当前已经使用的 HeapMemory 的数量    | MBytes          | host4trinotrinoworker、id4trinotrinoworker |
| TrinoWJvmMemMemnonheapcommittedm       | JVM内存_MemNonHeapCommittedM             | JVM 当前已经提交的 NonHeapMemory 的数量 | MBytes          | host4trinotrinoworker、id4trinotrinoworker |
| TrinoWJvmMemMemnonheapinitm            | JVM内存_MemNonHeapInitM                  | JVM 初始 NonHeapMem 的数量              | MBytes          | host4trinotrinoworker、id4trinotrinoworker |
| TrinoWJvmMemMemnonheapusedm            | JVM内存_MemNonHeapUsedM                  | JVM 当前已经使用的 NonHeapMemory 的数量 | MBytes          | host4trinotrinoworker、id4trinotrinoworker |
| TrinoWOsFdCountMaxfiledescriptorcount  | 文件描述符数_MaxFileDescriptorCount      | 最大文件描述符数                        | 次数总和(Count) | host4trinotrinoworker、id4trinotrinoworker |
| TrinoWOsFdCountOpenfiledescriptorcount | 文件描述符数_OpenFileDescriptorCount     | 已打开文件描述符数量                    | 次数总和(Count) | host4trinotrinoworker、id4trinotrinoworker |
| TrinoWRtUptimeUptime                   | 进程运行时间_Uptime                      | 进程运行时间                            | 秒(s)           | host4trinotrinoworker、id4trinotrinoworker |
| TrinoWThreadCountDaemonthreadcount     | 线程数量_DaemonThreadCount               | Daemon 线程数量                         | 次数总和(Count) | host4trinotrinoworker、id4trinotrinoworker |
| TrinoWThreadCountPeakthreadcount       | 线程数量_PeakThreadCount                 | 峰值线程数                              | 次数总和(Count) | host4trinotrinoworker、id4trinotrinoworker |
| TrinoWThreadCountThreadcount           | 线程数量_ThreadCount                     | 总线程数量                              | 次数总和(Count) | host4trinotrinoworker、Id4trinotrinoworker |

### TRINO-Coordinator

| 指标英文名                             | 指标中文名                           | 指标含义                                | 单位            | 维度                                                 |
| -------------------------------------- | ------------------------------------ | --------------------------------------- | --------------- | ---------------------------------------------------- |
| TrinoMGcUtilGcCountFgc                 | GC次数_FGC                           | Full GC 次数                            | 次数总和(Count) | host4trinotrinocoordinator、id4trinotrinocoordinator |
| TrinoMGcUtilGcCountYgc                 | GC次数_YGC                           | Young GC 次数                           | 次数总和(Count) | host4trinotrinocoordinator、id4trinotrinocoordinator |
| TrinoMGcUtilGcTimeFgct                 | GC时间_FGCT                          | Full GC 消耗时间                        | 秒(s)           | host4trinotrinocoordinator、id4trinotrinocoordinator |
| TrinoMGcUtilGcTimeGct                  | GC时间_GCT                           | 垃圾回收时间消耗                        | 秒(s)           | host4trinotrinocoordinator、id4trinotrinocoordinator |
| TrinoMGcUtilGcTimeYgct                 | GC时间_YGCT                          | Young GC 消耗时间                       | 秒(s)           | host4trinotrinocoordinator、id4trinotrinocoordinator |
| TrinoMGcUtilMemoryCcs                  | 内存区域占比_CCS                     | Compressed class space 区内存使用占比   | %               | host4trinotrinocoordinator、id4trinotrinocoordinator |
| TrinoMGcUtilMemoryE                    | 内存区域占比_E                       | Eden 区内存使用占比                     | %               | host4trinotrinocoordinator、id4trinotrinocoordinator |
| TrinoMGcUtilMemoryM                    | 内存区域占比_M                       | Metaspace 区内存使用占比                | %               | host4trinotrinocoordinator、id4trinotrinocoordinator |
| TrinoMGcUtilMemoryO                    | 内存区域占比_O                       | Old 区内存使用占比                      | %               | host4trinotrinocoordinator、id4trinotrinocoordinator |
| TrinoMGcUtilMemoryS0                   | 内存区域占比_S0                      | Survivor 0区内存使用占比                | %               | host4trinotrinocoordinator、id4trinotrinocoordinator |
| TrinoMGcUtilMemoryS1                   | 内存区域占比_S1                      | Survivor 1区内存使用占比                | %               | host4trinotrinocoordinator、id4trinotrinocoordinator |
| TrinoMJvmMemMemheapcommittedm          | JVM内存_MemHeapCommittedM            | JVM 已经提交的 HeapMemory 的数量        | MBytes          | host4trinotrinocoordinator、id4trinotrinocoordinator |
| TrinoMJvmMemMemheapinitm               | JVM内存_MemHeapInitM                 | JVM 初始 HeapMem 的数量                 | MBytes          | host4trinotrinocoordinator、id4trinotrinocoordinator |
| TrinoMJvmMemMemheapmaxm                | JVM内存_MemHeapMaxM                  | JVM 配置的 HeapMemory 的数量            | MBytes          | host4trinotrinocoordinator、id4trinotrinocoordinator |
| TrinoMJvmMemMemheapusedm               | JVM内存_MemHeapUsedM                 | JVM 当前已经使用的 HeapMemory 的数量    | MBytes          | host4trinotrinocoordinator、id4trinotrinocoordinator |
| TrinoMJvmMemMemnonheapcommittedm       | JVM内存_MemNonHeapCommittedM         | JVM 当前已经提交的 NonHeapMemory 的数量 | MBytes          | host4trinotrinocoordinator、id4trinotrinocoordinator |
| TrinoMJvmMemMemnonheapinitm            | JVM内存_MemNonHeapInitM              | JVM 初始 NonHeapMem 的数量              | MBytes          | host4trinotrinocoordinator、id4trinotrinocoordinator |
| TrinoMJvmMemMemnonheapusedm            | JVM内存_MemNonHeapUsedM              | JVM 当前已经使用的 NonHeapMemory 的数量 | MBytes          | host4trinotrinocoordinator、id4trinotrinocoordinator |
| TrinoMOsFdCountMaxfiledescriptorcount  | 文件描述符数_MaxFileDescriptorCount  | 最大文件描述符数                        | 次数总和(Count) | host4trinotrinocoordinator、id4trinotrinocoordinator |
| TrinoMOsFdCountOpenfiledescriptorcount | 文件描述符数_OpenFileDescriptorCount | 已打开文件描述符数量                    | 次数总和(Count) | host4trinotrinocoordinator、id4trinotrinocoordinator |
| TrinoMRtUptimeUptime                   | 进程运行时间_Uptime                  | 进程运行时间                            | 秒(s)           | host4trinotrinocoordinator、id4trinotrinocoordinator |
| TrinoMStartTimeStarttime               | 进程启动时间_StartTime               | 进程启动时间                            | 秒(s)           | host4trinotrinocoordinator、id4trinotrinocoordinator |
| TrinoMThreadCountDaemonthreadcount     | 线程数量_DaemonThreadCount           | Daemon 线程数量                         | 次数总和(Count) | host4trinotrinocoordinator、id4trinotrinocoordinator |
| TrinoMThreadCountPeakthreadcount       | 线程数量_PeakThreadCount             | 峰值线程数                              | 次数总和(Count) | host4trinotrinocoordinator、id4trinotrinocoordinator |
| TrinoMThreadCountThreadcount           | 线程数量_ThreadCount                 | 总线程数量                              | 次数总和(Count) | host4trinotrinocoordinator、id4trinotrinocoordinator |

## 各维度对应参数总览

| 参数名称                       | 维度名称                   | 维度解释                     | 格式                                                         |
| :----------------------------- | :------------------------- | :--------------------------- | :----------------------------------------------------------- |
| Instances.N.Dimensions.0.Name  | id4trinooverview           | EMR 实例 ID 的维度名称       | 输入 String 类型维度名称：id4trinooverview                   |
| Instances.N.Dimensions.0.Value | id4trinooverview           | EMR 实例具体 ID              | 输入 EMR 具体实例 ID，例如：emr-mm8bs222                     |
| Instances.N.Dimensions.0.Name  | host4trinotrinoworker      | EMR 实例中节点 IP 的维度名称 | 输入 String 类型维度名称：host4trinotrinoworker              |
| Instances.N.Dimensions.0.Value | host4trinotrinoworker      | EMR 实例中具体节点 IP        | 输入具体节点 IP ，可从控制台获取，登录 [腾讯云 MapReduce 控制台](https://console.cloud.tencent.com/emr)，单击**实例 > 集群资源 > 资源管理 > 节点内网 IP**。也可通过 [查询节点信息](https://cloud.tencent.com/document/product/589/41707) API 获取。 |
| Instances.N.Dimensions.0.Name  | id4trinotrinoworker        | EMR 实例 ID 的维度名称       | 输入 String 类型维度名称：id4trinotrinoworker                |
| Instances.N.Dimensions.0.Value | id4trinotrinoworker        | EMR 实例具体 ID              | 输入 EMR 具体实例 ID，例如：emr-mm8bs222                     |
| Instances.N.Dimensions.0.Name  | host4trinotrinocoordinator | EMR 实例中节点 IP 的维度名称 | 输入 String 类型维度名称：host4trinotrinocoordinator         |
| Instances.N.Dimensions.0.Value | host4trinotrinocoordinator | EMR 实例中具体节点 IP        | 输入具体节点 IP ，可从控制台获取，登录 [腾讯云 MapReduce 控制台](https://console.cloud.tencent.com/emr)，单击**实例 > 集群资源 > 资源管理 > 节点内网 IP**。也可通过 [查询节点信息](https://cloud.tencent.com/document/product/589/41707) API 获取。 |
| Instances.N.Dimensions.0.Name  | id4trinotrinocoordinator   | EMR 实例 ID 的维度名称       | 输入 String 类型维度名称：id4trinotrinocoordinator           |
| Instances.N.Dimensions.0.Value | id4trinotrinocoordinator   | EMR 实例具体 ID              | 输入 EMR 具体实例 ID，例如：emr-mm8bs222                     |



## 入参说明

**查询弹性 MapReduce（TRINO-概览）监控数据，入参取值如下：**

Namespace=QCE/TXMR_TRINO
&Instances.N.Dimensions.0.Name=id4trinooverview
&Instances.N.Dimensions.0.Value=EMR 实例具体 ID



**查询弹性 MapReduce（TRINO-WORKER）监控数据，入参取值如下：**

Namespace=QCE/TXMR_TRINO
&Instances.N.Dimensions.0.Name=host4trinotrinoworker
&Instances.N.Dimensions.0.Value=EMR 实例中具体节点 IP
&Instances.N.Dimensions.1.Name=id4trinotrinoworker
&Instances.N.Dimensions.1.Value=EMR 实例具体 ID



**查询弹性 MapReduce（TRINO-Coordinator）监控数据，入参取值如下：**

Namespace=QCE/TXMR_TRINO
&Instances.N.Dimensions.0.Name=host4trinotrinocoordinator
&Instances.N.Dimensions.0.Value=EMR 实例中具体节点 IP
&Instances.N.Dimensions.1.Name=id4trinotrinocoordinator
&Instances.N.Dimensions.1.Value=EMR 实例具体 ID

