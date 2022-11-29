## 命名空间

Namespace=QCE/TXMR_LIVY

## 监控指标

| 指标英文名                                     | 指标中文名                         | 指标含义                                | 单位 | 维度                                   |
| ---------------------------------------------- | ---------------------------------- | --------------------------------------- | ---- | -------------------------------------- |
| LivyLivyserverGcUtilGcCountYgc                 | GC次数_YGC                         | Young GC 次数                           | 次   | host4livylivyserver、id4livylivyserver |
| LivyLivyserverGcUtilGcCountFgc                 | GC次数_FGC                         | Full GC 次数                            | 次   | host4livylivyserver、id4livylivyserver |
| LivyLivyserverGcUtilGcTimeFgct                 | GC时间_FGC                         | Full GC 消耗时间                        | s    | host4livylivyserver、id4livylivyserver |
| LivyLivyserverGcUtilGcTimeGct                  | GC时间_GCT                         | 垃圾回收时间消耗                        | s    | host4livylivyserver、id4livylivyserver |
| LivyLivyserverGcUtilGcTimeYgct                 | GC时间_YGCT                        | Young GC 消耗时间                       | s    | host4livylivyserver、id4livylivyserver |
| LivyLivyserverGcUtilMemoryS0                   | 内存区域占比_S0                    | Survivor 0区内存使用占比                | %    | host4livylivyserver、id4livylivyserver |
| LivyLivyserverGcUtilMemoryE                    | 内存区域占比_E                     | Eden 区内存使用占比                     | %    | host4livylivyserver、id4livylivyserver |
| LivyLivyserverGcUtilMemoryCcs                  | 内存区域占比_CCS                   | Compressed class space 区内存使用占比   | %    | host4livylivyserver、id4livylivyserver |
| LivyLivyserverGcUtilMemoryS1                   | 内存区域占比_S1                    | Survivor 1区内存使用占比                | %    | host4livylivyserver、id4livylivyserver |
| LivyLivyserverGcUtilMemoryO                    | 内存区域占比_O                     | Old 区内存使用占比                      | %    | host4livylivyserver、id4livylivyserver |
| LivyLivyserverGcUtilMemoryM                    | 内存区域占比_M                     | Metaspace 区内存使用占比                | %    | host4livylivyserver、id4livylivyserver |
| LivyLivyserverJvmMemMemheapusedm               | JVM内存_MemMemHeapUsedM            | JVM 当前已经使用的 HeapMemory 的数量    | MB   | host4livylivyserver、id4livylivyserver |
| LivyLivyserverJvmMemMemheapcommittedm          | JVM内存_MemHeapCommittedM          | JVM 已经提交的 HeapMemory 的数量        | MB   | host4livylivyserver、id4livylivyserver |
| LivyLivyserverJvmMemMemheapmaxm                | JVM内存_MemHeapMaxM                | JVM 配置的 HeapMemory 的数量            | MB   | host4livylivyserver、id4livylivyserver |
| LivyLivyserverJvmMemMemheapinitm               | JVM内存_MemHeapInitM               | JVM 初始 HeapMem 的数量                 | MB   | host4livylivyserver、id4livylivyserver |
| LivyLivyserverJvmMemMemnonheapcommittedm       | JVM内存_MemNonHeapCommittedM       | JVM 当前已经提交的 NonHeapMemory 的数量 | MB   | host4livylivyserver、id4livylivyserver |
| LivyLivyserverJvmMemMemnonheapinitm            | JVM内存_MemNonHeapInitM            | JVM 初始 NonHeapMem 的数量              | MB   | host4livylivyserver、id4livylivyserver |
| LivyLivyserverJvmMemMemnonheapusedm            | JVM内存_MemNonHeapUsedM            | JVM 当前已经使用的 NonHeapMemory 的数量 | MB   | host4livylivyserver、id4livylivyserver |
| LivyLivyserverOsFdCountOpenfiledescriptorcount | 文件句柄数_OpenFileDescriptorCount | 已打开文件描述符数量                    | 个   | host4livylivyserver、id4livylivyserver |
| LivyLivyserverOsFdCountMaxfiledescriptorcount  | 文件句柄数_MaxFileDescriptorCount  | 最大文件描述符数                        | 个   | host4livylivyserver、id4livylivyserver |
| LivyLivyserverOsCpuLoadProcesscpuload          | CPU利用率_ProcessCpuLoad           | 进程 CPU 利用率                         | %    | host4livylivyserver、id4livylivyserver |
| LivyLivyserverThreadCountDaemonthreadcount     | 工作线程数_DaemonThreadCount       | 守护线程数                              | 个   | host4livylivyserver、id4livylivyserver |
| LivyLivyserverThreadCountPeakthreadcount       | 工作线程数_PeakThreadCount         | 峰值线程数量                            | 个   | host4livylivyserver、id4livylivyserver |
| LivyLivyserverThreadCountThreadcount           | 工作线程数_ThreadCount             | 线程总数                                | 个   | host4livylivyserver、id4livylivyserver |
| LivyLivyserverOsCpuTimeProcesscputime          | CPU使用时间_ProcessCpuTime         | CPU 累计使用时间                        | ms   | host4livylivyserver、id4livylivyserver |
| LivyLivyserverRtUptimeUptime                   | 进程运行时间_Uptime                | 进程运行时长                            | s    | host4livylivyserver、id4livylivyserver |

###  



## 各维度对应参数总览

| 参数名称                       | 维度名称            | 维度解释                     | 格式                                                         |
| :----------------------------- | :------------------ | :--------------------------- | :----------------------------------------------------------- |
| Instances.N.Dimensions.0.Name  | host4livylivyserver | EMR 实例中节点 IP 的维度名称 | 输入 String 类型维度名称：host4livylivyserver                |
| Instances.N.Dimensions.0.Value | host4livylivyserver | EMR 实例中具体节点 IP        | 输入具体节点 IP ，可从控制台获取，登录 [腾讯云 MapReduce 控制台](https://console.cloud.tencent.com/emr)，单击**实例 > 集群资源 > 资源管理 > 节点内网 IP**。也可通过 [查询节点信息](https://cloud.tencent.com/document/product/589/41707) API 获取。 |
| Instances.N.Dimensions.0.Name  | id4livylivyserver   | EMR 实例 ID 的维度名称       | 输入 String 类型维度名称：id4livylivyserver                  |
| Instances.N.Dimensions.0.Value | id4livylivyserver   | EMR 实例具体 ID              | 输入 EMR 具体实例 ID，例如：emr-mm8bs222                     |



## 入参说明

**查询弹性 MapReduce（LIVY）监控数据，入参取值如下：**

Namespace=QCE/TXMR_LIVY
&Instances.N.Dimensions.0.Name=host4livylivyserver
&Instances.N.Dimensions.0.Value=EMR 实例中具体节点 IP
&Instances.N.Dimensions.1.Name=id4livylivyserver
&Instances.N.Dimensions.1.Value=EMR 实例具体 ID







