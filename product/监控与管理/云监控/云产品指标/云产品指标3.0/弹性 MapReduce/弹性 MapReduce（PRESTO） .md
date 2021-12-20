## 命名空间

Namespace=QCE/TXMR_PRESTO

## 监控指标

### PRESTO-Overview

| 指标英文名                                                   | 指标中文名                                   | 指标单位 | 指标含义           | 维度              |
| ------------------------------------------------------------ | -------------------------------------------- | -------- | ------------------ | ----------------- |
| EmrPrestoOverviewPresto<br/>MNodesActive             | 节点数量_Active                              | 个       | 活跃节点数量       | id4prestooverview |
| EmrPrestoOverviewPresto<br/>MNodesTotal              | 节点数量_Total                               | 个       | 总节点数量         | id4prestooverview |
| EmrPrestoOverviewPresto<br/>MNodesFailed               | 节点数量_Failed                              | 个       | 失败节点数量       | id4prestooverview |
| EmrPrestoOverviewPresto<br/>MQueries<br>Runningqueries | 查询_RunningQueries                          | 个       | 正在运行的查询总数 | id4prestooverview |
| EmrPrestoOverviewPresto<br/>MQueriesOneMinute<br>Failedqueries | 查询频度_FailedQueries                       | 个/min   | 失败的查询总数     | id4prestooverview |
| EmrPrestoOverviewPresto<br/>MQueriesOneMinute<br>Abandonedqueries | 查询频度_AbandonedQueries                    | 个/min   | 放弃的查询总数     | id4prestooverview |
| EmrPrestoOverviewPresto<br/>MQueriesOneMinute<br>Canceledqueries | 查询频度_CanceledQueries                     | 个/min   | 取消的查询总数     | id4prestooverview |
| EmrPrestoOverviewPresto<br/>MQueriesOneMinute<br>Completedqueries | 查询频度_CompletedQueries                    | 个/min   | 完成的查询总数     | id4prestooverview |
| EmrPrestoOverviewPresto<br/>MQueriesOneMinute<br>Startedqueries | 查询频度_StartedQueries                      | 个/min   | 开始的查询总数     | id4prestooverview |
| EmrPrestoOverviewPresto<br/>MDataOneMinuteRate<br>Inputdatasizeoneminute | 每分钟数据输入输出量_InputDataSizeOneMinute  | GB/min   | 输入数据速率       | id4prestooverview |
| EmrPrestoOverviewPresto<br/>MDataOneMinuteRate<br>Outputdatasizeoneminute | 每分钟数据输入输出量_OutputDataSizeOneMinute | GB/min   | 输出数据速率       | id4prestooverview |

### PRESTO-OverviewOriginal

| 指标英文名                                                   | 指标中文名                                   | 指标单位 | 指标含义           | 维度                                        |
| ------------------------------------------------------------ | -------------------------------------------- | -------- | ------------------ | ------------------------------------------- |
| EmrPrestoOverview<br>OriginalPresto<br>MNodesActive    | 节点数量_Active                              | 个       | 活跃节点数量       | id4prestooverview、<br/>host4prestooverview |
| EmrPrestoOverview<br/>OriginalPresto<br/>MNodesTotal   | 节点数量_Total                               | 个       | 总节点数量         | id4prestooverview、<br/>host4prestooverview |
| EmrPrestoOverview<br/>OriginalPresto<br/>MNodesFailed  | 节点数量_Failed                              | 个       | 失败节点数量       | id4prestooverview、<br/>host4prestooverview |
| EmrPrestoOverview<br/>OriginalPresto<br/>MQueries<br>Runningqueries | 查询_RunningQueries                          | 个       | 正在运行的查询总数 | id4prestooverview、<br/>host4prestooverview |
| EmrPrestoOverview<br/>OriginalPresto<br/>MQueriesOneMinute<br>Failedqueries | 查询频度_FailedQueries                       | 个/min   | 失败的查询总数     | id4prestooverview、<br>host4prestooverview  |
| EmrPrestoOverview<br/>OriginalPresto<br/>MQueriesOneMinute Abandonedqueries | 查询频度_AbandonedQueries                    | 个/min   | 放弃的查询总数     | id4prestooverview、<br/>host4prestooverview |
| EmrPrestoOverview<br/>OriginalPresto<br/>MQueriesOneMinute<br>Canceledqueries | 查询频度_CanceledQueries                     | 个/min   | 取消的查询总数     | id4prestooverview、<br/>host4prestooverview |
| EmrPrestoOverview<br/>OriginalPresto<br/>MQueriesOneMinute<br>Completedqueries | 查询频度_CompletedQueries                    | 个/min   | 完成的查询总数     | id4prestooverview、<br/>host4prestooverview |
| EmrPrestoOverview<br/>OriginalPresto<br/>MQueriesOneMinute Startedqueries | 查询频度_StartedQueries                      | 个/min   | 开始的查询总数     | id4prestooverview、<br/>host4prestooverview |
| EmrPrestoOverview<br/>OriginalPresto<br/>MDataOneMinuteRate<br>Inputdatasizeoneminute | 每分钟数据输入输出量_InputDataSizeOneMinute  | GB/min   | 输入数据速率       | id4prestooverview、<br/>host4prestooverview |
| EmrPrestoOverview<br/>OriginalPresto<br/>MDataOneMinuteRate<br>Outputdatasizeoneminute | 每分钟数据输入输出量_OutputDataSizeOneMinute | GB/min   | 输出数据速率       | id4prestooverview、<br/>host4prestooverview |



### PRESTO-Worker

| 指标英文名                                              | 指标中文名                               | 指标单位 | 指标含义                                | 维度                                               |
| ------------------------------------------------------- | ---------------------------------------- | -------- | --------------------------------------- | -------------------------------------------------- |
| PrestoWGcUtilGcCountYgc                                 | GC 次数_YGC                              | 次       | Young GC 次数                           | host4prestoprestoworker、<br>id4prestoprestoworker |
| PrestoWGcUtilGcCountFgc                                 | GC 次数_FGC                              | 次       | Full GC 次数                            | host4prestoprestoworker、<br>id4prestoprestoworker |
| PrestoWGcUtilGcTimeFgct                                 | GC 时间_FGCT                             | s        | Full GC 消耗时间                        | host4prestoprestoworker、<br>id4prestoprestoworker |
| PrestoWGcUtilGcTimeGct                                  | GC 时间_FGCT                             | s        | 垃圾回收时间消耗                        | host4prestoprestoworker、<br>id4prestoprestoworker |
| PrestoWGcUtilGcTimeYgct                                 | GC 时间_YGCT                             | s        | Young GC 消耗时间                       | host4prestoprestoworker、<br>id4prestoprestoworker |
| PrestoWGcUtilMemoryS0                                   | 内存区域占比_S0                          | %        | Survivor 0区内存使用占比                | host4prestoprestoworker、<br>id4prestoprestoworker |
| PrestoWGcUtilMemoryE     | 内存区域占比\_E  | %        | Eden 区内存使用占比                     | host4prestoprestoworker、<br>id4prestoprestoworker |
| PrestoWGcUtilMemoryCcs                                  | 内存区域占比_CCS                         | %        | Compressed class space 区内存使用占比   | host4prestoprestoworker、<br>id4prestoprestoworker |
| PrestoWGcUtilMemoryS1                                   | 内存区域占比_S1                          | %        | Survivor 1区内存使用占比                | host4prestoprestoworker、<br>id4prestoprestoworker |
| PrestoWGcUtilMemoryO                                    |内存区域占比\_O  | %        | Old 区内存使用占比                      | host4prestoprestoworker、<br>id4prestoprestoworker |
| PrestoWGcUtilMemoryM                                    | 内存区域占比\_M  | %        | Metaspace 区内存使用占比                | host4prestoprestoworker、<br>id4prestoprestoworker |
| PrestoWJvmMemMem<br>nonheapusedm                        | JVM 内存_MemNonHeapUsedM                 | MB       | JVM 当前已经使用的 NonHeapMemory 的数量 | host4prestoprestoworker、<br>id4prestoprestoworker |
| PrestoWJvmMemMem<br>nonheapcommittedm                   | JVM 内存_MemNonHeapCommittedM            | MB       | JVM 当前已经提交的 NonHeapMemory 的数量 | host4prestoprestoworker、<br>id4prestoprestoworker |
| PrestoWJvmMem<br>Memheapusedm                           | JVM 内存_MemHeapUsedM                    | MB       | JVM 当前已经使用的 HeapMemory 的数量    | host4prestoprestoworker、<br>id4prestoprestoworker |
| PrestoWJvmMemMem<br>heapcommittedm                      | JVM 内存_MemHeapCommittedM               | MB       | JVM 当前已经提交的 HeapMemory 的数量    | host4prestoprestoworker、<br>id4prestoprestoworker |
| PrestoWJvmMem<br>Memheapmaxm                            | JVM 内存_MemHeapMaxM                     | MB       | JVM 配置的 HeapMemory 的数量            | host4prestoprestoworker、<br>id4prestoprestoworker |
| PrestoWJvmMem<br>Memheapinitm                           | JVM 内存_MemHeapInitM                    | MB       | JVM 初始 HeapMem 的数量                 | host4prestoprestoworker、<br>id4prestoprestoworker |
| PrestoWJvmMem<br>Memnonheapinitm                        | JVM 内存_MemNonHeapInitM                 | MB       | JVM 初始 NonHeapMem 的数量              | host4prestoprestoworker、<br>id4prestoprestoworker |
| PrestoWDataOneMinute<br>RateInputdatasizeoneminute      | 数据输入输出速率_InputDataSizeOneMinute  | GB/min   | 输入数据速率                            | host4prestoprestoworker、<br>id4prestoprestoworker |
| PrestoWDataOneMinute<br>RateOutputdata<br>sizeoneminute | 数据输入输出速率_OutputDataSizeOneMinute | GB/min   | 输出数据速率                            | host4prestoprestoworker、<br>id4prestoprestoworker |
| PrestoWThreadCount<br>Peakthreadcount                   | 进程数量_PeakThreadCount                 | 个       | 峰值线程数                              | host4prestoprestoworker、<br>id4prestoprestoworker |
| PrestoWThreadCount<br>Daemonthreadcount                 | 进程数量_DaemonThreadCount               | 个       | 线程数量                                | host4prestoprestoworker、<br>id4prestoprestoworker |
| PrestoWThreadCount<br>Threadcount                       | 进程数量_ThreadCount                     | 个       | 后台线程数量                            | host4prestoprestoworker、<br>id4prestoprestoworker |
| PrestoWUptimeUptime                                     | 进程运行时间_Uptime                      | s        | 进程运行时间                            | host4prestoprestoworker、<br>id4prestoprestoworker |
| PrestoWStartTimeStarttime                               | 进程启动时间_StartTime                   | s        | 进程启动时间                            | host4prestoprestoworker、<br>id4prestoprestoworker |
| PrestoWOsFdCount<br>Maxfiledescriptorcount              | 文件描述符数_MaxFileDescriptorCount      | 个       | 最大文件描述符数                        | host4prestoprestoworker、<br>id4prestoprestoworker |
| PrestoWOsFdCount<br>Openfiledescriptorcount             | 文件描述符数_OpenFileDescriptorCount     | 个       | 已打开文件描述符数                      | host4prestoprestoworker、<br>id4prestoprestoworker |

### PRESTO-Coordinator

| 指标英文名                                  | 指标中文名                           | 指标单位 | 指标含义                                | 维度                                                         |
| ------------------------------------------- | ------------------------------------ | -------- | --------------------------------------- | ------------------------------------------------------------ |
| PrestoMGc<br>UtilGcCountYgc                 | GC 次数_YGC                          | 次       | Young GC 次数                           | host4prestoprestocoordinator、<br>id4prestoprestocoordinator |
| PrestoMGc<br>UtilGcCountFgc                 | GC 次数_FGC                          | 次       | Full GC 次数                            | host4prestoprestocoordinator、<br>id4prestoprestocoordinator |
| PrestoMGc<br>UtilGcTimeFgct                 | GC 时间_FGCT                         | s        | Full GC 消耗时间                        | host4prestoprestocoordinator、<br>id4prestoprestocoordinator |
| PrestoMGc<br>UtilGcTimeGct                  | GC 时间_FGCT                         | s        | 垃圾回收时间消耗                        | host4prestoprestocoordinator、<br>id4prestoprestocoordinator |
| PrestoMGc<br>UtilGcTimeYgct                 | GC 时间_YGCT                         | s        | Young GC 消耗时间                       | host4prestoprestocoordinator、<br>id4prestoprestocoordinator |
| PrestoMGc<br>UtilMemoryS0                   | 内存区域占比_S0                      | %        | Survivor 0区内存使用占比                | host4prestoprestocoordinator、<br>id4prestoprestocoordinator |
| PrestoMGcUtilMemoryE                        | 内存区域占比_E                       | %        | Eden 区内存使用占比                     | host4prestoprestocoordinator、<br>id4prestoprestocoordinator |
| PrestoMGc<br>UtilMemoryCcs                  | 内存区域占比_CCS                     | %        | Compressed class space 区内存使用占比   | host4prestoprestocoordinator、<br>id4prestoprestocoordinator |
| PrestoMGcUtilMemoryS1                       | 内存区域占比_S1                      | %        | Survivor 1区内存使用占比                | host4prestoprestocoordinator、<br>id4prestoprestocoordinator |
| PrestoMGcUtilMemoryO                        | 内存区域占比_O                       | %        | Old 区内存使用占比                      | host4prestoprestocoordinator、<br>id4prestoprestocoordinator |
| PrestoMGcUtilMemoryM                        | 内存区域占比_M                       | %        | Metaspace 区内存使用占比                | host4prestoprestocoordinator、<br>id4prestoprestocoordinator |
| PrestoMJvmMemMem<br>nonheapusedm            | JVM 内存_MemNonHeapUsedM             | MB       | JVM 当前已经使用的 NonHeapMemory 的数量 | host4prestoprestocoordinator、<br>id4prestoprestocoordinator |
| PrestoMJvmMemMem<br>nonheapcommittedm       | JVM 内存_MemNonHeapCommittedM        | MB       | JVM 当前已经提交的 NonHeapMemory 的数量 | host4prestoprestocoordinator、<br>id4prestoprestocoordinator |
| PrestoMJvmMem<br>Memheapusedm               | JVM 内存_MemHeapUsedM                | MB       | JVM 当前已经使用的 HeapMemory 的数量    | host4prestoprestocoordinator、<br>id4prestoprestocoordinator |
| PrestoMJvmMem<br>Memheapcommittedm          | JVM 内存_MemHeapCommittedM           | MB       | JVM 当前已经提交的 HeapMemory 的数量    | host4prestoprestocoordinator、<br>id4prestoprestocoordinator |
| PrestoMJvmMem<br>Memheapmaxm                | JVM 内存_MemHeapMaxM                 | MB       | JVM 配置的 HeapMemory 的数量            | host4prestoprestocoordinator、<br>id4prestoprestocoordinator |
| PrestoMJvmMem<br>Memheapinitm               | JVM 内存_MemHeapInitM                | MB       | JVM 初始 HeapMem 的数量                 | host4prestoprestocoordinator、<br>id4prestoprestocoordinator |
| PrestoMJvmMem<br>Memnonheapinitm            | JVM 内存_MemNonHeapInitM             | MB       | JVM 初始 NonHeapMem 的数量              | host4prestoprestocoordinator、<br>id4prestoprestocoordinator |
| PrestoMThreadCount<br>Peakthreadcount       | 进程数量_PeakThreadCount             | 个       | 峰值线程数                              | host4prestoprestocoordinator、<br>id4prestoprestocoordinator |
| PrestoMThreadCount<br>Daemonthreadcount     | 进程数量_DaemonThreadCount           | 个       | 线程数量                                | host4prestoprestocoordinator、<br>id4prestoprestocoordinator |
| PrestoMThread<br>CountThreadcount           | 进程数量_ThreadCount                 | 个       | 后台线程数量                            | host4prestoprestocoordinator、<br>id4prestoprestocoordinator |
| PrestoMUptimeUptime                         | 进程运行时间_Uptime                  | s        | 进程运行时间                            | host4prestoprestocoordinator、<br>id4prestoprestocoordinator |
| PrestoMStart<br>TimeStarttime               | 进程启动时间_StartTime               | s        | 进程启动时间                            | host4prestoprestocoordinator、<br>id4prestoprestocoordinator |
| PrestoMOsFdCount<br>Maxfiledescriptorcount  | 文件描述符数_MaxFileDescriptorCount  | 个       | 最大文件描述符数                        | host4prestoprestocoordinator、<br>id4prestoprestocoordinator |
| PrestoMOsFdCount<br>Openfiledescriptorcount | 文件描述符数_OpenFileDescriptorCount | 个       | 已打开文件描述符数                      | host4prestoprestocoordinator、<br/>id4prestoprestocoordinator |

## 各维度对应参数总览

| 参数名称                       | 维度名称                     | 维度解释                     | 格式                                                         |
| :----------------------------- | :--------------------------- | :--------------------------- | :----------------------------------------------------------- |
| Instances.N.Dimensions.0.Name  | id4prestooverview            | EMR 实例 ID 的维度名称       | 输入 String 类型维度名称：id4prestooverview                  |
| Instances.N.Dimensions.0.Value | id4prestooverview            | EMR 实例具体 ID              | 输入 EMR 具体实例 ID，例如 ：emr-mm8bs222                    |
| Instances.N.Dimensions.1.Name  | host4prestooverview          | EMR 实例中节点 IP 的维度名称 | 输入String 类型维度名称：host4prestooverview                 |
| Instances.N.Dimensions.1.Value | host4prestooverview          | EMR 实例中具体节点 IP        | 输入具体节点  IP ，可从控制台获取，登录 [腾讯云 MapReduce 控制台](https://console.cloud.tencent.com/emr) > 单击实例 > 集群资源 > 资源管理 > 节点内网 IP。也可通过 [查询节点信息](https://cloud.tencent.com/document/product/589/41707) API 获取。 |
| Instances.N.Dimensions.0.Name  | id4prestoprestoworker        | EMR 实例 ID 的维度名称       | 输入 String 类型维度名称：id4prestoprestoworker              |
| Instances.N.Dimensions.0.Value | id4prestoprestoworker        | EMR 实例具体 ID              | 输入 EMR 具体实例 ID，例如 ：emr-mm8bs222                    |
| Instances.N.Dimensions.1.Name  | host4prestoprestoworker      | EMR 实例中节点 IP 的维度名称 | 输入 String 类型维度名称：host4prestoprestoworker            |
| Instances.N.Dimensions.1.Value | host4prestoprestoworker      | EMR 实例中具体节点 IP        | 输入具体节点  IP ，可从控制台获取，登录 [腾讯云 MapReduce 控制台](https://console.cloud.tencent.com/emr) > 单击实例 > 集群资源 > 资源管理 > 节点内网 IP。也可通过 [查询节点信息](https://cloud.tencent.com/document/product/589/41707) API 获取。 |
| Instances.N.Dimensions.0.Name  | id4prestoprestocoordinator   | EMR 实例 ID 的维度名称       | 输入 String 类型维度名称：id27prestoprestocoordinator        |
| Instances.N.Dimensions.0.Value | id4prestoprestocoordinator   | EMR 实例具体 ID              | 输入 EMR 具体实例 ID，例如 ：emr-mm8bs222                    |
| Instances.N.Dimensions.1.Name  | host4prestoprestocoordinator | EMR 实例中节点 IP 的维度名称 | 输入 String 类型维度名称：host4prestoprestocoordinator       |
| Instances.N.Dimensions.1.Value | host4prestoprestocoordinator | EMR 实例中具体节点 IP        | 输入具体节点  IP ，可从控制台获取，登录 [腾讯云 MapReduce 控制台](https://console.cloud.tencent.com/emr) > 单击实例 > 集群资源 > 资源管理 > 节点内网 IP。也可通过 [查询节点信息](https://cloud.tencent.com/document/product/589/41707) API 获取。 |



## 入参说明

弹性 MapReduce（PRESTO）支持以下四种维度组合的查询方式，四种入参取值如下： 

**1.查询  PRESTO-Overview  的指标监控数据，入参取值如下：**
&Namespace=QCE/TXMR_PRESTO
&Instances.N.Dimensions.0.Name=id4prestooverview
&Instances.N.Dimensions.0.Value=EMR 实例 ID

**2.查询  PRESTO-OverviewOriginal 的指标监控数据，入参取值如下：**
&Namespace=QCE/TXMR_PRESTO
&Instances.N.Dimensions.0.Name=id4prestooverview
&Instances.N.Dimensions.0.Value=EMR 实例 ID
&Instances.N.Dimensions.1.Name=host4prestooverview
&Instances.N.Dimensions.1.Value=EMR 实例中具体节点 IP

**3.查询  PRESTO-Worker  的指标监控数据，入参取值如下：**
&Namespace=QCE/TXMR_PRESTO
&Instances.N.Dimensions.0.Name=id4prestoprestoworker
&Instances.N.Dimensions.0.Value=EMR 实例 ID 
&Instances.N.Dimensions.1.Name=host4prestoprestoworker
&Instances.N.Dimensions.1.Value=EMR 实例中具体节点 IP

**4.查询  PRESTO-Coordinator  的指标监控数据，入参取值如下：**
&Namespace=QCE/TXMR_PRESTO
&Instances.N.Dimensions.0.Name=id27prestoprestocoordinator
&Instances.N.Dimensions.0.Value=EMR 实例 ID
&Instances.N.Dimensions.1.Name=host4prestoprestocoordinator
&Instances.N.Dimensions.1.Value=EMR 实例中具体节点 IP

