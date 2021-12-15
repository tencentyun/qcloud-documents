### YARN-概览
<table>
<tr>
<th width=20%>标题 </th>
<th width=20%>指标名称</th>
<th width=15%>指标单位</th>
<th width=45%>指标含义 </th>
</tr><tr><td rowspan=4>节点个数 </td>
<td >NumActiveNMs </td>
<td >个 </td>
<td >当前存活的 NodeManager 个数 </td>
</tr><tr>
<td >NumDecommissionedNMs </td>
<td >个 </td>
<td >当前 Decommissioned 的 NodeManager 个数 </td>
</tr><tr>
<td >NumLostNMs </td>
<td >个 </td>
<td >当前 Lost 的 NodeManager 个数 </td>
</tr><tr>
<td >NumUnhealthyNMs </td>
<td >个 </td>
<td >当前 Unhealthy 的 NodeManager 个数 </td>
</tr><tr><td rowspan=4>CPU 核数 </td>
<td >AllocatedVCores </td>
<td >核</td>
<td >当前队列分配的 VCore 个数 </td>
</tr><tr>
<td >ReservedVCores </td>
<td >核</td>
<td >当前队列中 reserved 的 VCore 个数 </td>
</tr><tr>
<td >AvailableVCores </td>
<td >核</td>
<td >当前队列可用的 VCore 个数 </td>
</tr><tr>
<td >PendingVCores </td>
<td >核</td>
<td >当前队列的资源请求中 pending 的 VCore 个数 </td>
</tr><tr><td rowspan=11>应用总数</td>
<td >AppsSubmitted</td>
<td >个</td>
<td >当前队列历史提交作业个数</td>
</tr><tr>
<td >AppsRunning</td>
<td >个</td>
<td >当前队列正在运行的作业个数</td>
</tr><tr>
<td >AppsPending</td>
<td >个</td>
<td >当前队列 pending 的作业个数</td>
</tr><tr>
<td >AppsCompleted</td>
<td >个</td>
<td >当前队列完成的作业个数</td>
</tr><tr>
<td >AppsKilled</td> 
<td >个</td>
<td >当前队列 kill 掉的作业个数</td>
</tr><tr>
<td >AppsFailed</td>
<td >个</td>
<td >当前队列失败的作业个数</td>
</tr><tr>
<td >ActiveApplications</td>
<td >个</td>
<td >当前队列中 active 的作业个数</td>
</tr><tr>
<td >running_0</td>
<td >个</td>
<td >当前队列中运行作业运行时间小于60分钟的作业个数</td>
</tr><tr>
<td >running_60</td>
<td >个</td>
<td >当前队列中运行作业运行时间介于60~300分钟的作业个数</td>
</tr><tr>
<td >running_300</td>
<td >个</td>
<td >当前队列中运行作业运行时间介于300~1440分钟的作业个数</td>
</tr><tr>
<td >running_1440</td>
<td >个</td>
<td >当前队列中运行作业运行时间大于1440分钟的作业个数</td>
</tr><tr>
<td rowspan=4>内存大小</td>
<td >AllocatedMB</td>
<td >MB</td>
<td >当前队列分配的内存大小</td>
</tr><tr>
<td >AvailableMB</td>
<td >MB</td>
<td >当前队列可用的内存大小</td>
</tr><tr>
<td >PendingMB</td>
<td >MB</td>
<td >当前队列的资源请求中 pending 的内存大小</td>
</tr><tr>
<td >ReservedMB</td>
<td >MB</td>
<td >当前队列中 reserved 内存大小</td>
</tr><tr>
<td rowspan=3>容器个数</td>
<td >AllocatedContainers</td>
<td >个</td>
<td >当前队列分配的 container 个数</td>
</tr><tr>
<td >PendingContainers</td>
<td >个</td>
<td >当前队列的资源请求中 pending 的 container 个数</td>
</tr><tr>
<td >ReservedContainers</td>
<td >个</td>
<td >当前队列中 reserved 的 container 个数</td>
</tr><tr>
<td rowspan=2>容器分配释放总数</td>
<td >AggregateContainersAllocated</td>
<td >个</td>
<td >当前队列分配的 container 总数</td>
</tr><tr>
<td >AggregateContainersReleased</td>
<td >个</td>
<td >当前队列 release 的 container 总数</td>
</tr><tr>
<td >用户数</td>
<td >ActiveUsers</td>
<td >个</td>
<td >当前队列活跃用户数</td>
</tr><tr>
<td rowspan=4>Memory</td>
<td >allocatedMB</td>
<td >MB</td>
<td >集群中已分配的内存资源</td>
</tr><tr>
<td >availableMB</td>
<td >MB</td>
<td >集群中可使用的内存资源</td>
</tr><tr>
<td >reservedMB</td>
<td >MB</td>
<td >集群中保留的内存资源</td>
</tr><tr>
<td >totalMB</td>
<td >MB</td>
<td >集群中全部的内存资源</td>
</tr><tr>

<td rowspan=6>Applications</td>
<td >completed</td>
<td >个</td>
<td >采样周期内集群中运行完成的作业数</td>
</tr><tr>
<td >failed</td>
<td >个</td>
<td >采样周期内集群中运行失败的作业数</td>
</tr><tr>
<td >killed</td>
<td >个</td>
<td >采样周期内集群中被杀掉的作业数</td>
</tr><tr>
<td >pending</td>
<td >个</td>
<td >采样周期内集群中等待运行的作业数</td>
</tr><tr>
<td >running</td>
<td >个</td>
<td >采样周期内集群中运行中的作业数</td>
</tr><tr>
<td >submitted</td>
<td >个</td>
<td >采样周期内集群中已提交的作业数</td>
</tr><tr>
<td >内存使用率</td>
<td >usageRatio</td>
<td >%</td>
<td >集群当前内存资源的使用率</td>
</tr><tr>
<td rowspan=4>Cores</td>
<td >allocatedVirtualCores</td>
<td >个</td>
<td >集群中已分配的 CPU 资源</td>
</tr><tr>
<td >availableVirtualCores</td>
<td >个</td>
<td >集群中可使用的 CPU 资源</td>
</tr><tr>
<td >reservedVirtualCores</td>
<td >个</td>
<td >集群中保留的 CPU 资源</td>
</tr><tr>
<td >totalVirtualCores</td>
<td >个</td>
<td >集群中全部的 CPU 资源</td>
</tr><tr>
<td >CPU 使用率</td>
<td >usageRatio</td>
<td >%</td>
<td >集群当前 CPU 资源的使用率</td>
</tr><tr>
<td >AM 启动数量</td>
<td >AMLaunchDelayNumOps</td>
<td >个</td>
<td >AM 启动数量</td>
</tr><tr>
<td >RM 启动 AM 的平均时间</td>
<td >AMLaunchDelayAvgTime</td>
<td >ms</td>
<td >RM 启动 AM 的平均时间</td>
</tr><tr>
<td >注册的 AM 总数</td>
<td >AMRegisterDelayNumOps</td>
<td >个</td>
<td >注册的 AM 总数</td>
</tr><tr>
<td >AM 注册到 RM 的平均时间</td>
<td >AMRegisterDelayAvgTime</td>
<td >ms</td>
<td >AM 注册到 RM 的平均时间</td>
</tr>
</table>

### YARN-ResourceManager
<table>
<tr>
<tr><th width=20%>标题 </th>
<th width=20%>指标名称</th>
<th width=15%>指标单位</th>
<th width=45%>指标含义 </th>
</tr><tr>
<td rowspan=4>RPC 认证授权数 </td>
<td >RpcAuthenticationFailures</td>
<td >个</td>
<td >RPC authentication 失败个数</td>
</tr><tr>
<td >RpcAuthenticationSuccesses</td>
<td >个</td>
<td >RPC authentication 成功个数</td>
</tr><tr>
<td >RpcAuthorizationFailures</td>
<td >个</td>
<td >RPC authorization 失败个数</td>
</tr><tr>
<td >RpcAuthorizationSuccesses</td>
<td >个</td>
<td >RPC authorization 成功个数</td>
</tr><tr>
<td rowspan=2>RPC 接收发送数据量</td>
<td >ReceivedBytes</td>
<td >bytes/s</td>
<td >RPC 接收数据量</td>
</tr><tr>
<td >SentBytes</td>
<td >bytes/s</td>
<td >RPC 发送数据量</td>
</tr><tr>
<td >RPC 连接数</td>
<td >NumOpenConnections</td>
<td >个</td>
<td >当前打开的连接个数</td>
</tr><tr>
<td rowspan=2>RPC 请求次数</td>
<td >RpcProcessingTimeNumOps</td>
<td >次</td>
<td >RPC 请求次数</td>
</tr><tr>
<td >RpcQueueTimeNumOps</td>
<td >次</td>
<td >RPC 请求次数</td>
</tr><tr>
<td >RPC 队列长度</td>
<td >CallQueueLength</td>
<td >个</td>
<td >当前 RPC 队列长度</td>
</tr><tr>
<td rowspan=2>RPC 平均处理时间</td>
<td >RpcProcessingTimeAvgTime</td>
<td >s</td>
<td >RPC 请求平均处理时间</td>
</tr><tr>
<td >RpcQueueTimeAvgTime</td>
<td >s</td>
<td >RPC 在 Queue 中平均时间</td>
</tr><tr>
<td rowspan=2>GC 次数 </td>
<td >YGC </td>
<td >次 </td>
<td >Young GC 次数 </td>
</tr><tr>
<td >FGC </td>
<td >次 </td>
<td >Full GC 次数 </td>
</tr><tr>
<td rowspan=3>GC 时间 </td>
<td >FGCT </td>
<td >s </td>
<td >Full GC 消耗时间 </td>
</tr><tr>
<td >GCT </td>
<td >s </td>
<td >垃圾回收时间消耗 </td>
</tr><tr>
<td >YGCT </td>
<td >s </td>
<td >Young GC 消耗时间 </td>
</tr><tr>
<td rowspan=6>内存区域占比 </td>
<td >S0</td>
<td >% </td>
<td >Survivor 0区内存使用占比 </td>
</tr><tr>
<td >E </td>
<td >% </td>
<td >Eden 区内存使用占比 </td>
</tr><tr>
<td >CCS </td>
<td >% </td>
<td >Compressed class space 区内存使用占比 </td>
</tr><tr>
<td >S1 </td>
<td >% </td>
<td >Survivor 1区内存使用占比 </td>
</tr><tr>
<td >O </td>
<td >% </td>
<td >Old 区内存使用占比 </td>
</tr><tr>
<td >M </td>
<td >% </td>
<td >Metaspace 区内存使用占比 </td>
</tr><tr>
<td rowspan=6>JVM 线程数量 </td>
<td >ThreadsNew </td>
<td >个 </td>
<td >处于 NEW 状态的线程数量 </td>
</tr><tr>
<td >ThreadsRunnable </td>
<td >个 </td>
<td >处于 RUNNABLE 状态的线程数量 </td>
</tr><tr>
<td >ThreadsBlocked </td>
<td >个 </td>
<td >处于 BLOCKED 状态的线程数量 </td>
</tr><tr>
<td >ThreadsWaiting </td>
<td >个 </td>
<td >处于 WAITING 状态的线程数量 </td>
</tr><tr>
<td >ThreadsTimedWaiting </td>
<td >个 </td>
<td >处于 TIMED WAITING 状态的线程数量 </td>
</tr><tr>
<td >ThreadsTerminated </td>
<td >个 </td>
<td >处于 Terminated 状态的线程数量 </td>
</tr><tr>
<td  rowspan=4>JVM 日志数量 </td>
<td >LogFatal </td>
<td >个 </td>
<td >Fatal 日志数量 </td>
</tr><tr>
<td >LogError </td>
<td >个 </td>
<td >Error 日志数量 </td>
</tr><tr>
<td >LogWarn </td>
<td >个 </td>
<td >Warn 日志数量 </td>
</tr><tr>
<td >LogInfo </td>
<td >个 </td>
<td >Info 日志数量 </td>
</tr><tr>
<td rowspan=6>JVM 内存 </td>
<td >MemNonHeapUsedM </td>
<td >MB </td>
<td >进程使用的非堆内存大小</td>
</tr><tr>
<td >MemNonHeapCommittedM </td>
<td >MB </td>
<td >进程 commit 的非堆内存大小</td>
</tr><tr>
<td >MemHeapUsedM </td>
<td >MB </td>
<td >进程使用的堆内存大小</td>
</tr><tr>
<td >MemHeapCommittedM </td>
<td >MB </td>
<td >进程 commit 的堆内存大小</td>
</tr><tr>
<td >MemHeapMaxM </td>
<td >MB </td>
<td >进程最大的堆内存大小</td>
</tr><tr>
<td >MemMaxM </td>
<td >MB </td>
<td >进程最大内存大小</td>
</tr><tr>
<td >CPU 利用率</td>
<td >ProcessCpuLoad</td>
<td >%</td>
<td >CPU 利用率</td>
</tr><tr>
<td >CPU 累计使用时间</td>
<td >ProcessCpuTime</td>
<td >ms</td>
<td >CPU 累计使用时间</td>
</tr><tr>
<td rowspan=2>文件描述符数</td>
<td >MaxFileDescriptorCount</td>
<td >个</td>
<td >最大文件描述符数</td>
</tr><tr>
<td >OpenFileDescriptorCount</td>
<td >个</td>
<td >打开文件描述符数</td>
</tr><tr>
<td >进程运行时长</td>
<td >Uptime</td>
<td >s</td>
<td >进程运行时长</td>
</tr><tr>
<td rowspan=2>工作线程数</td>
<td >DaemonThreadCount</td>
<td >个</td>
<td >进程的 Daemon 线程个数</td>
</tr><tr>
<td >ThreadCount</td>
<td >个</td>
<td >进程的线程个数</td>
</tr><tr>
<td >节点状态</td>
<td >haState</td>
<td >1:Active,0:Standby</td>
<td >ResourceManager 主备状态</td>
</tr><tr>
<td >主备切换</td>
<td >switchOccurred</td>
<td >-</td>
<td >ResourceManager 主备切换</td>
</tr>
</table>

### YARN-JobHistoryServer
<table>
<tr>
<tr><th width=20%>标题 </th>
<th width=20%>指标名称</th>
<th width=15%>指标单位</th>
<th width=45%>指标含义 </th>
</tr><tr>
</tr><tr>
<td rowspan=6>JVM线程数量 </td>
<td >ThreadsNew </td>
<td >个 </td>
<td >处于 NEW 状态的线程数量 </td>
</tr><tr>
<td >ThreadsRunnable </td>
<td >个 </td>
<td >处于 RUNNABLE 状态的线程数量 </td>
</tr><tr>
<td >ThreadsBlocked </td>
<td >个 </td>
<td >处于 BLOCKED 状态的线程数量 </td>
</tr><tr>
<td >ThreadsWaiting </td>
<td >个 </td>
<td >处于 WAITING 状态的线程数量 </td>
</tr><tr>
<td >ThreadsTimedWaiting </td>
<td >个 </td>
<td >处于 TIMED WAITING 状态的线程数量 </td>
</tr><tr>
<td >ThreadsTerminated </td>
<td >个 </td>
<td >处于 Terminated 状态的线程数量 </td>
</tr><tr>
<td rowspan=4>JVM 日志数量 </td>
<td >LogFatal </td>
<td >个 </td>
<td >FATAL 级别日志数量 </td>
</tr><tr>
<td >LogError </td>
<td >个 </td>
<td >ERROR 级别日志数量 </td>
</tr>			<tr>
<td >LogWarn </td>
<td >个 </td>
<td >WARN 级别日志数量 </td>
</tr><tr>
<td >LogInfo </td>
<td >个 </td>
<td >	INFO 级别日志数量 </td>
</tr><tr>
<td rowspan=6>JVM 内存 </td>
<td >MemNonHeapUsedM </td>
<td >MB </td>
<td >进程使用的非堆内存大小</td>
</tr><tr>
<td >MemNonHeapCommittedM </td>
<td >MB </td>
<td >进程 commit 的非堆内存大小</td>
</tr><tr>
<td >MemHeapUsedM </td>
<td >MB </td>
<td >进程使用的堆内存大小</td>
</tr><tr>
<td >MemHeapCommittedM </td>
<td >MB </td>
<td >进程 commit 的堆内存大小</td>
</tr><tr>
<td >MemHeapMaxM </td>
<td >MB </td>
<td >进程最大的堆内存大小</td>
</tr><tr>
<td >MemMaxM </td>
<td >MB </td>
<td >进程最大内存大小</td>
</tr><tr>
<td rowspan=2>GC 次数 </td>
<td >YGC </td>
<td >次 </td>
<td >Young GC 次数 </td>
</tr><tr>
<td >FGC </td>
<td >次 </td>
<td >Full GC 次数 </td>
</tr><tr>
<td rowspan=3>GC 时间 </td>
<td >FGCT </td>
<td >s </td>
<td >Full GC 消耗时间 </td>
</tr><tr>
<td >GCT </td>
<td >s </td>
<td >垃圾回收时间消耗 </td>
</tr><tr>
<td >YGCT </td>
<td >s </td>
<td >Young GC 消耗时间 </td>
</tr><tr>
<td rowspan=6>内存区域占比 </td>
<td >S0</td>
<td >% </td>
<td >Survivor 0区内存使用占比 </td>
</tr><tr>
<td >E </td>
<td >% </td>
<td >Eden 区内存使用占比 </td>
</tr><tr>
<td >CCS </td>
<td >% </td>
<td >Compressed class space 区内存使用占比 </td>
</tr><tr>
<td >S1 </td>
<td >% </td>
<td >Survivor 1区内存使用占比 </td>
</tr><tr>
<td >O </td>
<td >% </td>
<td >Old 区内存使用占比 </td>
</tr><tr>
<td >M </td>
<td >% </td>
<td >Metaspace 区内存使用占比 </td>
</tr><tr>
<td >CPU 利用率</td>
<td >ProcessCpuLoad</td>
<td >%</td>
<td >CPU 利用率</td>
</tr><tr>
<td >CPU 累计使用时间</td>
<td >ProcessCpuTime</td>
<td >ms</td>
<td >CPU 累计使用时间</td>
</tr><tr>
<td rowspan=2>文件描述符数</td>
<td >MaxFileDescriptorCount</td>
<td >个</td>
<td >最大文件描述符数</td>
</tr><tr>
<td >OpenFileDescriptorCount</td>
<td >个</td>
<td >打开文件描述符数</td>
</tr><tr>
<td >进程运行时长</td>
<td >Uptime</td>
<td >s</td>
<td >进程运行时长</td>
</tr><tr>
<td rowspan=2>工作线程数</td>
<td >DaemonThreadCount</td>
<td >个</td>
<td >进程的 Daemon 线程个数</td>
</tr><tr>
<td >ThreadCount</td>
<td >个</td>
<td >进程的线程个数</td>
</tr>
</table>

### TARN-NodeManager
<table>
<tr>
<tr><th width=20%>标题 </th>
<th width=20%>指标名称</th>
<th width=15%>指标单位</th>
<th width=45%>指标含义 </th>
</tr><tr>
<td rowspan=2>GC 次数 </td>
<td >YGC </td>
<td >次 </td>
<td >Young GC 次数 </td>
</tr><tr>
<td >FGC </td>
<td >次 </td>
<td >Full GC 次数 </td>
</tr><tr>
<td rowspan=3>GC 时间 </td>
<td >FGCT </td>
<td >s </td>
<td >Full GC 消耗时间 </td>
</tr><tr>
<td >GCT </td>
<td >s </td>
<td >垃圾回收时间消耗 </td>
</tr><tr>
<td >YGCT </td>
<td >s </td>
<td >Young GC 消耗时间 </td>
</tr><tr>
<td rowspan=6>内存区域占比 </td>
<td >S0</td>
<td >% </td>
<td >Survivor 0区内存使用占比 </td>
</tr><tr>
<td >E </td>
<td >% </td>
<td >Eden 区内存使用占比 </td>
</tr><tr>
<td >CCS </td>
<td >% </td>
<td >Compressed class space 区内存使用占比 </td>
</tr><tr>
<td >S1 </td>
<td >% </td>
<td >Survivor 1区内存使用占比 </td>
</tr><tr>
<td >O </td>
<td >% </td>
<td >Old 区内存使用占比 </td>
</tr><tr>
<td >M </td>
<td >% </td>
<td >Metaspace 区内存使用占比 </td>
</tr><tr>
<td rowspan=6>JVM 线程数量 </td>
<td >ThreadsNew </td>
<td >个 </td>
<td >处于 NEW 状态的线程数量 </td>
</tr><tr>
<td >ThreadsRunnable </td>
<td >个 </td>
<td >处于 RUNNABLE 状态的线程数量 </td>
</tr><tr>
<td >ThreadsBlocked </td>
<td >个 </td>
<td >处于 BLOCKED 状态的线程数量 </td>
</tr><tr>
<td >ThreadsWaiting </td>
<td >个 </td>
<td >处于 WAITING 状态的线程数量 </td>
</tr><tr>
<td >ThreadsTimedWaiting </td>
<td >个 </td>
<td >处于 TIMED WAITING 状态的线程数量 </td>
</tr><tr>
<td >ThreadsTerminated </td>
<td >个 </td>
<td >当前 TERMINATED 状态线程数量</td>
</tr><tr>
<td rowspan=4>JVM 日志数量 </td>
<td >LogFatal </td>
<td >个 </td>
<td >FATAL 级别日志数量 </td>
</tr><tr>
<td >LogError </td>
<td >个 </td>
<td >ERROR 级别日志数量 </td>
</tr>			<tr>
<td >LogWarn </td>
<td >个 </td>
<td >WARN 级别日志数量 </td>
</tr><tr>
<td >LogInfo </td>
<td >个 </td>
<td >	INFO 级别日志数量 </td>
</tr><tr>
<td rowspan=6>JVM 内存 </td>
<td >MemNonHeapUsedM </td>
<td >MB </td>
<td >进程使用的非堆内存大小</td>
</tr><tr>
<td >MemNonHeapCommittedM </td>
<td >MB </td>
<td >进程 commit 的非堆内存大小</td>
</tr><tr>
<td >MemHeapUsedM </td>
<td >MB </td>
<td >进程使用的堆内存大小</td>
</tr><tr>
<td >MemHeapCommittedM </td>
<td >MB </td>
<td >进程 commit 的堆内存大小</td>
</tr><tr>
<td >MemHeapMaxM </td>
<td >MB </td>
<td >进程最大的堆内存大小</td>
</tr><tr>
<td >MemMaxM </td>
<td >MB </td>
<td >进程最大内存大小</td>
</tr><tr>
<td rowspan=7>容器总数</td>
<td >ContainersLaunched</td>
<td >个</td>
<td >launch 的 container 个数</td>
</tr><tr>
<td >ContainersCompleted</td>
<td >个</td>
<td >运行完成的 container 个数</td>
</tr><tr>
<td >ContainersFailed</td>
<td >个</td>
<td >失败的 container 个数</td>
</tr><tr>
<td >ContainersKilled</td>
<td >个</td>
<td >被 kill 的 container 个数</td>
</tr><tr>
<td >ContainersIniting</td>
<td >个</td>
<td >初始化中的 container 个数</td>
</tr><tr>
<td >ContainersRunning</td>
<td >个</td>
<td >正在运行的 container 个数</td>
</tr><tr>
<td >AllocatedContainers</td>
<td >个</td>
<td >NodeManager 分配的 container 数量</td>
</tr><tr>
<td >容器启动平均耗时</td>
<td >ContainerLaunchDurationAvgTime</td>
<td >ms</td>
<td >容器启动平均耗时</td>
</tr><tr>
<td >容器启动操作数</td>
<td >ContainerLaunchDurationNumOps</td>
<td >个</td>
<td >容器启动操作数</td>
</tr><tr>
<td rowspan=2>CPU 核数</td>
<td >AvailableVCores</td>
<td >核</td>
<td >NodeManager 可用的 VCore 个数</td>
</tr><tr>
<td >AllocatedVCores</td>
<td >核</td>
<td >NodeManager 分配的 VCore个数</td>
</tr><tr>
<td rowspan=2>内存大小</td>
<td >AllocatedGB</td>
<td >GB</td>
<td >NodeManager 分配的内存大小</td>
</tr><tr>
<td >AvailableGB</td>
<td >GB</td>
<td >NodeManager 可用的内存大小</td>
</tr><tr>
<td >CPU 利用率</td>
<td >ProcessCpuLoad</td>
<td >%</td>
<td >CPU 利用率</td>
</tr><tr>
<td >CPU 累计使用时间</td>
<td >ProcessCpuTime</td>
<td >ms</td>
<td >CPU 累计使用时间</td>
</tr><tr>
<td rowspan=2>文件描述符数</td>
<td >MaxFileDescriptorCount</td>
<td >个</td>
<td >最大文件描述符数</td>
</tr><tr>
<td >OpenFileDescriptorCount</td>
<td >个</td>
<td >打开文件描述符数</td>
</tr><tr>
<td >进程运行时长</td>
<td >Uptime</td>
<td >s</td>
<td >进程运行时长</td>
</tr><tr>
<td rowspan=2>工作线程数</td>
<td >DaemonThreadCount</td>
<td >个</td>
<td >进程的 Daemon 线程个数</td>
</tr><tr>
<td >ThreadCount</td>
<td >个</td>
<td >进程的线程个数</td>
</tr>
</table>
