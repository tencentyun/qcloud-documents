## 命名空间

Namespace=QCE/TXMR_KYLIN



## 监控指标

| 指标英文名                                 | 指标中文名                           | 指标含义                                | 单位 | 维度                           |
| ------------------------------------------ | ------------------------------------ | --------------------------------------- | ---- | ------------------------------ |
| KylinKylinGcUtilGcCountFgc                 | GC次数FGC                           | Full GC 次数                            | 次   | host4kylinkylin、id4kylinkylin |
| KylinKylinGcUtilGcCountYgc                 | GC次数YGC                           | Young GC 次数                           | 次   | host4kylinkylin、id4kylinkylin |
| KylinKylinGcUtilGcTimeFgct                 | GC时间FGCT                          | Full GC 消耗时间                        | s    | host4kylinkylin、id4kylinkylin |
| KylinKylinGcUtilGcTimeGct                  | GC时间GCT                           | 垃圾回收时间消耗                        | s    | host4kylinkylin、id4kylinkylin |
| KylinKylinGcUtilGcTimeYgct                 | GC时间YGCT                          | Young GC 消耗时间                       | s    | host4kylinkylin、id4kylinkylin |
| KylinKylinGcUtilMemoryCcs                  | 内存区域占比CCS                     | Compressed class space 区内存使用占比   | %    | host4kylinkylin、id4kylinkylin |
| KylinKylinGcUtilMemoryE                    | 内存区域占比E                       | Eden 区内存使用占比                     | %    | host4kylinkylin、id4kylinkylin |
| KylinKylinGcUtilMemoryM                    | 内存区域占比M                       | Metaspace 区内存使用占比                | %    | host4kylinkylin、id4kylinkylin |
| KylinKylinGcUtilMemoryO                    | 内存区域占比O                       | Old 区内存使用占比                      | %    | host4kylinkylin、id4kylinkylin |
| KylinKylinGcUtilMemoryS0                   | 内存区域占比S0                      | Survivor 0区内存使用占比                | %    | host4kylinkylin、id4kylinkylin |
| KylinKylinGcUtilMemoryS1                   | 内存区域占比S1                      | Survivor 1区内存使用占比                | %    | host4kylinkylin、id4kylinkylin |
| KylinKylinJvmMemMemheapcommittedm          | JVM内存MemHeapCommittedM            | JVM 已经提交的 HeapMemory 的数量        | MB   | host4kylinkylin、id4kylinkylin |
| KylinKylinJvmMemMemheapinitm               | JVM内存MemHeapInitM                 | JVM 初始 HeapMem 的数量                 | MB   | host4kylinkylin、id4kylinkylin |
| KylinKylinJvmMemMemheapmaxm                | JVM内存MemHeapMaxM                  | JVM 配置的 HeapMemory 的数量            | MB   | host4kylinkylin、id4kylinkylin |
| KylinKylinJvmMemMemheapusedm               | JVM内存MemHeapUsedM                 | JVM 当前已经使用的 HeapMemory 的数量    | MB   | host4kylinkylin、id4kylinkylin |
| KylinKylinJvmMemMemnonheapcommittedm       | JVM内存MemNonHeapCommittedM         | JVM 当前已经提交的 NonHeapMemory 的数量 | MB   | host4kylinkylin、id4kylinkylin |
| KylinKylinJvmMemMemnonheapinitm            | JVM内存MemNonHeapInitM              | JVM 初始 NonHeapMem 的数量              | MB   | host4kylinkylin、id4kylinkylin |
| KylinKylinJvmMemMemnonheapusedm            | JVM内存MemNonHeapUsedM              | JVM 当前已经使用的 NonHeapMemory 的数量 | MB   | host4kylinkylin、id4kylinkylin |
| KylinKylinOsCpuLoadProcesscpuload          | CPU利用率ProcessCpuLoad             | 进程 CPU 利用率                         | %    | host4kylinkylin、id4kylinkylin |
| KylinKylinOsCpuTimeProcesscputime          | CPU累计使用时间ProcessCpuTime       | CPU累计使用时间                         | ms   | host4kylinkylin、id4kylinkylin |
| KylinKylinOsFdCountMaxfiledescriptorcount  | 文件描述符数MaxFileDescriptorCount  | 最大文件描述符数                        | 个   | host4kylinkylin、id4kylinkylin |
| KylinKylinOsFdCountOpenfiledescriptorcount | 文件描述符数OpenFileDescriptorCount | 已打开文件描述符数量                    | 个   | host4kylinkylin、id4kylinkylin |
| KylinKylinRtUptimeUptime                   | 进程运行时长Uptime                  | 进程运行时长                            | s    | host4kylinkylin、id4kylinkylin |
| KylinKylinThreadCountDaemonthreadcount     | 线程数量DaemonThreadCount           | 守护线程数                              | 个   | host4kylinkylin、id4kylinkylin |
| KylinKylinThreadCountPeakthreadcount       | 线程数量PeakThreadCount             | 峰值线程数量                            | 个   | host4kylinkylin、id4kylinkylin |
| KylinKylinThreadCountThreadcount           | 线程数量ThreadCount                 | 线程总数                                | 个   | host4kylinkylin、id4kylinkylin |
| KylinKylinOsCpuLoadSystemcpuload           | CPU利用率SystemCpuLoad              |                                         | %    | host4kylinkylin、id4kylinkylin |



## 各维度对应参数总览

| 参数名称                       | 维度名称        | 维度解释                     | 格式                                                         |
| :----------------------------- | :-------------- | :--------------------------- | :----------------------------------------------------------- |
| Instances.N.Dimensions.0.Name  | host4kylinkylin | EMR 实例中节点 IP 的维度名称 | 输入 String 类型维度名称：host4kylinkylin                    |
| Instances.N.Dimensions.0.Value | host4kylinkylin | EMR 实例中具体节点 IP        | 输入具体节点 IP ，可从控制台获取，登录 [腾讯云 MapReduce 控制台](https://console.cloud.tencent.com/emr)，单击**实例 > 集群资源 > 资源管理 > 节点内网 IP**。也可通过 [查询节点信息](https://cloud.tencent.com/document/product/589/41707) API 获取。 |
| Instances.N.Dimensions.0.Name  | id4kylinkylin   | EMR 实例 ID 的维度名称       | 输入 String 类型维度名称：id4kylinkylin                      |
| Instances.N.Dimensions.0.Value | id4kylinkylin   | EMR 实例具体 ID              | 输入 EMR 具体实例 ID，例如：emr-mm8bs222                     |



## 入参说明

**查询弹性 MapReduce（Kylin）监控数据，入参取值如下：**

Namespace=QCE/TXMR_KYLIN
&Instances.N.Dimensions.0.Name=host4kylinkylin
&Instances.N.Dimensions.0.Value=EMR 实例中具体节点 IP
&Instances.N.Dimensions.1.Name=id4kylinkylin
&Instances.N.Dimensions.1.Value=EMR 实例具体 ID

