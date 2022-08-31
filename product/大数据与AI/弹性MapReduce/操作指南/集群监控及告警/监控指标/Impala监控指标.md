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
<td rowspan=1>CPU 利用率</td>
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
<td rowspan=1>CPU 利用率</td>
<td >SystemCpuLoad</td>
<td >个</td>
<td >系统 CPU 利用率</td>
</tr>
<tr>
<td rowspan=4>Beeswax API 客户端连接数</td>
<td >Use</td>
<td >个</td>
<td >活跃 Beeswax API 连接数</td>
</tr><tr>
<td >Conn_In_Use</td>
<td >个</td>
<td >与此 Impala Daemon 的活跃 Beeswax API 连接数</td>
</tr>
<tr>
<td >TotalConns</td>
<td >个</td>
<td >与此 Impala Daemon 的活跃 Beeswax API 连接总数</td>
</tr>
<tr>
<td >ConnSetupQueueSize</td>
<td >个</td>
<td >此 Impala Daemon 已被接收并等待建立连接的 Beeswax API 连接数</td>
</tr>
<tr>
<td rowspan=4>HS2 API 客户端连接数</td>
<td >Use</td>
<td >个</td>
<td >活跃 HS2 API 连接数</td>
</tr><tr>
<td >Conn_In_Use</td>
<td >个</td>
<td >活跃 HS2 API 连接数</td>
</tr>
<tr>
<td >TotalConns</td>
<td >个</td>
<td >此 Impala Daemon 在生命周期内建立连接的 HS2 API 连接总数</td>
</tr>
<tr>
<td >ConnSetupQueueSize</td>
<td >个</td>
<td >此 Impala Daemon 已被接收并等待建立连接的 HS2 API 连接数</td>
</tr>
<tr>
<td rowspan=2>线程管理器</td>
<td >RunningThreads</td>
<td >个</td>
<td >运行线程数</td>
</tr><tr>
<td >TotalCreatedThreads</td>
<td >个</td>
<td >生命周期内创建的线程数</td>
</tr>
<tr>
<td rowspan=1>内存管理器限制</td>
<td >Limit</td>
<td >Bytes</td>
<td >超过其内存限制的内存量(默认值-1)</td>
</tr><tr>
<td rowspan=1>超过其内存限制的内存量(默认值-1)</td>
<td >OverLimit</td>
<td >Bytes</td>
<td >生命周期内创建的线程数</td>
</tr>
<tr>
<td rowspan=6>HS2 API 客户端等待建立连接时间</td>
<td >P20</td>
<td rowspan=6>us</td>
<td rowspan=6>HS2 API 客户端等待建立连接时间</td>
</tr>
<tr>
<td >P50</td>
</tr>
<tr>
<td >P70</td>
</tr><tr>
<td >P90</td>
</tr>
<tr>
<td >P95</td>
</tr>
<tr>
<td >P99.9</td>
</tr>
<tr>
<td rowspan=6>Beeswax API 客户端等待服务线程建立时间</td>
<td >P20</td>
<td rowspan=6>us</td>
<td rowspan=6>Beeswax API 客户端等待服务线程建立时间</td>
</tr>
<tr>
<td >P50</td>
</tr>
<tr>
<td >P70</td>
</tr><tr>
<td >P90</td>
</tr>
<tr>
<td >P95</td>
</tr>
<tr>
<td >P99.9</td>
</tr>
<tr>
<td rowspan=1>已超时的 Beeswax API 连接数</td>
<td >TimeOutCnncRequests</td>
<td >个</td>
<td >已超时的 Beeswax API 连接数</td>
</tr><tr>
<td rowspan=1>解析请求池请求所花费时间(毫秒)</td>
<td >Total</td>
<td >ms</td>
<td >解析请求池请求所花费时间(毫秒)</td>
</tr><tr>
<td rowspan=1>外部数据源缓存类中缓存未命中数</td>
<td >Misses</td>
<td >个</td>
<td >外部数据源缓存类中缓存未命中数</td>
</tr><tr>
<td rowspan=1>已超时等待设置的 Impala 后端服务器的连接请求数</td>
<td >ConnSetupQueueSize</td>
<td >个</td>
<td >已超时等待设置的 Impala 后端服务器的连接请求数</td>
</tr><tr>
<td rowspan=1>已超时等待设置的 Impala be 的连接请求数</td>
<td >TimeOutCnncRequests</td>
<td >个</td>
<td >已超时等待设置的 Impala be 的连接请求数</td>
</tr>
<tr>
<td rowspan=1>与此 Impala 守护程序建立的 Impala 后端客户端连接总数</td>
<td >TotalConnections</td>
<td >个</td>
<td >与此 Impala 守护程序建立的 Impala 后端客户端连接总数</td>
</tr>
<tr>
<td rowspan=8>Impala be 的客户端等待连接建立所花费的时间</td>
<td >P20</td>
<td rowspan=8>us</td>
<td rowspan=8>Impala be 的客户端等待连接建立所花费的时间</td>
</tr>
<tr>
<td >P50</td>
</tr>
<tr>
<td >P70</td>
</tr><tr>
<td >P90</td>
</tr>
<tr>
<td >P95</td>
</tr>
<tr>
<td >P99.9</td>
</tr><tr>
<td >Count</td>
</tr>
<tr>
<td >Sum</td>
</tr>
<tr>
<td rowspan=8>Impala be 的客户端等待服务线程所花费的时间</td>
<td >P20</td>
<td rowspan=8>us</td>
<td rowspan=8>Impala be 的客户端等待服务线程所花费的时间</td>
</tr>
<tr>
<td >P50</td>
</tr>
<tr>
<td >P70</td>
</tr><tr>
<td >P90</td>
</tr>
<tr>
<td >P95</td>
</tr>
<tr>
<td >P99.9</td>
</tr><tr>
<td >Count</td>
</tr>
<tr>
<td >Sum</td>
</tr><tr>
<td rowspan=8>HS2 API 客户端等待服务线程建立时间</td>
<td >P20</td>
<td rowspan=8>us</td>
<td rowspan=8>HS2 API 客户端等待服务线程建立时间</td>
</tr>
<tr>
<td >P50</td>
</tr>
<tr>
<td >P70</td>
</tr><tr>
<td >P90</td>
</tr>
<tr>
<td >P95</td>
</tr>
<tr>
<td >P99.9</td>
</tr><tr>
<td >Count</td>
</tr>
<tr>
<td >Sum</td>
</tr><tr>
<td rowspan=8>HS2 HTTP API 客户端等待服务线程时间</td>
<td >P20</td>
<td rowspan=8>us</td>
<td rowspan=8>HS2 HTTP API 客户端等待服务线程时间</td>
</tr>
<tr>
<td >P50</td>
</tr>
<tr>
<td >P70</td>
</tr><tr>
<td >P90</td>
</tr>
<tr>
<td >P95</td>
</tr>
<tr>
<td >P99.9</td>
</tr><tr>
<td >Count</td>
</tr>
<tr>
<td >Sum</td>
</tr>
<tr>
<td >DataStreamService：服务队列溢被拒绝数</td>
<td >RpcsQueueOverflow</td>
<td >个</td>
<td >DataStreamService：服务队列溢被拒绝数</td>
</tr>
<tr>
<td >ControlStreamService：服务队列溢被拒绝数</td>
<td >RpcsQueueOverflow</td>
<td >个</td>
<td >ControlStreamService：服务队列溢被拒绝数</td>
</tr>
<tr>
<td rowspan=2>DataStreamService：使用字节数</td>
<td >PeakUsageBytes</td>
<td >Bytes</td>
<td >Memtracker DataStreamService 峰值使用字节数</td>
</tr><tr>
<td >CurrentUsageBytes</td>
<td >Bytes</td>
<td >Memtracker DataStreamService 当前使用字节数</td>
</tr>
<tr>
<td rowspan=2>ControlService：使用字节数</td>
<td >PeakUsageBytes</td>
<td >Bytes</td>
<td >Memtracker ControlService 峰值使用字节数</td>
</tr><tr>
<td >CurrentUsageBytes</td>
<td >Bytes</td>
<td >Memtracker ControlService 当前使用字节数</td>
</tr>
<tr>
<td >此进程的驻留集大小（RSS)</td>
<td >RSS</td>
<td >Bytes</td>
<td >此进程的驻留集大小（RSS)</td>
</tr>
<tr>
<td >StateStore 中注册后端总数</td>
<td >Total</td>
<td rowspan=1>个</td>
<td rowspan=1>StateStore 中注册后端总数</td>
</tr>
<tr>
<td rowspan=8>查询延迟发布</td>
<td >P20</td>
<td rowspan=8>us</td>
<td rowspan=8>查询延迟发布</td>
</tr>
<tr>
<td >P50</td>
</tr>
<tr>
<td >P70</td>
</tr><tr>
<td >P90</td>
</tr>
<tr>
<td >P95</td>
</tr>
<tr>
<td >P99.9</td>
</tr><tr>
<td >Count</td>
</tr>
<tr>
<td >Sum</td>
</tr>
<tr>
<td >打开已进行写入 HDFS 文件数</td>
<td >NumFilesOpenForInsert</td>
<td >个</td>
<td >打开 HDFS 文件数</td>
</tr>
<tr>
<td >进程生命周期内读取的扫描范围</td>
<td >ScanRangesTotal</td>
<td >个</td>
<td >进程生命周期内读取扫描范围</td>
</tr>
<tr>
<td >打开 Beeswax 会话数量</td>
<td >NumOpenBeeswaxSessions</td>
<td >个</td>
<td >打开 Beeswax 会话数量</td>
</tr>
<tr>
<td >进程生命周期内处理查询 fragment 总数</td>
<td >NumFragments</td>
<td >个</td>
<td >进程生命周期内处理查询 fragment 总数</td>
</tr>
<tr>
<td >在无 volum 元数据的进程生命周期内读取的扫描范围总数</td>
<td >ScanRangesNumMissingVolumId</td>
<td >个</td>
<td >在无 volum 元数据的进程生命周期内读取的扫描范围总数</td>
</tr>
<tr>
<td >Hedged reads 尝试次数</td>
<td >HedgedReadOps</td>
<td >个</td>
<td >Hedged reads 尝试次数</td>
</tr>
<tr>
<td >在进程生命周期内处理查询总数</td>
<td >NumQueries</td>
<td >个</td>
<td >在进程生命周期内处理查询总数</td>
</tr>
<tr>
<td >支持缓存 HS2 FETCH_FIRST 的总行数</td>
<td >ResultSetCacheTotalNumRows</td>
<td >个</td>
<td >缓存已支持 HS2 FETCH_FIRST 总行数</td>
</tr><tr>
<td >此 Impala 服务器上注册的查询总数</td>
<td >NumQueriesRegistered</td>
<td >个</td>
<td >此 Impala 服务器上注册查询总数</td>
</tr>
<tr>
<td >be 查询总数</td>
<td >NumQueriesExecuted</td>
<td >个</td>
<td >be 查询总数</td>
</tr>
<tr>
<td >非活动状态而终止会话数</td>
<td >NumSessionsExpired</td>
<td >个</td>
<td >非活动状态而终止会话数</td>
</tr>
<tr>
<td >非活动状态而终止查询数</td>
<td >NumQueriesExpired</td>
<td >个</td>
<td >非活动状态而终止查询数</td>
</tr>
<tr>
<td >打开 HS2会话数</td>
<td >NumOpenHS2Sessions</td>
<td >个</td>
<td >打开 HS2会话数</td>
</tr>
<tr>
<td >Catalog 里面表数量</td>
<td >NumTables</td>
<td >个</td>
<td >	Catalog tables 数量</td>
</tr>
<tr>
<td >Catalog 里面数据库数量</td>
<td >NumDatabases</td>
<td >个</td>
<td >	Catalog Databases 数量</td>
</tr>
<tr>
<td >IO 管理器写入磁盘的字节数</td>
<td >BytesWritten</td>
<td >个</td>
<td >	IO 管理器写入磁盘的字节数</td>
</tr>
<tr>
<td >IO 管理器打开的文件数</td>
<td >NumOpenFiles</td>
<td >个</td>
<td >IO 管理器打开的文件数</td>
</tr>
<tr>
<td >使用的 HDFS 文件句柄数</td>
<td >NumFileHandlesOutstanding</td>
<td >Bytes</td>
<td >使用的 HDFS 文件句柄数</td>
</tr>
<tr>
<td >读取的本地字节数</td>
<td >LocalBytesRead</td>
<td >Bytes</td>
<td >IO 管理器读取的本地字节数</td>
</tr>
</table>
