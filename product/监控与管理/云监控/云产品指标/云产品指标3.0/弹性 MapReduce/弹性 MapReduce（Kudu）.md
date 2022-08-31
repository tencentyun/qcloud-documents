## 命名空间

Namespace=QCE/TXMR_KUDU

## 监控指标

### KUDU-Master

| 指标英文名                                                   | 指标中文名                                   | 单位  | 维度                                   |
| ------------------------------------------------------------ | -------------------------------------------- | ----- | -------------------------------------- |
| KuduMasterAllocated<br/>BytesAllocatedbytes                  | 分配的字节_AllocatedBytes                    | Bytes | host4kudukudumaster、id4kudukudumaster |
| KuduMasterBlock<br/>CacheBlockcachehit                       | 块缓存命中_BlockCacheHit                     | 次    | host4kudukudumaster、id4kudukudumaster |
| KuduMasterBlock<br/>CacheBlockcachemiss                      | 块缓存命中_BlockCacheMiss                    | 次    | host4kudukudumaster、id4kudukudumaster |
| KuduMasterBlockCacheUsage<br/>Blockcacheusage                | 块缓存使用率_BlockCacheUsage                 | Bytes | host4kudukudumaster、id4kudukudumaster |
| KuduMasterBlockManager<br/>BlocksBlockopenreading            | 块管理器 block 数_BlockOpenReading             | 个    | host4kudukudumaster、id4kudukudumaster |
| KuduMasterBlockManager<br/>BlocksBlockopenwriting            | 块管理器 block 数_BlockOpenWriting             | 个    | host4kudukudumaster、id4kudukudumaster |
| KuduMasterBlockManager<br/>BlocksBlockundermanagement        | 块管理器 block 数_BlockUnderManagement         | 个    | host4kudukudumaster、id4kudukudumaster |
| KuduMasterBlockManager<br/>BytesBytesundermanagement         | 块管理器字节数_BytesUnderManagement          | Bytes | host4kudukudumaster、id4kudukudumaster |
| KuduMasterBlockManager<br>ContainerContainer<br/>sundermanagement | 块管理器容器数_ContainersUnderManagement     | 个    | host4kudukudumaster、id4kudukudumaster |
| KuduMasterClusterReplica<br/>SkewClusterreplicaskew          | tablet 副本差值_ClusterReplicaSkew            | 个    | host4kudukudumaster、id4kudukudumaster |
| KuduMasterContextSwitches<br/>Involuntaryswitches            | 上下文_InvoluntarySwitches                   | 次    | host4kudukudumaster、id4kudukudumaster |
| KuduMasterContextSwitches<br/>Voluntaryswitches              | 上下文_InvoluntarySwitches                   | 次    | host4kudukudumaster、id4kudukudumaster |
| KuduMasterCpuTimeCpustime                                    | CPU 时间_CPUStime                             | ms    | host4kudukudumaster、id4kudukudumaster |
| KuduMasterCpuTimeCpuutime                                    | CPU 时间_CPUUtime                             | ms    | host4kudukudumaster、id4kudukudumaster |
| KuduMasterDataDirDatadirsfailed                              | 数据路径_DataDirsFailed                      | 个    | host4kudukudumaster、id4kudukudumaster |
| KuduMasterDataDirDatadirsfull                                | 数据路径_DataDirsFull                        | 个    | host4kudukudumaster、id4kudukudumaster |
| KuduMasterFileCacheFilecachehit                              | 文件缓存命中_FileCacheHit                    | 个    | host4kudukudumaster、id4kudukudumaster |
| KuduMasterFileCacheFilecachemiss                             | 文件缓存命中_FileCacheMiss                   | 个    | host4kudukudumaster、id4kudukudumaster |
| KuduMasterFileCache<br/>UsageFilecacheusage                  | 文件缓存使用率_FileCacheUsage                | 个    | host4kudukudumaster、id4kudukudumaster |
| KuduMasterHybridClock<br/>ErrorHybridclockerror              | 混合时钟错误_HybridClockError                | us    | host4kudukudumaster、id4kudukudumaster |
| KuduMasterHybridClock<br/>TimestampHybridclocktimestamp      | 混合时钟时间戳_HybridClockTimestamp          | us    | host4kudukudumaster、id4kudukudumaster |
| KuduMasterLogMessages<br/>Errormessages                      | 日志信息_ErrorMessages                       | 个    | host4kudukudumaster、id4kudukudumaster |
| KuduMasterLogMessages<br/>Warningmessages                    | 日志信息_WarningMessages                     | 个    | host4kudukudumaster、id4kudukudumaster |
| KuduMasterNumRaft<br/>LeadersNumraftleaders                  | tablet leader 个数_NumRaftLeaders             | 个    | host4kudukudumaster、id4kudukudumaster |
| KuduMasterOpenSource<br/>SessionsOpemsourcesessions          | tablet_session 数_OpenSourceSessions          | 个    | host4kudukudumaster、id4kudukudumaster |
| KuduMasterOpApply<br/>QueueLengthMax                         | 队列中操作数_Max                             | 个    | host4kudukudumaster、id4kudukudumaster |
| KuduMasterOpApply<br/>QueueLengthMean                        | 队列中操作数_Mean                            | 个    | host4kudukudumaster、id4kudukudumaster |
| KuduMasterOpApply<br/>QueueLengthMin                         | 队列中操作数_Min                             | 个    | host4kudukudumaster、id4kudukudumaster |
| KuduMasterOpApply<br/>QueueLengthPercentile999               | 队列中操作数_Percentile_99_9                 | 个    | host4kudukudumaster、id4kudukudumaster |
| KuduMasterOpApply<br/>QueueLengthTotalcount                  | 队列中操作数_TotalCount                      | 个    | host4kudukudumaster、id4kudukudumaster |
| KuduMasterOpApply<br/>QueueTimeTotalcount                    | 排队等待时间_TotalCount                      | us    | host4kudukudumaster、id4kudukudumaster |
| KuduMasterOp<br/>ApplyRunTimeMax                             | 操作运行时间_Max                             | us    | host4kudukudumaster、id4kudukudumaster |
| KuduMasterOp<br/>ApplyRunTimeMean                            | 操作运行时间_Mean                            | us    | host4kudukudumaster、id4kudukudumaster |
| KuduMasterOp<br/>ApplyRunTimeMin                             | 操作运行时间_Min                             | us    | host4kudukudumaster、id4kudukudumaster |
| KuduMasterOpApplyRun<br/>TimePercentile999                   | 操作运行时间_Percentile_99_9                 | us    | host4kudukudumaster、id4kudukudumaster |
| KuduMasterOpApplyRun<br/>TimeTotalcount                      | 操作运行时间_TotalCount                      | us    | host4kudukudumaster、id4kudukudumaster |
| KuduMasterOp<br/>ApplyQueueTimeMax                           | 排队等待时间_Max                             | us    | host4kudukudumaster、id4kudukudumaster |
| KuduMasterOp<br/>ApplyQueueTimeMean                          | 排队等待时间_Mean                            | us    | host4kudukudumaster、id4kudukudumaster |
| KuduMasterOp<br/>ApplyQueueTimeMin                           | 排队等待时间_Min                             | us    | host4kudukudumaster、id4kudukudumaster |
| KuduMasterOpApplyQueue<br/>TimePercentile999                 | 排队等待时间_Percentile_99_9                 | us    | host4kudukudumaster、id4kudukudumaster |
| KuduMasterRpcConsensus<br/>serviceRunleaderelectionMax       | RPCRunLeader 选举_Max                         | us    | host4kudukudumaster、id4kudukudumaster |
| KuduMasterRpcConsensus<br/>serviceRunleaderelectionMean      | RPCRunLeader 选举_Mean                        | us    | host4kudukudumaster、id4kudukudumaster |
| KuduMasterRpcConsensus<br/>serviceRunleaderelectionMin       | RPCRunLeader 选举_Min                         | us    | host4kudukudumaster、id4kudukudumaster |
| KuduMasterRpcConnections<br/>Connectionsaccepted             | RPC 请求_ConnectionsAccepted                  | 个    | host4kudukudumaster、id4kudukudumaster |
| KuduMasterRpcConnections<br/>Queueoverflow                   | RPC 请求_QueueOverflow                        | 个    | host4kudukudumaster、id4kudukudumaster |
| KuduMasterRpcConnections<br/>Timesoutinqueue                 | RPC 请求_TimesOutInQueue                      | 个    | host4kudukudumaster、id4kudukudumaster |
| KuduMasterRpcConsensus<br/>serviceRunleaderelectionTotalcount | RPCRunLeader 选举_TotalCount                  | us    | host4kudukudumaster、id4kudukudumaster |
| KuduMasterRpcMasterservice<br/>ConnecttomasterMax            | RPC 连接 Master 服务_Max                        | us    | host4kudukudumaster、id4kudukudumaster |
| KuduMasterRpcMasterservice<br/>ConnecttomasterMean           | RPC 连接 Master 服务_Mean                       | us    | host4kudukudumaster、id4kudukudumaster |
| KuduMasterRpcMasterservice<br/>ConnecttomasterMin            | RPC 连接 Master 服务_Min                        | us    | host4kudukudumaster、id4kudukudumaster |
| KuduMasterRpcMasterservice<br/>ConnecttomasterPercentile999  | RPC 连接 Master 服务_Percentile_99_9            | us    | host4kudukudumaster、id4kudukudumaster |
| KuduMasterRpcMasterservice<br/>ConnecttomasterTotalcount     | RPC 连接 Master 服务_TotalCount                 | us    | host4kudukudumaster、id4kudukudumaster |
| KuduMasterRpc<br/>MasterservicePingMax                       | RPCPing 连接_Max                              | us    | host4kudukudumaster、id4kudukudumaster |
| KuduMasterRpcMaster<br/>servicePingMean                      | RPCPing 连接_Mean                             | us    | host4kudukudumaster、id4kudukudumaster |
| KuduMasterRpcMaster<br/>servicePingMin                       | RPCPing 连接_Min                              | us    | host4kudukudumaster、id4kudukudumaster |
| KuduMasterRpcMaster<br/>servicePingPercentile999             | RPCPing 连接_Percentile_99_9                  | us    | host4kudukudumaster、id4kudukudumaster |
| KuduMasterRpcMaster<br/>servicePingTotalcount                | RPCPing 连接_TotalCount                       | us    | host4kudukudumaster、id4kudukudumaster |
| KuduMasterRpcMaster<br/>serviceTsheartbeatMax                | TSHeartbeatRPC 请求所用微秒数_Max             | us    | host4kudukudumaster、id4kudukudumaster |
| KuduMasterRpcMaster<br/>serviceTsheartbeatMean               | TSHeartbeatRPC 请求所用微妙数_Mean            | us    | host4kudukudumaster、id4kudukudumaster |
| KuduMasterRpcMaster<br/>serviceTsheartbeatMin                | TSHeartbeatRPC 请求所用微妙数_Min             | us    | host4kudukudumaster、id4kudukudumaster |
| KuduMasterRpcMasterservice<br/>TsheartbeatPercentile999      | TSHeartbeatRPC 请求所用微妙数_Percentile_99_9 | us    | host4kudukudumaster、id4kudukudumaster |
| KuduMasterRpcTabletcopy<br/>serviceFetchdataMax              | FetchDataRPC 请求所用微秒数_Max               | us    | host4kudukudumaster、id4kudukudumaster |
| KuduMasterRpcTabletcopy<br/>serviceFetchdataMean             | FetchDataRPC 请求所用微秒数_Mean              | us    | host4kudukudumaster、id4kudukudumaster |
| KuduMasterRpcTablet<br/>copyserviceFetchdataMin              | FetchDataRPC 请求所用微秒数_Min               | us    | host4kudukudumaster、id4kudukudumaster |
| KuduMasterRpcTabletcopy<br/>serviceFetchdataPercentile999    | FetchDataRPC 请求所用微秒数_Percentile_99_9   | us    | host4kudukudumaster、id4kudukudumaster |
| KuduMasterRpcTabletcopy<br/>serviceFetchdataTotalcount       | FetchDataRPC 请求所用微秒数_TotalCount        | us    | host4kudukudumaster、id4kudukudumaster |
| KuduMasterSpinlockContention<br/>TimeSpinlockcontentiontime  | 自旋锁_SpinlockContentionTime                | us    | host4kudukudumaster、id4kudukudumaster |
| KuduMasterTcmallocMemory<br/>Currentthreadcachebytes         | TCMalloc 内存_CurrentThreadCacheBytes         | Bytes | host4kudukudumaster、id4kudukudumaster |
| KuduMasterTcmalloc<br/>MemoryHeapsize                        | TCMalloc 内存_HeapSize                        | Bytes | host4kudukudumaster、id4kudukudumaster |
| KuduMasterTcmallocMemory<br/>Totalthreadcachebytes           | TCMalloc 内存_TotalThreadCacheBytes           | Bytes | host4kudukudumaster、id4kudukudumaster |
| KuduMasterTcmalloc<br/>PageheapFreebytes                     | TCMallocPageHeap 内存_FreeBytes               | Bytes | host4kudukudumaster、id4kudukudumaster |
| KuduMasterTcmallocPage<br/>heapUnmappedbytes                 | TCMallocPageHeap 内存_UnMappedBytes           | Bytes | host4kudukudumaster、id4kudukudumaster |
| KuduMasterThreadThreadsrunning                               | 运行线程数_ThreadsRunning                    | 个    | host4kudukudumaster、id4kudukudumaster |

### KUDU-Server

| 指标英文名                                                   | 指标中文名                                        | 单位              | 维度                                   |
| ------------------------------------------------------------ | ------------------------------------------------- | ----------------- | -------------------------------------- |
| KuduServerAllocated<br/>BytesAllocatedbytes                  | 分配的字节_AllocatedBytes                         | Bytes             | host4kudukuduserver、id4kudukuduserver |
| KuduServerBlock<br/>CacheHitBlockcachehit                    | 块缓存命中_BlockCacheHit                          | 次             | host4kudukuduserver、id4kudukuduserver |
| KuduServerBlockCache<br/>HitBlockcachemiss                   | 块缓存命中_BlockCacheMiss                         | 次            | host4kudukuduserver、id4kudukuduserver |
| KuduServerBlockCache<br/>UsageBlockcacheusage                | 块缓存使用率_BlockCacheUsage                      | Bytes             | host4kudukuduserver、id4kudukuduserver |
| KuduServerBlockManager<br/>BlockBlockopenreading             | 块管理器 block 数_BlockOpenReading                  | 个                | host4kudukuduserver、id4kudukuduserver |
| KuduServerBlockManager<br/>BlockBlockopenwriting             | 块管理器 block 数_BlockOpenWriting                  | 个                | host4kudukuduserver、id4kudukuduserver |
| KuduServerBlockManager<br/>BlockBlockundermanagement         | 块管理器 block 数_BlockUnderManagement              | 个                | host4kudukuduserver、id4kudukuduserver |
| KuduServerBlockManager<br/>ByteBytesundermanagement          | 块管理器字节数_BytesUnderManagement               | Bytes             | host4kudukuduserver、id4kudukuduserver |
| KuduServerBlockManager<br/>ContainerContainer<br/>sundermanagement | 块管理器容器数_ContainersUnderManagement          | 个                | host4kudukuduserver、id4kudukuduserver |
| KuduServerContextSwitch<br/>Involuntaryswitches              | 上下文_InvoluntarySwitches                        | 次                | host4kudukuduserver、id4kudukuduserver |
| KuduServerContextSwitch<br/>Voluntaryswitches                | 上下文_VoluntarySwitches                          | 次                | host4kudukuduserver、id4kudukuduserver |
| KuduServerCpuTimeCpustime                                    | CPU 时间_CPUStime                                  | ms                | host4kudukuduserver、id4kudukuduserver |
| KuduServerCpuTimeCpuutime                                    | CPU 时间_CPUUtime                                  | ms                | host4kudukuduserver、id4kudukuduserver |
| KuduServerDataDirDatadirsfailed                              | 数据路径_DataDirsFailed                           | 个                | host4kudukuduserver、id4kudukuduserver |
| KuduServerDataDirDatadirsfull                                | 数据路径_DataDirsFull                             | 个                | host4kudukuduserver、id4kudukuduserver |
| KuduServerFileCacheHitFilecachehit                           | 文件缓存命中_FileCacheHit                         | 个                | host4kudukuduserver、id4kudukuduserver |
| KuduServerFileCacheHit<br/>Filecachemiss                     | 文件缓存命中_FileCacheMiss                        | 个                | host4kudukuduserver、id4kudukuduserver |
| KuduServerGlogMessages<br/>Errormessages                     | 日志信息_ErrorMessages                            | 个                | host4kudukuduserver、id4kudukuduserver |
| KuduServerGlogMessages<br/>Warningmessages                   | 日志信息_WarningMessages                          | 个                | host4kudukuduserver、id4kudukuduserver |
| KuduServerHybridClock<br/>ErrorHybridclockerror              | 混合时钟错误_HybridClockError                     | us                | host4kudukuduserver、id4kudukuduserver |
| KuduServerHybridClock<br/>TimestampHybridclocktimestamp      | 混合时钟时间戳_HybridClockTimestamp               | us                | host4kudukuduserver、id4kudukuduserver |
| KuduServerNumRaft<br/>LeadersNumraftleaders                  | tabletleader 个数_NumRaftLeaders                   | 个                | host4kudukuduserver、id4kudukuduserver |
| KuduServerOpApply<br/>QueueLengthMax                         | 队列中操作数_Max                                  | 个                | host4kudukuduserver、id4kudukuduserver |
| KuduServerOpApply<br/>QueueLengthMean                        | 队列中操作数_Mean                                 | 个                | host4kudukuduserver、id4kudukuduserver |
| KuduServerOpApply<br/>QueueLengthMin                         | 队列中操作数_Min                                  | 个                | host4kudukuduserver、id4kudukuduserver |
| KuduServerOpApplyQueue<br/>LengthPercentile999               | 队列中操作数_Percentile_99_9                      | 个                | host4kudukuduserver、id4kudukuduserver |
| KuduServerOpApplyQueue<br/>LengthTotalcount                  | 队列中操作数_TotalCount                           | 个                | host4kudukuduserver、id4kudukuduserver |
| KuduServerOpApply<br/>QueueTimeMean                          | 排队等待时间_Mean                                 | us                | host4kudukuduserver、id4kudukuduserver |
| KuduServerOpApply<br/>QueueTimeMin                           | 排队等待时间_Min                                  | us                | host4kudukuduserver、id4kudukuduserver |
| KuduServerOpApply<br/>QueueTimePercentile999                 | 排队等待时间_Percentile_99_9                      | us                | host4kudukuduserver、id4kudukuduserver |
| KuduServerOpApply<br/>QueueTimeTotalcount                    | 排队等待时间_TotalCount                           | us                | host4kudukuduserver、id4kudukuduserver |
| KuduServerOpApplyRunTimeMax                                  | 操作运行时间_Max                                  | us                | host4kudukuduserver、id4kudukuduserver |
| KuduServerOpApplyRunTimeMean                                 | 操作运行时间_Mean                                 | us                | host4kudukuduserver、id4kudukuduserver |
| KuduServerOpApplyRunTimeMin                                  | 操作运行时间_Min                                  | us                | host4kudukuduserver、id4kudukuduserver |
| KuduServerOpApplyRun<br/>TimePercentile999                   | 操作运行时间_Percentile_99_9                      | us                | host4kudukuduserver、id4kudukuduserver |
| KuduServerOpApplyRun<br/>TimeTotalcount                      | 操作运行时间_TotalCount                           | us                | host4kudukuduserver、id4kudukuduserver |
| KuduServerRpcRequest<br/>Connectionsaccepted                 | RPC 请求_ConnectionsAccepted                       | 次                | host4kudukuduserver、id4kudukuduserver |
| KuduServerRpcRequest<br/>Queueoverflow                       | RPC 请求_QueueOverflow                             | 次                | host4kudukuduserver、id4kudukuduserver |
| KuduServerRpcRequest<br/>Timesoutinqueue                     | RPC 请求_TimesOutInQueue                           | 次                | host4kudukuduserver、id4kudukuduserver |
| KuduServerRpcTabletadmin<br/>serviceAlterschemaMax           | AlterSchemaRPC 请求所用微秒数_Max                  | us                | host4kudukuduserver、id4kudukuduserver |
| KuduServerRpcTabletadmin<br/>serviceAlterschemaMean          | AlterSchemaRPC 请求所用微秒数_Mean                 | us                | host4kudukuduserver、id4kudukuduserver |
| KuduServerRpcTabletadmin<br/>serviceAlterschemaMin           | AlterSchemaRPC 请求所用微秒数_Min                  | us                | host4kudukuduserver、id4kudukuduserver |
| KuduServerRpcTabletadmin<br/>serviceAlterschemaPercentile999 | AlterSchemaRPC 请求所用微秒数_Percentile_99_9      | us                | host4kudukuduserver、id4kudukuduserver |
| KuduServerRpcTabletadmin<br/>serviceAlterschemaTotalcount    | AlterSchemaRPC 请求所用微秒数_TotalCount           | us                | host4kudukuduserver、id4kudukuduserver |
| KuduServerRpcTabletadmin<br/>serviceCreatetabletMax          | CreateTabletRPC 请求所用微秒数_Max                 | us                | host4kudukuduserver、id4kudukuduserver |
| KuduServerRpcTabletadmin<br/>serviceCreatetabletMean         | CreateTabletRPC 请求所用微秒数_Mean                | us                | host4kudukuduserver、id4kudukuduserver |
| KuduServerRpcTabletadmin<br/>serviceCreatetabletMin          | CreateTabletRPC 请求所用微秒数_Min                 | us                | host4kudukuduserver、id4kudukuduserver |
| KuduServerRpcTabletadmin<br/>serviceCreatetabletPercentile999 | CreateTabletRPC 请求所用微秒数_Percentile_99_9     | us                | host4kudukuduserver、id4kudukuduserver |
| KuduServerRpcTabletadmin<br/>serviceCreatetabletTotalcount   | CreateTabletRPC 请求所用微秒数_TotalCount          | us                | host4kudukuduserver、id4kudukuduserver |
| KuduServerRpcTabletadmin<br/>serviceDeletetabletMax          | DeleteTabletRPC 请求所用微秒数_Max                 | us                | host4kudukuduserver、id4kudukuduserver |
| KuduServerRpcTabletadmin<br/>serviceDeletetabletMin          | DeleteTabletRPC 请求所用微秒数_Min                 | us                | host4kudukuduserver、id4kudukuduserver |
| KuduServerRpcTabletadmin<br/>serviceDeletetabletMean         | DeleteTabletRPC 请求所用微秒数_Mean                | us                | host4kudukuduserver、id4kudukuduserver |
| KuduServerRpcTabletadmin<br/>serviceDeletetabletPercentile999 | DeleteTabletRPC 请求所用微秒数_Percentile_99_9     | us                | host4kudukuduserver、id4kudukuduserver |
| KuduServerRpcTabletadmin<br/>serviceDeletetabletTotalcount   | DeleteTabletRPC 请求所用微秒数_TotalCount          | us                | host4kudukuduserver、id4kudukuduserver |
| KuduServerRpcTabletadmin<br/>serviceQuiesceMax               | QuiesceRPC 请求所用微秒数_Max                      | us                | host4kudukuduserver、id4kudukuduserver |
| KuduServerRpcTabletadmin<br/>serviceQuiesceMean              | QuiesceRPC 请求所用微秒数_Mean                     | us                | host4kudukuduserver、id4kudukuduserver |
| KuduServerRpcTabletadmin<br/>serviceQuiesceMin               | QuiesceRPC 请求所用微秒数_Min                      | us                | host4kudukuduserver、id4kudukuduserver |
| KuduServerRpcTabletadmin<br/>serviceQuiescePercentile999     | QuiesceRPC 请求所用微秒数_Percentile_99_9          | us                | host4kudukuduserver、id4kudukuduserver |
| KuduServerRpcTabletadmin<br/>serviceQuiesceTotalcount        | QuiesceRPC 请求所用微秒数_TotalCount               | us                | host4kudukuduserver、id4kudukuduserver |
| KuduServerRpcTablet<br/>copyFetchdataMax                     | FetchDataRPC 请求所用微秒数_Max                    | us                | host4kudukuduserver、id4kudukuduserver |
| KuduServerRpcTablet<br/>copyFetchdataMean                    | FetchDataRPC 请求所用微秒数_Mean                   | us                | host4kudukuduserver、id4kudukuduserver |
| KuduServerRpcTablet<br/>copyFetchdataMin                     | FetchDataRPC 请求所用微秒数_Min                    | us                | host4kudukuduserver、id4kudukuduserver |
| KuduServerRpcTabletcopy<br/>FetchdataPercentile999           | FetchDataRPC 请求所用微秒数_Percentile_99_9        | us                | host4kudukuduserver、id4kudukuduserver |
| KuduServerRpcTabletcopy<br/>FetchdataTotalcount              | FetchDataRPC 请求所用微秒数_TotalCount             | us                | host4kudukuduserver、id4kudukuduserver |
| KuduServerRpcTabletserver<br/>ScannerkeepaliveMax            | ScannerKeepAliveRPC 请求所用微秒数_Max             | us                | host4kudukuduserver、id4kudukuduserver |
| KuduServerRpcTabletserver<br/>ScannerkeepaliveMean           | ScannerKeepAliveRPC 请求所用微秒数_Mean            | us                | host4kudukuduserver、id4kudukuduserver |
| KuduServerRpcTabletserver<br/>ScannerkeepaliveMin            | ScannerKeepAliveRPC 请求所用微秒数_Min             | us                | host4kudukuduserver、id4kudukuduserver |
| KuduServerRpcTabletserver<br/>ScannerkeepalivePercentile999  | ScannerKeepAliveRPC 请求所用微秒数_Percentile_99_9 | us                | host4kudukuduserver、id4kudukuduserver |
| KuduServerRpcTabletserver<br/>ScannerkeepaliveTotalcount     | ScannerKeepAliveRPC 请求所用微秒数_TotalCount      | us                | host4kudukuduserver、id4kudukuduserver |
| KuduServerRpcTablet<br/>serverScanMax                        | ScanRPC 请求所用微秒数_Max                         | us                | host4kudukuduserver、id4kudukuduserver |
| KuduServerRpcTablet<br/>serverScanMean                       | ScanRPC 请求所用微秒数_Mean                        | us                | host4kudukuduserver、id4kudukuduserver |
| KuduServerRpcTablet<br/>serverScanMin                        | ScanRPC 请求所用微秒数_Min                         | us                | host4kudukuduserver、id4kudukuduserver |
| KuduServerRpcTabletserver<br/>ScanPercentile999              | ScanRPC 请求所用微秒数_Percentile_99_9             | us                | host4kudukuduserver、id4kudukuduserver |
| KuduServerRpcTabletserver<br/>ScanTotalcount                 | ScanRPC 请求所用微秒数_TotalCount                  | us                | host4kudukuduserver、id4kudukuduserver |
| KuduServerRpcTablet<br/>serverWriteMax                       | WriteRPC 请求所用微秒数_Max                        | us                | host4kudukuduserver、id4kudukuduserver |
| KuduServerRpcTablet<br/>serverWriteMean                      | WriteRPC 请求所用微秒数_Mean                       | us                | host4kudukuduserver、id4kudukuduserver |
| KuduServerRpcTablet<br/>serverWriteMin                       | WriteRPC 请求所用微秒数_Min                        | us                | host4kudukuduserver、id4kudukuduserver |
| KuduServerRpcTabletserver<br/>WritePercentile999             | WriteRPC 请求所用微秒数_Percentile_99_9            | us                | host4kudukuduserver、id4kudukuduserver |
| KuduServerRpcTabletserver<br/>WriteTotalcount                | WriteRPC 请求所用微秒数_TotalCount                 | us                | host4kudukuduserver、id4kudukuduserver |
| KuduServerScannerActivescanners                              | Scanner 数量_ActiveScanners                        | 个                | host4kudukuduserver、id4kudukuduserver |
| KuduServerScannerExpiredscanners                             | Scanner 数量_ExpiredScanners                       | 个                | host4kudukuduserver、id4kudukuduserver |
| KuduServerSpinlockContention<br/>TimeSpinlockcontentiontime  | 自旋锁_SpinlockContentionTime                     | us                | host4kudukuduserver、id4kudukuduserver |
| KuduServerTabletSession<br/>Opemsourcesessions               | tabletsession 数_OpenSourceSessions                | 个                | host4kudukuduserver、id4kudukuduserver |
| KuduServerTabletSession<br/>Openclientsessions               | tabletsession 数_OpenClientSessions                | 个                | host4kudukuduserver、id4kudukuduserver |
| KuduServerTablet<br/>Tabletbootstrapping                     | tablet 数_TabletBootstrapping                      | 个                | host4kudukuduserver、id4kudukuduserver |
| KuduServer<br/>TabletTabletfailed                            | tablet 数_TabletFailed                             | 个                | host4kudukuduserver、id4kudukuduserver |
| KuduServer<br/>TabletTabletinitialized                       | tablet 数_TabletInitialized                        | 个                | host4kudukuduserver、id4kudukuduserver |
| KuduServer<br/>TabletTabletnotinitialized                    | tablet 数_TabletNotInitialized                     | 个                | host4kudukuduserver、id4kudukuduserver |
| KuduServer<br/>TabletTabletrunning                           | tablet 数_TabletRunning                            | 个                | host4kudukuduserver、id4kudukuduserver |
| KuduServer<br/>TabletTabletshutdown                          | tablet 数_TabletShutdown                           | 个                | host4kudukuduserver、id4kudukuduserver |
| KuduServer<br/>TabletTabletstopped                           | tablet 数_ TabletStopped                           | 个                | host4kudukuduserver、id4kudukuduserver |
| KuduServer<br/>TabletTabletstopping                          | tablet 数_TabletStopping                           | 个                | host4kudukuduserver、id4kudukuduserver |
| KuduServerTcmallocMemory<br/>Currentthreadcachebytes         | TCMalloc 内存_CurrentThreadCacheBytes              | Bytes             | host4kudukuduserver、id4kudukuduserver |
| KuduServerTcmalloc<br/>MemoryHeapsize                        | TCMalloc 内存_HeapSize                             | Bytes             | host4kudukuduserver、id4kudukuduserver |
| KuduServerTcmallocMemory<br/>Totalthreadcachebytes           | TCMalloc 内存_TotalThreadCacheBytes                | Bytes             | host4kudukuduserver、id4kudukuduserver |
| KuduServerTcmalloc<br/>PageheapFreebytes                     | TCMallocPageHeap 内存_FreeBytes                    | Bytes             | host4kudukuduserver、id4kudukuduserver |
| KuduServerTcmalloc<br/>PageheapUnmappedbytes                 | TCMallocPageHeap 内存_UnMappedBytes                | Bytes             | host4kudukuduserver、id4kudukuduserver |
| KuduServerThread<br/>Threadsrunning                          | 运行线程_ThreadsRunning                           | 个                | host4kudukuduserver、id4kudukuduserver |
| KuduMasterRpcMasterservice<br/>TsheartbeatTotalcount         | TSHeartbeatRPC 请求所用微秒数_TotalCount           | us                | host4kudukuduserver、id4kudukuduserver |
| KuduServerOpApply<br/>QueueTimeMax                           | 排队等待时间_Max                                  | us                | host4kudukuduserver、id4kudukuduserver |
| KuduServerFileCache<br/>UsageFilecacheusage                  | 文件缓存中的条目数                                | 个                | host4kudukuduserver、id4kudukuduserver |
| KuduServerOpApply<br/>Queueoverloadrejections                | 队列过载拒写数                                    | 个                | host4kudukuduserver、id4kudukuduserver |
| KuduServerScannerBytes<br/>RateScannedfromdiskrate           | scanner 速率_ScannedFromDiskRate                   | Bytes/s           | host4kudukuduserver、id4kudukuduserver |
| KuduServerScannerBytesRate<br/>Scannerreturnedrate           | scanner 速率_ScannerReturnedRate                   | Bytes/s           | host4kudukuduserver、id4kudukuduserver |
| KuduServerScannerBytes<br/>TotalScannedfromdisk              | scanner 总量_ScannedFromDisk                       | 字节数(Bytes)     | host4kudukuduserver、id4kudukuduserver |
| KuduServerScannerBytes<br/>TotalScannerreturned              | scanner 总量_ScannerReturned                       | 字节数(Bytes)     | host4kudukuduserver、id4kudukuduserver |
| KuduServerRowsTotal<br/>CountRowsinserted                    | 行操作总量_RowsInserted                           | 次数总和(Count)   | host4kudukuduserver、id4kudukuduserver |
| KuduServerRowsTotal<br/>CountRowsdeleted                     | 行操作总量_RowsDeleted                            | 次数总和(Count)   | host4kudukuduserver、id4kudukuduserver |
| KuduServerRowsTotal<br/>CountRowsupserted                    | 行操作总量_RowsUpserted                           | 次数总和(Count)   | host4kudukuduserver、id4kudukuduserver |
| KuduServerRowsTotal<br/>CountRowsupdated                     | 行操作总量_RowsUpdated                            | 次数总和(Count)   | host4kudukuduserver、id4kudukuduserver |
| KuduServerRowsTotal<br/>RateRowsinsertedrate                 | 行操作速率_RowsInsertedRate                       | 每秒次数(Count/s) | host4kudukuduserver、id4kudukuduserver |
| KuduServerRowsTotal<br/>RateRowsdeletedrate                  | 行操作速率_RowsDeletedRate                        | 每秒次数(Count/s) | host4kudukuduserver、id4kudukuduserver |
| KuduServerRowsTotal<br/>RateRowsupsertedrate                 | 行操作速率_RowsUpsertedRate                       | 每秒次数(Count/s) | host4kudukuduserver、id4kudukuduserver |
| KuduServerRowsTotal<br/>RateRowsupdatedrate                  | 行操作速率_RowsUpdatedRate                        | 每秒次数(Count/s) | host4kudukuduserver、id4kudukuduserver |

## 各维度对应参数总览

| 参数名称                       | 维度名称            | 维度解释                     | 格式                                                         |
| :----------------------------- | :------------------ | :--------------------------- | :----------------------------------------------------------- |
| Instances.N.Dimensions.0.Name  | host4kudukudumaster | EMR 实例中节点 IP 的维度名称 | 输入 String 类型维度名称：host4kudukudumaster                |
| Instances.N.Dimensions.0.Value | host4kudukudumaster | EMR 实例中具体节点 IP        | 输入具体节点  IP ，可从控制台获取，登录<b> [腾讯云 MapReduce 控制台](https://console.cloud.tencent.com/emr) > 单击实例 > 集群资源 > 资源管理 > 节点内网 IP</b>。也可通过 [查询节点信息](https://cloud.tencent.com/document/product/589/41707) API 获取。 |
| Instances.N.Dimensions.1.Name  | id4kudukudumaster   | EMR 实例 ID 的维度名称       | 输入 String 类型维度名称：id4kudukudumaster                  |
| Instances.N.Dimensions.1.Value | id4kudukudumaster   | EMR 实例中节点 IP 的维度名称 | 输入 EMR 具体实例 ID，例如：emr-mm8bs222                     |
| Instances.N.Dimensions.0.Name  | host4kudukuduserver | EMR 实例 ID 的维度名称       | 输入 String 类型维度名称：host4kudukuduserver                |
| Instances.N.Dimensions.0.Value | host4kudukuduserver | EMR 实例具体 ID              | 输入具体节点  IP ，可从控制台获取，登录<b> [腾讯云 MapReduce 控制台](https://console.cloud.tencent.com/emr) > 单击实例 > 集群资源 > 资源管理 > 节点内网 IP</b>。也可通过 [查询节点信息](https://cloud.tencent.com/document/product/589/41707) API 获取。 |
| Instances.N.Dimensions.1.Name  | id4kudukuduserver   | EMR 实例 ID 的维度名称       | 输入 String 类型维度名称：id4kudukuduserver                  |
| Instances.N.Dimensions.1.Value | id4kudukuduserver   | EMR 实例 ID 的维度名称       | 输入 EMR 具体实例 ID，例如：emr-mm8bs222                     |

## 入参说明

#### 查询弹性 MapReduce（KUDU-Master）监控数据，入参取值如下：

Namespace=QCE/TXMR_KUDU
&Instances.N.Dimensions.0.Name=host4kudukudumaster
&Instances.N.Dimensions.0.Value=EMR 实例中具体节点 IP
&Instances.N.Dimensions.1.Name=id4kudukudumaster
&Instances.N.Dimensions.1.Value=EMR 实例 ID 



#### 查询弹性 MapReduce（KUDU-Server）监控数据，入参取值如下：

Namespace=QCE/TXMR_KUDU
&Instances.N.Dimensions.0.Name=host4kudukuduserver
&Instances.N.Dimensions.0.Value=EMR 实例中具体节点 IP
&Instances.N.Dimensions.1.Name=id4kudukuduserver
&Instances.N.Dimensions.1.Value=EMR 实例 ID 



