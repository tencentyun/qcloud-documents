## 命名空间

Namespace=QCE/TXMR_HBASE

## 监控指标

| 指标英文名                                                   | 指标中文名                                   | 指标单位 | 指标含义                                        | 维度                                      |
| ------------------------------------------------------------ | -------------------------------------------- | -------- | ----------------------------------------------- | ----------------------------------------- |
| EmrHbaseOverviewHbase<br/>MasterRsnumsNumregionservers       | 集群RS数量_numRegionServers                  | 个       | 当前存活的 RegionServer 个数                    | host4hbaseoverview、<br/>id4hbaseoverview |
| EmrHbaseOverviewHbase<br/>MasterRsnumsNumdeadregionservers   | 集群RS数量_numDeadRegionServers              | 个       | 当前Dead的 RegionServer 个数                    | host4hbaseoverview、<br/>id4hbaseoverview |
| EmrHbaseOverviewHbase<br/>MasterReqClusterrequests           | 集群接口总请求量_clusterRequests             | 个       | 集群总请求数量                                  | host4hbaseoverview、<br/>id4hbaseoverview |
| EmrHbaseOverviewHbase<br/>MasterBytesSentbytes               | 集群读写数量_sentBytes                       | b/s      | 集群发送数据量                                  | host4hbaseoverview、<br/>id4hbaseoverview |
| EmrHbaseOverviewHbase<br/>MasterBytesReceivedbytes           | 集群读写数量_receivedBytes                   | b/s      | 集群接收数据量                                  | host4hbaseoverview、<br/>id4hbaseoverview |
| EmrHbaseOverviewHbaseMaster<br/>BalancerOpsBalancerclusterNumOps | 集群负载均衡次数_BalancerCluster_num_ops     | 次       | 集群负载均衡次数                                | host4hbaseoverview、<br/>id4hbaseoverview |
| EmrHbaseOverviewHbaseMaster<br/>AvgloadAverageload           | 每个RS平均REGION数_averageLoad               | 个       | 每个 ResgionServer 平均 Region 数               | host4hbaseoverview、<br/>id4hbaseoverview |
| EmrHbaseOverviewHbaseMaster<br/>AssignmentmanagerTimeRitoldestage | 集群RIT时间_ritOldestAge                     | ms       | Region in transition 的最老年龄                 | host4hbaseoverview、<br/>id4hbaseoverview |
| EmrHbaseOverviewHbaseMaster<br/>AssignmentmanagerRitRitcountoverthreshold | 集群处于RIT Region个数_ritCountOverThreshold | 个       | Region in transition 时间超过阈值的 Region 个数 | host4hbaseoverview、<br/>id4hbaseoverview |
| EmrHbaseOverviewHbaseMaster<br/>AssignmentmanagerRitRitcount | 集群处于RIT Region个数_ritCount              | 个       | Region in transition 的个数                     | host4hbaseoverview、<br/>id4hbaseoverview |
| EmrHbaseOverviewHbaseMaster<br/>AssignmentmanagerOpsBulkassignNumOps | 集群Assignment管理器操作_BulkAssign_num_ops  | 次       | Bulk assign region次数                          | host4hbaseoverview、<br/>id4hbaseoverview |
| EmrHbaseOverviewHbaseMaster<br/>AssignmentmanagerOpsAssignNumOps | 集群Assignment管理器操作_Assign_num_ops      | 次       | Assign region次数                               | host4hbaseoverview、<br/>id4hbaseoverview |



### Hbase-OverviewAggregation

| 指标英文名                                                   | 指标中文名                                   | 单位 | 指标含义                                         | 维度             |
| ------------------------------------------------------------ | -------------------------------------------- | ---- | ------------------------------------------------ | ---------------- |
| EmrHbaseOverviewAggregationHbaseMaster<br/>AssignmentmanagerOpsBulkassignNumOps | 集群Assignment管理器操作_BulkAssign_num_ops  | 次   | Bulk assign region次数                           | id4hbaseoverview |
| EmrHbaseOverviewAggregationHbaseMaster<br/>AssignmentmanagerRitRitcountoverthreshold | 集群处于RIT_Region个数_ritCountOverThreshold | 个   | Region in transition 时间超过阈值的  Region 个数 | id4hbaseoverview |
| EmrHbaseOverviewAggregation<br/>HbaseMasterBytesSentbytes    | 集群读写数量_sentBytes                       | B/s  | 集群发送数据量                                   | id4hbaseoverview |
| EmrHbaseOverviewAggregationHbase<br/>MasterAssignmentmanagerRitRitcount | 集群处于RIT_Region个数_ritCount              | 个   | Region in transition 的个数                      | id4hbaseoverview |
| EmrHbaseOverviewAggregationHbase<br/>MasterRsnumsNumregionservers | 集群RS数量_numRegionServers                  | 个   | 当前存活的 RegionServer 个数                     | id4hbaseoverview |
| EmrHbaseOverviewAggregation<br/>HbaseMasterAvgloadAverageload | 每个RS平均REGION数_averageLoad               | 个   | 每个 ResgionServer 平均 Region 数                | id4hbaseoverview |
| EmrHbaseOverviewAggregation<br/>HbaseMasterBytesReceivedbytes | 集群读写数量_receivedBytes                   | B/s  | 集群接收数据量                                   | id4hbaseoverview |
| EmrHbaseOverviewAggregationHbase<br/>MasterAssignmentmanagerTimeRitoldestage | 集群RIT时间_ritOldestAge                     | ms   | Region in transition 的最老年龄                  | id4hbaseoverview |
| EmrHbaseOverviewAggregation<br/>HbaseMasterRsnumsNumdeadregionservers | 集群RS数量_numDeadRegionServers              | 个   | 当前Dead的 RegionServer 个数                     | id4hbaseoverview |
| EmrHbaseOverviewAggregationHbaseMaster<br/>BalancerOpsBalancerclusterNumOps | 集群负载均衡次数_BalancerCluster_num_ops     | 次   | 集群负载均衡次数                                 | id4hbaseoverview |
| EmrHbaseOverviewAggregationHbaseMaster<br/>AssignmentmanagerOpsAssignNumOps | 集群Assignment管理器操作_Assign_num_ops      | 次   | Assign region次数                                | id4hbaseoverview |
| HbaseMasterReqClusterrequests                                | 集群接口总请求量_clusterRequests             | 个   | 集群总请求数量                                   | id4hbaseoverview |

### HBASE-HMaster

| 指标英文名                                                 | 指标中文名                                 | 单位 | 指标含义                                | 维度                                 |
| ---------------------------------------------------------- | ------------------------------------------ | ---- | --------------------------------------- | ------------------------------------ |
| HbaseHmGcUtilMemoryS1                                      | 内存区域占比_S1                            | %    | Survivor 1区内存使用占比                | host4hbasehmaster、 id4hbasehmaster  |
| HbaseHmGcUtilMemoryS0                                      | 内存区域占比_S0                            | %    | Survivor 0区内存使用占比                | host4hbasehmaster、  id4hbasehmaster |
| HbaseHmGcUtilMemoryO                                       | 内存区域占比_O                             | %    | Old 区内存使用占比                      | host4hbasehmaster、  id4hbasehmaster |
| HbaseHmGcUtilMemoryM                                       | 内存区域占比_M                             | %    | Metaspace 区内存使用占比                | host4hbasehmaster、  id4hbasehmaster |
| HbaseHmGcUtilMemoryE                                       | 内存区域占比_E                             | %    | Eden 区内存使用占比                     | host4hbasehmaster、  id4hbasehmaster |
| HbaseHmGcUtilMemoryCcs                                     | 内存区域占比_CCS                           | %    | Compressed class space 区内存使用占比   | host4hbasehmaster、  id4hbasehmaster |
| HbaseMasterServer<br>TimeMasterstarttime                   | 进程启动时间_masterStartTime               | s    | Master 进程启动时间                     | host4hbasehmaster、  id4hbasehmaster |
| HbaseMasterServer<br/>TimeMasteractivetime                 | 进程启动时间_masterActiveTime              | s    | Master 进程 Active 时间                 | host4hbasehmaster、  id4hbasehmaster |
| HbaseMasterIpcException<br/>Unknownscannerexception        | RPC异常次数_UnknownScannerException        | 次   | UnknownScannerException 异常次数        | host4hbasehmaster、  id4hbasehmaster |
| HbaseMasterIpcException<br/>Regiontoobusyexception         | RPC异常次数_RegionTooBusyException         | 次   | RegionTooBusyException 异常次数         | host4hbasehmaster、  id4hbasehmaster |
| HbaseMasterIpcException<br/>Regionmovedexception           | RPC异常次数_RegionMovedException           | 次   | RegionMovedException 异常次数           | host4hbasehmaster、  id4hbasehmaster |
| HbaseMasterIpcException<br/>Outoforderscannernextexception | RPC异常次数_OutOfOrderScannerNextException | 次   | OutOfOrderScannerNextException 异常次数 | host4hbasehmaster、  id4hbasehmaster |
| HbaseMasterIpcException Notservingregionexception          | RPC异常次数_NotServingRegionException      | 次   | NotServingRegionException 异常次数      | host4hbasehmaster、  id4hbasehmaster |
| HbaseMasterIpcException<br/>Failedsanitycheckexception     | RPC异常次数_FailedSanityCheckException     | 次   | FiledSanityCheckException 异常次数      | host4hbasehmaster、  id4hbasehmaster |
| HbaseMasterIpcConnections<br/>Numopenconnections           | RPC连接数_numOpenConnections               | 个   | RPC 连接数                              | host4hbasehmaster、  id4hbasehmaster |
| HbaseMasterIpcQueue<br/>Numcallsinreplicationqueue         | RPC队列请求数_numCallsInReplicationQueue   | 个   | 复制队列 RPC 请求数                     | host4hbasehmaster、  id4hbasehmaster |
| HbaseMasterIpcQueue<br/>Numcallsinpriorityqueue            | RPC队列请求数_numCallsInPriorityQueue      | 次   | 通用队列 RPC 请求数                     | host4hbasehmaster、  id4hbasehmaster |
| HbaseMasterJvm<br/>ThreadsThreadswaiting                   | JVM线程数量_ThreadsWaiting                 | 个   | 处于 WAITING 状态的线程数量             | host4hbasehmaster、  id4hbasehmaster |
| HbaseMasterJvmThreads<br/>Threadstimedwaiting              | JVM线程数量_ThreadsTimedWaiting            | 个   | 处于 TIMED WAITING 状态的线程数量       | host4hbasehmaster、  id4hbasehmaster |
| HbaseMasterJvmThreads<br/>Threadsterminated                | JVM线程数量_ThreadsTerminated              | 个   | 当前 TERMINATED 状态线程数量            | host4hbasehmaster、  id4hbasehmaster |
| HbaseMasterJvmThreads<br/>Threadsrunnable                  | JVM线程数量_ThreadsRunnable                | 个   | 处于 RUNNABLE 状态的线程数量            | host4hbasehmaster、  id4hbasehmaster |
| HbaseMasterJvm<br/>ThreadsThreadsnew                       | JVM线程数量_ThreadsNew                     | 个   | 处于 NEW 状态的线程数量                 | host4hbasehmaster、  id4hbasehmaster |
| HbaseMasterJvmThreads<br/>Threadsblocked                   | JVM线程数量_ThreadsBlocked                 | 个   | 处于 BLOCKED 状态的线程数量             | host4hbasehmaster、  id4hbasehmaster |
| HbaseMasterJvm<br/>LogTotalLogwarn                         | JVM日志数量_LogWarn                        | 个   | Warn 日志数量                           | host4hbasehmaster、  id4hbasehmaster |
| HbaseMasterJvmLog<br/>TotalLoginfo                         | JVM日志数量_LogInfo                        | 个   | Info 日志数量                           | host4hbasehmaster、  id4hbasehmaster |
| HbaseMasterJvm<br/>LogTotalLogfatal                        | JVM日志数量_LogFatal                       | 个   | Fatal 日志数量                          | host4hbasehmaster、  id4hbasehmaster |
| HbaseMasterJvm<br/>LogTotalLogerror                        | JVM日志数量_LogError                       | 个   | Error 日志数量                          | host4hbasehmaster、  id4hbasehmaster |
| HbaseMasterJvm<br/>MemMemnonheapusedm                      | JVM内存_MemNonHeapUsedM                    | MB   | 进程使用的非堆内存大小                  | host4hbasehmaster、  id4hbasehmaster |
| HbaseMasterJvmMem<br/>Memnonheapcommittedm                 | JVM内存_MemNonHeapCommittedM               | MB   | 进程 commit 的非堆内存大小              | host4hbasehmaster、  id4hbasehmaster |
| HbaseMasterJvmMem<br/>Memmaxm                              | JVM内存_MemMaxM                            | MB   | 进程最大内存大小                        | host4hbasehmaster、  id4hbasehmaster |
| HbaseMasterJvm<br/>MemMemheapusedm                         | JVM内存_MemHeapUsedM                       | MB   | 进程使用的堆内存大小                    | host4hbasehmaster、  id4hbasehmaster |
| HbaseMasterJvm<br/>MemMemheapmaxm                          | JVM内存_MemHeapMaxM                        | MB   | 进程最大的堆内存大小                    | host4hbasehmaster、  id4hbasehmaster |
| HbaseMasterJvmMem<br/>Memheapcommittedm                    | JVM内存_MemHeapCommittedM                  | MB   | 进程 commit 的堆内存大小                | host4hbasehmaster、  id4hbasehmaster |
| HbaseHmGcUtilGcTimeYgct                                    | GC时间_YGCT                                | s    | Young GC 消耗时间                       | host4hbasehmaster、  id4hbasehmaster |
| HbaseHmGcUtilGcTimeGct                                     | GC时间_GCT                                 | s    | 垃圾回收时间消耗                        | host4hbasehmaster、  id4hbasehmaster |
| HbaseHmGcUtilGcTimeFgct                                    | GC时间_FGCT                                | s    | Full GC 消耗时间                        | host4hbasehmaster、  id4hbasehmaster |
| HbaseHmGcUtilGcCountYgc                                    | GC次数_YGC                                 | 次   | Young GC 次数                           | host4hbasehmaster、  id4hbasehmaster |
| HbaseHmGcUtilGcCountFgc                                    | GC次数_FGC                                 | 次   | Full GC  次数                           | host4hbasehmaster、  id4hbasehmaster |

### HBASE-RegionServer

| 指标英文名                                                   | 指标中文名                                         | 单位  | 指标含义                                         | 维度                                   |
| ------------------------------------------------------------ | -------------------------------------------------- | ----- | ------------------------------------------------ | -------------------------------------- |
| HbaseRegionserver<br>ScantimeMin                             | 最小ScanTime                                       | ms    | 最小 Scan 请求时间                               | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserver<br/>ScansizeMin                            | 最小ScanSize                                       | 次    | 最小Scan 请求量                                  | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserver<br/>ScantimeMax                            | 最大ScanTime                                       | ms    | 最大 Scan 请求时间                               | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserver<br/>ScansizeMax                            | 最大ScanSize                                       | 次    | 最大Scan 请求量                                  | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserver<br/>ServerCellsFlushedcellssize            | 写磁盘速率_flushedCellsSize                        | B/s   | 写磁盘速率                                       | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserver<br/>ServerIndexStorefileindexsize          | 索引大小_storeFileIndexSize                        | B     | 磁盘上 storeFile 中的索引大小                    | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserver<br/>ServerIndexStaticindexsize             | 索引大小_staticIndexSize                           | B     | 未压缩的静态索引大小                             | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserver<br/>ServerIndexStaticbloomsize             | 索引大小_staticBloomSize                           | B     | 未压缩的静态 Bloom Filters 大小                  | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserver<br/>ServerDelayUpdatesblockedtime          | 平均延时_updatesBlockedTime                        | ms    | Memstore 可 flush 前的更新阻塞时间               | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserver<br/>ServerDelayReplayMean                  | 平均延时_Replay_mean                               | ms    | Replay 请求平均延时                              | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserver<br/>ServerDelayGetMean                     | 平均延时_Get_mean                                  | ms    | Get 请求平均延时                                 | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserver<br/>ServerDelayAppendMean                  | 平均延时_Append_mean                               | ms    | Append 请求平均延时                              | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserver<br/>ScantimeMean                           | 平均ScanTime                                       | ms    | 平均 Scan 请求时间                               | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserver<br/>ScansizeMean                           | 平均ScanSize                                       | 次    | 平均 Scan 请求大小                               | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseHsGcUtilMemoryS1                                        | 内存区域占比_S1                                    | %     | Survivor 1区内存使用占比                         | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseHsGcUtilMemoryS0                                        | 内存区域占比_S0                                    | %     | Survivor 0区内存使用占比                         | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseHsGcUtilMemoryO                                         | 内存区域占比_O                                     | %     | Old 区内存使用占比                               | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseHsGcUtilMemoryM                                         | 内存区域占比_M                                     | %     | Metaspace 区内存使用占比                         | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseHsGcUtilMemoryE                                         | 内存区域占比_E                                     | %     | Eden 区内存使用占比                              | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseHsGcUtilMemoryCcs                                       | 内存区域占比_CCS                                   | %     | Compressed class space 区内存使用占比            | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverServer<br/>SlowSlowputcount                 | 慢操作次数_slowPutCount                            | 次    | Put 请求时间超过1s的数量                         | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverServer<br/>SlowSlowincrementcount           | 慢操作次数_slowIncrementCount                      | 次    | Increment 请求时间超过1s的数量                   | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverServer<br/>SlowSlowgetcount                 | 慢操作次数_slowGetCount                            | 次    | Get 请求时间超过1s的数量                         | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverServer<br/>SlowSlowdeletecount              | 慢操作次数_slowDeleteCount                         | 次    | Delete 请求时间超过1s的数量                      | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverServer<br/>SlowSlowappendcount              | 慢操作次数_slowAppendCount                         | 次    | Append 请求时间超过1s的数量                      | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverStarttime<br/>Regionserverstarttime         | 进程启动时间_regionServerStartTime                 | s     | 进程启动时间                                     | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverServer<br/>BlockcacheCountBlockcachemisscount | 缓存块数量_blockCacheMissCount                     | 个    | Block Cache miss 请求数                          | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverServer<br/>BlockcacheCountBlockcachehitcount | 缓存块数量_blockCacheHitCount                      | 个    | Block Cache hit 请求数                           | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverServer<br/>BlockcacheCountBlockcachecount   | 缓存块数量_blockCacheCount                         | 个    | Block Cache 中的 Block 数量                      | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverServer<br/>BlockcacheSizeBlockcachesize     | 缓存块内存占用大小_blockCacheSize                  | B     | 缓存块内存占用大小                               | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserver<br/>ReqcountWrite                          | 读写请求量_Write                                   | 个/秒 | 写请求量                                         | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserver<br/>ReqcountTotal                          | 读写请求量_Total                                   | 个/秒 | 总请求量，当有Scan请求时，该值会小于读写请求之和 | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserver<br/>ReqcountScantimeNumOps                 | 读写请求量_Scantime                                | ms    | Scan 请求时间                                    | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserver<br/>ReqcountScansizeNumOps                 | 读写请求量_Scansize                                | 个/秒 | Scan 请求量                                      | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverReqcountRead                                | 读写请求量_Read                                    | 个/秒 | 读请求量                                         | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserver<br/>ReqcountPutNumOps                      | 读写请求量_Put                                     | 个/秒 | Put 请求量                                       | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserver<br/>ReqcountIncrementNumOps                | 读写请求量_Increment                               | 个/秒 | Increment请求量                                  | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserver<br/>ReqcountGetNumOps                      | 读写请求量_Get                                     | 个/秒 | Get 请求量                                       | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserver<br/>ReqcountDeleteNumOps                   | 读写请求量_Delete                                  | 个/秒 | Delete 请求量                                    | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserver<br/>ReqcountAppendNumOps                   | 读写请求量_Append_num_ops                          | 个/秒 | Append 请求量                                    | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverIpc<br/>BytesSentbytes                      | 读写流量_sentBytes                                 | B/s   | 读写流量                                         | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverIpc<br/>BytesReceivedbytes                  | 读写流量_receivedBytes                             | B/s   | 接收数据量                                       | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverServer<br/>BlockcachePercentBlockcacheexpresshi | 读缓存命中率_blockCacheExpressHitPercent           | %     | 读缓存命中率                                     | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverServer<br/>QueueSplitqueuelength            | 操作队列请求数_splitQueueLength                    | 个    | Split 队列长度                                   | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverServer<br/>QueueFlushqueuelength            | 操作队列请求数_flushQueueLength                    | 个    | Region Flush 队列长度                            | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverServer<br/>QueueCompactionqueuelength       | 操作队列请求数_compactionQueueLength               | 个    | Compaction 队列长度                              | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserver<br/>HlogcountHlogfilecount                 | WAL文件数量_hlogFileCount                          | 个    | WAL 文件数量                                     | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserver<br/>HlogsizeHlogfilesize                   | WAL文件大小_hlogFileSize                           | B     | WAL 文件大小                                     | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserver<br/>StoreCountStorecount                   | Store个数_storeCount                               | 个    | Store 个数                                       | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserver<br/>StorefilecountStorefilecount           | Storefile个数_storeFileCount                       | 个    | Storefile 个数                                   | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserver<br/>StorefilesizeStorefilesize             | Storefile大小_storeFileSize                        | MB    | Storefile 大小                                   | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserver<br/>ServerSplitSplitsuccesscount           | split请求_splitSuccessCount                        | 次    | split 成功次数                                   | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserver<br/>ServerSplitSplitrequestcount           | split请求_splitRequestCount                        | 个    | split 请求数                                     | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserver<br/>ServerFlushFlushtimeNumOps             | RS写磁盘次数_FlushTime_num_ops                     | 次    | Memstore flush 写磁盘次数                        | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverIpc<br/>ExceptionUnknownscannerexception    | RPC异常次数_UnknownScannerException                | 次    | UnknownScannerException 异常次数                 | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverIpc<br/>ExceptionRegiontoobusyexception     | RPC异常次数_RegionTooBusyException                 | 次    | RegionTooBusyException 异常次数                  | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverIpc<br/>ExceptionRegionmovedexception       | RPC异常次数_RegionMovedException                   | 次    | RegionMovedException 异常次数                    | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverIpcException<br/>Outoforderscannernextexception | RPC异常次数_OutOfOrderScannerNextException         | 次    | OutOfOrderScannerNextException 异常次数          | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverIpcException<br/>Notservingregionexception  | RPC异常次数_NotServingRegionException              | 次    | NotServingRegionException 异常次数               | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverIpcException<br/>Failedsanitycheckexception | RPC异常次数_FailedSanityCheckException             | 次    | FailedSanityCheckException 异常次数              | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverIpc<br/>AuthenticationAuthenticationsuccesses | RPC认证次数_authenticationSuccesses                | 次    | RPC 认证成功次数                                 | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverIpc<br/>AuthenticationAuthenticationfailures | RPC认证次数_authenticationFailures                 | 次    | RPC 认证失败次数                                 | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverIpc<br/>ConnectionsNumopenconnections       | RPC连接数_numOpenConnections                       | 个    | RPC 连接数                                       | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverIpc<br/>HandlerNumactivehandler             | RPC句柄数_numActiveHandler                         | 个    | RPC 句柄数                                       | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverIpc<br/>QueueNumcallsinreplicationqueue     | RPC队列请求数_numCallsInReplicationQueue           | 个    | 复制队列 RPC 请求数                              | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverIpc<br/>QueueNumcallsinpriorityqueue        | RPC队列请求数_numCallsInPriorityQueue              | 个    | 优先队列 RPC 请求数                              | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverIpc<br/>QueueNumcallsingeneralqueue         | RPC队列请求数_numCallsInGeneralQueue               | 个    | 通用队列 RPC 请求数                              | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserver<br/>ServerReplayReplayNumOps               | Replay操作次数_Replay_num_ops                      | 次    | Replay操作次数                                   | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserver<br/>AvgsizeAverageregionsize               | Region平均大小_averageRegionSize                   | B     | Region平均大小                                   | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverRegion<br/>CountRegioncount                 | Region个数_regionCount                             | 个    | Region 个数                                      | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverServerHfiles<br/>PercentPercentfileslocalsecond | Region副本本地化_percentFilesLocalSecondaryRegions | %     | Region副本本地化                                 | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverServerMutation<br/>SizeMutationswithoutwalsize | mutation大小_mutationsWithoutWALSize               | B     | mutation大小                                     | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverServerMutation<br/>CountMutationswithoutwalcoun | muation个数_mutationsWithoutWALCount               | 个    | mutation 个数                                    | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserver<br/>MemstroreMemstoresize                  | Memstore大小_memStoreSize                          | MB    | Memstore 大小                                    | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserver<br/>JvmThreadsThreadswaiting               | JVM线程数量_ThreadsWaiting                         | 个    | 处于 WAITING 状态的线程数量                      | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverJvm<br/>ThreadsThreadstimedwaiting          | JVM线程数量_ThreadsTimedWaiting                    | 个    | 处于 TIMED WAITING 状态的线程数量                | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverJvm<br/>ThreadsThreadsterminated            | JVM线程数量_ThreadsTerminated                      | 个    | 当前 TERMINATED 状态线程数量                     | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverJvm<br/>ThreadsThreadsrunnable              | JVM线程数量_ThreadsRunnable                        | 个    | 处于 RUNNABLE 状态的线程数量                     | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverJvm<br/>ThreadsThreadsnew                   | JVM线程数量_ThreadsNew                             | 个    | 处于 NEW 状态的线程数量                          | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverJvm<br/>ThreadsThreadsblocked               | JVM线程数量_ThreadsBlocked                         | 个    | 处于 BLOCKED 状态的线程数量                      | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserver<br/>JvmLogTotalLogwarn                     | JVM日志数量_LogWarn                                | 个    | Warn日志数量                                     | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserver<br/>JvmLogTotalLoginfo                     | JVM日志数量_LogInfo                                | 个    | Info日志数量                                     | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserver<br/>JvmLogTotalLogfatal                    | JVM日志数量_LogFatal                               | 个    | Fatal 日志数量                                   | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserver<br/>JvmLogTotalLogerror                    | JVM日志数量_LogError                               | 个    | Error 日志数量                                   | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverJvm<br/>MemMemnonheapusedm                  | JVM内存_MemNonHeapUsedM                            | MB    | 进程使用的非堆内存大小                           | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverJvm<br/>MemMemnonheapcommittedm             | JVM内存_MemNonHeapCommittedM                       | MB    | 进程 commit 的非堆内存大小                       | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverJvm<br/>MemMemmaxm                          | JVM内存_MemMaxM                                    | MB    | 进程最大内存大小                                 | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverJvm<br/>MemMemheapusedm                     | JVM内存_MemHeapUsedM                               | MB    | 进程使用的堆内存大小                             | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverJvm<br/>MemMemheapmaxm                      | JVM内存_MemHeapMaxM                                | MB    | 进程最大的堆内存大小                             | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverJvm<br/>MemMemheapcommittedm                | JVM内存_MemHeapCommittedM                          | MB    | 进程 commit 的堆内存大小                         | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseHsGcUtilGcTimeYgct                                      | GC时间_YGCT                                        | s     | Young GC 消耗时间                                | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseHsGcUtilGcTimeGct                                       | GC时间_GCT                                         | s     | 垃圾回收时间消耗                                 | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseHsGcUtilGcTimeFgct                                      | GC时间_FGCT                                        | s     | Full GC 消耗时间                                 | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseHsGcUtilGcCountYgc                                      | GC次数_YGC                                         | 次    | Young GC 次数                                    | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseHsGcUtilGcCountFgc                                      | GC次数_FGC                                         | 次    | Full GC 次数                                     | host4hbasehmaster、<br>id4hbasehmaster |

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
