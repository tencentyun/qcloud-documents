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

| 指标英文名                                                   | 指标中文名                                  | 指标单位 | 指标含义        | 维度                                    |
| ------------------------------------------------------------ | ------------------------------------------- | -------- | --------------- | --------------------------------------- |
| HbaseHmGcUtilGcCountYgc                                      | GC 次数_YGC                                 | 次       | GC  次数        | host4hbasehmaster、<br>id4hbasehmaster  |
| HbaseHmGcUtilGcCountFgc                                      | GC 次数_FGC                                 | 次       | GC  次数        | host4hbasehmaster、<br/>id4hbasehmaster |
| HbaseHmGcUtilGcTimeFgct                                      | GC 时间_FGCT                                | s        | GC  时间        | host4hbasehmaster、<br/>id4hbasehmaster |
| HbaseHmGcUtilGcTimeGct                                       | GC 时间_GCT                                 | s        | GC  时间        | host4hbasehmaster、<br/>id4hbasehmaster |
| HbaseHmGcUtilGcTimeYgct                                      | GC 时间_YGCT                                | s        | GC  时间        | host4hbasehmaster、<br/>id4hbasehmaster |
| HbaseHmGcUtilMemoryS0                                        | 内存区域占比_S0                             | %        | 内存区域占比    | host4hbasehmaster、<br/>id4hbasehmaster |
| HbaseHmGcUtilMemoryE                                         | 内存区域占比_E                              | %        | 内存区域占比    | host4hbasehmaster、<br/>id4hbasehmaster |
| HbaseHmGcUtilMemoryCcs                                       | 内存区域占比_CCS                            | %        | 内存区域占比    | host4hbasehmaster、<br/>id4hbasehmaster |
| HbaseHmGcUtilMemoryS1                                        | 内存区域占比_S1                             | %        | 内存区域占比    | host4hbasehmaster、<br/>id4hbasehmaster |
| HbaseHmGcUtilMemoryO                                         | 内存区域占比_O                              | %        | 内存区域占比    | host4hbasehmaster、<br/>id4hbasehmaster |
| HbaseHmGcUtilMemoryM                                         | 内存区域占比_M                              | %        | 内存区域占比    | host4hbasehmaster、<br/>id4hbasehmaster |
| HbaseMasterJvm<br>LogTotalLogfatal                           | JVM 日志数量_LogFatal                       | 次       | JVM  日志数量   | host4hbasehmaster、<br/>id4hbasehmaster |
| HbaseMasterJvm<br>LogTotalLogerror                           | JVM 日志数量_LogError                       | 次       | JVM  日志数量   | host4hbasehmaster、<br/>id4hbasehmaster |
| HbaseMasterJvm<br>LogTotalLogwarn                            | JVM 日志数量_LogWarn                        | 次       | JVM  日志数量   | host4hbasehmaster、<br/>id4hbasehmaster |
| HbaseMasterJvm<br>LogTotalLoginfo                            | JVM 日志数量_LogInfo                        | 次       | JVM  日志数量   | host4hbasehmaster、<br/>id4hbasehmaster |
| HbaseMasterJvmMem<br>Memnonheapusedm                         | JVM 内存_MemNonHeapUsedM                    | MB       | JVM  内存       | host4hbasehmaster、<br/>id4hbasehmaster |
| HbaseMasterJvmMem<br>Memnonheapcommittedm                    | JVM 内存_MemNonHeapCommittedM               | MB       | JVM  内存       | host4hbasehmaster、<br/>id4hbasehmaster |
| HbaseMasterJvmMemMem<br>heapcommittedm                       | JVM 内存_MemHeapUsedM                       | MB       | JVM  内存       | host4hbasehmaster、<br/>id4hbasehmaster |
| HbaseMasterJvmMem<br>Memheapusedm                            | JVM 内存_MemHeapUsedM                       | MB       | JVM  内存       | host4hbasehmaster、<br/>id4hbasehmaster |
| HbaseMasterJvmMem<br>Memheapcommittedm                       | JVM 内存_MemHeapCommittedM                  | MB       | JVM  内存       | host4hbasehmaster、<br/>id4hbasehmaster |
| HbaseMasterJvmMem<br>Memheapmaxm                             | JVM 内存_MemHeapMaxM                        | MB       | JVM  内存       | host4hbasehmaster、<br/>id4hbasehmaster |
| HbaseMasterJvmMem<br>Memmaxm                                 | JVM 内存_MemMaxM                            | MB       | JVM  内存       | host4hbasehmaster、<br/>id4hbasehmaster |
| HbaseMasterJvmThreads<br>Threadsnew                          | JVM 线程数量_ThreadsNew                     | 个       | JVM  线程数量   | host4hbasehmaster、<br/>id4hbasehmaster |
| HbaseMasterJvmThreads<br>Threadsrunnable                     | JVM 线程数量_ThreadsRunnable                | 个       | JVM  线程数量   | host4hbasehmaster、<br/>id4hbasehmaster |
| HbaseMasterJvmThreads<br>Threadsblocked                      | JVM 线程数量_ThreadsBlocked                 | 个       | JVM  线程数量   | host4hbasehmaster、<br/>id4hbasehmaster |
| HbaseMasterJvmThreads<br>Threadswaiting                      | JVM 线程数量_ThreadsWaiting                 | 个       | JVM  线程数量   | host4hbasehmaster、<br/>id4hbasehmaster |
| HbaseMasterJvmThreads<br>Threadstimedwaiting                 | JVM 线程数量_ThreadsTimedWaiting            | 个       | JVM  线程数量   | host4hbasehmaster、<br/>id4hbasehmaster |
| HbaseMasterJvmThreads<br>Threadsterminated                   | JVM 线程数量_ThreadsTerminated              | 个       | JVM  线程数量   | host4hbasehmaster、<br/>id4hbasehmaster |
| HbaseMasterIpcConnections<br>Numopenconnections              | RPC 连接数_numOpenConnections               | 个       | RPC  连接数     | host4hbasehmaster、<br/>id4hbasehmaster |
| HbaseMasterIpcException<br>Failedsanitycheckexception        | RPC 异常次数_FailedSanityCheckException     | 次       | RPC  异常次数   | host4hbasehmaster、<br/>id4hbasehmaster |
| HbaseMasterIpcException<br>Notservingregionexception         | RPC 异常次数_NotServingRegionException      | 次       | RPC  异常次数   | host4hbasehmaster、<br/>id4hbasehmaster |
| HbaseMasterIpcException<br>Outoforderscanner<br>nextexception | RPC 异常次数_OutOfOrderScannerNextException | 次       | RPC  异常次数   | host4hbasehmaster、<br/>id4hbasehmaster |
| HbaseMasterIpcException<br>Regionmovedexception              | RPC 异常次数_RegionMovedException           | 次       | RPC  异常次数   | host4hbasehmaster、<br/>id4hbasehmaster |
| HbaseMasterIpcException<br>Regiontoobusyexception            | RPC 异常次数_RegionTooBusyException         | 次       | RPC  异常次数   | host4hbasehmaster、<br/>id4hbasehmaster |
| HbaseMasterIpcException<br>Unknownscannerexception           | RPC 异常次数_UnknownScannerException        | 次       | RPC  异常次数   | host4hbasehmaster、<br/>id4hbasehmaster |
| HbaseMasterIpc<br>QueueNumcalls<br>inpriorityqueue           | RPC 队列请求数_numCallsInPriorityQueue      | 个       | RPC  队列请求数 | host4hbasehmaster、<br/>id4hbasehmaster |
| HbaseMasterIpc<br>QueueNumcalls<br>inreplicationqueue        | RPC 队列请求数_numCallsInReplicationQueue   | 个       | RPC  队列请求数 | host4hbasehmaster、<br/>id4hbasehmaster |
| HbaseMasterServerTime<br>Masteractivetime                    | 进程启动时间_masterActiveTime               | s        | 进程启动时间    | host4hbasehmaster、<br/>id4hbasehmaster |
| HbaseMasterServerTime<br>Masterstarttime                     | 进程启动时间_masterStartTime                | s        | 进程启动时间    | host4hbasehmaster、<br/>id4hbasehmaster |

### HBASE-RegionServer

| 指标中文名                                                   | 指标中文名                                              | 指标单位 | 指标含义           | 维度                                               |
| :----------------------------------------------------------- | ------------------------------------------------------- | -------- | ------------------ | -------------------------------------------------- |
| HbaseHsGcUtilGcCountYgc                                      | GC 次数_YGC                                             | 次       | GC 次数            | host4hbaseregionserver、<br>id4hbaseregionserver   |
| HbaseHsGcUtilGcCountFgc                                      | GC 次数_FGC                                             | 次       | GC 次数            | host4hbaseregionserver、<br> id4hbaseregionserver  |
| HbaseHsGcUtilGcTimeFgct                                      | GC 时间_FGCT                                            | s        | GC 时间            | host4hbaseregionserver、<br>id4hbaseregionserver   |
| HbaseHsGcUtilGcTimeGct                                       | GC 时间_GCT                                             | s        | GC 时间            | host4hbaseregionserver、<br>id4hbaseregionserver   |
| HbaseHsGcUtilGcTimeYgct                                      | GC 时间_YGCT                                            | s        | GC 时间            | host4hbaseregionserver<br>id4hbaseregionserver     |
| HbaseHsGcUtilMemoryS0                                        | 内存区域占比_S0                                         | %        | 内存区域占比       | host4hbaseregionserver、<br> id4hbaseregionserver  |
| HbaseHsGcUtilMemoryE                                         | 内存区域占比_E                                          | %        | 内存区域占比       | host4hbaseregionserver、<br> id4hbaseregionserver  |
| HbaseHsGcUtilMemoryCcs                                       | 内存区域占比_CCS                                        | %        | 内存区域占比       | host4hbaseregionserver、<br> id4hbaseregionserver  |
| HbaseHsGcUtilMemoryS1                                        | 内存区域占比_S1                                         | %        | 内存区域占比       | host4hbaseregionserver、<br> id4hbaseregionserver  |
| HbaseHsGcUtilMemoryO                                         | 内存区域占比_O                                          | %        | 内存区域占比       | host4hbaseregionserver、<br> id4hbaseregionserver  |
| HbaseHsGcUtilMemoryM                                         | 内存区域占比_M                                          | %        | 内存区域占比       | host4hbaseregionserver、<br> id4hbaseregionserver  |
| HbaseMasterJvmLog<br>TotalLogfatal                           | JVM 日志数量_LogFatal                                   | 次       | JVM 日志数量       | host4hbaseregionserver、<br> id4hbaseregionserver  |
| HbaseMasterJvmLog<br>TotalLogerror                           | JVM 日志数量_LogError                                   | 次       | JVM 日志数量       | host4hbaseregionserver、<br> id4hbaseregionserver  |
| HbaseMasterJvmLog<br>TotalLogwarn                            | JVM 日志数量_LogWarn                                    | 次       | JVM 日志数量       | host4hbaseregionserver、<br> id4hbaseregionserver  |
| HbaseMasterJvmLog<br>TotalLoginfo                            | JVM 日志数量_LogInfo                                    | 次       | JVM 日志数量       | host4hbaseregionserver、<br> id4hbaseregionserver  |
| HbaseMasterJvmMem<br>Memnonheapusedm                         | JVM 内存<br/>_MemNonHeapUsedM                           | MB       | JVM 内存           | host4hbaseregionserver、<br> id4hbaseregionserver  |
| HbaseMasterJvmMem<br>Memnonheapcommittedm                    | JVM 内存<br/>_MemNonHeapCommittedM                      | MB       | JVM 内存           | host4hbaseregionserver、<br> id4hbaseregionserver  |
| HbaseMasterJvmMem<br>Memheapmaxm                             | JVM 内存<br/>_MemHeapMaxM                               | MB       | JVM 内存           | host4hbaseregionserver、<br> id4hbaseregionserver  |
| HbaseMasterJvmMem<br>Memheapusedm                            | JVM 内存<br/>_MemHeapUsedM                              | MB       | JVM 内存           | host4hbaseregionserver、<br> id4hbaseregionserver  |
| HbaseMasterJvmMemMem<br>heapcommittedm                       | JVM 内存<br/>_MemHeapCommittedM                         | MB       | JVM 内存           | host4hbaseregionserver、<br> id4hbaseregionserver  |
| HbaseMasterJvmMemMem<br>heapmaxm                             | JVM 内存_MemHeapMaxM                                    | MB       | JVM 内存           | host4hbaseregionserver、<br> id4hbaseregionserver  |
| HbaseMasterJvmMem<br>Memmaxm                                 | JVM 内存_MemMaxM                                        | MB       | JVM 内存           | host4hbaseregionserver、<br> id4hbaseregionserver  |
| HbaseMasterJvm<br>ThreadsThreadsnew                          | JVM 线程数量_ThreadsNew                                 | 个       | JVM 线程数量       | host4hbaseregionserver、<br> id4hbaseregionserver  |
| HbaseMasterJvmThreads<br>Threadsrunnable                     | JVM 线程数量<br/>_ThreadsRunnable                       | 个       | JVM 线程数量       | host4hbaseregionserver、<br> id4hbaseregionserver  |
| HbaseMasterJvmThreads<br>Threadsblocked                      | JVM 线程数量<br/>_ThreadsBlocked                        | 个       | JVM 线程数量       | host4hbaseregionserver、<br> id4hbaseregionserver  |
| HbaseMasterJvmThreads<br>Threadswaiting                      | JVM 线程数量<br/>_ThreadsWaiting                        | 个       | JVM 线程数量       | host4hbaseregionserver、<br> id4hbaseregionserver  |
| HbaseMasterJvmThreads<br>Threadstimedwaiting                 | JVM 线程数量_ThreadsTimedWaiting                        | 个       | JVM 线程数量       | host4hbaseregionserver、<br> id4hbaseregionserver  |
| HbaseMasterJvmThreads<br>Threadsterminated                   | JVM 线程数量_ThreadsTerminated                          | 个       | JVM 线程数量       | host4hbaseregionserver、<br> id4hbaseregionserver  |
| HbaseRegionserver<br>AvgsizeAverageregionsize                | Region 平均大小_averageRegionSize                       | Byte     | Region 平均大小    | host4hbaseregionserver、<br> id4hbaseregionserver  |
| HbaseRegionserver<br>RegionCountRegioncount                  | Region 个数_regionCount                                 | 个       | Region 个数        | host4hbaseregionserver、<br> id4hbaseregionserver  |
| HbaseRegionserver<br>ServerHfilesPercentPercent<br>fileslocalsecond | Region 副本本地化_percentFilesLocal<br>SecondaryRegions | %        | Region 副本本地化  | host4hbaseregionserver、<br> id4hbaseregionserver  |
| HbaseRegionserver<br>IpcAuthentication<br>Authenticationfailures | RPC 认证次数_authenticationFailures                     | 次       | RPC 认证次数       | host4hbaseregionserver、<br> id4hbaseregionserver  |
| HbaseRegionserver<br>IpcAuthentication<br>Authenticationsuccesses | RPC 认证次数_authenticationSuccesses                    | 次       | RPC 认证次数       | host4hbaseregionserver、<br> id4hbaseregionserver  |
| HbaseMasterIpcConnections<br>Numopenconnections              | RPC 连接数<br/>_numOpenConnections                      | 个       | RPC 连接数         | host4hbaseregionserver、<br> id4hbaseregionserver  |
| HbaseMasterIpcException<br>Failedsanitycheckexception        | RPC 异常次数<br/>_FailedSanityCheckException            | 次       | RPC 异常次数       | host4hbaseregionserver、<br> id4hbaseregionserver  |
| HbaseMasterIpcException<br>Notservingregionexception         | RPC 异常次数<br/>_NotServingRegionException             | 次       | RPC 异常次数       | host4hbaseregionserver、<br> id4hbaseregionserver  |
| HbaseMasterIpcException<br>Outoforderscannernextexception    | RPC 异常次数<br/>_OutOfOrderScannerNext<br/>Exception   | 次       | RPC 异常次数       | host4hbaseregionserver、<br/> id4hbaseregionserver |
| HbaseMasterIpcException<br>Regionmovedexception              | RPC 异常次数_RegionMovedException                       | 次       | RPC 异常次数       | host4hbaseregionserver、<br/> id4hbaseregionserver |
| HbaseMasterIpcException<br>Regiontoobusyexception            | RPC 异常次数<br/>_RegionTooBusyException                | 次       | RPC 异常次数       | host4hbaseregionserver、<br/> id4hbaseregionserver |
| HbaseMasterIpcException<br>Unknownscannerexception           | RPC 异常次数<br/>_UnknownScannerException               | 次       | RPC 异常次数       | host4hbaseregionserver、<br/> id4hbaseregionserver |
| HbaseRegionserver<br>IpcHandlerNumactivehandler              | RPC 句柄数<br/>_numActiveHandler                        | 个       | RPC 句柄数         | host4hbaseregionserver、<br/> id4hbaseregionserver |
| HbaseMasterIpcQueue<br>Numcallsinpriorityqueue               | RPC 队列请求数<br/>_numCallsInPriorityQueue             | 个       | RPC 队列请求数     | host4hbaseregionserver、<br/> id4hbaseregionserver |
| HbaseMasterIpcQueue<br>Numcallsinreplicationqueue            | RPC 队列请求数<br/>_numCallsInReplicationQueue          | 个       | RPC 队列请求数     | host4hbaseregionserver、<br/> id4hbaseregionserver |
| HbaseRegionserver<br>IpcQueueNumcalls<br>ingeneralqueue      | RPC 队列请求数<br/>_numCallsInGeneralQueue              | 个       | RPC 队列请求数     | host4hbaseregionserver、<br/>id4hbaseregionserver  |
| HbaseRegionserver<br>HlogcountHlogfilecount                  | WAL 文件数量_hlogFileCount                              | 个       | WAL 文件数量       | host4hbaseregionserver、<br/>id4hbaseregionserver  |
| HbaseRegionserver<br>HlogsizeHlogfilesize                    | WAL 文件大小_hlogFileSize                               | Byte     | WAL 文件大小       | host4hbaseregionserver、<br/>id4hbaseregionserver  |
| HbaseRegionserver<br>MemstroreMemstoresize                   | Memstore 大小_memStoreSize                              | MB       | Memstore 大小      | host4hbaseregionserver、<br/>id4hbaseregionserver  |
| HbaseRegionserver<br>StoreCountStorecount                    | Store 个数_storeCount                                   | 个       | Store 个数         | host4hbaseregionserver、<br/>id4hbaseregionserver  |
| HbaseRegionserver<br>StorefilecountStorefilecount            | Storefile 个数\_storeFileCount                           | 个       | Storefile 个数     | host4hbaseregionserver、<br/>id4hbaseregionserver  |
| HbaseRegionserver<br>StorefilesizeStorefilesize              | Storefile 大小\_storeFileSize                            | MB       | Storefile 大小     | host4hbaseregionserver、<br/>id4hbaseregionserver  |
| HbaseRegionserver<br>ServerCellsFlushedcellssize             | 写磁盘速率\_flushedCellsSize                             | bytes/s  | 写磁盘速率         | host4hbaseregionserver、<br/>id4hbaseregionserver  |
| HbaseRegionserver<br>ServerDelayAppendMean                   | 平均延时\_Append_mean                                    | ms       | 平均延时           | host4hbaseregionserver、<br/>id4hbaseregionserver  |
| HbaseRegionserver<br>ServerDelayReplayMean                   | 平均延时\_Replay_mean                                    | ms       | 平均延时           | host4hbaseregionserver、<br/>id4hbaseregionserver  |
| HbaseRegionserver<br>ServerDelayGetMean                      | 平均延时\_Get_mean                                       | ms       | 平均延时           | host4hbaseregionserver、<br/>id4hbaseregionserver  |
| HbaseRegionserver<br>ServerDelayUpdatesblockedtime           | 平均延时<br/>\_updatesBlockedTime                        | ms       | 平均延时           | host4hbaseregionserver、<br/>id4hbaseregionserver  |
| HbaseRegionserver<br>ServerFlushFlushtimeNumOps              | RS 写磁盘次数<br/>\_FlushTime_num_ops                   | 次       | RS 写磁盘次数      | host4hbaseregionserver、<br/>id4hbaseregionserver  |
| HbaseRegionserver<br>ServerQueueSplitqueuelength             | 操作队列请求数<br/>\_splitQueueLength                    | 个       | 操作队列请求数     | host4hbaseregionserver、<br/>id4hbaseregionserver  |
| HbaseRegionserver<br>ServerQueueCompaction<br>queuelength    | 操作队列请求数\_compactionQueueLength                    | 个       | 操作队列请求数     | host4hbaseregionserver、<br/>id4hbaseregionserver  |
| HbaseRegionserver<br>ServerQueueFlushqueuelength             | 操作队列请求数<br/>\_flushQueueLength                    | 个       | 操作队列请求数     | host4hbaseregionserver、<br/>id4hbaseregionserver  |
| HbaseRegionserver<br>ServerReplayReplayNumOps                | Replay 操作次数<br/>\_Replay_num_ops                     | 次       | Replay 操作次数    | host4hbaseregionserver、<br/>id4hbaseregionserver  |
| HbaseRegionserver<br>ServerSlowSlowappendcount               | 慢操作次数<br/>\_slowAppendCount                         | 次       | 慢操作次数         | host4hbaseregionserver、<br/>id4hbaseregionserver  |
| HbaseRegionserver<br>ServerSlowSlowdeletecount               | 慢操作次数\_slowDeleteCount                              | 次       | 慢操作次数         | host4hbaseregionserver、<br/>id4hbaseregionserver  |
| HbaseRegionserver<br>ServerSlowSlowgetcount                  | 慢操作次数<br/>\_slowGetCount                            | 次       | 慢操作次数         | host4hbaseregionserver、<br/>id4hbaseregionserver  |
| HbaseRegionserver<br>ServerSlowSlowincrementcount            | 慢操作次数<br/>\_slowIncrementCount                      | 次       | 慢操作次数         | host4hbaseregionserver、<br/>id4hbaseregionserver  |
| HbaseRegionserver<br>ServerSlowSlowputcount                  | 慢操作次数\_slowPutCount                                 | 次       | 慢操作次数         | host4hbaseregionserver、<br/>id4hbaseregionserver  |
| HbaseRegionserver<br>ServerSplitSplitrequestcount            | split 请求\_splitRequestCount                            | 次       | split 请求         | host4hbaseregionserver、<br/>id4hbaseregionserver  |
| HbaseRegionserver<br>ServerSplitSplitsuccesscount            | split 请求\_splitSuccessCount                            | 次       | split 请求         | host4hbaseregionserver、<br/>id4hbaseregionserver  |
| HbaseRegionserver<br>ServerBlockcacheCountBlock<br>cachecount | 缓存块数量<br/>\_blockCacheCount                         | 个       | 缓存块数量         | host4hbaseregionserver、<br/>id4hbaseregionserver  |
| HbaseRegionserver<br>ServerBlockcacheCountBlock<br>cachehitcount | 缓存块数量<br/>\_blockCacheHitCount                      | 个       | 缓存块数量         | host4hbaseregionserver、<br/>id4hbaseregionserver  |
| HbaseRegionserver<br>ServerBlockcacheCountBlock<br>cachemisscount | 缓存块数量<br/>\_blockCacheMissCount                     | 个       | 缓存块数量         | host4hbaseregionserver、<br/>id4hbaseregionserver  |
| HbaseRegionserver<br>ServerBlockcachePercent<br>Blockcacheexpresshi | 读缓存命中率<br/>\_blockCacheExpress<br/>HitPercent      | %        | 读缓存命中率       | host4hbaseregionserver、<br/>id4hbaseregionserver  |
| HbaseRegionserver<br>ServerBlockcacheSize<br>Blockcachesize  | 缓存块内存占用大小\_blockCacheSize                       | Byte     | 缓存块内存占用大小 | host4hbaseregionserver、<br/>id4hbaseregionserver  |
| HbaseRegionserver<br>ServerIndexStaticbloomsize              | 索引大小\_staticBloomSize                                | Byte     | 索引大小           | host4hbaseregionserver、<br/>id4hbaseregionserver  |
| HbaseRegionserver<br>ServerIndexStaticindexsize              | 索引大小\_staticIndexSize                                | Byte     | 索引大小           | host4hbaseregionserver、<br/>id4hbaseregionserver  |
| HbaseRegionserver<br>ServerIndexStorefileindexsize           | 索引大小\_storeFileIndexSize                             | Byte     | 索引大小           | host4hbaseregionserver、<br/>id4hbaseregionserver  |
| HbaseRegionserver<br>IpcBytesReceivedbytes                   | 读写流量\_receivedBytes                                  | bytes/s  | 读写流量           | host4hbaseregionserver、<br/>id4hbaseregionserver  |
| HbaseRegionserver<br>IpcBytesSentbytes                       | 读写流量\_sentBytes                                      | bytes/s  | 读写流量           | host4hbaseregionserver、<br/>id4hbaseregionserver  |
| HbaseMasterJvm<br>LogTotalLogerror                           | 读写请求量\_Total                                        | 个/s     | 读写请求量         | host4hbaseregionserver、<br>id4hbaseregionserver   |
| HbaseMasterJvmThreads<br>Threadsblocked                      | JVM 线程数量<br/>\_ThreadsBlocked                        | 个/s     | 读写请求量         | host4hbaseregionserver、<br>id4hbaseregionserver   |
| HbaseRegionserver<br>ReqcountWrite                           | 读写请求量\_Write                                       | 个/s     | 读写请求量         | host4hbaseregionserver、<br>id4hbaseregionserver   |
| HbaseRegionserver<br>ReqcountAppendNumOps                    | 读写请求量\_Append_num_ops                               | 个/s     | 读写请求量         | host4hbaseregionserver、<br>id4hbaseregionserver   |
| HbaseRegionserver<br>ServerMutationCount<br>Mutationswithoutwalcoun | muation 个数\_mutationsWithout<br/>WALCount              | 个       | mutation 个数      | host4hbaseregionserver、<br>id4hbaseregionserver   |
| HbaseRegionserver<br>ServerMutationSizeMutation<br>swithoutwalsize | mutation 大小\_mutationsWithoutWALSize               | Byte     | mutation 大小      | host4hbaseregionserver、<br>id4hbaseregionserver   |
| HbaseRegionserver<br>StarttimeRegionserverstarttime          | 进程启动时间_regionServerStartTime                      | s        | 进程启动时间       | host4hbaseregionserver、<br>id4hbaseregionserver   |

## 各维度对应参数总览

| 参数名称                       | 维度名称               | 维度解释                     | 格式                                                         |
| :----------------------------- | :--------------------- | :--------------------------- | :----------------------------------------------------------- |
| Instances.N.Dimensions.0.Name  | id4hbaseoverview       | EMR 实例 ID 的维度名称       | 输入 String 类型维度名称：id4hbaseoverview                   |
| Instances.N.Dimensions.0.Value | id4hbaseoverview       | EMR 实例具体 ID              | 输入 EMR 具体实例 ID，例如 ：emr-mm8bs222                    |
| Instances.N.Dimensions.1.Name  | host4hbaseoverview     | EMR 实例中节点 IP 的维度名称 | 输入 String 类型维度名称：host4hbaseoverview                 |
| Instances.N.Dimensions.1.Value | host4hbaseoverview     | EMR 实例中具体节点 IP        | 输入具体节点  IP ，可从控制台获取，登录 [腾讯云 MapReduce 控制台](https://console.cloud.tencent.com/emr) > 点击实例 > 集群资源 > 资源管理 > 节点内网 IP。也可通过 [查询节点信息](https://cloud.tencent.com/document/product/589/41707) API 获取。 |
| Instances.N.Dimensions.0.Name  | id4hbasehmaster        | EMR 实例 ID 的维度名称       | 输入 String 类型维度名称：id4hbasehmaster                    |
| Instances.N.Dimensions.0.Value | id4hbasehmaster        | EMR 实例具体 ID              | 输入 EMR 具体实例 ID，例如 ：emr-mm8bs222                    |
| Instances.N.Dimensions.1.Name  | host4hbasehmaster      | EMR 实例中节点 IP 的维度名称 | 输入 String 类型维度名称：host4hbasehmaster                  |
| Instances.N.Dimensions.1.Value | host4hbasehmaster      | EMR 实例中具体节点 IP        | 输入具体节点  IP ，可从控制台获取，登录 [腾讯云 MapReduce 控制台](https://console.cloud.tencent.com/emr) > 点击实例 > 集群资源 > 资源管理 > 节点内网 IP。也可通过 [查询节点信息](https://cloud.tencent.com/document/product/589/41707) API 获取。 |
| Instances.N.Dimensions.0.Name  | id4hbaseregionserver   | EMR 实例 ID 的维度名称       | 输入 String 类型维度名称：id4hbaseregionserver               |
| Instances.N.Dimensions.0.Value | id4hbaseregionserver   | EMR 实例具体 ID              | 输入 EMR 具体实例 ID，例如 ：emr-mm8bs222                    |
| Instances.N.Dimensions.1.Name  | host4hbaseregionserver | EMR 实例中节点 IP 的维度名称 | 输入 String 类型维度名称：host4hbaseregionserver             |
| Instances.N.Dimensions.1.Value | host4hbaseregionserver | EMR 实例中具体节点 IP        | 输入具体节点  IP ，可从控制台获取，登录 [腾讯云 MapReduce 控制台](https://console.cloud.tencent.com/emr) > 点击实例 > 集群资源 > 资源管理 > 节点内网 IP。也可通过 [查询节点信息](https://cloud.tencent.com/document/product/589/41707) API 获取。 |





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


