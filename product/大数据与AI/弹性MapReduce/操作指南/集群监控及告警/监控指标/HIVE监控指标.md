### HIVE-HiveMetaStore 
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
<td >MemHeapUsedM </td>
<td >MB </td>
<td >JVM 当前已经使用的 HeapMemory 的数量</td>
</tr><tr>
<td >MemHeapCommittedM	</td>
<td >MB </td>
<td >JVM 已经提交的 HeapMemory 的数量</td>
</tr><tr>
<td >MemHeapMaxM </td>
<td >MB </td>
<td >JVM 配置的 HeapMemory 的数量</td>
</tr><tr>
<td >MemHeapInitM </td>
<td >MB </td>
<td >JVM 初始 HeapMem 的数量</td>
</tr><tr>
<td >MemNonHeapUsedM </td>
<td >MB </td>
<td >JVM 当前已经使用的 NonHeapMemory 的数量</td>
</tr><tr>
<td >MemNonHeapCommittedM </td>
<td >MB </td>
<td >JVM 当前已经提交的 NonHeapMemory 的数量</td>
</tr><tr>
<td >MemNonHeapInitM </td>
<td >MB </td>
<td >JVM 初始 NonHeapMem 的数量</td>
</tr><tr>
<td rowspan=2>文件描述符数</td>
<td >OpenFileDescriptorCount</td>
<td >个</td>
<td >已打开文件描述符数量</td>
</tr><tr>
<td >MaxFileDescriptorCount</td>
<td >个</td>
<td >最大文件描述符数</td>
</tr><tr>
<td rowspan=2>CPU 利用率</td>
<td >ProcessCpuLoad</td>
<td >%</td>
<td >进程 CPU 利用率</td>
</tr><tr>
<td >SystemCpuLoad</td>
<td >%</td>
<td >系统 CPU 利用率</td>
</tr><tr>
<td >CPU 使用时间占比</td>
<td >CPURate</td>
<td >seconds/second</td>
<td > CPU 使用时间占比</td>
</tr><tr>
<td rowspan=2>工作线程数</td>
<td >DaemonThreadCount</td>
<td >个</td>
<td >守护线程数</td>
</tr><tr>
<td >ThreadCount</td>
<td >个</td>
<td >线程总数</td>		
</tr><tr>
<td >CPU 累计使用时间</td>
<td >ProcessCpuTime</td>
<td >ms</td>
<td >CPU 累计使用时间</td>
</tr><tr>
<td >进程运行时长</td>
<td >Uptime</td>
<td >s</td>
<td >进程运行时长</td>
</tr><tr>
<td >GC 额外睡眠时间</td>
<td >ExtraSleepTime</td>
<td >s</td>
<td >GC 额外睡眠时间</td>
</tr>
</table>

### HIVE-HiveServer2
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
<td >堆内存使用占比 </td>
<td >MemHeapUsedRate </td>
<td >% </td>
<td >JVM 当前已经使用的 HeapMemory 的数量所占 JVM 配置的 HeapMemory 的数量的百分比</td>
</tr><tr>
<td> CPU 利用率</td>
<td> ProcessCpuLoad </td>
<td > % </td>
<td > CPU 利用率 </td>
</tr><tr>
<td> CPU 使用时间占比</td>
<td> CPUUsedRate </td>
<td > seconds/second</td>
<td > CPU 使用时间占比</td>
</tr><tr>
<td rowspan=2> 文件描述符数</td>
<td>MaxFileDescriptorCount </td>
<td > 个 </td>
<td > 最大文件描述符数 </td>
</tr><tr>
<td>OpenFileDescriptorCount </td>
<td > 个 </td>
<td > 已打开文件描述符数 </td>
</tr><tr>
<td> CPU 累计使用时间</td>
<td>ProcessCpuTime </td>
<td > ms </td>
<td > CPU 累计使用时间 </td>
</tr><tr>
<td> 进程运行时长 </td>
<td> Uptime </td>
<td > s </td>
<td > 进程运行时长 </td>
</tr><tr>
<td rowspan=2> 工作线程数</td>
<td> DaemonThreadCount </td>
<td > 个 </td>
<td > Daemon 线程数 </td>
</tr><tr>
<td> ThreadCount </td>
<td > 个 </td>
<td > 总线程数 </td>
</tr><tr>
<td rowspan=2> Driver 执行时延</td>
<td> 99th_percentile </td>
<td > ms </td>
<td > Driver 执行99%的时延 </td>
</tr><tr>
<td> Avg </td>
<td > ms </td>
<td > Driver 执行平均执行时延 </td>
</tr><tr>
<td >打开连接数量 </td>
<td>NumOpenConnections </td>
<td > 个 </td>
<td > 打开连接数量 </td>
</tr><tr>
<td >hs2异步线程池当前大小 </td>
<td >PoolSize </td>
<td > 个 </td>
<td > hs2异步线程池当前大小 </td>
</tr><tr>
<td > hs2异步操作队列当前大小 </td>
<td>QueueSize </td>
<td > 个 </td>
<td > hs2 异步操作队列当前大小 </td>
</tr><tr>
<td rowspan=4> Hive 操作数量 </td>
<td> Closed </td>
<td > 个 </td>
<td > 关闭的操作数量 </td>
</tr><tr>
<td>Finished </td>
<td > 个 </td>
<td > 完成的操作数量 </td>
</tr><tr>
<td>Canceled </td>
<td > 个 </td>
<td > 取消的操作数量 </td>
</tr><tr>
<td>Error </td>
<td > 个/</td>
<td > 出错的操作数量 </td>
</tr><tr>
<td> GC 额外睡眠时间 </td>
<td> ExtraSleepTime </td>
<td >-</td>
<td >-</td>
</tr>
</table>

### HIVE-HiveWebHcat
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
</tr>
</table>
