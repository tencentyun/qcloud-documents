腾讯云提供下列 Doris Broker 服务的监控项。Broker 服务可部署在 FE 或 BE 节点上，因此在腾讯云集群监控页面，Broker 的监控项也分是在 BE 指标和 FE 指标 Tab 页内。不论部署在哪种节点上，由于都是 Broker 服务，相关的监控项都一致。
![](https://qcloudimg.tencent-cloud.cn/raw/a417df8e759d82d14b55768fd18ba8ae.png)

Broker 监控项总体分为两类：
1. BROKER_JSTAT：Broker GC 相关的监控数据。
2. BROKER_JVM：Broker 内存使用数据、CPU 相关数据及线程相关数据。

<table>
<thead>
<tr>
<th>指标名称</th>
<th>前台标题</th>
<th>指标 Tag 名称</th>
<th>单位</th>
<th>指标含义</th>
<th>英文指标含义</th>
<th>统计方法</th>
</tr>
</thead>
<tbody><tr>
<td rowspan=2>DORIS.BK.GC_UTIL_GC_COUNT</td>
<td rowspan=2>GC 次数</td>
<td>YGC</td>
<td>次</td>
<td>Young GC 次数</td>
<td>Number of young generation GC events</td>
<td>数据来源 jstat -gcutil pid 命令 YGC 一栏，表示 Young GC 次数</td>
</tr>
<tr>
<td>FGC</td>
<td>次</td>
<td>Full GC 次数</td>
<td>Number of full GC events</td>
<td>数据来源 jstat -gcutil pid 命令 FGC 一栏，表示 Full GC 次数</td>
</tr>
<tr>
<td rowspan=3>DORIS.BK.GC_UTIL_GC_TIME</td>
<td rowspan=3>GC 时间</td>
<td>FGCT</td>
<td>秒</td>
<td>Full GC 消耗时间</td>
<td>Full garbage collection time</td>
<td>数据来源 jstat -gcutil pid 命令 FGCT 一栏，表示 Full GC 消耗时间</td>
</tr>
<tr>
<td>GCT</td>
<td>秒</td>
<td>垃圾回收时间消耗</td>
<td>Total garbage collection time</td>
<td>数据来源 jstat -gcutil pid 命令 GCT 一栏，表示垃圾回收时间消耗</td>
</tr>
<tr>
<td>YGCT</td>
<td>秒</td>
<td>Young GC 消耗时间</td>
<td>Young generation garbage collection time</td>
<td>数据来源 jstat -gcutil pid 命令 YGCT 一栏，表示 Young GC 消耗时间</td>
</tr>
<tr>
<td rowspan=6>DORIS.BK.GC_UTIL_MEMORY</td>
<td rowspan=6>内存区域占比</td>
<td>S0</td>
<td>%</td>
<td>Survivor 0 区内存使用占比</td>
<td>The percentage of survivor 0 space memory usage</td>
<td>数据来源 jstat -gcutil pid 命令 S0 一栏，表示 Survivor 0 区内存使用占比</td>
</tr>
<tr>
<td>E</td>
<td>%</td>
<td>Eden 区内存使用占比</td>
<td>The percentage of Eden space memory usage</td>
<td>数据来源 jstat -gcutil pid 命令 E 一栏，表示 Eden 区内存使用占比</td>
</tr>
<tr>
<td>CCS</td>
<td>%</td>
<td>Compressed class space 区内存使用占比</td>
<td>The percentage of Compressed class space memory usage</td>
<td>数据来源 jstat -gcutil pid 命令 CCS 一栏，表示 Compressed class space 区内存使用占比</td>
</tr>
<tr>
<td>S1</td>
<td>%</td>
<td>Survivor 1区内存使用占比</td>
<td>The percentage of Survivor 1 space memory usage</td>
<td>数据来源 jstat -gcutil pid 命令 S1 一栏，表示 Survivor 1 区内存使用占比</td>
</tr>
<tr>
<td>O</td>
<td>%</td>
<td>Old 区内存使用占比</td>
<td>The percentage of Old space memory usage</td>
<td>数据来源 jstat -gcutil pid 命令 O 一栏，表示 Old 区内存使用占比</td>
</tr>
<tr>
<td>M</td>
<td>%</td>
<td>Metaspace 区内存使用占比</td>
<td>Metaspace utilization as a percentage of the space's current capacity</td>
<td>数据来源 jstat -gcutil pid 命令 M 一栏，表示 Metaspace 区内存使用占比</td>
</tr>
<tr>
<td rowspan=7>DORIS.BK.JVM.MEM</td>
<td rowspan=7>JVM 内存</td>
<td>MemNonHeapUsedM</td>
<td>MB</td>
<td>JVM 当前已经使用的 NonHeapMemory 的数量</td>
<td>Used JVM NonHeapMemory size</td>
<td>数据来源 JMX JvmMetrics:MemNonHeapUsedM，表示 JVM 当前已经使用的非堆内存</td>
</tr>
<tr>
<td>MemNonHeapCommittedM</td>
<td>MB</td>
<td>JVM 当前已经提交的 NonHeapMemory 的数量</td>
<td>NonHeapCommittedM size that JVM is configured with</td>
<td>数据来源 JMX JvmMetrics:MemNonHeapCommittedM，表示 JVM 当前已经提交的非堆内存</td>
</tr>
<tr>
<td>MemHeapUsedM</td>
<td>MB</td>
<td>JVM 当前已经使用的 HeapMemory 的数量</td>
<td>Used JVM HeapMemory size</td>
<td>数据来源 JMX JvmMetrics:MemHeapUsedM，表示 JVM 当前已经使用的堆内存</td>
</tr>
<tr>
<td>MemHeapCommittedM</td>
<td>MB</td>
<td>JVM 当前已经提交的 HeapMemory 的数量</td>
<td>Submitted JVM HeapMemory</td>
<td>数据来源 JMX JvmMetrics:MemHeapCommittedM，表示 JVM 当前已经提交的堆内存</td>
</tr>
<tr>
<td>MemHeapMaxM</td>
<td>MB</td>
<td>JVM 配置的 HeapMemory 的数量</td>
<td>HeapMemory size that JVM is configured with</td>
<td>数据来源 JMX JvmMetrics:MemHeapMaxM，表示 JVM 配置的堆内存大小</td>
</tr>
<tr>
<td>MemHeapInitM</td>
<td>MB</td>
<td>JVM 初始 HeapMemory 的数量</td>
<td>Initial JVM HeapMem size</td>
<td>数据来源 JMX JvmMetrics:MemHeapInitM，表示 JVM 初始堆内存大小</td>
</tr>
<tr>
<td>MemNonHeapInitM</td>
<td>MB</td>
<td>JVM 初始 NonHeapMemory 的数量</td>
<td>Initial JVM NonHeapMem size</td>
<td>数据来源 JMX JvmMetrics:MemNonHeapInitM，表示 JVM 初始非堆内存大小</td>
</tr>
<tr>
<td>DORIS.BK.OS.CPU.LOAD</td>
<td>CPU 利用率</td>
<td>ProcessCpuLoad</td>
<td>%</td>
<td>CPU 利用率</td>
<td>CPU utilization</td>
<td>数据来源 JMX OperatingSystem:ProcessCpuLoad，表示 CPU 利用率</td>
</tr>
<tr>
<td rowspan=2>DORIS.BK.OS.FD.COUNT</td>
<td rowspan=2>文件句柄数</td>
<td>MaxFileDescriptorCount</td>
<td>个</td>
<td>最大文件描述符数</td>
<td>Maximum number of file descriptors</td>
<td>数据来源 JMX OperatingSystem:MaxFileDescriptorCount，表示最大文件描述符数</td>
</tr>
<tr>
<td>OpenFileDescriptorCount</td>
<td>个</td>
<td>已打开文件描述符数</td>
<td>Number of opened file descriptors</td>
<td>数据来源 JMX OperatingSystem:OpenFileDescriptorCount，表示已打开文件描述符数</td>
</tr>
<tr>
<td>DORIS.BK.OS.CPU.TIME</td>
<td>CPU 使用时间</td>
<td>ProcessCpuTime</td>
<td>ms</td>
<td>CPU 累计使用时间</td>
<td>Cumulative CPU time</td>
<td>数据来源 JMX OperatingSystem:ProcessCpuTime，单位转换为毫秒，表示进程 CPU 累计使用时间</td>
</tr>
<tr>
<td>DORIS.BK.RT.UPTIME</td>
<td>进程运行时间</td>
<td>Uptime</td>
<td>秒</td>
<td>进程运行时长</td>
<td>Process run time</td>
<td>数据来源 JMX OperatingSystem:Uptime，单位转换为秒，表示进程运行时长</td>
</tr>
<tr>
<td rowspan=3>DORIS.BK.THREAD_COUNT</td>
<td rowspan=3>工作线程数</td>
<td>ThreadCount</td>
<td>个</td>
<td>线程数量</td>
<td>The number of threads</td>
<td>数据来源 JMX Threading:ThreadCount，表示线程数量</td>
</tr>
<tr>
<td>PeckThreadCount</td>
<td>个</td>
<td>峰值线程数量</td>
<td>Peak number of threads</td>
<td>数据来源 JMX Threading:PeckThreadCount，表示峰值线程数量</td>
</tr>
<tr>
<td>DaemonThreadCount</td>
<td>个</td>
<td>后台线程数量</td>
<td>The number of backend threads</td>
<td>数据来源 JMX Threading:DaemonThreadCount，表示后台线程数量</td>
</tr>
</tbody></table>
