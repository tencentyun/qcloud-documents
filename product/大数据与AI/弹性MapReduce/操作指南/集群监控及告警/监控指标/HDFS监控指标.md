### HDFS-概览
<table>
<tr>
<th width=20%>标题 </th>
<th width=20%>指标名称</th>
<th width=15%>指标单位</th>
<th width=45%>指标含义 </th>
</tr><tr>
<td rowspan=4>集群存储容量 </td>
<td >CapacityTotal </td>
<td >GB </td>
<td >集群存储总容量 </td>
</tr><tr>
<td >CapacityUsed </td>
<td >GB </td>
<td >集群存储已使用容量 </td>
</tr><tr>
<td >CapacityRemaining </td>
<td >GB </td>
<td >集群存储剩余容量 </td>
</tr><tr>
<td >CapacityUsedNonDFS </td>
<td >GB </td>
<td >集群非 HDFS 使用容量 </td>
</tr><tr>
<td >集群负载 </td>
<td >TotalLoad </td>
<td >1 </td>
<td >当前连接数 </td>
</tr><tr>
<td >集群文件总数量 </td>
<td >FilesTotal </td>
<td >个 </td>
<td >总文件数量 </td>
</tr><tr>
<td rowspan=8>BLOCKS数量 </td>
<td >BlocksTotal </td>
<td >个 </td>
<td >总 BLOCK 数量 </td>
</tr><tr>
<td >PendingReplicationBlocks </td>
<td >个 </td>
<td >等待被备份的块数量 </td>
</tr><tr>
<td >UnderReplicatedBlocks </td>
<td >个 </td>
<td >副本数不够的块数量 </td>
</tr><tr>
<td >CorruptBlocks </td>
<td >个 </td>
<td >坏块数量 </td>
</tr><tr>
<td >ScheduledReplicationBlocks </td>
<td >个 </td>
<td >安排要备份的块数量 </td>
</tr><tr>
<td >PendingDeletionBlocks </td>
<td >个 </td>
<td >等待被删除的块数量 </td>
</tr><tr>
<td >ExcessBlocks </td>
<td >个 </td>
<td >多余的块数量 </td>
</tr><tr>
<td >PostponedMisreplicatedBlocks</td>
<td >个 </td>
<td >被推迟处理的异常块数量 </td>
</tr><tr>
<td >BLOCK容量 </td>
<td >BlockCapacity </td>
<td >个 </td>
<td >BLOCK 容量 </td>
</tr><tr>
<td rowspan=6>集群数据节点 </td>
<td >NumLiveDataNodes </td>
<td >个 </td>
<td >活的数据节点数量 </td>
</tr><tr>
<td >NumDeadDataNodes </td>
<td >个 </td>
<td >已经标记为 Dead 状态的数据节点数量 </td>
</tr><tr>
<td >NumDecomLiveDataNodes </td>
<td >个 </td>
<td >下线且 Live 的节点数量 </td>
</tr><tr>
<td >NumDecomDeadDataNodes </td>
<td >个 </td>
<td >下线且 Dead 的节点数量 </td>
</tr><tr>
<td >NumDecommissioningDataNodes </td>
<td >个 </td>
<td >正在下线的节点数量 </td>
</tr><tr>
<td >NumStaleDataNodes </td>
<td >个 </td>
<td >标记为过期状态的DataNode数目</td>
</tr><tr>
<td >HDFS存储空间使用率 </td>
<td >CapacityUsedRate </td>
<td >个 </td>
<td >HDFS集群存储空间使用率 </td>
</tr><tr>
<td >SNAPSHOT相关 </td>
<td >Snapshots </td>
<td >次 </td>
<td >Snapshots 数量 </td>
</tr><tr>
<td >磁盘故障 </td>
<td >VolumeFailuresTotal </td>
<td >次 </td>
<td >所有 Datanodes 的卷故障总数 </td>
</tr>
</table>

### HDFS-NameNode
<table>
<tr>
<th width=20%>标题 </th>
<th width=20%>指标名称</th>
<th width=15%>指标单位</th>
<th width=45%>指标含义 </th>
</tr><tr>
<td rowspan=2> 数据流量 </td>
<td >ReceivedBytes</td>
<td >Bytes/s</td>
<td >接收数据速率</td>
</tr><tr>
<td >SentBytes </td>
<td >Bytes/s </td>
<td >发送数据速率 </td>
</tr><tr>
<td >QPS </td>
<td >RpcQueueTimeNumOps </td>
<td >1/s </td>
<td >RPC 调用速率 </td>
</tr><tr>
<td rowspan=2>请求处理延迟 </td>
<td >RpcQueueTimeAvgTime </td>
<td >ms </td>
<td >RPC 平均延迟时间 </td>
</tr><tr>
<td >RpcProcessingTimeAvgTime </td>
<td >ms </td>
<td >RPC 请求平均处理时间 </td>
</tr><tr>
 <td rowspan=4>验证和授权 </td>
 <td >RpcAuthenticationFailures </td>
<td >	1/次 </td>
<td >RPC 验证失败次数 </td>
</tr><tr>
<td >RpcAuthenticationSuccesses </td>
<td >2/次 </td>
<td >RPC 验证成功次数 </td>
</tr><tr>
<td >RpcAuthorizationFailures </td>
<td >3/次 </td>
<td >RPC 授权失败次数 </td>
</tr><tr>
<td >RpcAuthorizationSuccesses </td>
<td >4/次 </td>
<td >RPC 授权成功次数 </td>
</tr><tr>
<td >当前连接数 </td>
<td >NumOpenConnections </td>
<td >1/个 </td>
<td >当前连接数量 </td>
</tr><tr>
<td >RPC处理队列长度 </td>
<td >CallQueueLength </td>
<td >1/个 </td>
<td >当前 RPC 处理队列长度 </td>
</tr><tr>
<td rowspan=6>JVM内存 </td>
<td >MemNonHeapUsedM </td>
<td >MB </td>
<td >JVM 当前已经使用的 NonHeapMemory 的大小 </td>
</tr><tr>
<td >MemNonHeapCommittedM </td>
<td >MB </td>
<td >JVM 配置的 NonHeapCommittedM 的大小 </td>
</tr><tr>
<td >MemHeapUsedM </td>
<td >MB </td>
<td >JVM 当前已经使用的 HeapMemory 的大小 </td>
</tr><tr>
<td >MemHeapCommittedM </td>
<td >MB </td>
<td >JVM HeapMemory 提交大小 </td>
</tr><tr>
<td >MemHeapMaxM </td>
<td >MB </td>
<td >JVM 配置的 HeapMemory 的大小 </td>
</tr><tr>
<td >MemMaxM </td>
<td >MB </td>
<td >JVM 运行时可以使用的最大内存大小 </td>
</tr><tr>
<td >数据块汇报延迟 </td>
<td >BlockReportAvgTime </td>
<td >次/s </td>
<td >每秒处理 DataNode Blcok 平均延迟 </td>
</tr><tr>
<td rowspan=6>JVM线程数量 </td>
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
<td >处于 Terminated 状态的线程数量 </td>
</tr><tr>
<td rowspan=4>JVM日志数量 </td>
<td >LogFatal </td>
<td >个 </td>
<td >FATAL级别日志数量 </td>
</tr><tr>
<td >LogError </td>
<td >个 </td>
<td >ERROR级别日志数量 </td>
</tr>			<tr>
<td >LogWarn </td>
<td >个 </td>
<td >WARN级别日志数量 </td>
</tr><tr>
<td >LogInfo </td>
<td >个 </td>
<td >	INFO级别日志数量 </td>
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
<td >Survivor 0 区内存使用占比 </td>
</tr><tr>
<td >S1 </td>
<td >% </td>
<td >Survivor 1 区内存使用占比 </td>
</tr><tr>
<td >E </td>
<td >% </td>
<td >Eden 区内存使用占比 </td>
</tr><tr>
<td >O </td>
<td >% </td>
<td >Old 区内存使用占比 </td>
</tr><tr>
<td >M </td>
<td >% </td>
<td >Metaspace 区内存使用占比 </td>
</tr><tr>
<td >CCS </td>
<td >% </td>
<td >Compressed class space 区内存使用占比 </td>
</tr><tr>
<td >被标记为过期的存储的数量 </td>
<td >NumStaleStorages </td>
<td >个 </td>
<td >所有过期DataNode的存储目总数 </td>
</tr><tr>
<td >备NN上挂起的与BLOCK相关操作的消息数量 </td>
<td >PendingDataNodeMessageCount </td>
<td >个/s </td>
<td >DATANODE 的请求被 QUEUE 在 standby namenode 中的个数</td>
</tr><tr>
<td rowspan=2>缺失块统计 </td>
<td >NumberOfMissingBlocks </td>
<td >个 </td>
<td >缺失的数据块数量 </td>
</tr><tr>
<td >NumberOfMissingBlocksWithReplicationFactorOne</td>
<td >个 </td>
<td >缺失的数据库数量（rf = 1） </td>
</tr><tr>
<td rowspan=7>SNAPSHOT操作 </td>
<td >AllowSnapshotOps </td>
<td >次/s </td>
<td >每秒执行 AllowSnapshot 操作的次数 </td>
</tr><tr>
<td >DisallowSnapshotOps </td>
<td >次/s </td>
<td >每秒执行 DisallowSnapshot 操作的次数 </td>
</tr><tr>
<td >CreateSnapshotOps </td>
<td >次/s </td>
<td >每秒执行 CreateSnapshot 操作的次数 </td>
</tr><tr>
<td >DeleteSnapshotOps </td>
<td >次/s </td>
<td >每秒执行 DeleteSnapshot 操作的次数 </td>
</tr><tr>
<td >ListSnapshottableDirOps </td>
<td >次/s </td>
<td >每秒执行 ListSnapshottableDir 操作次数 </td>
</tr><tr>
<td >SnapshotDiffReportOps </td>
<td >次/s </td>
<td >每秒执行 SnapshotDiffReportOps 的次数 </td>
</tr><tr>
<td >RenameSnapshotOps </td>
<td >次/s </td>
<td >每秒执行 RenameSnapshotOps 的次数 </td>
</tr><tr>
<td rowspan=9>文件操作 </td>
<td >CreateFileOps </td>
<td >次/s </td>
<td >每秒执行 CreateFile 操作的次数 </td>
</tr><tr>
<td >GetListingOps </td>
<td >次/s </td>
<td >每秒执行 GetListing 操作的次数 </td>
</tr><tr>
<td >TotalFileOps </td>
<td >次/s </td>
<td >每秒执行 TotalFileOps 的次数 </td>
</tr><tr>
<td >DeleteFileOps </td>
<td >次/s </td>
<td >每秒执行 DeleteFile 操作的次数 </td>
</tr><tr>
<td >FileInfoOps </td>
<td >次/s </td>
<td >每秒执行 FileInfo 操作的次数 </td>
</tr><tr>
<td >GetAdditionalDatanodeOps </td>
<td >次/s </td>
<td >每秒执行 GetAdditionalDatanode 操作的次数 </td>
</tr><tr>
<td >CreateSymlinkOps </td>
<td >次/s </td>
<td >每秒执行 CreateSymlink 操作的次数 </td>
</tr><tr>
<td >GetLinkTargetOps </td>
<td >次/s </td>
<td >每秒执行 GetLinkTarget 操作的次数 </td>
</tr><tr>
<td >FilesInGetListingOps </td>
<td >次/s </td>
<td >每秒执行 FilesInGetListing 操作的次数 </td>
</tr><tr>
<td rowspan=2>事务操作 </td>
<td >TransactionsNumOps </td>
<td >次/s </td>
<td >每秒处理 Journal transaction 操作的次数 </td>
</tr><tr>
<td >TransactionsBatchedInSync </td>
<td >次/s </td>
<td >每秒批量处理 Journal transaction 操作次数 </td>
</tr><tr>
<td rowspan=3>镜像操作  </td>
<td >GetEditNumOps </td>
<td >次/s </td>
<td >每秒执行 GetEditNumOps 的次数 </td>
</tr><tr>
<td >GetImageNumOps </td>
<td >次/s </td>
<td >每秒执行 GetImageNumOps 的次数 </td>
</tr><tr>
<td >PutImageNumOps </td>
<td >次/s </td>
<td >每秒执行 PutImageNumOps 的次数 </td>
</tr><tr>
<td >SYNC操作 </td>
<td >SyncsNumOps </td>
<td >次/s </td>
<td >每秒处理 Journal syncs 操作的次数 </td>
</tr><tr>
<td rowspan=2>数据块操作 </td>
<td >BlockReceivedAndDeletedOps </td>
<td >次/s </td>
<td >每秒执行 BlockReceivedAndDeletedOps 的次数 </td>
</tr><tr>
<td >BlockOpsQueued </td>
<td >次/s </td>
<td >处理 DataNode Block 上报操作的次数 </td>
</tr><tr>
<td >缓存汇报 </td>
<td >CacheReportNumOps </td>
<td >次/s </td>
<td >每秒处理 CacheReport 操作的次数 </td>
</tr><tr>
<td >数据块汇报 </td>
<td >BlockReportNumQps </td>
<td >次/s </td>
<td >每秒处理 DataNode Blcok 上报操作的次数 </td>
</tr><tr>
<td >SYNCS操作延迟 </td>
<td >SyncsAvgTime </td>
<td >ms </td>
<td >处理 Journal syncs 操作的平均延迟 </td>
</tr><tr>
<td >Cache汇报延迟 </td>
<td >CacheReportAvgTime </td>
<td >ms </td>
<td >缓存上报动作平均延迟 </td>
</tr><tr>
<td rowspan=3>镜像操作延迟 </td>
<td >GetEditAvgTime </td>
<td >ms </td>
<td >读取 Edit 文件操作平均延迟 </td>
</tr><tr>
<td >GetImageAvgTime </td>
<td >ms </td>
<td >读取镜像文件平均延迟 </td>
</tr><tr>
<td >PutImageAvgTime </td>
<td >ms </td>
<td >写入镜像文件平均延迟 </td>
</tr><tr>
<td >事务操作延迟 </td>
<td >TransactionsAvgTime </td>
<td >ms </td>
<td >处理 Journal Transaction 操作的平均延迟 </td>
</tr><tr>
<td >启动时间 </td>
<td >StartTime </td>
<td >ms </td>
<td >进程启动时间 </td>
</tr><tr>
<td >主备情况 </td>
<td >State </td>
<td >1 </td>
<td >NN HA状态 </td>
</tr><tr>
<td >主备情况 </td>
<td >State </td>
<td >1:主，0:备 </td>
<td >NameNode主备情况 </td>
</tr><tr>
<td rowspan=3>线程数量 </td>
<td >PeakThreadCount </td>
<td >个 </td>
<td >峰值线程数 </td>
</tr><tr>
<td >ThreadCount </td>
<td >个 </td>
<td >线程数量 </td>
</tr><tr>
<td >DaemonThreadCount </td>
<td >个 </td>
<td >后台线程数量 </td>
</tr>
</table>

### HDFS-DataNode
<table>
<tr>
<th width=15%>标题 </th>
<th width=20%>指标名称 </th>
<th width=15%>指标单位</th>
<th width=50%>指标含义 </th>
</tr><tr>
<td >XCEIVER数量 </td>
<td >XceiverCount </td>
<td >个 </td>
<td >Xceiver 数量 </td>
</tr><tr>
<td rowspan=4>数据读写速率 </td>
<td >BytesWrittenMB</td>
<td >Bytes/s </td>
<td >写入 DN 的字节速率 </td>
</tr><tr>
<td >BytesReadMB</td>
<td >Bytes/s </td>
<td >读取 DN 的字节速率 </td>
</tr><tr>
<td >RemoteBytesReadMB </td>
<td >Bytes/s </td>
<td >远程客户端读取字节速率 </td>
</tr><tr>
<td >RemoteBytesWrittenMB </td>
<td >Bytes/s </td>
<td >远程客户端写入字节速率 </td>
</tr><tr>
 <td  rowspan=4>客户端连接数 </td>
<td >WritesFromRemoteClient </td>
<td >个 </td>
<td >来自远程客户端写操作 QPS </td>
</tr><tr>
<td >WritesFromLocalClient </td>
<td >个 </td>
<td >来自本地客户端写操作 OPS </td>
</tr><tr>
<td >ReadsFromRemoteClient </td>
<td >个 </td>
<td >来自远程客户端读操作 QPS </td>
</tr><tr>
<td >ReadsFromLocalClient </td>
<td >个 </td>
<td >来自本地客户端读操作 QPS </td>
</tr><tr>
<td >Block校验失败 </td>
<td >BlockVerificationFailures </td>
<td >次/s </td>
<td >BLOCK 校验失败数量 </td>
</tr><tr>
<td >磁盘故障 </td>
<td >VolumeFailures </td>
<td >次/s </td>
<td >磁盘故障次数 </td>
</tr><tr>
<td >网络错误 </td>
<td >DatanodeNetworkErrors </td>
<td >次/s </td>
<td >网络错误统计 </td>
</tr><tr>
<td >心跳延迟 </td>
<td >HeartbeatsAvgTime </td>
<td >ms </td>
<td >心跳接口平均时间 </td>
</tr><tr>
<td >心跳QPS </td>
<td >HeartbeatsNumOps </td>
<td >次/s </td>
<td >心跳接口 QPS </td>
</tr><tr>
<td >包传输操作RT </td>
<td >SendDataPacketTransferNanosAvgTime </td>
<td >ms </td>
<td >发送数据包平均时间 </td>
</tr><tr>
<td rowspan=9>数据块操作 </td>
<td >ReadBlockOpNumOps </td>
<td >次/s </td>
<td >从 DataNode 读取 Block OPS </td>
</tr><tr>
<td >WriteBlockOpNumOps </td>
<td >次/s </td>
<td >向 DataNode 写入 Block OPS </td>
</tr><tr>
<td >BlockChecksumOpNumOps </td>
<td >次/s </td>
<td >DataNode 进行 Checksum 操作的 OPS </td>
</tr><tr>
<td >CopyBlockOpNumOps </td>
<td >次/s </td>
<td >复制 Block 操作的 OPS </td>
</tr><tr>
<td >ReplaceBlockOpNumOps </td>
<td >次/s </td>
<td >Replace Block 操作的 OPS </td>
</tr><tr>
<td >BlockReportsNumOps </td>
<td >次/s </td>
<td >BLOCK 汇报动作的 OPS </td>
</tr><tr>
<td >IncrementalBlockReportsNumOps </td>
<td >次/s </td>
<td >BLOCK 增量汇报的 OPS </td>
</tr><tr>
<td >CacheReportsNumOps </td>
<td >次/s </td>
<td >缓存汇报的 OPS </td>
</tr><tr>
<td >PacketAckRoundTripTimeNanosNumOps </td>
<td >次/s </td>
<td >每秒处理 ACK ROUND TRIP 次数 </td>
</tr><tr>	
<td >FSYNC操作 </td>
<td >FsyncNanosNumOps </td>
<td >次/s </td>
<td >每秒处理 FSYNC 操作次数 </td>
</tr><tr>
<td >FLUSH操作 </td>
<td >FlushNanosNumOps </td>
<td >次/s </td>
<td >每秒处理 Flush 操作次数 </td>
</tr><tr>
<td rowspan=9>数据块操作延迟统计 </td>
<td >ReadBlockOpAvgTime </td>
<td >ms </td>
<td >读取 Block 操作平均时间 </td>
</tr><tr>
<td >WriteBlockOpAvgTime </td>
<td >ms </td>
<td >写 Blcok 操作平均时间 </td>
</tr><tr>
<td >BlockChecksumOpAvgTime </td>
<td >ms </td>
<td >块校验操作平均时间 </td>
</tr><tr>
<td >CopyBlockOpAvgTime </td>
<td >ms </td>
<td >复制块操作平均时间 </td>
</tr><tr>
<td >ReplaceBlockOpAvgTime </td>
<td >ms </td>
<td >Replace Block 操作平均时间 </td>
</tr><tr>
<td >BlockReportsAvgTime </td>
<td >ms </td>
<td >块汇报平均时间 </td>
</tr><tr>
<td >IncrementalBlockReportsAvgTime </td>
<td >ms </td>
<td >增量块汇报平均时间 </td>
</tr><tr>
<td >CacheReportsAvgTime </td>
<td >ms </td>
<td >缓存汇报平均时间 </td>
</tr><tr>
<td >PacketAckRoundTripTimeNanosAvgTime </td>
<td >ms </td>
<td >处理 ACK ROUND TRIP 平均时间 </td>
</tr><tr>
<td >FLUSH延迟 </td>
<td >FlushNanosAvgTime </td>
<td >ms </td>
<td >Flush 操作平均时间 </td>
</tr><tr>
<td >FSYNC延迟 </td>
<td >FsyncNanosAvgTime </td>
<td >ms </td>
<td >Fsync 操作平均时间 </td>
</tr><tr>
<td rowspan=8>RAMDISK Blocks </td>
<td >RamDiskBlocksWrite </td>
<td >块/s </td>
<td >写入内存的块的总数 </td>
</tr><tr>
<td >RamDiskBlocksWriteFallback </td>
<td >块/s </td>
<td >写入内存但未成功的块总数（故障转移到磁盘）</td>
</tr><tr>
<td >RamDiskBlocksDeletedBeforeLazyPersisted</td>
<td >块/s </td>
<td >应用程序在被保存到磁盘之前被删除的块的总数</td>
</tr><tr>
<td >RamDiskBlocksReadHits </td>
<td >块/s </td>
<td >内存中的块被读取的总次数 </td>
</tr><tr>
<td >RamDiskBlocksEvicted </td>
<td >块/s </td>
<td >内存中被清除的块总数 </td>
</tr><tr>
<td >RamDiskBlocksEvictedWithoutRead </td>
<td >块/s </td>
<td >从内存中取出的内存块总数 </td>
</tr><tr>
<td >RamDiskBlocksLazyPersisted </td>
<td >块/s </td>
<td >惰性写入器写入磁盘的总数 </td>
</tr><tr>
<td >RamDiskBytesLazyPersisted </td>
<td >Bytes/s </td>
<td >由惰性写入器写入磁盘的总字节数 </td>
</tr><tr>
<td >RAMDISK写入速度 </td>
<td >RamDiskBytesWrite </td>
<td >Bytes/s </td>
<td >写入内存的总字节数 </td>
</tr><tr>
<td rowspan=6>JVM内存 </td>
<td >MemNonHeapUsedM </td>
<td >MB </td>
<td >JVM 当前已经使用的 NonHeapMemory 的大小 </td>
</tr><tr>
<td >MemNonHeapCommittedM </td>
<td >MB </td>
<td >JVM 配置的 NonHeapCommittedM 的大小 </td>
</tr><tr>
<td >MemHeapUsedM </td>
<td >MB </td>
<td >JVM 当前已经使用的 HeapMemory 的大小 </td>
</tr><tr>
<td >MemHeapCommittedM </td>
<td >MB </td>
<td >JVM HeapMemory 提交大小 </td>
</tr><tr>
<td >MemHeapMaxM </td>
<td >MB </td>
<td >JVM 配置的 HeapMemory 的大小 </td>
</tr><tr>
<td >MemMaxM </td>
<td >MB </td>
<td >JVM 运行时可以使用的最大内存大小 </td>
</tr><tr>
<td rowspan=6>JVM线程数量 </td>
<td >ThreadsNew </td>
<td >个 </td>
<td >处于新建状态的线程数量 </td>
</tr><tr>
<td >ThreadsRunnable </td>
<td >个 </td>
<td >处于可运行状态的线程数量 </td>
</tr><tr>
<td >ThreadsBlocked </td>
<td >个 </td>
<td >处于阻塞状态的线程数量 </td>
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
<td >处于 Terminated 状态的线程数量 </td>
</tr><tr>
<td  rowspan=4>JVM日志数量 </td>
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
<td rowspan=2>GC 次数</td>
<td >YGC </td>
<td >次</td>
<td >Young GC 次数 </td>
</tr><tr>
<td >FGC </td>
<td >次</td>
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
<td >S0 </td>
<td >% </td>
<td >Survivor 0 区内存使用占比 </td>
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
<td >Survivor 1 区内存使用占比 </td>
</tr><tr>
<td >O </td>
<td >% </td>
<td >Old 区内存使用占比 </td>
</tr><tr>
<td >M </td>
<td >% </td>
<td >Metaspace 区内存使用占比 </td>
</tr><tr>
<td rowspan=2>数据流量 </td>
<td >ReceivedBytes </td>
<td >Bytes/s </td>
<td >接收数据速率 </td>
</tr><tr>
<td >SentBytes </td>
<td >Bytes/s </td>
<td >发送数据速率 </td>
</tr><tr>
<td >QPS </td>
<td >RpcQueueTimeNumOps </td>
<td >次/s </td>
<td >RPC 调用速率 </td>
</tr><tr>
<td rowspan=2>请求处理延迟 </td>
<td >RpcQueueTimeAvgTime </td>
<td >ms </td>
<td >RPC 平均延迟时间 </td>
</tr><tr>
<td >RpcProcessingTimeAvgTime </td>
<td >次/s </td>
<td >RPC 请求平均处理时间 </td>
</tr><tr>
<td rowspan=4>验证和授权  </td>
<td >RpcAuthenticationFailures </td>
<td >次/s </td>
<td >RPC 验证失败次数 </td>
</tr><tr>
<td >RpcAuthenticationSuccesses </td>
<td >次/s </td>
<td >RPC 验证成功次数 </td>
</tr><tr>
<td >RpcAuthorizationFailures </td>
<td >次/s </td>
<td >RPC 授权失败次数 </td>
</tr><tr>
<td >RpcAuthorizationSuccesses </td>
<td >次/s </td>
<td >RPC 授权成功次数 </td>
</tr><tr>
<td >当前连接数 </td>
<td >NumOpenConnections </td>
<td >个 </td>
<td >当前链接数量 </td>
</tr><tr>
<td >RPC处理队列长度 </td>
<td >CallQueueLength </td>
<td >1 </td>
<td >当前 RPC 处理队列长度 </td>
</tr><tr>
<td rowspan=2>CPU时间 </td>
<td >CurrentThreadSystemTime </td>
<td >ms </td>
<td >系统时间 </td>
</tr><tr>
<td >CurrentThreadUserTime </td>
<td >ms </td>
<td >用户时间 </td>
</tr><tr>
<td >启动时间 </td>
<td >StartTime </td>
<td >s </td>
<td >进程启动时间 </td>
</tr><tr>
<td rowspan=2>线程数量 </td>
<td >PeckThreadCount </td>
<td >个 </td>
<td >峰值线程数量 </td>
</tr><tr>
<td >DaemonThreadCount </td>
<td >个 </td>
<td >后台线程数量 </td>
</tr><tr>
<td rowspan=2>读写延迟 </td>
<td >write </td>
<td >ms </td>
<td >写操作耗时 </td>
</tr><tr>
<td >read </td>
<td >ms </td>
<td >读操作耗时</td>
</tr><tr>
<td >包传输操作QPS </td>
<td >DataPacketOps </td>
<td >次/s </td>
<td >包传输操作 QPS </td>
</tr>
</table>

### HDFS-Journal Node
<table>
<tr>
<th width=15%>标题 </th>
<th width=20%>指标名称 </th>
<th width=15%>指标单位</th>
<th width=50%>指标含义 </th>
</tr><tr>
<td rowspan=6>JVM内存 </td>
<td >MemNonHeapUsedM </td>
<td >MB </td>
<td >JVM 当前已经使用的 NonHeapMemory 的大小</td>
</tr><tr>
<td >MemNonHeapCommittedM </td>
<td >MB </td>
<td >JVM 配置的 NonHeapCommittedM 的大小 </td>
</tr><tr>
<td >MemHeapUsedM </td>
<td >MB </td>
<td >JVM 当前已经使用的 HeapMemory 的大小 </td>
</tr><tr>
<td >MemHeapCommittedM </td>
<td >MB </td>
<td >JVM HeapMemory 提交大小 </td>
</tr><tr>
<td >MemHeapMaxM </td>
<td >MB </td>
<td >JVM 配置的 HeapMemory 的大小 </td>
</tr><tr>
<td >MemMaxM </td>
<td >MB </td>
<td >JVM 运行时可以使用的最大内存大小 </td>
</tr><tr>
<td rowspan=6>JVM线程数量 </td>
<td >ThreadsNew </td>
<td >个 </td>
<td >处于 NEW 状态的线程数量 </td>
</tr><tr>
<td >ThreadsRunnable </td>
<td >个 </td>
<td >处于 RUNNABLE 状态的线程数量</td>
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
<td >处于 Terminated 状态的线程数量 </td>
</tr><tr>
<td rowspan=4>JVM日志数量 </td>
<td >LogFatal </td>
<td >个 </td>
<td >FATAL 级别日志数量 </td>
</tr><tr>
<td >LogError </td>
<td >个 </td>
<td >ERROR 级别日志数量</td>
</tr><tr>
<td >LogWarn </td>
<td >个 </td>
<td >WARN 级别日志数量</td>
</tr><tr>
<td >LogInfo </td>
<td >个 </td>
<td >INFO 级别日志数量</td>
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
<td >S0 </td>
<td >% </td>
<td >Survivor 0 区内存使用占比 </td>
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
<td >Survivor 1 区内存使用占比 </td>
</tr><tr>
<td >O </td>
<td >% </td>
<td >Old 区内存使用占比 </td>
</tr><tr>
<td >M </td>
<td >% </td>
<td >Metaspace 区内存使用占比 </td>
</tr><tr>
<td rowspan=2>数据流量 </td>
<td >ReceivedBytes </td>
<td >Bytes/s </td>
<td >接收数据速率 </td>
</tr><tr>
<td >SentBytes </td>
<td >Bytes/s </td>
<td >发送数据速率 </td>
</tr><tr>
<td >请求处理延迟 </td>
<td >RpcQueueTimeAvgTime </td>
<td >ms </td>
<td >RPC 平均延迟时间 </td>
</tr><tr>

<td rowspan=4>验证和授权 </td>
<td >RpcAuthenticationFailures </td>
<td >次/s </td>
<td >RPC 验证失败次数 </td>
</tr><tr>
<td >RpcAuthenticationSuccesses </td>
<td >次/s </td>
<td >RPC 验证成功次数 </td>
</tr><tr>
<td >RpcAuthorizationFailures </td>
<td >次/s </td>
<td >RPC 授权失败次数 </td>
</tr><tr>
<td >RpcAuthorizationSuccesses </td>
<td >次/s </td>
<td >RPC 授权成功次数 </td>
</tr><tr>
<td >当前连接数 </td>
<td >NumOpenConnections </td>
<td >个 </td>
<td >当前链接数量 </td>
</tr><tr>
<td >RPC处理队列长度 </td>
<td >CallQueueLength </td>
<td >1 </td>
<td >当前 RPC 处理队列长度 </td>
</tr><tr>
<td rowspan=2>CPU时间 </td>
<td >CurrentThreadSystemTime </td>
<td >ms </td>
<td >系统时间 </td>
</tr><tr>
<td >CurrentThreadUserTime </td>
<td >ms </td>
<td >用户时间 </td>
</tr><tr>
<td >启动时间 </td>
<td >StartTime </td>
<td >s </td>
<td >进程启动时间 </td>
</tr><tr>
<td rowspan=2>线程数量 </td>
<td >PeckThreadCount </td>
<td >个 </td>
<td >峰值线程数量 </td>
</tr><tr>
<td >DaemonThreadCount </td>
<td >个 </td>
<td >后台线程数量 </td>
</tr>
</table>

### HDFS-ZKFC
<table>
<tr>
<th width=15%>标题 </th>
<th width=20%>指标名称 </th>
<th width=15%>指标单位</th>
<th width=50%>指标含义 </th>
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
<td >S0 </td>
<td >% </td>
<td >Survivor 0 区内存使用占比 </td>
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
<td >Survivor 1 区内存使用占比 </td>
</tr><tr>
<td >O </td>
<td >% </td>
<td >Old 区内存使用占比 </td>
</tr><tr>
<td >M </td>
<td >% </td>
<td >Metaspace 区内存使用占比 </td>
</tr><tr>
<table>
