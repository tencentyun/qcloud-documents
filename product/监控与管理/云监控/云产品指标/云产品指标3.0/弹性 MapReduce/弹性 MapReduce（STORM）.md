

## 命名空间

Namespace=QCE/TXMR_STORM

## 监控指标

### Storm-Supervisor

| 指标英文名                                      | 指标中文名                         | 指标含义                                | 单位 | 维度                                     |
| ----------------------------------------------- | ---------------------------------- | --------------------------------------- | ---- | ---------------------------------------- |
| StormSupervisorGcUtilGcCountYgc                 | GC次数_YGC                         | Young GC 次数                           | 次   | host4stormsupervisor、id4stormsupervisor |
| StormSupervisorGcUtilGcCountFgc                 | GC次数_FGC                         | Full GC 次数                            | 次   | host4stormsupervisor、id4stormsupervisor |
| StormSupervisorGcUtilGcTimeFgct                 | GC时间_FGC                         | Full GC 消耗时间                        | s    | host4stormsupervisor、id4stormsupervisor |
| StormSupervisorGcUtilGcTimeGct                  | GC时间_GCT                         | 垃圾回收时间消耗                        | s    | host4stormsupervisor、id4stormsupervisor |
| StormSupervisorGcUtilGcTimeYgct                 | GC时间_YGCT                        | Young GC 消耗时间                       | s    | host4stormsupervisor、id4stormsupervisor |
| StormSupervisorGcUtilMemoryS0                   | 内存区域占比_S0                    | Survivor 0区内存使用占比                | %    | host4stormsupervisor、id4stormsupervisor |
| StormSupervisorGcUtilMemoryE                    | 内存区域占比_E                     | Eden 区内存使用占比                     | %    | host4stormsupervisor、id4stormsupervisor |
| StormSupervisorGcUtilMemoryCcs                  | 内存区域占比_CCS                   | Compressed class space 区内存使用占比   | %    | host4stormsupervisor、id4stormsupervisor |
| StormSupervisorGcUtilMemoryS1                   | 内存区域占比_S1                    | Survivor 1区内存使用占比                | %    | host4stormsupervisor、id4stormsupervisor |
| StormSupervisorGcUtilMemoryO                    | 内存区域占比_O                     | Old 区内存使用占比                      | %    | host4stormsupervisor、id4stormsupervisor |
| StormSupervisorGcUtilMemoryM                    | 内存区域占比_M                     | Metaspace 区内存使用占比                | %    | host4stormsupervisor、id4stormsupervisor |
| StormSupervisorJvmMemMemheapusedm               | JVM内存_MemMemHeapUsedM            | JVM 当前已经使用的 HeapMemory 的数量    | MB   | host4stormsupervisor、id4stormsupervisor |
| StormSupervisorJvmMemMemheapcommittedm          | JVM内存_MemHeapCommittedM          | JVM 已经提交的 HeapMemory 的数量        | MB   | host4stormsupervisor、id4stormsupervisor |
| StormSupervisorJvmMemMemheapmaxm                | JVM内存_MemHeapMaxM                | JVM 配置的 HeapMemory 的数量            | MB   | host4stormsupervisor、id4stormsupervisor |
| StormSupervisorJvmMemMemheapinitm               | JVM内存_MemHeapInitM               | JVM 初始 HeapMem 的数量                 | MB   | host4stormsupervisor、id4stormsupervisor |
| StormSupervisorJvmMemMemnonheapcommittedm       | JVM内存_MemNonHeapCommittedM       | JVM 当前已经提交的 NonHeapMemory 的数量 | MB   | host4stormsupervisor、id4stormsupervisor |
| StormSupervisorJvmMemMemnonheapinitm            | JVM内存_MemNonHeapInitM            | JVM 初始 NonHeapMem 的数量              | MB   | host4stormsupervisor、id4stormsupervisor |
| StormSupervisorJvmMemMemnonheapusedm            | JVM内存_MemNonHeapUsedM            | JVM 当前已经使用的 NonHeapMemory 的数量 | MB   | host4stormsupervisor、id4stormsupervisor |
| StormSupervisorOsFdCountOpenfiledescriptorcount | 文件句柄数_OpenFileDescriptorCount | 已打开文件描述符数量                    | 个   | host4stormsupervisor、id4stormsupervisor |
| StormSupervisorOsFdCountMaxfiledescriptorcount  | 文件句柄数_MaxFileDescriptorCount  | 最大文件描述符数                        | 个   | host4stormsupervisor、id4stormsupervisor |
| StormSupervisorOsCpuLoadProcesscpuload          | CPU利用率_ProcessCpuLoad           | 进程 CPU 利用率                         | %    | host4stormsupervisor、id4stormsupervisor |
| StormSupervisorThreadCountDaemonthreadcount     | 工作线程数_DaemonThreadCount       | 守护线程数                              | 个   | host4stormsupervisor、id4stormsupervisor |
| StormSupervisorThreadCountThreadcount           | 工作线程数_ThreadCount             | 峰值线程数量                            | 个   | host4stormsupervisor、id4stormsupervisor |
| StormSupervisorOsCpuTimeProcesscputime          | CPU使用时间_ProcessCpuTime         | 线程总数                                | 个   | host4stormsupervisor、id4stormsupervisor |
| StormSupervisorRtUptimeUptime                   | 进程运行时间_Uptime                | CPU 累计使用时间                        | ms   | host4stormsupervisor、id4stormsupervisor |
| StormSupervisorThreadCountPeakthreadcount       | 工作线程数_PeakThreadCount         | 进程运行时长                            | s    | host4stormsupervisor、id4stormsupervisor |

### Storm-Nimbus

| 指标英文名                                  | 指标中文名                         | 指标含义                                | 单位 | 维度                             |
| ------------------------------------------- | ---------------------------------- | --------------------------------------- | ---- | -------------------------------- |
| StormNimbusGcUtilGcCountYgc                 | GC次数_YGC                         | Young GC 次数                           | 次   | host4stormnimbus、id4stormnimbus |
| StormNimbusGcUtilGcCountFgc                 | GC次数_FGC                         | Full GC 次数                            | 次   | host4stormnimbus、id4stormnimbus |
| StormNimbusGcUtilGcTimeFgct                 | GC时间_FGC                         | Full GC 消耗时间                        | s    | host4stormnimbus、id4stormnimbus |
| StormNimbusGcUtilGcTimeGct                  | GC时间_GCT                         | 垃圾回收时间消耗                        | s    | host4stormnimbus、id4stormnimbus |
| StormNimbusGcUtilGcTimeYgct                 | GC时间_YGCT                        | Young GC 消耗时间                       | s    | host4stormnimbus、id4stormnimbus |
| StormNimbusGcUtilMemoryS0                   | 内存区域占比_S0                    | Survivor 0区内存使用占比                | %    | host4stormnimbus、id4stormnimbus |
| StormNimbusGcUtilMemoryE                    | 内存区域占比_E                     | Eden 区内存使用占比                     | %    | host4stormnimbus、id4stormnimbus |
| StormNimbusGcUtilMemoryCcs                  | 内存区域占比_CCS                   | Compressed class space 区内存使用占比   | %    | host4stormnimbus、id4stormnimbus |
| StormNimbusGcUtilMemoryS1                   | 内存区域占比_S1                    | Survivor 1区内存使用占比                | %    | host4stormnimbus、id4stormnimbus |
| StormNimbusGcUtilMemoryO                    | 内存区域占比_O                     | Old 区内存使用占比                      | %    | host4stormnimbus、id4stormnimbus |
| StormNimbusGcUtilMemoryM                    | 内存区域占比_M                     | Metaspace 区内存使用占比                | %    | host4stormnimbus、id4stormnimbus |
| StormNimbusJvmMemMemheapusedm               | JVM内存_MemMemHeapUsedM            | JVM 当前已经使用的 HeapMemory 的数量    | MB   | host4stormnimbus、id4stormnimbus |
| StormNimbusJvmMemMemheapcommittedm          | JVM内存_MemHeapCommittedM          | JVM 已经提交的 HeapMemory 的数量        | MB   | host4stormnimbus、id4stormnimbus |
| StormNimbusJvmMemMemheapmaxm                | JVM内存_MemHeapMaxM                | JVM 配置的 HeapMemory 的数量            | MB   | host4stormnimbus、id4stormnimbus |
| StormNimbusJvmMemMemheapinitm               | JVM内存_MemHeapInitM               | JVM 初始 HeapMem 的数量                 | MB   | host4stormnimbus、id4stormnimbus |
| StormNimbusJvmMemMemnonheapusedm            | JVM内存_MemNonHeapUsedM            | JVM 当前已经提交的 NonHeapMemory 的数量 | MB   | host4stormnimbus、id4stormnimbus |
| StormNimbusJvmMemMemnonheapcommittedm       | JVM内存_MemNonHeapCommittedM       | JVM 初始 NonHeapMem 的数量              | MB   | host4stormnimbus、id4stormnimbus |
| StormNimbusJvmMemMemnonheapinitm            | JVM内存_MemNonHeapInitM            | JVM 当前已经使用的 NonHeapMemory 的数量 | MB   | host4stormnimbus、id4stormnimbus |
| StormNimbusOsFdCountOpenfiledescriptorcount | 文件句柄数_OpenFileDescriptorCount | 已打开文件描述符数量                    | 个   | host4stormnimbus、id4stormnimbus |
| StormNimbusOsFdCountMaxfiledescriptorcount  | 文件句柄数_MaxFileDescriptorCount  | 最大文件描述符数                        | 个   | host4stormnimbus、id4stormnimbus |
| StormNimbusOsCpuLoadProcesscpuload          | CPU利用率_ProcessCpuLoad           | 进程 CPU 利用率                         | %    | host4stormnimbus、id4stormnimbus |
| StormNimbusThreadCountDaemonthreadcount     | 工作线程数_DaemonThreadCount       | 守护线程数                              | 个   | host4stormnimbus、id4stormnimbus |
| StormNimbusThreadCountPeackthreadcount      | 工作线程数_PeakThreadCount         | 峰值线程数量                            | 个   | host4stormnimbus、id4stormnimbus |
| StormNimbusThreadCountThreadcount           | 工作线程数_ThreadCount             | 线程总数                                | 个   | host4stormnimbus、id4stormnimbus |
| StormNimbusOsCpuTimeProcesscputime          | CPU使用时间_ProcessCpuTime         | CPU 累计使用时间                        | ms   | host4stormnimbus、id4stormnimbus |
| StormNimbusRtUptimeUptime                   | 进程运行时间_Uptime                | 进程运行时长                            | s    | host4stormnimbus、id4stormnimbus |



## 各维度对应参数总览

| 参数名称                       | 维度名称             | 维度解释                     | 格式                                                         |
| :----------------------------- | :------------------- | :--------------------------- | :----------------------------------------------------------- |
| Instances.N.Dimensions.0.Name  | host4stormsupervisor | EMR 实例中节点 IP 的维度名称 | 输入 String 类型维度名称：host4stormsupervisor               |
| Instances.N.Dimensions.0.Value | host4stormsupervisor | EMR 实例中具体节点 IP        | 输入具体节点 IP ，可从控制台获取，登录 [腾讯云 MapReduce 控制台](https://console.cloud.tencent.com/emr)，单击**实例 > 集群资源 > 资源管理 > 节点内网 IP**。也可通过 [查询节点信息](https://cloud.tencent.com/document/product/589/41707) API 获取。 |
| Instances.N.Dimensions.0.Name  | id4stormsupervisor   | EMR 实例 ID 的维度名称       | 输入 String 类型维度名称：id4stormsupervisor                 |
| Instances.N.Dimensions.0.Value | id4stormsupervisor   | EMR 实例具体 ID              | 输入 EMR 具体实例 ID，例如：emr-mm8bs222                     |
| Instances.N.Dimensions.0.Name  | host4stormnimbus     | EMR 实例中节点 IP 的维度名称 | 输入 String 类型维度名称：host4stormnimbus                   |
| Instances.N.Dimensions.0.Value | host4stormnimbus     | EMR 实例中具体节点 IP        | 输入具体节点 IP，可从控制台获取，登录 [腾讯云 MapReduce 控制台](https://console.cloud.tencent.com/emr)，单击**实例 > 集群资源 > 资源管理 > 节点内网 IP**。也可通过 [查询节点信息](https://cloud.tencent.com/document/product/589/41707) API 获取。 |
| Instances.N.Dimensions.0.Name  | id4stormnimbus       | EMR 实例 ID 的维度名称       | 输入 String 类型维度名称：id4stormnimbus                     |
| Instances.N.Dimensions.0.Value | id4stormnimbus       | EMR 实例具体 ID              | 输入 EMR 具体实例 ID，例如：emr-mm8bs222                     |



## 入参说明

**查询弹性 MapReduce（STORM）监控数据，入参取值如下：**

Namespace=QCE/TXMR_STORM
&Instances.N.Dimensions.1.Name=id4alluxiooverview
&Instances.N.Dimensions.1.Value=EMR 实例具体 ID



**查询弹性 MapReduce（STORM）监控数据，入参取值如下：**

Namespace=QCE/TXMR_STORM
&Instances.N.Dimensions.0.Name=host4stormnimbus
&Instances.N.Dimensions.0.Value=EMR 实例中具体节点 IP
&Instances.N.Dimensions.1.Name=id4stormnimbus
&Instances.N.Dimensions.1.Value=EMR 实例具体 ID

