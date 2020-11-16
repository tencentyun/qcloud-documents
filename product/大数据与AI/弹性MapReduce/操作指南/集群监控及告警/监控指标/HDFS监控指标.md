### HDFS-概览

| 指标名称                     | 指标单位 | 指标含义                                      |
| ---------------------------- | -------- | --------------------------------------------- |
| CapacityTotal                | GB       | 集群存储总容量                                |
| CapacityUsed                 | GB       | 集群存储已使用容量                            |
| CapacityRemaining            | GB       | 集群存储剩余容量                              |
| CapacityUsedNonDFS           | GB       | 集群非 HDFS 使用容量                          |
| TotalLoad                    | 1        | 当前连接数                                    |
| FilesTotal                   | 个       | 总文件数量                                    |
| BlocksTotal                  | 个       | 总 BLOCK 数量                                 |
| PendingReplicationBlocks     | 个       | 等待被备份的块数量                            |
| UnderReplicatedBlocks        | 个       | 副本数不够的块数量                            |
| CorruptBlocks                | 个       | 坏块数量                                      |
| ScheduledReplicationBlocks   | 个       | 安排要备份的块数量                            |
| PendingDeletionBlocks        | 个       | 等待被删除的块数量                            |
| ExcessBlocks                 | 个       | 多于的块数量                                  |
| PostponedMisreplicatedBlocks | 个       | 被推迟处理的异常块数量                        |
| BlockCapacity                | 个       | BLOCK 容量                                    |
| NumLiveDataNodes             | 个       | 活的数据节点数量                              |
| NumDeadDataNodes             | 个       | 已经标记为 Dead 状态的数据节点数量            |
| NumDecomLiveDataNodes        | 个       | 下线且 Live 的节点数量                        |
| NumDecomDeadDataNodes        | 个       | 下线且 Dead 的节点数量                        |
| NumDecommissioningDataNodes  | 个       | 正在下线的节点数量                            |
| NumStaleDataNodes            | 个       | 由于心跳延迟而标记为过期的 DataNodes 当前数量 |
| Snapshots                    | 个       | Snapshots 数量                                |
| VolumeFailuresTotal          | 次       | 所有 Datanodes 的全故障总数                   |

### HDFS-NameNode

| 指标名称                                      | 指标单位 | 指标含义                                             |
| --------------------------------------------- | -------- | ---------------------------------------------------- |
| ReceivedBytes                                 | Bytes/s  | 接收数据速率                                         |
| SentBytes                                     | Bytes/s  | 发送数据速率                                         |
| RpcQueueTimeNumOps                            | 1/s      | RPC 调用速率                                         |
| RpcQueueTimeAvgTime                           | ms       | RPC 平均延迟时间                                     |
| RpcAuthenticationFailures                     | 次     | RPC 验证失败次数                                     |
| RpcAuthenticationSuccesses                    | 次     | RPC 验证成功次数                                     |
| RpcAuthorizationFailures                      | 次     | RPC 授权失败次数                                     |
| RpcAuthorizationSuccesses                     | 次     | RPC 授权成功次数                                     |
| NumOpenConnections                            | 个     | 当前链接数量                                         |
| CallQueueLength                               | 个     | 当前 RPC 处理队列长度                                |
| MemNonHeapUsedM                               | MB       | JVM 当前已经使用的 NonHeapMemory 的大小              |
| MemNonHeapCommittedM                          | MB       | JVM 内存                                             |
| MemHeapUsedM                                  | MB       | JVM 当前已经使用的 HeapMemory 的大小                 |
| MemHeapCommittedM                             | MB       | JVM HeapMemory 提交大小                              |
| MemHeapMaxM                                   | MB       | JVM 配置的 HeapMemory 的大小                         |
| MemMaxM                                       | MB       | JVM 运行时可以使用的最大内存大小               |
| BlockReportAvgTime                            | 次/s     | 每秒处理 DataNode Blcok 平均延迟                     |
| FGC                                           | 1/s      | Full GC 次数                                         |
| YGC                                           | 2/s      | Young GC 次数                                        |
| YGCT                                          | ms       | Young GC 消耗时间                                    |
| FGCT                                          | ms       | Full GC 消耗时间                                     |
| GCT                                           | ms       | 垃圾回收时间消耗                                     |
| ThreadsNew                                    | 个       | 处于新建状态的线程数量                               |
| ThreadsRunnable                               | 个       | 处于可运行状态的线程数量                             |
| ThreadsBlocked                                | 个       | 处于阻塞状态的线程数量                               |
| ThreadsWaiting                                | 个       | 处于 WAITING 状态的线程数量                          |
| ThreadsTimedWaiting                           | 个       | 处于 TIMED WAITING 状态的线程数量                    |
| ThreadsTerminated                             | 个       | 处于 Terminated 状态的线程数量                       |
| LogFatal                                      | 个       | Fatal 日志数量                                       |
| LogError                                      | 个       | Error 日志数量                                       |
| LogWarn                                       | 个       | Warn 日志数量                                        |
| LogInfo                                       | 个       | Info 日志数量                                        |
| S0                                            | %        | Survivor 0区内存使用占比                             |
| S1                                            | %        | Survivor 1区内存使用占比                             |
| E                                             | %        | Eden 区内存使用占比                                  |
| O                                             | %        | Old 区内存使用占比                                   |
| M                                             | %        | Metaspace 区内存使用占比                             |
| CCS                                           | %        | Compressed class space 区内存使用占比                |
| NumStaleStorages                              | 个       | 由于心跳延迟而标记为过期的 DataNodes 当前数目        |
| PendingDataNodeMessageCount                   | 个/s     | DATANODE 的请求被 QUEUE 在 standby namenode 中的个数 |
| NumberOfMissingBlocks                         | 个       | 缺失的数据块数量                                     |
| NumberOfMissingBlocksWithReplicationFactorOne | 个       | 缺失的数据库数量（rf = 1）                           |
| AllowSnapshotOps                              | 次/s     | 每秒执行 AllowSnapshot 操作的次数                    |
| DisallowSnapshotOps                           | 次/s     | 每秒执行 DisallowSnapshot 操作的次数                 |
| CreateSnapshotOps                             | 次/s     | 每秒执行 CreateSnapshot 操作的次数                   |
| DeleteSnapshotOps                             | 次/s     | 每秒执行 DeleteSnapshot 操作的次数                   |
| ListSnapshottableDirOps                       | 次/s     | 每秒执行 ListSnapshottableDir 操作次数               |
| SnapshotDiffReportOps                         | 次/s     | 每秒执行 SnapshotDiffReportOps 的次数                |
| RenameSnapshotOps                             | 次/s     | 每秒执行 RenameSnapshotOps 的次数                    |
| CreateFileOps                                 | 次/s     | 每秒执行 CreateFile 操作的次数                       |
| GetListingOps                                 | 次/s     | 每秒执行 GetListing 操作的次数                       |
| TotalFileOps                                  | 次/s     | 每秒执行 TotalFileOps 的次数                         |
| DeleteFileOps                                 | 次/s     | 每秒执行 DeleteFile 操作的次数                       |
| FileInfoOps                                   | 次/s     | 每秒执行 FileInfo 操作的次数                         |
| GetAdditionalDatanodeOps                      | 次/s     | 每秒执行 GetAdditionalDatanode 操作的次数            |
| CreateSymlinkOps                              | 次/s     | 每秒执行 CreateSymlink 操作的次数                    |
| GetLinkTargetOps                              | 次/s     | 每秒执行 GetLinkTarget 操作的次数                    |
| FilesInGetListingOps                          | 次/s     | 每秒执行 FilesInGetListing 操作的次数                |
| TransactionsNumOps                            | 次/s     | 每秒处理 Journal transaction 操作的次数              |
| TransactionsBatchedInSync                     | 次/s     | 每秒批量处理 Journal transaction 操作次数            |
| GetEditNumOps                                 | 次/s     | 每秒执行 GetEditNumOps 的次数                        |
| GetImageNumOps                                | 次/s     | 每秒执行 GetImageNumOps 的次数                       |
| PutImageNumOps                                | 次/s     | 每秒执行 PutImageNumOps 的次数                       |
| SyncsNumOps                                   | 次/s     | 每秒处理 Journal syncs 操作的次数                    |
| BlockReceivedAndDeletedOps                    | 次/s     | 每秒执行 BlockReceivedAndDeletedOps 的次数           |
| BlockOpsQueued                                | 次/s     | 处理 DataNode Block 上报操作的延迟                   |
| CacheReportNumOps                             | 次/s     | 每秒处理 CacheReport 操作的次数                      |
| BlockReportNumQps                             | 次/s     | 每秒处理 DataNode Blcok 上报操作的次数               |
| SyncsAvgTime                                  | ms       | 处理 Journal syncs 操作的平均延迟                    |
| CacheReportAvgTime                            | ms       | 缓存上报动作平均延迟                                 |
| GetEditAvgTime                                | ms       | 读取 Edit 文件操作平均延迟                           |
| GetImageAvgTime                               | ms       | 读取镜像文件平均延迟                                 |
| PutImageAvgTime                               | ms       | 写入镜像文件平均延迟                                 |
| TransactionsAvgTime                           | ms       | 处理 Journal transaction 操作的平均延迟              |
| StartTime                                     | ms       | 进程启动时间                                         |
| State                                         | 1        | NN 状态                                              |
| PeakThreadCount                               | 个       | 峰值线程数                                           |
| ThreadCount                                   | 个       | 线程数量                                             |
| DaemonThreadCount                             | 个       | 后台线程数量                                         |

### HDFS-DataNode

| 指标名称                                | 指标单位 | 指标含义                                   |
| --------------------------------------- | -------- | ------------------------------------------ |
| XceiverCount                            | 个       | Xceiver 数量                               |
| BytesWrittenMB                          | Bytes/s  | 写入 DN 的字节速率                         |
| BytesReadMB                             | Bytes/s  | 读取 DN 的字节速率                         |
| RemoteBytesReadMB                       | Bytes/s  | 远程客户端读取字节速率                     |
| RemoteBytesWrittenMB                    | Bytes/s  | 远程客户端写入字节速率                     |
| WritesFromRemoteClient                  | 个       | 来自远程客户端写操作 QPS                   |
| WritesFromLocalClient                   | 个       | 来自本地客户端写操作 OPS                   |
| ReadsFromRemoteClient                   | 个       | 来自远程客户端读操作 QPS                   |
| ReadsFromLocalClient                    | 个       | 来自本地客户端读操作 QPS                   |
| BlockVerificationFailures               | 次/s     | BLOCK 校验失败数量                         |
| VolumeFailures                          | 次/s     | 磁盘故障次数                               |
| DatanodeNetworkErrors                   | 次/s     | 网络错误统计                               |
| HeartbeatsAvgTime                       | ms       | 心跳接口平均时间                           |
| HeartbeatsNumOps                        | 次/s     | 心跳接口 QPS                               |
| SendDataPacketTransferNanosAvgTime      | ms       | 发送数据包平均时间                         |
| ReadBlockOpNumOps                       | 次/s     | 从 DataNode 读取 Block OPS                 |
| WriteBlockOpNumOps                      | 次/s     | 向 DataNode 写入 Block OPS                 |
| BlockChecksumOpNumOps                   | 次/s     | DataNode 进行 Checksum 操作的 OPS          |
| CopyBlockOpNumOps                       | 次/s     | 复制 Block 操作的 OPS                      |
| ReplaceBlockOpNumOps                    | 次/s     | Replace Block 操作的 OPS                   |
| BlockReportsNumOps                      | 次/s     | BLOCK 汇报动作的 OPS                       |
| IncrementalBlockReportsNumOps           | 次/s     | BLOCK 增量汇报的 OPS                       |
| CacheReportsNumOps                      | 次/s     | 缓存汇报的 OPS                             |
| PacketAckRoundTripTimeNanosNumOps       | 次/s     | 每秒处理 ACK ROUND TRIP 次数               |
| FlushNanosNumOps                        | 次/s     | 每秒处理 Flush 操作次数                    |
| ReadBlockOpAvgTime                      | ms       | 读取 Block 操作平均时间                    |
| WriteBlockOpAvgTime                     | ms       | 写 Blcok 操作平均时间                      |
| BlockChecksumOpAvgTime                  | ms       | 块校验操作平均时间                         |
| CopyBlockOpAvgTime                      | ms       | 复制块操作平均时间                         |
| ReplaceBlockOpAvgTime                   | ms       | Replace Block 操作平均时间                 |
| BlockReportsAvgTime                     | ms       | 块汇报平均时间                             |
| IncrementalBlockReportsAvgTime          | ms       | 增量块汇报平均时间                         |
| CacheReportsAvgTime                     | ms       | 缓存汇报平均时间                           |
| PacketAckRoundTripTimeNanosAvgTime      | ms       | 处理 ACK ROUND TRIP 平均时间               |
| FlushNanosAvgTime                       | ms       | Flush 操作平均时间                         |
| FsyncNanosAvgTime                       | ms       | Fsync 操作平均时间                         |
| RamDiskBlocksWrite                      | 块/s     | 写入内存的块的总数                         |
| RamDiskBlocksWriteFallback              | 块/s     | 写入内存但未成功的块总数（故障转移到磁盘） |
| RamDiskBlocksDeletedBeforeLazyPersisted | 块/s     | 应用程序在被保存到磁盘之前被删除的块的总数 |
| RamDiskBlocksReadHits                   | 块/s     | 内存中的块被读取的总次数                   |
| RamDiskBlocksEvicted                    | 块/s     | 内存中被清除的块总数                       |
| RamDiskBlocksEvictedWithoutRead         | 块/s     | 从内存中取出的内存块总数          |
| RamDiskBlocksLazyPersisted              | 块/s     | 惰性写入器写入磁盘的总数                   |
| RamDiskBytesLazyPersisted               | Bytes/s  | 由惰性写入器写入磁盘的总字节数             |
| RamDiskBytesWrite                       | Bytes/s  | 写入内存的总字节数                         |
| MemNonHeapUsedM                         | MB       | JVM 当前已经使用的 NonHeapMemory 的大小    |
| MemNonHeapCommittedM                    | MB       | JVM 配置的 NonHeapCommittedM 的大小        |
| MemHeapUsedM                            | MB       | JVM 当前已经使用的 HeapMemory 的大小       |
| MemHeapCommittedM                       | MB       | JVM HeapMemory 提交大小                    |
| MemHeapMaxM                             | MB       | JVM 配置的 HeapMemory 的大小               |
| MemMaxM                                 | MB       | JVM 运行时可以使用的最大内存大小     |
| ThreadsNew                              | 个       | 处于新建状态的线程数量                     |
| ThreadsRunnable                         | 个       | 处于可运行状态的线程数量                   |
| ThreadsBlocked                          | 个       | 处于阻塞状态的线程数量                     |
| ThreadsWaiting                          | 个       | 处于 WAITING 状态的线程数量                |
| ThreadsTimedWaiting                     | 个       | 处于 TIMED WAITING 状态的线程数量          |
| ThreadsTerminated                       | 个       | 处于 Terminated 状态的线程数量             |
| LogFatal                                | 个       | Fatal 日志数量                             |
| LogError                                | 个       | Error 日志数量                             |
| LogWarn                                 | 个       | Warn 日志数量                              |
| LogInfo                                 | 个       | Info 日志数量                              |
| S0                                      | %        | Survivor 0区内存使用占比                   |
| S1                                      | %        | Survivor 1区内存使用占比                   |
| E                                       | %        | Eden 区内存使用占比                        |
| O                                       | %        | Old 区内存使用占比                         |
| M                                       | %        | Metaspace 区内存使用占比                   |
| CCS                                     | %        | Compressed class space 区内存使用占比      |
| FGC                                     | 次       | Full GC 次数                               |
| YGC                                     | ms       | Young GC 次数                              |
| YGCT                                    | s        | Young GC 消耗时间                          |
| FGCT                                    | s        | Full GC 消耗时间                           |
| GCT                                     | s        | 垃圾回收时间消耗                           |
| ReceivedBytes                           | Bytes/s  | 接收数据速率                               |
| SentBytes                               | Bytes/s  | 发送数据速率                               |
| RpcQueueTimeNumOps                      | 次/s     | RPC 调用速率                               |
| RpcQueueTimeAvgTime                     | ms       | RPC 平均延迟时间                           |
| RpcAuthenticationFailures               | 次/s     | RPC 验证失败次数                           |
| RpcAuthenticationSuccesses              | 次/s     | RPC 验证成功次数                           |
| RpcAuthorizationFailures                | 次/s     | RPC 授权失败次数                           |
| RpcAuthorizationSuccesses               | 次/s     | RPC 授权成功次数                           |
| NumOpenConnections                      | 个       | 当前链接数量                               |
| CallQueueLength                         | 1        | 当前 RPC 处理队列长度                      |
| CurrentThreadSystemTime                 | ms       | 系统时间                                   |
| CurrentThreadUserTime                   | ms       | 用户时间                                   |
| StartTime                               | s        | 进程启动时间                               |
| PeckThreadCount                         | 个       | 峰值线程数量                               |
| DaemonThreadCount                       | 个       | 后台线程数量                               |
| write                                   | MB/s     | 磁盘写速率                                 |
| read                                    | 次/s     | 读操作 QPS                                 |
| FsyncNanosOps                           | 次/s     | Fsync 操作平均次数                         |
| DataPacketOps                           | 次/s     | 包传输操作 QPS                              |

### HDFS-Journal Node 

| 指标名称                   | 指标单位 | 指标含义                                |
| -------------------------- | -------- | --------------------------------------- |
| MemNonHeapUsedM            | MB       | JVM 当前已经使用的 NonHeapMemory 的大小 |
| MemNonHeapCommittedM       | MB       | JVM 内存                                |
| MemHeapUsedM               | MB       | JVM 当前已经使用的 HeapMemory 的大小    |
| MemHeapCommittedM          | MB       | JVM HeapMemory 提交大小                 |
| MemHeapMaxM                | MB       | JVM 配置的 HeapMemory 的大小            |
| MemMaxM                    | MB       | JVM 运行时可以使用的最大内存大小  |
| ThreadsNew                 | 个       | 处于新建状态的线程数量                  |
| ThreadsRunnable            | 个       | 处于可运行状态的线程数量                |
| ThreadsBlocked             | 个       | 处于阻塞状态的线程数量                  |
| ThreadsWaiting             | 个       | 处于 WAITING 状态的线程数量             |
| ThreadsTimedWaiting        | 个       | 处于 TIMED WAITING 状态的线程数量       |
| ThreadsTerminated          | 个       | 处于 Terminated 状态的线程数量          |
| LogFatal                   | 个       | Fatal 日志数量                          |
| LogError                   | 个       | Error 日志数量                          |
| LogWarn                    | 个       | Warn 日志数量                           |
| LogInfo                    | 个       | Info 日志数量                           |
| S0                         | %        | Survivor 0区内存使用占比                |
| S1                         | %        | Survivor 1区内存使用占比                |
| E                          | %        | Eden 区内存使用占比                     |
| O                          | %        | Old 区内存使用占比                      |
| M                          | %        | Metaspace 区内存使用占比                |
| CCS                        | %        | Compressed class space 区内存使用占比   |
| FGC                        | 次       | Full GC 次数                            |
| YGC                        | 次       | Young GC 次数                           |
| YGCT                       | s        | Young GC 消耗时间                       |
| FGCT                       | s        | Full GC 消耗时间                        |
| GCT                        | s        | 垃圾回收时间消耗                        |
| ReceivedBytes              | Bytes/s  | 接收数据速率                            |
| SentBytes                  | Bytes/s  | 发送数据速率                            |
| RpcQueueTimeNumOps         | 次/s     | RPC 调用速率                            |
| RpcQueueTimeAvgTime        | ms       | RPC 平均延迟时间                        |
| RpcAuthenticationFailures  | 次/s     | RPC 验证失败次数                        |
| RpcAuthenticationSuccesses | 次/s     | RPC 验证成功次数                        |
| RpcAuthorizationFailures   | 次/s     | RPC 授权失败次数                        |
| NumOpenConnections         | 个       | 当前链接数量                            |
| CallQueueLength            | 1        | 当前 RPC 处理队列长度                   |
| CurrentThreadSystemTime    | ms       | 系统时间                                |
| CurrentThreadUserTime      | ms       | 用户时间                                |
| StartTime                  | s        | 进程启动时间                            |
| ThreadCount                | 个       | 线程数量                                |
| PeckThreadCount            | 个       | 峰值线程数量                            |
| DaemonThreadCount          | 个       | 后台线程数量                            |

### HDFS-ZKFC

| 指标名称 | 指标单位 | 指标含义                              |
| -------- | -------- | ------------------------------------- |
| S0       | %        | Survivor 0区内存使用占比              |
| S1       | %        | Survivor 1区内存使用占比              |
| E        | %        | Eden 区内存使用占比                   |
| O        | %        | Old 区内存使用占比                    |
| M        | %        | Metaspace 区内存使用占比              |
| CCS      | %        | Compressed class space 区内存使用占比 |
| FGC      | 次       | Full GC 次数                          |
| YGC      | 次       | Young GC 次数                         |
| YGCT     | s        | Young GC 消耗时间                     |
| FGCT     | s        | Full GC 消耗时间                      |
| GCT      | s        | 垃圾回收时间消耗                      |
