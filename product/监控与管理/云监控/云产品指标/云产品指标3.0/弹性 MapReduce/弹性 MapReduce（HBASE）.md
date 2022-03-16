### 

## 命名空间

Namespace=QCE/TXMR_HBASE

## 监控指标

### Hbase-Overview

| 指标中文名                                                   | 指标中文名                                     | 指标单位 | 维度                                      |
| ------------------------------------------------------------ | ---------------------------------------------- | -------- | ----------------------------------------- |
| EmrHbaseOverview<br>HbaseMasterAssignment<br>managerRitRitcount | 集群处于 RITRegion 个数_ritCount               | 个       | host4hbaseoverview、<br>id4hbaseoverview  |
| EmrHbaseOverview<br/>HbaseMaster<br>Assignmentmanager<br>RitRitcountoverthreshold | 集群处于 RITRegion 个数_ritCountOverThreshold  | 个       | host4hbaseoverview、<br>id4hbaseoverview  |
| EmrHbaseOverview<br/>HbaseMaster<br>Assignmentmanager<br>TimeRitoldestage | 集群 RIT 时间_ritOldestAge                     | ms       | host4hbaseoverview、<br/>id4hbaseoverview |
| EmrHbaseOverview<br/>HbaseMaster<br>AvgloadAverageload       | 每个 RS 平均 REGION 数_averageLoad             | 个       | host4hbaseoverview、<br/>id4hbaseoverview |
| EmrHbaseOverview<br/>HbaseMasterRsnums<br>Numregionservers   | 集群 RS 数量_numRegionServers                  | 个       | host4hbaseoverview、<br/>id4hbaseoverview |
| EmrHbaseOverview<br/>HbaseMasterRsnumsNum<br>deadregionservers | 集群 RS 数量_numDeadRegionServers              | 个       | host4hbaseoverview、<br/>id4hbaseoverview |
| EmrHbaseOverview<br/>HbaseMaster<br>BytesReceivedbytes       | 集群读写数量_receivedBytes                     | B/s      | host4hbaseoverview、<br/>id4hbaseoverview |
| EmrHbaseOverview<br/>HbaseMaster<br>BytesSentbytes           | 集群读写数量_sentBytes                         | B/s      | host4hbaseoverview、<br/>id4hbaseoverview |
| EmrHbaseOverview<br/>HbaseMasterReq<br>Clusterrequests       | 集群总请求数量\_clusterRequests                | 个       | host4hbaseoverview、<br/>id4hbaseoverview |
| EmrHbaseOverview<br/>HbaseMaster<br>Assignmentmanager<br>OpsAssignNumOps | 集群 Assignment 管理器操作\_Assign_num_ops     | 次       | host4hbaseoverview、<br/>id4hbaseoverview |
| EmrHbaseOverview<br/>HbaseMaste<br>rAssignmentmanager<br>OpsBulkassignNumOps | 集群 Assignment 管理器操作\_BulkAssign_num_ops | 次       | host4hbaseoverview、<br/>id4hbaseoverview |
| EmrHbaseOverview<br/>HbaseMasterBalancerOps<br>BalancerclusterNumOps | 集群负载均衡次数\_BalancerclusterNum           | 次       | host4hbaseoverview、<br/>id4hbaseoverview |
| EmrHbaseOverview<br/>HbaseMasterServerPlan<br>Mergeplancount | 集群 Plan_mergePlanCount                       | 个       | host4hbaseoverview、<br/>id4hbaseoverview |
| EmrHbaseOverview<br/>HbaseMasterServerPlan<br>Splitplancount | 集群 Plan_splitPlanCount                       | 个       | host4hbaseoverview、<br/>id4hbaseoverview |

### Hbase-OverviewAggregation

| 指标中文名                                                   | 指标中文名                                     | 指标单位 | 维度             |
| ------------------------------------------------------------ | ---------------------------------------------- | -------- | ---------------- |
| EmrHbaseOverviewAggregation<br>HbaseMasterAssignment<br>managerRitRitcount | 集群处于 RITRegion 个数_ritCount               | 个       | id4hbaseoverview |
| EmrHbaseOverviewAggregation<br/>HbaseMasterAssign<br>mentmanagerRitRitcountover<br>threshold | 集群处于 RITRegion 个数_ritCountOverThreshold  | 个       | id4hbaseoverview |
| EmrHbaseOverviewAggregation<br/>HbaseMasterAssign<br>mentmanager TimeRitoldestage | 集群 RIT 时间_ritOldestAge                     | ms       | id4hbaseoverview |
| EmrHbaseOverviewAggregation<br/>HbaseMaster AvgloadAverageload | 每个 RS 平均REGION数_averageLoad               | 个       | id4hbaseoverview |
| EmrHbaseOverviewAggregation<br/>HbaseMasterRsnums<br>Numregionservers | 集群 RS 数量_numRegionServers                  | 个       | id4hbaseoverview |
| EmrHbaseOverviewAggregation<br/>HbaseMasterRsnumsNum <br>deadregionservers | 集群 RS 数量_numDeadRegionServers              | 个       | id4hbaseoverview |
| EmrHbaseOverviewAggregation<br/>HbaseMaster BytesReceivedbytes | 集群读写数量_receivedBytes                     | bytes/s  | id4hbaseoverview |
| EmrHbaseOverviewAggregation<br/>HbaseMaster<br>BytesSentbytes | 集群读写数量_sentBytes                         | bytes/s  | id4hbaseoverview |
| EmrHbaseOverviewAggregation<br/>HbaseMasterReq<br>Clusterrequests | 集群总请求数量_clusterRequests                 | 个/s     | id4hbaseoverview |
| EmrHbaseOverviewAggregation<br/>HbaseMasterAssign<br>mentmanagerOpsAssignNumOps | 集群 Assignment 管理器操作\_Assign_num_ops     | 次       | id4hbaseoverview |
| EmrHbaseOverviewAggregation<br/>HbaseMasterAssign<br/>mentmanagerOpsBulkassignNumOps | 集群 Assignment 管理器操作\_BulkAssign_num_ops | 次       | id4hbaseoverview |
| EmrHbaseOverviewAggregation<br/>HbaseMasterBalancerOps<br>BalancerclusterNumOps | 集群负载均衡次数\_BalancerclusterNum           | 次       | id4hbaseoverview |
| EmrHbaseOverviewAggregation<br/>HbaseMasterServerPlan<br>Mergeplancount | 集群 Plan_mergePlanCount                       | 个       | id4hbaseoverview |
| EmrHbaseOverviewAggregation<br/>HbaseMasterServerPlan<br>Splitplancount | 集群 Plan_splitPlanCount                       | 个       | id4hbaseoverview |

### HBASE-HMaster

| 指标中文名                                                 | 指标中文名                                 | 指标单位 | 维度                                |
| ---------------------------------------------------------- | ------------------------------------------ | -------- | ----------------------------------- |
| HbaseHmGcUtilGcCountFgc                                    | GC次数_FGC                                 | 次       | host4hbasehmaster、 id4hbasehmaster |
| HbaseHmGcUtilGcCounYgc                                     | GC次数_YGC                                 | 次       | host4hbasehmaster、 id4hbasehmaster |
| HbaseHmGcUtilGcTimeFgct                                    | GC时间_FGCT                                | s        | host4hbasehmaster、 id4hbasehmaster |
| HbaseHmGcUtilGcTimeGct                                     | GC时间_GCT                                 | s        | host4hbasehmaster、 id4hbasehmaster |
| HbaseHmGcUtilGcTimeYgct                                    | GC时间_YGCT                                | s        | host4hbasehmaster、 id4hbasehmaster |
| HbaseHmGcUtilMemoryCcs                                     | 内存区域占比_CCS                           | %        | host4hbasehmaster、 id4hbasehmaster |
| HbaseHmGcUtilMemoryE                                       | 内存区域占比_E                             | %        | host4hbasehmaster、 id4hbasehmaster |
| HbaseHmGcUtilMemoryM                                       | 内存区域占比_M                             | %        | host4hbasehmaster、 id4hbasehmaster |
| HbaseHmGcUtilMemoryO                                       | 内存区域占比_O                             | %        | host4hbasehmaster、 id4hbasehmaster |
| HbaseHmGcUtilMemoryS0                                      | 内存区域占比_S0                            | %        | host4hbasehmaster、 id4hbasehmaster |
| HbaseHmGcUtilMemoryS1                                      | 内存区域占比_S1                            | %        | host4hbasehmaster、 id4hbasehmaster |
| HbaseMasterIpcConnections<br>Numopenconnections            | RPC连接数_numOpenConnections               | 次       | host4hbasehmaster、 id4hbasehmaster |
| HbaseMasterIpcException<br/>Failedsanitycheckexception     | RPC异常次数_FailedSanityCheckException     | 次       | host4hbasehmaster、 id4hbasehmaster |
| HbaseMasterIpcException<br/>Notservingregionexception      | RPC异常次数_NotServingRegionException      | 次       | host4hbasehmaster、 id4hbasehmaster |
| HbaseMasterIpcException<br/>Outoforderscannernextexception | RPC异常次数_OutOfOrderScannerNextException | 次       | host4hbasehmaster、 id4hbasehmaster |
| HbaseMasterIpcException<br/>Regionmovedexception           | RPC异常次数_RegionMovedException           | 次       | host4hbasehmaster、 id4hbasehmaster |
| HbaseMasterIpcException<br/>Regiontoobusyexception         | RPC异常次数_RegionTooBusyException         | 次       | host4hbasehmaster、 id4hbasehmaster |
| HbaseMasterIpcException<br/>Unknownscannerexception        | RPC异常次数_UnknownScannerException        | 次       | host4hbasehmaster、 id4hbasehmaster |
| HbaseMasterIpcQueue<br/>Numcallsinpriorityqueue            | RPC队列请求数_numCallsInPriorityQueue      | 次       | host4hbasehmaster、 id4hbasehmaster |
| HbaseMasterIpcQueue<br/>Numcallsinreplicationqueue         | RPC队列请求数_numCallsInReplicationQueue   | 次       | host4hbasehmaster、 id4hbasehmaster |
| HbaseMasterJvm<br/>LogTotalLogerror                        | JVM日志数量_LogError                       | 个       | host4hbasehmaster、 id4hbasehmaster |
| HbaseMasterJvm<br/>LogTotalLogfatal                        | JVM日志数量_LogFatal                       | 个       | host4hbasehmaster、 id4hbasehmaster |
| HbaseMasterJvm<br/>LogTotalLoginfo                         | JVM日志数量_LogInfo                        | 个       | host4hbasehmaster、 id4hbasehmaster |
| HbaseMasterJvm<br/>LogTotalLogwarn                         | JVM日志数量_LogWarn                        | 个       | host4hbasehmaster、 id4hbasehmaster |
| HbaseMasterJvmMem<br/>Memheapcommittedm                    | JVM内存_MemHeapCommittedM                  | MB       | host4hbasehmaster、 id4hbasehmaster |
| HbaseMasterJvm<br/>MemMemheapmaxm                          | JVM内存_MemHeapMaxM                        | MB       | host4hbasehmaster、 id4hbasehmaster |
| HbaseMasterJvmMem<br/>Memheapusedm                         | JVM内存_MemHeapUsedM                       | MB       | host4hbasehmaster、 id4hbasehmaster |
| HbaseMasterJvmMemMemmaxm                                   | JVM内存_MemMaxM                            | MB       | host4hbasehmaster、 id4hbasehmaster |
| HbaseMasterJvmMem<br/>Memnonheapcommittedm                 | JVM内存_MemNonHeapCommittedM               | 个       | host4hbasehmaster、 id4hbasehmaster |
| HbaseMasterJvm<br/>MemMemnonheapusedm                      | JVM内存_MemNonHeapUsedM                    | 个       | host4hbasehmaster、 id4hbasehmaster |
| HbaseMasterJvm<br/>ThreadsThreadsblocked                   | JVM线程数量_ThreadsBlocked                 | 个       | host4hbasehmaster、 id4hbasehmaster |
| HbaseMasterJvm<br/>ThreadsThreadsnew                       | JVM线程数量_ThreadsNew                     | 个       | host4hbasehmaster、 id4hbasehmaster |
| HbaseMasterJvm<br/>ThreadsThreadsrunnable                  | JVM线程数量_ThreadsRunnable                | 个       | host4hbasehmaster、 id4hbasehmaster |
| HbaseMasterJvm<br/>ThreadsThreadsterminated                | JVM线程数量_ThreadsTerminated              | 个       | host4hbasehmaster、 id4hbasehmaster |
| HbaseMasterJvm<br/>ThreadsThreadstimedwaiting              | JVM线程数量_ThreadsTimedWaiting            | 个       | host4hbasehmaster、 id4hbasehmaster |
| HbaseMasterJvm<br/>ThreadsThreadswaiting                   | JVM线程数量_ThreadsWaiting                 | 个       | host4hbasehmaster、 id4hbasehmaster |
| HbaseMasterServer<br/>TimeMasteractivetime                 | 进程启动时间_masterActiveTime              | s        | host4hbasehmaster、 id4hbasehmaster |
| HbaseMasterServer<br/>TimeMasterstarttime                  | 进程启动时间_masterStartTime               | s        | host4hbasehmaster、 id4hbasehmaster |

### HBASE-RegionServer

| 指标英文名                                                   | 指标中文名                                         | 指标单位 | 维度                                   |
| ------------------------------------------------------------ | -------------------------------------------------- | -------- | -------------------------------------- |
| HbaseRegionserver<br>ScantimeMin                             | 最小ScanTime                                       | ms       | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserver<br/>ScansizeMin                            | 最小ScanSize                                       | 次       | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserver<br/>ScantimeMax                            | 最大ScanTime                                       | ms       | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserver<br/>ScansizeMax                            | 最大ScanSize                                       | 次       | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserver<br/>ServerCellsFlushedcellssize            | 写磁盘速率_flushedCellsSize                        | B/s      | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserver<br/>ServerIndexStorefileindexsize          | 索引大小_storeFileIndexSize                        | B        | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserver<br/>ServerIndexStaticindexsize             | 索引大小_staticIndexSize                           | B        | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserver<br/>ServerIndexStaticbloomsize             | 索引大小_staticBloomSize                           | B        | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserver<br/>ServerDelayUpdatesblockedtime          | 平均延时_updatesBlockedTime                        | ms       | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserver<br/>ServerDelayReplayMean                  | 平均延时_Replay_mean                               | ms       | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserver<br/>ServerDelayGetMean                     | 平均延时_Get_mean                                  | ms       | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserver<br/>ServerDelayAppendMean                  | 平均延时_Append_mean                               | ms       | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserver<br/>ScantimeMean                           | 平均ScanTime                                       | ms       | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserver<br/>ScansizeMean                           | 平均ScanSize                                       | 次       | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseHsGcUtilMemoryS1                                        | 内存区域占比_S1                                    | %        | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseHsGcUtilMemoryS0                                        | 内存区域占比_S0                                    | %        | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseHsGcUtilMemoryO                                         | 内存区域占比_O                                     | %        | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseHsGcUtilMemoryM                                         | 内存区域占比_M                                     | %        | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseHsGcUtilMemoryE                                         | 内存区域占比_E                                     | %        | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseHsGcUtilMemoryCcs                                       | 内存区域占比_CCS                                   | %        | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverServer<br/>SlowSlowputcount                 | 慢操作次数_slowPutCount                            | 次       | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverServer<br/>SlowSlowincrementcount           | 慢操作次数_slowIncrementCount                      | 次       | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverServer<br/>SlowSlowgetcount                 | 慢操作次数_slowGetCount                            | 次       | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverServer<br/>SlowSlowdeletecount              | 慢操作次数_slowDeleteCount                         | 次       | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverServer<br/>SlowSlowappendcount              | 慢操作次数_slowAppendCount                         | 次       | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverStarttime<br/>Regionserverstarttime         | 进程启动时间_regionServerStartTime                 | s        | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverServer<br/>BlockcacheCountBlockcachemisscount | 缓存块数量_blockCacheMissCount                     | 次       | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverServer<br/>BlockcacheCountBlockcachehitcount | 缓存块数量_blockCacheHitCount                      | 次       | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverServer<br/>BlockcacheCountBlockcachecount   | 缓存块数量_blockCacheCount                         | 次       | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverServer<br/>BlockcacheSizeBlockcachesize     | 缓存块内存占用大小_blockCacheSize                  | Bytes    | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserver<br/>ReqcountWrite                          | 读写请求量_Write                                   | 次       | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserver<br/>ReqcountTotal                          | 读写请求量_Total                                   | 次       | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserver<br/>ReqcountScantimeNumOps                 | 读写请求量_Scantime                                | 次       | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserver<br/>ReqcountScansizeNumOps                 | 读写请求量_Scansize                                | 次       | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverReqcountRead                                | 读写请求量_Read                                    | 次       | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserver<br/>ReqcountPutNumOps                      | 读写请求量_Put                                     | 次       | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserver<br/>ReqcountIncrementNumOps                | 读写请求量_Increment                               | 次       | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserver<br/>ReqcountGetNumOps                      | 读写请求量_Get                                     | 次       | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserver<br/>ReqcountDeleteNumOps                   | 读写请求量_Delete                                  | 次       | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserver<br/>ReqcountAppendNumOps                   | 读写请求量_Append_num_ops                          | 次       | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverIpc<br/>BytesSentbytes                      | 读写流量_sentBytes                                 | B/s      | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverIpc<br/>BytesReceivedbytes                  | 读写流量_receivedBytes                             | B/s      | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverServer<br/>BlockcachePercentBlockcacheexpresshi | 读缓存命中率_blockCacheExpressHitPercent           | %        | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverServer<br/>QueueSplitqueuelength            | 操作队列请求数_splitQueueLength                    | 个       | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverServer<br/>QueueFlushqueuelength            | 操作队列请求数_flushQueueLength                    | 个       | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverServer<br/>QueueCompactionqueuelength       | 操作队列请求数_compactionQueueLength               | 个       | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserver<br/>HlogcountHlogfilecount                 | WAL文件数量_hlogFileCount                          | 个       | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserver<br/>HlogsizeHlogfilesize                   | WAL文件大小_hlogFileSize                           | B        | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserver<br/>StoreCountStorecount                   | Store个数_storeCount                               | 个       | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserver<br/>StorefilecountStorefilecount           | Storefile个数_storeFileCount                       | 个       | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserver<br/>StorefilesizeStorefilesize             | Storefile大小_storeFileSize                        | MB       | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserver<br/>ServerSplitSplitsuccesscount           | split请求_splitSuccessCount                        | 个       | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserver<br/>ServerSplitSplitrequestcount           | split请求_splitRequestCount                        | 个       | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserver<br/>ServerFlushFlushtimeNumOps             | RS写磁盘次数_FlushTime_num_ops                     | 次       | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverIpc<br/>ExceptionUnknownscannerexception    | RPC异常次数_UnknownScannerException                | 次       | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverIpc<br/>ExceptionRegiontoobusyexception     | RPC异常次数_RegionTooBusyException                 | 次       | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverIpc<br/>ExceptionRegionmovedexception       | RPC异常次数_RegionMovedException                   | 次       | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverIpcException<br/>Outoforderscannernextexception | RPC异常次数_OutOfOrderScannerNextException         | 次       | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverIpcException<br/>Notservingregionexception  | RPC异常次数_NotServingRegionException              | 次       | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverIpcException<br/>Failedsanitycheckexception | RPC异常次数_FailedSanityCheckException             | 次       | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverIpc<br/>AuthenticationAuthenticationsuccesses | RPC认证次数_authenticationSuccesses                | 次       | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverIpc<br/>AuthenticationAuthenticationfailures | RPC认证次数_authenticationFailures                 | 次       | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverIpc<br/>ConnectionsNumopenconnections       | RPC连接数_numOpenConnections                       | 个       | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverIpc<br/>HandlerNumactivehandler             | RPC句柄数_numActiveHandler                         | 个       | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverIpc<br/>QueueNumcallsinreplicationqueue     | RPC队列请求数_numCallsInReplicationQueue           | 个       | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverIpc<br/>QueueNumcallsinpriorityqueue        | RPC队列请求数_numCallsInPriorityQueue              | 个       | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverIpc<br/>QueueNumcallsingeneralqueue         | RPC队列请求数_numCallsInGeneralQueue               | 个       | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserver<br/>ServerReplayReplayNumOps               | Replay操作次数_Replay_num_ops                      | 次       | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserver<br/>AvgsizeAverageregionsize               | Region平均大小_averageRegionSize                   | B        | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverRegion<br/>CountRegioncount                 | Region个数_regionCount                             | 个       | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverServerHfiles<br/>PercentPercentfileslocalsecond | Region副本本地化_percentFilesLocalSecondaryRegions | %        | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverServerMutation<br/>SizeMutationswithoutwalsize | mutation大小_mutationsWithoutWALSize               | B        | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverServerMutation<br/>CountMutationswithoutwalcoun | muation个数_mutationsWithoutWALCount               | 个       | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserver<br/>MemstroreMemstoresize                  | Memstore大小_memStoreSize                          | MBytes   | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserver<br/>JvmThreadsThreadswaiting               | JVM线程数量_ThreadsWaiting                         | 个       | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverJvm<br/>ThreadsThreadstimedwaiting          | JVM线程数量_ThreadsTimedWaiting                    | 个       | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverJvm<br/>ThreadsThreadsterminated            | JVM线程数量_ThreadsTerminated                      | 个       | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverJvm<br/>ThreadsThreadsrunnable              | JVM线程数量_ThreadsRunnable                        | 个       | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverJvm<br/>ThreadsThreadsnew                   | JVM线程数量_ThreadsNew                             | 个       | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverJvm<br/>ThreadsThreadsblocked               | JVM线程数量_ThreadsBlocked                         | 个       | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserver<br/>JvmLogTotalLogwarn                     | JVM日志数量_LogWarn                                | 个       | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserver<br/>JvmLogTotalLoginfo                     | JVM日志数量_LogInfo                                | 个       | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserver<br/>JvmLogTotalLogfatal                    | JVM日志数量_LogFatal                               | 个       | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserver<br/>JvmLogTotalLogerror                    | JVM日志数量_LogError                               | 个       | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverJvm<br/>MemMemnonheapusedm                  | JVM内存_MemNonHeapUsedM                            | MB       | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverJvm<br/>MemMemnonheapcommittedm             | JVM内存_MemNonHeapCommittedM                       | MB       | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverJvm<br/>MemMemmaxm                          | JVM内存_MemMaxM                                    | MB       | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverJvm<br/>MemMemheapusedm                     | JVM内存_MemHeapUsedM                               | MB       | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverJvm<br/>MemMemheapmaxm                      | JVM内存_MemHeapMaxM                                | MB       | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverJvm<br/>MemMemheapcommittedm                | JVM内存_MemHeapCommittedM                          | MB       | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseHsGcUtilGcTimeYgct                                      | GC时间_YGCT                                        | s        | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseHsGcUtilGcTimeGct                                       | GC时间_GCT                                         | s        | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseHsGcUtilGcTimeFgct                                      | GC时间_FGCT                                        | s        | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseHsGcUtilGcCountYgc                                      | GC次数_YGC                                         | 次       | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseHsGcUtilGcCountFgc                                      | GC次数_FGC                                         | 次       | host4hbasehmaster、<br>id4hbasehmaster |

## 各维度对应参数总览

| 参数名称                       | 维度名称               | 维度解释                     | 格式                                                         |
| :----------------------------- | :--------------------- | :--------------------------- | :----------------------------------------------------------- |
| Instances.N.Dimensions.0.Name  | id4hbaseoverview       | EMR 实例 ID 的维度名称       | 输入 String 类型维度名称：id4hbaseoverview                   |
| Instances.N.Dimensions.0.Value | id4hbaseoverview       | EMR 实例具体 ID              | 输入 EMR 具体实例 ID，例如 ：emr-mm8bs222                    |
| Instances.N.Dimensions.1.Name  | host4hbaseoverview     | EMR 实例中节点 IP 的维度名称 | 输入 String 类型维度名称：host4hbaseoverview                 |
| Instances.N.Dimensions.1.Value | host4hbaseoverview     | EMR 实例中具体节点 IP        | 输入具体节点  IP ，可从控制台获取，登录 [腾讯云 MapReduce 控制台](https://console.cloud.tencent.com/emr) > 单击实例 > 集群资源 > 资源管理 > 节点内网 IP。也可通过 [查询节点信息](https://cloud.tencent.com/document/product/589/41707) API 获取。 |
| Instances.N.Dimensions.0.Name  | id4hbasehmaster        | EMR 实例 ID 的维度名称       | 输入 String 类型维度名称：id4hbasehmaster                    |
| Instances.N.Dimensions.0.Value | id4hbasehmaster        | EMR 实例具体 ID              | 输入 EMR 具体实例 ID，例如 ：emr-mm8bs222                    |
| Instances.N.Dimensions.1.Name  | host4hbasehmaster      | EMR 实例中节点 IP 的维度名称 | 输入 String 类型维度名称：host4hbasehmaster                  |
| Instances.N.Dimensions.1.Value | host4hbasehmaster      | EMR 实例中具体节点 IP        | 输入具体节点  IP ，可从控制台获取，登录 [腾讯云 MapReduce 控制台](https://console.cloud.tencent.com/emr) > 单击实例 > 集群资源 > 资源管理 > 节点内网 IP。也可通过 [查询节点信息](https://cloud.tencent.com/document/product/589/41707) API 获取。 |
| Instances.N.Dimensions.0.Name  | id4hbaseregionserver   | EMR 实例 ID 的维度名称       | 输入 String 类型维度名称：id4hbaseregionserver               |
| Instances.N.Dimensions.0.Value | id4hbaseregionserver   | EMR 实例具体 ID              | 输入 EMR 具体实例 ID，例如 ：emr-mm8bs222                    |
| Instances.N.Dimensions.1.Name  | host4hbaseregionserver | EMR 实例中节点 IP 的维度名称 | 输入 String 类型维度名称：host4hbaseregionserver             |
| Instances.N.Dimensions.1.Value | host4hbaseregionserver | EMR 实例中具体节点 IP        | 输入具体节点  IP ，可从控制台获取，登录 [腾讯云 MapReduce 控制台](https://console.cloud.tencent.com/emr) > 单击实例 > 集群资源 > 资源管理 > 节点内网 IP。也可通过 [查询节点信息](https://cloud.tencent.com/document/product/589/41707) API 获取。 |





## 入参说明

弹性 MapReduce（HBASE）支持以下四种维度组合的查询方式，四种入参取值如下： 

**1. 查询  Hbase-OverviewAggregation  的指标监控数据，入参取值如下：**
&Namespace=QCE/TXMR_HBASE
&Instances.N.Dimensions.0.Name=id4hbaseoverview
&Instances.N.Dimensions.0.Value=EMR 实例 ID

**2. 查询 Hbase-Overview  的指标监控数据，入参取值如下：**
&Namespace=QCE/TXMR_HBASE
&Instances.N.Dimensions.0.Name=id4hbaseoverview
&Instances.N.Dimensions.0.Value=EMR 实例 ID 
&Instances.N.Dimensions.1.Name=host4hbaseoverview
&Instances.N.Dimensions.1.Value=EMR 实例中具体节点 IP

**3. 查询  HBASE-HMaster 的指标监控数据，入参取值如下：**
&Namespace=QCE/TXMR_HBASE
&Instances.N.Dimensions.0.Name=id4hbasehmaster
&Instances.N.Dimensions.0.Value=EMR 实例 ID 
&Instances.N.Dimensions.1.Name= host4hbasehmaster
&Instances.N.Dimensions.1.Value=EMR 实例中具体节点 IP

**4. 查询  HBASE-RegionServer  的指标监控数据，入参取值如下：**
&Namespace=QCE/TXMR_HBASE
&Instances.N.Dimensions.0.Name=id4hbaseregionserver 
&Instances.N.Dimensions.0.Value=EMR 实例 ID
&Instances.N.Dimensions.1.Name=host4hbaseregionserver
&Instances.N.Dimensions.1.Value=EMR 实例中具体节点 IP
