## 命名空间

Namespace=QCE/TXMR_HIVE

## 监控指标

### HIVE-HiveMetaStore

| 指标英文名              | 指标中文名       | 指标单位 | 指标含义                              | 维度                                   |
| ----------------------- | ---------------- | -------- | ------------------------------------- | -------------------------------------- |
| HiveHmsGcUtilGcCountYgc | GC 次数_YGC       | 次       | Young GC 次数                         | id4hivemetastore<br>host4hivemetastore |
| HiveHmsGcUtilGcCountFgc | GC 次数_FGC       | 次       | Full GC 次数                          | id4hivemetastore<br>host4hivemetastore |
| HiveHmsGcUtilGcTimeFgct | GC 时间_FGCT      | s        | Full GC 消耗时间                      | id4hivemetastore<br>host4hivemetastore |
| HiveHmsGcUtilGcTimeGct  | GC 时间_FGCT      | s        | 垃圾回收时间消耗                      | id4hivemetastore<br>host4hivemetastore |
| HiveHmsGcUtilGcTimeYgct | GC 时间_YGCT      | s        | Young GC 消耗时间                     | id4hivemetastore<br>host4hivemetastore |
| HiveHmsGcUtilMemoryS0   | 内存区域占比_S0  | %        | Survivor 0区内存使用占比              | id4hivemetastore<br>host4hivemetastore |
| HiveHmsGcUtilMemoryE    | 内存区域占比_E   | %        | Eden 区内存使用占比                   | id4hivemetastore<br>host4hivemetastore |
| HiveHmsGcUtilMemoryCcs  | 内存区域占比_CCS | %        | Compressed class space 区内存使用占比 | id4hivemetastore<br>host4hivemetastore |
| HiveHmsGcUtilMemoryS1   | 内存区域占比_S1  | %        | Survivor 1区内存使用占比              | id4hivemetastore<br>host4hivemetastore |
| HiveHmsGcUtilMemoryO    | 内存区域占比_O   | %        | Old 区内存使用占比                    | id4hivemetastore<br>host4hivemetastore |
| HiveHmsGcUtilMemoryM    | 内存区域占比_M   | %        | Metaspace 区内存使用占比              | id4hivemetastore<br>host4hivemetastore |

### HIVE-HiveServer2

| 指标英文名                                  | 指标中文名                           | 指标单位 | 指标含义                                | 维度                                          |
| ------------------------------------------- | ------------------------------------ | -------- | --------------------------------------- | --------------------------------------------- |
| HiveH2GcUtilGcCountYgc                      | GC 次数_YGC                           | 次       | Young GC 次数                           | host4hivehiveserver2、<br>id4hivehiveserver2  |
| HiveH2GcUtilGcCountFgc                      | GC 次数_FGC                           | 次       | Full GC 次数                            | host4hivehiveserver2、<br>id4hivehiveserver2  |
| HiveH2GcUtilGcTimeFgct                      | GC 时间_FGCT                          | s        | Full GC 消耗时间                        | host4hivehiveserver2、<br/>id4hivehiveserver2 |
| HiveH2GcUtilGcTimeGct                       | GC 时间_FGCT                          | s        | 垃圾回收时间消耗                        | host4hivehiveserver2、<br/>id4hivehiveserver2 |
| HiveH2GcUtilGcTimeYgct                      | GC 时间_YGCT                          | s        | Young GC 消耗时间                       | host4hivehiveserver2、<br/>id4hivehiveserver2 |
| HiveH2GcUtilMemoryS0                        | 内存区域占比_S0                      | %        | Survivor 0区内存使用占比                | host4hivehiveserver2、<br/>id4hivehiveserver2 |
| HiveH2GcUtilMemoryE                         | 内存区域占比_E                       | %        | Eden 区内存使用占比                     | host4hivehiveserver2、<br/>id4hivehiveserver2 |
| HiveH2GcUtilMemoryCcs                       | 内存区域占比_CCS                     | %        | Compressed class space 区内存使用占比   | host4hivehiveserver2、<br/>id4hivehiveserver2 |
| HiveH2GcUtilMemoryS1                        | 内存区域占比_S1                      | %        | Survivor 1区内存使用占比                | host4hivehiveserver2、<br/>id4hivehiveserver2 |
| HiveH2GcUtilMemoryO                        | 内存区域占比_O                       | %        | Old 区内存使用占比                      | host4hivehiveserver2、<br/>id4hivehiveserver2 |
| HiveH2GcUtilMemoryM                         | 内存区域占比_M                       | %        | Metaspace 区内存使用占比                | host4hivehiveserver2、<br/>id4hivehiveserver2 |
| HiveH2JvmMemMem<br> nonheapusedm            | JVM 内存_MemNonHeapUsedM              | MB       | JVM 当前已经使用的 NonHeapMemory 的数量 | host4hivehiveserver2、<br/>id4hivehiveserver2 |
| HiveH2JvmMemMem<br> nonheapcommittedm       | JVM 内存_MemNonHeapCommittedM         | MB       | JVM 当前已经提交的 NonHeapMemory 的数量 | host4hivehiveserver2、<br/>id4hivehiveserver2 |
| HiveH2JvmMemMem<br> heapusedm               | JVM 内存_MemHeapUsedM                 | MB       | JVM 当前已经使用的 HeapMemory 的数量    | host4hivehiveserver2、<br/>id4hivehiveserver2 |
| HiveH2JvmMemMem<br> heapcommittedm          | JVM 内存_MemHeapCommittedM            | MB       | JVM 当前已经提交的 HeapMemory 的数量    | host4hivehiveserver2、<br/>id4hivehiveserver2 |
| HiveH2JvmMemMem<br> heapmaxm                | JVM 内存_MemHeapMaxM                  | MB       | JVM 配置的 HeapMemory 的数量            | host4hivehiveserver2、<br/>id4hivehiveserver2 |
| HiveH2JvmMemMem<br> heapinitm               | JVM 内存_MemHeapInitM                 | MB       | JVM 初始 HeapMem 的数量                 | host4hivehiveserver2、<br/>id4hivehiveserver2 |
| HiveH2JvmMemMem<br> nonheapinitm            | JVM 内存_MemNonHeapInitM              | MB       | JVM 初始 NonHeapMem 的数量              | host4hivehiveserver2、<br/>id4hivehiveserver2 |
| HiveH2OsCpuLoad<br>Processcpuload           | CPU 利用率_ProcessCpuLoad             | %        | CPU 利用率                              | host4hivehiveserver2、<br/>id4hivehiveserver2 |
| HiveH2OsFdCount<br>Maxfiledescriptorcount   | 文件描述符数_MaxFileDescriptorCount  | 个       | 最大文件描述符数                        | host4hivehiveserver2、<br/>id4hivehiveserver2 |
| HiveH2OsFdCount<br> Openfiledescriptorcount | 文件描述符数_OpenFileDescriptorCount | 个       | 已打开文件描述符数                      | host4hivehiveserver2、<br/>id4hivehiveserver2 |
| HiveH2OsCpuTime<br>Processcputime           | CPU 累计使用时间_ProcessCpuTime       | ms       | CPU 累计使用时间                        | host4hivehiveserver2、<br/>id4hivehiveserver2 |
| HiveH2RtUptimeUptime                        | 进程运行时长_Uptime                  | s        | 进程运行时长                            | host4hivehiveserver2、<br/>id4hivehiveserver2 |
| HiveH2ThreadCount<br>Daemonthreadcount      | 工作线程数_DaemonThreadCount         | 个       | Daemon 线程数                           | host4hivehiveserver2、<br/>id4hivehiveserver2 |
| HiveH2ThreadCount<br>Threadcount            | 工作线程数_ThreadCount               | 个       | 总线程数                                | host4hivehiveserver2、<br/>id4hivehiveserver2 |

### HIVE-HiveWebHcat

| 指标英文名             | 指标名称 | 指标中文名       | 指标单位 | 指标含义                              | 维度                                          |
| ---------------------- | -------- | ---------------- | -------- | ------------------------------------- | --------------------------------------------- |
| HiveHcGcUtilGcCountYgc | YGC      | GC 次数\_YGC       | 次       | Young GC 次数                         | host4hivehivewebhcat、<br>id4hivehivewebhcat  |
| HiveHcGcUtilGcCountFgc | FGC      | GC 次数_FGC       | 次       | Full GC 次数                          | host4hivehivewebhcat、<br>id4hivehivewebhcat  |
| HiveHcGcUtilGcTimeFgct | FGCT     | GC 时间_FGCT      | s        | Full GC 消耗时间                      | host4hivehivewebhcat、<br>id4hivehivewebhcat  |
| HiveHcGcUtilGcTimeGct  | GCT      | GC 时间_FGCT      | s        | 垃圾回收时间消耗                      | host4hivehivewebhcat、<br/>id4hivehivewebhca  |
| HiveHcGcUtilGcTimeYgct | YGCT     | GC 时间_YGCT      | s        | Young GC 消耗时间                     | host4hivehivewebhcat、<br/>id4hivehivewebhca  |
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

