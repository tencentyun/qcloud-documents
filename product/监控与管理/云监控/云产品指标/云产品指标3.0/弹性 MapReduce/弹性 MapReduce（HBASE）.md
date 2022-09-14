## 命名空间

Namespace=QCE/TXMR_HBASE

## 监控指标

| 指标英文名                                                   | 指标中文名                                   | 指标单位 | 指标含义                                        | 维度                                      |
| ------------------------------------------------------------ | -------------------------------------------- | -------- | ----------------------------------------------- | ----------------------------------------- |
| EmrHbaseOverviewHbaseMasterRsnumsNumregionservers            | 集群RS数量_numRegionServers                  | 个       | 当前存活的 RegionServer 个数                    | host4hbaseoverview、<br/>id4hbaseoverview |
| EmrHbaseOverviewHbaseMasterRsnumsNumdeadregionservers        | 集群RS数量_numDeadRegionServers              | 个       | 当前Dead的 RegionServer 个数                    | host4hbaseoverview、<br/>id4hbaseoverview |
| EmrHbaseOverviewHbaseMasterReqClusterrequests                | 集群接口总请求量_clusterRequests             | 个       | 集群总请求数量                                  | host4hbaseoverview、<br/>id4hbaseoverview |
| EmrHbaseOverviewHbaseMasterBytesSentbytes                    | 集群读写数量_sentBytes                       | b/s      | 集群发送数据量                                  | host4hbaseoverview、<br/>id4hbaseoverview |
| EmrHbaseOverviewHbaseMasterBytesReceivedbytes                | 集群读写数量_receivedBytes                   | b/s      | 集群接收数据量                                  | host4hbaseoverview、<br/>id4hbaseoverview |
| EmrHbaseOverviewHbaseMasterBalancerOpsBalancerclusterNumOps  | 集群负载均衡次数_BalancerCluster_num_ops     | 次       | 集群负载均衡次数                                | host4hbaseoverview、<br/>id4hbaseoverview |
| EmrHbaseOverviewHbaseMasterAvgloadAverageload                | 每个RS平均REGION数_averageLoad               | 个       | 每个 ResgionServer 平均 Region 数               | host4hbaseoverview、<br/>id4hbaseoverview |
| EmrHbaseOverviewHbaseMasterAssignmentmanagerTimeRitoldestage | 集群RIT时间_ritOldestAge                     | ms       | Region in transition 的最老年龄                 | host4hbaseoverview、<br/>id4hbaseoverview |
| EmrHbaseOverviewHbaseMasterAssignmentmanagerRitRitcountoverthreshold | 集群处于RIT Region个数_ritCountOverThreshold | 个       | Region in transition 时间超过阈值的 Region 个数 | host4hbaseoverview、<br/>id4hbaseoverview |
| EmrHbaseOverviewHbaseMasterAssignmentmanagerRitRitcount      | 集群处于RIT Region个数_ritCount              | 个       | Region in transition 的个数                     | host4hbaseoverview、<br/>id4hbaseoverview |
| EmrHbaseOverviewHbaseMasterAssignmentmanagerOpsBulkassignNumOps | 集群Assignment管理器操作_BulkAssign_num_ops  | 次       | Bulk assign region次数                          | host4hbaseoverview、<br/>id4hbaseoverview |
| EmrHbaseOverviewHbaseMasterAssignmentmanagerOpsAssignNumOps  | 集群Assignment管理器操作_Assign_num_ops      | 次       | Assign region次数                               | host4hbaseoverview、<br/>id4hbaseoverview |



### Hbase-OverviewAggregation

| 指标英文名                                                   | 指标中文名                                   | 单位 | 指标含义                                         | 维度             |
| ------------------------------------------------------------ | -------------------------------------------- | ---- | ------------------------------------------------ | ---------------- |
| EmrHbaseOverviewAggregationHbaseMasterAssignmentmanagerOpsBulkassignNumOps | 集群Assignment管理器操作_BulkAssign_num_ops  | 次   | Bulk assign region次数                           | id4hbaseoverview |
| EmrHbaseOverviewAggregationHbaseMasterAssignmentmanagerRitRitcountoverthreshold | 集群处于RIT_Region个数_ritCountOverThreshold | 个   | Region in transition 时间超过阈值的  Region 个数 | id4hbaseoverview |
| EmrHbaseOverviewAggregationHbaseMasterBytesSentbytes         | 集群读写数量_sentBytes                       | B/s  | 集群发送数据量                                   | id4hbaseoverview |
| EmrHbaseOverviewAggregationHbaseMasterAssignmentmanagerRitRitcount | 集群处于RIT_Region个数_ritCount              | 个   | Region in transition 的个数                      | id4hbaseoverview |
| EmrHbaseOverviewAggregationHbaseMasterRsnumsNumregionservers | 集群RS数量_numRegionServers                  | 个   | 当前存活的 RegionServer 个数                     | id4hbaseoverview |
| EmrHbaseOverviewAggregationHbaseMasterAvgloadAverageload     | 每个RS平均REGION数_averageLoad               | 个   | 每个 ResgionServer 平均 Region 数                | id4hbaseoverview |
| EmrHbaseOverviewAggregationHbaseMasterBytesReceivedbytes     | 集群读写数量_receivedBytes                   | B/s  | 集群接收数据量                                   | id4hbaseoverview |
| EmrHbaseOverviewAggregationHbaseMasterAssignmentmanagerTimeRitoldestage | 集群RIT时间_ritOldestAge                     | ms   | Region in transition 的最老年龄                  | id4hbaseoverview |
| EmrHbaseOverviewAggregationHbaseMasterRsnumsNumdeadregionservers | 集群RS数量_numDeadRegionServers              | 个   | 当前Dead的 RegionServer 个数                     | id4hbaseoverview |
| EmrHbaseOverviewAggregationHbaseMasterBalancerOpsBalancerclusterNumOps | 集群负载均衡次数_BalancerCluster_num_ops     | 次   | 集群负载均衡次数                                 | id4hbaseoverview |
| EmrHbaseOverviewAggregationHbaseMasterAssignmentmanagerOpsAssignNumOps | 集群Assignment管理器操作_Assign_num_ops      | 次   | Assign region次数                                | id4hbaseoverview |
| HbaseMasterReqClusterrequests                                | 集群接口总请求量_clusterRequests             | 个   | 集群总请求数量                                   | id4hbaseoverview |

### HBASE-HMaster

| 指标英文名                                            | 指标中文名                                 | 单位 | 指标含义                                | 维度                                 |
| ----------------------------------------------------- | ------------------------------------------ | ---- | --------------------------------------- | ------------------------------------ |
| HbaseHmGcUtilMemoryS1                                 | 内存区域占比_S1                            | %    | Survivor 1区内存使用占比                | host4hbasehmaster、 id4hbasehmaster  |
| HbaseHmGcUtilMemoryS0                                 | 内存区域占比_S0                            | %    | Survivor 0区内存使用占比                | host4hbasehmaster、  id4hbasehmaster |
| HbaseHmGcUtilMemoryO                                  | 内存区域占比_O                             | %    | Old 区内存使用占比                      | host4hbasehmaster、  id4hbasehmaster |
| HbaseHmGcUtilMemoryM                                  | 内存区域占比_M                             | %    | Metaspace 区内存使用占比                | host4hbasehmaster、  id4hbasehmaster |
| HbaseHmGcUtilMemoryE                                  | 内存区域占比_E                             | %    | Eden 区内存使用占比                     | host4hbasehmaster、  id4hbasehmaster |
| HbaseHmGcUtilMemoryCcs                                | 内存区域占比_CCS                           | %    | Compressed class space 区内存使用占比   | host4hbasehmaster、  id4hbasehmaster |
| HbaseMasterServerTimeMasterstarttime                  | 进程启动时间_masterStartTime               | s    | Master 进程启动时间                     | host4hbasehmaster、  id4hbasehmaster |
| HbaseMasterServerTimeMasteractivetime                 | 进程启动时间_masterActiveTime              | s    | Master 进程 Active 时间                 | host4hbasehmaster、  id4hbasehmaster |
| HbaseMasterIpcExceptionUnknownscannerexception        | RPC异常次数_UnknownScannerException        | 次   | UnknownScannerException 异常次数        | host4hbasehmaster、  id4hbasehmaster |
| HbaseMasterIpcExceptionRegiontoobusyexception         | RPC异常次数_RegionTooBusyException         | 次   | RegionTooBusyException 异常次数         | host4hbasehmaster、  id4hbasehmaster |
| HbaseMasterIpcExceptionRegionmovedexception           | RPC异常次数_RegionMovedException           | 次   | RegionMovedException 异常次数           | host4hbasehmaster、  id4hbasehmaster |
| HbaseMasterIpcExceptionOutoforderscannernextexception | RPC异常次数_OutOfOrderScannerNextException | 次   | OutOfOrderScannerNextException 异常次数 | host4hbasehmaster、  id4hbasehmaster |
| HbaseMasterIpcException Notservingregionexception     | RPC异常次数_NotServingRegionException      | 次   | NotServingRegionException 异常次数      | host4hbasehmaster、  id4hbasehmaster |
| HbaseMasterIpcExceptionFailedsanitycheckexception     | RPC异常次数_FailedSanityCheckException     | 次   | FiledSanityCheckException 异常次数      | host4hbasehmaster、  id4hbasehmaster |
| HbaseMasterIpcConnectionsNumopenconnections           | RPC连接数_numOpenConnections               | 个   | RPC 连接数                              | host4hbasehmaster、  id4hbasehmaster |
| HbaseMasterIpcQueueNumcallsinreplicationqueue         | RPC队列请求数_numCallsInReplicationQueue   | 个   | 复制队列 RPC 请求数                     | host4hbasehmaster、  id4hbasehmaster |
| HbaseMasterIpcQueueNumcallsinpriorityqueue            | RPC队列请求数_numCallsInPriorityQueue      | 次   | 通用队列 RPC 请求数                     | host4hbasehmaster、  id4hbasehmaster |
| HbaseMasterJvmThreadsThreadswaiting                   | JVM线程数量_ThreadsWaiting                 | 个   | 处于 WAITING 状态的线程数量             | host4hbasehmaster、  id4hbasehmaster |
| HbaseMasterJvmThreadsThreadstimedwaiting              | JVM线程数量_ThreadsTimedWaiting            | 个   | 处于 TIMED WAITING 状态的线程数量       | host4hbasehmaster、  id4hbasehmaster |
| HbaseMasterJvmThreadsThreadsterminated                | JVM线程数量_ThreadsTerminated              | 个   | 当前 TERMINATED 状态线程数量            | host4hbasehmaster、  id4hbasehmaster |
| HbaseMasterJvmThreadsThreadsrunnable                  | JVM线程数量_ThreadsRunnable                | 个   | 处于 RUNNABLE 状态的线程数量            | host4hbasehmaster、  id4hbasehmaster |
| HbaseMasterJvmThreadsThreadsnew                       | JVM线程数量_ThreadsNew                     | 个   | 处于 NEW 状态的线程数量                 | host4hbasehmaster、  id4hbasehmaster |
| HbaseMasterJvmThreadsThreadsblocked                   | JVM线程数量_ThreadsBlocked                 | 个   | 处于 BLOCKED 状态的线程数量             | host4hbasehmaster、  id4hbasehmaster |
| HbaseMasterJvmLogTotalLogwarn                         | JVM日志数量_LogWarn                        | 个   | Warn 日志数量                           | host4hbasehmaster、  id4hbasehmaster |
| HbaseMasterJvmLogTotalLoginfo                         | JVM日志数量_LogInfo                        | 个   | Info 日志数量                           | host4hbasehmaster、  id4hbasehmaster |
| HbaseMasterJvmLogTotalLogfatal                        | JVM日志数量_LogFatal                       | 个   | Fatal 日志数量                          | host4hbasehmaster、  id4hbasehmaster |
| HbaseMasterJvmLogTotalLogerror                        | JVM日志数量_LogError                       | 个   | Error 日志数量                          | host4hbasehmaster、  id4hbasehmaster |
| HbaseMasterJvmMemMemnonheapusedm                      | JVM内存_MemNonHeapUsedM                    | MB   | 进程使用的非堆内存大小                  | host4hbasehmaster、  id4hbasehmaster |
| HbaseMasterJvmMemMemnonheapcommittedm                 | JVM内存_MemNonHeapCommittedM               | MB   | 进程 commit 的非堆内存大小              | host4hbasehmaster、  id4hbasehmaster |
| HbaseMasterJvmMemMemmaxm                              | JVM内存_MemMaxM                            | MB   | 进程最大内存大小                        | host4hbasehmaster、  id4hbasehmaster |
| HbaseMasterJvmMemMemheapusedm                         | JVM内存_MemHeapUsedM                       | MB   | 进程使用的堆内存大小                    | host4hbasehmaster、  id4hbasehmaster |
| HbaseMasterJvmMemMemheapmaxm                          | JVM内存_MemHeapMaxM                        | MB   | 进程最大的堆内存大小                    | host4hbasehmaster、  id4hbasehmaster |
| HbaseMasterJvmMemMemheapcommittedm                    | JVM内存_MemHeapCommittedM                  | MB   | 进程 commit 的堆内存大小                | host4hbasehmaster、  id4hbasehmaster |
| HbaseHmGcUtilGcTimeYgct                               | GC时间_YGCT                                | s    | Young GC 消耗时间                       | host4hbasehmaster、  id4hbasehmaster |
| HbaseHmGcUtilGcTimeGct                                | GC时间_GCT                                 | s    | 垃圾回收时间消耗                        | host4hbasehmaster、  id4hbasehmaster |
| HbaseHmGcUtilGcTimeFgct                               | GC时间_FGCT                                | s    | Full GC 消耗时间                        | host4hbasehmaster、  id4hbasehmaster |
| HbaseHmGcUtilGcCountYgc                               | GC次数_YGC                                 | 次   | Young GC 次数                           | host4hbasehmaster、  id4hbasehmaster |
| HbaseHmGcUtilGcCountFgc                               | GC次数_FGC                                 | 次   | Full GC  次数                           | host4hbasehmaster、  id4hbasehmaster |

### HBASE-RegionServer

| 指标英文名                                                  | 指标中文名                                         | 单位  | 指标含义                                         | 维度                                   |
| ----------------------------------------------------------- | -------------------------------------------------- | ----- | ------------------------------------------------ | -------------------------------------- |
| HbaseRegionserverScantimeMin                                | 最小ScanTime                                       | ms    | 最小 Scan 请求时间                               | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverScansizeMin                                | 最小ScanSize                                       | 次    | 最小Scan 请求量                                  | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverScantimeMax                                | 最大ScanTime                                       | ms    | 最大 Scan 请求时间                               | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverScansizeMax                                | 最大ScanSize                                       | 次    | 最大Scan 请求量                                  | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverServerCellsFlushedcellssize                | 写磁盘速率_flushedCellsSize                        | B/s   | 写磁盘速率                                       | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverServerIndexStorefileindexsize              | 索引大小_storeFileIndexSize                        | B     | 磁盘上 storeFile 中的索引大小                    | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverServerIndexStaticindexsize                 | 索引大小_staticIndexSize                           | B     | 未压缩的静态索引大小                             | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverServerIndexStaticbloomsize                 | 索引大小_staticBloomSize                           | B     | 未压缩的静态 Bloom Filters 大小                  | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverServerDelayUpdatesblockedtime              | 平均延时_updatesBlockedTime                        | ms    | Memstore 可 flush 前的更新阻塞时间               | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverServerDelayReplayMean                      | 平均延时_Replay_mean                               | ms    | Replay 请求平均延时                              | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverServerDelayGetMean                         | 平均延时_Get_mean                                  | ms    | Get 请求平均延时                                 | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverServerDelayAppendMean                      | 平均延时_Append_mean                               | ms    | Append 请求平均延时                              | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverScantimeMean                               | 平均ScanTime                                       | ms    | 平均 Scan 请求时间                               | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverScansizeMean                               | 平均ScanSize                                       | 次    | 平均 Scan 请求大小                               | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseHsGcUtilMemoryS1                                       | 内存区域占比_S1                                    | %     | Survivor 1区内存使用占比                         | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseHsGcUtilMemoryS0                                       | 内存区域占比_S0                                    | %     | Survivor 0区内存使用占比                         | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseHsGcUtilMemoryO                                        | 内存区域占比_O                                     | %     | Old 区内存使用占比                               | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseHsGcUtilMemoryM                                        | 内存区域占比_M                                     | %     | Metaspace 区内存使用占比                         | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseHsGcUtilMemoryE                                        | 内存区域占比_E                                     | %     | Eden 区内存使用占比                              | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseHsGcUtilMemoryCcs                                      | 内存区域占比_CCS                                   | %     | Compressed class space 区内存使用占比            | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverServerSlowSlowputcount                     | 慢操作次数_slowPutCount                            | 次    | Put 请求时间超过1s的数量                         | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverServerSlowSlowincrementcount               | 慢操作次数_slowIncrementCount                      | 次    | Increment 请求时间超过1s的数量                   | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverServerSlowSlowgetcount                     | 慢操作次数_slowGetCount                            | 次    | Get 请求时间超过1s的数量                         | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverServerSlowSlowdeletecount                  | 慢操作次数_slowDeleteCount                         | 次    | Delete 请求时间超过1s的数量                      | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverServerSlowSlowappendcount                  | 慢操作次数_slowAppendCount                         | 次    | Append 请求时间超过1s的数量                      | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverStarttimeRegionserverstarttime             | 进程启动时间_regionServerStartTime                 | s     | 进程启动时间                                     | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverServerBlockcacheCountBlockcachemisscount   | 缓存块数量_blockCacheMissCount                     | 个    | Block Cache miss 请求数                          | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverServerBlockcacheCountBlockcachehitcount    | 缓存块数量_blockCacheHitCount                      | 个    | Block Cache hit 请求数                           | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverServerBlockcacheCountBlockcachecount       | 缓存块数量_blockCacheCount                         | 个    | Block Cache 中的 Block 数量                      | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverServerBlockcacheSizeBlockcachesize         | 缓存块内存占用大小_blockCacheSize                  | B     | 缓存块内存占用大小                               | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverReqcountWrite                              | 读写请求量_Write                                   | 个/秒 | 写请求量                                         | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverReqcountTotal                              | 读写请求量_Total                                   | 个/秒 | 总请求量，当有Scan请求时，该值会小于读写请求之和 | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverReqcountScantimeNumOps                     | 读写请求量_Scantime                                | ms    | Scan 请求时间                                    | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverReqcountScansizeNumOps                     | 读写请求量_Scansize                                | 个/秒 | Scan 请求量                                      | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverReqcountRead                               | 读写请求量_Read                                    | 个/秒 | 读请求量                                         | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverReqcountPutNumOps                          | 读写请求量_Put                                     | 个/秒 | Put 请求量                                       | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverReqcountIncrementNumOps                    | 读写请求量_Increment                               | 个/秒 | Increment请求量                                  | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverReqcountGetNumOps                          | 读写请求量_Get                                     | 个/秒 | Get 请求量                                       | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverReqcountDeleteNumOps                       | 读写请求量_Delete                                  | 个/秒 | Delete 请求量                                    | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverReqcountAppendNumOps                       | 读写请求量_Append_num_ops                          | 个/秒 | Append 请求量                                    | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverIpcBytesSentbytes                          | 读写流量_sentBytes                                 | B/s   | 读写流量                                         | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverIpcBytesReceivedbytes                      | 读写流量_receivedBytes                             | B/s   | 接收数据量                                       | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverServerBlockcachePercentBlockcacheexpresshi | 读缓存命中率_blockCacheExpressHitPercent           | %     | 读缓存命中率                                     | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverServerQueueSplitqueuelength                | 操作队列请求数_splitQueueLength                    | 个    | Split 队列长度                                   | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverServerQueueFlushqueuelength                | 操作队列请求数_flushQueueLength                    | 个    | Region Flush 队列长度                            | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverServerQueueCompactionqueuelength           | 操作队列请求数_compactionQueueLength               | 个    | Compaction 队列长度                              | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverHlogcountHlogfilecount                     | WAL文件数量_hlogFileCount                          | 个    | WAL 文件数量                                     | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverHlogsizeHlogfilesize                       | WAL文件大小_hlogFileSize                           | B     | WAL 文件大小                                     | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverStoreCountStorecount                       | Store个数_storeCount                               | 个    | Store 个数                                       | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverStorefilecountStorefilecount               | Storefile个数_storeFileCount                       | 个    | Storefile 个数                                   | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverStorefilesizeStorefilesize                 | Storefile大小_storeFileSize                        | MB    | Storefile 大小                                   | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverServerSplitSplitsuccesscount               | split请求_splitSuccessCount                        | 次    | split 成功次数                                   | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverServerSplitSplitrequestcount               | split请求_splitRequestCount                        | 个    | split 请求数                                     | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverServerFlushFlushtimeNumOps                 | RS写磁盘次数_FlushTime_num_ops                     | 次    | Memstore flush 写磁盘次数                        | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverIpcExceptionUnknownscannerexception        | RPC异常次数_UnknownScannerException                | 次    | UnknownScannerException 异常次数                 | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverIpc<ExceptionRegiontoobusyexception        | RPC异常次数_RegionTooBusyException                 | 次    | RegionTooBusyException 异常次数                  | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverIpcExceptionRegionmovedexception           | RPC异常次数_RegionMovedException                   | 次    | RegionMovedException 异常次数                    | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverIpcExceptionOutoforderscannernextexception | RPC异常次数_OutOfOrderScannerNextException         | 次    | OutOfOrderScannerNextException 异常次数          | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverIpcExceptionNotservingregionexception      | RPC异常次数_NotServingRegionException              | 次    | NotServingRegionException 异常次数               | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverIpcExceptionFailedsanitycheckexception     | RPC异常次数_FailedSanityCheckException             | 次    | FailedSanityCheckException 异常次数              | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverIpcAuthenticationAuthenticationsuccesses   | RPC认证次数_authenticationSuccesses                | 次    | RPC 认证成功次数                                 | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverIpcAuthenticationAuthenticationfailures    | RPC认证次数_authenticationFailures                 | 次    | RPC 认证失败次数                                 | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverIpcConnectionsNumopenconnections           | RPC连接数_numOpenConnections                       | 个    | RPC 连接数                                       | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverIpcHandlerNumactivehandler                 | RPC句柄数_numActiveHandler                         | 个    | RPC 句柄数                                       | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverIpcQueueNumcallsinreplicationqueue         | RPC队列请求数_numCallsInReplicationQueue           | 个    | 复制队列 RPC 请求数                              | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverIpcQueueNumcallsinpriorityqueue            | RPC队列请求数_numCallsInPriorityQueue              | 个    | 优先队列 RPC 请求数                              | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverIpcQueueNumcallsingeneralqueue             | RPC队列请求数_numCallsInGeneralQueue               | 个    | 通用队列 RPC 请求数                              | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverServerReplayReplayNumOps                   | Replay操作次数_Replay_num_ops                      | 次    | Replay操作次数                                   | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverAvgsizeAverageregionsize                   | Region平均大小_averageRegionSize                   | B     | Region平均大小                                   | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverRegionCountRegioncount                     | Region个数_regionCount                             | 个    | Region 个数                                      | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverServerHfilesPercentPercentfileslocalsecond | Region副本本地化_percentFilesLocalSecondaryRegions | %     | Region副本本地化                                 | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverServerMutationSizeMutationswithoutwalsize  | mutation大小_mutationsWithoutWALSize               | B     | mutation大小                                     | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverServerMutationCountMutationswithoutwalcoun | muation个数_mutationsWithoutWALCount               | 个    | mutation 个数                                    | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverMemstroreMemstoresize                      | Memstore大小_memStoreSize                          | MB    | Memstore 大小                                    | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverJvmThreadsThreadswaiting                   | JVM线程数量_ThreadsWaiting                         | 个    | 处于 WAITING 状态的线程数量                      | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverJvmThreadsThreadstimedwaiting              | JVM线程数量_ThreadsTimedWaiting                    | 个    | 处于 TIMED WAITING 状态的线程数量                | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverJvmThreadsThreadsterminated                | JVM线程数量_ThreadsTerminated                      | 个    | 当前 TERMINATED 状态线程数量                     | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverJvmThreadsThreadsrunnable                  | JVM线程数量_ThreadsRunnable                        | 个    | 处于 RUNNABLE 状态的线程数量                     | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverJvmThreadsThreadsnew                       | JVM线程数量_ThreadsNew                             | 个    | 处于 NEW 状态的线程数量                          | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverJvmThreadsThreadsblocked                   | JVM线程数量_ThreadsBlocked                         | 个    | 处于 BLOCKED 状态的线程数量                      | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverJvmLogTotalLogwarn                         | JVM日志数量_LogWarn                                | 个    | Warn日志数量                                     | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverJvmLogTotalLoginfo                         | JVM日志数量_LogInfo                                | 个    | Info日志数量                                     | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverJvmLogTotalLogfatal                        | JVM日志数量_LogFatal                               | 个    | Fatal 日志数量                                   | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverJvmLogTotalLogerror                        | JVM日志数量_LogError                               | 个    | Error 日志数量                                   | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverJvmMemMemnonheapusedm                      | JVM内存_MemNonHeapUsedM                            | MB    | 进程使用的非堆内存大小                           | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverJvmMemMemnonheapcommittedm                 | JVM内存_MemNonHeapCommittedM                       | MB    | 进程 commit 的非堆内存大小                       | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverJvmMemMemmaxm                              | JVM内存_MemMaxM                                    | MB    | 进程最大内存大小                                 | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverJvmMemMemheapusedm                         | JVM内存_MemHeapUsedM                               | MB    | 进程使用的堆内存大小                             | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverJvmMemMemheapmaxm                          | JVM内存_MemHeapMaxM                                | MB    | 进程最大的堆内存大小                             | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseRegionserverJvmMemMemheapcommittedm                    | JVM内存_MemHeapCommittedM                          | MB    | 进程 commit 的堆内存大小                         | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseHsGcUtilGcTimeYgct                                     | GC时间_YGCT                                        | s     | Young GC 消耗时间                                | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseHsGcUtilGcTimeGct                                      | GC时间_GCT                                         | s     | 垃圾回收时间消耗                                 | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseHsGcUtilGcTimeFgct                                     | GC时间_FGCT                                        | s     | Full GC 消耗时间                                 | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseHsGcUtilGcCountYgc                                     | GC次数_YGC                                         | 次    | Young GC 次数                                    | host4hbasehmaster、<br>id4hbasehmaster |
| HbaseHsGcUtilGcCountFgc                                     | GC次数_FGC                                         | 次    | Full GC 次数                                     | host4hbasehmaster、<br>id4hbasehmaster |

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
