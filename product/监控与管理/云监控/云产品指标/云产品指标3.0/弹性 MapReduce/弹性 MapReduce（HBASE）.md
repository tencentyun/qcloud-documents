## 命名空间

Namespace=QCE/TXMR_HBASE

## 监控指标

### Hbase-Overview

| 指标中文名                                                   | 指标中文名                                    | 指标单位 | 指标含义                    | 维度                                      |
| ------------------------------------------------------------ | --------------------------------------------- | -------- | --------------------------- | ----------------------------------------- |
| EmrHbaseOverview<br>HbaseMasterAssignment<br>managerRitRitcount | 集群处于 RITRegion 个数_ritCount              | 个       | 集群处于  RIT Region 个数   | host4hbaseoverview、<br>id4hbaseoverview  |
| EmrHbaseOverview<br/>HbaseMaster<br>Assignmentmanager<br>RitRitcountoverthreshold | 集群处于 RITRegion 个数_ritCountOverThreshold | 个       | 集群处于  RIT Region 个数   | host4hbaseoverview、<br>id4hbaseoverview  |
| EmrHbaseOverview<br/>HbaseMaster<br>Assignmentmanager<br>TimeRitoldestage | 集群 RIT 时间_ritOldestAge                    | ms       | 集群  RIT 时间              | host4hbaseoverview、<br/>id4hbaseoverview |
| EmrHbaseOverview<br/>HbaseMaster<br>AvgloadAverageload       | 每个 RS 平均 REGION 数_averageLoad            | 个       | 每个  RS 平均 REGION 数     | host4hbaseoverview、<br/>id4hbaseoverview |
| EmrHbaseOverview<br/>HbaseMasterRsnums<br>Numregionservers   | 集群 RS 数量_numRegionServers                 | 个       | 集群  RS 数量               | host4hbaseoverview、<br/>id4hbaseoverview |
| EmrHbaseOverview<br/>HbaseMasterRsnumsNum<br>deadregionservers | 集群 RS 数量_numDeadRegionServers             | 个       | 集群  RS 数量               | host4hbaseoverview、<br/>id4hbaseoverview |
| EmrHbaseOverview<br/>HbaseMaster<br>BytesReceivedbytes       | 集群读写数量_receivedBytes                    | bytes/s  | 集群读写数量                | host4hbaseoverview、<br/>id4hbaseoverview |
| EmrHbaseOverview<br/>HbaseMaster<br>BytesSentbytes           | 集群读写数量_sentBytes                        | bytes/s  | 集群读写数量                | host4hbaseoverview、<br/>id4hbaseoverview |
| EmrHbaseOverview<br/>HbaseMasterReq<br>Clusterrequests       | 集群总请求数量\_clusterRequests                | 个/s     | 集群总请求数量              | host4hbaseoverview、<br/>id4hbaseoverview |
| EmrHbaseOverview<br/>HbaseMaster<br>Assignmentmanager<br>OpsAssignNumOps | 集群 Assignment 管理器操作\_Assign_num_ops     | 次       | 集群  Assignment 管理器操作 | host4hbaseoverview、<br/>id4hbaseoverview |
| EmrHbaseOverview<br/>HbaseMaste<br>rAssignmentmanager<br>OpsBulkassignNumOps | 集群 Assignment 管理器操作\_BulkAssign_num_ops | 次       | 集群  Assignment 管理器操作 | host4hbaseoverview、<br/>id4hbaseoverview |
| EmrHbaseOverview<br/>HbaseMasterBalancerOps<br>BalancerclusterNumOps | 集群负载均衡次数\_BalancerclusterNum                    | 次       | 集群负载均衡次数            | host4hbaseoverview、<br/>id4hbaseoverview |
| EmrHbaseOverview<br/>HbaseMasterServerPlan<br>Mergeplancount | 集群 Plan_mergePlanCount                      | 个       | 集群  Plan                  | host4hbaseoverview、<br/>id4hbaseoverview |
| EmrHbaseOverview<br/>HbaseMasterServerPlan<br>Splitplancount | 集群 Plan_splitPlanCount                      | 个       | 集群  Plan                  | host4hbaseoverview、<br/>id4hbaseoverview |

### Hbase-OverviewAggregation

| 指标中文名                                                   | 指标中文名                                    | 指标单位 | 指标含义                    | 维度             |
| ------------------------------------------------------------ | --------------------------------------------- | -------- | --------------------------- | ---------------- |
| EmrHbaseOverviewAggregation<br>HbaseMasterAssignment<br>managerRitRitcount | 集群处于 RITRegion 个数_ritCount              | 个       | 集群处于  RIT Region 个数   | id4hbaseoverview |
| EmrHbaseOverviewAggregation<br/>HbaseMasterAssign<br>mentmanagerRitRitcountover<br>threshold | 集群处于 RITRegion 个数_ritCountOverThreshold | 个       | 集群处于  RIT Region 个数   | id4hbaseoverview |
| EmrHbaseOverviewAggregation<br/>HbaseMasterAssign<br>mentmanager TimeRitoldestage | 集群 RIT 时间_ritOldestAge                    | ms       | 集群  RIT 时间              | id4hbaseoverview |
| EmrHbaseOverviewAggregation<br/>HbaseMaster AvgloadAverageload | 每个 RS 平均REGION数_averageLoad              | 个       | 每个  RS 平均 REGION 数     | id4hbaseoverview |
| EmrHbaseOverviewAggregation<br/>HbaseMasterRsnums<br>Numregionservers | 集群 RS 数量_numRegionServers                 | 个       | 集群  RS 数量               | id4hbaseoverview |
| EmrHbaseOverviewAggregation<br/>HbaseMasterRsnumsNum <br>deadregionservers | 集群 RS 数量_numDeadRegionServers             | 个       | 集群  RS 数量               | id4hbaseoverview |
| EmrHbaseOverviewAggregation<br/>HbaseMaster BytesReceivedbytes | 集群读写数量_receivedBytes                    | bytes/s  | 集群读写数量                | id4hbaseoverview |
| EmrHbaseOverviewAggregation<br/>HbaseMaster<br>BytesSentbytes | 集群读写数量_sentBytes                        | bytes/s  | 集群读写数量                | id4hbaseoverview |
| EmrHbaseOverviewAggregation<br/>HbaseMasterReq<br>Clusterrequests | 集群总请求数量_clusterRequests                | 个/s     | 集群总请求数量              | id4hbaseoverview |
| EmrHbaseOverviewAggregation<br/>HbaseMasterAssign<br>mentmanagerOpsAssignNumOps | 集群 Assignment 管理器操作\_Assign_num_ops     | 次       | 集群  Assignment 管理器操作 | id4hbaseoverview |
| EmrHbaseOverviewAggregation<br/>HbaseMasterAssign<br/>mentmanagerOpsBulkassignNumOps | 集群 Assignment 管理器操作\_BulkAssign_num_ops | 次       | 集群  Assignment 管理器操作 | id4hbaseoverview |
| EmrHbaseOverviewAggregation<br/>HbaseMasterBalancerOps<br>BalancerclusterNumOps | 集群负载均衡次数\_BalancerclusterNum                    | 次       | 集群负载均衡次数            | id4hbaseoverview |
| EmrHbaseOverviewAggregation<br/>HbaseMasterServerPlan<br>Mergeplancount | 集群 Plan_mergePlanCount                      | 个       | 集群  Plan                  | id4hbaseoverview |
| EmrHbaseOverviewAggregation<br/>HbaseMasterServerPlan<br>Splitplancount | 集群 Plan_splitPlanCount                      | 个       | 集群  Plan                  | id4hbaseoverview |

### HBASE-HMaster

| 指标中文名                                            | 指标中文名                                 | 指标单位 | 指标含义       | 维度                                |
| ----------------------------------------------------- | ------------------------------------------ | -------- | -------------- | ----------------------------------- |
| HbaseHmGcUtilGcCounYgc                                | GC次数_FGC                                 | 次       | GC 次数        | host4hbasehmaster、 id4hbasehmaster |
| HbaseHmGcUtilGcCountgc                                | GC次数_YGC                                 | 次       | GC 次数        | host4hbasehmaster、 id4hbasehmaster |
| HbaseHmGcUtilGcTimeFgct                               | GC时间_FGCT                                | s        | GC 时间        | host4hbasehmaster、 id4hbasehmaster |
| HbaseHmGcUtilGcTimeGct                                | GC时间_GCT                                 | s        | GC 时间        | host4hbasehmaster、 id4hbasehmaster |
| HbaseHmGcUtilGcTimeYgct                               | GC时间_YGCT                                | s        | GC 时间        | host4hbasehmaster、 id4hbasehmaster |
| HbaseHmGcUtilMemoryCcs                                | 内存区域占比_CCS                           | %        | 内存区域占比   | host4hbasehmaster、 id4hbasehmaster |
| HbaseHmGcUtilMemoryE                                  | 内存区域占比_E                             | %        | 内存区域占比   | host4hbasehmaster、 id4hbasehmaster |
| HbaseHmGcUtilMemoryM                                  | 内存区域占比_M                             | %        | 内存区域占比   | host4hbasehmaster、 id4hbasehmaster |
| HbaseHmGcUtilMemoryO                                  | 内存区域占比_O                             | %        | 内存区域占比   | host4hbasehmaster、 id4hbasehmaster |
| HbaseHmGcUtilMemoryS0                                 | 内存区域占比_S0                            | %        | 内存区域占比   | host4hbasehmaster、 id4hbasehmaster |
| HbaseHmGcUtilMemoryS1                                 | 内存区域占比_S1                            | %        | 内存区域占比   | host4hbasehmaster、 id4hbasehmaster |
| HbaseMasterIpcConnectionsNumopenconnections           | RPC连接数_numOpenConnections               | 次       | RPC 连接数     | host4hbasehmaster、 id4hbasehmaster |
| HbaseMasterIpcExceptionFailedsanitycheckexception     | RPC异常次数_FailedSanityCheckException     | 次       | RPC 异常次数   | host4hbasehmaster、 id4hbasehmaster |
| HbaseMasterIpcExceptionNotservingregionexception      | RPC异常次数_NotServingRegionException      | 次       | RPC 异常次数   | host4hbasehmaster、 id4hbasehmaster |
| HbaseMasterIpcExceptionOutoforderscannernextexception | RPC异常次数_OutOfOrderScannerNextException | 次       | RPC 异常次数   | host4hbasehmaster、 id4hbasehmaster |
| HbaseMasterIpcExceptionRegionmovedexception           | RPC异常次数_RegionMovedException           | 次       | RPC 异常次数   | host4hbasehmaster、 id4hbasehmaster |
| HbaseMasterIpcExceptionRegiontoobusyexception         | RPC异常次数_RegionTooBusyException         | 次       | RPC 异常次数   | host4hbasehmaster、 id4hbasehmaster |
| HbaseMasterIpcExceptionUnknownscannerexception        | RPC异常次数_UnknownScannerException        | 次       | RPC 异常次数   | host4hbasehmaster、 id4hbasehmaster |
| HbaseMasterIpcQueueNumcallsinpriorityqueue            | RPC队列请求数_numCallsInPriorityQueue      | 次       | RPC 队列请求数 | host4hbasehmaster、 id4hbasehmaster |
| HbaseMasterIpcQueueNumcallsinreplicationqueue         | RPC队列请求数_numCallsInReplicationQueue   | 次       | RPC 队列请求数 | host4hbasehmaster、 id4hbasehmaster |
| HbaseMasterJvmLogTotalLogerror                        | JVM日志数量_LogError                       | 个       | JVM 日志数量   | host4hbasehmaster、 id4hbasehmaster |
| HbaseMasterJvmLogTotalLogfatal                        | JVM日志数量_LogFatal                       | 个       | JVM 日志数量   | host4hbasehmaster、 id4hbasehmaster |
| HbaseMasterJvmLogTotalLoginfo                         | JVM日志数量_LogInfo                        | 个       | JVM 日志数量   | host4hbasehmaster、 id4hbasehmaster |
| HbaseMasterJvmLogTotalLogwarn                         | JVM日志数量_LogWarn                        | 个       | JVM 日志数量   | host4hbasehmaster、 id4hbasehmaster |
| HbaseMasterJvmMemMemheapcommittedm                    | JVM内存_MemHeapCommittedM                  | MB       | JVM 内存       | host4hbasehmaster、 id4hbasehmaster |
| HbaseMasterJvmMemMemheapmaxm                          | JVM内存_MemHeapMaxM                        | MB       | JVM 内存       | host4hbasehmaster、 id4hbasehmaster |
| HbaseMasterJvmMemMemheapusedm                         | JVM内存_MemHeapUsedM                       | MB       | JVM 内存       | host4hbasehmaster、 id4hbasehmaster |
| HbaseMasterJvmMemMemmaxm                              | JVM内存_MemMaxM                            | MB       | JVM 内存       | host4hbasehmaster、 id4hbasehmaster |
| HbaseMasterJvmMemMemnonheapcommittedm                 | JVM内存_MemNonHeapCommittedM               | 个       | JVM 线程数量   | host4hbasehmaster、 id4hbasehmaster |
| HbaseMasterJvmMemMemnonheapusedm                      | JVM内存_MemNonHeapUsedM                    | 个       | JVM 线程数量   | host4hbasehmaster、 id4hbasehmaster |
| HbaseMasterJvmThreadsThreadsblocked                   | JVM线程数量_ThreadsBlocked                 | 个       | JVM 线程数量   | host4hbasehmaster、 id4hbasehmaster |
| HbaseMasterJvmThreadsThreadsnew                       | JVM线程数量_ThreadsNew                     | 个       | JVM 线程数量   | host4hbasehmaster、 id4hbasehmaster |
| HbaseMasterJvmThreadsThreadsrunnable                  | JVM线程数量_ThreadsRunnable                | 个       | JVM 线程数量   | host4hbasehmaster、 id4hbasehmaster |
| HbaseMasterJvmThreadsThreadsterminated                | JVM线程数量_ThreadsTerminated              | 个       | JVM 线程数量   | host4hbasehmaster、 id4hbasehmaster |
| HbaseMasterJvmThreadsThreadstimedwaiting              | JVM线程数量_ThreadsTimedWaiting            | 个       | JVM 线程数量   | host4hbasehmaster、 id4hbasehmaster |
| HbaseMasterJvmThreadsThreadswaiting                   | JVM线程数量_ThreadsWaiting                 | 个       | JVM 线程数量   | host4hbasehmaster、 id4hbasehmaster |
| HbaseMasterServerTimeMasteractivetime                 | 进程启动时间_masterActiveTime              | s        | 进程启动时间   | host4hbasehmaster、 id4hbasehmaster |
| HbaseMasterServerTimeMasterstarttime                  | 进程启动时间_masterStartTime               | s        | 进程启动时间   | host4hbasehmaster、 id4hbasehmaster |

### HBASE-RegionServer

| 指标中文名                                                   | 指标中文名                                         | 指标单位 | 指标含义           | 维度                                         |
| ------------------------------------------------------------ | -------------------------------------------------- | -------- | ------------------ | -------------------------------------------- |
| HbaseHsGcUtilGcCountYgc | GC 次数_YGC      | 次   | GC 次数      | host4hbaseregionserver、 id4hbaseregionserver |
| HbaseHsGcUtilGcCountFgc | GC 次数_FGC      | 次   | GC 次数      | host4hbaseregionserver、 id4hbaseregionserver |
| HbaseHsGcUtilGcTimeFgct | GC 时间_FGCT     | s    | GC 时间      | host4hbaseregionserver、 id4hbaseregionserver |
| HbaseHsGcUtilGcTimeGct  | GC 时间_GCT      | s    | GC 时间      | host4hbaseregionserver、 id4hbaseregionserver |
| HbaseHsGcUtilGcTimeYgct | GC 时间_YGCT     | s    | GC 时间      | host4hbaseregionserver id4hbaseregionserver   |
| HbaseHsGcUtilMemoryS0   | 内存区域占比_S0  | %    | 内存区域占比 | host4hbaseregionserver、 id4hbaseregionserver |
| HbaseHsGcUtilMemoryE    | 内存区域占比_E   | %    | 内存区域占比 | host4hbaseregionserver、 id4hbaseregionserver |
| HbaseHsGcUtilMemoryCcs  | 内存区域占比_CCS | %    | 内存区域占比 | host4hbaseregionserver、 id4hbaseregionserver |
| HbaseHsGcUtilMemoryS1   | 内存区域占比_S1  | %    | 内存区域占比 | host4hbaseregionserver、 id4hbaseregionserver |
| HbaseHsGcUtilMemoryO    | 内存区域占比_O   | %    | 内存区域占比 | host4hbaseregionserver、 id4hbaseregionserver |
| HbaseHsGcUtilMemoryM    | 内存区域占比_M   | %    | 内存区域占比 | host4hbaseregionserver、 id4hbaseregionserver |
| HbaseRegionserver<br>AvgsizeAverageregionsize                | Region平均大小_averageRegionSize                   | B        | Region平均大小     | host4hbaseregionserver、id4hbaseregionserver |
| HbaseRegionserver<br/>HlogcountHlogfilecount                 | WAL文件数量_hlogFileCount                          | 个       | WAL文件数量        | host4hbaseregionserver、id4hbaseregionserver |
| HbaseRegionserver<br/>HlogsizeHlogfilesize                   | WAL文件大小_hlogFileSize                           | B        | WAL文件大小        | host4hbaseregionserver、id4hbaseregionserver |
| HbaseRegionserverIpc<br/>AuthenticationAuthenticationfailures | RPC认证次数_authenticationFailures                 | 次       | RPC认证次数        | host4hbaseregionserver、id4hbaseregionserver |
| HbaseRegionserverIpc<br/>AuthenticationAuthenticationsuccesses | RPC认证次数_authenticationSuccesses                | Count    | RPC认证次数        | host4hbaseregionserver、id4hbaseregionserver |
| HbaseRegionserver<br/>IpcBytesReceivedbytes                  | 读写流量_receivedBytes                             | B/s      | 读写流量           | host4hbaseregionserver、id4hbaseregionserver |
| HbaseRegionserver<br/>IpcBytesSentbytes                      | 读写流量_sentBytes                                 | Bs       | 读写流量           | host4hbaseregionserver、id4hbaseregionserver |
| HbaseRegionserverIpc<br/>ConnectionsNumopenconnections       | RPC连接数_numOpenConnections                       | 次       | RPC连接数          | host4hbaseregionserver、id4hbaseregionserver |
| HbaseRegionserverIpcException<br/>Failedsanitycheckexception | RPC异常次数_FailedSanityCheckException             | 次       | RPC异常次数        | host4hbaseregionserver、id4hbaseregionserver |
| HbaseRegionserverIpcException<br/>Notservingregionexception  | RPC异常次数_NotServingRegionException              | 次       | RPC异常次数        | host4hbaseregionserver、id4hbaseregionserver |
| HbaseRegionserverIpcException<br/>Outoforderscannernextexception | RPC异常次数_OutOfOrderScannerNextException         | 次       | RPC异常次数        | host4hbaseregionserver、id4hbaseregionserver |
| HbaseRegionserverIpcException<br/>Regionmovedexception       | RPC异常次数_RegionMovedException                   | 次       | RPC异常次数        | host4hbaseregionserver、id4hbaseregionserver |
| HbaseRegionserverIpcException<br/>Regiontoobusyexception     | RPC异常次数_RegionTooBusyException                 | 次       | RPC异常次数        | host4hbaseregionserver、id4hbaseregionserver |
| HbaseRegionserverIpcException<br/>Unknownscannerexception    | RPC异常次数_UnknownScannerException                | 次       | RPC异常次数        | host4hbaseregionserver、id4hbaseregionserver |
| HbaseRegionserverIpc<br/>HandlerNumactivehandler             | RPC句柄数_numActiveHandler                         | 个       | RPC句柄数          | host4hbaseregionserver、id4hbaseregionserver |
| HbaseRegionserverIpc<br/>QueueNumcallsingeneralqueue         | RPC队列请求数_numCallsInGeneralQueue               | 个       | RPC队列请求数      | host4hbaseregionserver、id4hbaseregionserver |
| HbaseRegionserverIpc<br/>QueueNumcallsinpriorityqueue        | RPC队列请求数_numCallsInPriorityQueue              | 个       | RPC队列请求数      | host4hbaseregionserver、id4hbaseregionserver |
| HbaseRegionserverIpc<br/>QueueNumcallsinreplicationqueue     | RPC队列请求数_numCallsInReplicationQueue           | 个       | RPC队列请求数      | host4hbaseregionserver、id4hbaseregionserver |
| HbaseRegionserverJvm<br/>LogTotalLogerror                    | JVM日志数量_LogError                               | 个       | JVM日志数量        | host4hbaseregionserver、id4hbaseregionserver |
| HbaseRegionserverJvm<br/>LogTotalLogfatal                    | JVM日志数量_LogFatal                               | 个       | JVM日志数量        | host4hbaseregionserver、id4hbaseregionserver |
| HbaseRegionserverJvm<br/>LogTotalLoginfo                     | JVM日志数量_LogInfo                                | 个       | JVM日志数量        | host4hbaseregionserver、id4hbaseregionserver |
| HbaseRegionserverJvm<br/>LogTotalLogwarn                     | JVM日志数量_LogWarn                                | 个       | JVM日志数量        | host4hbaseregionserver、id4hbaseregionserver |
| HbaseRegionserverJvm<br/>MemMemheapcommittedm                | JVM内存_MemHeapCommittedM                          | MB       | JVM内存            | host4hbaseregionserver、id4hbaseregionserver |
| HbaseRegionserverJvm<br/>MemMemheapmaxm                      | JVM内存_MemHeapMaxM                                | MB       | JVM内存            | host4hbaseregionserver、id4hbaseregionserver |
| HbaseRegionserverJvm<br/>MemMemheapusedm                     | JVM内存_MemHeapUsedM                               | MB       | JVM内存            | host4hbaseregionserver、id4hbaseregionserver |
| HbaseRegionserverJvm<br/>MemMemmaxm                          | JVM内存_MemMaxM                                    | MB       | JVM内存            | host4hbaseregionserver、id4hbaseregionserver |
| HbaseRegionserverJvm<br/>MemMemnonheapcommittedm             | JVM内存_MemNonHeapCommittedM                       | MB       | JVM内存            | host4hbaseregionserver、id4hbaseregionserver |
| HbaseRegionserverJvm<br/>MemMemnonheapusedm                  | JVM内存_MemNonHeapUsedM                            | MB       | JVM内存            | host4hbaseregionserver、id4hbaseregionserver |
| HbaseRegionserverJvm<br/>ThreadsThreadsblocked               | JVM线程数量_ThreadsBlocked                         | 个       | JVM线程数量        | host4hbaseregionserver、id4hbaseregionserver |
| HbaseRegionserverJvm<br/>ThreadsThreadsnew                   | JVM线程数量_ThreadsNew                             | 个       | JVM线程数量        | host4hbaseregionserver、id4hbaseregionserver |
| HbaseRegionserverJvm<br/>ThreadsThreadsrunnable              | JVM线程数量_ThreadsRunnable                        | 个       | JVM线程数量        | host4hbaseregionserver、id4hbaseregionserver |
| HbaseRegionserverJvm<br/>ThreadsThreadsterminated            | JVM线程数量_ThreadsTerminated                      | 个       | JVM线程数量        | host4hbaseregionserver、id4hbaseregionserver |
| HbaseRegionserverJvm<br/>ThreadsThreadstimedwaiting          | JVM线程数量_ThreadsTimedWaiting                    | 个       | JVM线程数量        | host4hbaseregionserver、id4hbaseregionserver |
| HbaseRegionserverJvm<br/>ThreadsThreadswaiting               | JVM线程数量_ThreadsWaiting                         | 个       | JVM线程数量        | host4hbaseregionserver、id4hbaseregionserver |
| HbaseRegionserver<br/>MemstroreMemstoresize                  | Memstore大小_memStoreSize                          | MB       | Memstore大小       | host4hbaseregionserver、id4hbaseregionserver |
| HbaseRegionserver<br/>RegionCountRegioncount                 | Region个数_regionCount                             | 个       | Region个数         | host4hbaseregionserver、id4hbaseregionserver |
| HbaseRegionserver<br/>ReqcountAppendNumOps                   | 读写请求量_Append_num_ops                          | 个/秒    | 读写请求量         | host4hbaseregionserver、id4hbaseregionserver |
| HbaseRegionserver<br/>ReqcountRead                           | 读写请求量_Read                                    | 个/秒    | 读写请求量         | host4hbaseregionserver、id4hbaseregionserver |
| HbaseRegionserverReqcountTotal                               | 读写请求量_Total                                   | 个/秒    | 读写请求量         | host4hbaseregionserver、id4hbaseregionserver |
| HbaseRegionserverReqcountWrite                               | 读写请求量_Write                                   | 个/秒    | 读写请求量         | host4hbaseregionserver、id4hbaseregionserver |
| HbaseRegionserverServer<br/>BlockcacheCountBlockcachecount   | 缓存块数量_blockCacheCount                         | 个       | 缓存块数量         | host4hbaseregionserver、id4hbaseregionserver |
| HbaseRegionserverServer<br/>BlockcacheCountBlockcachehitcount | 缓存块数量_blockCacheHitCount                      | 个       | 缓存块数量         | host4hbaseregionserver、id4hbaseregionserver |
| HbaseRegionserverServerBlock<br/>cacheCountBlockcachemisscount | 缓存块数量_blockCacheMissCount                     | 个       | 缓存块数量         | host4hbaseregionserver、id4hbaseregionserver |
| HbaseRegionserverServerBlock<br/>cachePercentBlockcacheexpresshi | 读缓存命中率_blockCacheExpressHitPercent           | %        | 读缓存命中率       | host4hbaseregionserver、id4hbaseregionserver |
| HbaseRegionserverServerBlock<br/>cacheSizeBlockcachesize     | 缓存块内存占用大小_blockCacheSize                  | B        | 缓存块内存占用大小 | host4hbaseregionserver、id4hbaseregionserver |
| HbaseRegionserverServer<br/>CellsFlushedcellssize            | 写磁盘速率_flushedCellsSize                        | B/s      | 写磁盘速率         | host4hbaseregionserver、id4hbaseregionserver |
| HbaseRegionserverServer<br/>DelayAppendMean                  | 平均延时_Append_mean                               | ms       | 平均延时           | host4hbaseregionserver、id4hbaseregionserver |
| HbaseRegionserverServer<br/>DelayGetMean                     | 平均延时_Get_mean                                  | ms       | 平均延时           | host4hbaseregionserver、id4hbaseregionserver |
| HbaseRegionserverServer<br/>DelayReplayMean                  | 平均延时_Replay_mean                               | ms       | 平均延时           | host4hbaseregionserver、id4hbaseregionserver |
| HbaseRegionserverServer<br/>DelayUpdatesblockedtime          | 平均延时_updatesBlockedTime                        | ms       | 平均延时           | host4hbaseregionserver、id4hbaseregionserver |
| HbaseRegionserverServer<br/>FlushFlushtimeNumOps             | RS写磁盘次数_FlushTime_num_ops                     | 次       | RS写磁盘次数       | host4hbaseregionserver、id4hbaseregionserver |
| HbaseRegionserverServer<br/>HfilesPercentPercentfileslocalsecond | Region副本本地化_percentFilesLocalSecondaryRegions | %        | Region副本本地化   | host4hbaseregionserver、id4hbaseregionserver |
| HbaseRegionserverServer<br/>IndexStaticbloomsize             | 索引大小_staticBloomSize                           | B        | 索引大小           | host4hbaseregionserver、id4hbaseregionserver |
| HbaseRegionserverServer<br/>IndexStaticindexsize             | 索引大小_staticIndexSize                           | B        | 索引大小           | host4hbaseregionserver、id4hbaseregionserver |
| HbaseRegionserverServer<br/>IndexStorefileindexsize          | 索引大小_storeFileIndexSize                        | B        | 索引大小           | host4hbaseregionserver、id4hbaseregionserver |
| HbaseRegionserver<br/>ServerMutation<br/>CountMutationswithoutwalcoun | muation个数_mutationsWithoutWALCount               | 个       | muation个数        | host4hbaseregionserver、id4hbaseregionserver |
| HbaseRegionserver<br/>ServerMutation<br/>SizeMutationswithoutwalsize | mutation大小_mutationsWithoutWALSize               | Bytes    | mutation大小       | host4hbaseregionserver、id4hbaseregionserver |
| HbaseRegionserverServer<br/>QueueCompactionqueuelength       | 操作队列请求数_compactionQueueLength               | 个       | 操作队列请求数     | host4hbaseregionserver、id4hbaseregionserver |
| HbaseRegionserverServer<br/>QueueFlushqueuelength            | 操作队列请求数_flushQueueLength                    | 个       | 操作队列请求数     | host4hbaseregionserver、id4hbaseregionserver |
| HbaseRegionserverServer<br/>QueueSplitqueuelength            | 操作队列请求数_splitQueueLength                    | 个       | 操作队列请求数     | host4hbaseregionserver、id4hbaseregionserver |
| HbaseRegionserverServer<br/>ReplayReplayNumOps               | Replay操作次数_Replay_num_ops                      | 次       | Replay操作次数     | host4hbaseregionserver、id4hbaseregionserver |
| HbaseRegionserverServer<br/>SlowSlowappendcount              | 慢操作次数_slowAppendCount                         | 次       | 慢操作次数         | host4hbaseregionserver、id4hbaseregionserver |
| HbaseRegionserverServer<br/>SlowSlowdeletecount              | 慢操作次数_slowDeleteCount                         | 次       | 慢操作次数         | host4hbaseregionserver、id4hbaseregionserver |
| HbaseRegionserverServer<br/>SlowSlowgetcount                 | 慢操作次数_slowGetCount                            | 次       | 慢操作次数         | host4hbaseregionserver、id4hbaseregionserver |
| HbaseRegionserverServer<br/>SlowSlowincrementcount           | 慢操作次数_slowIncrementCount                      | 次       | 慢操作次数         | host4hbaseregionserver、id4hbaseregionserver |
| HbaseRegionserverServer<br/>SlowSlowputcount                 | 慢操作次数_slowPutCount                            | 次       | 慢操作次数         | host4hbaseregionserver、id4hbaseregionserver |
| HbaseRegionserverServer<br/>SplitSplitrequestcount           | split请求_splitRequestCount                        | 个       | split请求          | host4hbaseregionserver、id4hbaseregionserver |
| HbaseRegionserverServer<br/>SplitSplitsuccesscount           | split请求_splitSuccessCount                        | 个       | split请求          | host4hbaseregionserver、id4hbaseregionserver |
| HbaseRegionserverStarttime<br/>Regionserverstarttime         | 进程启动时间_regionServerStartTime                 | s        | 进程启动时间       | host4hbaseregionserver、id4hbaseregionserver |
| HbaseRegionserverStore<br/>CountStorecount                   | Store个数_storeCount                               | 个       | Store个数          | host4hbaseregionserver、id4hbaseregionserver |
| HbaseRegionserverStore<br/>filecountStorefilecount           | Storefile个数_storeFileCount                       | 个       | Storefile个数      | host4hbaseregionserver、id4hbaseregionserver |
| HbaseRegionserverStore<br/>filesizeStorefilesize             | Storefile大小_storeFileSize                        | MB       | Storefile大小      | host4hbaseregionserver、id4hbaseregionserver |


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


