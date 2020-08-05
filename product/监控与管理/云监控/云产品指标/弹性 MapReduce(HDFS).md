## 命名空间

Namespace=QCE/TXMR_HDFS

## 监控指标

弹性 MapReduce（HDFS）提供 [HDFS-Overview、HDFS-OverviewAggregation](#hdfs-overview.E3.80.81hdfs-overviewaggregation)、[HDFS-NameNode](#hdfs-namenode)、[HDFS-DataNode](#hdfs-datanode)、[HDFS-Journal Node](#hdfs-journal-node) 和 [HDFS-ZKFC](#hdfs-zkfc) 指标。

> ?维度对应参数，请单击 [各维度对应参数总览](#.E5.90.84.E7.BB.B4.E5.BA.A6.E5.AF.B9.E5.BA.94.E5.8F.82.E6.95.B0.E6.80.BB.E8.A7.88) 查看。

### HDFS-Overview、HDFS-OverviewAggregation 

> ?
>
> 1. 查询 HDFS-Overview 的指标时，需加上前缀“EmrHdfsOverview”。
> 2. 查询 HDFS-OverviewAggregation 的指标时，需加上前缀“EmrHdfsOverviewAggregation”。

| 指标英文名                                  | 指标中文名                                | 单位 | 指标含义                                      | 维度               |
| ------------------------------------------- | ----------------------------------------- | ---- | --------------------------------------------- | ------------------ |
| HdfsNnBlockCapacityTotal                    | 集群存储容量_CapacityTotal                | GB   | 集群存储总容量                                | InstanceId、NodeIP |
| HdfsNnBlockCapacityUsed                     | 集群存储容量_CapacityUsed                 | GB   | 集群储存已使用容量                            | InstanceId、NodeIP |
| HdfsNnBlockCapacityRemaining                | 集群存储容量_CapacityRemaining            | GB   | 集群存储剩余容量                              | InstanceId、NodeIP |
| HdfsNnBlockCapacity<br>UsedNonDFS           | 集群存储容量_CapacityUsedNonDFS           | GB   | 集群非 HDFS 使用容量                          | InstanceId、NodeIP |
| HdfsNnBlockTotalLoad                        | 集群负载_TotalLoad                        | 个   | 当前连接数                                    | InstanceId、NodeIP |
| HdfsNnBlockFilesTotal                       | 群文件总数量_FilesTotal                   | 个   | 总文件数量                                    | InstanceId、NodeIP |
| HdfsNnBlockBlockstotal                      | BLOCKS 数量_BlocksTotal                    | 个   | 总 BLOCK 数量                                 | InstanceId、NodeIP |
| HdfsNnBlockPending<br>ReplicationBlocks     | BLOCKS 数量_PendingReplicationBlocks      | 个   | 等待被备份的块数量                            | InstanceId、NodeIP |
| HdfsNnBlockUnder<br>ReplicatedBlocks        | BLOCKS 数量 _UnderReplicatedBlocks        | 个   | 副本数不够的块数量                            | InstanceId、NodeIP |
| HdfsNnBlockBlocksCorruptblocks              | BLOCKS 数量 _CorruptBlocks                | 个   | 坏块数量                                      | InstanceId、NodeIP |
| HdfsNnBlockScheduled<br>ReplicationBlocks   | BLOCKS 数量 _ScheduledReplicationBlocks   | 个   | 安排要备份的块数量                            | InstanceId、NodeIP |
| HdfsNnBlockPending<br>DeletionBlocks        | BLOCKS 数量 _PendingDeletionBlocks        | 个   | 等待被删除的块数量                            | InstanceId、NodeIP |
| HdfsNnBlockCorruptblocks                    | BLOCKS 数量 _CorruptBlocks                | 个   | 多于的块数量                                  | InstanceId、NodeIP |
| HdfsNnBlockPostponed<br>MisreplicatedBlocks | BLOCKS 数量 _PostponedMisreplicatedBlocks | 个   | 被推迟处理的异常块数量                        | InstanceId、NodeIP |
| HdfsNnBlockBlockCapacity                    | BLOCK 容量 _BlockCapacity                 | 个   | BLOCK 容量                                    | InstanceId、NodeIP |
| HdfsNnBlockNumLiveDataNodes                 | 集群数据节点 _NumLiveDataNodes            | 个   | 存活的数据节点数量                            | InstanceId、NodeIP |
| HdfsNnBlockNumDeadDataNodes                 | 集群数据节点 _NumDeadDataNodes            | 个   | 已经标记为 Dead 状态的数据节点数量            | InstanceId、NodeIP |
| HdfsNnBlockNum<br>DecomLiveDataNodes        | 集群数据节点 _NumDecomLiveDataNodes       | 个   | 下线且 Live 的节点数量                        | InstanceId、NodeIP |
| HdfsNnBlockNum<br>DecomDeadDataNodes        | 集群数据节点 _NumDecomDeadDataNodes       | 个   | 下线且 Dead 的节点数量                        | InstanceId、NodeIP |
| HdfsNnBlockNum<br>DecommissioningDataNodes  | 集群数据节点 _NumDecommissioningDataNodes | 个   | 正在下线的节点数量                            | InstanceId、NodeIP |
| HdfsNnBlockNum<br>StaleDataNodes            | 集群数据节点 _NumStaleDataNodes           | 个   | 由于心跳延迟而标记为过期的 DataNodes 当前数量 | InstanceId、NodeIP |
| HdfsNnBlockSnapshots                        | SNAPSHOT 相关 _Snapshots                  | 个   | Snapshots 数量                                | InstanceId、NodeIP |
| HdfsNnBlockVolumeFailuresTotal              | 磁盘故障 _VolumeFailuresTotal             | 次   | 所有 Datanodes 的全故障总数                   | InstanceId、NodeIP |

### HDFS-NameNode

| 指标英文名                                                   | 指标中文名                                                   | 指标单位 | 指标含义                                             | 维度               |
| ------------------------------------------------------------ | ------------------------------------------------------------ | -------- | ---------------------------------------------------- | ------------------ |
| HdfsNnPort4007RxtxReceivedbytes                              | 数据流量<br/>_ReceivedBytes                                  | Bytes/s  | 接收数据速率                                         | InstanceId、CoreIp |
| HdfsNnPort4007RxtxSentbytes                                  | 数据流量<br/>_SentBytes                                      | Bytes/s  | 发送数据速率                                         | InstanceId、CoreIp |
| HdfsNnPort4007Qps<br>Rpcqueuetimenumops                      | QPS_RpcQueueTimeNumOps                                       | 次/s     | RPC 调用速率                                         | InstanceId、CoreIp |
| HdfsNnPort4007RtRpc<br>queuetimeavgtime                      | 请求处理延迟<br/> _RpcQueueTimeAvgTime                       | ms       | RPC 平均延迟时间                                     | InstanceId、CoreIp |
| HdfsNnPort4007AuthRpc<br>authenticationfailures              | 验证和授权<br/> _RpcAuthenticationFailure                    | 次       | RPC 验证失败次数                                     | InstanceId、CoreIp |
| HdfsNnPort4007AuthRpc<br>authenticationsuccesses             | 验证和授权<br/> _RpcAuthenticationSuccesses                  | 次       | RPC 验证成功次数                                     | InstanceId、CoreIp |
| HdfsNnPort4007AuthRpc<br>authorizationfailures               | 验证和授权<br/> _RpcAuthorizationFailures                    | 次       | RPC 授权失败次数                                     | InstanceId、CoreIp |
| HdfsNnPort4007AuthRpc<br>authorizationsuccesses              | 验证和授权<br/> _RpcAuthorizationSuccesses                   | 次       | RPC 授权成功次数                                     | InstanceId、CoreIp |
| HdfsNnPort4007Connections<br>Numopenconnections              | 当前连接数<br/> _NumOpenConnections                          | 个       | 当前链接数量                                         | InstanceId、CoreIp |
| HdfsNnPort4007Queue<br>LenCallqueuelength                    | RPC 处理队列长度<br/>_CallQueueLength                        | 个       | 当前 RPC 处理队列长度                                | InstanceId、CoreIp |
| HdfsNnJvmMemMemnonheapusedm                                  | JVM 内存<br/> _MemNonHeapUsedM                               | MB       | JVM 当前已经使用的 NonHeapMemory 的大小              | InstanceId、CoreIp |
| HdfsNnJvmMemMemnon<br>heapcommittedm                         | JVM 内存<br/>  _MemNonHeapCommittedM                         | MB       | JVM 内存                                             | InstanceId、CoreIp |
| HdfsNnJvmMemMemheapusedm                                     | JVM 内存 _MemHeapUsedM                                       | MB       | JVM 当前已经使用的 HeapMemory 的大小                 | InstanceId、CoreIp |
| HdfsNnJvmMem<br>Memheapcommittedm                            | JVM 内存  _MemHeapCommittedM                                 | MB       | JVM HeapMemory 提交大小                              | InstanceId、CoreIp |
| HdfsNnJvmMemMemheapmaxm                                      | JVM 内存  _MemHeapMaxM                                       | MB       | JVM 配置的 HeapMemory 的大小                         | InstanceId、CoreIp |
| HdfsNnJvmMemMemmaxm                                          | JVM 内存 _MemMaxM                                            | MB       | JVM 运行时的可以使用的最大的内存的大小               | InstanceId、CoreIp |
| HdfsNnBlockReportRt<br>Blockreportavgtime                    | 数据块汇报延迟<br/>_BlockReportAvgTime                       | 次/s     | 每秒处理 DataNode Blcok 平均延迟                     | InstanceId、CoreIp |
| HdfsNnGcUtilGcCountFgc                                       | GC 次数 _FGC                                                 | 次/s     | Full GC 次数                                         | InstanceId、CoreIp |
| HdfsNnGcUtilGcCountYgc                                       | C 次数  _YGC                                                 | 2次/s    | Young GC 次数                                        | InstanceId、CoreIp |
| HdfsNnGcUtilGcTimeYgct                                       | GC 时间  _YGCT                                               | ms       | Young GC 消耗时间                                    | InstanceId、CoreIp |
| HdfsNnGcUtilGcTimeFgct                                       | GC 时间 _FGCT                                                | ms       | Full GC 消耗时间                                     | InstanceId、CoreIp |
| HdfsNnGcUtilGcTimeGct                                        | GC 时间 _GCT                                                 | ms       | 垃圾回收时间消耗                                     | InstanceId、CoreIp |
| HdfsNnJvmJavaThreadsThreadsnew                               | JVM 线程数量<br/> _ThreadsNew                                | 个       | 处于新建状态的线程数量                               | InstanceId、CoreIp |
| HdfsNnJvmJavaThreads<br>Threadsrunnable                      | JVM 线程数量<br/> _ThreadsRunnable                           | 个       | 处于可运行状态的线程数量                             | InstanceId、CoreIp |
| HdfsNnJvmJavaThreads<br>Threadsblocked                       | JVM 线程数量<br/> _ThreadsBlocked                            | 个       | 处于阻塞状态的线程数量                               | InstanceId、CoreIp |
| HdfsNnJvmJavaThreads<br>Threadswaiting                       | JVM 线程数量<br/> _ThreadsWaiting                            | 个       | 处于 WAITING 状态的线程数量                          | InstanceId、CoreIp |
| HdfsNnJvmJavaThreads<br>Threadstimedwaiting                  | JVM 线程数量<br/> _ThreadsTimedWaiting                       | 个       | 处于 TIMED WAITING 状态的线程数量                    | InstanceId、CoreIp |
| HdfsNnJvmJavaThreads<br>Threadsterminated                    | JVM 线程数量<br/>_ThreadsTerminated                          | 个       | 处于 Terminated 状态的线程数量                       | InstanceId、CoreIp |
| HdfsNnJvmLogTotalLogfatal                                    | JVM 日志数量<br/> _LogFatal                                  | 个       | Fatal 日志数量                                       | InstanceId、CoreIp |
| HdfsNnJvmLogTotalLogerror                                    | JVM 日志数量<br/> _LogError                                  | 个       | Error 日志数量                                       | InstanceId、CoreIp |
| HdfsNnJvmLogTotalLogwarn                                     | JVM 日志数量<br/> _LogWarn                                   | 个       | Warn 日志数量                                        | InstanceId、CoreIp |
| HdfsNnJvmLogTotalLoginfo                                     | JVM 日志数量<br/> _LogInfo                                   | 个       | Info 日志数量                                        | InstanceId、CoreIp |
| HdfsNnGcUtilMemoryS0                                         | 内存区域占比 _S0                                             | %        | Survivor 0区内存使用占比                             | InstanceId、CoreIp |
| HdfsNnGcUtilMemoryS1                                         | 内存区域占比 _S1                                             | %        | Survivor 1区内存使用占比                             | InstanceId、CoreIp |
| HdfsNnGcUtilMemoryE                                          | 内存区域占比 _E                                              | %        | Eden 区内存使用占比                                  | InstanceId、CoreIp |
| HdfsNnGcUtilMemoryO                                          | 内存区域占比 _O                                              | %        | Old 区内存使用占比                                   | InstanceId、CoreIp |
| HdfsNnGcUtilMemoryM                                          | 内存区域占比 _M                                              | %        | Metaspace 区内存使用占比                             | InstanceId、CoreIp |
| HdfsNnGcUtilMemoryCcs                                        | 内存区域占比 _CCS                                            | %        | Compressed class space 区内存使用占比                | InstanceId、CoreIp |
| HdfsNnStaleStorages<br>CountNumstalestorages                 | 被标记为过期的存储的数量<br/> _NumStaleStorages              | 个       | 由于心跳延迟而标记为过期的 DataNodes 当前数目        | InstanceId、CoreIp |
| HdfsNnPendingDatanodeMessage<br>CountPendingdatanodemessagecount | 备 NN 上挂起的与 BLOCK 相关操作的消息数量<br/>_PendingDataNodeMessageCount | 个/s     | DATANODE 的请求被 QUEUE 在 standby namenode 中的个数 | InstanceId、CoreIp |
| HdfsNnBlocksMissingNum<br>berofmissingblocks                 | 缺失块统计<br/> _NumberOfMissingBlocks                       | 个       | 缺失的数据块数量                                     | InstanceId、CoreIp |
| HdfsNnBlocksMissingNumberof<br>missingblockswithreplicationfactorOne | 缺失块统计<br/> _NumberOfMissingBlocks<br>WithReplicationFactorOne | 个       | 缺失的数据库数量（rf = 1）                           | InstanceId、CoreIp |
| HdfsNnSnapshotOpsAllowsnapshotops                            | SNAPSHOT 操作<br/> _AllowSnapshotOps                         | 次/s     | 每秒执行 AllowSnapshot 操作的次数                    | InstanceId、CoreIp |
| HdfsNnSnapshotOps<br>Disallowsnapshotops                     | SNAPSHOT 操作<br/> _DisallowSnapshotOps                      | 次/s     | 每秒执行 DisallowSnapshot 操作的次数                 | InstanceId、CoreIp |
| HdfsNnSnapshotOps<br>Createsnapshotops                       | SNAPSHOT 操作<br/> _CreateSnapshotOps                        | 次/s     | 每秒执行 CreateSnapshot 操作的次数                   | InstanceId、CoreIp |
| HdfsNnSnapshotOps<br>Deletesnapshotops                       | SNAPSHOT 操作<br/> _DeleteSnapshotOps                        | 次/s     | 每秒执行 DeleteSnapshot 操作的次数                   | InstanceId、CoreIp |
| HdfsNnSnapshotOps<br>Listsnapshottabledirops                 | SNAPSHOT 操作<br/> _ListSnapshottableDirOps                  | 次/s     | 每秒执行 ListSnapshottableDir 操作次数               | InstanceId、CoreIp |
| HdfsNnSnapshotOps<br>Snapshotdiffreportops                   | SNAPSHOT 操作<br/> _SnapshotDiffReportOps                    | 次/s     | 每秒执行 SnapshotDiffReportOps 的次数                | InstanceId、CoreIp |
| HdfsNnSnapshotOps<br>Renamesnapshotops                       | SNAPSHOT 操作<br/> _RenameSnapshotOps                        | 次/s     | 每秒执行 RenameSnapshotOps 的次数                    | InstanceId、CoreIp |
| HdfsNnFilesOpsCreatefileops                                  | 文件操作 _CreateFileOps                                      | 次/s     | 每秒执行 CreateFile 操作的次数                       | InstanceId、CoreIp |
| HdfsNnFilesOpsGetlistingops                                  | 文件操作 _GetListingOps                                      | 次/s     | 每秒执行 GetListing 操作的次数                       | InstanceId、CoreIp |
| HdfsNnFilesOpsTotalfileops                                   | 文件操作 _TotalFileOps                                       | 次/s     | 每秒执行 TotalFileOps 的次数                         | InstanceId、CoreIp |
| HdfsNnFilesOpsDeletefileops                                  | 文件操作 _DeleteFileOps                                      | 次/s     | 每秒执行 DeleteFile 操作的次数                       | InstanceId、CoreIp |
| HdfsNnFilesOpsFileinfoops                                    | 文件操作 _FileInfoOps                                        | 次/s     | 每秒执行 FileInfo 操作的次数                         | InstanceId、CoreIp |
| HdfsNnFilesOpsGetadditional<br>datanodeops                   | 文件操作<br/> _GetAdditionalDatanodeOps                      | 次/s     | 每秒执行 GetAdditionalDatanode 操作的次数            | InstanceId、CoreIp |
| HdfsNnFilesOpsCreatesymlinkops                               | 文件操作<br/> _CreateSymlinkOps                              | 次/s     | 每秒执行 CreateSymlink 操作的次数                    | InstanceId、CoreIp |
| HdfsNnFilesOpsGetlinktargetops                               | 文件操作<br/> _GetLinkTargetOps                              | 次/s     | 每秒执行 GetLinkTarget 操作的次数                    | InstanceId、CoreIp |
| HdfsNnFilesOpsFilesingetlistingops                           | 文件操作<br/> _FilesInGetListingOps                          | 次/s     | 每秒执行 FilesInGetListing 操作的次数                | InstanceId、CoreIp |
| HdfsNnTransactionOps<br>Transactionsnumops                   | 事务操作<br/> _TransactionsNumOps                            | 次/s     | 每秒处理 Journal transaction 操作的次数              | InstanceId、CoreIp |
| HdfsNnTransactionOps<br>Transactionsbatchedinsync            | 事务操作<br/> _TransactionsBatchedInSync                     | 次/s     | 每秒批量处理 Journal transaction 操作次数            | InstanceId、CoreIp |
| HdfsNnImageOpsGeteditnumops                                  | 镜像操作<br/> _GetEditNumOps                                 | 次/s     | 每秒执行 GetEditNumOps 的次数                        | InstanceId、CoreIp |
| HdfsNnImageOpsGetimagenumops                                 | 镜像操作<br/> _GetImageNumOps                                | 次/s     | 每秒执行 GetImageNumOps 的次数                       | InstanceId、CoreIp |
| HdfsNnImageOpsPutimagenumops                                 | 镜像操作<br/> _PutImageNumOps                                | 次/s     | 每秒执行 PutImageNumOps 的次数                       | InstanceId、CoreIp |
| HdfsNnSyncsOpsSyncsnumops                                    | SYN C操作 <br/>_SyncsNumOps                                  | 次/s     | 每秒处理 Journal syncs 操作的次数                    | InstanceId、CoreIp |
| HdfsNnBlocksOpsBlock<br>receivedanddeletedops                | 数据块操作<br/>_BlockOpsQueued                               | 次/s     | 每秒执行 BlockReceivedAndDeletedOps 的次数           | InstanceId、CoreIp |
| HdfsNnBlocksOpsBlockopsqueued                                | 数据块操作<br/> _BlockOpsQueued                              | 次/s     | 处理 DataNode Block 上报操作的延迟                   | InstanceId、CoreIp |
| HdfsNnCacheReportOps<br>Cachereportnumops                    | 缓存汇报<br/> _CacheReportNumOps                             | 次/s     | 每秒处理 CacheReport 操作的次数                      | InstanceId、CoreIp |
| HdfsNnBlockReportOps<br>Blockreportnumops                    | 数据块汇报<br/> _BlockReportNumOps                           | 次/s     | 每秒处理 DataNode Blcok 上报操作的次数               | InstanceId、CoreIp |
| HdfsNnSyncsRtSyncsavgtime                                    | SYNCS 操作延迟<br/> _SyncsAvgTime                            | ms       | 处理 Journal syncs 操作的平均延迟                    | InstanceId、CoreIp |
| HdfsNnCacheReportRt<br>Cachereportavgtime                    | Cache 汇报延迟<br/> _CacheReportAvgTime                      | ms       | 缓存上报动作平均延迟                                 | InstanceId、CoreIp |
| HdfsNnImageRtGeteditavgtime                                  | 镜像操作延迟<br/> _GetEditAvgTime                            | ms       | 读取 Edit 文件操作平均延迟                           | InstanceId、CoreIp |
| HdfsNnImageRtGetimageavgtime                                 | 镜像操作延迟<br/> _GetImageAvgTime                           | ms       | 读取镜像文件平均延迟                                 | InstanceId、CoreIp |
| HdfsNnImageRtPutimageavgtime                                 | 镜像操作延迟<br/> _PutImageAvgTime                           | ms       | 写入镜像文件平均延迟                                 | InstanceId、CoreIp |
| HdfsNnTransactionRt<br>Transactionsavgtime                   | 事务操作延迟<br/> _TransactionsAvgTime                       | ms       | 处理 Journal transaction 操作的平均延迟              | InstanceId、CoreIp |
| HdfsNnStartTimeStarttime                                     | 启动时间<br/> _StartTime                                     | ms       | 进程启动时间                                         | InstanceId、CoreIp |
| HdfsNnStateState                                             | 主备情况 <br/>_State                                         | -        | NN 状态                                              | InstanceId、CoreIp |
| HdfsNnThreadCountPeakthreadcount                             | 线程数量<br/> _PeakThreadCount                               | 个       | 峰值线程数                                           | InstanceId、CoreIp |
| HdfsNnThreadCountThreadcount                                 | 线程数量<br/> _ThreadCount                                   | 个       | 线程数量                                             | InstanceId、CoreIp |
| HdfsNnThreadCount<br>Daemonthreadcount                       | 线程数量<br/> _DaemonThreadCount                             | 个       | 后台线程数量                                         | InstanceId、CoreIp |

### HDFS-DataNode

| 指标英文名                                                   | 指标中文名                                                | 指标单位 | 指标含义                                   | 维度               |
| ------------------------------------------------------------ | --------------------------------------------------------- | -------- | ------------------------------------------ | ------------------ |
| HdfsDnXceiverXceivercount                                    | XCEIVER 数量 _XceiverCount                                | 个       | Xceiver 数量                               | InstanceId、CoreIp |
| HdfsDnBytesByteswrittenmb                                    | 数据读写速率 _BytesReadMB                                 | Bytes/s  | 写入 DN 的字节速率                         | InstanceId、CoreIp |
| HdfsDnBytesBytesreadmb                                       | 数据读写速率 _BytesReadMB                                 | Bytes/s  | 读取 DN 的字节速率                         | InstanceId、CoreIp |
| HdfsDnBytesRemotebytesreadmb                                 | 数据读写速率 _RemoteBytesReadMB                           | Bytes/s  | 远程客户端读取字节速率                     | InstanceId、CoreIp |
| HdfsDnBytesRemoteby<br>teswrittenmb                          | 数据读写速率 _RemoteBytesWrittenMB                        | Bytes/s  | 远程客户端写入字节速率                     | InstanceId、CoreIp |
| HdfsDnClientWritesfrom<br>remoteclient                       | 客户端连接数 _WritesFromRemoteClient                      | 个       | 来自远程客户端写操作 QPS                   | InstanceId、CoreIp |
| HdfsDnClientWritesfromlocalclient                            | 客户端连接数 _WritesFromLocalClient                       | 个       | 来自本地客户端写操作 OPS                   | InstanceId、CoreIp |
| HdfsDnClientReadsfrom<br>remoteclient                        | 客户端连接数 _ReadsFromRemoteClient                       | 个       | 来自远程客户端读操作 QPS                   | InstanceId、CoreIp |
| HdfsDnClientReadsfromlocalclient                             | 客户端连接数 _ReadsFromLocalClient                        | 个       | 来自本地客户端读操作 QPS                   | InstanceId、CoreIp |
| HdfsDnBlocksVerifiedFailures<br>Blockverificationfailures    | Block 校验失败 _BlockVerificationFailures                 | 次/s     | BLOCK 校验失败数量                         | InstanceId、CoreIp |
| HdfsDnVolumeFailures<br>Volumefailures                       | 磁盘故障 _VolumeFailures                                  | 次/s     | 磁盘故障次数                               | InstanceId、CoreIp |
| HdfsDnNetworkErrors<br>Datanodenetworkerrors                 | 网络错误 _DatanodeNetworkErrors                           | 次/s     | 网络错误统计                               | InstanceId、CoreIp |
| HdfsDnHbRtHeartbeatsavgtime                                  | 心跳延迟 _HeartbeatsAvgTime                               | ms       | 心跳接口平均时间                           | InstanceId、CoreIp |
| HdfsDnHbOpsHeartbeatsnumops                                  | 心跳 QPS_HeartbeatsNumOps                                 | 次/s     | 心跳接口 QPS                               | InstanceId、CoreIp |
| HdfsDnDatapacketAvgtimeSend<br>datapackettransfernanosavgtime | 包传输操作QPS_SendDataPacketTransferNanosAvgTime          | ms       | 发送数据包平均时间                         | InstanceId、CoreIp |
| HdfsDnBlocksOpsRead<br>blockopnumops                         | 数据块操作 _ReadBlockOpNumOps                             | 次/s     | 从 DataNode 读取 Block OPS                 | InstanceId、CoreIp |
| HdfsDnBlocksOpsWrite<br>blockopnumops                        | 数据块操作 _WriteBlockOpNumOps                            | 次/s     | 向 DataNode 写入 Block OPS                 | InstanceId、CoreIp |
| HdfsDnBlocksOpsBlock<br>checksumopnumops                     | 数据块操作 _BlockChecksumOpNumOps                         | 次/s     | DataNode 进行 Checksum 操作的 OPS          | InstanceId、CoreIp |
| HdfsDnBlocksOpsCopy<br>blockopnumops                         | 数据块操作 _CopyBlockOpNumOps                             | 次/s     | 复制 Block 操作的 OPS                      | InstanceId、CoreIp |
| HdfsDnBlocksOpsReplace<br>blockopnumops                      | 数据块操作 _ReplaceBlockOpNumOps                          | 次/s     | Replace Block 操作的 OPS                   | InstanceId、CoreIp |
| HdfsDnBlocksOpsBlock<br>reportsnumops                        | 数据块操作 _BlockReportsNumOps                            | 次/s     | BLOCK 汇报动作的 OPS                       | InstanceId、CoreIp |
| HdfsDnBlocksOpsIncremental<br>blockreportsnumops             | 数据块操作 _IncrementalBlockReportsNumOps                 | 次/s     | BLOCK 增量汇报的 OPS                       | InstanceId、CoreIp |
| HdfsDnBlocksOpsCache<br>reportsnumops                        | 数据块操作 _CacheReportsNumOps                            | 次/s     | 缓存汇报的 OPS                             | InstanceId、CoreIp |
| HdfsDnBlocksOpsPacketack<br>roundtriptimenanosnumops         | 数据块操作_PacketAckRoundTripTimeNanosNumOps              | 次/s     | 每秒处理 ACK ROUND TRIP 次数               | InstanceId、CoreIp |
| HdfsDnFsyncOpsFsync<br>nanosnumops                           | FSYNC操作 _FsyncNanosNumOps                               | 次/s     | FSYNC 次数                                 | InstanceId、CoreIp |
| HdfsDnFlushOpsFlush<br>nanosnumops                           | FLUSH操作 _FlushNanosNumOps                               | 次/s     | 每秒处理 Flush 操作次数                    | InstanceId、CoreIp |
| HdfsDnBlocksRtRead<br>blockopavgtime                         | 数据块操作延迟统计 _ReadBlockOpAvgTime                    | ms       | 读取 Block 操作平均时间                    | InstanceId、CoreIp |
| HdfsDnBlocksRtWrite<br>blockopavgtime                        | 数据块操作延迟统计 _ReplaceBlockOpAvgTime                 | ms       | 写 Blcok 操作平均时间                      | InstanceId、CoreIp |
| HdfsDnBlocksRtBlock<br>checksumopavgtime                     | 数据块操作延迟统计 _BlockChecksumOpAvgTime                | ms       | 块校验操作平均时间                         | InstanceId、CoreIp |
| HdfsDnBlocksRtCopy<br>blockopavgtime                         | 数据块操作延迟统计 _CopyBlockOpAvgTime                    | ms       | 复制块操作平均时间                         | InstanceId、CoreIp |
| HdfsDnBlocksRt<br>Replaceblockopavgtime                      | 数据块操作延迟统计_Replaceblockopavgtime                  | ms       | Replace Block 操作平均时间                 | InstanceId、CoreIp |
| HdfsDnBlocksRtBlock<br>reportsavgtime                        | 数据块操作延迟统计 _BlockReportsAvgTime                   | ms       | 块汇报平均时间                             | InstanceId、CoreIp |
| HdfsDnBlocksRtIncremental<br>blockreportsavgtime             | 数据块操作延迟统计_IncrementalBlockReportsAvgTime         | ms       | 增量块汇报平均时间                         | InstanceId、CoreIp |
| HdfsDnBlocksRtCache<br>reportsavgtime                        | 数据块操作延迟统计 _CacheReportsAvgTime                   | ms       | 缓存汇报平均时间                           | InstanceId、CoreIp |
| HdfsDnBlocksRtPacketack<br>roundtriptimenanosavgtime         | 数据块操作延迟统计_PacketAckRoundTripTimeNanosAvgTime     | ms       | 处理 ACK ROUND TRIP 平均时间               | InstanceId、CoreIp |
| HdfsDnFlushRtFlushnanosavgtime                               | FLUSH 延迟 _FlushNanosAvgTime                             | ms       | Flush 操作平均时间                         | InstanceId、CoreIp |
| HdfsDnFsyncRtFsyncnanosavgtime                               | FSYNC 延迟 _FsyncNanosAvgTime                             | ms       | Fsync 操作平均时间                         | InstanceId、CoreIp |
| HdfsDnRamBlocksOp<br>Ramdiskblockswrite                      | RAMDISKBlocks_RamDiskBlocksWrite                          | 块/s     | 写入内存的块的总数                         | InstanceId、CoreIp |
| HdfsDnRamBlocksOp<br>Ramdiskblockswritefallback              | RAMDISKBlocks_RamDiskBlocksWriteFallback                  | 块/s     | 写入内存但未成功的块总数（故障转移到磁盘） | InstanceId、CoreIp |
| HdfsDnRamBlocksOpRamdisk<br>blocksdeletedbeforelazypersisted | RAMDISKBlocks_RamDiskBlocks<br>DeletedBeforeLazyPersisted | 块/s     | 应用程序在被保存到磁盘之前被删除的块的总数 | InstanceId、CoreIp |
| HdfsDnRamBlocksOp<br>Ramdiskblocksreadhits                   | RAMDISKBlocks_RamDiskBlocksReadHits                       | 块/s     | 内存中的块被读取的总次数                   | InstanceId、CoreIp |
| HdfsDnRamBlocksOp<br>Ramdiskblocksevicted                    | RAMDISKBlocks_RamDiskBlocksEvicted                        | 块/s     | 内存中被清除的块总数                       | InstanceId、CoreIp |
| HdfsDnRamBlocksOpRamdisk<br>blocksevictedwithoutread         | RAMDISKBlocks_RamDiskBlocks<br>EvictedWithoutRead         | 块/s     | 从内存中取出的内存块总数                   | InstanceId、CoreIp |
| HdfsDnRamBlocksOp<br>Ramdiskblockslazypersisted              | RAMDISKBlocks_RamDisk<br>BlocksLazyPersisted              | 块/s     | 惰性写入器写入磁盘的总数                   | InstanceId、CoreIp |
| HdfsDnRamBlocksOp<br>Ramdiskbyteslazypersisted               | RAMDISKBlocks_RamDiskBytesLazyPersisted                   | Bytes/s  | 由懒惰写入器写入磁盘的总字节数             | InstanceId、CoreIp |
| HdfsDnRamBlocksBytes<br>Ramdiskbyteswrite                    | RAMDISK写入速度_RamDiskBytesWrite                         | Bytes/s  | 写入内存的总字节数                         | InstanceId、CoreIp |
| HdfsDnJvmMem<br>Memnonheapusedm                              | JVM内存_MemNonHeapUsedM                                   | MB       | JVM 当前已经使用的 NonHeapMemory 的大小    | InstanceId、CoreIp |
| HdfsDnJvmMem<br>Memnonheapcommittedm                         | JVM内存_MemNonHeapCommittedM                              | MB       | JVM 配置的 NonHeapCommittedM 的大小        | InstanceId、CoreIp |
| HdfsDnJvmMemMemheapusedm                                     | JVM内存_MemHeapUsedM                                      | MB       | JVM 当前已经使用的 HeapMemory 的大小       | InstanceId、CoreIp |
| HdfsDnJvmMem<br>Memheapcommittedm                            | JVM 内存 _MemHeapCommittedM                               | MB       | JVM HeapMemory 提交大小                    | InstanceId、CoreIp |
| HdfsDnJvmMemMemheapmaxm                                      | JVM 内存 _MemHeapMaxM                                     | MB       | JVM 配置的 HeapMemory 的大小               | InstanceId、CoreIp |
| HdfsDnJvmMemMemmaxm                                          | JVM内存 _MemMaxM                                          | MB       | JVM 运行时的可以使用的最大的内存的大小     | InstanceId、CoreIp |
| HdfsDnJvmJavaThreadsThreadsnew                               | JVM 线程数量_ThreadsNew                                   | 个       | 处于新建状态的线程数量                     | InstanceId、CoreIp |
| HdfsDnJvmJavaThreads<br>Threadsrunnable                      | JVM 线程数量 _ThreadsRunnable                             | 个       | 处于可运行状态的线程数量                   | InstanceId、CoreIp |
| HdfsDnJvmJavaThreads<br>Threadsblocked                       | JVM 线程数量 _ThreadsBlocked                              | 个       | 处于阻塞状态的线程数量                     | InstanceId、CoreIp |
| HdfsDnJvmJavaThreads<br>Threadswaiting                       | JVM 线程数量 _ThreadsWaiting                              | 个       | 处于 WAITING 状态的线程数量                | InstanceId、CoreIp |
| HdfsDnJvmJavaThreads<br>Threadstimedwaiting                  | JVM 线程数量 _ThreadsTimedWaiting                         | 个       | 处于 TIMED WAITING 状态的线程数量          | InstanceId、CoreIp |
| HdfsDnJvmJavaThreads<br>Threadsterminated                    | JVM 线程数量 _ThreadsTerminated                           | 个       | 处于 Terminated 状态的线程数量             | InstanceId、CoreIp |
| HdfsDnJvmLogTotalLogfatal                                    | JVM 日志数量 _LogFatal                                    | 个       | Fatal 日志数量                             | InstanceId、CoreIp |
| HdfsDnJvmLogTotalLogerror                                    | JVM 日志数量 _LogError                                    | 个       | Error 日志数量                             | InstanceId、CoreIp |
| HdfsDnJvmLogTotalLogwarn                                     | JVM 日志数量 _LogWarn                                     | 个       | Warn 日志数量                              | InstanceId、CoreIp |
| HdfsDnJvmLogTotalLoginfo                                     | JVM 日志数量 _LogInfo                                     | 个       | Info 日志数量                              | InstanceId、CoreIp |
| HdfsDnGcUtilMemoryS0                                         | 内存区域占比 _S0                                          | %        | Survivor 0区内存使用占比                   | InstanceId、CoreIp |
| HdfsDnGcUtilMemoryS1                                         | 内存区域占比 _S1                                          | %        | Survivor 1区内存使用占比                   | InstanceId、CoreIp |
| HdfsDnGcUtilMemoryE                                          | 内存区域占比 _E                                           | %        | Eden 区内存使用占比                        | InstanceId、CoreIp |
| HdfsDnGcUtilMemoryO                                          | 内存区域占比 _O                                           | %        | Old 区内存使用占比                         | InstanceId、CoreIp |
| HdfsDnGcUtilMemoryM                                          | 内存区域占比 _M                                           | %        | Metaspace 区内存使用占比                   | InstanceId、CoreIp |
| HdfsDnGcUtilMemoryCcs                                        | 内存区域占比 _CCS                                         | %        | Compressed class space 区内存使用占比      | InstanceId、CoreIp |
| HdfsDnGcUtilGcCountFgc                                       | GC 次数 _FGC                                              | 次       | Full GC 次数                               | InstanceId、CoreIp |
| HdfsDnGcUtilGcCountYgc                                       | GC 次数 _YGC                                              | 次       | Young GC 次数                              | InstanceId、CoreIp |
| HdfsDnGcUtilGcTimeYgct                                       | GC 时间 _YGCT                                             | s        | Young GC 消耗时间                          | InstanceId、CoreIp |
| HdfsDnGcUtilGcTimeFgct                                       | GC 时间 _FGCT                                             | s        | Full GC 消耗时间                           | InstanceId、CoreIp |
| HdfsDnGcUtilGcTimeGct                                        | GC 时间 _GCT                                              | s        | 垃圾回收时间消耗                           | InstanceId、CoreIp |
| HdfsDnPort4004RxtxReceivedbytes                              | 数据流量 _ReceivedBytes                                   | Bytes/s  | 接收数据速率                               | InstanceId、CoreIp |
| HdfsDnPort4004RxtxSentbytes                                  | 数据流量 _SentBytes                                       | Bytes/s  | 发送数据速率                               | InstanceId、CoreIp |
| HdfsDnPort4004QpsRpc<br>queuetimenumops                      | QPS_RpcQueueTimeNumOps                                    | 次/s     | RPC 调用速率                               | InstanceId、CoreIp |
| HdfsDnPort4004RtRpc<br>queuetimeavgtime                      | 请求处理延迟 _RpcQueueTimeAvgTime                         | ms       | RPC 平均延迟时间                           | InstanceId、CoreIp |
| HdfsDnPort4004AuthRpc<br>authenticationfailures              | 验证和授权 _RpcAuthenticationFailures                     | 次/s     | RPC 验证失败次数                           | InstanceId、CoreIp |
| HdfsDnPort4004AuthRpc<br>authenticationsuccesses             | 验证和授权 _RpcAuthenticationSuccesses                    | 次/s     | RPC 验证成功次数                           | InstanceId、CoreIp |
| HdfsDnPort4004AuthRpc<br>authorizationfailures               | 验证和授权 _RpcAuthorizationFailures                      | 次/s     | RPC 授权失败次数                           | InstanceId、CoreIp |
| HdfsDnPort4004AuthRpc<br>authorizationsuccesses              | 验证和授权 _RpcAuthorizationSuccesses                     | 次/s     | RPC 授权成功次数                           | InstanceId、CoreIp |
| HdfsDnPort4004Connections<br>Numopenconnections              | 当前连接数 _NumOpenConnections                            | 个       | 当前链接数量                               | InstanceId、CoreIp |
| HdfsDnPort4004QueueLen<br>Callqueuelength                    | RPC 处理队列长度 _CallQueueLength                         | 个       | 当前 RPC 处理队列长度                      | InstanceId、CoreIp |
| HdfsDnThreadTimeCurrent<br>threadcputime                     | CPU 时间 _CurrentThreadCpuTime                            | ms       | CPU时间                                    | InstanceId、CoreIp |
| HdfsDnThreadTimeCurrent<br>threadusertime                    | CPU 时间 _CurrentThreadUserTime                           | ms       | 用户时间                                   | InstanceId、CoreIp |
| HdfsDnStartTimeStarttime                                     | 线程数量 _DaemonThreadCount                               | s        | 进程启动时间                               | InstanceId、CoreIp |
| HdfsDnThreadCount<br>Peakthreadcount                         | 程数量 _PeakThreadCount                                   | 个       | 峰值线程数量                               | InstanceId、CoreIp |
| HdfsDnThreadCount<br>Daemonthreadcount                       | 线程数量 _DaemonThreadCount                               | 个       | 后台线程数量                               | InstanceId、CoreIp |
| HdfsDnRtWrit                                                 | 读写延迟 _Write                                           | MB/s     | 磁盘写速率                                 | InstanceId、CoreIp |
| HdfsDnRtRead                                                 | 读写延迟 _Read                                            | 次/s     | 读操作 QPS                                 | InstanceId、CoreIp |
| HdfsDnDatapacketOps<br>Datapacketops                         | 包传输操作 QPS_DataPacketOps                              | 次/s     | 包传输操作 QPS                             | InstanceId、CoreIp |

### HDFS-Journal Node 

| 指标英文名                                       | 指标中文名                             | 指标单位 | 指标含义                                |                    |
| ------------------------------------------------ | -------------------------------------- | -------- | --------------------------------------- | ------------------ |
| HdfsJnJvmMemMemnon<br>heapusedm                  | JVM 内存 _MemNonHeapUsedM              | MB       | JVM 当前已经使用的 NonHeapMemory 的大小 | InstanceId、CoreIp |
| HdfsJnJvmMemMemnon<br>heapcommittedm             | JVM 内存 _MemNonHeapCommittedM         | MB       | JVM 内存                                | InstanceId、CoreIp |
| HdfsJnJvmMemMem<br>heapusedm                     | JVM 内存 _MemHeapUsedM                 | MB       | JVM 当前已经使用的 HeapMemory 的大小    | InstanceId、CoreIp |
| HdfsJnJvmMemMem<br>heapcommittedm                | JVM 内存 _MemHeapCommittedM            | MB       | JVM HeapMemory 提交大小                 | InstanceId、CoreIp |
| HdfsJnJvmMemMem<br>heapmaxm                      | JVM 内存 _MemHeapMaxM                  | MB       | JVM 配置的 HeapMemory 的大小            | InstanceId、CoreIp |
| HdfsJnJvmMemMemmaxm                              | JVM 内存_MemMaxM                       | MB       | JVM 运行时的可以使用的最大的内存的大小  | InstanceId、CoreIp |
| HdfsJnJvmJavaThreads<br>Threadsnew               | JVM 线程数量 _ThreadsNew               | 个       | 处于新建状态的线程数量                  | InstanceId、CoreIp |
| HdfsJnJvmJavaThreads<br>Threadsrunnable          | JVM 线程数量 _ThreadsRunnable          | 个       | 处于可运行状态的线程数量                | InstanceId、CoreIp |
| HdfsJnJvmJavaThreads<br>Threadsblocked           | JVM 线程数量 _ThreadsBlocked           | 个       | 处于阻塞状态的线程数量                  | InstanceId、CoreIp |
| HdfsJnJvmJavaThreads<br>Threadswaiti             | JVM 线程数量 _ThreadsWaiting           | 个       | 处于 WAITING 状态的线程数量             | InstanceId、CoreIp |
| HdfsJnJvmJavaThreads<br>Threadstimedwaiting      | JVM 线程数量 _ThreadsTimedWaiting      | 个       | 处于 TIMED WAITING 状态的线程数量       | InstanceId、CoreIp |
| HdfsJnJvmJavaThreads<br>Threadsterminated        | JVM 线程数量 _ThreadsTerminated        | 个       | 处于 Terminated 状态的线程数量          | InstanceId、CoreIp |
| HdfsJnJvmLogTotalLogfatal                        | JVM 日志数量 _LogFatal                 | 个       | Fatal 日志数量                          | InstanceId、CoreIp |
| HdfsJnJvmLogTotalLogerror                        | JVM 日志数量 _LogError                 | 个       | Error 日志数量                          | InstanceId、CoreIp |
| HdfsJnJvmLogTotalLogwarn                         | JVM 日志数量 _LogWarn                  | 个       | Warn 日志数量                           | InstanceId、CoreIp |
| HdfsJnJvmLogTotalLoginfo                         | JVM 日志数量 _LogInfo                  | 个       | Info 日志数量                           | InstanceId、CoreIp |
| HdfsJnGcUtilMemoryS0                             | 内存区域占比 _S0                       | %        | Survivor 0区内存使用占比                | InstanceId、CoreIp |
| HdfsJnGcUtilMemoryS1                             | 内存区域占比 _S1                       | %        | Survivor 1区内存使用占比                | InstanceId、CoreIp |
| HdfsJnGcUtilMemoryE                              | 内存区域占比 _E                        | %        | Eden 区内存使用占比                     | InstanceId、CoreIp |
| HdfsJnGcUtilMemoryO                              | 内存区域占比 _O                        | %        | Old 区内存使用占比                      | InstanceId、CoreIp |
| HdfsJnGcUtilMemoryM                              | 内存区域占比 _M                        | %        | Metaspace 区内存使用占比                | InstanceId、CoreIp |
| HdfsJnGcUtilMemoryCcs                            | 内存区域占比 _CCS                      | %        | Compressed class space 区内存使用占比   | InstanceId、CoreIp |
| HdfsJnGcUtilGcCountFgc                           | GC 次数 _FGC                           | 次       | Full GC 次数                            | InstanceId、CoreIp |
| HdfsJnGcUtilGcCountYgc                           | GC 次数 _YGC                           | 次       | Young GC 次数                           | InstanceId、CoreIp |
| HdfsJnGcUtilGcTimeYgct                           | GC 时间 _YGCT                          | s        | Young GC 消耗时间                       | InstanceId、CoreIp |
| HdfsJnGcUtilGcTimeFgct                           | GC 时间  _FGCT                         | s        | Full GC 消耗时间                        | InstanceId、CoreIp |
| HdfsJnGcUtilGcTimeGct                            | GC 时间 _GC                            | s        | 垃圾回收时间消耗                        | InstanceId、CoreIp |
| HdfsJnPort4005Rxtx<br>Receivedbytes              | 数据流量 _ReceivedBytes                | Bytes/s  | 接收数据速率                            | InstanceId、CoreIp |
| HdfsJnPort4005Rxtx<br>Receivedbytes              | 数据流量 _ReceivedBytes                | Bytes/s  | 发送数据速率                            | InstanceId、CoreIp |
| HdfsJnPort4005QpsRpc<br>queuetimenumops          | QPS_RpcQueueTimeNumOps                 | 次/s     | RPC 调用速率                            | InstanceId、CoreIp |
| HdfsJnPort4005RtRpc<br>queuetimeavgtime          | 请求处理延迟 _RpcQueueTimeAvgTime      | ms       | RPC 平均延迟时间                        | InstanceId、CoreIp |
| HdfsJnPort4005AuthRpc<br>authenticationfailures  | 验证和授权 _RpcAuthenticationFailures  | 次/s     | RPC 验证失败次数                        | InstanceId、CoreIp |
| HdfsJnPort4005AuthRpc<br>authorizationsuccesses  | 验证和授权 _RpcAuthorizationSuccesses  | 次/s     | RPC 授权成功次数                        | InstanceId、CoreIp |
| HdfsJnPort4005AuthRpc<br>authenticationsuccesses | 验证和授权 _RpcAuthenticationSuccesses | 次/s     | RPC 验证成功次数                        | InstanceId、CoreIp |
| HdfsJnPort4005AuthRpc<br>authorizationfailures   | 验证和授权 _RpcAuthorizationFailures   | 次/s     | RPC 授权失败次数                        | InstanceId、CoreIp |
| HdfsJnPort4005Connections<br>Numopenconnections  | 当前连接数 _NumOpenConnections         | 个       | 当前链接数量                            | InstanceId、CoreIp |
| HdfsJnPort4005QueueLen<br>Callqueuelength        | RPC 处理队列长度 _CallQueueLength      | 个       | 当前 RPC 处理队列长度                   | InstanceId、CoreIp |
| HdfsJnThreadTimeCurrent<br>threadcputime         | CPU 时间 _CurrentThreadCpuTime         | ms       | CPU时间                                 | InstanceId、CoreIp |
| HdfsJnThreadTimeCurrent<br>threadusertime        | CPU 时间 _CurrentThreadUserTime        | ms       | 用户时间                                | InstanceId、CoreIp |
| HdfsJnStartTimeStarttime                         | 启动时间 _StartTime                    | s        | 进程启动时间                            | InstanceId、CoreIp |
| HdfsJnThreadCount<br>Threadcount                 | 线程数量 _ThreadCount                  | 个       | 线程数量                                | InstanceId、CoreIp |
| HdfsJnThreadCount<br>Peakthreadcount             | 线程数量 _PeakThreadCount              | 个       | 峰值线程数量                            | InstanceId、CoreIp |
| HdfsJnThreadCountDaemon<br>threadcount           | 线程数量 _DaemonThreadCount            | 个       | 后台线程数量                            | InstanceId、CoreIp |

### HDFS-ZKFC

| 指标英文名               | 指标中文名       | 指标单位 | 指标含义                              | 维度               |
| ------------------------ | ---------------- | -------- | ------------------------------------- | ------------------ |
| HdfsDfzkGcUtilMemoryS0   | 内存区域占比_S0  | %        | Survivor 0区内存使用占比              | InstanceId、CoreIp |
| HdfsDfzkGcUtilMemoryS1   | 内存区域占比_S1  | %        | Survivor 1区内存使用占比              | InstanceId、CoreIp |
| HdfsDfzkGcUtilMemoryE    | 内存区域占比_E   | %        | Eden 区内存使用占比                   | InstanceId、CoreIp |
| HdfsDfzkGcUtilMemoryO    | 内存区域占比_O   | %        | Old 区内存使用占比                    | InstanceId、CoreIp |
| HdfsDfzkGcUtilMemoryM    | 内存区域占比_M   | %        | Metaspace 区内存使用占比              | InstanceId、CoreIp |
| HdfsDfzkGcUtilMemoryCcs  | 内存区域占比_CCS | %        | Compressed class space 区内存使用占比 | InstanceId、CoreIp |
| HdfsDfzkGcUtilGcCountFgc | GC次数_FGC       | 次       | Full GC 次数                          | InstanceId、CoreIp |
| HdfsDfzkGcUtilGcCountYgc | GC次数_YGC       | 次       | Young GC 次数                         | InstanceId、CoreIp |
| HdfsDfzkGcUtilGcTimeYgct | GC时间_YGCT      | s        | Young GC 消耗时间                     | InstanceId、CoreIp |
| HdfsDfzkGcUtilGcTimeFgct | GC时间_FGCT      | s        | Full GC 消耗时间                      | InstanceId、CoreIp |
| HdfsDfzkGcUtilGcTimeGct  | GC时间_GCT       | s        | 垃圾回收时间消耗                      | InstanceId、CoreIp |

## 各维度对应参数总览

| 参数名称                       | 维度名称   | 维度解释              | 格式                                          |
| ------------------------------ | ---------- | --------------------- | --------------------------------------------- |
| Instances.N.Dimensions.0.Name  | InstanceId | EMR 实例 ID           | 输入String 类型维度名称，例如 id4hdfsdatanode |
| Instances.N.Dimensions.0.Value | InstanceId | EMR 实例 ID           | 输入EMR具体实例 ID，例如 ins-mm8bs222         |
| Instances.N.Dimensions.1.Name  | CoreIp     | EMR 实例中具体节点 IP | 输入String 类型维度名称，例如 InstanceId      |
| Instances.N.Dimensions.1.Value | CoreIp     | EMR 实例中具体节点 IP | 输入具体节点IP ，例如 host4hdfsdatanode       |


## 入参说明
查询 弹性 MapReduce（HDFS）监控数据，入参取值如下：
&Namespace=QCE/TXMR_HDFS 
&Instances.N.Dimensions.0.Name=id4hdfsdatanode
&Instances.N.Dimensions.0.Value=EMR 实例具体 ID
&Instances.N.Dimensions.1.Name=host4hdfsdatanode
&Instances.N.Dimensions.1.Value EMR 实例中具体节点 IP 

