### KUDU-概览
<table>
<tr>
<th width=20%>标题 </th>
<th width=20%>指标名称</th>
<th width=15%>指标单位</th>
<th width=45%>指标含义 </th>
</tr><tr>
<td >tablet 数 </td>
<td>TabletRunning</td>
<td>个</td>
<td>所有 tablet server 中当前正在运行的 tablet 总个数</td>
</tr><tr>
<td >tablet 副本数差 </td>
<td>ClusterReplicaSkew</td>
<td>个</td>
<td>承载最多副本的 tablet 服务器上的副本数与承载最少副本的 tablet 服务器上的副本数之间的差异</td>
</tr><tr>
<td >tserver 线程数</td>
<td>ThreadsRunning</td>
<td>个</td>
<td>	所有 tablet server 中当前正在运行的线程数</td>
</tr><tr>
<td >master 线程数</td>
<td>ThreadsRunning</td>
<td>个</td>
<td>	所有 master 中当前正在运行的线程数</td>
</tr><tr>
<td >tserver 日志数</td>
<td>ErrorMessages</td>
<td>个</td>
<td>	所有进程中发出的 ERROR 级日志消息数</td>
</tr><tr>
<td rowspan=2>master 日志数</td>
<td>ErrorMessages</td>
<td>个</td>
<td>所有进程中发出的 ERROR 级日志消息数</td>
</tr><tr>
<td>WarningMessages</td>
<td>个</td>
<td>所有进程中发出的 WARNING 级日志消息数</td>
</tr><tr>
<td>过大的写请求数</td>
<td>OversizedWriteRequests</td>
<td>个</td>
<td>启动后 master 拒绝的对 system catalog tablet 的过大写请求数</td>
</tr>
</table>

### KUDU-Server
<table>
<tr>
<th width=20%>标题 </th>
<th width=20%>指标名称</th>
<th width=15%>指标单位</th>
<th width=45%>指标含义 </th>
</tr><tr>
<td rowspan=2>块缓存命中</td>
<td >BlockCacheHit</td>
<td >次</td>
<td >预期并命中块的查找数。当确定缓存的效率时，使用此值代替 cache_hits</td>
</tr><tr>
<td >BlockCacheMiss</td>
<td >次</td>
<td >预期但未命中块的查找数。当确定缓存的效率时，使用此值代替 cache_misses</td>
</tr><tr>
<td >块缓存使用率</td>
<td >BlockCacheUsage</td>
<td >bytes</td>
<td >块缓存占用的内存</td>
</tr><tr>
<td rowspan=2>文件缓存命中</td>
<td >FileCacheHit</td>
<td >次</td>
<td >预期并命中文件描述符的查找数。当确定缓存的效率时，使用此值代替 cache_hits</td>
</tr><tr>
<td >FileCacheMiss</td>
<td >次</td>
<td >预期但未命中文件描述符的查找数。当确定缓存的效率时，使用此值代替cache_misses</td>
</tr><tr>
<td >文件缓存使用率</td>
<td >FileCacheUsage</td>
<td >个</td>
<td >文件缓存中的条目数</td>
</tr><tr>
<td rowspan=2>Scanner</td>
<td >ActiveScanners</td>
<td >个</td>
<td >当前处于活动状态的 scanner 个数</td>
</tr><tr>
<td >ExpiredScanners</td>
<td >个</td>
<td >自服务启动后由于不活动而过期的 scanner 个数</td>
</tr><tr>
<td rowspan=3>块管理器 block 数</td>
<td >BlockUnderManagement</td>
<td >个</td>
<td >当前管理的数据块数</td>
</tr><tr>
<td >BlockOpenReading</td>
<td >个</td>
<td >当前打开供读取的数据块数</td>
</tr><tr>
<td >BlockOpenWriting</td>
<td >个</td>
<td >当前打开进行写入的数据块数</td>
</tr><tr>
<td >块管理器字节数</td>
<td >BytesUnderManagement</td>
<td >bytes</td>
<td >当前管理的数据块字节数</td>
</tr><tr>
<td rowspan=2>块管理器容器数</td>
<td >ContainersUnderManagement</td>
<td >个</td>
<td >日志块容器数</td>
</tr><tr>
<td >FullContainersUnderManagement</td>
<td >个</td>
<td >完整日志块容器数</td>
</tr><tr>
<td >tablet leader个数</td>
<td >NumRaftLeaders</td>
<td >个</td>
<td >Raft leaders的tablet副本数量</td>
</tr><tr>
<td rowspan=2>tablet session 数</td>
<td >OpenClientSessions</td>
<td >个</td>
<td >此服务器上当前打开的 tablet 复制客户端 session 个数</td>
</tr><tr>
<td >OpemSourceSessions</td>
<td >个</td>
<td >此服务器上当前打开的 tablet 复制源 session 个数</td>
</tr><tr>
<td rowspan=8>tablet 数</td>
<td >TabletBootstrapping</td>
<td >个</td>
<td >当前正在 bootstrap 的 tablet 个数</td>
</tr><tr>
<td >TabletFailed</td>
<td >个</td>
<td >失败的 tablet 个数</td>
</tr><tr>
<td >TabletInitialized</td>
<td >个</td>
<td >当前初始化过的 tablet 个数</td>
</tr><tr>
<td >TabletNotInitialized</td>
<td >个</td>
<td >当前未初始化过的 tablet 个数</td>
</tr><tr>
<td >TabletRunning</td>
<td >个</td>
<td >当前正在运行的 tablet 个数/当前正在运行的线程数</td>
</tr><tr>
<td >TabletShutdown</td>
<td >个</td>
<td >当前关闭的 tablet 个数</td>
</tr><tr>
<td >TabletStopped</td>
<td >个</td>
<td >当前停止的 tablet 个数</td>
</tr><tr>
<td >TabletStopping</td>
<td >个</td>
<td >当前正在停止的 tablet 个数</td>
</tr><tr>
<td rowspan=2>Cpu 时间</td>
<td >CpuStime</td>
<td >毫秒</td>
<td >进程的总系统 CPU 时间</td>
</tr><tr>
<td >CpuUtime</td>
<td >毫秒</td>
<td >进程的用户 CPU 总时间</td>
</tr><tr>
<td rowspan=2>数据路径</td>
<td >DataDirsFailed</td>
<td >个</td>
<td >磁盘当前处于故障状态的数据目录数</td>
</tr><tr>
<td >DataDirsFull</td>
<td >个</td>
<td >磁盘当前已满的数据目录数</td>
</tr><tr>
<td >线程</td>
<td >ThreadsRunning</td>
<td >个</td>
<td >当前正在运行的线程数</td>
</tr><tr>
<td rowspan=2>上下文</td>
<td >InvoluntarySwitches</td>
<td >次</td>
<td >非自发的上下文切换</td>
</tr><tr>
<td >VoluntarySwitches</td>
<td >次</td>
<td >自发的上下文切换</td>
</tr><tr>
<td >自旋锁</td>
<td >SpinlockContentionTime</td>
<td >微秒</td>
<td >自服务器启动后，内部自旋锁上的争用所消耗的时间量</td>
</tr><tr>
<td rowspan=2>日志信息</td>
<td >ErrorMessages</td>
<td >个</td>
<td >应用程序发出的 ERROR 级日志消息数</td>
</tr><tr>
<td >WarningMessages</td>
<td >个</td>
<td >应用程序发出的 WARNING 级日志消息数</td>
</tr><tr>
<td rowspan=5>队列中操作数</td>
<td >TotalCount</td>
<td >个</td>
<td >总数</td>
</tr><tr>
<td >Min</td>
<td >个</td>
<td >队列中最小等待任务数</td>
</tr><tr>
<td >Max</td>
<td >个</td>
<td >队列中最大等待任务数</td>
</tr><tr>
<td >Mean</td>
<td >个</td>
<td >队列中平均等待任务数</td>
</tr><tr>
<td >Percentile_99_9</td>
<td >个</td>
<td >队列中等待任务数的99.9分位数</td>
</tr><tr>
<td rowspan=5>操作运行时间</td>
<td >TotalCount</td>
<td >微秒</td>
<td >总操作数</td>
</tr><tr>
<td >Min</td>
<td >微秒</td>
<td >最小运行时间</td>
</tr><tr>
<td >Max</td>
<td >微秒</td>
<td >最大运行时间</td>
</tr><tr>
<td >Mean</td>
<td >微秒</td>
<td >平均运行时间</td>
</tr><tr>
<td >Percentile_99_9</td>
<td >微秒</td>
<td >运行时间的99.9分位数</td>
</tr><tr>
<td rowspan=5>排队等待时间</td>
<td >TotalCount</td>
<td >微秒</td>
<td >总操作数</td>
</tr><tr>
<td >Min</td>
<td >微秒</td>
<td >最小等待时间</td>
</tr><tr>
<td >Max</td>
<td >微秒</td>
<td >最大等待时间</td>
</tr><tr>
<td >Mean</td>
<td >微秒</td>
<td >平均等待时间</td>
</tr><tr>
<td >Percentile_99_9</td>
<td >微秒</td>
<td >等待时间的99.9分位数</td>
</tr><tr>
<td >分配的字节</td>
<td >AllocatedBytes</td>
<td >bytes</td>
<td >应用程序使用的字节数。这通常与操作系统报告的内存使用情况不匹配，因为它不包括TCMalloc开销或内存碎片</td>
</tr><tr>
<td >混合时钟错误</td>
<td >HybridClockError</td>
<td >微秒</td>
<td >服务器时钟最大错误；无法读取基础时钟时返回2^64-1</td>
</tr><tr>
<td >混合时钟时间戳</td>
<td >HybridClockTimestamp</td>
<td >微秒</td>
<td >混合时钟时间戳；无法读取基础时钟时返回2^64-1</td>
</tr><tr>			
<td rowspan=3>TCMalloc 内存</td>
<td >HeapSize</td>
<td >bytes</td>
<td >TCMalloc 保留的系统内存字节</td>
</tr><tr>			
<td >CurrentThreadCacheBytes</td>
<td >bytes</td>
<td >	TCMalloc 正在使用的内存的度量（对于小对象）</td>
</tr><tr>			
<td >TotalThreadCacheBytes</td>
<td >bytes</td>
<td >	TCMalloc 用于小对象的内存限制</td>
</tr><tr>		
<td rowspan=2>TCMalloc PageHeap</td>
<td >FreeBytes</td>
<td >bytes</td>
<td >页堆中可用的映射页的字节数</td>
</tr><tr>				
<td >UnMappedBytes</td>
<td >bytes</td>
<td >页堆中空闲的未映射页的字节数</td>
</tr><tr>			
<td rowspan=3>RPC 请求</td>
<td >ConnectionsAccepted</td>
<td >个</td>
<td >到 RPC 服务器的连入 TCP 连接数</td>
</tr><tr>				
<td >QueueOverflow</td>
<td >个</td>
<td >由于服务队列已满而丢弃的 RPC 数</td>
</tr><tr>			
<td >TimesOutInQueue</td>
<td >个</td>
<td >在服务队列中等待时超时并因此未被处理的 RPC 数</td>
</tr><tr>			
<td rowspan=5>RPC FetchData</td>
<td >TotalCount</td>
<td >微秒</td>
<td >总操作数</td>
</tr><tr>
<td >Min</td>
<td >微秒</td>
<td >最小处理时间</td>
</tr><tr>
<td >Max</td>
<td >微秒</td>
<td >最大处理时间</td>
</tr><tr>
<td >Mean</td>
<td >微秒</td>
<td >平均处理时间</td>
</tr><tr>
<td >Percentile_99_9</td>
<td >微秒</td>
<td >处理时间的99.9分位数</td>
</tr><tr>
<td rowspan=5>RPC AlterSchema</td>
<td >TotalCount</td>
<td >微秒</td>
<td >总操作数</td>
</tr><tr>
<td >Min</td>
<td >微秒</td>
<td >最小处理时间</td>
</tr><tr>
<td >Max</td>
<td >微秒</td>
<td >最大处理时间</td>
</tr><tr>
<td >Mean</td>
<td >微秒</td>
<td >平均处理时间</td>
</tr><tr>
<td >Percentile_99_9</td>
<td >微秒</td>
<td >处理时间的99.9分位数</td>
</tr><tr>
<td rowspan=5>RPC CreateTablet</td>
<td >TotalCount</td>
<td >微秒</td>
<td >总操作数</td>
</tr><tr>
<td >Min</td>
<td >微秒</td>
<td >最小处理时间</td>
</tr><tr>
<td >Max</td>
<td >微秒</td>
<td >最大处理时间</td>
</tr><tr>
<td >Mean</td>
<td >微秒</td>
<td >平均处理时间</td>
</tr><tr>
<td >Percentile_99_9</td>
<td >微秒</td>
<td >处理时间的99.9分位数</td>
</tr><tr>
<td rowspan=5>RPC DeleteTablet</td>
<td >TotalCount</td>
<td >微秒</td>
<td >总操作数</td>
</tr><tr>
<td >Min</td>
<td >微秒</td>
<td >最小处理时间</td>
</tr><tr>
<td >Max</td>
<td >微秒</td>
<td >最大处理时间</td>
</tr><tr>
<td >Mean</td>
<td >微秒</td>
<td >平均处理时间</td>
</tr><tr>
<td >Percentile_99_9</td>
<td >微秒</td>
<td >处理时间的99.9分位数</td>
</tr><tr>
<td rowspan=5>RPC Quiesce</td>
<td >TotalCount</td>
<td >微秒</td>
<td >总操作数</td>
</tr><tr>
<td >Min</td>
<td >微秒</td>
<td >最小处理时间</td>
</tr><tr>
<td >Max</td>
<td >微秒</td>
<td >最大处理时间</td>
</tr><tr>
<td >Mean</td>
<td >微秒</td>
<td >平均处理时间</td>
</tr><tr>
<td >Percentile_99_9</td>
<td >微秒</td>
<td >处理时间的99.9分位数</td>
</tr><tr>
<td rowspan=5>RPC Scan</td>
<td >TotalCount</td>
<td >微秒</td>
<td >总操作数</td>
</tr><tr>
<td >Min</td>
<td >微秒</td>
<td >最小处理时间</td>
</tr><tr>
<td >Max</td>
<td >微秒</td>
<td >最大处理时间</td>
</tr><tr>
<td >Mean</td>
<td >微秒</td>
<td >平均处理时间</td>
</tr><tr>
<td >Percentile_99_9</td>
<td >微秒</td>
<td >处理时间的99.9分位数</td>
</tr><tr>
<td rowspan=5>RPC ScannerKeepAlive</td>
<td >TotalCount</td>
<td >微秒</td>
<td >总操作数</td>
</tr><tr>
<td >Min</td>
<td >微秒</td>
<td >最小处理时间</td>
</tr><tr>
<td >Max</td>
<td >微秒</td>
<td >最大处理时间</td>
</tr><tr>
<td >Mean</td>
<td >微秒</td>
<td >平均处理时间</td>
</tr><tr>
<td >Percentile_99_9</td>
<td >微秒</td>
<td >处理时间的99.9分位数</td>
</tr><tr>
<td rowspan=5>RPC Write</td>
<td >TotalCount</td>
<td >微秒</td>
<td >总操作数</td>
</tr><tr>
<td >Min</td>
<td >微秒</td>
<td >最小处理时间</td>
</tr><tr>
<td >Max</td>
<td >微秒</td>
<td >最大处理时间</td>
</tr><tr>
<td >Mean</td>
<td >微秒</td>
<td >平均处理时间</td>
</tr><tr>
<td >Percentile_99_9</td>
<td >微秒</td>
<td >处理时间的99.9分位数</td>
</tr>
</table>

### KUDU-Master
<table>
<tr>
<th width=20%>标题 </th>
<th width=20%>指标名称</th>
<th width=15%>指标单位</th>
<th width=45%>指标含义 </th>
</tr><tr>
<td rowspan=2>块缓存命中</td>
<td >BlockCacheHit</td>
<td >次</td>
<td >期望一个块并查找到的次数。当确定缓存的效率时，使用此值代替cache_hits</td>
</tr><tr>
<td >BlockCacheMiss</td>
<td >次</td>
<td >预期未生成块的查找数。使用此值来确定缓存的效率，而不是cache_misses</td>
</tr><tr>
<td >块缓存使用率</td>
<td >BlockCacheUsage</td>
<td >bytes</td>
<td >块缓存占用的内存</td>
</tr><tr>
<td rowspan=2>文件缓存命中</td>
<td >FileCacheHit</td>
<td >次</td>
<td >预期并命中文件描述符的查找数。当确定缓存的效率时，使用此值代替 cache_hits</td>
</tr><tr>
<td >FileCacheMiss</td>
<td >次</td>
<td >预期但未命中文件描述符的查找数。当确定缓存的效率时，使用此值代替cache_misses</td>
</tr><tr>
<td >文件缓存使用率</td>
<td >FileCacheUsage</td>
<td >个</td>
<td >文件缓存中的条目数</td>

</tr><tr>
<td rowspan=3>块管理器 block 数</td>
<td >BlockUnderManagement</td>
<td >个</td>
<td >当前管理的数据块数</td>
</tr><tr>
<td >BlockOpenReading</td>
<td >个</td>
<td >当前打开供读取的数据块数</td>
</tr><tr>
<td >BlockOpenWriting</td>
<td >个</td>
<td >当前打开进行写入的数据块数</td>
</tr><tr>
<td >块管理器字节数</td>
<td >BytesUnderManagement</td>
<td >bytes</td>
<td >当前管理的数据块字节数</td>
</tr><tr>
<td rowspan=2>块管理器容器数</td>
<td >ContainersUnderManagement</td>
<td >个</td>
<td >日志块容器数</td>
</tr><tr>
<td >FullContainersUnderManagement</td>
<td >个</td>
<td >完整日志块容器数</td>
</tr><tr>
<td rowspan=2>Cpu 时间</td>
<td >CpuStime</td>
<td >毫秒</td>
<td >进程的总系统 CPU 时间</td>
</tr><tr>
<td >CpuUtime</td>
<td >毫秒</td>
<td >进程的用户 CPU 总时间</td>
</tr><tr>
<td >线程</td>
<td >ThreadsRunning</td>
<td >个</td>
<td >当前正在运行的线程数</td>
</tr><tr>
<td rowspan=2>数据路径</td>
<td >DataDirsFailed</td>
<td >个</td>
<td >磁盘当前处于故障状态的数据目录数</td>
</tr><tr>
<td >DataDirsFull</td>
<td >个</td>
<td >磁盘当前已满的数据目录数</td>
</tr><tr>
<td >分配的字节</td>
<td >AllocatedBytes</td>
<td >bytes</td>
<td >应用程序使用的字节数。这通常与操作系统报告的内存使用情况不匹配，因为它不包括TCMalloc开销或内存碎片</td>
</tr><tr>
<td rowspan=2>日志信息</td>
<td >ErrorMessages</td>
<td >个</td>
<td >应用程序发出的 ERROR 级日志消息数</td>
</tr><tr>
<td >WarningMessages</td>
<td >个</td>
<td >应用程序发出的 WARNING 级日志消息数</td>
</tr><tr>
<td rowspan=2>上下文</td>
<td >InvoluntarySwitches</td>
<td >次</td>
<td >非自发的上下文切换</td>
</tr><tr>
<td >VoluntarySwitches</td>
<td >次</td>
<td >自发的上下文切换</td>
</tr><tr>
<td rowspan=5>队列中操作数</td>
<td >TotalCount</td>
<td >个</td>
<td >总数</td>
</tr><tr>
<td >Min</td>
<td >个</td>
<td >队列中最小等待任务数</td>
</tr><tr>
<td >Max</td>
<td >个</td>
<td >队列中最大等待任务数</td>
</tr><tr>
<td >Mean</td>
<td >个</td>
<td >队列中平均等待任务数</td>
</tr><tr>
<td >Percentile_99_9</td>
<td >个</td>
<td >队列中等待任务数的99.9分位数</td>
</tr><tr>
<td rowspan=5>排队等待时间</td>
<td >TotalCount</td>
<td >微秒</td>
<td >总操作数</td>
</tr><tr>
<td >Min</td>
<td >微秒</td>
<td >最小等待时间</td>
</tr><tr>
<td >Max</td>
<td >微秒</td>
<td >最大等待时间</td>
</tr><tr>
<td >Mean</td>
<td >微秒</td>
<td >平均等待时间</td>
</tr><tr>
<td >Percentile_99_9</td>
<td >微秒</td>
<td >等待时间的99.9分位数</td>
</tr><tr>
<td rowspan=5>操作运行时间</td>
<td >TotalCount</td>
<td >微秒</td>
<td >总操作数</td>
</tr><tr>
<td >Min</td>
<td >微秒</td>
<td >最小运行时间</td>
</tr><tr>
<td >Max</td>
<td >微秒</td>
<td >最大运行时间</td>
</tr><tr>
<td >Mean</td>
<td >微秒</td>
<td >平均运行时间</td>
</tr><tr>
<td >Percentile_99_9</td>
<td >微秒</td>
<td >运行时间的99.9分位数</td>
</tr><tr>
<td >自旋锁</td>
<td >SpinlockContentionTime</td>
<td >微秒</td>
<td >自服务器启动后，内部自旋锁上的争用所消耗的时间量</td>
</tr><tr>
<td >过大的读请求数</td>
<td >OversizedWriteRequests</td>
<td >个</td>
<td >启动后拒绝的对system catalog tablet的过大写请求数</td>
</tr><tr>
<td >混合时钟错误</td>
<td >HybridClockError</td>
<td >微秒</td>
<td >服务器时钟最大错误；无法读取基础时钟时返回2^64-1</td>
</tr><tr>
<td >混合时钟时间戳</td>
<td >HybridClockTimestamp</td>
<td >微秒</td>
<td >混合时钟时间戳；无法读取基础时钟时返回2^64-1</td>
</tr><tr>
<td >tablet 副本差值</td>
<td >ClusterReplicaSkew</td>
<td >个</td>
<td >承载最多副本的 tablet 服务器上的副本数与承载最少副本的 tablet 服务器上的副本数之间的差异</td>
</tr><tr>
<td >tablet leader个数</td>
<td >NumRaftLeaders</td>
<td >个</td>
<td >Raft leaders的tablet副本数量</td>
</tr><tr>
<td >tablet session 数</td>
<td >OpemSourceSessions</td>
<td >个</td>
<td >此服务器上当前打开的 tablet 复制源 session 个数</td>
</tr><tr>
<td rowspan=3>TCMalloc 内存</td>
<td >HeapSize</td>
<td >bytes</td>
<td >TCMalloc 保留的系统内存字节</td>
</tr><tr>			
<td >CurrentThreadCacheBytes</td>
<td >bytes</td>
<td >	TCMalloc 正在使用的内存的度量（对于小对象）</td>
</tr><tr>			
<td >TotalThreadCacheBytes</td>
<td >bytes</td>
<td >	TCMalloc 用于小对象的内存限制</td>
</tr><tr>		
<td rowspan=2>TCMalloc PageHeap</td>
<td >FreeBytes</td>
<td >bytes</td>
<td >页堆中可用的映射页的字节数</td>
</tr><tr>				
<td >UnMappedBytes</td>
<td >bytes</td>
<td >页堆中空闲的未映射页的字节数</td>
</tr><tr>			
<td rowspan=3>RPC 请求</td>
<td >ConnectionsAccepted</td>
<td >个</td>
<td >到 RPC 服务器的连入 TCP 连接数</td>
</tr><tr>				
<td >QueueOverflow</td>
<td >个</td>
<td >由于服务队列已满而丢弃的 RPC 数</td>
</tr><tr>			
<td >TimesOutInQueue</td>
<td >个</td>
<td >在服务队列中等待时超时并因此未被处理的 RPC 数</td>
</tr><tr>			
<td rowspan=5>RPC RunLeaderElection</td>
<td >TotalCount</td>
<td >微秒</td>
<td >总操作数</td>
</tr><tr>
<td >Min</td>
<td >微秒</td>
<td >最小处理时间</td>
</tr><tr>
<td >Max</td>
<td >微秒</td>
<td >最大处理时间</td>
</tr><tr>
<td >Mean</td>
<td >微秒</td>
<td >平均处理时间</td>
</tr><tr>
<td >Percentile_99_9</td>
<td >微秒</td>
<td >处理时间的99.9分位数</td>
</tr><tr>
<td rowspan=5>RPC ConnectToMaster</td>
<td >TotalCount</td>
<td >微秒</td>
<td >总操作数</td>
</tr><tr>
<td >Min</td>
<td >微秒</td>
<td >最小处理时间</td>
</tr><tr>
<td >Max</td>
<td >微秒</td>
<td >最大处理时间</td>
</tr><tr>
<td >Mean</td>
<td >微秒</td>
<td >平均处理时间</td>
</tr><tr>
<td >Percentile_99_9</td>
<td >微秒</td>
<td >处理时间的99.9分位数</td>
</tr><tr>
<td rowspan=5>RPC Ping</td>
<td >TotalCount</td>
<td >微秒</td>
<td >总操作数</td>
</tr><tr>
<td >Min</td>
<td >微秒</td>
<td >最小处理时间</td>
</tr><tr>
<td >Max</td>
<td >微秒</td>
<td >最大处理时间</td>
</tr><tr>
<td >Mean</td>
<td >微秒</td>
<td >平均处理时间</td>
</tr><tr>
<td >Percentile_99_9</td>
<td >微秒</td>
<td >处理时间的99.9分位数</td>
</tr><tr>
<td rowspan=5>RPC TSHeartbeat</td>
<td >TotalCount</td>
<td >微秒</td>
<td >总操作数</td>
</tr><tr>
<td >Min</td>
<td >微秒</td>
<td >最小处理时间</td>
</tr><tr>
<td >Max</td>
<td >微秒</td>
<td >最大处理时间</td>
</tr><tr>
<td >Mean</td>
<td >微秒</td>
<td >平均处理时间</td>
</tr><tr>
<td >Percentile_99_9</td>
<td >微秒</td>
<td >处理时间的99.9分位数</td>
</tr><tr>
<td rowspan=5>RPC FetchData</td>
<td >TotalCount</td>
<td >微秒</td>
<td >总操作数</td>
</tr><tr>
<td >Min</td>
<td >微秒</td>
<td >最小处理时间</td>
</tr><tr>
<td >Max</td>
<td >微秒</td>
<td >最大处理时间</td>
</tr><tr>
<td >Mean</td>
<td >微秒</td>
<td >平均处理时间</td>
</tr><tr>
<td >Percentile_99_9</td>
<td >微秒</td>
<td >处理时间的99.9分位数</td>
</tr>
</table>
