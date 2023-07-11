>!PrestoSQL 指标目前仅支持 PrestoSQL322 和 PrestoSQL350 及以上版本。

### PrestoSQL-概览
<table>
<tr>
<th width=20%>标题 </th>
<th width=20%>指标名称</th>
<th width=15%>指标单位</th>
<th width=45%>指标含义 </th>
</tr><tr>
<td rowspan=3>节点数量</td>
<td>Active</td>
<td >个</td>
<td >活跃节点数量</td>
</tr><tr>
<td >Total</td>
<td >个</td>
<td >总节点数量</td>
</tr><tr>
<td >Failed</td>
<td >个</td>
<td >失败节点数量</td>
</tr><tr>
<td rowspan=2>查询</td>
<td >RunningQueries</td>
<td >个</td>
<td >正在运行的查询总数</td>
</tr><tr>
<td >QueuedQueries</td>
<td >个</td>
<td >等待状态的查询总数</td>
</tr><tr>
<td  rowspan=5>查询频度</td>
<td >FailedQueries</td>
<td >个/min</td>
<td >失败的查询总数</td>
</tr><tr>
<td >AbandonedQueries</td>
<td >个/min</td>
<td >放弃的查询总数</td>
</tr><tr>
<td >CanceledQueries</td>
<td >个/min</td>
<td >取消的查询总数</td>
</tr><tr>
<td >CompletedQueries</td>
<td >个/min</td>
<td >完成的查询总数</td>
</tr><tr>	
<td >StartedQueries</td>
<td >个/min</td>
<td >已启动的查询总数</td>
</tr><tr>	
<td rowspan=2>每分钟数据输入输出量</td>
<td >InputDataSizeOneMinute</td>
<td >GB/min</td>
<td >输入数据速率</td>
</tr><tr>
<td >OutputDataSizeOneMinute</td>
<td >GB/min</td>
<td >输出数据速率</td>
</tr>
<tr>
<td>每分钟用户异常导致的失败查询数</td>
<td>UserErrorFailures</td>
<td>count/min</td>
<td>每分钟用户异常导致的失败查询数</td>
</tr>
<tr>
<td>每分钟内部异常导致的失败查询数</td>
<td>InternalFailures</td>
<td>count/min</td>
<td>每分钟内部异常导致的失败查询数</td>
</tr>
<tr>
<td>每分钟资源不足导致的失败查询数</td>
<td>InsufficientResourcesFailures</td>
<td>count/min</td>
<td>每分钟资源不足导致的失败查询数</td>
</tr>
<tr>
<td>每分钟外部异常导致的失败查询数</td>
<td>ExternalFailures</td>
<td>count/min</td>
<td>每分钟外部异常导致的失败查询数</td>
</tr>
<tr>
<td>每分钟查询处理的记录数</td>
<td>ConsumedInputRows</td>
<td>count/min</td>
<td>每分钟查询处理的记录数</td>
</tr>
<tr>
<td>每分钟查询处理的字节数</td>
<td>ConsumedInput</td>
<td>bytes/min</td>
<td>每分钟查询处理的字节数</td>
</tr>
<tr>
<td>每分钟查询处理的 CPU 时间</td>
<td>ConsumedCpuTimeSecs</td>
<td>count/min</td>
<td>每分钟查询处理的 CPU 时间</td>
</tr>
<tr>
<td rowspan=4>Splits 数</td>
<td>BlockedSplits</td>
<td>count</td>
<td>阻塞的Splits数</td>
</tr>
<tr>
<td>RunningSplits</td>
<td>count</td>
<td>运行中的 Splits 数</td>
</tr>
<tr>
<td>TotalSplits</td>
<td>count</td>
<td>任务执行器总 Splits 数</td>
</tr>
<tr>
<td>WaitingSplits</td>
<td>count</td>
<td>TaskExecutor 上等待的 Splits 数</td>
</tr>
<tr>
<td>向 TaskExecutor 注册的所有任务</td>
<td>Tasks</td>
<td>count</td>
<td>向 TaskExecutor 注册的所有任务</td>
</tr>
<tr>
<td>每分钟失败的 Task 数目</td>
<td>FailedTasks</td>
<td>count/min</td>
<td>每分钟失败的 Task 数目</td>
</tr>
<tr>
<td rowspan=2>每分钟 Task 输入输出数据行</td>
<td>InputPositionsOneMinute</td>
<td>count/min</td>
<td>每分钟 Task 输入数据行</td>
</tr>
<tr>
<td>OutputPositionsOneMinute</td>
<td>count/min</td>
<td>每分钟 Task 输出数据行</td>
</tr>
</table>

### PrestoSQL-Worker
<table>
<tr>
<th width=20%>标题 </th>
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
<td rowspan=7>JVM 内存 </td>
<td >MemNonHeapUsedM </td>
<td >MB </td>
<td >JVM 当前已经使用的 NonHeapMemory 的数量</td>
</tr><tr>
<td >MemNonHeapCommittedM </td>
<td >MB </td>
<td >JVM 当前已经提交的 NonHeapMemory 的数量</td>
</tr><tr>
<td >MemHeapUsedM </td>
<td >MB </td>
<td >JVM 当前已经使用的 HeapMemory 的数量</td>
</tr><tr>
<td >MemHeapCommittedM </td>
<td >MB </td>
<td >JVM 当前已经提交的 HeapMemory 的数量</td>
</tr><tr>
<td >MemHeapMaxM </td>
<td >MB </td>
<td >JVM 配置的 HeapMemory 的数量</td>
</tr><tr>
<td >MemHeapInitM </td>
<td >MB </td>
<td >JVM 初始 HeapMem 的数量</td>
</tr><tr>
<td >MemNonHeapInitM </td>
<td >MB </td>
<td >JVM 初始 NonHeapMem 的数量</td>

</tr><tr>
<td rowspan=2>数据输入输出速率 </td>
<td >InputDataSize.OneMinute.Rate </td>
<td >GB/min </td>
<td >输入数据速率</td>
</tr><tr>
<td >OutputDataSize.OneMinute.Rate</td>
<td >GB/min </td>
<td >输出数据速率</td>
</tr><tr>
<td rowspan=3>进程数量 </td>
<td >PeakThreadCount </td>
<td >个 </td>
<td >峰值线程数</td>
</tr><tr>
<td >ThreadCount</td>
<td >个 </td>
<td >总线程数量</td>
</tr><tr>
<td >DaemonThreadCount</td>
<td >个 </td>
<td >Daemon 线程数量</td>
</tr><tr>
<td >进程运行时间</td>
<td >Uptime</td>
<td >s</td>
<td >进程运行时间</td>
</tr><tr>
<td >进程启动时间</td>
<td >StartTime</td>
<td >s</td>
<td >进程启动时间</td>
</tr><tr>
<td rowspan=2>文件描述符数</td>
<td >MaxFileDescriptorCount</td>
<td >个</td>
<td >最大文件描述符数</td>
</tr><tr>
<td >OpenFileDescriptorCount</td>
<td >个</td>
<td >已打开文件描述符数量</td>
</tr>
</table >

### PRESTOSQL-Coordinator
<table>
<tr>
<th width=20%>标题 </th>
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
<td rowspan=7>JVM 内存 </td>
<td >MemNonHeapUsedM </td>
<td >MB </td>
<td >JVM 当前已经使用的 NonHeapMemory 的数量</td>
</tr><tr>
<td >MemNonHeapCommittedM </td>
<td >MB </td>
<td >JVM 当前已经提交的 NonHeapMemory 的数量</td>
</tr><tr>
<td >MemHeapUsedM </td>
<td >MB </td>
<td >JVM 当前已经使用的 HeapMemory 的数量</td>
</tr><tr>
<td >MemHeapCommittedM </td>
<td >MB </td>
<td >JVM 当前已经提交的 HeapMemory 的数量</td>
</tr><tr>
<td >MemHeapMaxM </td>
<td >MB </td>
<td >JVM 配置的 HeapMemory 的数量</td>
</tr><tr>
<td >MemHeapInitM </td>
<td >MB </td>
<td >JVM 初始 HeapMem 的数量</td>
</tr><tr>
<td >MemNonHeapInitM </td>
<td >MB </td>
<td >JVM 初始 NonHeapMem 的数量</td>
</tr><tr>
<td rowspan=3>进程数量 </td>
<td >PeakThreadCount </td>
<td >个 </td>
<td >峰值线程数</td>
</tr><tr>
<td >ThreadCount</td>
<td >个 </td>
<td >线程数量</td>
</tr><tr>
<td >DaemonThreadCount</td>
<td >个 </td>
<td >后台线程数量</td>
</tr><tr>
<td >进程运行时间</td>
<td >Uptime</td>
<td >s</td>
<td >进程运行时间</td>
</tr><tr>
<td >进程启动时间</td>
<td >StartTime</td>
<td >s</td>
<td >进程启动时间</td>
</tr><tr>
<td rowspan=2>文件描述符数</td>
<td >MaxFileDescriptorCount</td>
<td >个</td>
<td >最大文件描述符数</td>
</tr><tr>
<td >OpenFileDescriptorCount</td>
<td >个</td>
<td >已打开文件描述符数量</td>
</tr>
</table >
