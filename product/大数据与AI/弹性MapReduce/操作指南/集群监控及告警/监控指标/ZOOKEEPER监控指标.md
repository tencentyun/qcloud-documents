### Zookeeper
<table>
<tr>
<th width=18%>标题 </th>
<th width=20%>指标名称</th>
<th width=22%>指标单位</th>
<th width=40%>指标含义 </th>
<tr></tr>
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
<td >CPU 利用率</td>
<td >ProcessCpuLoad</td>
<td >%</td>
<td >CPU 利用率</td>
</tr><tr>
<td rowspan=2>文件描述符数</td>
<td >zk_max_file_descriptor_count</td>
<td >个</td>
<td >最大文件描述符数</td>
</tr><tr>
<td >zk_open_file_descriptor_count</td>
<td >个</td>
<td >打开文件描述符数</td>
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
<td rowspan=2>工作线程数</td>
<td >DaemonThreadCount</td>
<td >个</td>
<td >Daemon 线程数</td>
</tr><tr>
<td >ThreadCount</td>
<td >个</td>
<td >总线程数</td>
</tr><tr>
<td >连接数</td>
<td >zk_num_alive_connections</td>
<td >个</td>
<td >当前连接数</td>
</tr><tr>
<td rowspan=3>延迟</td>
<td >zk_avg_latency</td>
<td >ms</td>
<td >zk 处理平均延迟</td>
</tr><tr>
<td >zk_max_latency</td>
<td >ms</td>
<td >zk 处理最大时延</td>
</tr><tr>
<td >zk_min_latency</td>
<td >ms</td>
<td >zk 处理最小时延</td>
</tr><tr>
<td rowspan=3>ZONDE 个数</td>
<td >zk_watch_count</td>
<td >个</td>
<td >zk 的 watch 数目</td></tr><tr>
<td >zk_znode_count</td>
<td >个</td>
<td >zk 的 znode 数量</td></tr><tr>
<td >zk_ephemerals_count</td>
<td >个</td>
<td >zk 的临时节点数目</td>
</tr><tr>
<td >数据大小</td>
<td >zk_approximate_data_size</td>
<td >Byte</td>
<td >zk 存储数据量</td>
</tr><tr>
<td >节点状态</td>
<td >zk_server_state</td>
<td >1：主，0：备，2：单机</td>
<td >zk 节点类型</td>
</tr><tr>
<td rowspan=2>接收发送包量</td>
<td >zk_packets_received</td>
<td >个/s</td>
<td >zk 接收的数据包速率</td>
</tr><tr>
<td >zk_packets_sent</td>
<td >个/s</td>
<td >zk 发送的数据包速率</td>
</tr><tr>
<td >排队请求数</td>
<td >zk_outstanding_requests</td>
<td >个</td>
<td >排队请求数</td>
</tr>
</table>
