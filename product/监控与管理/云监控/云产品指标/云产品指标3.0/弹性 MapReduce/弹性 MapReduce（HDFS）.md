## 命名空间

Namespace=QCE/TXMR_HDFS


## 监控指标

弹性 MapReduce（HDFS）提供 [HDFS-Overview](#hdfs-overview)、[HDFS-OverviewAggregation](#hdfs-overviewaggregation)、[HDFS-NameNode](#hdfs-namenode)、[HDFS-DataNode](#hdfs-datanode)、[HDFS-Journal Node](#hdfs-journal-node) 和 [HDFS-ZKFC](#hdfs-zkfc) 指标。

>?维度对应参数，请单击 [各维度对应参数总览](#.E5.90.84.E7.BB.B4.E5.BA.A6.E5.AF.B9.E5.BA.94.E5.8F.82.E6.95.B0.E6.80.BB.E8.A7.88) 查看。

### HDFS-Overview

| 指标英文名                                                   | 指标中文名                               | 单位 | 指标含义                                      | 维度                                    |
| ------------------------------------------------------------ | ---------------------------------------- | ---- | --------------------------------------------- | --------------------------------------- |
| EmrHdfsOverviewHdfsNn<br>CapacityCapacitytotal               | 集群存储容量_CapacityTotal               | GB   | 集群存储总容量                                | id4hdfsoverview |
| EmrHdfsOverviewHdfsNn<br/>CapacityCapacityused               | 集群存储容量_CapacityUsed                | GB   | 集群储存已使用容量                            | id4hdfsoverview |
| EmrHdfsOverviewHdfsNn<br/>CapacityCapacityremaining          | 集群存储容量_CapacityRemaining           | GB   | 集群存储剩余容量                              | id4hdfsoverview |
| EmrHdfsOverviewHdfsNn<br/>CapacityCapacityusednondfs         | 集群存储容量_CapacityUsedNonDFS          | GB   | 集群非 HDFS 使用容量                          | id4hdfsoverview |
| EmrHdfsOverview<br/>HdfsNnLoadTotalload                      | 集群负载_TotalLoad                       | 个   | 当前连接数                                    | id4hdfsoverview |
| EmrHdfsOverview<br/>HdfsNnFilesTotalFilestotal               | 群文件总数量_FilesTotal                  | 个   | 总文件数量                                    | id4hdfsoverview |
| EmrHdfsOverviewHdfsNn<br/>BlocksBlockstotal                  | BLOCKS 数量_BlocksTotal                  | 个   | 总 BLOCK 数量                                 | id4hdfsoverview |
| EmrHdfsOverviewHdfsNn<br/>BlocksPending<br>replicationblocks     | BLOCKS 数量_PendingReplicationBlocks     | 个   | 等待被备份的块数量                            | id4hdfsoverview |
| EmrHdfsOverviewHdfs<br/>NnBlocksUnderre<br>plicatedblocks        | BLOCKS 数量_UnderReplicatedBlocks        | 个   | 副本数不够的块数量                            | id4hdfsoverview |
| EmrHdfsOverviewHdfsNn<br/>BlocksCorruptblocks                | BLOCKS 数量_CorruptBlocks                | 个   | 坏块数量                                      | id4hdfsoverview |
| EmrHdfsOverviewHdfsNn<br/>BlocksScheduledreplicationblocks   | BLOCKS 数量_ScheduledReplicationBlocks   | 个   | 安排要备份的块数量                            | id4hdfsoverview |
| EmrHdfsOverviewHdfsNn<br/>BlocksPendingdeletionblocks        | BLOCKS 数量_PendingDeletionBlocks        | 个   | 等待被删除的块数量                            | id4hdfsoverview |
| EmrHdfsOverviewHdfs<br/>NnBlocksCorruptblocks                | BLOCKS 数量_CorruptBlocks                | 个   | 多于的块数量                                  | id4hdfsoverview |
| EmrHdfsOverviewHdfs<br/>NnBlocksPostponedmisre<br/>plicatedblocks | BLOCKS 数量_PostponedMisreplicatedBlocks | 个   | 被推迟处理的异常块数量                        | id4hdfsoverview |
| EmrHdfsOverviewHdfsNnBlock<br/>CapacityBlockcapacity         | BLOCK容量_BlockCapacity                  | 个   | BLOCK 容量                                    | id4hdfsoverview |
| EmrHdfsOverviewHdfsNn<br/>DatanodesCountNum<br/>livedatanodes | 集群数据节点_NumLiveDataNodes            | 个   | 个活的数据节点数量                            | id4hdfsoverview |
| EmrHdfsOverviewHdfsNn<br/>DatanodesCountNum<br/>deaddatanodes | 集群数据节点_NumDeadDataNodes            | 个   | 已经标记为 Dead 状态的数据节点数量            | id4hdfsoverview |
| EmrHdfsOverviewHdfsNn<br/>DatanodesCountNumdecom<br/>livedatanodes | 集群数据节点_NumDecomLiveDataNodes       | 个   | 下线且 Live 的节点数量                        | id4hdfsoverview |
| EmrHdfsOverviewHdfsNn<br/>DatanodesCountNumde<br/>comdeaddatanodes | 集群数据节点_NumDecomDeadDataNodes       | 个   | 下线且 Dead 的节点数量                        | id4hdfsoverview |
| EmrHdfsOverviewHdfs<br/>NnDatanodesCountNumde<br/>commissioningdatanodes | 集群数据节点_NumDecommissioningDataNodes | 个   | 正在下线的节点数量                            | id4hdfsoverview |
| EmrHdfsOverviewHdfs<br/>NnDatanodesCountNumstale<br/>datanodes | 集群数据节点_NumStaleDataNodes           | 个   | 由于心跳延迟而标记为过期的 DataNodes 当前数量 | id4hdfsoverview |
| EmrHdfsOverviewHdfsNn<br/>SnapshotsSnapshots                 | SNAPSHOT 相关_Snapshots                  | 个   | Snapshots 数量                                | id4hdfsoverview |
| EmrHdfsOverviewHdfs<br/>NnVolumeFailures<br/>Volumefailurestotal | 磁盘故障_VolumeFailuresTotal             | 次   | 所有 Datanodes 的全故障总数                   | id4hdfsoverview |
|HdfsStatUsageRatio<br>Capacityusedrate | 	HDFS存储空间使用率         |%  | HDFS存储空间使用率              | id4hdfsoverview |

## HDFS-OverviewAggregation

| 指标英文名                                                   | 指标中文名                               | 单位 | 指标含义                                      | 维度            |
| ------------------------------------------------------------ | ---------------------------------------- | ---- | --------------------------------------------- | --------------- |
| EmrHdfsOverview<br>Aggregation<br>HdfsNnBlockCapacityTotal   | 集群存储容量_CapacityTotal               | GB   | 集群存储总容量                                | id4hdfsoverview |
| EmrHdfsOverview<br>Aggregation<br/>HdfsNnBlockCapacityUsed   | 集群存储容量_CapacityUsed                | GB   | 集群储存已使用容量                            | id4hdfsoverview |
| EmrHdfsOverview<br>AggregationHdfsNn<br>BlockCapacityRemaining | 集群存储容量_CapacityRemaining           | GB   | 集群存储剩余容量                              | id4hdfsoverview |
| EmrHdfsOverview<br>AggregationHdfsNn<br>BlockCapacity UsedNonDFS | 集群存储容量_CapacityUsedNonDFS          | GB   | 集群非 HDFS 使用容量                          | id4hdfsoverview |
| EmrHdfsOverview<br>AggregationHdfsNn<br>BlockTotalLoad       | 集群负载_TotalLoad                       | 个   | 当前连接数                                    | id4hdfsoverview |
| EmrHdfsOverview<br>AggregationHdfsNn<br>BlockFilesTotal      | 群文件总数量_FilesTotal                  | 个   | 总文件数量                                    | id4hdfsoverview |
| EmrHdfsOverview<br>AggregationHdfsNn<br>BlockBlockstotal     | BLOCKS 数量_BlocksTotal                  | 个   | 总 BLOCK 数量                                 | id4hdfsoverview |
| EmrHdfsOverview<br>AggregationHdfsNn<br>BlockPending ReplicationBlocks | BLOCKS 数量_PendingReplicationBlocks     | 个   | 等待被备份的块数量                            | id4hdfsoverview |
| EmrHdfsOverview<br/>AggregationHdfsNn<br>BlockUnder ReplicatedBlocks | BLOCKS 数量_UnderReplicatedBlocks        | 个   | 副本数不够的块数量                            | id4hdfsoverview |
| EmrHdfsOverview<br/>AggregationHdfsNn<br>BlockBlocksCorruptblocks | BLOCKS 数量_CorruptBlocks                | 个   | 坏块数量                                      | id4hdfsoverview |
| EmrHdfsOverview<br/>AggregationHdfsNn<br/>BlockScheduled ReplicationBlocks | BLOCKS 数量_ScheduledReplicationBlocks   | 个   | 安排要备份的块数量                            | id4hdfsoverview |
| EmrHdfsOverview<br/>AggregationHdfsNn<br/>BlockPending DeletionBlocks | BLOCKS 数量_PendingDeletionBlocks        | 个   | 等待被删除的块数量                            | id4hdfsoverview |
| EmrHdfsOverview<br/>AggregationHdfsNn<br/>BlockCorruptblocks | BLOCKS 数量_CorruptBlocks                | 个   | 多于的块数量                                  | id4hdfsoverview |
| EmrHdfsOverview<br/>AggregationHdfsNn<br/>BlockPostponed MisreplicatedBlocks | BLOCKS 数量_PostponedMisreplicatedBlocks | 个   | 被推迟处理的异常块数量                        | id4hdfsoverview |
| EmrHdfsOverview<br/>AggregationHdfsNn<br/>BlockBlockCapacity | BLOCK容量_BlockCapacity                  | 个   | BLOCK 容量                                    | id4hdfsoverview |
| EmrHdfsOverview<br/>AggregationHdfsNn<br/>BlockNumLiveDataNodes | 集群数据节点_NumLiveDataNodes            | 个   | 个活的数据节点数量                            | id4hdfsoverview |
| EmrHdfsOverview<br/>AggregationHdfsNn<br/>BlockNumDeadDataNodes | 集群数据节点_NumDeadDataNodes            | 个   | 已经标记为 Dead 状态的数据节点数量            | id4hdfsoverview |
| EmrHdfsOverview<br/>AggregationHdfsNn<br/>BlockNum DecomLiveDataNodes | 集群数据节点_NumDecomLiveDataNodes       | 个   | 下线且 Live 的节点数量                        | id4hdfsoverview |
| EmrHdfsOverview<br/>AggregationHdfsNn<br/>BlockNum DecomDeadDataNodes | 集群数据节点_NumDecomDeadDataNodes       | 个   | 下线且 Dead 的节点数量                        | id4hdfsoverview |
| EmrHdfsOverview<br/>AggregationHdfsNn<br/>BlockNum DecommissioningDataNodes | 集群数据节点_NumDecommissioningDataNodes | 个   | 正在下线的节点数量                            | id4hdfsoverview |
| EmrHdfsOverview<br/>AggregationHdfsNn<br/>BlockNum StaleDataNodes | 集群数据节点_NumStaleDataNodes           | 个   | 由于心跳延迟而标记为过期的 DataNodes 当前数量 | id4hdfsoverview |
| EmrHdfsOverview<br/>AggregationHdfsNn<br/>BlockSnapshots     | SNAPSHOT 相关_Snapshots                  | 个   | Snapshots 数量                                | id4hdfsoverview |
| EmrHdfsOverview<br/>AggregationHdfsNn<br/>BlockVolumeFailuresTotal | 磁盘故障_VolumeFailuresTotal             | 次   | 所有 Datanodes 的全故障总数                   | id4hdfsoverview |

### HDFS-NameNode

| 指标英文名                                                   | 指标中文名                                                   | 指标单位 | 指标含义                                             | 维度                                    |
| ------------------------------------------------------------ | ------------------------------------------------------------ | -------- | ---------------------------------------------------- | --------------------------------------- |
| HdfsNnPort4007RxtxReceivedbytes                              | 数据流量_ReceivedBytes                                       | Bytes/s  | 接收数据速率                                         | host4hdfsnamenode、<br>id4hdfsnamenode  |
| HdfsNnPort4007RxtxSentbytes                                  | 数据流量_SentBytes                                           | Bytes/s  | 发送数据速率                                         | host4hdfsnamenode、<br> id4hdfsnamenode |
| HdfsNnPort4007Qps<br>Rpcqueuetimenumops                      | QPS_RpcQueueTimeNumOps                                       | 次/s     | RPC 调用速率                                         | host4hdfsnamenode、<br> id4hdfsnamenode |
| HdfsNnPort4007RtRpc<br>queuetimeavgtime                      | 请求处理延迟<br>_RpcQueueTimeAvgTime                         | ms       | RPC 平均延迟时间                                     | host4hdfsnamenode、<br> id4hdfsnamenode |
| HdfsNnPort4007AuthRpc<br>authenticationfailures              | 验证和授权<br>_RpcAuthenticationFailure                      | 次       | RPC 验证失败次数                                     | host4hdfsnamenode、<br> id4hdfsnamenode |
| HdfsNnPort4007AuthRpc<br>authenticationsuccesses             | 验证和授权<br>_RpcAuthenticationSuccesses                    | 次       | RPC 验证成功次数                                     | host4hdfsnamenode、<br> id4hdfsnamenode |
| HdfsNnPort4007AuthRpc<br>authorizationfailures               | 验证和授权<br>_RpcAuthorizationFailures                      | 次       | RPC 授权失败次数                                     | host4hdfsnamenode、<br> id4hdfsnamenode |
| HdfsNnPort4007AuthRpc<br>authorizationsuccesses              | 验证和授权<br>_RpcAuthorizationSuccesses                     | 次       | RPC 授权成功次数                                     | host4hdfsnamenode、<br> id4hdfsnamenode |
| HdfsNnPort4007Connections<br>Numopenconnections              | 当前连接数<br>_NumOpenConnections                            | 个       | 当前链接数量                                         | host4hdfsnamenode、<br> id4hdfsnamenode |
| HdfsNnPort4007Queue<br>LenCallqueuelength                    | RPC 处理队列长度<br>_CallQueueLength                         | 个       | 当前 RPC 处理队列长度                                | host4hdfsnamenode、<br> id4hdfsnamenode |
| HdfsNnJvmMemMemnonheapusedm                                  | JVM 内存<br>_MemNonHeapUsedM                                 | MB       | JVM 当前已经使用的 NonHeapMemory 的大小              | host4hdfsnamenode、<br> id4hdfsnamenode |
| HdfsNnJvmMemMemnon<br>heapcommittedm                         | JVM 内存<br>_MemNonHeapCommittedM                            | MB       | JVM 内存                                             | host4hdfsnamenode、<br> id4hdfsnamenode |
| HdfsNnJvmMemMemheapusedm                                     | JVM 内存<br>_MemHeapUsedM                                    | MB       | JVM 当前已经使用的 HeapMemory 的大小                 | host4hdfsnamenode、<br> id4hdfsnamenode |
| HdfsNnJvmMem<br>Memheapcommittedm                            | JVM 内存<br>_MemHeapCommittedM                               | MB       | JVM HeapMemory 提交大小                              | host4hdfsnamenode、<br> id4hdfsnamenode |
| HdfsNnJvmMemMemheapmaxm                                      | JVM 内存_MemHeapMaxM                                         | MB       | JVM 配置的 HeapMemory 的大小                         | host4hdfsnamenode、<br> id4hdfsnamenode |
| HdfsNnJvmMemMemmaxm                                          | JVM 内存_MemMaxM                                             | MB       | JVM 运行时的可以使用的最大的内存的大小               | host4hdfsnamenode、<br> id4hdfsnamenode |
| HdfsNnBlockReportRt<br>Blockreportavgtime                    | 数据块汇报延迟<br>_BlockReportAvgTime                        | 次/s     | 每秒处理 DataNode Blcok 平均延迟                     | host4hdfsnamenode、<br> id4hdfsnamenode |
| HdfsNnGcUtilGcCountFgc                                       | GC 次数_FGC                                                  | 次/s     | Full GC 次数                                         | host4hdfsnamenode、<br> id4hdfsnamenode |
| HdfsNnGcUtilGcCountYgc                                       | C 次数_YGC                                                   | 2次/s    | Young GC 次数                                        | host4hdfsnamenode、<br>id4hdfsnamenode  |
| HdfsNnGcUtilGcTimeYgct                                       | GC 时间_YGCT                                                 | ms       | Young GC 消耗时间                                    | host4hdfsnamenode、<br>id4hdfsnamenode  |
| HdfsNnGcUtilGcTimeFgct                                       | GC 时间_FGCT                                                 | ms       | Full GC 消耗时间                                     | host4hdfsnamenode、<br>id4hdfsnamenode  |
| HdfsNnGcUtilGcTimeGct                                        | GC 时间_GCT                                                  | ms       | 垃圾回收时间消耗                                     | host4hdfsnamenode、<br> id4hdfsnamenode |
| HdfsNnJvmJavaThreadsThreadsnew                               | JVM 线程数量<br>_ThreadsNew                                  | 个       | 处于新建状态的线程数量                               | host4hdfsnamenode、<br> id4hdfsnamenode |
| HdfsNnJvmJavaThreads<br>Threadsrunnable                      | JVM 线程数量<br>_ThreadsRunnable                             | 个       | 处于可运行状态的线程数量                             | host4hdfsnamenode、<br> id4hdfsnamenode |
| HdfsNnJvmJavaThreads<br>Threadsblocked                       | JVM 线程数量<br>_ThreadsBlocked                              | 个       | 处于阻塞状态的线程数量                               | host4hdfsnamenode、<br> id4hdfsnamenode |
| HdfsNnJvmJavaThreads<br>Threadswaiting                       | JVM 线程数量<br>_ThreadsWaiting                              | 个       | 处于 WAITING 状态的线程数量                          | host4hdfsnamenode、<br> id4hdfsnamenode |
| HdfsNnJvmJavaThreads<br>Threadstimedwaiting                  | JVM 线程数量<br>_ThreadsTimedWaiting                         | 个       | 处于 TIMED WAITING 状态的线程数量                    | host4hdfsnamenode、<br> id4hdfsnamenode |
| HdfsNnJvmJavaThreads<br>Threadsterminated                    | JVM 线程数量<br>_ThreadsTerminated                           | 个       | 处于 Terminated 状态的线程数量                       | host4hdfsnamenode、<br> id4hdfsnamenode |
| HdfsNnJvmLogTotalLogfatal                                    | JVM 日志数量_LogFatal                                        | 个       | Fatal 日志数量                                       | host4hdfsnamenode、<br> id4hdfsnamenode |
| HdfsNnJvmLogTotalLogerror                                    | JVM 日志数量_LogError                                        | 个       | Error 日志数量                                       | host4hdfsnamenode、<br> id4hdfsnamenode |
| HdfsNnJvmLogTotalLogwarn                                     | JVM 日志数量_LogWarn                                         | 个       | Warn 日志数量                                        | host4hdfsnamenode、<br> id4hdfsnamenode |
| HdfsNnJvmLogTotalLoginfo                                     | JVM 日志数量_LogInfo                                         | 个       | Info 日志数量                                        | host4hdfsnamenode、<br> id4hdfsnamenode |
| HdfsNnGcUtilMemoryS0                                         | 内存区域占比_S0                                              | %        | Survivor 0区内存使用占比                             | host4hdfsnamenode、<br> id4hdfsnamenode |
| HdfsNnGcUtilMemoryS1                                         | 内存区域占比_S1                                              | %        | Survivor 1区内存使用占比                             | host4hdfsnamenode、<br> id4hdfsnamenode |
| HdfsNnGcUtilMemoryE                                          | 内存区域占比_E                                               | %        | Eden 区内存使用占比                                  | host4hdfsnamenode、<br> id4hdfsnamenode |
| HdfsNnGcUtilMemoryO                                          | 内存区域占比_O                                               | %        | Old 区内存使用占比                                   | host4hdfsnamenode、<br> id4hdfsnamenode |
| HdfsNnGcUtilMemoryM                                          | 内存区域占比_M                                               | %        | Metaspace 区内存使用占比                             | host4hdfsnamenode、<br> id4hdfsnamenode |
| HdfsNnGcUtilMemoryCcs                                        | 内存区域占比_CCS                                             | %        | Compressed class space 区内存使用占比                | host4hdfsnamenode、<br> id4hdfsnamenode |
| HdfsNnStaleStorages<br>CountNumstalestorages                 | 被标记为过期的存储的数量<br>_NumStaleStorages                | 个       | 由于心跳延迟而标记为过期的 DataNodes 当前数目        | host4hdfsnamenode、<br> id4hdfsnamenode |
| HdfsNnPendingDatanodeMessage<br>CountPendingdatanode<br/>messagecount | 备 NN 上挂起的与 BLOCK 相关操作的消息数量<br>_PendingDataNode<br/>MessageCount | 个/s     | DATANODE 的请求被 QUEUE 在 standby namenode 中的个数 | host4hdfsnamenode、<br> id4hdfsnamenode |
| HdfsNnBlocksMissingNum<br>berofmissingblocks                 | 缺失块统计<br>_NumberOfMissingBlocks                         | 个       | 缺失的数据块数量                                     | host4hdfsnamenode、<br> id4hdfsnamenode |
| HdfsNnBlocksMissingNumberof<br>missingblockswithreplication<br/>factorOne | 缺失块统计_NumberOf<br>MissingBlocksWithReplication<br/>FactorOne | 个       | 缺失的数据库数量（rf = 1）                           | host4hdfsnamenode、<br> id4hdfsnamenode |
| HdfsNnSnapshotOpsAllowsnapshotops                            | SNAPSHOT 操作<br>_AllowSnapshotOps                           | 次/s     | 每秒执行 AllowSnapshot 操作的次数                    | host4hdfsnamenode、<br> id4hdfsnamenode |
| HdfsNnSnapshotOps<br>Disallowsnapshotops                     | SNAPSHOT 操作<br>_DisallowSnapshotOps                        | 次/s     | 每秒执行 DisallowSnapshot 操作的次数                 | host4hdfsnamenode、<br> id4hdfsnamenode |
| HdfsNnSnapshotOps<br>Createsnapshotops                       | SNAPSHOT 操作<br>_CreateSnapshotOps                          | 次/s     | 每秒执行 CreateSnapshot 操作的次数                   | host4hdfsnamenode、<br> id4hdfsnamenode |
| HdfsNnSnapshotOps<br>Deletesnapshotops                       | SNAPSHOT 操作<br>_DeleteSnapshotOps                          | 次/s     | 每秒执行 DeleteSnapshot 操作的次数                   | host4hdfsnamenode、<br> id4hdfsnamenode |
| HdfsNnSnapshotOps<br>Listsnapshottabledirops                 | SNAPSHOT 操作_ListSnapshottableDirOps                        | 次/s     | 每秒执行 ListSnapshottableDir 操作次数               | host4hdfsnamenode、<br> id4hdfsnamenode |
| HdfsNnSnapshotOps<br>Snapshotdiffreportops                   | SNAPSHOT 操作_SnapshotDiffReportOps                          | 次/s     | 每秒执行 SnapshotDiffReportOps 的次数                | host4hdfsnamenode、<br> id4hdfsnamenode |
| HdfsNnSnapshotOps<br>Renamesnapshotops                       | SNAPSHOT 操作_RenameSnapshotOps                              | 次/s     | 每秒执行 RenameSnapshotOps 的次数                    | host4hdfsnamenode、<br> id4hdfsnamenode |
| HdfsNnFilesOpsCreatefileops                                  | 文件操作_CreateFileOps                                       | 次/s     | 每秒执行 CreateFile 操作的次数                       | host4hdfsnamenode、<br> id4hdfsnamenode |
| HdfsNnFilesOpsGetlistingops                                  | 文件操作_GetListingOps                                       | 次/s     | 每秒执行 GetListing 操作的次数                       | host4hdfsnamenode、<br> id4hdfsnamenode |
| HdfsNnFilesOpsTotalfileops                                   | 文件操作_TotalFileOps                                        | 次/s     | 每秒执行 TotalFileOps 的次数                         | host4hdfsnamenode、<br> id4hdfsnamenode |
| HdfsNnFilesOpsDeletefileops                                  | 文件操作_DeleteFileOps                                       | 次/s     | 每秒执行 DeleteFile 操作的次数                       | host4hdfsnamenode、<br> id4hdfsnamenode |
| HdfsNnFilesOpsFileinfoops                                    | 文件操作_FileInfoOps                                         | 次/s     | 每秒执行 FileInfo 操作的次数                         | host4hdfsnamenode、<br> id4hdfsnamenode |
| HdfsNnFilesOpsGetadditional<br>datanodeops                   | 文件操作<br>_GetAdditionalDatanodeOps                        | 次/s     | 每秒执行 GetAdditionalDatanode 操作的次数            | host4hdfsnamenode、<br> id4hdfsnamenode |
| HdfsNnFilesOpsCreatesymlinkops                               | 文件操作_CreateSymlinkOps                                    | 次/s     | 每秒执行 CreateSymlink 操作的次数                    | host4hdfsnamenode、<br> id4hdfsnamenode |
| HdfsNnFilesOpsGetlinktargetops                               | 文件操作_GetLinkTargetOps                                    | 次/s     | 每秒执行 GetLinkTarget 操作的次数                    | host4hdfsnamenode、<br> id4hdfsnamenode |
| HdfsNnFilesOpsFilesingetlistingops                           | 文件操作<br>_FilesInGetListingOps                            | 次/s     | 每秒执行 FilesInGetListing 操作的次数                | host4hdfsnamenode、<br> id4hdfsnamenode |
| HdfsNnTransactionOps<br>Transactionsnumops                   | 事务操作<br>_TransactionsNumOps                              | 次/s     | 每秒处理 Journal transaction 操作的次数              | host4hdfsnamenode、<br> id4hdfsnamenode |
| HdfsNnTransactionOps<br>Transactionsbatchedinsync            | 事务操作<br>_TransactionsBatchedInSync                       | 次/s     | 每秒批量处理 Journal transaction 操作次数            | host4hdfsnamenode、<br> id4hdfsnamenode |
| HdfsNnImageOpsGeteditnumops                                  | 镜像操作_GetEditNumOps                                       | 次/s     | 每秒执行 GetEditNumOps 的次数                        | host4hdfsnamenode、<br> id4hdfsnamenode |
| HdfsNnImageOpsGetimagenumops                                 | 镜像操作_GetImageNumOps                                      | 次/s     | 每秒执行 GetImageNumOps 的次数                       | host4hdfsnamenode、<br> id4hdfsnamenode |
| HdfsNnImageOpsPutimagenumops                                 | 镜像操作_PutImageNumOps                                      | 次/s     | 每秒执行 PutImageNumOps 的次数                       | host4hdfsnamenode、<br> id4hdfsnamenode |
| HdfsNnSyncsOpsSyncsnumops                                    | SYNC 操作_SyncsNumOps                                        | 次/s     | 每秒处理 Journal syncs 操作的次数                    | host4hdfsnamenode、<br> id4hdfsnamenode |
| HdfsNnBlocksOpsBlock<br>receivedanddeletedops                | 数据块操作<br/>_BlockOpsQueued                               | 次/s     | 每秒执行 BlockReceivedAndDeletedOps 的次数           | host4hdfsnamenode、<br> id4hdfsnamenode |
| HdfsNnBlocksOpsBlockopsqueued                                | 数据块操作<br/>_BlockOpsQueued                               | 次/s     | 处理 DataNode Block 上报操作的延迟                   | host4hdfsnamenode、<br> id4hdfsnamenode |
| HdfsNnCacheReportOps<br>Cachereportnumops                    | 缓存汇报<br/>_CacheReportNumOps                              | 次/s     | 每秒处理 CacheReport 操作的次数                      | host4hdfsnamenode、<br> id4hdfsnamenode |
| HdfsNnBlockReportOps<br>Blockreportnumops                    | 数据块汇报<br/>_BlockReportNumOps                            | 次/s     | 每秒处理 DataNode Blcok 上报操作的次数               | host4hdfsnamenode、<br> id4hdfsnamenode |
| HdfsNnSyncsRtSyncsavgtime                                    | SYNCS 操作延迟_SyncsAvgTime                                  | ms       | 处理 Journal syncs 操作的平均延迟                    | host4hdfsnamenode、<br> id4hdfsnamenode |
| HdfsNnCacheReportRt<br>Cachereportavgtime                    | Cache 汇报延迟_CacheReportAvgTime                            | ms       | 缓存上报动作平均延迟                                 | host4hdfsnamenode、<br> id4hdfsnamenode |
| HdfsNnImageRtGeteditavgtime                                  | 镜像操作延迟<br/>_GetEditAvgTime                             | ms       | 读取 Edit 文件操作平均延迟                           | host4hdfsnamenode、<br> id4hdfsnamenode |
| HdfsNnImageRtGetimageavgtime                                 | 镜像操作延迟<br/>_GetImageAvgTime                            | ms       | 读取镜像文件平均延迟                                 | host4hdfsnamenode、<br> id4hdfsnamenode |
| HdfsNnImageRtPutimageavgtime                                 | 镜像操作延迟<br/>_PutImageAvgTime                            | ms       | 写入镜像文件平均延迟                                 | host4hdfsnamenode、<br> id4hdfsnamenode |
| HdfsNnTransactionRt<br>Transactionsavgtime                   | 事务操作延迟<br/>_TransactionsAvgTime                        | ms       | 处理 Journal transaction 操作的平均延迟              | host4hdfsnamenode、<br> id4hdfsnamenode |
| HdfsNnStartTimeStarttime                                     | 启动时间_StartTime                                           | ms       | 进程启动时间                                         | host4hdfsnamenode、<br> id4hdfsnamenode |
| HdfsNnStateState                                             | 主备情况_State                                               | -        | NN 状态                                              | host4hdfsnamenode、<br> id4hdfsnamenode |
| HdfsNnThreadCountPeakthreadcount                             | 线程数量_PeakThreadCount                                     | 个       | 峰值线程数                                           | host4hdfsnamenode、<br> id4hdfsnamenode |
| HdfsNnThreadCountThreadcount                                 | 线程数量_ThreadCount                                         | 个       | 线程数量                                             | host4hdfsnamenode、<br> id4hdfsnamenode |
| HdfsNnThreadCount<br>Daemonthreadcount                       | 线程数量_DaemonThreadCount                                   | 个       | 后台线程数量                                         | host4hdfsnamenode、<br> id4hdfsnamenode |
| HdfsNnPort4007Rt<br>Rpcprocessingtimeavgtime                     | 请求处理延迟_ RpcProcessingTimeAvgTime	                                  | ms       | 请求处理延迟                                  | host4hdfsnamenode、<br> id4hdfsnamenode |


### HDFS-DataNode

| 指标英文名                                                   | 指标中文名                                                   | 指标单位 | 指标含义                                   | 维度                                   |
| ------------------------------------------------------------ | ------------------------------------------------------------ | -------- | ------------------------------------------ | -------------------------------------- |
| HdfsDnXceiverXceivercount                                    | XCEIVER 数量_XceiverCount                                    | 个       | Xceiver 数量                               | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnBytesByteswrittenmb                                    | 数据读写速率_BytesReadMB                                     | Bytes/s  | 写入 DN 的字节速率                         | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnBytesBytesreadmb                                       | 数据读写速率_BytesReadMB                                     | Bytes/s  | 读取 DN 的字节速率                         | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnBytesRemotebytesreadmb                                 | 数据读写速率<br/>_RemoteBytesReadMB                          | Bytes/s  | 远程客户端读取字节速率                     | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnBytesRemoteby<br>teswrittenmb                          | 数据读写速率<br/>_RemoteBytesWrittenMB                       | Bytes/s  | 远程客户端写入字节速率                     | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnClientWritesfrom<br>remoteclient                       | 客户端连接数<br/>_WritesFromRemoteClient                     | 个       | 来自远程客户端写操作 QPS                   | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnClientWritesfromlocalclient                            | 客户端连接数<br/>_WritesFromLocalClient                      | 个       | 来自本地客户端写操作 OPS                   | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnClientReadsfrom<br>remoteclient                        | 客户端连接数<br/>_ReadsFromRemoteClient                      | 个       | 来自远程客户端读操作 QPS                   | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnClientReadsfromlocalclient                             | 客户端连接数<br/>_ReadsFromLocalClient                       | 个       | 来自本地客户端读操作 QPS                   | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnBlocksVerifiedFailures<br>Blockverificationfailures    | Block 校验失败<br/>_BlockVerificationFailures                | 次/s     | BLOCK 校验失败数量                         | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnVolumeFailures<br>Volumefailures                       | 磁盘故障_VolumeFailures                                      | 次/s     | 磁盘故障次数                               | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnNetworkErrors<br>Datanodenetworkerrors                 | 网络错误<br/>_DatanodeNetworkErrors                          | 次/s     | 网络错误统计                               | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnHbRtHeartbeatsavgtime                                  | 心跳延迟_HeartbeatsAvgTime                                   | ms       | 心跳接口平均时间                           | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnHbOpsHeartbeatsnumops                                  | 心跳 QPS_HeartbeatsNumOps                                    | 次/s     | 心跳接口 QPS                               | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnDatapacketAvgtimeSend<br>datapackettransfer<br/>nanosavgtime | 包传输操作<br/> QPS_SendDataPacketTransfer<br/>NanosAvgTime  | ms       | 发送数据包平均时间                         | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnBlocksOpsRead<br>blockopnumops                         | 数据块操作<br/>_ReadBlockOpNumOps                            | 次/s     | 从 DataNode 读取 Block OPS                 | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnBlocksOpsWrite<br>blockopnumops                        | 数据块操作<br/>_WriteBlockOpNumOps                           | 次/s     | 向 DataNode 写入 Block OPS                 | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnBlocksOpsBlock<br>checksumopnumops                     | 数据块操作<br/>_BlockChecksumOpNumOps                        | 次/s     | DataNode 进行 Checksum 操作的 OPS          | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnBlocksOpsCopy<br>blockopnumops                         | 数据块操作<br/>_CopyBlockOpNumOps                            | 次/s     | 复制 Block 操作的 OPS                      | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnBlocksOpsReplace<br>blockopnumops                      | 数据块操作<br/>_ReplaceBlockOpNumOps                         | 次/s     | Replace Block 操作的 OPS                   | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnBlocksOpsBlock<br>reportsnumops                        | 数据块操作<br/>_BlockReportsNumOps                           | 次/s     | BLOCK 汇报动作的 OPS                       | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnBlocksOpsIncremental<br>blockreports<br/>numops        | 数据块操作<br/>_IncrementalBlockReports<br/>NumOps           | 次/s     | BLOCK 增量汇报的 OPS                       | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnBlocksOpsCache<br>reportsnumops                        | 数据块操作<br/>_CacheReportsNumOps                           | 次/s     | 缓存汇报的 OPS                             | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnBlocksOpsPacketack<br>roundtriptimenanos<br/>numops    | 数据块操作<br/>_PacketAckRoundTripTimeNanos<br/>NumOps       | 次/s     | 每秒处理 ACK ROUND TRIP 次数               | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnFsyncOpsFsync<br>nanosnumops                           | FSYNC 操作<br/>_FsyncNanosNumOps                             | 次/s     | FSYNC 次数                                 | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnFlushOpsFlush<br>nanosnumops                           | FLUSH 操作<br/>_FlushNanosNumOps                             | 次/s     | 每秒处理 Flush 操作次数                    | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnBlocksRtRead<br>blockopavgtime                         | 数据块操作延迟统计<br/>_ReadBlockOpAvgTime                   | ms       | 读取 Block 操作平均时间                    | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnBlocksRtWrite<br>blockopavgtime                        | 数据块操作延迟统计<br/>_ReplaceBlockOpAvgTime                | ms       | 写 Blcok 操作平均时间                      | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnBlocksRtBlock<br>checksumopavgtime                     | 数据块操作延迟统计_BlockChecksumOpAvgTime                    | ms       | 块校验操作平均时间                         | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnBlocksRtCopy<br>blockopavgtime                         | 数据块操作延迟统计<br/>_CopyBlockOpAvgTime                   | ms       | 复制块操作平均时间                         | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnBlocksRt<br>Replaceblockopavgtime                      | 数据块操作延迟统计<br/>_Replaceblockopavgtime                | ms       | Replace Block 操作平均时间                 | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnBlocksRtBlock<br>reportsavgtime                        | 数据块操作延迟统计<br/>_BlockReportsAvgTime                  | ms       | 块汇报平均时间                             | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnBlocksRtIncremental<br>blockreportsavgtime             | 数据块操作延迟统计<br/>_IncrementalBlockReportsAvgTime       | ms       | 增量块汇报平均时间                         | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnBlocksRtCache<br>reportsavgtime                        | 数据块操作延迟统计<br/>_CacheReportsAvgTime                  | ms       | 缓存汇报平均时间                           | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnBlocksRtPacketack<br>roundtriptimenanos<br/>avgtime    | 数据块操作延迟统计<br/>_PacketAckRoundTripTimeNanos<br/>AvgTime | ms       | 处理 ACK ROUND TRIP 平均时间               | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnFlushRtFlushnanosavgtime                               | FLUSH延迟_FlushNanosAvgTime                                  | ms       | Flush 操作平均时间                         | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnFsyncRtFsyncnanosavgtime                               | FSYNC延迟_FsyncNanosAvgTime                                  | ms       | Fsync 操作平均时间                         | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnRamBlocksOp<br>Ramdiskblockswrite                      | RAMDISKBlocks_Ram<br/>DiskBlocksWrite                        | 块/s     | 写入内存的块的总数                         | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnRamBlocksOp<br>Ramdiskblockswritefallback              | RAMDISKBlocks_Ram<br/>DiskBlocksWriteFallback                | 块/s     | 写入内存但未成功的块总数（故障转移到磁盘） | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnRamBlocksOpRamdisk<br>blocksdeletedbeforelazypersisted | RAMDISKBlocks_RamDiskBlocks<br>DeletedBeforeLazyPersisted    | 块/s     | 应用程序在被保存到磁盘之前被删除的块的总数 | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnRamBlocksOp<br>Ramdiskblocksreadhits                   | RAMDISKBlocks_Ram<br/>DiskBlocksReadHits                     | 块/s     | 内存中的块被读取的总次数                   | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnRamBlocksOp<br>Ramdiskblocksevicted                    | RAMDISKBlocks_Ram<br/>DiskBlocksEvicted                      | 块/s     | 内存中被清除的块总数                       | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnRamBlocksOpRamdisk<br>blocksevictedwithoutread         | RAMDISKBlocks_RamDiskBlocks<br>EvictedWithoutRead            | 块/s     | 从内存中取出的内存块总数                   | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnRamBlocksOp<br>Ramdiskblockslazypersisted              | RAMDISKBlocks_RamDisk<br>BlocksLazyPersisted                 | 块/s     | 惰性写入器写入磁盘的总数                   | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnRamBlocksOp<br>Ramdiskbyteslazypersisted               | RAMDISKBlocks_Ram<br/>DiskBytesLazyPersisted                 | Bytes/s  | 由懒惰写入器写入磁盘的总字节数             | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnRamBlocksBytes<br>Ramdiskbyteswrite                    | RAMDISK 写入速度_RamDiskBytesWrite                           | Bytes/s  | 写入内存的总字节数                         | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnJvmMem<br>Memnonheapusedm                              | JVM 内存<br/>_MemNonHeapUsedM                                | MB       | JVM 当前已经使用的 NonHeapMemory 的大小    | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnJvmMem<br>Memnonheapcommittedm                         | JVM 内存<br/>_MemNonHeapCommittedM                           | MB       | JVM 配置的 NonHeapCommittedM 的大小        | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnJvmMemMemheapusedm                                     | JVM 内存<br/>_MemHeapUsedM                                   | MB       | JVM 当前已经使用的 HeapMemory 的大小       | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnJvmMem<br>Memheapcommittedm                            | JVM 内存<br/>_MemHeapCommittedM                              | MB       | JVM HeapMemory 提交大小                    | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnJvmMemMemheapmaxm                                      | JVM 内存<br/>_MemHeapMaxM                                    | MB       | JVM 配置的 HeapMemory 的大小               | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnJvmMemMemmaxm                                          | JVM 内存<br/>_MemMaxM                                        | MB       | JVM 运行时的可以使用的最大的内存的大小     | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnJvmJavaThreadsThreadsnew                               | JVM 线程数量<br/>_ThreadsNew                                 | 个       | 处于新建状态的线程数量                     | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnJvmJavaThreads<br>Threadsrunnable                      | JVM 线程数量<br/>_ThreadsRunnable                            | 个       | 处于可运行状态的线程数量                   | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnJvmJavaThreads<br>Threadsblocked                       | JVM线程数量<br/>_ThreadsBlocked                              | 个       | 处于阻塞状态的线程数量                     | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnJvmJavaThreads<br>Threadswaiting                       | JVM 线程数量<br/>_ThreadsWaiting                             | 个       | 处于 WAITING 状态的线程数量                | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnJvmJavaThreads<br>Threadstimedwaiting                  | JVM 线程数量<br/>_ThreadsTimedWaiting                        | 个       | 处于 TIMED WAITING 状态的线程数量          | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnJvmJavaThreads<br>Threadsterminated                    | JVM 线程数量<br/>_ThreadsTerminated                          | 个       | 处于 Terminated 状态的线程数量             | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnJvmLogTotalLogfatal                                    | JVM 日志数量_LogFatal                                        | 个       | Fatal 日志数量                             | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnJvmLogTotalLogerror                                    | JVM 日志数量_LogError                                        | 个       | Error 日志数量                             | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnJvmLogTotalLogwarn                                     | JVM 日志数量_LogWarn                                         | 个       | Warn 日志数量                              | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnJvmLogTotalLoginfo                                     | JVM 日志数量_LogInfo                                         | 个       | Info 日志数量                              | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnGcUtilMemoryS0                                         | 内存区域占比_S0                                              | %        | Survivor 0区内存使用占比                   | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnGcUtilMemoryS1                                         | 内存区域占比_S1                                              | %        | Survivor 1区内存使用占比                   | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnGcUtilMemoryE                                          | 内存区域占比_E                                               | %        | Eden 区内存使用占比                        | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnGcUtilMemoryO                                          | 内存区域占比_O                                               | %        | Old 区内存使用占比                         | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnGcUtilMemoryM                                          | 内存区域占比_M                                               | %        | Metaspace 区内存使用占比                   | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnGcUtilMemoryCcs                                        | 内存区域占比_CCS                                             | %        | Compressed class space 区内存使用占比      | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnGcUtilGcCountFgc                                       | GC 次数_FGC                                                  | 次       | Full GC 次数                               | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnGcUtilGcCountYgc                                       | GC 次数_YGC                                                  | 次       | Young GC 次数                              | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnGcUtilGcTimeYgct                                       | GC 时间_YGCT                                                 | s        | Young GC 消耗时间                          | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnGcUtilGcTimeFgct                                       | GC 时间_FGCT                                                 | s        | Full GC 消耗时间                           | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnGcUtilGcTimeGct                                        | GC 时间_GCT                                                  | s        | 垃圾回收时间消耗                           | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnPort4004RxtxReceivedbytes                              | 数据流量_ReceivedBytes                                       | Bytes/s  | 接收数据速率                               | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnPort4004RxtxSentbytes                                  | 数据流量_SentBytes                                           | Bytes/s  | 发送数据速率                               | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnPort4004QpsRpc<br>queuetimenumops                      | QPS_RpcQueueTimeNumOps                                       | 次/s     | RPC 调用速率                               | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnPort4004RtRpc<br>queuetimeavgtime                      | 请求处理延迟<br/>_RpcQueueTimeAvgTime                        | ms       | RPC 平均延迟时间                           | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnPort4004AuthRpc<br>authenticationfailures              | 验证和授权<br/>_RpcAuthenticationFailures                    | 次/s     | RPC 验证失败次数                           | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnPort4004AuthRpc<br>authenticationsuccesses             | 验证和授权<br/>_RpcAuthenticationSuccesses                   | 次/s     | RPC 验证成功次数                           | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnPort4004AuthRpc<br>authorizationfailures               | 验证和授权<br/>_RpcAuthorizationFailures                     | 次/s     | RPC 授权失败次数                           | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnPort4004AuthRpc<br>authorizationsuccesses              | 验证和授权<br/>_RpcAuthorizationSuccesses                    | 次/s     | RPC 授权成功次数                           | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnPort4004Connections<br>Numopenconnections              | 当前连接数<br/>_NumOpenConnections                           | 个       | 当前链接数量                               | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnPort4004QueueLen<br>Callqueuelength                    | RPC 处理队列长度<br/>_CallQueueLength                        | 个       | 当前 RPC 处理队列长度                      | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnThreadTimeCurrent<br>threadcputime                     | CPU 时间<br/>_CurrentThreadCpuTime                           | ms       | CPU时间                                    | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnThreadTimeCurrent<br>threadusertime                    | CPU 时间<br/>_CurrentThreadUserTime                          | ms       | 用户时间                                   | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnStartTimeStarttime                                     | 线程数量<br/>_DaemonThreadCount                              | s        | 进程启动时间                               | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnThreadCount<br>Peakthreadcount                         | 程数量_PeakThreadCount                                       | 个       | 峰值线程数量                               | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnThreadCount<br>Daemonthreadcount                       | 线程数量_DaemonThreadCount                                   | 个       | 后台线程数量                               | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnRtWrit                                                 | 读写延迟_Write                                               | MB/s     | 磁盘写速率                                 | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnRtRead                                                 | 读写延迟_Read                                                | 次/s     | 读操作 QPS                                 | id4hdfsdatanode、<br>host4hdfsdatanode |
| HdfsDnDatapacketOps<br>Datapacketops                         | 包传输操作 QPS_DataPacketOps                                 | 次/s     | 包传输操作 QPS                             | id4hdfsdatanode、<br>host4hdfsdatanode |

### HDFS-Journal Node

| 指标英文名                                       | 指标中文名                            | 指标单位 | 指标含义                                |                                               |
| ------------------------------------------------ | ------------------------------------- | -------- | --------------------------------------- | --------------------------------------------- |
| HdfsJnJvmMemMemnon<br>heapusedm                  | JVM 内存_MemNonHeapUsedM              | MB       | JVM 当前已经使用的 NonHeapMemory 的大小 | host4hdfsjournalnode、<br>id4hdfsjournalnode  |
| HdfsJnJvmMemMemnon<br>heapcommittedm             | JVM 内存_MemNonHeapCommittedM         | MB       | JVM 内存                                | host4hdfsjournalnode、<br>id4hdfsjournalnode  |
| HdfsJnJvmMemMem<br>heapusedm                     | JVM 内存_MemHeapUsedM                 | MB       | JVM 当前已经使用的 HeapMemory 的大小    | host4hdfsjournalnode、<br>id4hdfsjournalnode  |
| HdfsJnJvmMemMem<br>heapcommittedm                | JVM 内存_MemHeapCommittedM            | MB       | JVM HeapMemory 提交大小                 | host4hdfsjournalnode、<br>id4hdfsjournalnode  |
| HdfsJnJvmMemMem<br>heapmaxm                      | JVM 内存_MemHeapMaxM                  | MB       | JVM 配置的 HeapMemory 的大小            | host4hdfsjournalnode、<br>id4hdfsjournalnode  |
| HdfsJnJvmMemMemmaxm                              | JVM 内存_MemMaxM                      | MB       | JVM 运行时的可以使用的最大的内存的大小  | host4hdfsjournalnode、<br>id4hdfsjournalnode  |
| HdfsJnJvmJavaThreads<br>Threadsnew               | JVM 线程数量_ThreadsNew               | 个       | 处于新建状态的线程数量                  | host4hdfsjournalnode、<br>id4hdfsjournalnode  |
| HdfsJnJvmJavaThreads<br>Threadsrunnable          | JVM 线程数量_ThreadsRunnable          | 个       | 处于可运行状态的线程数量                | host4hdfsjournalnode、<br>id4hdfsjournalnode  |
| HdfsJnJvmJavaThreads<br>Threadsblocked           | JVM 线程数量_ThreadsBlocked           | 个       | 处于阻塞状态的线程数量                  | host4hdfsjournalnode、<br>id4hdfsjournalnode  |
| HdfsJnJvmJavaThreads<br>Threadswaiti             | JVM 线程数量_ThreadsWaiting           | 个       | 处于 WAITING 状态的线程数量             | host4hdfsjournalnode、<br>id4hdfsjournalnode  |
| HdfsJnJvmJavaThreads<br>Threadstimedwaiting      | JVM 线程数量_ThreadsTimedWaiting      | 个       | 处于 TIMED WAITING 状态的线程数量       | host4hdfsjournalnode、<br>id4hdfsjournalnode  |
| HdfsJnJvmJavaThreads<br>Threadsterminated        | JVM 线程数量_ThreadsTerminated        | 个       | 处于 Terminated 状态的线程数量          | host4hdfsjournalnode、<br>id4hdfsjournalnode  |
| HdfsJnJvmLogTotalLogfatal                        | JVM 日志数量_LogFatal                 | 个       | Fatal 日志数量                          | host4hdfsjournalnode、<br>id4hdfsjournalnode  |
| HdfsJnJvmLogTotalLogerror                        | JVM 日志数量_LogError                 | 个       | Error 日志数量                          | host4hdfsjournalnode、<br>id4hdfsjournalnode  |
| HdfsJnJvmLogTotalLogwarn                         | JVM 日志数量_LogWarn                  | 个       | Warn 日志数量                           | host4hdfsjournalnode、<br>id4hdfsjournalnode  |
| HdfsJnJvmLogTotalLoginfo                         | JVM 日志数量_LogInfo                  | 个       | Info 日志数量                           | host4hdfsjournalnode、<br>id4hdfsjournalnode  |
| HdfsJnGcUtilMemoryS0                             | 内存区域占比_S0                       | %        | Survivor 0区内存使用占比                | host4hdfsjournalnode、<br>id4hdfsjournalnode  |
| HdfsJnGcUtilMemoryS1                             | 内存区域占比_S1                       | %        | Survivor 1区内存使用占比                | host4hdfsjournalnode、<br>id4hdfsjournalnode  |
| HdfsJnGcUtilMemoryE                              | 内存区域占比_E                        | %        | Eden 区内存使用占比                     | host4hdfsjournalnode、<br>id4hdfsjournalnode  |
| HdfsJnGcUtilMemoryO                              | 内存区域占比_O                        | %        | Old 区内存使用占比                      | host4hdfsjournalnode、<br>id4hdfsjournalnode  |
| HdfsJnGcUtilMemoryM                              | 内存区域占比_M                        | %        | Metaspace 区内存使用占比                | host4hdfsjournalnode、<br>id4hdfsjournalnode  |
| HdfsJnGcUtilMemoryCcs                            | 内存区域占比_CCS                      | %        | Compressed class space 区内存使用占比   | host4hdfsjournalnode、<br>id4hdfsjournalnode  |
| HdfsJnGcUtilGcCountFgc                           | GC 次数_FGC                           | 次       | Full GC 次数                            | host4hdfsjournalnode、<br>id4hdfsjournalnode  |
| HdfsJnGcUtilGcCountYgc                           | GC 次数_YGC                           | 次       | Young GC 次数                           | host4hdfsjournalnode、<br>id4hdfsjournalnode  |
| HdfsJnGcUtilGcTimeYgct                           | GC 时间_YGCT                          | s        | Young GC 消耗时间                       | host4hdfsjournalnode、<br>id4hdfsjournalnode  |
| HdfsJnGcUtilGcTimeFgct                           | GC 时间_FGCT                          | s        | Full GC 消耗时间                        | host4hdfsjournalnode、<br>id4hdfsjournalnode  |
| HdfsJnGcUtilGcTimeGct                            | GC 时间_GC                            | s        | 垃圾回收时间消耗                        | host4hdfsjournalnode、<br>id4hdfsjournalnode  |
| HdfsJnPort4005Rxtx<br>Receivedbytes              | 数据流量_ReceivedBytes                | Bytes/s  | 接收数据速率                            | host4hdfsjournalnode、<br>id4hdfsjournalnode  |
| HdfsJnPort4005Rxtx<br>Receivedbytes              | 数据流量_ReceivedBytes                | Bytes/s  | 发送数据速率                            | host4hdfsjournalnode、<br>id4hdfsjournalnode  |
| HdfsJnPort4005QpsRpc<br>queuetimenumops          | QPS_RpcQueueTimeNumOps                | 次/s     | RPC 调用速率                            | host4hdfsjournalnode、<br>id4hdfsjournalnode  |
| HdfsJnPort4005RtRpc<br>queuetimeavgtime          | 请求处理延迟_RpcQueueTimeAvgTime      | ms       | RPC 平均延迟时间                        | host4hdfsjournalnode、<br>id4hdfsjournalnode  |
| HdfsJnPort4005AuthRpc<br>authenticationfailures  | 验证和授权_RpcAuthenticationFailures  | 次/s     | RPC 验证失败次数                        | host4hdfsjournalnode、<br>id4hdfsjournalnode  |
| HdfsJnPort4005AuthRpc<br>authorizationsuccesses  | 验证和授权_RpcAuthorizationSuccesses  | 次/s     | RPC 授权成功次数                        | host4hdfsjournalnode、<br>id4hdfsjournalnode  |
| HdfsJnPort4005AuthRpc<br>authenticationsuccesses | 验证和授权_RpcAuthenticationSuccesses | 次/s     | RPC 验证成功次数                        | host4hdfsjournalnode、<br>id4hdfsjournalnode  |
| HdfsJnPort4005AuthRpc<br>authorizationfailures   | 验证和授权_RpcAuthorizationFailures   | 次/s     | RPC 授权失败次数                        | host4hdfsjournalnode、<br>id4hdfsjournalnode  |
| HdfsJnPort4005Connections<br>Numopenconnections  | 当前连接数_NumOpenConnections         | 个       | 当前链接数量                            | host4hdfsjournalnode、<br>id4hdfsjournalnode  |
| HdfsJnPort4005QueueLen<br>Callqueuelength        | RPC 处理队列长度_CallQueueLength      | 个       | 当前 RPC 处理队列长度                   | host4hdfsjournalnode、<br>id4hdfsjournalnode  |
| HdfsJnThreadTimeCurrent<br>threadcputime         | CPU 时间_CurrentThreadCpuTime         | ms       | CPU时间                                 | host4hdfsjournalnode、<br>id4hdfsjournalnode  |
| HdfsJnThreadTimeCurrent<br>threadusertime        | CPU 时间_CurrentThreadUserTime        | ms       | 用户时间                                | host4hdfsjournalnode、<br>id4hdfsjournalnode  |
| HdfsJnStartTimeStarttime                         | 启动时间_StartTime                    | s        | 进程启动时间                            | host4hdfsjournalnode、<br>id4hdfsjournalnode  |
| HdfsJnThreadCount<br>Threadcount                 | 线程数量_ThreadCount                  | 个       | 线程数量                                | host4hdfsjournalnode、<br>id4hdfsjournalnode  |
| HdfsJnThreadCount<br>Peakthreadcount             | 线程数量_PeakThreadCount              | 个       | 峰值线程数量                            | host4hdfsjournalnode、<br>id4hdfsjournalnode  |
| HdfsJnThreadCountDaemon<br>threadcount           | 线程数量_DaemonThreadCount            | 个       | 后台线程数量                            | host4hdfsjournalnode、<br/>id4hdfsjournalnode |

### HDFS-ZKFC

| 指标英文名               | 指标中文名       | 指标单位 | 指标含义                              | 维度                                                         |
| ------------------------ | ---------------- | -------- | ------------------------------------- | ------------------------------------------------------------ |
| HdfsDfzkGcUtilMemoryS0   | 内存区域占比_S0  | %        | Survivor 0区内存使用占比              | host4hdfszkfailovercontroller、<br>id4hdfszkfailovercontroller |
| HdfsDfzkGcUtilMemoryS1   | 内存区域占比_S1  | %        | Survivor 1区内存使用占比              | host4hdfszkfailovercontroller、<br>id4hdfszkfailovercontroller |
| HdfsDfzkGcUtilMemoryE    | 内存区域占比_E   | %        | Eden 区内存使用占比                   | host4hdfszkfailovercontroller、<br>id4hdfszkfailovercontroller |
| HdfsDfzkGcUtilMemoryO    | 内存区域占比_O   | %        | Old 区内存使用占比                    | host4hdfszkfailovercontroller、<br>id4hdfszkfailovercontroller |
| HdfsDfzkGcUtilMemoryM    | 内存区域占比_M   | %        | Metaspace 区内存使用占比              | host4hdfszkfailovercontroller、<br>id4hdfszkfailovercontroller |
| HdfsDfzkGcUtilMemoryCcs  | 内存区域占比_CCS | %        | Compressed class space 区内存使用占比 | host4hdfszkfailovercontroller、<br>id4hdfszkfailovercontroller |
| HdfsDfzkGcUtilGcCountFgc | GC次数_FGC       | 次       | Full GC 次数                          | host4hdfszkfailovercontroller、<br>id4hdfszkfailovercontroller |
| HdfsDfzkGcUtilGcCountYgc | GC次数_YGC       | 次       | Young GC 次数                         | host4hdfszkfailovercontroller、<br>id4hdfszkfailovercontroller |
| HdfsDfzkGcUtilGcTimeYgct | GC时间_YGCT      | s        | Young GC 消耗时间                     | host4hdfszkfailovercontroller、<br>id4hdfszkfailovercontroller |
| HdfsDfzkGcUtilGcTimeFgct | GC时间_FGCT      | s        | Full GC 消耗时间                      | host4hdfszkfailovercontroller、<br>id4hdfszkfailovercontroller |
| HdfsDfzkGcUtilGcTimeGct  | GC时间_GCT       | s        | 垃圾回收时间消耗                      | host4hdfszkfailovercontroller、<br>id4hdfszkfailovercontroller |

> ?每个指标的统计粒度（Period）可取值不一定相同，可通过 [DescribeBaseMetrics](https://cloud.tencent.com/document/product/248/30351) 接口获取每个指标支持的统计粒度。

## 各维度对应参数总览

| 参数名称                       | 维度名称                      | 维度解释                      | 格式                                                         |
| ------------------------------ | ----------------------------- | ----------------------------- | ------------------------------------------------------------ |
| Instances.N.Dimensions.0.Name  | id4hdfsoverview               | EMR 实例 ID 的维度名称        | 输入  String 类型维度名称：id4hdfsoverview                   |
| Instances.N.Dimensions.0.Value | id4hdfsoverview               | EMR  实例具体 ID              | 输入  EMR 具体实例 ID，例如 ：emr-mm8bs222                   |
| Instances.N.Dimensions.1.Name  | host4hdfsoverview             | EMR  实例中节点 IP 的维度名称 | 输入String  类型维度名称：host4hdfsoverview                  |
| Instances.N.Dimensions.1.Value | host4hdfsoverview             | EMR  实例中具体节点 IP        | 输入具体节点  IP ，可从控制台获取，登录 [腾讯云 MapReduce 控制台](https://console.cloud.tencent.com/emr) > 单击实例 > 集群资源 > 资源管理 > 节点内网 IP。也可通过 [查询节点信息](https://cloud.tencent.com/document/product/589/41707) API 获取。 |
| Instances.N.Dimensions.0.Name  | id4hdfsnamenode               | EMR 实例 ID 的维度名称        | 输入 String  类型维度名称：id4hdfsnamenode                   |
| Instances.N.Dimensions.0.Value | id4hdfsnamenode               | EMR 实例具体 ID               | 输入 EMR 具体实例 ID，例如  ：emr-mm8bs222                   |
| Instances.N.Dimensions.1.Name  | host4hdfsnamenode             | EMR 实例中节点 IP 的维度名称  | 输入String  类型维度名称：host4hdfsnamenode                  |
| Instances.N.Dimensions.1.Value | host4hdfsnamenode             | EMR 实例中具体节点 IP         | 输入具体节点  IP ，可从控制台获取，登录 [腾讯云 MapReduce 控制台](https://console.cloud.tencent.com/emr) > 单击实例 > 集群资源 > 资源管理 > 节点内网 IP。也可通过 [查询节点信息](https://cloud.tencent.com/document/product/589/41707) API 获取。 |
| Instances.N.Dimensions.0.Name  | id4hdfsdatanode               | EMR  实例 ID 的维度名称       | 输入 String  类型维度名称：id4hdfsdatanode                   |
| Instances.N.Dimensions.0.Value | id4hdfsdatanode               | EMR  实例具体 ID              | 输入 EMR 具体实例 ID，例如  ：emr-mm8bs222                   |
| Instances.N.Dimensions.1.Name  | host4hdfsdatanode             | EMR  实例中节点 IP 的维度名称 | 输入String  类型维度名称：host4hdfsdatanode                  |
| Instances.N.Dimensions.1.Value | host4hdfsdatanode             | EMR  实例中具体节点 IP        | 输入具体节点  IP ，可从控制台获取，登录 [腾讯云 MapReduce 控制台](https://console.cloud.tencent.com/emr) > 单击实例 > 集群资源 > 资源管理 > 节点内网 IP。也可通过 [查询节点信息](https://cloud.tencent.com/document/product/589/41707) API 获取。 |
| Instances.N.Dimensions.0.Name  | id4hdfsjournalnode            | EMR 实例 ID 的维度名称        | 输入 String  类型维度名称：id4hdfsjournalnode                |
| Instances.N.Dimensions.0.Value | id4hdfsjournalnode            | EMR 实例具体 ID               | 输入 EMR 具体实例 ID，例如  ：emr-mm8bs222                   |
| Instances.N.Dimensions.1.Name  | host4hdfsjournalnode          | EMR 实例中节点 IP 的维度名称  | 输入String  类型维度名称：host4hdfsjournalnode               |
| Instances.N.Dimensions.1.Value | host4hdfsjournalnode          | EMR 实例中具体节点 IP         | 输入具体节点  IP ，可从控制台获取，登录 [腾讯云 MapReduce 控制台](https://console.cloud.tencent.com/emr) > 单击实例 > 集群资源 > 资源管理 > 节点内网 IP。也可通过 [查询节点信息](https://cloud.tencent.com/document/product/589/41707) API 获取。 |
| Instances.N.Dimensions.0.Name  | id4hdfszkfailovercontroller   | EMR  实例 ID 的维度名称       | 输入  String 类型维度名称：id4hdfszkfailovercontroller       |
| Instances.N.Dimensions.0.Value | id4hdfszkfailovercontroller   | EMR  实例具体 ID              | 输入  EMR 具体实例 ID，例如 ：emr-mm8bs222                   |
| Instances.N.Dimensions.1.Name  | host4hdfszkfailovercontroller | EMR  实例中节点 IP 的维度名称 | 输入String  类型维度名称：host4hdfszkfailovercontroller      |
| Instances.N.Dimensions.1.Value | host4hdfszkfailovercontroller | EMR  实例中具体节点 IP        | 输入具体节点  IP ，可从控制台获取，登录 [腾讯云 MapReduce 控制台](https://console.cloud.tencent.com/emr) > 单击实例 > 集群资源 > 资源管理 > 节点内网IP。也可通过 [查询节点信息](https://cloud.tencent.com/document/product/589/41707) API 获取。 |

## 入参说明

弹性 MapReduce（HDFS）支持以下六种维度组合的查询方式，六种入参取值如下：

**1. 查询  HDFS-OverviewAggregation  的指标监控数据，入参取值如下：**
&Namespace=QCE/TXMR_HDFS
&Instances.N.Dimensions.0.Name=id4hdfsoverview
&Instances.N.Dimensions.0.Value=EMR 实例 ID

**2. 查询 HDFS-Overview  的指标监控数据，入参取值如下：**
&Namespace=QCE/TXMR_HDFS
&Instances.N.Dimensions.0.Name=id4hdfsoverview
&Instances.N.Dimensions.0.Value=EMR 实例 ID
&Instances.N.Dimensions.1.Name=host4hdfsoverview
&Instances.N.Dimensions.1.Value=EMR 实例中具体节点 IP

**3. 查询  HDFS-NameNode 的指标监控数据，入参取值如下：**
&Namespace=QCE/TXMR_HDFS
&Instances.N.Dimensions.0.Name=id4hdfsnamenode
&Instances.N.Dimensions.0.Value=EMR 实例 ID
&Instances.N.Dimensions.1.Name=host4hdfsnamenode
&Instances.N.Dimensions.1.Value=EMR实例中具体节点 IP

**4. 查询  HDFS-DataNode 的指标监控数据，入参取值如下：**
&Namespace=QCE/TXMR_HDFS
&Instances.N.Dimensions.0.Name=id4hdfsdatanode
&Instances.N.Dimensions.0.Value=EMR 实例 ID
&Instances.N.Dimensions.1.Name=host4hdfsdatanode
&Instances.N.Dimensions.1.Value=EMR实例中具体节点 IP

**5. 查询  HDFS-Journal Node 的指标监控数据，入参取值如下：**
&Namespace=QCE/TXMR_HDFS
&Instances.N.Dimensions.0.Name=id4hdfsjournalnode
&Instances.N.Dimensions.0.Value=EMR 实例具体 ID
&Instances.N.Dimensions.1.Name=host4hdfsjournalnode
&Instances.N.Dimensions.1.Value=EMR 实例中具体节点 IP

**6. 查询  HDFS-ZKFC 的指标监控数据，入参取值如下：**
&Namespace=QCE/TXMR_HDFS
&Instances.N.Dimensions.0.Name=id4hdfszkfailovercontroller
&Instances.N.Dimensions.0.Value=EMR 实例具体 ID
&Instances.N.Dimensions.1.Name=host4hdfszkfailovercontroller
&Instances.N.Dimensions.1.Value=EMR 实例中具体节点 IP





