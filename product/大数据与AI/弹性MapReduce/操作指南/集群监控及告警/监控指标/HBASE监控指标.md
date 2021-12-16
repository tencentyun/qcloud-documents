### HBASE-概览
<table>
<tr>
<th width=20%>标题 </th>
<th width=20%>指标名称</th>
<th width=15%>指标单位</th>
<th width=45%>指标含义 </th>
</tr><tr>
<td rowspan=2>集群处于 RIT Region 个数</td>
<td >ritCount</td>
<td >个</td>
<td >Region in transition 的个数</td>
</tr><tr>
<td >ritCountOverThreshold</td>
<td >个</td>
<td >Region in transition 时间超过阈值的 Region 个数</td>
</tr><tr>
<td >集群 RIT 时间</td>
<td >ritOldestAge</td>
<td >ms</td>
<td >Region in transition 的最老年龄</td>
</tr><tr>
<td >每个 RS 平均 REGION 数</td>
<td >averageLoad</td>
<td >个</td>
<td >每个 ResgionServer 平均 Region 数</td>
</tr><tr>
<td rowspan=2>集群 RS 数量</td>
<td >numRegionServers</td>
<td >个</td>
<td >当前存活的 RegionServer 个数</td>
</tr><tr>
<td >numDeadRegionServers</td>
<td >个</td>
<td >当前Dead的 RegionServer 个数</td>
</tr><tr>
<td rowspan=2>HMaster 读写数据量</td>
<td >receivedBytes</td>
<td >bytes/s</td>
<td >集群接收数据量</td>
</tr><tr>
<td >sentBytes</td>
<td >bytes/s</td>
<td >集群发送数据量</td>
</tr><tr>
<td >集群接口总请求量</td>
<td >clusterRequests</td>
<td >个/s</td>
<td >集群总请求数量</td>
</tr><tr>
<td rowspan=2>集群 Assignment 管理器操作</td>
<td >Assign_num_ops</td>
<td >次</td>
<td >Assign region次数</td>
</tr><tr>
<td >BulkAssign_num_ops</td>
<td >次</td>
<td >Bulk assign region次数</td>
</tr><tr>
<td >集群负载均衡次数</td>
<td >BalancerCluster_num_ops</td>
<td >次</td>
<td >集群负载均衡次数</td>
</tr>
</table>

### HBASE-HMaster
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
<td >RPC 连接数</td>
<td >numOpenConnections</td>
<td >个</td>
<td >RPC 连接数</td>
</tr><tr>
<td rowspan=6>RPC 异常次数</td>
<td >FailedSanityCheckException</td>
<td >次</td>
<td >FailedSanityCheckException 异常次数</td>
</tr><tr>
<td >NotServingRegionException</td>
<td >次</td>
<td >NotServingRegionException 异常次数</td>
</tr><tr>
<td >OutOfOrderScannerNextException</td>
<td >次</td>
<td >OutOfOrderScannerNextException 异常次数</td>
</tr><tr>
<td >RegionMovedException</td>
<td >次</td>
<td >RegionMovedException 异常次数</td>
</tr><tr>
<td >RegionTooBusyException</td>
<td >次</td>
<td >RegionTooBusyException 异常次数</td>
</tr><tr>
<td >UnknownScannerException</td>
<td >次</td>
<td >UnknownScannerException 异常次数</td>
</tr><tr>
<td rowspan=2>RPC 队列请求数</td>
<td >numCallsInPriorityQueue</td>
<td >个</td>
<td >通用队列 RPC 请求数</td>
</tr><tr>
<td >numCallsInReplicationQueue</td>
<td >个</td>
<td >复制队列 RPC 请求数</td>
</tr><tr>
<td rowspan=2>进程启动时间</td>
<td >masterActiveTime</td>
<td >s</td>
<td >Master 进程 Active 时间</td>
</tr><tr>
<td >masterStartTime</td>
<td >s</td>
<td >Master 进程启动时间</td>
</tr>
</table>

### HBASE-RegionServer
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
<td >Region 个数</td>
<td >regionCount</td>
<td >个</td>
<td >Region 个数</td>
</tr><tr>
<td >Region 本地化</td>
<td >percentFilesLocal	</td>
<td >%</td>
<td >Region 的 HFile 位于本地 HDFS data node的比例</td>
</tr><tr>
<td >Region 副本本地化</td>
<td >percentFilesLocalSecondaryRegions</td>
<td >%</td>
<td >Region 副本的 HFile 位于本地 HDFS data node的比例</td>
</tr><tr>
<td rowspan=2>RPC 认证次数</td>
<td >authenticationFailures</td>
<td >次</td>
<td >RPC 认证失败次数</td>
</tr><tr>
<td >authenticationSuccesses</td>
<td >次</td>
<td >RPC 认证成功次数</td>
</tr><tr>
<td >RPC 连接数</td>
<td >numOpenConnections</td>
<td >个</td>
<td >RPC 连接数</td>
</tr><tr>
<td rowspan=6>RPC 异常次数</td>
<td >FailedSanityCheckException</td>
<td >次</td>
<td >FailedSanityCheckException 异常次数</td>
</tr><tr>
<td >NotServingRegionException</td>
<td >次</td>
<td >NotServingRegionException 异常次数</td>
</tr><tr>
<td >OutOfOrderScannerNextException</td>
<td >次</td>
<td >OutOfOrderScannerNextException 异常次数</td>
</tr><tr>
<td >RegionMovedException</td>
<td >次</td>
<td >RegionMovedException 异常次数</td>
</tr><tr>
<td >RegionTooBusyException</td>
<td >次</td>
<td >RegionTooBusyException 异常次数</td>
</tr><tr>
<td >UnknownScannerException</td>
<td >次</td>
<td >UnknownScannerException 异常次数</td>
</tr><tr>
<td rowspan=4>RPC 句柄数</td>
<td >numActiveHandler</td>
<td >个</td>
<td >RPC 句柄数</td>
</tr><tr>
<td >numActiveWriteHandler</td>
<td >个</td>
<td >RPC 读句柄数</td>
</tr><tr>
<td >numActiveReadHandler</td>
<td >个</td>
<td >RPC 写句柄数</td>
</tr><tr>
<td >numActiveScanHandler</td>
<td >个</td>
<td >RPC 扫描句柄数</td>
</tr><tr>
</tr><tr>
<td rowspan=6>RPC 队列请求数</td>
<td >numCallsInPriorityQueue</td>
<td >个</td>
<td >优先队列 RPC 请求数</td>
</tr><tr>
<td >numCallsInReplicationQueue</td>
<td >个</td>
<td >复制队列 RPC 请求数</td>
</tr><tr>
<td >numCallsInPriorityQueue</td>
<td >个</td>
<td >通用队列 RPC 请求数</td>
</tr><tr>
<td >numCallsInWriteQueue</td>
<td >个</td>
<td >写调用队列调用 RPC 请求数</td>
</tr><tr>
<td >numCallsInReadQueue</td>
<td >个</td>
<td >读取调用队列中 RPC 请求数</td>
</tr><tr>
<td >numCallsInScanQueue</td>
<td >个</td>
<td >扫描调用队列中 RPC 请求数</td>
</tr><tr>
<td >WAL 文件数量</td>
<td >hlogFileCount</td>
<td >个</td>
<td >WAL 文件数量</td>
</tr><tr>
<td >WAL 文件大小</td>
<td >hlogFileSize</td>
<td >Byte</td>
<td >WAL 文件大小</td>
</tr><tr>
<td >Memstore 大小</td>
<td >memStoreSize</td>
<td >MB</td>
<td >Memstore 大小</td>
</tr><tr>
<td >Store 个数</td>
<td >storeCount</td>
<td >个</td>
<td >Store 个数</td>
</tr><tr>
<td >Storefile 个数</td>
<td >storeFileCount</td>
<td >个</td>
<td >Storefile 个数</td>
</tr><tr>
<td >Storefile 大小</td>
<td >storeFileSize</td>
<td >MB</td>
<td >Storefile 大小</td>
</tr><tr>、
<td >写磁盘速率</td>
<td >flushedCellsSize</td>
<td >bytes/s</td>
<td >写磁盘速率</td>
</tr><tr>
<td rowspan=4>平均延时</td>
<td >Append_mean</td>
<td >ms</td>
<td >Append 请求平均延时</td>
</tr><tr>
<td >Replay_mean</td>
<td >ms</td>
<td >Replay 请求平均延时</td>
</tr><tr>
<td >Get_mean</td>
<td >ms</td>
<td >Get 请求平均延时</td>
</tr><tr>
<td >updatesBlockedTime</td>
<td >ms</td>
<td >Memstore 可 flush 前的更新阻塞时间</td>
</tr><tr>
<td >RS 写磁盘次数</td>
<td >FlushTime_num_ops</td>
<td >次</td>
<td >Memstore flush 写磁盘次数</td>
</tr><tr>
<td rowspan=3>操作队列请求数</td>
<td >splitQueueLength</td>
<td >个</td>
<td >Split 队列长度</td>
</tr><tr>
<td >compactionQueueLength</td>
<td >个</td>
<td >Compaction 队列长度</td>
</tr><tr>
<td >flushQueueLength</td>
<td >个</td>
<td >Region Flush 队列长度</td>
</tr><tr>
<td >Replay 操作次数</td>
<td >Replay_num_ops</td>
<td >次</td>
<td >Replay 操作次数</td>
</tr><tr>
<td rowspan=5>慢操作次数</td>
<td >slowAppendCount</td>
<td >次</td>
<td >Append 请求时间超过1s的数量</td>
</tr><tr>
<td >slowDeleteCount</td>
<td >次</td>
<td >Delete 请求时间超过1s的数量</td>
</tr><tr>
<td >slowGetCount</td>
<td >次</td>
<td >Get 请求时间超过1s的数量</td>
</tr><tr>
<td >slowIncrementCount</td>
<td >次</td>
<td >Increment 请求时间超过1s的数量</td>
</tr><tr>
<td >slowPutCount</td>
<td >次</td>
<td >Put 请求时间超过1s的数量</td>
</tr><tr>
<td rowspan=2>split 请求</td>
<td >splitRequestCount</td>
<td >次</td>
<td >split 请求数</td>
</tr><tr>
<td >splitSuccessCount</td>
<td >次</td>
<td >split 成功次数</td>
</tr><tr>
<td rowspan=3>缓存块数量</td>
<td >blockCacheCount</td>
<td >个</td>
<td >Block Cache 中的 Block 数量</td>
</tr><tr>
<td >blockCacheHitCount</td>
<td >个</td>
<td >Block Cache hit 请求数</td>
</tr><tr>
<td >blockCacheMissCount</td>
<td >个</td>
<td >Block Cache miss 请求数</td>
</tr><tr>
<td >读缓存命中率</td>
<td >blockCacheExpressHitPercent</td>
<td >%</td>
<td >读缓存命中率</td>
</tr><tr>
<td >缓存块内存占用大小</td>
<td >blockCacheSize</td>
<td >Byte</td>
<td >缓存块内存占用大小</td>
</tr><tr>
<td rowspan=3>索引大小</td>
<td >staticBloomSize</td>
<td >Byte</td>
<td >未压缩的静态 Bloom Filters 大小</td>
</tr><tr>
<td >staticIndexSize</td>
<td >Byte</td>
<td >未压缩的静态索引大小</td>
</tr><tr>
<td >storeFileIndexSize</td>
<td >Byte</td>
<td >磁盘上 storeFile 中的索引大小</td>
</tr><tr>
<td rowspan=2>读写流量</td>
<td >receivedBytes</td>
<td >bytes/s</td>
<td >读写流量</td>
</tr><tr>
<td >sentBytes</td>
<td >bytes/s</td>
<td >接收数据量</td>
</tr><tr>
<td rowspan=10>写请求量</td>
<td >Total</td>
<td >个/s</td>
<td >总请求量，当有Scan请求时，该值会小于读写请求之和</td>
</tr><tr>
<td >Read</td>
<td >个/s</td>
<td >读请求量</td>
</tr><tr>
<td >Write</td>
<td >个/s</td>
<td >写请求量</td>
</tr><tr>
<td >Append_num_ops</td>
<td >个/s</td>
<td >Append 请求量</td>
</tr><tr>
<td >Mutate_num_ops</td>
<td >个/s</td>
<td >Mutate请求量</td>
</tr><tr>
<td >Delete_num_ops</td>
<td >个/s</td>
<td >Delete 请求量</td>
</tr><tr>
<td >Increment_num_ops</td>
<td >个/s</td>
<td >Increment请求量</td>
</tr><tr>
<td >Get_num_ops</td>
<td >个/s</td>
<td >Get 请求量</td>
</tr><tr>
<td >ScanTime_num_ops</td>
<td >个/s</td>
<td >Scan 请求量</td>
</tr><tr>
<td >ScanSize_num_ops</td>
<td >个/s</td>
<td >Scan 请求量</td>
</tr><tr>
<td >mutation 个数</td>
<td >mutationsWithoutWALCount</td>
<td >个</td>
<td >mutation 个数</td>
</tr><tr>
<td >mutation 大小</td>
<td >mutationsWithoutWALSize</td>
<td >Byte</td>
<td >mutation 大小</td>
</tr><tr>
<td >进程启动时间</td>
<td >regionServerStartTime</td>
<td >s</td>
<td >进程启动时间</td>
</tr><tr>
<td >同步Log</td>
<td >	source.sizeOfLogQueue</td>
<td >个</td>
<td >同步Log长度</td>
</tr><tr>
<td >同步耗时</td>
<td >	source.ageOfLastShippedOp</td>
<td >ms</td>
<td >同步耗时</td>
</tr><tr>
<td rowspan=2>请求量</td>
<td >	ReadRequestCount</td>
<td >	个/s</td>
<td >读请求量/s</td>
</tr><tr>
<td >	WriteRequestCount</td>
<td >	个/s</td>
<td >写请求量/s</td>
</tr><tr>
<td rowspan=2>请求量</td>
<td >	Read</td>
<td >	个/s</td>
<td >读请求量/s</td>
</tr><tr>
<td >	Write</td>
<td >	个/s</td>
<td >写请求量/s</td>
</tr><tr>
<td rowspan=2>Store大小</td>
<td >	memstoreSize</td>
<td >	Byte</td>
<td >memstore大小</td>
</tr><tr>
<td >	storeFileSize</td>
<td >	Byte</td>
<td storeFile大小</td>
</tr><tr>
<td rowspan=6>表级别请求延迟</td>		
<td >getTime_99th_percentile</td>
<td >ms</td>
<td >99%请求处理时延</td>
</tr><tr>
<td >scanTime_99th_percentile</td>
<td >ms</td>
<td >99%请求处理时延</td>
</tr><tr>
<td >putTime_99th_percentile</td>
<td >ms</td>
<td >99%请求处理时延</td>
</tr><tr>
<td >incrementTime_99th_percentile</td>
<td >ms</td>
<td >99%请求处理时延</td>
</tr><tr>
<td >appendTime_99th_percentile</td>
<td >ms</td>
<td >99%请求处理时延</td>
</tr><tr>
<td >deleteTime_99th_percentile</td>
<td >ms</td>
<td >99%请求处理时延</td>
</tr><tr>
<td rowspan=2>请求处理时延</td>
<td >99th_percentile</td>
<td >ms</td>
<td >99%请求处理时延</td>
</tr><tr>
<td >99.9th_percentile</td>
<td >ms</td>
<td >99.9%请求处理时延</td>
</tr><tr>
<td rowspan=2>请求排队时延</td>
<td >99th_percentile</td>
<td >ms</td>
<td >99%请求排队时延</td>
</tr><tr>
<td >99.9th_percentile</td>
<td >ms</td>
<td >99.9%请求排队时延</td>
</tr>
</table>
