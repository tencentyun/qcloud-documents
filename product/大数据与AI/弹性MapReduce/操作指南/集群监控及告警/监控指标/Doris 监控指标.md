### Doris-FE
<table>
<tr>
<th width=20%>标题 </th>
<th width=20%>指标名称</th>
<th width=15%>指标单位</th>
<th width=45%>指标含义 </th>
</tr><tr>
<td rowspan=3>节点信息</td>
<td >FeNodeNum </td>
<td >count </td>
<td >FE 总节点数 </td>
</tr><tr>
<td >BeAliveNum </td>
<td >count </td>
<td >BE 活动节点数 </td>
</tr><tr>
<td >BkDeadNum </td>
<td >count </td>
<td >Broker 死亡节点数 </td>
</tr><tr>			
<td >CONNECTION 数量 </td>
<td >Num </td>
<td >count </td>
<td >	FE 节点 JVM connection 数量</td>
</tr><tr>		
<td rowspan=2>JVM 线程数 </td>
<td >Total </td>
<td >count </td>
<td >FE节点JVM中线程总数，包含daemon线程和非daemon线程</td>
</tr><tr>		
<td >Peak </td>
<td >count </td>
<td >FE节点JVM线程峰值</td>
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
<td rowspan=4>FE 查询延时 </td>
<td >Quantile75 </td>
<td >ms </td>
<td >FE 查询延时的75分位数</td>
</tr><tr>
<td >Quantile95 </td>
<td >ms </td>
<td >FE 查询延时的95分位数 </td>
</tr><tr>
<td >Quantile99 </td>
<td >ms </td>
<td >FE 查询延时的99分位数</td>
</tr><tr>
<td >Quantile999 </td>
<td >ms </td>
<td >FE 查询延时的99.9分位数</td>
</tr><tr>
<td >TABLET_COMPACTION 最高分 </td>
<td >MAX </td>
<td >score </td>
<td >FE tablet 进行compaction时compaction score 最大值</td>
</tr><tr>
<td >SCHEDULED_TABLET 数量 </td>
<td >ScheduledTablet </td>
<td >count </td>
<td >FE 中 scheduled tablet 数量</td>
</tr><tr>
<td rowspan=2>请求响应 </td>
<td >QPS </td>
<td >count </td>
<td >每秒查询率</td>
</tr><tr>			
<td >RPS </td>
<td >count </td>
<td >每秒能处理的请求数目</td>
</tr><tr>			
<td >查询失败率 </td>
<td >ErrRate </td>
<td >% </td>
<td >查询错误率</td>
</tr><tr>			

<td rowspan=6>缓存查询 </td>
<td >SqlModelHitQuery </td>
<td >count </td>
<td >模式为 sql 的 Query 命中 Cache 的数量</td>
</tr><tr>			
<td >PartitionModelHitQuery </td>
<td >count </td>
<td >通过 Partition 命中的 Query 数量</td>
</tr><tr>			
<td >SqlModelQuery </td>
<td >count</td>
<td >识别缓存模式为 sql 的 Query 数量</td>
</tr><tr>		
<td >PartitionModelQuery </td>
<td >count </td>
<td >识别缓存模式为 Partition 的 Query 数量</td>
</tr><tr>			
<td >CachePartitionHit </td>
<td >count </td>
<td >查询中通过 cache 命中的分区数量</td>
</tr><tr>			
<td >CachePartitionScan </td>
<td >count</td>
<td >查询中扫描的所有分区数量</td>
</tr><tr>		
<td rowspan=2>ROUTINE_LOAD 行数 </td>
<td >TotalRows </td>
<td >count</td>
<td >FE routine load的行数</td>
</tr><tr>		
<td >ErrorRows </td>
<td >count</td>
<td >FE routine load 错误的行数</td>
</tr><tr>		

<td rowspan=4>TRANSACTION 状态统计 </td>
<td >Reject </td>
<td >count</td>
<td >FE 被拒绝的 transaction 数量</td>
</tr><tr>		
<td >Begin </td>
<td >count</td>
<td >FE 开始的 transaction 数量</td>
</tr><tr>		
<td >Success </td>
<td >count</td>
<td >FE 成功的 transaction 数量</td>
</tr><tr>		
<td >Failed </td>
<td >count</td>
<td >FE 失败的 transaction 数量</td>
</tr><tr>		
<td rowspan=2>IMAGE 数量 </td>
<td >Write </td>
<td >count</td>
<td >	FE image write 的数量</td>
</tr><tr>		
<td >Push </td>
<td >count</td>
<td >	FE image push 的数量</td>
</tr><tr>		
<td rowspan=2>ALTER 任务统计</td>
<td >RollupRunning </td>
<td >count</td>
<td >	运行中的 alter job,类型为 ROLLUP 的数量</td>
</tr><tr>		
<td >SchemaChangeRunning </td>
<td >count</td>
<td >	运行中的 alter job,类型为 SCHEMA_CHANGE 的数量</td>
</tr><tr>		
<td rowspan=7>UNKNOWN_LOAD 任务统计</td>
<td >UNKNOWN </td>
<td >count</td>
<td >	类型为 UNKNOWN，状态为 UNKNOWN 的 load job 数量</td>
</tr><tr>		
<td >PENDING </td>
<td >count</td>
<td >	类型为 UNKNOWN，状态为 PENDING 的 load job 数量</td>
</tr><tr>		
<td >ETL </td>
<td >count</td>
<td >	类型为 UNKNOWN，状态为 ETL 的 load job 数量</td>
</tr><tr>		
<td >LOADING </td>
<td >count</td>
<td >	类型为 UNKNOWN，状态为 LOADING 的 load job 数量</td>
</tr><tr>		
<td >COMMITTED </td>
<td >count</td>
<td >	类型为 UNKNOWN，状态为 COMMITTED 的 load job 数量</td>
</tr><tr>		
<td >FINISHED </td>
<td >count</td>
<td >	类型为 UNKNOWN，状态为 FINISHED 的 load job 数量</td>
</tr><tr>		
<td >CANCELLED </td>
<td >count</td>
<td >	类型为 UNKNOWN，状态为 CANCELLED 的 load job 数量</td>
</tr><tr>		

<td rowspan=7>SPARK_LOAD 任务统计</td>
<td >UNKNOWN </td>
<td >count</td>
<td >	类型为 SPARK，状态为 UNKNOWN 的 load job 数量</td>
</tr><tr>		
<td >PENDING </td>
<td >count</td>
<td >	类型为 SPARK，状态为 PENDING 的 load job 数量</td>
</tr><tr>		
<td >ETL </td>
<td >count</td>
<td >	类型为 SPARK，状态为 ETL 的 load job 数量</td>
</tr><tr>		
<td >LOADING </td>
<td >count</td>
<td >	类型为 SPARK，状态为 LOADING 的 load job 数量</td>
</tr><tr>		
<td >COMMITTED </td>
<td >count</td>
<td >	类型为 SPARK，状态为 COMMITTED 的 load job 数量</td>
</tr><tr>		
<td >FINISHED </td>
<td >count</td>
<td >	类型为 SPARK，状态为 FINISHED 的 load job 数量</td>
</tr><tr>		
<td >CANCELLED </td>
<td >count</td>
<td >	类型为 SPARK，状态为 CANCELLED 的 load job 数量</td>
</tr><tr>	

<td rowspan=7>DELETE_LOAD 任务统计</td>
<td >UNKNOWN </td>
<td >count</td>
<td >	类型为 DELETE，状态为 UNKNOWN 的 load job 数量</td>
</tr><tr>		
<td >PENDING </td>
<td >count</td>
<td >	类型为 DELETE，状态为 PENDING 的 load job 数量</td>
</tr><tr>		
<td >ETL </td>
<td >count</td>
<td >	类型为 DELETE，状态为 ETL 的 load job 数量</td>
</tr><tr>		
<td >LOADING </td>
<td >count</td>
<td >	类型为 DELETE，状态为LOADING 的 load job 数量</td>
</tr><tr>		
<td >COMMITTED </td>
<td >count</td>
<td >	类型为 DELETE，状态为 COMMITTED 的 load job 数量</td>
</tr><tr>		
<td >FINISHED </td>
<td >count</td>
<td >	类型为 DELETE，状态为 FINISHED 的 load job 数量</td>
</tr><tr>		
<td >CANCELLED </td>
<td >count</td>
<td >	类型为 DELETE，状态为 CANCELLED 的 load job 数量</td>
</tr><tr>	

<td rowspan=7>INSERT_LOAD 任务统计</td>
<td >UNKNOWN </td>
<td >count</td>
<td >	类型为 INSERT，状态为 UNKNOWN 的 load job 数量</td>
</tr><tr>		
<td >PENDING </td>
<td >count</td>
<td >	类型为 INSERT，状态为 PENDING 的 load job 数量</td>
</tr><tr>		
<td >ETL </td>
<td >count</td>
<td >	类型为 INSERT，状态为 ETL 的 load job 数量</td>
</tr><tr>		
<td >LOADING </td>
<td >count</td>
<td >	类型为 INSERT，状态为 LOADING 的 load job 数量</td>
</tr><tr>		
<td >COMMITTED </td>
<td >count</td>
<td >	类型为 INSERT，状态为 COMMITTED 的 load job 数量</td>
</tr><tr>		
<td >FINISHED </td>
<td >count</td>
<td >	类型为 INSERT，状态为 FINISHED 的 load job 数量</td>
</tr><tr>		
<td >CANCELLED </td>
<td >count</td>
<td >	类型为 INSERT，状态为 CANCELLED 的 load job 数量</td>
</tr><tr>	

<td rowspan=7>BROKER_LOAD 任务统计</td>
<td >UNKNOWN </td>
<td >count</td>
<td >	类型为 BROKER，状态为 UNKNOWN 的 load job 数量</td>
</tr><tr>		
<td >PENDING </td>
<td >count</td>
<td >	类型为 BROKER，状态为 PENDING 的 load job 数量</td>
</tr><tr>		
<td >ETL </td>
<td >count</td>
<td >	类型为 BROKER，状态为 ETL 的 load job 数量</td>
</tr><tr>		
<td >LOADING </td>
<td >count</td>
<td >	类型为 BROKER，状态为 LOADING 的  load job 数量</td>
</tr><tr>		
<td >COMMITTED </td>
<td >count</td>
<td >	类型为 BROKER，状态为 COMMITTED 的 load job 数量</td>
</tr><tr>		
<td >FINISHED </td>
<td >count</td>
<td >	类型为 BROKER，状态为 FINISHED 的 load job 数量</td>
</tr><tr>		
<td >CANCELLED </td>
<td >count</td>
<td >	类型为 BROKER，状态为 CANCELLED 的 load job 数量</td>
</tr><tr>	

<td rowspan=7>MINI_LOAD 任务统计</td>
<td >UNKNOWN </td>
<td >count</td>
<td >	类型为 MINI，状态为 UNKNOWN 的 load job 数量</td>
</tr><tr>		
<td >PENDING </td>
<td >count</td>
<td >	类型为 MINI，状态为 PENDING 的 load job 数量</td>
</tr><tr>		
<td >ETL </td>
<td >count</td>
<td >	类型为 MINI，状态为 ETL 的 load job 数量</td>
</tr><tr>		
<td >LOADING </td>
<td >count</td>
<td >	类型为 MINI，状态为 LOADING 的 load job 数量</td>
</tr><tr>		
<td >COMMITTED </td>
<td >count</td>
<td >	类型为 MINI，状态为 COMMITTED 的 load job 数量</td>
</tr><tr>		
<td >FINISHED </td>
<td >count</td>
<td >	类型为 MINI，状态为 FINISHED 的 load job 数量</td>
</tr><tr>		
<td >CANCELLED </td>
<td >count</td>
<td >	类型为 MINI，状态为 CANCELLED 的 load job 数量</td>
</tr><tr>	

<td rowspan=7>HADOOP_LOAD 任务统计</td>
<td >UNKNOWN </td>
<td >count</td>
<td >	类型为 HADOOP，状态为 UNKNOWN 的 load job 数量</td>
</tr><tr>		
<td >PENDING </td>
<td >count</td>
<td >	类型为 HADOOP，状态为 PENDING 的 load job 数量</td>
</tr><tr>		
<td >ETL </td>
<td >count</td>
<td >	类型为 HADOOP，状态为 ETL 的 load job 数量</td>
</tr><tr>		
<td >LOADING </td>
<td >count</td>
<td >	类型为 HADOOP，状态为 LOADING 的 load job 数量</td>
</tr><tr>		
<td >COMMITTED </td>
<td >count</td>
<td >	类型为 HADOOP，状态为 COMMITTED 的 load job 数量</td>
</tr><tr>		
<td >FINISHED </td>
<td >count</td>
<td >	类型为 HADOOP，状态为 FINISHED 的 load job 数量</td>
</tr><tr>		
<td >CANCELLED </td>
<td >count</td>
<td >	类型为 HADOOP，状态为 CANCELLED 的 load job 数量</td>
</tr>
</table>

### Doris-BE
<table>
<tr>
<th width=20%>标题 </th>
<th width=20%>指标名称</th>
<th width=15%>指标单位</th>
<th width=45%>指标含义 </th>
</tr><tr>
<td rowspan=4>THRIFT 使用情况</td>
<td >Broker </td>
<td >count </td>
<td >Broker 使用 thrift 的数量 </td>
</tr><tr>
<td >Backend </td>
<td >count </td>
<td >BE 使用 thrift 的数量 </td>
</tr><tr>

<td >Extdatasource </td>
<td >count </td>
<td >extdatasource 使用 thrift 的数量</td>
</tr><tr>
<td >Frontend </td>
<td >count </td>
<td >FE 使用 thrift 的数量</td>
</tr><tr>

<td rowspan=3>STREAMING_LOAD 统计</td>
<td >RequestsTotal </td>
<td >count </td>
<td >streaming load 请求数量 </td>
</tr><tr>
<td >CurrentProcessing </td>
<td >count </td>
<td >streaming load 现有进程数 </td>
</tr><tr>
<td >PipeCount </td>
<td >count </td>
<td >streaming load Pipe 数量</td>
</tr><tr>

<td >STREAMING_LOAD 时间</td>
<td >Duration </td>
<td >ms </td>
<td >streaming load 持续时间 </td>
</tr><tr>
<td >STREAMING_LOAD 数据量 </td>
<td >LoadTotal </td>
<td >bytes </td>
<td >stream load 导入的数据大小</td>
</tr><tr>
<td rowspan=3>FRAGMENT 统计 </td>
<td >PlanFragment </td>
<td >count </td>
<td >plan fragment 数量</td>
</tr><tr>
<td >Endpoint </td>
<td >count </td>
<td >DataStream 的数量</td>
</tr><tr>
<td >RequestsTotal </td>
<td >count </td>
<td >fragment 的请求次数</td>
</tr><tr>
<td >FRAGMENT 请求时间 </td>
<td >Duration </td>
<td >μs (微秒) </td>
<td >fragment 的请求时间</td>
</tr><tr>
<td rowspan=2>BE 内存</td>
<td >Total </td>
<td >bytes</td>
<td >BE memory pool 大小</td>
</tr><tr>
<td >Allocated </td>
<td >bytes</td>
<td >BE memory allocated 大小</td>
</tr><tr>
<td rowspan=2>TABLET_COMPACTIO最高分</td>
<td >CumulativeMax </td>
<td >score</td>
<td >tablet 中最大的 base compaction score</td>
</tr><tr>
<td >BaseMax </td>
<td >score</td>
<td >tablet base 最大 compaction 分数</td>
</tr><tr> 			
<td rowspan=2>COMPACTION 数据量 </td>
<td >Cumulative </td>
<td >bytes</td>
<td >Cumulative compaction 的数据量</td>
</tr><tr> 						
<td >Base </td>
<td >bytes</td>
<td >Base compaction 的数据量</td>
</tr><tr> 					

<td rowspan=2>COMPACTION_DELTAS 数据量 </td>
<td >Cumulative </td>
<td >bytes</td>
<td >Cumulative compaction deltas 的数据量</td>
</tr><tr> 						
<td >Base </td>
<td >bytes</td>
<td >Base compaction deltas 的数据量</td>
</tr><tr> 		
<td >COMPACTION 使用的 MemPool 数量 </td>
<td >CurrentConsumption </td>
<td >count</td>
<td >Compaction 使用的 MemPool 总和(所有 Compaction 线程)</td>
</tr><tr> 		

<td rowspan=3>进程文件句柄数</td>
<td >Used </td>
<td >count</td>
<td >	BE 进程使用文件句柄数量</td>
</tr><tr>
<td >SoftLimit </td>
<td >count</td>
<td >	BE 进程文件句柄 soft 限制数量</td>
</tr><tr> 
<td >HardLimit </td>
<td >count</td>
<td >	BE 进程文件句柄 hard 限制数量</td>
</tr><tr> 
<td >进程运行线程数 </td>
<td >NUM </td>
<td >count</td>
<td >	BE 进程运行的线程个数</td>
</tr><tr> 

<td rowspan=4>ENGINE REQUESTS 统计</td>
<td >FailedBaseCompaction </td>
<td >count</td>
<td >	类型为base_compaction，engine 请求失败数量</td>
</tr><tr>
<td >FailedCultCompt </td>
<td >count</td>
<td >	类型为cumulative_compaction，engine 请求失败数量</td>
</tr><tr> 
<td >TotalBaseCompaction </td>
<td >count</td>
<td >	类型为base_compaction，engine 请求总数</td>
</tr><tr> 
<td >TotalCultCompt </td>
<td >count</td>
<td >	类型为cumulative_compaction，engine 请求总数</td>
</tr>
</table>

### Doris-BK
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
<td >进程运行时间 </td>
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
</tr></table>