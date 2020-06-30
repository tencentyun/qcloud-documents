## 命名空间

Namespace=QCE/TXMR_HDFS

## 监控指标

### HDFS-Overview、HDFS-OverviewAggregation 

> ?1.查询HDFS-Overview的指标时，需加上前缀“EmrHdfsOverview“。
>
> 2.查询HDFS-OverviewAggregation 的指标时，需加上前缀“EmrHdfsOverviewAggregation”。

| 指标英文名                                  | 指标中文名                               | 单位 | 指标含义                                      | 维度                                   |
| ------------------------------------------- | ---------------------------------------- | ---- | --------------------------------------------- | -------------------------------------- |
| HdfsNnBlockCapacityTotal                    | 集群存储容量_CapacityTotal               | GB   | 集群存储总容量                                | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnBlockCapacityUsed                     | 集群存储容量_CapacityUsed                | GB   | 集群储存已使用容量                            | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnBlockCapacityRemaining                | 集群存储容量_CapacityRemaining           | GB   | 集群存储剩余容量                              | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnBlockCapacity<br>UsedNonDFS           | 集群存储容量_CapacityUsedNonDFS          | GB   | 集群非 HDFS 使用容量                          | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnBlockTotalLoad                        | 集群负载_TotalLoad                       | 个   | 当前连接数                                    | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnBlockFilesTotal                       | 群文件总数量_FilesTotal                  | 个   | 总文件数量                                    | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnBlockBlockstotal                      | BLOCKS数量_BlocksTotal                   | 个   | 总 BLOCK 数量                                 | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnBlockPending<br>ReplicationBlocks     | BLOCKS数量_PendingReplicationBlocks      | 个   | 等待被备份的块数量                            | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnBlockUnder<br>ReplicatedBlocks        | BLOCKS数量_UnderReplicatedBlocks         | 个   | 副本数不够的块数量                            | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnBlockBlocksCorruptblocks              | BLOCKS数量_CorruptBlocks                 | 个   | 坏块数量                                      | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnBlockScheduled<br>ReplicationBlocks   | BLOCKS数量_ScheduledReplicationBlocks    | 个   | 安排要备份的块数量                            | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnBlockPending<br>DeletionBlocks        | BLOCKS数量_PendingDeletionBlocks         | 个   | 等待被删除的块数量                            | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnBlockCorruptblocks                    | BLOCKS数量_CorruptBlocks                 | 个   | 多于的块数量                                  | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnBlockPostponed<br>MisreplicatedBlocks | BLOCKS数量_PostponedMisreplicatedBlocks  | 个   | 被推迟处理的异常块数量                        | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnBlockBlockCapacity                    | BLOCK容量_BlockCapacity                  | 个   | BLOCK 容量                                    | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnBlockNumLiveDataNodes                 | 集群数据节点_NumLiveDataNodes            | 个   | 个活的数据节点数量                            | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnBlockNumDeadDataNodes                 | 集群数据节点_NumDeadDataNodes            | 个   | 已经标记为 Dead 状态的数据节点数量            | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnBlockNum<br>DecomLiveDataNodes        | 集群数据节点_NumDecomLiveDataNodes       | 个   | 下线且 Live 的节点数量                        | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnBlockNum<br>DecomDeadDataNodes        | 集群数据节点_NumDecomDeadDataNodes       | 个   | 下线且 Dead 的节点数量                        | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnBlockNum<br>DecommissioningDataNodes  | 集群数据节点_NumDecommissioningDataNodes | 个   | 正在下线的节点数量                            | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnBlockNum<br>StaleDataNodes            | 集群数据节点_NumStaleDataNodes           | 个   | 由于心跳延迟而标记为过期的 DataNodes 当前数量 | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnBlockSnapshots                        | SNAPSHOT相关_Snapshots                   | 个   | Snapshots 数量                                | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnBlockVolumeFailuresTotal              | 磁盘故障_VolumeFailuresTotal             | 次   | 所有 Datanodes 的全故障总数                   | id4hdfsdatanode、<br>host4hdfsdatanode |

### HDFS-NameNode

| 指标英文名                                                   | 指标中文名                                                   | 指标单位 | 指标含义                                             | 维度                                   |
| ------------------------------------------------------------ | ------------------------------------------------------------ | -------- | ---------------------------------------------------- | -------------------------------------- |
| HdfsNnPort4007RxtxReceivedbytes                              | 数据流量_ReceivedBytes                                       | Bytes/s  | 接收数据速率                                         | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnPort4007RxtxSentbytes                                  | 数据流量_SentBytes                                           | Bytes/s  | 发送数据速率                                         | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnPort4007Qps<br>Rpcqueuetimenumops                      | QPS_RpcQueueTimeNumOps                                       | 次/s     | RPC 调用速率                                         | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnPort4007RtRpc<br>queuetimeavgtime                      | 请求处理延迟_RpcQueueTimeAvgTime                             | ms       | RPC 平均延迟时间                                     | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnPort4007AuthRpc<br>authenticationfailures              | 验证和授权_RpcAuthenticationFailure                          | 次       | RPC 验证失败次数                                     | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnPort4007AuthRpc<br>authenticationsuccesses             | 验证和授权_RpcAuthenticationSuccesses                        | 次       | RPC 验证成功次数                                     | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnPort4007AuthRpc<br>authorizationfailures               | 验证和授权_RpcAuthorizationFailures                          | 次       | RPC 授权失败次数                                     | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnPort4007AuthRpc<br>authorizationsuccesses              | 验证和授权_RpcAuthorizationSuccesses                         | 次       | RPC 授权成功次数                                     | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnPort4007Connections<br>Numopenconnections              | 当前连接数_NumOpenConnections                                | 个       | 当前链接数量                                         | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnPort4007Queue<br>LenCallqueuelength                    | RPC处理队列长度_CallQueueLength                              | 个       | 当前 RPC 处理队列长度                                | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnJvmMemMemnonheapusedm                                  | JVM内存_MemNonHeapUsedM                                      | MB       | JVM 当前已经使用的 NonHeapMemory 的大小              | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnJvmMemMemnon<br>heapcommittedm                         | JVM内存_MemNonHeapCommittedM                                 | MB       | JVM 内存                                             | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnJvmMemMemheapusedm                                     | JVM内存_MemHeapUsedM                                         | MB       | JVM 当前已经使用的 HeapMemory 的大小                 | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnJvmMem<br>Memheapcommittedm                            | JVM内存_MemHeapCommittedM                                    | MB       | JVM HeapMemory 提交大小                              | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnJvmMemMemheapmaxm                                      | JVM内存_MemHeapMaxM                                          | MB       | JVM 配置的 HeapMemory 的大小                         | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnJvmMemMemmaxm                                          | JVM内存_MemMaxM                                              | MB       | JVM 运行时的可以使用的最大的内存的大小               | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnBlockReportRt<br>Blockreportavgtime                    | 数据块汇报延迟_BlockReportAvgTime                            | 次/s     | 每秒处理 DataNode Blcok 平均延迟                     | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnGcUtilGcCountFgc                                       | GC次数_FGC                                                   | 次/s     | Full GC 次数                                         | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnGcUtilGcCountYgc                                       | C次数_YGC                                                    | 2次/s    | Young GC 次数                                        | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnGcUtilGcTimeYgct                                       | GC时间_YGCT                                                  | ms       | Young GC 消耗时间                                    | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnGcUtilGcTimeFgct                                       | GC时间_FGCT                                                  | ms       | Full GC 消耗时间                                     | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnGcUtilGcTimeGct                                        | GC时间_GCT                                                   | ms       | 垃圾回收时间消耗                                     | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnJvmJavaThreadsThreadsnew                               | JVM线程数量_ThreadsNew                                       | 个       | 处于新建状态的线程数量                               | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnJvmJavaThreads<br>Threadsrunnable                      | JVM线程数量_ThreadsRunnable                                  | 个       | 处于可运行状态的线程数量                             | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnJvmJavaThreads<br>Threadsblocked                       | JVM线程数量_ThreadsBlocked                                   | 个       | 处于阻塞状态的线程数量                               | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnJvmJavaThreads<br>Threadswaiting                       | JVM线程数量_ThreadsWaiting                                   | 个       | 处于 WAITING 状态的线程数量                          | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnJvmJavaThreads<br>Threadstimedwaiting                  | JVM线程数量_ThreadsTimedWaiting                              | 个       | 处于 TIMED WAITING 状态的线程数量                    | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnJvmJavaThreads<br>Threadsterminated                    | JVM线程数量_ThreadsTerminated                                | 个       | 处于 Terminated 状态的线程数量                       | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnJvmLogTotalLogfatal                                    | JVM日志数量_LogFatal                                         | 个       | Fatal 日志数量                                       | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnJvmLogTotalLogerror                                    | JVM日志数量_LogError                                         | 个       | Error 日志数量                                       | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnJvmLogTotalLogwarn                                     | JVM日志数量_LogWarn                                          | 个       | Warn 日志数量                                        | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnJvmLogTotalLoginfo                                     | JVM日志数量_LogInfo                                          | 个       | Info 日志数量                                        | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnGcUtilMemoryS0                                         | 内存区域占比_S0                                              | %        | Survivor 0区内存使用占比                             | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnGcUtilMemoryS1                                         | 内存区域占比_S1                                              | %        | Survivor 1区内存使用占比                             | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnGcUtilMemoryE                                          | 内存区域占比_E                                               | %        | Eden 区内存使用占比                                  | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnGcUtilMemoryO                                          | 内存区域占比_O                                               | %        | Old 区内存使用占比                                   | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnGcUtilMemoryM                                          | 内存区域占比_M                                               | %        | Metaspace 区内存使用占比                             | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnGcUtilMemoryCcs                                        | 内存区域占比_CCS                                             | %        | Compressed class space 区内存使用占比                | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnStaleStorages<br>CountNumstalestorages                 | 被标记为过期的存储的数量_NumStaleStorages                    | 个       | 由于心跳延迟而标记为过期的 DataNodes 当前数目        | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnPendingDatanodeMessage<br>CountPendingdatanodemessagecount | 备NN上挂起的与BLOCK相关操作的消息数量_PendingDataNodeMessageCount | 个/s     | DATANODE 的请求被 QUEUE 在 standby namenode 中的个数 | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnBlocksMissingNum<br>berofmissingblocks                 | 缺失块统计_NumberOfMissingBlocks                             | 个       | 缺失的数据块数量                                     | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnBlocksMissingNumberof<br>missingblockswithreplicationfactorOne | 缺失块统计_NumberOf<br>MissingBlocksWithReplicationFactorOne | 个       | 缺失的数据库数量（rf = 1）                           | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnSnapshotOpsAllowsnapshotops                            | SNAPSHOT操作_AllowSnapshotOps                                | 次/s     | 每秒执行 AllowSnapshot 操作的次数                    | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnSnapshotOps<br>Disallowsnapshotops                     | SNAPSHOT操作_DisallowSnapshotOps                             | 次/s     | 每秒执行 DisallowSnapshot 操作的次数                 | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnSnapshotOps<br>Createsnapshotops                       | SNAPSHOT操作_CreateSnapshotOps                               | 次/s     | 每秒执行 CreateSnapshot 操作的次数                   | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnSnapshotOps<br>Deletesnapshotops                       | SNAPSHOT操作_DeleteSnapshotOps                               | 次/s     | 每秒执行 DeleteSnapshot 操作的次数                   | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnSnapshotOps<br>Listsnapshottabledirops                 | SNAPSHOT操作_ListSnapshottableDirOps                         | 次/s     | 每秒执行 ListSnapshottableDir 操作次数               | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnSnapshotOps<br>Snapshotdiffreportops                   | SNAPSHOT操作_SnapshotDiffReportOps                           | 次/s     | 每秒执行 SnapshotDiffReportOps 的次数                | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnSnapshotOps<br>Renamesnapshotops                       | SNAPSHOT操作_RenameSnapshotOps                               | 次/s     | 每秒执行 RenameSnapshotOps 的次数                    | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnFilesOpsCreatefileops                                  | 文件操作_CreateFileOps                                       | 次/s     | 每秒执行 CreateFile 操作的次数                       | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnFilesOpsGetlistingops                                  | 文件操作_GetListingOps                                       | 次/s     | 每秒执行 GetListing 操作的次数                       | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnFilesOpsTotalfileops                                   | 文件操作_TotalFileOps                                        | 次/s     | 每秒执行 TotalFileOps 的次数                         | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnFilesOpsDeletefileops                                  | 文件操作_DeleteFileOps                                       | 次/s     | 每秒执行 DeleteFile 操作的次数                       | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnFilesOpsFileinfoops                                    | 文件操作_FileInfoOps                                         | 次/s     | 每秒执行 FileInfo 操作的次数                         | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnFilesOpsGetadditional<br>datanodeops                   | 文件操作_GetAdditionalDatanodeOps                            | 次/s     | 每秒执行 GetAdditionalDatanode 操作的次数            | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnFilesOpsCreatesymlinkops                               | 文件操作_CreateSymlinkOps                                    | 次/s     | 每秒执行 CreateSymlink 操作的次数                    | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnFilesOpsGetlinktargetops                               | 文件操作_GetLinkTargetOps                                    | 次/s     | 每秒执行 GetLinkTarget 操作的次数                    | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnFilesOpsFilesingetlistingops                           | 文件操作_FilesInGetListingOps                                | 次/s     | 每秒执行 FilesInGetListing 操作的次数                | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnTransactionOps<br>Transactionsnumops                   | 事务操作_TransactionsNumOps                                  | 次/s     | 每秒处理 Journal transaction 操作的次数              | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnTransactionOps<br>Transactionsbatchedinsync            | 事务操作_TransactionsBatchedInSync                           | 次/s     | 每秒批量处理 Journal transaction 操作次数            | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnImageOpsGeteditnumops                                  | 镜像操作_GetEditNumOps                                       | 次/s     | 每秒执行 GetEditNumOps 的次数                        | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnImageOpsGetimagenumops                                 | 镜像操作_GetImageNumOps                                      | 次/s     | 每秒执行 GetImageNumOps 的次数                       | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnImageOpsPutimagenumops                                 | 镜像操作_PutImageNumOps                                      | 次/s     | 每秒执行 PutImageNumOps 的次数                       | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnSyncsOpsSyncsnumops                                    | SYNC操作_SyncsNumOps                                         | 次/s     | 每秒处理 Journal syncs 操作的次数                    | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnBlocksOpsBlock<br>receivedanddeletedops                | 数据块操作_BlockOpsQueued                                    | 次/s     | 每秒执行 BlockReceivedAndDeletedOps 的次数           | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnBlocksOpsBlockopsqueued                                | 数据块操作_BlockOpsQueued                                    | 次/s     | 处理 DataNode Block 上报操作的延迟                   | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnCacheReportOps<br>Cachereportnumops                    | 缓存汇报_CacheReportNumOps                                   | 次/s     | 每秒处理 CacheReport 操作的次数                      | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnBlockReportOps<br>Blockreportnumops                    | 数据块汇报_BlockReportNumOps                                 | 次/s     | 每秒处理 DataNode Blcok 上报操作的次数               | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnSyncsRtSyncsavgtime                                    | SYNCS操作延迟_SyncsAvgTime                                   | ms       | 处理 Journal syncs 操作的平均延迟                    | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnCacheReportRt<br>Cachereportavgtime                    | Cache汇报延迟_CacheReportAvgTime                             | ms       | 缓存上报动作平均延迟                                 | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnImageRtGeteditavgtime                                  | 镜像操作延迟_GetEditAvgTime                                  | ms       | 读取 Edit 文件操作平均延迟                           | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnImageRtGetimageavgtime                                 | 镜像操作延迟_GetImageAvgTime                                 | ms       | 读取镜像文件平均延迟                                 | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnImageRtPutimageavgtime                                 | 镜像操作延迟_PutImageAvgTime                                 | ms       | 写入镜像文件平均延迟                                 | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnTransactionRt<br>Transactionsavgtime                   | 事务操作延迟_TransactionsAvgTime                             | ms       | 处理 Journal transaction 操作的平均延迟              | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnStartTimeStarttime                                     | 启动时间_StartTime                                           | ms       | 进程启动时间                                         | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnStateState                                             | 主备情况_State                                               | -        | NN 状态                                              | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnThreadCountPeakthreadcount                             | 线程数量_PeakThreadCount                                     | 个       | 峰值线程数                                           | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnThreadCountThreadcount                                 | 线程数量_ThreadCount                                         | 个       | 线程数量                                             | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsNnThreadCount<br>Daemonthreadcount                       | 线程数量_DaemonThreadCount                                   | 个       | 后台线程数量                                         | id4hdfsdatanode、<br>host4hdfsdatanode |

### HDFS-DataNode

| 指标英文名                                                   | 指标中文名                                                | 指标单位 | 指标含义                                   | 维度                                   |
| ------------------------------------------------------------ | --------------------------------------------------------- | -------- | ------------------------------------------ | -------------------------------------- |
| HdfsDnXceiverXceivercount                                    | XCEIVER数量_XceiverCount                                  | 个       | Xceiver 数量                               | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnBytesByteswrittenmb                                    | 数据读写速率_BytesReadMB                                  | Bytes/s  | 写入 DN 的字节速率                         | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnBytesBytesreadmb                                       | 数据读写速率_BytesReadMB                                  | Bytes/s  | 读取 DN 的字节速率                         | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnBytesRemotebytesreadmb                                 | 数据读写速率_RemoteBytesReadMB                            | Bytes/s  | 远程客户端读取字节速率                     | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnBytesRemoteby<br>teswrittenmb                          | 数据读写速率_RemoteBytesWrittenMB                         | Bytes/s  | 远程客户端写入字节速率                     | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnClientWritesfrom<br>remoteclient                       | 客户端连接数_WritesFromRemoteClient                       | 个       | 来自远程客户端写操作 QPS                   | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnClientWritesfromlocalclient                            | 客户端连接数_WritesFromLocalClient                        | 个       | 来自本地客户端写操作 OPS                   | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnClientReadsfrom<br>remoteclient                        | 客户端连接数_ReadsFromRemoteClient                        | 个       | 来自远程客户端读操作 QPS                   | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnClientReadsfromlocalclient                             | 客户端连接数_ReadsFromLocalClient                         | 个       | 来自本地客户端读操作 QPS                   | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnBlocksVerifiedFailures<br>Blockverificationfailures    | Block校验失败_BlockVerificationFailures                   | 次/s     | BLOCK 校验失败数量                         | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnVolumeFailures<br>Volumefailures                       | 磁盘故障_VolumeFailures                                   | 次/s     | 磁盘故障次数                               | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnNetworkErrors<br>Datanodenetworkerrors                 | 网络错误_DatanodeNetworkErrors                            | 次/s     | 网络错误统计                               | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnHbRtHeartbeatsavgtime                                  | 心跳延迟_HeartbeatsAvgTime                                | ms       | 心跳接口平均时间                           | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnHbOpsHeartbeatsnumops                                  | 心跳QPS_HeartbeatsNumOps                                  | 次/s     | 心跳接口 QPS                               | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnDatapacketAvgtimeSend<br>datapackettransfernanosavgtime | 包传输操作QPS_SendDataPacketTransferNanosAvgTime          | ms       | 发送数据包平均时间                         | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnBlocksOpsRead<br>blockopnumops                         | 数据块操作_ReadBlockOpNumOps                              | 次/s     | 从 DataNode 读取 Block OPS                 | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnBlocksOpsWrite<br>blockopnumops                        | 数据块操作_WriteBlockOpNumOps                             | 次/s     | 向 DataNode 写入 Block OPS                 | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnBlocksOpsBlock<br>checksumopnumops                     | 数据块操作_BlockChecksumOpNumOps                          | 次/s     | DataNode 进行 Checksum 操作的 OPS          | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnBlocksOpsCopy<br>blockopnumops                         | 数据块操作_CopyBlockOpNumOps                              | 次/s     | 复制 Block 操作的 OPS                      | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnBlocksOpsReplace<br>blockopnumops                      | 数据块操作_ReplaceBlockOpNumOps                           | 次/s     | Replace Block 操作的 OPS                   | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnBlocksOpsBlock<br>reportsnumops                        | 数据块操作_BlockReportsNumOps                             | 次/s     | BLOCK 汇报动作的 OPS                       | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnBlocksOpsIncremental<br>blockreportsnumops             | 数据块操作_IncrementalBlockReportsNumOps                  | 次/s     | BLOCK 增量汇报的 OPS                       | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnBlocksOpsCache<br>reportsnumops                        | 数据块操作_CacheReportsNumOps                             | 次/s     | 缓存汇报的 OPS                             | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnBlocksOpsPacketack<br>roundtriptimenanosnumops         | 数据块操作_PacketAckRoundTripTimeNanosNumOps              | 次/s     | 每秒处理 ACK ROUND TRIP 次数               | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnFsyncOpsFsync<br>nanosnumops                           | FSYNC操作_FsyncNanosNumOps                                | 次/s     | FSYNC 次数                                 | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnFlushOpsFlush<br>nanosnumops                           | FLUSH操作_FlushNanosNumOps                                | 次/s     | 每秒处理 Flush 操作次数                    | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnBlocksRtRead<br>blockopavgtime                         | 数据块操作延迟统计_ReadBlockOpAvgTime                     | ms       | 读取 Block 操作平均时间                    | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnBlocksRtWrite<br>blockopavgtime                        | 数据块操作延迟统计_ReplaceBlockOpAvgTime                  | ms       | 写 Blcok 操作平均时间                      | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnBlocksRtBlock<br>checksumopavgtime                     | 数据块操作延迟统计_BlockChecksumOpAvgTime                 | ms       | 块校验操作平均时间                         | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnBlocksRtCopy<br>blockopavgtime                         | 数据块操作延迟统计_CopyBlockOpAvgTime                     | ms       | 复制块操作平均时间                         | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnBlocksRt<br>Replaceblockopavgtime                      | 数据块操作延迟统计_Replaceblockopavgtime                  | ms       | Replace Block 操作平均时间                 | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnBlocksRtBlock<br>reportsavgtime                        | 数据块操作延迟统计_BlockReportsAvgTime                    | ms       | 块汇报平均时间                             | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnBlocksRtIncremental<br>blockreportsavgtime             | 数据块操作延迟统计_IncrementalBlockReportsAvgTime         | ms       | 增量块汇报平均时间                         | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnBlocksRtCache<br>reportsavgtime                        | 数据块操作延迟统计_CacheReportsAvgTime                    | ms       | 缓存汇报平均时间                           | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnBlocksRtPacketack<br>roundtriptimenanosavgtime         | 数据块操作延迟统计_PacketAckRoundTripTimeNanosAvgTime     | ms       | 处理 ACK ROUND TRIP 平均时间               | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnFlushRtFlushnanosavgtime                               | FLUSH延迟_FlushNanosAvgTime                               | ms       | Flush 操作平均时间                         | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnFsyncRtFsyncnanosavgtime                               | FSYNC延迟_FsyncNanosAvgTime                               | ms       | Fsync 操作平均时间                         | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnRamBlocksOp<br>Ramdiskblockswrite                      | RAMDISKBlocks_RamDiskBlocksWrite                          | 块/s     | 写入内存的块的总数                         | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnRamBlocksOp<br>Ramdiskblockswritefallback              | RAMDISKBlocks_RamDiskBlocksWriteFallback                  | 块/s     | 写入内存但未成功的块总数（故障转移到磁盘） | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnRamBlocksOpRamdisk<br>blocksdeletedbeforelazypersisted | RAMDISKBlocks_RamDiskBlocks<br>DeletedBeforeLazyPersisted | 块/s     | 应用程序在被保存到磁盘之前被删除的块的总数 | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnRamBlocksOp<br>Ramdiskblocksreadhits                   | RAMDISKBlocks_RamDiskBlocksReadHits                       | 块/s     | 内存中的块被读取的总次数                   | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnRamBlocksOp<br>Ramdiskblocksevicted                    | RAMDISKBlocks_RamDiskBlocksEvicted                        | 块/s     | 内存中被清除的块总数                       | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnRamBlocksOpRamdisk<br>blocksevictedwithoutread         | RAMDISKBlocks_RamDiskBlocks<br>EvictedWithoutRead         | 块/s     | 从内存中取出的内存块总数                   | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnRamBlocksOp<br>Ramdiskblockslazypersisted              | RAMDISKBlocks_RamDisk<br>BlocksLazyPersisted              | 块/s     | 惰性写入器写入磁盘的总数                   | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnRamBlocksOp<br>Ramdiskbyteslazypersisted               | RAMDISKBlocks_RamDiskBytesLazyPersisted                   | Bytes/s  | 由懒惰写入器写入磁盘的总字节数             | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnRamBlocksBytes<br>Ramdiskbyteswrite                    | RAMDISK写入速度_RamDiskBytesWrite                         | Bytes/s  | 写入内存的总字节数                         | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnJvmMem<br>Memnonheapusedm                              | JVM内存_MemNonHeapUsedM                                   | MB       | JVM 当前已经使用的 NonHeapMemory 的大小    | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnJvmMem<br>Memnonheapcommittedm                         | JVM内存_MemNonHeapCommittedM                              | MB       | JVM 配置的 NonHeapCommittedM 的大小        | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnJvmMemMemheapusedm                                     | JVM内存_MemHeapUsedM                                      | MB       | JVM 当前已经使用的 HeapMemory 的大小       | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnJvmMem<br>Memheapcommittedm                            | JVM内存_MemHeapCommittedM                                 | MB       | JVM HeapMemory 提交大小                    | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnJvmMemMemheapmaxm                                      | JVM内存_MemHeapMaxM                                       | MB       | JVM 配置的 HeapMemory 的大小               | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnJvmMemMemmaxm                                          | JVM内存_MemMaxM                                           | MB       | JVM 运行时的可以使用的最大的内存的大小     | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnJvmJavaThreadsThreadsnew                               | JVM线程数量_ThreadsNew                                    | 个       | 处于新建状态的线程数量                     | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnJvmJavaThreads<br>Threadsrunnable                      | JVM线程数量_ThreadsRunnable                               | 个       | 处于可运行状态的线程数量                   | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnJvmJavaThreads<br>Threadsblocked                       | JVM线程数量_ThreadsBlocked                                | 个       | 处于阻塞状态的线程数量                     | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnJvmJavaThreads<br>Threadswaiting                       | JVM线程数量_ThreadsWaiting                                | 个       | 处于 WAITING 状态的线程数量                | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnJvmJavaThreads<br>Threadstimedwaiting                  | JVM线程数量_ThreadsTimedWaiting                           | 个       | 处于 TIMED WAITING 状态的线程数量          | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnJvmJavaThreads<br>Threadsterminated                    | JVM线程数量_ThreadsTerminated                             | 个       | 处于 Terminated 状态的线程数量             | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnJvmLogTotalLogfatal                                    | JVM日志数量_LogFatal                                      | 个       | Fatal 日志数量                             | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnJvmLogTotalLogerror                                    | JVM日志数量_LogError                                      | 个       | Error 日志数量                             | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnJvmLogTotalLogwarn                                     | JVM日志数量_LogWarn                                       | 个       | Warn 日志数量                              | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnJvmLogTotalLoginfo                                     | JVM日志数量_LogInfo                                       | 个       | Info 日志数量                              | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnGcUtilMemoryS0                                         | 内存区域占比_S0                                           | %        | Survivor 0区内存使用占比                   | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnGcUtilMemoryS1                                         | 内存区域占比_S1                                           | %        | Survivor 1区内存使用占比                   | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnGcUtilMemoryE                                          | 内存区域占比_E                                            | %        | Eden 区内存使用占比                        | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnGcUtilMemoryO                                          | 内存区域占比_O                                            | %        | Old 区内存使用占比                         | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnGcUtilMemoryM                                          | 内存区域占比_M                                            | %        | Metaspace 区内存使用占比                   | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnGcUtilMemoryCcs                                        | 内存区域占比_CCS                                          | %        | Compressed class space 区内存使用占比      | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnGcUtilGcCountFgc                                       | GC次数_FGC                                                | 次       | Full GC 次数                               | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnGcUtilGcCountYgc                                       | GC次数_YGC                                                | 次       | Young GC 次数                              | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnGcUtilGcTimeYgct                                       | GC时间_YGCT                                               | s        | Young GC 消耗时间                          | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnGcUtilGcTimeFgct                                       | GC时间_FGCT                                               | s        | Full GC 消耗时间                           | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnGcUtilGcTimeGct                                        | GC时间_GCT                                                | s        | 垃圾回收时间消耗                           | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnPort4004RxtxReceivedbytes                              | 数据流量_ReceivedBytes                                    | Bytes/s  | 接收数据速率                               | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnPort4004RxtxSentbytes                                  | 数据流量_SentBytes                                        | Bytes/s  | 发送数据速率                               | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnPort4004QpsRpc<br>queuetimenumops                      | QPS_RpcQueueTimeNumOps                                    | 次/s     | RPC 调用速率                               | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnPort4004RtRpc<br>queuetimeavgtime                      | 请求处理延迟_RpcQueueTimeAvgTime                          | ms       | RPC 平均延迟时间                           | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnPort4004AuthRpc<br>authenticationfailures              | 验证和授权_RpcAuthenticationFailures                      | 次/s     | RPC 验证失败次数                           | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnPort4004AuthRpc<br>authenticationsuccesses             | 验证和授权_RpcAuthenticationSuccesses                     | 次/s     | RPC 验证成功次数                           | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnPort4004AuthRpc<br>authorizationfailures               | 验证和授权_RpcAuthorizationFailures                       | 次/s     | RPC 授权失败次数                           | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnPort4004AuthRpc<br>authorizationsuccesses              | 验证和授权_RpcAuthorizationSuccesses                      | 次/s     | RPC 授权成功次数                           | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnPort4004Connections<br>Numopenconnections              | 当前连接数_NumOpenConnections                             | 个       | 当前链接数量                               | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnPort4004QueueLen<br>Callqueuelength                    | RPC处理队列长度_CallQueueLength                           | 个       | 当前 RPC 处理队列长度                      | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnThreadTimeCurrent<br>threadcputime                     | CPU时间_CurrentThreadCpuTime                              | ms       | CPU时间                                    | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnThreadTimeCurrent<br>threadusertime                    | CPU时间_CurrentThreadUserTime                             | ms       | 用户时间                                   | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnStartTimeStarttime                                     | 线程数量_DaemonThreadCount                                | s        | 进程启动时间                               | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnThreadCount<br>Peakthreadcount                         | 程数量_PeakThreadCount                                    | 个       | 峰值线程数量                               | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnThreadCount<br>Daemonthreadcount                       | 线程数量_DaemonThreadCount                                | 个       | 后台线程数量                               | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnRtWrit                                                 | 读写延迟_Write                                            | MB/s     | 磁盘写速率                                 | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnRtRead                                                 | 读写延迟_Read                                             | 次/s     | 读操作 QPS                                 | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnDatapacketOps<br>Datapacketops                         | 包传输操作QPS_DataPacketOps                               | 次/s     | 包传输操作 QPS                             | id4hdfsdatanode、<br>host4hdfsdatanode |

### HDFS-Journal Node 

| 指标英文名                                       | 指标中文名                            | 指标单位 | 指标含义                                |                                        |
| ------------------------------------------------ | ------------------------------------- | -------- | --------------------------------------- | -------------------------------------- |
| HdfsJnJvmMemMemnon<br>heapusedm                  | JVM内存_MemNonHeapUsedM               | MB       | JVM 当前已经使用的 NonHeapMemory 的大小 | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsJnJvmMemMemnon<br>heapcommittedm             | JVM内存_MemNonHeapCommittedM          | MB       | JVM 内存                                | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsJnJvmMemMem<br>heapusedm                     | JVM内存_MemHeapUsedM                  | MB       | JVM 当前已经使用的 HeapMemory 的大小    | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsJnJvmMemMem<br>heapcommittedm                | JVM内存_MemHeapCommittedM             | MB       | JVM HeapMemory 提交大小                 | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsJnJvmMemMem<br>heapmaxm                      | JVM内存_MemHeapMaxM                   | MB       | JVM 配置的 HeapMemory 的大小            | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsJnJvmMemMemmaxm                              | JVM内存_MemMaxM                       | MB       | JVM 运行时的可以使用的最大的内存的大小  | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsJnJvmJavaThreads<br>Threadsnew               | JVM线程数量_ThreadsNew                | 个       | 处于新建状态的线程数量                  | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsJnJvmJavaThreads<br>Threadsrunnable          | JVM线程数量_ThreadsRunnable           | 个       | 处于可运行状态的线程数量                | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsJnJvmJavaThreads<br>Threadsblocked           | JVM线程数量_ThreadsBlocked            | 个       | 处于阻塞状态的线程数量                  | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsJnJvmJavaThreads<br>Threadswaiti             | JVM线程数量_ThreadsWaiting            | 个       | 处于 WAITING 状态的线程数量             | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsJnJvmJavaThreads<br>Threadstimedwaiting      | JVM线程数量_ThreadsTimedWaiting       | 个       | 处于 TIMED WAITING 状态的线程数量       | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsJnJvmJavaThreads<br>Threadsterminated        | JVM线程数量_ThreadsTerminated         | 个       | 处于 Terminated 状态的线程数量          | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsJnJvmLogTotalLogfatal                        | JVM日志数量_LogFatal                  | 个       | Fatal 日志数量                          | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsJnJvmLogTotalLogerror                        | JVM日志数量_LogError                  | 个       | Error 日志数量                          | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsJnJvmLogTotalLogwarn                         | JVM日志数量_LogWarn                   | 个       | Warn 日志数量                           | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsJnJvmLogTotalLoginfo                         | JVM日志数量_LogInfo                   | 个       | Info 日志数量                           | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsJnGcUtilMemoryS0                             | 内存区域占比_S0                       | %        | Survivor 0区内存使用占比                | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsJnGcUtilMemoryS1                             | 内存区域占比_S1                       | %        | Survivor 1区内存使用占比                | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsJnGcUtilMemoryE                              | 内存区域占比_E                        | %        | Eden 区内存使用占比                     | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsJnGcUtilMemoryO                              | 内存区域占比_O                        | %        | Old 区内存使用占比                      | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsJnGcUtilMemoryM                              | 内存区域占比_M                        | %        | Metaspace 区内存使用占比                | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsJnGcUtilMemoryCcs                            | 内存区域占比_CCS                      | %        | Compressed class space 区内存使用占比   | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsJnGcUtilGcCountFgc                           | GC次数_FGC                            | 次       | Full GC 次数                            | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsJnGcUtilGcCountYgc                           | GC次数_YGC                            | 次       | Young GC 次数                           | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsJnGcUtilGcTimeYgct                           | GC时间_YGCT                           | s        | Young GC 消耗时间                       | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsJnGcUtilGcTimeFgct                           | GC时间_FGCT                           | s        | Full GC 消耗时间                        | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsJnGcUtilGcTimeGct                            | GC时间_GC                             | s        | 垃圾回收时间消耗                        | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsJnPort4005Rxtx<br>Receivedbytes              | 数据流量_ReceivedBytes                | Bytes/s  | 接收数据速率                            | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsJnPort4005Rxtx<br>Receivedbytes              | 数据流量_ReceivedBytes                | Bytes/s  | 发送数据速率                            | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsJnPort4005QpsRpc<br>queuetimenumops          | QPS_RpcQueueTimeNumOps                | 次/s     | RPC 调用速率                            | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsJnPort4005RtRpc<br>queuetimeavgtime          | 请求处理延迟_RpcQueueTimeAvgTime      | ms       | RPC 平均延迟时间                        | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsJnPort4005AuthRpc<br>authenticationfailures  | 验证和授权_RpcAuthenticationFailures  | 次/s     | RPC 验证失败次数                        | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsJnPort4005AuthRpc<br>authorizationsuccesses  | 验证和授权_RpcAuthorizationSuccesses  | 次/s     | RPC 授权成功次数                        | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsJnPort4005AuthRpc<br>authenticationsuccesses | 验证和授权_RpcAuthenticationSuccesses | 次/s     | RPC 验证成功次数                        | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsJnPort4005AuthRpc<br>authorizationfailures   | 验证和授权_RpcAuthorizationFailures   | 次/s     | RPC 授权失败次数                        | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsJnPort4005Connections<br>Numopenconnections  | 当前连接数_NumOpenConnections         | 个       | 当前链接数量                            | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsJnPort4005QueueLen<br>Callqueuelength        | RPC处理队列长度_CallQueueLength       | 个       | 当前 RPC 处理队列长度                   | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsJnThreadTimeCurrent<br>threadcputime         | CPU时间_CurrentThreadCpuTime          | ms       | CPU时间                                 | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsJnThreadTimeCurrent<br>threadusertime        | CPU时间_CurrentThreadUserTime         | ms       | 用户时间                                | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsJnStartTimeStarttime                         | 启动时间_StartTime                    | s        | 进程启动时间                            | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsJnThreadCount<br>Threadcount                 | 线程数量_ThreadCount                  | 个       | 线程数量                                | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsJnThreadCount<br>Peakthreadcount             | 线程数量_PeakThreadCount              | 个       | 峰值线程数量                            | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsJnThreadCountDaemon<br>threadcount           | 线程数量_DaemonThreadCount            | 个       | 后台线程数量                            | id4hdfsdatanode、<br>host4hdfsdatanode |

### HDFS-ZKFC

| 指标英文名               | 指标中文名       | 指标单位 | 指标含义                              | 维度                                   |
| ------------------------ | ---------------- | -------- | ------------------------------------- | -------------------------------------- |
| HdfsDfzkGcUtilMemoryS0   | 内存区域占比_S0  | %        | Survivor 0区内存使用占比              | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDfzkGcUtilMemoryS1   | 内存区域占比_S1  | %        | Survivor 1区内存使用占比              | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDfzkGcUtilMemoryE    | 内存区域占比_E   | %        | Eden 区内存使用占比                   | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDfzkGcUtilMemoryO    | 内存区域占比_O   | %        | Old 区内存使用占比                    | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDfzkGcUtilMemoryM    | 内存区域占比_M   | %        | Metaspace 区内存使用占比              | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDfzkGcUtilMemoryCcs  | 内存区域占比_CCS | %        | Compressed class space 区内存使用占比 | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDfzkGcUtilGcCountFgc | GC次数_FGC       | 次       | Full GC 次数                          | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDfzkGcUtilGcCountYgc | GC次数_YGC       | 次       | Young GC 次数                         | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDfzkGcUtilGcTimeYgct | GC时间_YGCT      | s        | Young GC 消耗时间                     | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDfzkGcUtilGcTimeFgct | GC时间_FGCT      | s        | Full GC 消耗时间                      | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDfzkGcUtilGcTimeGct  | GC时间_GCT       | s        | 垃圾回收时间消耗                      | id4hdfsdatanode、<br>host4hdfsdatanode |

> ?每个指标的统计粒度（Period）可取值不一定相同，可通过 [DescribeBaseMetrics](https://cloud.tencent.com/document/product/248/30351) 接口获取每个指标支持的统计粒度。

## 各维度对应参数总览

| 参数名称                       | 维度名称          | 维度解释                  | 格式                                       |
| ------------------------------ | ----------------- | ------------------------- | ------------------------------------------ |
| Instances.N.Dimensions.0.Name  | id4hdfsdatanode   | EMR 实例ID的维度名称      | 输入String 类型维度名称：id4hdfsdatanode   |
| Instances.N.Dimensions.0.Value | id4hdfsdatanode   | EMR 实例具体ID            | 输入EMR具体实例 ID，例如 ：emr-mm8bs222    |
| Instances.N.Dimensions.0.Name  | host4hdfsdatanode | EMR实例中节点IP的维度名称 | 输入String 类型维度名称：host4hdfsdatanode |
| Instances.N.Dimensions.0.Value | host4hdfsdatanode | EMR实例中具体节点IP       | 输入具体节点IP ，例如：1.1.1.1             |
