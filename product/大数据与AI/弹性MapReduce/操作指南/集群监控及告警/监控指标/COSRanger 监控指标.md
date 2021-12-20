### COSRANGER-CosRangerServer
<table>
<tr>
<th width=30%>标题 </th>
<th width=20%>指标名称</th>
<th width=15%>指标单位</th>
<th width=35%>指标含义 </th>
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
<td >CPU 利用率 </td>
<td >ProcessCpuLoad </td>
<td >% </td>
<td >	CPU 利用率</td>
</tr><tr>
<td rowspan=2>文件句柄数 </td>
<td >MaxFileDescriptorCount </td>
<td >个 </td>
<td >最大文件描述符数</td>
</tr><tr>
<td >OpenFileDescriptorCount </td>
<td >个 </td>
<td >已打开文件描述符数</td>
</tr><tr>	
<td >CPU 使用时间 </td>
<td >ProcessCpuTime </td>
<td >ms </td>
<td >CPU 累计使用时间</td>
</tr><tr>	
<td >进程运行时长 </td>
<td >Uptime </td>
<td >s </td>
<td >进程运行时长</td>
</tr><tr>	
<td rowspan=3>工作线程数 </td>
<td >ThreadCount </td>
<td >个 </td>
<td >线程数量</td>
</tr><tr>
<td >PeakThreadCount </td>
<td >个 </td>
<td >峰值线程数量</td>
</tr><tr>			
<td >DaemonThreadCount </td>
<td >个 </td>
<td >后台线程数量</td>
</tr><tr>
<td >- </td>
<td >Leader </td>
<td >-</td>
<td >是否为cosranger主节点</td>
</tr><tr>
<td rowspan=3>check 统计</td>		
<td >PermissionAllowCnt</td>
<td >count(次)</td>
<td >鉴权通过总数</td>
</tr><tr>
<td >AuthDenyCnt</td>
<td >count(次)</td>
<td >认证失败总数</td>
</tr><tr>
<td >PermissionDenyCnt</td>
<td >count(次)</td>
<td >鉴权失败总数</td>
</tr><tr>

<td rowspan=5>认证成功统计</td>
<td >Qps</td>
<td >count(次)</td>
<td >每秒查询率</td>
</tr><tr>
<td >Total_5m</td>
<td >count(次)</td>
<td >五分钟请求总数</td>
</tr><tr>
<td >Total_1m</td>
<td >count(次)</td>
<td >一分钟请求总数</td>
</tr><tr>
<td >Qps_5m</td>
<td >count(次)</td>
<td >五分钟平均请求数</td>
</tr><tr>
<td >Qps_1m</td>
<td >count(次)</td>
<td >一分钟平均请求数</td>
</tr><tr>

<td rowspan=5>accessStat_DELETE 操作统计</td>
<td >Qps</td>
<td >count(次)</td>
<td >每秒查询率</td>
</tr><tr>
<td >Total_5m</td>
<td >count(次)</td>
<td >五分钟请求总数</td>
</tr><tr>
<td >Total_1m</td>
<td >count(次)</td>
<td >一分钟请求总数</td>
</tr><tr>
<td >Qps_5m</td>
<td >count(次)</td>
<td >五分钟平均请求数</td>
</tr><tr>
<td >Qps_1m</td>
<td >count(次)</td>
<td >一分钟平均请求数</td>
</tr><tr>

<td rowspan=5>accessStat_LIST 操作统计</td>
<td >Qps</td>
<td >count(次)</td>
<td >每秒查询率</td>
</tr><tr>
<td >Total_5m</td>
<td >count(次)</td>
<td >五分钟请求总数</td>
</tr><tr>
<td >Total_1m</td>
<td >count(次)</td>
<td >一分钟请求总数</td>
</tr><tr>
<td >Qps_5m</td>
<td >count(次)</td>
<td >五分钟平均请求数</td>
</tr><tr>
<td >Qps_1m</td>
<td >count(次)</td>
<td >一分钟平均请求数</td>
</tr><tr>

<td rowspan=5>accessStat_READ 操作统计</td>
<td >Qps</td>
<td >count(次)</td>
<td >每秒查询率</td>
</tr><tr>
<td >Total_5m</td>
<td >count(次)</td>
<td >五分钟请求总数</td>
</tr><tr>
<td >Total_1m</td>
<td >count(次)</td>
<td >一分钟请求总数</td>
</tr><tr>
<td >Qps_5m</td>
<td >count(次)</td>
<td >五分钟平均请求数</td>
</tr><tr>
<td >Qps_1m</td>
<td >count(次)</td>
<td >一分钟平均请求数</td>
</tr><tr>

<td rowspan=5>accessStat_WRITE 操作统计</td>
<td >Qps</td>
<td >count(次)</td>
<td >每秒查询率</td>
</tr><tr>
<td >Total_5m</td>
<td >count(次)</td>
<td >五分钟请求总数</td>
</tr><tr>
<td >Total_1m</td>
<td >count(次)</td>
<td >一分钟请求总数</td>
</tr><tr>
<td >Qps_5m</td>
<td >count(次)</td>
<td >五分钟平均请求数</td>
</tr><tr>
<td >Qps_1m</td>
<td >count(次)</td>
<td >一分钟平均请求数</td>
</tr><tr>

<td rowspan=5>rpc_getRangerAuthPolicy 调用数统计</td>
<td >Qps</td>
<td >count(次)</td>
<td >每秒查询率</td>
</tr><tr>
<td >Total_5m</td>
<td >count(次)</td>
<td >五分钟请求总数</td>
</tr><tr>
<td >Total_1m</td>
<td >count(次)</td>
<td >一分钟请求总数</td>
</tr><tr>
<td >Qps_5m</td>
<td >count(次)</td>
<td >五分钟平均请求数</td>
</tr><tr>
<td >Qps_1m</td>
<td >count(次)</td>
<td >一分钟平均请求数</td>
</tr><tr>

<td rowspan=5>rpc_checkPermission 调用数统计</td>
<td >Qps</td>
<td >count(次)</td>
<td > 每秒查询率</td>
</tr><tr>
<td > Total_5m</td>
<td >count(次)</td>
<td > 五分钟请求总数</td>
</tr><tr>
<td > Total_1m</td>
<td >count(次)</td>
<td > 一分钟请求总数</td>
</tr><tr>
<td > Qps_5m</td>
<td >count(次)</td>
<td > 五分钟平均请求数</td>
</tr><tr>
<td > Qps_1m</td>
<td >count(次)</td>
<td > 一分钟平均请求数</td>
</tr><tr>

<td rowspan=5>rpc_getDelegationToken 调用数统计</td>
<td >Qps</td>
<td >count(次)</td>
<td >每秒查询率</td>
</tr><tr>
<td >Total_5m</td>
<td >count(次)</td>
<td >五分钟请求总数</td>
</tr><tr>
<td >Total_1m</td>
<td >count(次)</td>
<td >一分钟请求总数</td>
</tr><tr>
<td >Qps_5m</td>
<td >count(次)</td>
<td >五分钟平均请求数</td>
</tr><tr>
<td >Qps_1m</td>
<td >count(次)</td>
<td >一分钟平均请求数</td>
</tr><tr>

<td rowspan=5>rpc_renewDelegationToken 调用数统计</td>
<td >Qps</td>
<td >count(次)</td>
<td >每秒查询率</td>
</tr><tr>
<td >Total_5m</td>
<td >count(次)</td>
<td >五分钟请求总数</td>
</tr><tr>
<td >Total_1m</td>
<td >count(次)</td>
<td >一分钟请求总数</td>
</tr><tr>
<td >Qps_5m</td>
<td >count(次)</td>
<td >五分钟平均请求数</td>
</tr><tr>
<td >Qps_1m</td>
<td >count(次)</td>
<td >一分钟平均请求数</td>
</tr><tr>

<td rowspan=5>rpc_cancelDelegationToken 调用数统计 </td>
<td >Qps</td>
<td >count(次)</td>
<td >每秒查询率</td>
</tr><tr>
<td >Total_5m</td>
<td >count(次)</td>
<td >五分钟请求总数</td>
</tr><tr>
<td >Total_1m</td>
<td >count(次)</td>
<td >一分钟请求总数</td>
</tr><tr>
<td >Qps_5m</td>
<td >count(次)</td>
<td >五分钟平均请求数</td>
</tr><tr>
<td >Qps_1m</td>
<td >count(次)</td>
<td >一分钟平均请求数</td>
</tr><tr>

<td rowspan=5>rpc_getSTS 调用数统计</td>
<td >Qps</td>
<td >count(次)</td>
<td >每秒查询率</td>
</tr><tr>
<td >Total_5m</td>
<td >count(次)</td>
<td >五分钟请求总数</td>
</tr><tr>
<td >Total_1m</td>
<td >count(次)</td>
<td >一分钟请求总数</td>
</tr><tr>
<td >Qps_5m</td>
<td >count(次)</td>
<td >五分钟平均请求数</td>
</tr><tr>
<td >Qps_1m</td>
<td >count(次)</td>
<td >一分钟平均请求数</td>
</tr><tr>

<td rowspan=5>cosRpc_getSTS 调用耗时</td>
<td >Cost_Avg</td>
<td >μs (微秒)</td>
<td >当前一秒内平均耗时</td>
</tr><tr>
<td >Cost_Avg_1m</td>
<td >μs(微秒)</td>
<td >一分钟平均耗时</td>
</tr><tr>
<td >Cost_Avg_5m</td>
<td >μs(微秒)</td>
<td >五分钟平均耗时</td>
</tr><tr>
<td >Cost_Max</td>
<td >μs(微秒)</td>
<td >当前一秒内最大耗时</td>
</tr><tr>
<td >Cost_Max_1m</td>
<td >μs(微秒)</td>
<td >一分钟内最大耗时</td>
</tr><tr>

<td rowspan=9>cosRpc_getSTS 调用耗时</td>
<td >Cost_Avg</td>
<td >μs(微秒)</td>
<td >当前一秒内平均耗时</td>
</tr><tr>
<td >Cost_Avg_1m</td>
<td >μs(微秒)</td>
<td >一分钟平均耗时</td>
</tr><tr>
<td >Cost_Avg_5m</td>
<td >μs(微秒)</td>
<td >五分钟平均耗时</td>
</tr><tr>
<td >Cost_Max</td>
<td >μs(微秒)</td>
<td >当前一秒内最大耗时</td>
</tr><tr>
<td >Cost_Max_1m</td>
<td >μs(微秒)</td>
<td >一分钟内最大耗时</td>
</tr><tr>
<td >Cost_Max_5m</td>
<td >μs(微秒)</td>
<td >五分钟内最大耗时</td>
</tr><tr>
<td >Cost_Min</td>
<td >μs(微秒)</td>
<td >当前一秒内最小耗时</td>
</tr><tr>
<td >Cost_Min_1m</td>
<td >μs(微秒)</td>
<td >一分钟内最小耗时</td>
</tr><tr>
<td >Cost_Min_5m</td>
<td >μs(微秒)</td>
<td >五分钟内最小耗时</td>
</tr><tr>

<td rowspan=9>cosRpc_renewDelegationToken 调用耗时 </td>
<td >Cost_Avg</td>
<td >μs(微秒)</td>
<td >当前一秒内平均耗时</td>
</tr><tr>
<td >Cost_Avg_1m</td>
<td >μs(微秒)</td>
<td >一分钟平均耗时</td>
</tr><tr>
<td >Cost_Avg_5m</td>
<td >μs(微秒)</td>
<td >五分钟平均耗时</td>
</tr><tr>
<td >Cost_Max</td>
<td >μs(微秒)</td>
<td >当前一秒内最大耗时</td>
</tr><tr>
<td >Cost_Max_1m</td>
<td >μs(微秒)</td>
<td >一分钟内最大耗时</td>
</tr><tr>
<td >Cost_Max_5m</td>
<td >μs(微秒)</td>
<td >五分钟内最大耗时</td>
</tr><tr>
<td >Cost_Min</td>
<td >μs(微秒)</td>
<td >当前一秒内最小耗时</td>
</tr><tr>
<td >Cost_Min_1m</td>
<td >μs(微秒)</td>
<td >一分钟内最小耗时</td>
</tr><tr>
<td >Cost_Min_5m</td>
<td >μs(微秒)</td>
<td >五分钟内最小耗时</td>
</tr><tr>

<td rowspan=9>cosRpc_cancelDelegationToken 调用耗时 </td>
<td >Cost_Avg</td>
<td >μs(微秒)</td>
<td >当前一秒内平均耗时</td>
</tr><tr>
<td >Cost_Avg_1m</td>
<td >μs(微秒)</td>
<td >一分钟平均耗时</td>
</tr><tr>
<td >Cost_Avg_5m</td>
<td >μs(微秒)</td>
<td >五分钟平均耗时</td>
</tr><tr>
<td >Cost_Max</td>
<td >μs(微秒)</td>
<td >当前一秒内最大耗时</td>
</tr><tr>
<td >Cost_Max_1m</td>
<td >μs(微秒)</td>
<td >一分钟内最大耗时</td>
</tr><tr>
<td >Cost_Max_5m</td>
<td >μs(微秒)</td>
<td >五分钟内最大耗时</td>
</tr><tr>
<td >Cost_Min</td>
<td >μs(微秒)</td>
<td >当前一秒内最小耗时</td>
</tr><tr>
<td >Cost_Min_1m</td>
<td >μs(微秒)</td>
<td >一分钟内最小耗时</td>
</tr><tr>
<td >Cost_Min_5m</td>
<td >μs(微秒)</td>
<td >五分钟内最小耗时</td>
</tr><tr>

<td rowspan=9>cosRpc_getDelegationToken 调用耗时 </td>
<td >Cost_Avg</td>
<td >μs(微秒)</td>
<td >当前一秒内平均耗时</td>
</tr><tr>
<td >Cost_Avg_1m</td>
<td >μs(微秒)</td>
<td >一分钟平均耗时</td>
</tr><tr>
<td >Cost_Avg_5m</td>
<td >μs(微秒)</td>
<td >五分钟平均耗时</td>
</tr><tr>
<td >Cost_Max</td>
<td >μs(微秒)</td>
<td >当前一秒内最大耗时</td>
</tr><tr>
<td >Cost_Max_1m</td>
<td >μs(微秒)</td>
<td >一分钟内最大耗时</td>
</tr><tr>
<td >Cost_Max_5m</td>
<td >μs(微秒)</td>
<td >五分钟内最大耗时</td>
</tr><tr>
<td >Cost_Min</td>
<td >μs(微秒)</td>
<td >当前一秒内最小耗时</td>
</tr><tr>
<td >Cost_Min_1m</td>
<td >μs(微秒)</td>
<td >一分钟内最小耗时</td>
</tr><tr>
<td >Cost_Min_5m</td>
<td >μs(微秒)</td>
<td >五分钟内最小耗时</td>
</tr><tr>

<td rowspan=9>cosRpc_checkPermission 调用耗时</td>
<td >Cost_Avg</td>
<td >μs(微秒)</td>
<td >当前一秒内平均耗时</td>
</tr><tr>
<td >Cost_Avg_1m</td>
<td >μs(微秒)</td>
<td >一分钟平均耗时</td>
</tr><tr>
<td >Cost_Avg_5m</td>
<td >μs(微秒)</td>
<td >五分钟平均耗时</td>
</tr><tr>
<td >Cost_Max</td>
<td >μs(微秒)</td>
<td >当前一秒内最大耗时</td>
</tr><tr>
<td >Cost_Max_1m</td>
<td >μs(微秒)</td>
<td >一分钟内最大耗时</td>
</tr><tr>
<td >Cost_Max_5m</td>
<td >μs(微秒)</td>
<td >五分钟内最大耗时</td>
</tr><tr>
<td >Cost_Min</td>
<td >μs(微秒)</td>
<td >当前一秒内最小耗时</td>
</tr><tr>
<td >Cost_Min_1m</td>
<td >μs(微秒)</td>
<td >一分钟内最小耗时</td>
</tr><tr>
<td >Cost_Min_5m</td>
<td >μs(微秒)</td>
<td >五分钟内最小耗时</td>
</tr><tr>

<td rowspan=9>cosRpc_getRangerAuthPolicy 调用耗时</td>
<td >Cost_Avg</td>
<td >μs(微秒)</td>
<td >当前一秒内平均耗时</td>
</tr><tr>
<td >Cost_Avg_1m</td>
<td >μs(微秒)</td>
<td >一分钟平均耗时</td>
</tr><tr>
<td >Cost_Avg_5m</td>
<td >μs(微秒)</td>
<td >五分钟平均耗时</td>
</tr><tr>
<td >Cost_Max</td>
<td >μs(微秒)</td>
<td >当前一秒内最大耗时</td>
</tr><tr>
<td >Cost_Max_1m</td>
<td >μs(微秒)</td>
<td >一分钟内最大耗时</td>
</tr><tr>
<td >Cost_Max_5m</td>
<td >μs(微秒)</td>
<td >五分钟内最大耗时</td>
</tr><tr>
<td >Cost_Min</td>
<td >μs(微秒)</td>
<td >当前一秒内最小耗时</td>
</tr><tr>
<td >Cost_Min_1m</td>
<td >μs(微秒)</td>
<td >一分钟内最小耗时</td>
</tr><tr>
<td >Cost_Min_5m</td>
<td >μs(微秒)</td>
<td >五分钟内最小耗时</td>
</tr>
</table>
