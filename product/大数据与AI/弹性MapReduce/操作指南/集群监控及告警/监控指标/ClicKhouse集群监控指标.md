### CLICKHOUSE-Metrics
<table>
<tr>
<th width=20%>标题 </th>
<th width=20%>指标名称</th>
<th width=15%>指标单位</th>
<th width=45%>指标含义 </th>
</tr><tr>
<td rowspan=2>网络连接数 </td>
<td >tcp</td>
<td >个</td>
<td >TCP 服务器的连接数</td>
</tr><tr>
<td >http</td>
<td >个</td>
<td >HTTP 服务器的连接数</td>
</tr><tr>
<td >ZK 事件订阅数</td>
<td >watches</td>
<td >个</td>
<td >ZK 事件订阅数</td>
</tr><tr>
<td >ZooKeeper 中保存的临时节点数</td>
<td >ephemeralNode</td>
<td >个</td>
<td >ZooKeeper 中保存的临时节点数</td>
</tr><tr>
<td rowspan=2>BackgroundPool 中的活跃任务数</td>
<td >backgroundPoolTask</td>
<td >个</td>
<td >BackgroundProcessingPool 中的活跃任务数</td>
</tr><tr>
<td >backgroundSchedulePoolTask</td>
<td >个</td>
<td >BackgroundSchedulePool 中的活跃任务数</td>
</tr><tr>
<td >在 Context 中等待锁的线程数</td>
<td >contextLockWait</td>
<td >个</td>
<td >在 Context 中等待锁的线程数</td>
</tr><tr>
<td >被抑制的 Insert 查询数</td>
<td >delayedInserts</td>
<td >个</td>
<td >被抑制的 Insert 查询数</td>
</tr><tr>
<td >cache 类型字典的数据源中的请求数</td>
<td >dictCacheRequests</td>
<td >个</td>
<td >cache 类型字典的数据源中的请求数</td>
</tr><tr>
<td >pending 的异步插入到分布式表的文件数</td>
<td >distributedSend</td>
<td >个</td>
<td >pending 的异步插入到分布式表的文件数</td>
</tr><tr>
<td rowspan=4>线程数</td>
<td >global</td>
<td >个</td>
<td >全局线程池中的线程数</td>
</tr><tr>
<td >globalActive</td>
<td >个</td>
<td >全局线程池中活跃的线程数</td>
</tr><tr>
<td >local</td>
<td >个</td>
<td >本地线程池中的线程数</td>
</tr><tr>
<td >localActive</td>
<td >个</td>
<td >本地线程池中活跃的线程数</td>
</tr><tr>
<td >参与 leader 选举的副本数量</td>
<td >leaderElection</td>
<td >个</td>
<td >参与 leader 选举的副本数量</td>
</tr><tr>
<td rowspan=2>Replicated table 的数量</td>
<td >leaderReplica</td>
<td >个</td>
<td >属于 leader 的 Replicated table 的数量</td>
</tr><tr>
<td >readonlyReplica</td>
<td >个</td>
<td >处于只读状态的 Replicated table 的数量</td>
</tr><tr>
<td rowspan=4>分配的内存总量</td>
<td >memoryTracking</td>
<td >GB</td>
<td >当前执行的查询中所分配的内存总量</td>
</tr><tr>
<td >backgroundProcessingPool</td>
<td >GB</td>
<td >后台处理池中分配的内存总量</td>
</tr><tr>
<td >backgroundSchedulePool</td>
<td >GB</td>
<td >后台调度池中所分配的内存总量</td>
</tr><tr>
<td >memoryTrackingForMerges</td>
<td >GB</td>
<td >后台 merges 所分配的内存总量</td>
</tr><tr>
<td >正在后台执行的 merge 数量</td>
<td >merge</td>
<td >个</td>
<td >正在后台执行的 merge 数量</td>
</tr><tr>
<td rowspan=2>打开的文件数量</td>
<td >read</td>
<td >个</td>
<td >打开的可读文件的数量</td>
</tr><tr>
<td >write</td>
<td >个</td>
<td >打开的可写文件的数量</td>
</tr><tr>
<td >表变更的次数</td>
<td >partMutation</td>
<td >个</td>
<td >表变更的次数</td>
</tr><tr>
<td >查询处理的线程数量</td>
<td >queryThread</td>
<td >个</td>
<td >查询处理的线程数量</td>
</tr><tr>
<td >停止或等待的查询数量</td>
<td >queryPreempted</td>
<td >个</td>
<td >停止或等待的查询数量</td>
</tr><tr>
<td rowspan=2>系统调用的数量</td>
<td >read</td>
<td >个</td>
<td >读系统调用的数量</td>
</tr><tr>
<td >write</td>
<td >个</td>
<td >写系统调用的数量</td>
</tr><tr>
<td rowspan=3>数据块数量</td>
<td >fetch</td>
<td >个</td>
<td >从副本收集的数据块数量</td>
</tr><tr>
<td >send</td>
<td >个</td>
<td >发送到副本的数量块数量</td>
</tr><tr>
<td >check</td>
<td >个</td>
<td >检查一致性的数据块数量</td>
</tr><tr>
<td >server 的修改</td>
<td >revision</td>
<td >个</td>
<td >server 的修改</td>
</tr><tr>
<td >版本号</td>
<td >version</td>
<td >1</td>
<td >版本号</td>
</tr><tr>
<td rowspan=4>等待持有读写锁的线程数量</td>
<td >waitingRead</td>
<td >个</td>
<td >等待读表的读写锁的线程数量</td>
</tr><tr>
<td >waitingWrite</td>
<td >个</td>
<td >等待写表的读写锁的线程数量</td>
</tr><tr>
<td >activeRead</td>
<td >个</td>
<td >在一个表的读写锁中持有读锁的线程数</td>
</tr><tr>
<td >activeWrite</td>
<td >个</td>
<td >在一个表的读写锁中持有写锁的线程数</td>
</tr><tr>
<td >Buffer tables 中的行数</td>
<td >storageBufferRows</td>
<td >个</td>
<td >Buffer tables 中的行数</td>
</tr><tr>
<td >Buffer tables 中的字节数</td>
<td >storageBufferBytes</td>
<td >MB</td>
<td >Buffer tables 中的字节数</td>
</tr>
</table>

### CLICKHOUSE-Events
<table>
<tr>
<th width=20%>标题 </th>
<th width=20%>指标名称</th>
<th width=15%>指标单位</th>
<th width=45%>指标含义 </th>
</tr><tr>
<td rowspan=3>查询数 </td>
<td >total</td>
<td >个</td>
<td >可能执行的查询总数</td>
</tr><tr>
<td >select</td>
<td >个</td>
<td >可能执行的 Select 查询数</td>
</tr><tr>
<td >insert</td>
<td >个</td>
<td >可能执行的 Insert 查询数</td>
</tr><tr>
<td >insert行数</td>
<td >insertedRows</td>
<td >个</td>
<td >被插入到所有表中的行数</td>
</tr><tr>
<td >insert字节数</td>
<td >insertedBytes</td>
<td >个</td>
<td >被插入到所有表中的字节数</td>
</tr><tr>
<td rowspan=2>等待系统调用的总时间</td>
<td >read</td>
<td >微秒</td>
<td >等待读系统调用的总时间</td>
</tr><tr>
<td >write</td>
<td >微秒</td>
<td >等待写系统调用的总时间</td>
</tr><tr>
<td >已打开的文件数</td>
<td >fileOpen</td>
<td >个</td>
<td >已打开的文件数</td>
</tr><tr>
<td rowspan=2>来自文件描述器的读写个数</td>
<td >read</td>
<td >个</td>
<td >来自文件描述器的读个数</td>
</tr><tr>
<td >write</td>
<td >个</td>
<td >来自文件描述器的写个数</td>
</tr><tr>
<td  rowspan=2>来自文件描述器的读写字节数</td>
<td >read</td>
<td >MB</td>
<td >来自文件描述器的读字节数</td>
</tr><tr>
<td >write</td>
<td >MB</td>
<td >写入文件描述器的字节数</td>
</tr><tr>
<td rowspan=3>处理线程花费的总时间</td>
<td >realtime</td>
<td >微秒</td>
<td >处理线程花费的总时间</td>
</tr><tr>
<td >user</td>
<td >微秒</td>
<td >在用户空间下处理线程在执行 CPU 指令花费的总时间</td>
</tr><tr>
<td >system</td>
<td >微秒</td>
<td >在操作系统内核空间下处理线程在执行 CPU 指令花费的总时间</td>
</tr><tr>
<td >编译的正则表达式数</td>
<td >regexpCreated</td>
<td >个</td>
<td >编译的正则表达式数</td>
</tr>
</table>

### CLICKHOUSE-Asynchronous_metrics

<table>
<tr>
<th width=20%>标题 </th>
<th width=20%>指标名称</th>
<th width=15%>指标单位</th>
<th width=45%>指标含义 </th>
</tr><tr>
<td >StorageMergeTree 的 marks 的缓存大小</td>
<td >markCacheBytes</td>
<td >MB</td>
<td >StorageMergeTree 的 marks 的缓存大小</td>
</tr><tr>
<td >StorageMergeTree 的 marks 的缓存文件数</td>
<td >markCacheFiles</td>
<td >个</td>
<td >StorageMergeTree 的 marks 的缓存文件数</td>
</tr><tr>
<td >活跃数据块的最大值</td>
<td >maxPartCountForPartition</td>
<td >个</td>
<td >partitions 中最大的活跃数据块的数量</td>
</tr><tr>
<td >数据库数量</td>
<td >databaseCount</td>
<td >个</td>
<td >数据库数量</td>
</tr><tr>
<td >数据表数量</td>
<td >tableCount</td>
<td >个</td>
<td >数据表数量</td>
</tr><tr>
<td rowspan=2>replica 最大时延</td>
<td >absolute</td>
<td >微秒</td>
<td >最大的 replica 队列时延</td>
</tr><tr>
<td >relative</td>
<td >微秒</td>
<td >来自其他块的绝对时延的差异的最大值</td>
</tr><tr>
<td >待完成的操作队列的大小</td>
<td >replicasMaxQueueSize</td>
<td >个</td>
<td >待完成的操作队列的大小</td>
</tr>
</table>
