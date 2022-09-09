腾讯云提供下列Doris Broker服务的监控项。Broker服务可部署在 FE 或 BE 节点上，因此在腾讯云集群监控页面，Broker的监控项也分是在BE指标和FE指标 Tab 页内。不论部署在哪种节点上，由于都是Broker服务，相关的监控项都一致。

![](https://qcloudimg.tencent-cloud.cn/raw/a417df8e759d82d14b55768fd18ba8ae.png)

Broker 监控项总体分为两类：
1. BROKER_JSTAT: Broker GC相关的监控数据。
2. BROKER_JVM: Broker 内存使用数据、cpu相关数据及线程相关数据。


|指标名称|前台标题|指标Tag名称|单位|指标含义|英文指标含义|统计方法|
|-------|-------|-------|-------|-------|-------|-------|
|DORIS.BK.GC_UTIL_GC_COUNT|GC次数|YGC|次|Young GC 次数|Number of young generation GC events|数据来源 jstat -gcutil pid 命令YGC一栏，表示Young GC 次数|
|||FGC|次|Full GC 次数|Number of full GC events|数据来源 jstat -gcutil pid 命令FGC一栏，表示Full GC 次数|
|DORIS.BK.GC_UTIL_GC_TIME|GC时间|FGCT|秒|Full GC 消耗时间|Full garbage collection time|数据来源 jstat -gcutil pid 命令FGCT一栏，表示Full GC 消耗时间|
|||GCT|秒|垃圾回收时间消耗|Total garbage collection time|数据来源 jstat -gcutil pid 命令GCT一栏，表示垃圾回收时间消耗|
|||YGCT|秒|Young GC 消耗时间|Young generation garbage collection time|数据来源 jstat -gcutil pid 命令YGCT一栏，表示Young GC 消耗时间|
|DORIS.BK.GC_UTIL_MEMORY|内存区域占比|S0|%|Survivor 0区内存使用占比|The percentage of survivor 0 space memory usage|数据来源 jstat -gcutil pid 命令S0一栏，表示Survivor 0区内存使用占比|
|||E|%|Eden 区内存使用占比|The percentage of Eden space memory usage|数据来源 jstat -gcutil pid 命令E一栏，表示Eden 区内存使用占比|
|||CCS|%|Compressed class space 区内存使用占比|The percentage of Compressed class space memory usage|数据来源 jstat -gcutil pid 命令CCS一栏，表示Compressed class space 区内存使用占比|
|||S1|%|Survivor 1区内存使用占比|The percentage of Survivor 1 space memory usage|数据来源 jstat -gcutil pid 命令S1一栏，表示Survivor 1区内存使用占比|
|||O|%|Old 区内存使用占比|The percentage of Old space memory usage|数据来源 jstat -gcutil pid 命令O一栏，表示Old 区内存使用占比|
|||M|%|Metaspace 区内存使用占比|Metaspace utilization as a percentage of the space's current capacity|数据来源 jstat -gcutil pid 命令M一栏，表示Metaspace 区内存使用占比|
|DORIS.BK.JVM.MEM|JVM内存|MemNonHeapUsedM|MB|JVM 当前已经使用的 NonHeapMemory 的数量|Used JVM NonHeapMemory size|数据来源 JMX JvmMetrics:MemNonHeapUsedM，表示JVM 当前已经使用的非堆内存|
|||MemNonHeapCommittedM|MB|JVM 当前已经提交的 NonHeapMemory 的数量|NonHeapCommittedM size that JVM is configured with|数据来源 JMX JvmMetrics:MemNonHeapCommittedM，表示JVM 当前已经提交的非堆内存|
|||MemHeapUsedM|MB|JVM 当前已经使用的 HeapMemory 的数量|Used JVM HeapMemory size|数据来源 JMX JvmMetrics:MemHeapUsedM，表示JVM 当前已经使用的堆内存|
|||MemHeapCommittedM|MB|JVM 当前已经提交的 HeapMemory 的数量|Submitted JVM HeapMemory|数据来源 JMX JvmMetrics:MemHeapCommittedM，表示JVM 当前已经提交的堆内存|
|||MemHeapMaxM|MB|JVM 配置的 HeapMemory 的数量|HeapMemory size that JVM is configured with|数据来源 JMX JvmMetrics:MemHeapMaxM，表示JVM 配置的 堆内存大小|
|||MemHeapInitM|MB|JVM 初始 HeapMemory的数量|Initial JVM HeapMem size|数据来源 JMX JvmMetrics:MemHeapInitM，表示JVM 初始堆内存大小|
|||MemNonHeapInitM|MB|JVM 初始 NonHeapMemory 的数量|Initial JVM NonHeapMem size|数据来源 JMX JvmMetrics:MemNonHeapInitM，表示JVM 初始非堆内存大小|
|DORIS.BK.OS.CPU.LOAD|cpu利用率|ProcessCpuLoad|%|CPU 利用率|CPU utilization|数据来源 JMX OperatingSystem:ProcessCpuLoad，表示CPU 利用率|
|DORIS.BK.OS.FD.COUNT|文件句柄数|MaxFileDescriptorCount|个|最大文件描述符数|Maximum number of file descriptors|数据来源 JMX OperatingSystem:MaxFileDescriptorCount，表示最大文件描述符数|
|||OpenFileDescriptorCount|个|已打开文件描述符数|Number of opened file descriptors|数据来源 JMX OperatingSystem:OpenFileDescriptorCount，表示已打开文件描述符数|
|DORIS.BK.OS.CPU.TIME|cpu使用时间|ProcessCpuTime|ms|CPU 累计使用时间|Cumulative CPU time|数据来源 JMX OperatingSystem:ProcessCpuTime，单位转换为毫秒，表示进程CPU 累计使用时间|
|DORIS.BK.RT.UPTIME|进程运行时间|Uptime|秒|进程运行时长|Process run time|数据来源 JMX OperatingSystem:Uptime，单位转换为秒，表示进程运行时长|
|DORIS.BK.THREAD_COUNT|工作线程数|ThreadCount|个|线程数量|The number of threads|数据来源 JMX Threading:ThreadCount，表示线程数量|
|||PeckThreadCount|个|峰值线程数量|Peak number of threads|数据来源 JMX Threading:PeckThreadCount，表示峰值线程数量|
|||DaemonThreadCount|个|后台线程数量|The number of backend threads|数据来源 JMX Threading:DaemonThreadCount，表示后台线程数量|