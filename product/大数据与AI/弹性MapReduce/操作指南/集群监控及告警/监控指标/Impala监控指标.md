>! Impala 指标目前仅支持 Impala3.4.0 及以上版本。
### Impala-CATALOG
<table>
<tr>
<th width=20%>标题 </th>
<th width=20%>指标名称</th>
<th width=15%>指标单位</th>
<th width=45%>指标含义 </th>
</tr><tr>
<td >常驻内存集</td>
<td >RSS</td>
<td >bytes</td>
<td >常驻内存集</td>
</tr><tr>
<td rowspan=7>JVM 内存</td>
<td >MemHeapInitM</td>
<td >MB</td>
<td >JVM 初始 HeapMemory 的数量峰值</td>
</tr><tr>
<td >MemHeapCommittedM</td>
<td >MB</td>
<td >JVM 当前已经提交的 HeapMemory 的数量</td>
</tr><tr>
<td >MemHeapMaxM</td>
<td >MB</td>
<td >JVM 配置的 HeapMemory 的数量</td>
</tr><tr>
<td >MemHeapUsedM</td>
<td >MB</td>
<td >JVM 当前已经使用的 HeapMemory 的数量</td>
</tr><tr>
<td >MemNonHeapInitM</td>
<td >MB</td>
<td >JVM 初始 NonHeapMemory的数量</td>
</tr><tr>
<td >MemNonHeapCommittedM</td>
<td >MB</td>
<td >JVM 当前已经提交的 NonHeapMemory 的数量</td>
</tr><tr>
<td >MemNonHeapUsedM</td>
<td >MB</td>
<td >JVM 当前已经使用的 NonHeapMemory 的数量</td>
</tr><tr>
<td rowspan=5>守护进程到 StateStore 的心跳间隔</td>
<td >Last</td>
<td >s</td>
<td >守护进程到 StateStore 的最近心跳间隔</td>
</tr><tr>
<td >Max</td>
<td >s</td>
<td >守护进程到 StateStore 的最大心跳间隔</td>
</tr><tr>
<td >Mean</td>
<td >s</td>
<td >守护进程到 StateStore 的平均心跳间隔</td>
</tr><tr>
<td >Min</td>
<td >s</td>
<td >守护进程到 StateStore 的最小心跳间隔</td>
</tr><tr>
<td >Stddev</td>
<td >s</td>
<td >守护进程到 StateStore 的心跳之间的标准偏差</td>
</tr><tr>
<td rowspan=5>TCMALLOC 内存</td>
<td >Used</td>
<td >bytes</td>
<td >程序使用的字节数</td>
</tr><tr>
<td >PageheapFreeBytes</td>
<td >bytes</td>
<td >页堆中空闲映射页的字节数</td>
</tr><tr>
<td >PageheapUnmappedBytes</td>
<td >bytes</td>
<td >页堆中空闲、未映射页的字节数</td>
</tr><tr>
<td >PhysicalBytesReserved</td>
<td >bytes</td>
<td >计算进程使用的物理内存量</td>
</tr><tr>
<td >TotalBytesReserved</td>
<td >bytes</td>
<td >TCMalloc 保留的系统内存字节数</td>
</tr><tr>
<td >活跃连接数</td>
<td >Thrift_Server_Connections_Used</td>
<td >个</td>
<td >活跃连接数</td>
</tr><tr>
<td >进程运行时间</td>
<td >Uptime</td>
<td >s</td>
<td >进程运行时间</td>
</tr><tr>
<td rowspan=2>文件描述符数</td>
<td >MaxFileDescriptorCount</td>
<td >个</td>
<td >最大文件描述符数</td>
</tr><tr>
<td >OpenFileDescriptorCount</td>
<td >个</td>
<td >已打开文件描述符数</td>
</tr><tr>
<td rowspan=2>线程数</td>
<td >ThreadCount</td>
<td >个</td>
<td >总线程数量</td>
</tr><tr>
<td >DaemonThreadCount</td>
<td >个</td>
<td >Daemon 线程数</td>
</tr><tr>
<td rowspan=2>CPU 利用率</td>
<td >ProcessCpuLoad</td>
<td >%</td>
<td >进程 CPU 利用率</td>
</tr><tr>
<td >SystemCpuLoad</td>
<td >个</td>
<td >系统 CPU 利用率</td>
</tr></table>

### Impala-STATESTORE
<table>
<tr>
<th width=20%>标题 </th>
<th width=20%>指标名称</th>
<th width=15%>指标单位</th>
<th width=45%>指标含义 </th>
</tr><tr>
<td >常驻内存集</td>
<td >RSS</td>
<td >bytes</td>
<td >常驻内存集</td>
</tr><tr>
<td rowspan=5>TCMALLOC 内存</td>
<td >Used</td>
<td >bytes</td>
<td >程序使用的字节数</td>
</tr><tr>
<td >PageheapFreeBytes</td>
<td >bytes</td>
<td >页堆中空闲映射页的字节数</td>
</tr><tr>
<td >PageheapUnmappedBytes</td>
<td >bytes</td>
<td >页堆中空闲、未映射页的字节数</td>
</tr><tr>
<td >PhysicalBytesReserved</td>
<td >bytes</td>
<td >计算进程使用的物理内存量</td>
</tr><tr>
<td >TotalBytesReserved</td>
<td >bytes</td>
<td >TCMalloc 保留的系统内存字节数</td>
</tr><tr>
<td >连接数</td>
<td >Used</td>
<td >个</td>
<td >活跃连接数</td>
</tr><tr>
<td >运行线程数</td>
<td >Count</td>
<td >个</td>
<td >运行线程数</td>
</tr><tr>
<td >StateStore 订阅者数量</td>
<td >Count</td>
<td >个</td>
<td >StateStore 订阅者数量</td>
</tr></table>

### Impala-DAEMON
<table>
<tr>
<th width=20%>标题 </th>
<th width=20%>指标名称</th>
<th width=15%>指标单位</th>
<th width=45%>指标含义 </th>
</tr><tr>
<td rowspan=7>JVM 内存</td>
<td >MemHeapInitM</td>
<td >MB</td>
<td >JVM 初始 HeapMemory 的数量峰值</td>
</tr><tr>
<td >MemHeapCommittedM</td>
<td >MB</td>
<td >JVM 当前已经提交的 HeapMemory 的数量</td>
</tr><tr>
<td >MemHeapMaxM</td>
<td >MB</td>
<td >JVM 配置的 HeapMemory 的数量</td>
</tr><tr>
<td >MemHeapUsedM</td>
<td >MB</td>
<td >JVM 当前已经使用的 HeapMemory 的数量</td>
</tr><tr>
<td >MemNonHeapInitM</td>
<td >MB</td>
<td >JVM 初始 NonHeapMemory的数量</td>
</tr><tr>
<td >MemNonHeapCommittedM</td>
<td >MB</td>
<td >JVM 当前已经提交的 NonHeapMemory 的数量</td>
</tr><tr>
<td >MemNonHeapUsedM</td>
<td >MB</td>
<td >JVM 当前已经使用的 NonHeapMemory 的数量</td>
</tr><tr>
<td rowspan=5>TCMALLOC 内存</td>
<td >Used</td>
<td >bytes</td>
<td >程序使用的字节数</td>
</tr><tr>
<td >PageheapFreeBytes</td>
<td >bytes</td>
<td >页堆中空闲映射页的字节数</td>
</tr><tr>
<td >PageheapUnmappedBytes</td>
<td >bytes</td>
<td >页堆中空闲、未映射页的字节数</td>
</tr><tr>
<td >PhysicalBytesReserved</td>
<td >bytes</td>
<td >计算进程使用的物理内存量</td>
</tr><tr>
<td >TotalBytesReserved</td>
<td >bytes</td>
<td >TCMalloc 保留的系统内存字节数</td>
</tr><tr>
<td rowspan=2>线程数</td>
<td >ThreadCount</td>
<td >个</td>
<td >总线程数量</td>
</tr><tr>
<td >DaemonThreadCount</td>
<td >个</td>
<td >Daemon 线程数</td>
</tr><tr>
<td >进程运行时间</td>
<td >Uptime</td>
<td >s</td>
<td >进程运行时间</td>
</tr><tr>
<td rowspan=2>文件描述符数</td>
<td >MaxFileDescriptorCount</td>
<td >个</td>
<td >最大文件描述符数</td>
</tr><tr>
<td >OpenFileDescriptorCount</td>
<td >个</td>
<td >已打开文件描述符数</td>
</tr><tr>
<td rowspan=2>CPU 利用率</td>
<td >ProcessCpuLoad</td>
<td >%</td>
<td >进程 CPU 利用率</td>
</tr><tr>
<td >SystemCpuLoad</td>
<td >个</td>
<td >系统 CPU 利用率</td>
</tr>
</table>
