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
<td >ms/s</td>
<td >GC 额外睡眠时间</td>
</tr><tr>
<td>alter  table 请求时间</td>
<td>HIVE.HMS.API_ALTER_TABLE</td>
<td>ms</td>
<td>alter table 请求平均时间</td>
</tr>
<tr>
<td>alter table with env context 请求时间</td>
<td>HIVE.HMS.API_ALTER_TABLE_WITH_ENV_CONTEXT</td>
<td>ms</td>
<td>alter table with env context 请求平均时间</td>
</tr>
<tr>
<td>create table 请求时间</td>
<td>HIVE.HMS.API_CREATE_TABLE</td>
<td>ms</td>
<td>create table 请求平均时间</td>
</tr>
<tr>
<td>create table with env context 请求时间</td>
<td>HIVE.HMS.API_CREATE_TABLE_WITH_ENV_CONTEXT</td>
<td>ms</td>
<td>create table with env context 请求平均时间</td>
</tr>
<tr>
<td>drop table 请求时间</td>
<td>HIVE.HMS.API_DROP_TABLE</td>
<td>ms</td>
<td>drop table 平均请求时间</td>
</tr>
<tr>
<td>drop table with env context 请求时间</td>
<td>HIVE.HMS.API_DROP_TABLE_WITH_ENV_CONTEXT</td>
<td>ms</td>
<td>drop table with env context 平均请求时间</td>
</tr>
<tr>
<td>get table 请求时间</td>
<td>HIVE.HMS.API_GET_TABLE</td>
<td>ms</td>
<td>get table 平均请求时间</td>
</tr>
<tr>
<td>get tables 请求时间</td>
<td>HIVE.HMS.API_GET_TABLES</td>
<td>ms</td>
<td>get tables 平均请求时间</td>
</tr>
<tr>
<td>get multi table 请求时间</td>
<td>HIVE.HMS.API_GET_MULTI_TABLE</td>
<td>ms</td>
<td>get multi table 平均请求时间</td>
</tr>
<tr>
<td>get table req 请求时间</td>
<td>HIVE.HMS.API_GET_TABLE_REQ</td>
<td>ms</td>
<td>get table req 平均请求时间</td>
</tr>
<tr>
<td>get database 请求时间</td>
<td>HIVE.HMS.API_GET_DATABASE</td>
<td>ms</td>
<td>get database 平均请求时间</td>
</tr>
<tr>
<td>get databases 请求时间</td>
<td>HIVE.HMS.API_GET_DATABASES</td>
<td>ms</td>
<td>get databases 平均请求时间</td>
</tr>
<tr>
<td>get all database 请求时间</td>
<td>HIVE.HMS.API_GET_ALL_DATABASES</td>
<td>ms</td>
<td>get all databases 平均请求时间</td>
</tr>
<tr>
<td>get all functions 请求时间</td>
<td>HIVE.HMS.API_GET_ALL_FUNCTIONS</td>
<td>ms</td>
<td>get all functions 平均请求时间</td>
</tr>
<tr>
<td>当前活跃 create table 请求数</td>
<td>HIVE.HMS.ACTIVE_CALLS_API_CREATE_TABLE</td>
<td>个</td>
<td>当前活跃 create  table 请求数</td>
</tr>
<tr>
<td>当前活跃 drop table 请求数</td>
<td>HIVE.HMS.ACTIVE_CALLS_API_DROP_TABLE</td>
<td>个</td>
<td>当前活跃 drop  table 请求数</td>
</tr>
<tr>
<td>当前活跃 alter table 请求数</td>
<td>HIVE.HMS.ACTIVE_CALLS_API_ALTER_TABLE</td>
<td>个</td>
<td>当前活跃 alter  table 请求数</td>
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
<td >ms/s</td>
<td >GC 额外睡眠时间</td>
</tr><tr>
<td rowspan=5>API 请求数</td>
<td rowspan=5>HIVE.H2.ACTIVE.CALLS.API</td>
<td>Count</td>
<td>当前 serializePlan 请求数</td>
</tr>
<tr>
<td>Count</td>
<td>当前 semanticAnalyze 请求数</td>
</tr>
<tr>
<td>Count</td>
<td>当前 runtask 请求数</td>
</tr>
<tr>
<td>Count</td>
<td>当前 releaseLocks 请求数</td>
</tr>
<tr>
<td>Count</td>
<td>当前 getSplits 数</td>
</tr>
<tr>
<td>SQL 任务处于 PEDING 状态的时间</td>
<td>HIVE.H2.SQL.OPERATION.PENDING</td>
<td>ms</td>
<td>SQL 任务处于 PEDING 状态的平均时间</td>
</tr>
<tr>
<td>SQL 任务处于RUNNING 状态的时间</td>
<td>HIVE.H2.SQL.OPERATION.RUNNING</td>
<td>ms</td>
<td>SQL 任务处于 RUNNING 状态的平均时间</td>
</tr>
<tr>
<td>当前活跃用户数</td>
<td>HIVE.H2.SQL.OPERATION</td>
<td>Count</td>
<td>当前活跃的用户数</td>
</tr>
<tr>
<td>执行查询的时间</td>
<td>HIVE.H2.EXECUTING.QUERIES</td>
<td>ms</td>
<td>执行查询的平均时间</td>
</tr>
<tr>
<td>提交查询的时间</td>
<td>HIVE.H2.SUBMITTED.QUERIES</td>
<td>ms</td>
<td>提交查询的时间</td>
</tr>
<tr>
<td>提交的 Hive on MR 作业数</td>
<td>HIVE.H2.MR.TASKS</td>
<td>Count</td>
<td>提交的 Hive on MR 作业数</td>
</tr>
<tr>
<td>提交的 Hive on Spark 作业数</td>
<td>HIVE.H2.SPARK.TASKS</td>
<td>Count</td>
<td>提交的 Hive on Tez 作业数</td>
</tr>
<tr>
<td>提交的 Hive on Tez 作业数</td>
<td>HIVE.H2.TEZ.TASKS</td>
<td>Count</td>
<td>提交的 Hive on Spark 作业数</td>
</tr>
<tr>
<td>失败查询</td>
<td>HIVE.H2.FAILED.QUERIES.RATE</td>
<td>Count/min</td>
<td>失败查询 OneMinuteRate</td>
</tr>
<tr>
<td rowspan=7>工作线程数</td>
<td rowspan=7>HIVE.H2.THREAD.COUNT</td>
<td>个</td>
<td>JVM  blocked 线程数</td>
</tr>
<tr>
<td>个</td>
<td>JVM  terminate 线程数</td>
</tr>
<tr>
<td>个</td>
<td>JVM  deadlock 线程数</td>
</tr>
<tr>
<td>个</td>
<td>JVM  new 线程数</td>
</tr>
<tr>
<td>个</td>
<td>JVM  runnable 线程数</td>
</tr>
<tr>
<td>个</td>
<td>JVM  timed_waiting 线程数</td>
</tr>
<tr>
<td>个</td>
<td>JVM  waiting 线程数</td>
</tr>
<tr>
<td>会话数量</td>
<td>HIVE.H2.OPEN.SESSIONS</td>
<td>个</td>
<td>打开的会话个数</td>
</tr>
<tr>
<td>当前活跃的 session 个数</td>
<td>HIVE.H2.ACTIVE.SESSIONS</td>
<td>个</td>
<td>活跃的会话个数</td>
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
