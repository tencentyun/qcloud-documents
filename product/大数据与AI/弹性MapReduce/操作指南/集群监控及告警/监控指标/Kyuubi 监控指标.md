### Kyuubi-KyuubiServer
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
<td >	Young GC 次数</td>
</tr><tr>
<td >FGC </td>
<td >次 </td>
<td >Full GC 次数 </td>
</tr><tr>
<td rowspan=3>GC 时间 </td>
<td >FGCT </td>
<td >s </td>
<td >Full GC 消耗时间</td>
</tr><tr>
<td >GCT </td>
<td >s </td>
<td >垃圾回收时间消耗</td>
</tr><tr>
<td >YGCT </td>
<td >s </td>
<td >Young GC 消耗时间</td>
</tr><tr>
<td rowspan=6>内存区域占比 </td>
<td >S0 </td>
<td >% </td>
<td >Survivor 0区内存使用占比</td>
</tr><tr>
<td >E </td>
<td >% </td>
<td >Eden 区内存使用占比</td>
</tr><tr>
<td >CCS </td>
<td >% </td>
<td >Compressed class space 区内存使用占比</td>
</tr><tr>		
<td >S1 </td>
<td >% </td>
<td >Survivor 1区内存使用占比</td>
</tr><tr>
<td >O </td>
<td >% </td>
<td >Old 区内存使用占比</td>
</tr><tr>
<td >M </td>
<td >% </td>
<td >Metaspace 区内存使用占比</td>
</tr><tr>	
<td rowspan=7>JVM 内存 </td>
<td >MemHeapUsedM </td>
<td >MB </td>
<td >JVM 当前已经使用的 HeapMemory 的数量</td>
</tr><tr>
<td >MemHeapCommittedM </td>
<td >MB </td>
<td >JVM 已经提交的 HeapMemory 的数量</td>
</tr><tr>
<td >MemHeapMaxM </td>
<td >MB </td>
<td >JVM 配置的 HeapMemory 的数量</td>
</tr><tr>		
<td >MemHeapInitM </td>
<td >MB </td>
<td >JVM 初始 HeapMemory 的数量</td>
</tr><tr>
<td >MemNonHeapUsedM</td>
<td >MB</td>
<td >	JVM 当前已经使用的 NonHeapMemory 的数量</td>
</tr><tr>
<td >MemNonHeapCommittedM </td>
<td >MB </td>
<td >JVM 已经提交的 NonHeapMemory 的数量</td>
</tr><tr>
<td >MemNonHeapInitM </td>
<td >MB </td>
<td >JVM 初始 NonHeapMemory 的数量</td>
</tr><tr>
<td rowspan=2>文件描述符数 </td>
<td >OpenFileDescriptorCount </td>
<td >个 </td>
<td >已打开文件描述符数量</td>
</tr><tr>
<td >MaxFileDescriptorCount </td>
<td >个 </td>
<td >最大文件描述符数</td>
</tr><tr>
<td >CPU 利用率 </td>
<td >ProcessCpuLoad </td>
<td >% </td>
<td >进程 CPU 利用率</td>
</tr><tr>
<td rowspan=3>工作线程数 </td>
<td >DaemonThreadCount </td>
<td >个 </td>
<td >守护线程数</td>
</tr><tr>
<td >PeakThreadCount </td>
<td >个 </td>
<td >峰值线程数量</td>
</tr><tr>
<td >ThreadCount </td>
<td >个 </td>
<td >线程总数</td>
</tr><tr>
<td >CPU 累计使用时间 </td>
<td >ProcessCpuTime </td>
<td >ms </td>
<td >CPU 累计使用时间</td>
</tr><tr>
<td >进程运行时长 </td>
<td >Uptime </td>
<td >s </td>
<td >进程运行时长</td>
</tr>
<tr>
<td>进入 Running 操作状态事件频率</td>
<td>Ratio</td>
<td>count/s</td>
<td>进入 Running 操作状态事件频率</td>
</tr>
<tr>
<td>进入 Pending 操作状态事件频率</td>
<td>Ratio</td>
<td>count/s</td>
<td>进入 Pending 操作状态事件频率</td>
</tr>
<tr>
<td>进入 Initialized 操作状态事件频率</td>
<td>Ratio</td>
<td>count/s</td>
<td>进入 Initialized 操作状态事件频率</td>
</tr>
<tr>
<td>进入 Finished 操作状态事件频率</td>
<td>Ratio</td>
<td>count/s</td>
<td>进入 Finished 操作状态事件频率</td>
</tr>
<tr>
<td>进入 Closed 操作状态事件频率</td>
<td>Ratio</td>
<td>count/s</td>
<td>进入 Closed 操作状态事件频率</td>
</tr>
<tr>
<td>FetchResultRows 方法调用频率</td>
<td>Ratio</td>
<td>count/s</td>
<td>FetchResultRows 方法调用频率</td>
</tr>
<tr>
<td>FetchLogRows 方法调用频率</td>
<td>Ratio</td>
<td>count/s</td>
<td>FetchLogRows 方法调用频率</td>
</tr>
<tr>
<td rowspan=5>GetResultSetMetadata 方法调用时间</td>
<td>P50</td>
<td  rowspan=5>ms</td>
<td>GetResultSetMetadata 方法调用时间的50分位数</td>
</tr>
<tr>
<td>P75</td>
<td>GetResultSetMetadata 方法调用时间的75分位数</td>
</tr>
<tr>
<td>P95</td>
<td>GetResultSetMetadata 方法调用时间的95分位数</td>
</tr>
<tr>
<td>P99</td>
<td>GetResultSetMetadata 方法调用时间的99分位数</td>
</tr>
<tr>
<td>P999</td>
<td>GetResultSetMetadata 方法调用时间的999分位数</td>
</tr>
<tr>
<td  rowspan=5>CloseOperation 方法调用时间</td>
<td>P50</td>
<td  rowspan=5>ms</td>
<td>CloseOperation 方法调用时间的50分位数</td>
</tr>
<tr>
<td>P75</td>
<td>CloseOperation 方法调用时间的75分位数</td>
</tr>
<tr>
<td>P95</td>
<td>CloseOperation 方法调用时间的95分位数</td>
</tr>
<tr>
<td>P99</td>
<td>CloseOperation 方法调用时间的99分位数</td>
</tr>
<tr>
<td>P999</td>
<td>CloseOperation 方法调用时间的999分位数</td>
</tr>
<tr>
<td  rowspan=5>GetOperationStatus 方法调用时间</td>
<td>P50</td>
<td  rowspan=5>ms</td>
<td>GetOperationStatus 方法调用时间的50分位数</td>
</tr>
<tr>
<td>P75</td>
<td>GetOperationStatus 方法调用时间的75分位数</td>
</tr>
<tr>
<td>P95</td>
<td>GetOperationStatus 方法调用时间的95分位数</td>
</tr>
<tr>
<td>P99</td>
<td>GetOperationStatus 方法调用时间的99分位数</td>
</tr>
<tr>
<td>P999</td>
<td>GetOperationStatus 方法调用时间的999分位数</td>
</tr>
<tr>
<td  rowspan=5>GetInfo 方法调用时间</td>
<td>P50</td>
<td  rowspan=5>ms</td>
<td>GetInfo 方法调用时间的50分位数</td>
</tr>
<tr>
<td>P75</td>
<td>GetInfo 方法调用时间的75分位数</td>
</tr>
<tr>
<td>P95</td>
<td>GetInfo 方法调用时间的95分位数</td>
</tr>
<tr>
<td>P99</td>
<td>GetInfo 方法调用时间的99分位数</td>
</tr>
<tr>
<td>P999</td>
<td>GetInfo 方法调用时间的999分位数</td>
</tr>
<tr>
<td  rowspan=5>FetchResults 方法调用时间</td>
<td>P50</td>
<td  rowspan=5>ms</td>
<td>FetchResults 方法调用时间的50分位数</td>
</tr>
<tr>
<td>P75</td>
<td>FetchResults 方法调用时间的75分位数</td>
</tr>
<tr>
<td>P95</td>
<td>FetchResults 方法调用时间的95分位数</td>
</tr>
<tr>
<td>P99</td>
<td>FetchResults 方法调用时间的99分位数</td>
</tr>
<tr>
<td>P999</td>
<td>FetchResults 方法调用时间的999分位数</td>
</tr>
<tr>
<td  rowspan=5>ExecuteStatement 方法调用时间</td>
<td>P50</td>
<td  rowspan=5>ms</td>
<td>ExecuteStatement 方法调用时间的50分位数</td>
</tr>
<tr>
<td>P75</td>
<td>ExecuteStatement 方法调用时间的75分位数</td>
</tr>
<tr>
<td>P95</td>
<td>ExecuteStatement 方法调用时间的95分位数</td>
</tr>
<tr>
<td>P99</td>
<td>ExecuteStatement 方法调用时间的99分位数</td>
</tr>
<tr>
<td>P999</td>
<td>ExecuteStatement 方法调用时间的999分位数</td>
</tr>
<tr>
<td  rowspan=5>CloseSession 方法调用时间</td>
<td>P50</td>
<td  rowspan=5>ms</td>
<td>CloseSession 方法调用时间的50分位数</td>
</tr>
<tr>
<td>P75</td>
<td>CloseSession 方法调用时间的75分位数</td>
</tr>
<tr>
<td>P95</td>
<td>CloseSession 方法调用时间的95分位数</td>
</tr>
<tr>
<td>P99</td>
<td>CloseSession 方法调用时间的99分位数</td>
</tr>
<tr>
<td>P999</td>
<td>CloseSession 方法调用时间的999分位数</td>
</tr>
<tr>
<td  rowspan=5>OpenSession 方法调用时间</td>
<td>P50</td>
<td  rowspan=5>ms</td>
<td>OpenSession 方法调用时间的50分位数</td>
</tr>
<tr>
<td>P75</td>
<td>OpenSession 方法调用时间的75分位数</td>
</tr>
<tr>
<td>P95</td>
<td>OpenSession 方法调用时间的95分位数</td>
</tr>
<tr>
<td>P99</td>
<td>OpenSession 方法调用时间的99分位数</td>
</tr>
<tr>
<td>P999</td>
<td>OpenSession 方法调用时间的999分位数</td>
</tr>
<tr>
<td>当前 Lauch Engine 操作数</td>
<td>Count</td>
<td>个</td>
<td>当前 Lauch Engine 操作数</td>
</tr>
<tr>
<td>当前 Execute Statement 操作数</td>
<td>Count</td>
<td>个</td>
<td>当前 Execute Statement 操作数</td>
</tr>
<tr>
<td>当前操作数</td>
<td>Count</td>
<td>个</td>
<td>当前操作数</td>
</tr>
<tr>
<td  rowspan=6>JVM 线程数量</td>
<td>ThreadsNew</td>
<td>个</td>
<td>处于 NEW 状态的线程数量</td>
</tr>
<tr>
<td>ThreadsRunnable</td>
<td>个</td>
<td>处于 RUNNABLE 状态的线程数量</td>
</tr>
<tr>
<td>ThreadsBlocked</td>
<td>个</td>
<td>处于 BLOCKED 状态的线程数量</td>
</tr>
<tr>
<td>ThreadsWaiting</td>
<td>个</td>
<td>处于 WAITING 状态的线程数量</td>
</tr>
<tr>
<td>ThreadsTimedWaiting</td>
<td>个</td>
<td>处于 TIMED WAITING 状态的线程数量</td>
</tr>
<tr>
<td>ThreadsTerminated</td>
<td>个</td>
<td>处于 Terminated 状态的线程数量</td>
</tr>
</table>
