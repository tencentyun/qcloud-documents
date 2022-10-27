命名空间

Namespace=QCE/TXMR_IMPALA

## 监控指标

### Impala-CATALOG

| 指标英文名                                    | 指标中文名                           | 单位  | 维度                                 |
| --------------------------------------------- | ------------------------------------ | ----- | ------------------------------------ |
| ImpalaCatalogHeartbeatIntervalTimeLast        | 心跳间隔_Last                        | s     | host4impalacatalog、id4impalacatalog |
| ImpalaCatalogHeartbeatIntervalTimeMax         | 心跳间隔_Max                         | s     | host4impalacatalog、id4impalacatalog |
| ImpalaCatalogHeartbeatIntervalTimeMean        | 心跳间隔_Mean                        | s     | host4impalacatalog、id4impalacatalog |
| ImpalaCatalogHeartbeatIntervalTimeMin         | 心跳间隔_Min                         | s     | host4impalacatalog、id4impalacatalog |
| ImpalaCatalogHeartbeatIntervalTimeStddev      | 心跳间隔_Stddev                      | s     | host4impalacatalog、id4impalacatalog |
| ImpalaCatalogJvmMemMemheapcommittedm          | JVM 内存_MemHeapCommittedM           | MB    | host4impalacatalog、id4impalacatalog |
| ImpalaCatalogJvmMemMemheapinitm               | JVM 内存_MemHeapInitM                | MB    | host4impalacatalog、id4impalacatalog |
| ImpalaCatalogJvmMemMemheapmaxm                | JVM 内存_MemHeapMaxM                 | MB    | host4impalacatalog、id4impalacatalog |
| ImpalaCatalogJvmMemMemheapusedm               | JVM 内存_MemHeapUsedM                | MB    | host4impalacatalog、id4impalacatalog |
| ImpalaCatalogJvmMemMemnonheapcommittedm       | JVM 内存_MemNonHeapCommittedM        | MB    | host4impalacatalog、id4impalacatalog |
| ImpalaCatalogJvmMemMemnonheapinitm            | JVM 内存_MemNonHeapInitM             | MB    | host4impalacatalog、id4impalacatalog |
| ImpalaCatalogJvmMemMemnonheapusedm            | JVM 内存_MemNonHeapUsedM             | MB    | host4impalacatalog、id4impalacatalog |
| ImpalaCatalogOsFdCountMaxfiledescriptorcount  | 文件描述符数_MaxFileDescriptorCount  | 个    | host4impalacatalog、id4impalacatalog |
| ImpalaCatalogOsFdCountOpenfiledescriptorcount | 文件描述符数_OpenFileDescriptorCount | 个    | host4impalacatalog、id4impalacatalog |
| ImpalaCatalogRss                              | 常驻内存集_RSS                       | Bytes | host4impalacatalog、id4impalacatalog |
| ImpalaCatalogRtUptimeUptime                   | 进程运行时间_Uptime                  | s     | host4impalacatalog、id4impalacatalog |
| ImpalaCatalogTcmallocPageheapfreebytes        | Tcmalloc 内存_PageheapFreeBytes      | Bytes | host4impalacatalog、id4impalacatalog |
| ImpalaCatalogTcmallocPageheapunmappedbytes    | Tcmalloc 内存_PageheapUnmappedBytes  | Bytes | host4impalacatalog、id4impalacatalog |
| ImpalaCatalogTcmallocPhysicalbytesreserved    | Tcmallo 内存_PhysicalBytesReserved   | Bytes | host4impalacatalog、id4impalacatalog |
| ImpalaCatalogTcmallocTotalbytesreserved       | Tcmalloc 内存_TotalBytesReserved     | Bytes | host4impalacatalog、id4impalacatalog |
| ImpalaCatalogTcmallocUsed                     | Tcmalloc 内存_Used                   | Bytes | host4impalacatalog、id4impalacatalog |
| ImpalaCatalogThreadCountDaemonthreadcount     | 线程数量_DaemonThreadCount           | 个    | host4impalacatalog、id4impalacatalog |
| ImpalaCatalogThreadCountThreadcount           | 线程数量_ThreadCount                 | 个    | host4impalacatalog、id4impalacatalog |
| ImpalaCatalogThriftServerConnectionsUsed      | 连接数_Used                          | 个    | host4impalacatalog、id4impalacatalog |



### Impala-STATESTORE

| 指标英文名                                    | 指标中文名                          | 单位  | 维度                                       |
| --------------------------------------------- | ----------------------------------- | ----- | ------------------------------------------ |
| ImpalaStatestoreRss                           | 常驻内存集_RSS                      | Bytes | host4impalastatestore、id4impalastatestore |
| ImpalaStatestoreStatestoreLiveBackendsCount   | StateStore 订阅者数量_Count         | 个    | host4impalastatestore、id4impalastatestore |
| ImpalaStatestoreTcmallocPageheapfreebytes     | Tcmalloc 内存_PageheapFreeBytes     | Bytes | host4impalastatestore、id4impalastatestore |
| ImpalaStatestoreTcmallocPageheapunmappedbytes | Tcmalloc 内存_PageheapUnmappedBytes | Bytes | host4impalastatestore、id4impalastatestore |
| ImpalaStatestoreTcmallocPhysicalbytesreserved | Tcmallo 内存_PhysicalBytesReserved  | Bytes | host4impalastatestore、id4impalastatestore |
| ImpalaStatestoreTcmallocTotalbytesreserved    | Tcmalloc 内存_TotalBytesReserved    | Bytes | host4impalastatestore、id4impalastatestore |
| ImpalaStatestoreTcmallocUsed                  | Tcmalloc 内存_Used                  | Bytes | host4impalastatestore、id4impalastatestore |
| ImpalaStatestoreThriftServerConnectionsUsed   | 连接数_Used                         | 个    | host4impalastatestore、id4impalastatestore |
| ImpalaStatestoreRunningThreadsCount           | 运行线程数_Count                    | 个    | host4impalastatestore、id4impalastatestore |



### Impala-DAEMON

| 指标英文名                                    | 指标中文名                                                   | 单位            | 维度                               |
| --------------------------------------------- | ------------------------------------------------------------ | --------------- | ---------------------------------- |
| ImpalaDaemonJvmMemMemheapcommittedm           | JVM 内存_MemHeapCommittedM                                   | MB              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonJvmMemMemheapinitm                | JVM 内存_MemHeapInitM                                        | MB              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonJvmMemMemheapmaxm                 | JVM 内存_MemHeapMaxM                                         | MB              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonJvmMemMemheapusedm                | JVM 内存_MemHeapUsedM                                        | MB              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonJvmMemMemnonheapcommittedm        | JVM 内存_MemNonHeapCommittedM                                | MB              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonJvmMemMemnonheapusedm             | JVM 内存_MemNonHeapUsedM                                     | MB              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonJvmMemMemnonheapinitm             | JVM 内存_MemNonHeapInitM                                     | MB              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonOsFdCountMaxfiledescriptorcount   | 文件描述符数_MaxFileDescriptorCount                          | 个              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonRtUptimeUptime                    | 进程运行时间_Uptime                                          | s               | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonTcmallocPageheapfreebytes         | Tcmalloc 内存_PageheapFreeBytes                              | Bytes           | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonTcmallocPageheapunmappedbytes     | Tcmalloc 内存_PageheapUnmappedBytes                          | Bytes           | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonTcmallocPhysicalbytesreserved     | Tcmalloc 内存_PhysicalBytesReserved                          | Bytes           | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonTcmallocTotalbytesreserved        | Tcmalloc 内存_TotalBytesReserved                             | Bytes           | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonTcmallocUsed                      | Tcmalloc 内存_Used                                           | Bytes           | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonThreadCountDaemonthreadcount      | 线程数量_DaemonThreadCount                                   | 个              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonOsFdCountOpenfiledescriptorcount  | 文件描述符数_OpenFileDescriptorCount                         | 个              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonThreadCountThreadcount            | 线程数量_ThreadCount                                         | 个              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonBeeswaxFrontendConnInUse          | BeeswaxAPI 客户端连接数                                      | 个              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonH2FrontendConnInUse               | HS2_API 客户端连接数_ConnInUse                               | 个              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonBeeswaxFrontendTotalconns         | Beeswax_API 客户端连接数_TotalConns                          | 次数总和(Count) | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonBeeswaxFrontendConnsetupqueuesize | Beeswax_API 客户端连接数_ConnSetupQueueSize                  | 次数总和(Count) | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonH2FrontendTotalconns              | HS2_API 客户端连接数_TotalConns                              | 次数总和(Count) | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonH2FrontendConnsetupqueuesize      | HS2_API 客户端连接数_ConnSetupQueueSize                      | 次数总和(Count) | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonThreadManagerRunningthreads       | 线程管理器_RunningThreads                                    | 次数总和(Count) | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonThreadManagerTotalcreatedthreads  | 线程管理器_TotalCreatedThreads                               | 次数总和(Count) | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonMemTrackerProcess1Limit           | 内存管理器限制_Limit                                         | 字节数(Bytes)   | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonMemTrackerProcessBytesOverlimit   | 超过其内存限制的内存量_OverLimit                             | 字节数(Bytes)   | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonBeeswaxFrontedTimeoutcnncrequests | 已超时的 BeeswaxAPI 连接数_TimeOutCnncRequests               | 次数总和(Count) | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonServerBackendConnsetupqueuesize   | 已超时等待设置的 Impala 后端服务器的连接请求数_ConnSetupQueueSize | 次数总和(Count) | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonServerBackend1Timeoutcnncrequests | 已超时等待设置的Impalabe的连接请求数_TimeOutCnncRequests     | 次数总和(Count) | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonServerBackend2Totalconnections    | 与此Impala守护程序建立的 Impala 后端客户端连接总数_TotalConnections | 次数总和(Count) | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonRequestPoolServiceResolveTotal    | 解析请求池请求所花费时间_Total                               | 毫秒(ms)        | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonMemoryRss                         | 此进程的驻留集大小_RSS                                       | 字节数(Bytes)   | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonClusterMembershipBackendsTotal    | StateStore 中注册后端总数_Total                              | 次数总和(Count) | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonServerQueryDurationsMsCount       | 查询延迟发布_Count                                           | 毫秒(ms)        | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonServerQueryDurationsMsSum         | 查询延迟发布_Sum                                             | 毫秒(ms)        | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonServer1Numfilesopenforinsert      | 打开已进行写入 HDFS 文件数_NumFilesOpenForInsert             | 次数总和(Count) | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonServer2Scanrangestotal            | 进程生命周期内读取的扫描范围_ScanRangesTotal                 | 次数总和(Count) | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonServer3Numopenbeeswaxsessions     | 打开 Beeswax 会话数量_NumOpenBeeswaxSessions                 | 次数总和(Count) | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonServer4Numfragments               | 进程生命周期内处理查询 fragment 总数_NumFragments            | 次数总和(Count) | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonServer14Hedgedreadops             | Hedgedreads 尝试次数_HedgedReadOps                           | 次数总和(Count) | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonServer5Numqueries                 | 在进程生命周期内处理查询总数_NumQueries                      | 次数总和(Count) | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonServer6Resultsetcachetotalnumrows | 支持缓存 HS2FETCH_FIRST 的总行数_ResultSetCacheTotalNumRows  | 次数总和(Count) | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonServer8Numqueriesregistered       | 此 Impala 服务器上注册的查询总数_NumQueriesRegistered        | 次数总和(Count) | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonServer9Numqueriesexecuted         | be 查询总数_NumQueriesExecuted                               | 次数总和(Count) | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonServer10Numsessionsexpired        | 非活动状态而终止会话数_NumSessionsExpired                    | 次数总和(Count) | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonServer11Numqueriesexpired         | 非活动状态而终止查询数_NumQueriesExpired                     | 次数总和(Count) | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonServer12Numopenhs2sessions        | 打开 HS2 会话数_NumOpenHS2Sessions                           | 次数总和(Count) | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonCatalog1Numtables                 | Catalog 里面表数量_NumTables                                 | 次数总和(Count) | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonCatalog2Numdatabases              | Catalog 里面数据库数量_NumDatabases                          | 次数总和(Count) | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonServerIoMgr2Byteswritten          | IO 管理器写入磁盘的字节数_BytesWritten                       | 字节数(Bytes)   | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonServerIoMgr3Numopenfiles          | IO 管理器打开的文件数_NumOpenFiles                           | 次数总和(Count) | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonServerIoMgr5Localbytesread        | 读取的本地字节数_LocalBytesRead                              | 字节数(Bytes)   | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonBeeswaxFrSvcThWaitTimeP20         | Beeswax_API 客户端等待服务线程建立时间_P20                   | us              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonBeeswaxFrSvcThWaitTimeP50         | Beeswax_API 客户端等待服务线程建立时间_P50                   | us              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonBeeswaxFrSvcThWaitTimeP70         | Beeswax_API 客户端等待服务线程建立时间_P70                   | us              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonBeeswaxFrSvcThWaitTimeP90         | Beeswax_API 客户端等待服务线程建立时间_P90                   | us              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonBeeswaxFrSvcThWaitTimeP95         | Beeswax_API 客户端等待服务线程建立时间_P95                   | us              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonExDsClassChMisses                 | 外部数据源缓存类中缓存未命中数_Misses                        | 个              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonH2FrConnSetupTimeP20              | HS2_API 客户端等待建立连接时间_P20                           | us              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonH2FrConnSetupTimeP50              | HS2_API 客户端等待建立连接时间_P50                           | us              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonH2FrConnSetupTimeP70              | HS2_API 客户端等待建立连接时间_P70                           | us              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonH2FrConnSetupTimeP90              | HS2_API 客户端等待建立连接时间_P90                           | us              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonH2FrConnSetupTimeP95              | HS2_API 客户端等待建立连接时间_P95                           | us              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonH2FrSvcThWaitTimeCount            | HS2_API 客户端等待服务线程建立时间_Count                     | us              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonH2FrSvcThWaitTimeP20              | HS2_API 客户端等待服务线程建立时间_P20                       | us              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonH2FrSvcThWaitTimeP50              | HS2_API 客户端等待服务线程建立时间_P50                       | us              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonH2FrSvcThWaitTimeP70              | HS2_API 客户端等待服务线程建立时间_P70                       | us              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonH2FrSvcThWaitTimeP90              | HS2_API 客户端等待服务线程建立时间_P90                       | us              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonH2FrSvcThWaitTimeP95              | HS2_API 客户端等待服务线程建立时间_P95                       | us              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonH2FrSvcThWaitTimeSum              | HS2_API 客户端等待服务线程建立时间_Sum                       | us              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonMemTrCsrvCurrentusagebytes        | ControlService 使用字节数_CurrentUsageBytes                  | Bytes           | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonMemTrCsrvPeakusagebytes           | ControlService 使用字节数_PeakUsageBytes                     | Bytes           | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonMemTrDssrvCurrentusagebytes       | DataStreamService 使用字节数_currentusagebytes               | Bytes           | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonMemTrDssrvPeakusagebytes          | DataStreamService 使用字节数_PeakUsageBytes                  | Bytes           | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonRpcCsrvRpcsqueueoverflow          | ControlStreamService 服务队列溢被拒绝数_RpcsQueueOverflow    | 个              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonRpcDssrvRpcsqueueoverflow         | DataStreamService 服务队列溢被拒绝数_RpcsQueueOverflow       | 个              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonServerBaConnSetupTimeCount        | Impala_be 的客户端等待连接建立所花费的时间_Count             | us              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonServerBaConnSetupTimeP20          | Impala_be 的客户端等待连接建立所花费的时间_P20               | us              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonServerBaConnSetupTimeP50          | Impala_be 的客户端等待连接建立所花费的时间_P50               | us              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonServerBaConnSetupTimeP70          | Impala_be 的客户端等待连接建立所花费的时间_P70               | us              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonServerBaConnSetupTimeP90          | Impala_be 的客户端等待连接建立所花费的时间_P90               | us              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonServerBaConnSetupTimeP95          | Impala_be 的客户端等待连接建立所花费的时间_P95               | us              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonServerBaConnSetupTimeSum          | Impala_be 的客户端等待连接建立所花费的时间_Sum               | us              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonServerBaSvcThWaitTimeCount        | Impala_be 的客户端等待服务线程所花费的时间_Count             | us              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonServerBaSvcThWaitTimeP20          | Impala_be 的客户端等待服务线程所花费的时间_P20               | us              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonServerBaSvcThWaitTimeP50          | Impala_be 的客户端等待服务线程所花费的时间_P50               | us              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonServerBaSvcThWaitTimeP70          | Impala_be 的客户端等待服务线程所花费的时间_P70               | us              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonServerBaSvcThWaitTimeP90          | Impala_be 的客户端等待服务线程所花费的时间_P90               | us              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonServerBaSvcThWaitTimeP95          | Impala_be 的客户端等待服务线程所花费的时间_P95               | us              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonServerBaSvcThWaitTimeSum          | Impala_be 的客户端等待服务线程所花费的时间_sum               | us              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonServerQueryDurationsMsP20         | 查询延迟发布_P20                                             | ms              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonServerQueryDurationsMsP50         | 查询延迟发布_P50                                             | ms              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonServerQueryDurationsMsP70         | 查询延迟发布_P70                                             | ms              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonServerQueryDurationsMsP90         | 查询延迟发布_P90                                             | ms              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonServerQueryDurationsMsP95         | 查询延迟发布_P95                                             | ms              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonSrvIoMgrNumfilehandlesoutstanding | 使用的 HDFS 文件句柄数_NumFileHandlesOutstanding             | 个              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonSrvScanrangesnummissingvolumid    | 在无 volum 元数据的进程生命周期内读取的扫描范围总数_ScanRangesNumMissingVolumId | 个              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonH2HttpFrSvcThWaitTimeCount        | HS2_HTTP_API 客户端等待服务线程建立时间_Count                | us              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonH2HttpFrSvcThWaitTimeP20          | HS2_HTTP_API 客户端等待服务线程建立时间_P20                  | us              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonH2HttpFrSvcThWaitTimeP50          | HS2_HTTP_API 客户端等待服务线程建立时间_P50                  | us              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonH2HttpFrSvcThWaitTimeP70          | HS2_HTTP_API 客户端等待服务线程建立时间_P70                  | us              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonH2HttpFrSvcThWaitTimeP90          | HS2_HTTP_API 客户端等待服务线程建立时间_P90                  | us              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonH2HttpFrSvcThWaitTimeP95          | HS2_HTTP_API 客户端等待服务线程建立时间_P95                  | us              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonH2HttpFrSvcThWaitTimeSum          | HS2_HTTP_API 客户端等待服务线程建立时间_Sum                  | us              | host4impaladaemon、id4impaladaemon |

## 各维度对应参数总览

| 参数名称                       | 维度名称              | 维度解释                     | 格式                                                         |
| :----------------------------- | :-------------------- | :--------------------------- | :----------------------------------------------------------- |
| Instances.N.Dimensions.0.Name  | host4impalacatalog    | EMR 实例中节点 IP 的维度名称 | 输入 String 类型维度名称：host4impalacatalog                 |
| Instances.N.Dimensions.0.Value | host4impalacatalog    | EMR 实例中具体节点 IP        | 输入具体节点  IP ，可从控制台获取，登录<b> [腾讯云 MapReduce 控制台](https://console.cloud.tencent.com/emr) > 单击实例 > 集群资源 > 资源管理 > 节点内网 IP</b>。也可通过 [查询节点信息](https://cloud.tencent.com/document/product/589/41707) API 获取。 |
| Instances.N.Dimensions.1.Name  | id4impalacatalog      | EMR 实例 ID 的维度名称       | 输入 String 类型维度名称：id4impalacatalog                   |
| Instances.N.Dimensions.1.Value | id4impalacatalog      | EMR 实例 ID 的维度名称| 输入 EMR 具体实例 ID，例如：emr-mm8bs222                     |
| Instances.N.Dimensions.0.Name  | host4impalastatestore | EMR 实例中节点 IP 的维度名称       | 输入 String 类型维度名称：host4impalastatestore              |
| Instances.N.Dimensions.0.Value | host4impalastatestore | EMR 实例中具体节点 IP            | 输入具体节点  IP ，可从控制台获取，登录 <b>[腾讯云 MapReduce 控制台](https://console.cloud.tencent.com/emr) > 单击实例 > 集群资源 > 资源管理 > 节点内网 IP</b>。也可通过 [查询节点信息](https://cloud.tencent.com/document/product/589/41707) API 获取。 |
| Instances.N.Dimensions.1.Name  | id4impalastatestore   | EMR 实例 ID 的维度名称       | 输入 String 类型维度名称：id4impalastatestore                |
| Instances.N.Dimensions.1.Value | id4impalastatestore   | EMR 实例 ID 的维度名称       | 输入 EMR 具体实例 ID，例如：emr-mm8bs222                     |
| Instances.N.Dimensions.0.Name  | host4impaladaemon     | EMR 实例中节点 IP 的维度名称     | 输入 String 类型维度名称：host4impaladaemon                  |
| Instances.N.Dimensions.0.Value | host4impaladaemon     |  EMR 实例中具体节点 IP           | 输入具体节点  IP ，可从控制台获取，登录<b> [腾讯云 MapReduce 控制台](https://console.cloud.tencent.com/emr) > 单击实例 > 集群资源 > 资源管理 > 节点内网 IP</b>。也可通过 [查询节点信息](https://cloud.tencent.com/document/product/589/41707) API 获取。 |
| Instances.N.Dimensions.1.Name  | id4impaladaemon       | EMR 实例 ID 的维度名称       | 输入 String 类型维度名称：id4impaladaemon                    |
| Instances.N.Dimensions.1.Value | id4impaladaemon       | EMR 实例 ID 的维度名称       | 输入 EMR 具体实例 ID，例如：emr-mm8bs222                     |

## 入参说明

#### 查询弹性 MapReduce（Impala-CATALOG）监控数据，入参取值如下：

Namespace=QCE/TXMR_IMPALA
&Instances.N.Dimensions.0.Name=host4impalacatalog
&Instances.N.Dimensions.0.Value=EMR 实例中具体节点 IP
&Instances.N.Dimensions.1.Name=id4impalacatalog
&Instances.N.Dimensions.1.Value=EMR 实例 ID 



#### 查询弹性 MapReduce（Impala-STATESTORE）监控数据，入参取值如下：

Namespace=QCE/TXMR_IMPALA
&Instances.N.Dimensions.0.Name=host4impalastatestore
&Instances.N.Dimensions.0.Value=EMR 实例中具体节点 IP
&Instances.N.Dimensions.1.Name=id4impalastatestore
&Instances.N.Dimensions.1.Value=EMR 实例 ID 



#### 查询弹性 MapReduce（Impala-DAEMON）监控数据，入参取值如下：

Namespace=QCE/TXMR_IMPALA
&Instances.N.Dimensions.0.Name=host4impaladaemon
&Instances.N.Dimensions.0.Value=EMR 实例中具体节点 IP
&Instances.N.Dimensions.1.Name=id4impaladaemon
&Instances.N.Dimensions.1.Value=EMR 实例 ID 
