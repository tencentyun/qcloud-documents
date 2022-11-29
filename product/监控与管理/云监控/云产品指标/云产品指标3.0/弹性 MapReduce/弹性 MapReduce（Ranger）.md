## 命名空间

Namespace=QCE/TXMR_RANGER



## 监控指标

### Ranger-Admin

| 指标英文名                                  | 指标中文名                           | 指标含义                                | 指标单位 | 维度                                         |
| ------------------------------------------- | ------------------------------------ | --------------------------------------- | -------- | -------------------------------------------- |
| RangerAdminGcUtilGcCountFgc                 | GC次数_FGC                           | Young GC 次数                           | 次       | host4rangerrangeradmin、id4rangerrangeradmin |
| RangerAdminGcUtilGcCountYgc                 | GC次数_YGC                           | Full GC 次数                            | 次       | host4rangerrangeradmin、id4rangerrangeradmin |
| RangerAdminGcUtilGcTimeFgct                 | GC时间_FGCT                          | Full GC 消耗时间                        | s        | host4rangerrangeradmin、id4rangerrangeradmin |
| RangerAdminGcUtilGcTimeGct                  | GC时间_GCT                           | 垃圾回收时间消耗                        | s        | host4rangerrangeradmin、id4rangerrangeradmin |
| RangerAdminGcUtilGcTimeYgct                 | GC时间_YGCT                          | Young GC 消耗时间                       | s        | host4rangerrangeradmin、id4rangerrangeradmin |
| RangerAdminGcUtilMemoryCcs                  | 内存区域占比_CCS                     | Compressed class space 区内存使用占比   | %        | host4rangerrangeradmin、id4rangerrangeradmin |
| RangerAdminGcUtilMemoryE                    | 内存区域占比_E                       | Eden 区内存使用占比                     | %        | host4rangerrangeradmin、id4rangerrangeradmin |
| RangerAdminGcUtilMemoryM                    | 内存区域占比_M                       | Metaspace 区内存使用占比                | %        | host4rangerrangeradmin、id4rangerrangeradmin |
| RangerAdminGcUtilMemoryO                    | 内存区域占比_O                       | Old 区内存使用占比                      | %        | host4rangerrangeradmin、id4rangerrangeradmin |
| RangerAdminGcUtilMemoryS0                   | 内存区域占比_S0                      | Survivor 0区内存使用占比                | %        | host4rangerrangeradmin、id4rangerrangeradmin |
| RangerAdminGcUtilMemoryS1                   | 内存区域占比_S1                      | Survivor 1区内存使用占比                | %        | host4rangerrangeradmin、id4rangerrangeradmin |
| RangerAdminJvmMemMemheapcommittedm          | JVM内存_MemHeapCommittedM            | JVM 已经提交的 HeapMemory 的数量        | MB       | host4rangerrangeradmin、id4rangerrangeradmin |
| RangerAdminJvmMemMemheapinitm               | JVM内存_MemHeapInitM                 | JVM 初始 HeapMem 的数量                 | MB       | host4rangerrangeradmin、id4rangerrangeradmin |
| RangerAdminJvmMemMemheapmaxm                | JVM内存_MemHeapMaxM                  | JVM 配置的 HeapMemory 的数量            | MB       | host4rangerrangeradmin、id4rangerrangeradmin |
| RangerAdminJvmMemMemheapusedm               | JVM内存_MemHeapUsedM                 | JVM 当前已经使用的 HeapMemory 的数量    | MB       | host4rangerrangeradmin、id4rangerrangeradmin |
| RangerAdminJvmMemMemnonheapcommittedm       | JVM内存_MemNonHeapCommittedM         | JVM 当前已经提交的 NonHeapMemory 的数量 | MB       | host4rangerrangeradmin、id4rangerrangeradmin |
| RangerAdminJvmMemMemnonheapinitm            | JVM内存_MemNonHeapInitM              | JVM 初始 NonHeapMem 的数量              | MB       | host4rangerrangeradmin、id4rangerrangeradmin |
| RangerAdminJvmMemMemnonheapusedm            | JVM内存_MemNonHeapUsedM              | JVM 当前已经使用的 NonHeapMemory 的数量 | MB       | host4rangerrangeradmin、id4rangerrangeradmin |
| RangerAdminOsCpuLoadProcesscpuload          | CPU利用率_ProcessCpuLoad             | CPU 利用率                              | %        | host4rangerrangeradmin、id4rangerrangeradmin |
| RangerAdminOsCpuTimeProcesscputime          | CPU累计使用时间_ProcessCpuTime       | CPU 累计使用时间                        | ms       | host4rangerrangeradmin、id4rangerrangeradmin |
| RangerAdminOsFdCountMaxfiledescriptorcount  | 文件描述符数_MaxFileDescriptorCount  | 最大文件描述符数                        | 个       | host4rangerrangeradmin、id4rangerrangeradmin |
| RangerAdminOsFdCountOpenfiledescriptorcount | 文件描述符数_OpenFileDescriptorCount | 已打开文件描述符数                      | 个       | host4rangerrangeradmin、id4rangerrangeradmin |
| RangerAdminRtUptimeUptime                   | 进程运行时长_Uptime                  | 进程运行时长                            | s        | host4rangerrangeradmin、id4rangerrangeradmin |
| RangerAdminTdCountDaemonthreadcount         | 线程数量_DaemonThreadCount           | 后台线程数量                            | 个       | host4rangerrangeradmin、id4rangerrangeradmin |
| RangerAdminTdCountPeakthreadcount           | 线程数量_PeakThreadCount             | 峰值线程数量                            | 个       | host4rangerrangeradmin、id4rangerrangeradmin |
| RangerAdminTdCountThreadcount               | 线程数量_ThreadCount                 | 线程数量                                | 个       | host4rangerrangeradmin、id4rangerrangeradmin |

###  Ranger-UserSync

| 指标英文名                                     | 指标中文名                           | 指标含义                                | 指标单位 | 维度                                               |
| ---------------------------------------------- | ------------------------------------ | --------------------------------------- | -------- | -------------------------------------------------- |
| RangerUsersyncJvmMemMemnonheapinitm            | JVM内存_MemNonHeapInitM              | Young GC 次数                           | MB       | host4rangerrangerusersync、id4rangerrangerusersync |
| RangerUsersyncJvmMemMemnonheapusedm            | JVM内存_MemNonHeapUsedM              | Full GC 次数                            | MB       | host4rangerrangerusersync、id4rangerrangerusersync |
| RangerUsersyncOsCpuLoadProcesscpuload          | CPU利用率_ProcessCpuLoad             | Full GC 消耗时间                        | %        | host4rangerrangerusersync、id4rangerrangerusersync |
| RangerUsersyncOsCpuTimeProcesscputime          | CPU累计使用时间_ProcessCpuTime       | 垃圾回收时间消耗                        | ms       | host4rangerrangerusersync、id4rangerrangerusersync |
| RangerUsersyncOsFdCountMaxfiledescriptorcount  | 文件描述符数_MaxFileDescriptorCount  | Young GC 消耗时间                       | 个       | host4rangerrangerusersync、id4rangerrangerusersync |
| RangerUsersyncOsFdCountOpenfiledescriptorcount | 文件描述符数_OpenFileDescriptorCount | Compressed class space 区内存使用占比   | 个       | host4rangerrangerusersync、id4rangerrangerusersync |
| RangerUsersyncRtUptimeUptime                   | 进程运行时长_Uptime                  | Eden 区内存使用占比                     | s        | host4rangerrangerusersync、id4rangerrangerusersync |
| RangerUsersyncTdCountDaemonthreadcount         | 线程数量_DaemonThreadCount           | Metaspace 区内存使用占比                | 个       | host4rangerrangerusersync、id4rangerrangerusersync |
| RangerUsersyncTdCountPeakthreadcount           | 线程数量_PeakThreadCount             | Old 区内存使用占比                      | 个       | host4rangerrangerusersync、id4rangerrangerusersync |
| RangerUsersyncTdCountThreadcount               | 线程数量_ThreadCount                 | Survivor 0区内存使用占比                | 个       | host4rangerrangerusersync、id4rangerrangerusersync |
| RangerUsersyncGcUtilGcCountFgc                 | GC次数_FGC                           | Survivor 1区内存使用占比                | 次       | host4rangerrangerusersync、id4rangerrangerusersync |
| RangerUsersyncGcUtilGcCountYgc                 | GC次数_YGC                           | JVM 已经提交的 HeapMemory 的数量        | 次       | host4rangerrangerusersync、id4rangerrangerusersync |
| RangerUsersyncGcUtilGcTimeFgct                 | GC时间_FGCT                          | JVM 初始 HeapMem 的数量                 | s        | host4rangerrangerusersync、id4rangerrangerusersync |
| RangerUsersyncGcUtilGcTimeGct                  | GC时间_GCT                           | JVM 配置的 HeapMemory 的数量            | s        | host4rangerrangerusersync、id4rangerrangerusersync |
| RangerUsersyncGcUtilGcTimeYgct                 | GC时间_YGCT                          | JVM 当前已经使用的 HeapMemory 的数量    | s        | host4rangerrangerusersync、id4rangerrangerusersync |
| RangerUsersyncGcUtilMemoryCcs                  | 内存区域占比_CCS                     | JVM 当前已经提交的 NonHeapMemory 的数量 | %        | host4rangerrangerusersync、id4rangerrangerusersync |
| RangerUsersyncGcUtilMemoryE                    | 内存区域占比_E                       | JVM 初始 NonHeapMem 的数量              | %        | host4rangerrangerusersync、id4rangerrangerusersync |
| RangerUsersyncGcUtilMemoryM                    | 内存区域占比_M                       | JVM 当前已经使用的 NonHeapMemory 的数量 | %        | host4rangerrangerusersync、id4rangerrangerusersync |
| RangerUsersyncGcUtilMemoryO                    | 内存区域占比_O                       | CPU 利用率                              | %        | host4rangerrangerusersync、id4rangerrangerusersync |
| RangerUsersyncGcUtilMemoryS0                   | 内存区域占比_S0                      | CPU 累计使用时间                        | %        | host4rangerrangerusersync、id4rangerrangerusersync |
| RangerUsersyncGcUtilMemoryS1                   | 内存区域占比_S1                      | 最大文件描述符数                        | %        | host4rangerrangerusersync、id4rangerrangerusersync |
| RangerUsersyncJvmMemMemheapcommittedm          | JVM内存_MemHeapCommittedM            | 已打开文件描述符数                      | MB       | host4rangerrangerusersync、id4rangerrangerusersync |
| RangerUsersyncJvmMemMemheapinitm               | JVM内存_MemHeapInitM                 | 进程运行时长                            | MB       | host4rangerrangerusersync、id4rangerrangerusersync |
| RangerUsersyncJvmMemMemheapmaxm                | JVM内存_MemHeapMaxM                  | 后台线程数量                            | MB       | host4rangerrangerusersync、id4rangerrangerusersync |
| RangerUsersyncJvmMemMemheapusedm               | JVM内存_MemHeapUsedM                 | 峰值线程数量                            | MB       | host4rangerrangerusersync、id4rangerrangerusersync |
| RangerUsersyncJvmMemMemnonheapcommittedm       | JVM内存_MemNonHeapCommittedM         | 线程数量                                | MB       | host4rangerrangerusersync、id4rangerrangerusersync |



## 各维度对应参数总览

| 参数名称                       | 维度名称                  | 维度解释                     | 格式                                                         |
| :----------------------------- | :------------------------ | :--------------------------- | :----------------------------------------------------------- |
| Instances.N.Dimensions.0.Name  | host4rangerrangeradmin    | EMR 实例中节点 IP 的维度名称 | 输入 String 类型维度名称：host4rangerrangeradmin             |
| Instances.N.Dimensions.0.Value | host4rangerrangeradmin    | EMR 实例中具体节点 IP        | 输入具体节点 IP ，可从控制台获取，登录 [腾讯云 MapReduce 控制台](https://console.cloud.tencent.com/emr)，单击**实例 > 集群资源 > 资源管理 > 节点内网 IP**。也可通过 [查询节点信息](https://cloud.tencent.com/document/product/589/41707) API 获取。 |
| Instances.N.Dimensions.0.Name  | id4rangerrangeradmin      | EMR 实例 ID 的维度名称       | 输入 String 类型维度名称：id4rangerrangeradmin               |
| Instances.N.Dimensions.0.Value | id4rangerrangeradmin      | EMR 实例具体 ID              | 输入 EMR 具体实例 ID，例如：emr-mm8bs222                     |
| Instances.N.Dimensions.0.Name  | host4rangerrangerusersync | EMR 实例中节点 IP 的维度名称 | 输入 String 类型维度名称：host4rangerrangerusersync          |
| Instances.N.Dimensions.0.Value | host4rangerrangerusersync | EMR 实例中具体节点 IP        | 输入具体节点 IP ，可从控制台获取，登录 [腾讯云 MapReduce 控制台](https://console.cloud.tencent.com/emr)，单击**实例 > 集群资源 > 资源管理 > 节点内网 IP**。也可通过 [查询节点信息](https://cloud.tencent.com/document/product/589/41707) API 获取。 |
| Instances.N.Dimensions.0.Name  | id4rangerrangerusersync   | EMR 实例 ID 的维度名称       | 输入 String 类型维度名称：id4rangerrangerusersync            |
| Instances.N.Dimensions.0.Value | id4rangerrangerusersync   | EMR 实例具体 ID              | 输入 EMR 具体实例 ID，例如：emr-mm8bs222                     |



## 入参说明

**查询弹性 MapReduce（Ranger-Admin）监控数据，入参取值如下：**

Namespace=QCE/TXMR_RANGER
&Instances.N.Dimensions.0.Name=host4rangerrangeradmin
&Instances.N.Dimensions.0.Value=EMR 实例中具体节点 IP
&Instances.N.Dimensions.1.Name=id4trinotrinoworker
&Instances.N.Dimensions.1.Value=EMR 实例具体 ID



**查询弹性 MapReduce（Ranger-UserSync）监控数据，入参取值如下：**

Namespace=QCE/TXMR_RANGER
&Instances.N.Dimensions.0.Name=host4rangerrangerusersync
&Instances.N.Dimensions.0.Value=EMR 实例中具体节点 IP
&Instances.N.Dimensions.1.Name=id4rangerrangerusersync
&Instances.N.Dimensions.1.Value=EMR 实例具体 ID


