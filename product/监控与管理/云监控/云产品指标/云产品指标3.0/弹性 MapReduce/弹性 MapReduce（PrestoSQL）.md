## 命名空间

Namespace=QCE/TXMR_PRESTOSQL



## 监控指标

### PrestoSQL-概览

| 指标英文名                                 | 指标中文名                               | 指标含义           | 指标单位 | 维度                 |
| ------------------------------------------ | ---------------------------------------- | ------------------ | -------- | -------------------- |
| PrestosqlMNodesActive                      | 节点数量_Active                          | 活跃节点数量       | 个       | id4prestosqloverview |
| PrestosqlMNodesFailed                      | 节点数量_Failed                          | 失败节点数量       | 个       | id4prestosqloverview |
| PrestosqlMNodesTotal                       | 节点数量_Total                           | 总节点数量         | 个       | id4prestosqloverview |
| PrestosqlMQueriesOneMinuteAbandonedqueries | 查询频度_AbandonedQueries                | 放弃的查询总数     | 个       | id4prestosqloverview |
| PrestosqlMQueriesOneMinuteCanceledqueries  | 查询频度_CanceledQueries                 | 取消的查询总数     | 个       | id4prestosqloverview |
| PrestosqlMQueriesOneMinuteCompletedqueries | 查询频度_CompletedQueries                | 完成的查询总数     | 个       | id4prestosqloverview |
| PrestosqlMQueriesOneMinuteFailedqueries    | 查询频度_FailedQueries                   | 失败的查询总数     | 个       | id4prestosqloverview |
| PrestosqlMQueriesOneMinuteStartedqueries   | 查询频度_StartedQueries                  | 已启动的查询总数   | 个       | id4prestosqloverview |
| PrestosqlMQueriesQueuedqueries             | 查询_ QueuedQueries                      | 等待状态的查询总数 | 个       | id4prestosqloverview |
| PrestosqlMQueriesRunningqueries            | 查询_RunningQueries                      | 正在运行的查询总数 | 个       | id4prestosqloverview |
| PrestosqlMDataRateInputdatasizeoneminute   | 数据输入输出速率_InputDataSizeOneMinute  | 输入数据速率       | GB       | id4prestosqloverview |
| PrestosqlMDataRateOutputdatasizeoneminute  | 数据输入输出速率_OutputDataSizeOneMinute | 输出数据速率       | GB       | id4prestosqloverview |
| PrestosqlMQueriesOneMinuteSubmittedqueries | 查询频度_SubmittedQueries                | 已提交的查询总数   | 次       | id4prestosqloverview |

###  PrestoSQL-Worker

| 指标英文名                                 | 指标中文名                           | 指标含义                                | 指标单位 | 维度                                                         |
| ------------------------------------------ | ------------------------------------ | --------------------------------------- | -------- | ------------------------------------------------------------ |
| PrestosqlMGcUtilGcCountFgc                 | GC次数_FGC                           | Full GC 次数                            | 次       | host4prestosqlprestosqlcoordinator、id4prestosqlprestosqlcoordinator |
| PrestosqlMGcUtilGcCountYgc                 | GC次数_YGC                           | Young GC 次数                           | 次       | host4prestosqlprestosqlcoordinator、id4prestosqlprestosqlcoordinator |
| PrestosqlMGcUtilGcTimeFgct                 | GC时间_FGCT                          | Full GC 消耗时间                        | s        | host4prestosqlprestosqlcoordinator、id4prestosqlprestosqlcoordinator |
| PrestosqlMGcUtilGcTimeGct                  | GC时间_GCT                           | 垃圾回收时间消耗                        | s        | host4prestosqlprestosqlcoordinator、id4prestosqlprestosqlcoordinator |
| PrestosqlMGcUtilGcTimeYgct                 | GC时间_YGCT                          | Young GC 消耗时间                       | s        | host4prestosqlprestosqlcoordinator、id4prestosqlprestosqlcoordinator |
| PrestosqlMGcUtilMemoryCcs                  | 内存区域占比_CCS                     | Compressed class space 区内存使用占比   | %        | host4prestosqlprestosqlcoordinator、id4prestosqlprestosqlcoordinator |
| PrestosqlMGcUtilMemoryE                    | 内存区域占比_E                       | Eden 区内存使用占比                     | %        | host4prestosqlprestosqlcoordinator、id4prestosqlprestosqlcoordinator |
| PrestosqlMGcUtilMemoryM                    | 内存区域占比_M                       | Metaspace 区内存使用占比                | %        | host4prestosqlprestosqlcoordinator、id4prestosqlprestosqlcoordinator |
| PrestosqlMGcUtilMemoryO                    | 内存区域占比_O                       | Old 区内存使用占比                      | %        | host4prestosqlprestosqlcoordinator、id4prestosqlprestosqlcoordinator |
| PrestosqlMGcUtilMemoryS0                   | 内存区域占比_S0                      | Survivor 0区内存使用占比                | %        | host4prestosqlprestosqlcoordinator、id4prestosqlprestosqlcoordinator |
| PrestosqlMGcUtilMemoryS1                   | 内存区域占比_S1                      | Survivor 1区内存使用占比                | %        | host4prestosqlprestosqlcoordinator、id4prestosqlprestosqlcoordinator |
| PrestosqlMJvmMemMemheapcommittedm          | JVM内存_MemHeapCommittedM            | JVM 已经提交的 HeapMemory 的数量        | MB       | host4prestosqlprestosqlcoordinator、id4prestosqlprestosqlcoordinator |
| PrestosqlMJvmMemMemheapinitm               | JVM内存_MemHeapInitM                 | JVM 初始 HeapMem 的数量                 | MB       | host4prestosqlprestosqlcoordinator、id4prestosqlprestosqlcoordinator |
| PrestosqlMJvmMemMemheapmaxm                | JVM内存_MemHeapMaxM                  | JVM 配置的 HeapMemory 的数量            | MB       | host4prestosqlprestosqlcoordinator、id4prestosqlprestosqlcoordinator |
| PrestosqlMJvmMemMemheapusedm               | JVM内存_MemHeapUsedM                 | JVM 当前已经使用的 HeapMemory 的数量    | MB       | host4prestosqlprestosqlcoordinator、id4prestosqlprestosqlcoordinator |
| PrestosqlMJvmMemMemnonheapcommittedm       | JVM内存_MemNonHeapCommittedM         | JVM 当前已经提交的 NonHeapMemory 的数量 | MB       | host4prestosqlprestosqlcoordinator、id4prestosqlprestosqlcoordinator |
| PrestosqlMJvmMemMemnonheapinitm            | JVM内存_MemNonHeapInitM              | JVM 初始 NonHeapMem 的数量              | MB       | host4prestosqlprestosqlcoordinator、id4prestosqlprestosqlcoordinator |
| PrestosqlMJvmMemMemnonheapusedm            | JVM内存_MemNonHeapUsedM              | JVM 当前已经使用的 NonHeapMemory 的数量 | MB       | host4prestosqlprestosqlcoordinator、id4prestosqlprestosqlcoordinator |
| PrestosqlMOsFdCountMaxfiledescriptorcount  | 文件描述符数_MaxFileDescriptorCount  | 最大文件描述符数                        | 个       | host4prestosqlprestosqlcoordinator、id4prestosqlprestosqlcoordinator |
| PrestosqlMOsFdCountOpenfiledescriptorcount | 文件描述符数_OpenFileDescriptorCount | 已打开文件描述符数量                    | 个       | host4prestosqlprestosqlcoordinator、id4prestosqlprestosqlcoordinator |
| PrestosqlMRtUptimeUptime                   | 进程运行时间_Uptime                  | 进程运行时间                            | 个       | host4prestosqlprestosqlcoordinator、id4prestosqlprestosqlcoordinator |
| PrestosqlMStartTimeStarttime               | 进程启动时间_StartTime               | 进程启动时间                            | s        | host4prestosqlprestosqlcoordinator、id4prestosqlprestosqlcoordinator |
| PrestosqlMThreadCountDaemonthreadcount     | 线程数量_DaemonThreadCount           | Daemon 线程数量                         | 个       | host4prestosqlprestosqlcoordinator、id4prestosqlprestosqlcoordinator |
| PrestosqlMThreadCountPeakthreadcount       | 线程数量_PeakThreadCount             | 峰值线程数                              | 个       | host4prestosqlprestosqlcoordinator、id4prestosqlprestosqlcoordinator |
| PrestosqlMThreadCountThreadcount           | 线程数量_ThreadCount                 | 总线程数量                              | 个       | host4prestosqlprestosqlcoordinator、id4prestosqlprestosqlcoordinator |

### PRESTOSQL-Coordinator

| 指标英文名                                 | 指标中文名                               | 指标含义                                | 指标单位 | 维度                                                       |
| ------------------------------------------ | ---------------------------------------- | --------------------------------------- | -------- | ---------------------------------------------------------- |
| PrestosqlWGcUtilGcCountFgc                 | GC次数_FGC                               | Full GC 次数                            | 个       | host4prestosqlprestosqlworker、id4prestosqlprestosqlworker |
| PrestosqlWGcUtilGcCountYgc                 | GC次数_YGC                               | Young GC 次数                           | 个       | host4prestosqlprestosqlworker、id4prestosqlprestosqlworker |
| PrestosqlWGcUtilGcTimeFgct                 | GC时间_FGCT                              | Full GC 消耗时间                        | s        | host4prestosqlprestosqlworker、id4prestosqlprestosqlworker |
| PrestosqlWGcUtilGcTimeGct                  | GC时间_GCT                               | 垃圾回收时间消耗                        | s        | host4prestosqlprestosqlworker、id4prestosqlprestosqlworker |
| PrestosqlWGcUtilGcTimeYgct                 | GC时间_YGCT                              | Young GC 消耗时间                       | s        | host4prestosqlprestosqlworker、id4prestosqlprestosqlworker |
| PrestosqlWGcUtilMemoryCcs                  | 内存区域占比_CCS                         | Compressed class space 区内存使用占比   | %        | host4prestosqlprestosqlworker、id4prestosqlprestosqlworker |
| PrestosqlWGcUtilMemoryE                    | 内存区域占比_E                           | Eden 区内存使用占比                     | %        | host4prestosqlprestosqlworker、id4prestosqlprestosqlworker |
| PrestosqlWGcUtilMemoryM                    | 内存区域占比_M                           | Metaspace 区内存使用占比                | %        | host4prestosqlprestosqlworker、id4prestosqlprestosqlworker |
| PrestosqlWGcUtilMemoryO                    | 内存区域占比_O                           | Old 区内存使用占比                      | %        | host4prestosqlprestosqlworker、id4prestosqlprestosqlworker |
| PrestosqlWGcUtilMemoryS0                   | 内存区域占比_S0                          | Survivor 0区内存使用占比                | %        | host4prestosqlprestosqlworker、id4prestosqlprestosqlworker |
| PrestosqlWGcUtilMemoryS1                   | 内存区域占比_S1                          | Survivor 1区内存使用占比                | %        | host4prestosqlprestosqlworker、id4prestosqlprestosqlworker |
| PrestosqlWJvmMemMemheapcommittedm          | JVM内存_MemHeapCommittedM                | JVM 已经提交的 HeapMemory 的数量        | MB       | host4prestosqlprestosqlworker、id4prestosqlprestosqlworker |
| PrestosqlWJvmMemMemheapinitm               | JVM内存_MemHeapInitM                     | JVM 初始 HeapMem 的数量                 | MB       | host4prestosqlprestosqlworker、id4prestosqlprestosqlworker |
| PrestosqlWJvmMemMemheapmaxm                | JVM内存_MemHeapMaxM                      | JVM 配置的 HeapMemory 的数量            | MB       | host4prestosqlprestosqlworker、id4prestosqlprestosqlworker |
| PrestosqlWJvmMemMemheapusedm               | JVM内存_MemHeapUsedM                     | JVM 当前已经使用的 HeapMemory 的数量    | MB       | host4prestosqlprestosqlworker、id4prestosqlprestosqlworker |
| PrestosqlWJvmMemMemnonheapcommittedm       | JVM内存_MemNonHeapCommittedM             | JVM 当前已经提交的 NonHeapMemory 的数量 | MB       | host4prestosqlprestosqlworker、id4prestosqlprestosqlworker |
| PrestosqlWJvmMemMemnonheapinitm            | JVM内存_MemNonHeapInitM                  | JVM 初始 NonHeapMem 的数量              | MB       | host4prestosqlprestosqlworker、id4prestosqlprestosqlworker |
| PrestosqlWJvmMemMemnonheapusedm            | JVM内存_MemNonHeapUsedM                  | JVM 当前已经使用的 NonHeapMemory 的数量 | MB       | host4prestosqlprestosqlworker、id4prestosqlprestosqlworker |
| PrestosqlWOsFdCountMaxfiledescriptorcount  | 文件描述符数_MaxFileDescriptorCount      | 最大文件描述符数                        | 个       | host4prestosqlprestosqlworker、id4prestosqlprestosqlworker |
| PrestosqlWOsFdCountOpenfiledescriptorcount | 文件描述符数_OpenFileDescriptorCount     | 已打开文件描述符数量                    | 个       | host4prestosqlprestosqlworker、id4prestosqlprestosqlworker |
| PrestosqlWRtUptimeUptime                   | 进程运行时间_Uptime                      | 进程运行时间                            | s        | host4prestosqlprestosqlworker、id4prestosqlprestosqlworker |
| PrestosqlWStartTimeStarttime               | 进程启动时间_StartTime                   | 进程启动时间                            | s        | host4prestosqlprestosqlworker、id4prestosqlprestosqlworker |
| PrestosqlWThreadCountDaemonthreadcount     | 线程数量_DaemonThreadCount               | Daemon 线程数量                         | 个       | host4prestosqlprestosqlworker、id4prestosqlprestosqlworker |
| PrestosqlWThreadCountPeakthreadcount       | 线程数量_PeakThreadCount                 | 峰值线程数                              | 个       | host4prestosqlprestosqlworker、id4prestosqlprestosqlworker |
| PrestosqlWThreadCountThreadcount           | 线程数量_ThreadCount                     | 总线程数量                              | 个       | host4prestosqlprestosqlworker、id4prestosqlprestosqlworker |
| PrestosqlWDataRateInputdatasizeoneminute   | 数据输入输出速率_InputDataSizeOneMinute  | 输入数据速率                            | GB       | host4prestosqlprestosqlworker、id4prestosqlprestosqlworker |
| PrestosqlWDataRateOutputdatasizeoneminute  | 数据输入输出速率_OutputDataSizeOneMinute | 输出数据速率                            | GB       | host4prestosqlprestosqlworker、id4prestosqlprestosqlworker |

## 各维度对应参数总览

| 参数名称                       | 维度名称                           | 维度解释                     | 格式                                                         |
| :----------------------------- | :--------------------------------- | :--------------------------- | :----------------------------------------------------------- |
| Instances.N.Dimensions.0.Name  | id4prestosqloverview               | EMR 实例 ID 的维度名称       | 输入 String 类型维度名称：id4trinooverview                   |
| Instances.N.Dimensions.0.Value | id4prestosqloverview               | EMR 实例具体 ID              | 输入 EMR 具体实例 ID，例如：emr-mm8bs222                     |
| Instances.N.Dimensions.0.Name  | host4prestosqlprestosqlcoordinator | EMR 实例中节点 IP 的维度名称 | 输入 String 类型维度名称：host4trinotrinoworker              |
| Instances.N.Dimensions.0.Value | host4prestosqlprestosqlcoordinator | EMR 实例中具体节点 IP        | 输入具体节点 IP ，可从控制台获取，登录 [腾讯云 MapReduce 控制台](https://console.cloud.tencent.com/emr)，单击**实例 > 集群资源 > 资源管理 > 节点内网 IP**。也可通过 [查询节点信息](https://cloud.tencent.com/document/product/589/41707) API 获取。 |
| Instances.N.Dimensions.0.Name  | id4prestosqlprestosqlcoordinator   | EMR 实例 ID 的维度名称       | 输入 String 类型维度名称：id4trinotrinoworker                |
| Instances.N.Dimensions.0.Value | id4prestosqlprestosqlcoordinator   | EMR 实例具体 ID              | 输入 EMR 具体实例 ID，例如：emr-mm8bs222                     |
| Instances.N.Dimensions.0.Name  | host4prestosqlprestosqlworker      | EMR 实例中节点 IP 的维度名称 | 输入 String 类型维度名称：host4prestosqlprestosqlworker      |
| Instances.N.Dimensions.0.Value | host4prestosqlprestosqlworker      | EMR 实例中具体节点 IP        | 输入具体节点 IP ，可从控制台获取，登录 [腾讯云 MapReduce 控制台](https://console.cloud.tencent.com/emr)，单击**实例 > 集群资源 > 资源管理 > 节点内网 IP**。也可通过 [查询节点信息](https://cloud.tencent.com/document/product/589/41707) API 获取。 |
| Instances.N.Dimensions.0.Name  | id4prestosqlprestosqlworker        | EMR 实例 ID 的维度名称       | 输入 String 类型维度名称：id4prestosqlprestosqlworker        |
| Instances.N.Dimensions.0.Value | id4prestosqlprestosqlworker        | EMR 实例具体 ID              | 输入 EMR 具体实例 ID，例如：emr-mm8bs222                     |



## 入参说明

**查询弹性 MapReduce（PrestoSQL-概览）监控数据，入参取值如下：**
Namespace=QCE/TXMR_PRESTOSQL
&Instances.N.Dimensions.0.Name=id4prestosqloverview
&Instances.N.Dimensions.0.Value=EMR 实例具体 ID



**查询弹性 MapReduce（PrestoSQL-Worker）监控数据，入参取值如下：**

Namespace=QCE/TXMR_PRESTOSQL
&Instances.N.Dimensions.0.Name=host4prestosqlprestosqlcoordinator
&Instances.N.Dimensions.0.Value=EMR 实例中具体节点 IP
&Instances.N.Dimensions.1.Name=id4prestosqlprestosqlcoordinator
&Instances.N.Dimensions.1.Value=EMR 实例具体 ID



**查询弹性 MapReduce（PRESTOSQL-Coordinator）监控数据，入参取值如下：**

Namespace=QCE/TXMR_PRESTOSQL
&Instances.N.Dimensions.0.Name=host4prestosqlprestosqlworker
&Instances.N.Dimensions.0.Value=EMR 实例中具体节点 IP
&Instances.N.Dimensions.1.Name=id4prestosqlprestosqlworker
&Instances.N.Dimensions.1.Value=EMR 实例具体 ID




