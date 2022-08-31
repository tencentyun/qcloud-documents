命名空间

Namespace=QCE/TXMR_IMPALA

## 监控指标

### Impala-CATALOG

| 指标英文名                                         | 指标中文名                           | 单位  | 维度                                 |
| -------------------------------------------------- | ------------------------------------ | ----- | ------------------------------------ |
| ImpalaCatalogHeart<br/>beatIntervalTimeLast        | 心跳间隔_Last                        | s     | host4impalacatalog、id4impalacatalog |
| ImpalaCatalogHeart<br>beatIntervalTimeMax          | 心跳间隔_Max                         | s     | host4impalacatalog、id4impalacatalog |
| ImpalaCatalogHeart<br/>beatIntervalTimeMean        | 心跳间隔_Mean                        | s     | host4impalacatalog、id4impalacatalog |
| ImpalaCatalogHeart<br/>beatIntervalTimeMin         | 心跳间隔_Min                         | s     | host4impalacatalog、id4impalacatalog |
| ImpalaCatalogHeart<br/>beatIntervalTimeStddev      | 心跳间隔_Stddev                      | s     | host4impalacatalog、id4impalacatalog |
| ImpalaCatalogJvmMem<br/>Memheapcommittedm          | JVM 内存_MemHeapCommittedM            | MB    | host4impalacatalog、id4impalacatalog |
| ImpalaCatalogJvm<br/>MemMemheapinitm               | JVM 内存_MemHeapInitM                 | MB    | host4impalacatalog、id4impalacatalog |
| ImpalaCatalogJvm<br/>MemMemheapmaxm                | JVM 内存_MemHeapMaxM                  | MB    | host4impalacatalog、id4impalacatalog |
| ImpalaCatalogJvm<br/>MemMemheapusedm               | JVM 内存_MemHeapUsedM                 | MB    | host4impalacatalog、id4impalacatalog |
| ImpalaCatalogJvmMem<br/>Memnonheapcommittedm       | JVM 内存_MemNonHeapCommittedM         | MB    | host4impalacatalog、id4impalacatalog |
| ImpalaCatalogJvmMem<br/>Memnonheapinitm            | JVM 内存_MemNonHeapInitM              | MB    | host4impalacatalog、id4impalacatalog |
| ImpalaCatalogJvmMem<br/>Memnonheapusedm            | JVM 内存_MemNonHeapUsedM              | MB    | host4impalacatalog、id4impalacatalog |
| ImpalaCatalogOsFdCount<br/>Maxfiledescriptorcount  | 文件描述符数_MaxFileDescriptorCount  | 个    | host4impalacatalog、id4impalacatalog |
| ImpalaCatalogOsFdCount<br/>Openfiledescriptorcount | 文件描述符数_OpenFileDescriptorCount | 个    | host4impalacatalog、id4impalacatalog |
| ImpalaCatalogRss                                   | 常驻内存集_RSS                       | Bytes | host4impalacatalog、id4impalacatalog |
| ImpalaCatalogRtUptimeUptime                        | 进程运行时间_Uptime                  | s     | host4impalacatalog、id4impalacatalog |
| ImpalaCatalogTcmalloc<br/>Pageheapfreebytes        | Tcmalloc 内存_PageheapFreeBytes       | Bytes | host4impalacatalog、id4impalacatalog |
| ImpalaCatalogTcmalloc<br/>Pageheapunmappedbytes    | Tcmalloc 内存_PageheapUnmappedBytes   | Bytes | host4impalacatalog、id4impalacatalog |
| ImpalaCatalogTcmalloc<br/>Physicalbytesreserved    | Tcmallo 内存_PhysicalBytesReserved    | Bytes | host4impalacatalog、id4impalacatalog |
| ImpalaCatalogTcmalloc<br/>Totalbytesreserved       | Tcmalloc 内存_TotalBytesReserved      | Bytes | host4impalacatalog、id4impalacatalog |
| ImpalaCatalogTcmallocUsed                          | Tcmalloc 内存_Used                    | Bytes | host4impalacatalog、id4impalacatalog |
| ImpalaCatalogThreadCount<br/>Daemonthreadcount     | 线程数量_DaemonThreadCount           | 个    | host4impalacatalog、id4impalacatalog |
| ImpalaCatalogThread<br/>CountThreadcount           | 线程数量_ThreadCount                 | 个    | host4impalacatalog、id4impalacatalog |
| ImpalaCatalogThriftServer<br/>ConnectionsUsed      | 连接数_Used                          | 个    | host4impalacatalog、id4impalacatalog |



### Impala-STATESTORE

| 指标英文名                                         | 指标中文名                         | 单位  | 维度                                       |
| -------------------------------------------------- | ---------------------------------- | ----- | ------------------------------------------ |
| ImpalaStatestoreRss                                | 常驻内存集_RSS                     | Bytes | host4impalastatestore、id4impalastatestore |
| ImpalaStatestoreStatestore<br/>LiveBackendsCount   | StateStore 订阅者数量_Count         | 个    | host4impalastatestore、id4impalastatestore |
| ImpalaStatestoreTcmalloc<br/>Pageheapfreebytes     | Tcmalloc 内存_PageheapFreeBytes     | Bytes | host4impalastatestore、id4impalastatestore |
| ImpalaStatestoreTcmalloc<br/>Pageheapunmappedbytes | Tcmalloc 内存_PageheapUnmappedBytes | Bytes | host4impalastatestore、id4impalastatestore |
| ImpalaStatestoreTcmalloc<br/>Physicalbytesreserved | Tcmallo 内存_PhysicalBytesReserved  | Bytes | host4impalastatestore、id4impalastatestore |
| ImpalaStatestoreTcmalloc<br/>Totalbytesreserved    | Tcmalloc 内存_TotalBytesReserved    | Bytes | host4impalastatestore、id4impalastatestore |
| ImpalaStatestoreTcmallocUsed                       | Tcmalloc 内存_Used                  | Bytes | host4impalastatestore、id4impalastatestore |
| ImpalaStatestoreThriftServer<br/>ConnectionsUsed   | 连接数_Used                        | 个    | host4impalastatestore、id4impalastatestore |
| ImpalaStatestoreRunning<br/>ThreadsCount           | 运行线程数_Count                   | 个    | host4impalastatestore、id4impalastatestore |



### Impala-DAEMON

| 指标英文名                                         | 指标中文名                                                   | 单位            | 维度                               |
| -------------------------------------------------- | ------------------------------------------------------------ | --------------- | ---------------------------------- |
| ImpalaDaemonJvmMem<br/>Memheapcommittedm           | JVM 内存_MemHeapCommittedM                                    | MB              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonJvmMem<br/>Memheapinitm                | JVM 内存_MemHeapInitM                                         | MB              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonJvmMem<br/>Memheapmaxm                 | JVM 内存_MemHeapMaxM                                          | MB              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonJvmMem<br/>Memheapusedm                | JVM 内存_MemHeapUsedM                                         | MB              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonJvmMem<br/>Memnonheapcommittedm        | JVM 内存_MemNonHeapCommittedM                                 | MB              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonJvmMem<br/>Memnonheapusedm             | JVM 内存_MemNonHeapUsedM                                      | MB              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonJvmMem<br/>Memnonheapinitm             | JVM 内存_MemNonHeapInitM                                      | MB              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonOsFdCount<br/>Maxfiledescriptorcount   | 文件描述符数_MaxFileDescriptorCount                          | 个        | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonRtUptimeUptime                         | 进程运行时间_Uptime                                          | s               | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonTcmalloc<br/>Pageheapfreebytes         | Tcmalloc 内存_PageheapFreeBytes                               | Bytes           | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonTcmalloc<br/>Pageheapunmappedbytes     | Tcmalloc 内存_PageheapUnmappedBytes                           | Bytes           | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonTcmalloc<br/>Physicalbytesreserved     | Tcmalloc 内存_PhysicalBytesReserved                            | Bytes           | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonTcmalloc<br/>Totalbytesreserved        | Tcmalloc 内存_TotalBytesReserved                              | Bytes           | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonTcmallocUsed                           | Tcmalloc 内存_Used                                            | Bytes           | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonThreadCount<br/>Daemonthreadcount      | 线程数量_DaemonThreadCount                                   | 个              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonOsFdCount<br/>Openfiledescriptorcount  | 文件描述符数_OpenFileDescriptorCount                         | 个              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonThread<br/>CountThreadcount            | 线程数量_ThreadCount                                         | 个              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonBeeswax<br/>FrontendConnInUse          | BeeswaxAPI 客户端连接数                                       | 个              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonH2<br/>FrontendConnInUse               | HS2_API 客户端连接数_ConnInUse                                | 个              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonBeeswax<br/>FrontendTotalconns         | Beeswax_API 客户端连接数_TotalConns                           | 次数总和(Count) | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonBeeswaxFrontend<br/>Connsetupqueuesize | Beeswax_API 客户端连接数_ConnSetupQueueSize                   | 次数总和(Count) | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonH2<br/>FrontendTotalconns              | HS2_API 客户端连接数_TotalConns                               | 次数总和(Count) | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonH2Frontend<br/>Connsetupqueuesize      | HS2_API 客户端连接数_ConnSetupQueueSize                       | 次数总和(Count) | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonThreadManager<br/>Runningthreads       | 线程管理器_RunningThreads                                    | 次数总和(Count) | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonThreadManager<br/>Totalcreatedthreads  | 线程管理器_TotalCreatedThreads                               | 次数总和(Count) | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonMem<br/>TrackerProcess1Limit           | 内存管理器限制_Limit                                         | 字节数(Bytes)   | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonMemTracker<br/>ProcessBytesOverlimit   | 超过其内存限制的内存量_OverLimit                             | 字节数(Bytes)   | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonBeeswaxFronted<br/>Timeoutcnncrequests | 已超时的 BeeswaxAPI 连接数_TimeOutCnncRequests                 | 次数总和(Count) | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonServerBackend<br/>Connsetupqueuesize   | 已超时等待设置的 Impala 后端服务器的连接请求数_ConnSetupQueueSize | 次数总和(Count) | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonServerBackend1<br/>Timeoutcnncrequests | 已超时等待设置的Impalabe的连接请求数_TimeOutCnncRequests     | 次数总和(Count) | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonServer<br/>Backend2Totalconnections    | 与此Impala守护程序建立的 Impala 后端客户端连接总数_TotalConnections | 次数总和(Count) | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonRequest<br/>PoolServiceResolveTotal    | 解析请求池请求所花费时间_Total                               | 毫秒(ms)        | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonMemoryRss                              | 此进程的驻留集大小_RSS                                       | 字节数(Bytes)   | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonCluster<br/>MembershipBackendsTotal    | StateStore 中注册后端总数_Total                               | 次数总和(Count) | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonServerQuery<br/>DurationsMsCount       | 查询延迟发布_Count                                           | 毫秒(ms)        | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonServer<br/>QueryDurationsMsSum         | 查询延迟发布_Sum                                             | 毫秒(ms)        | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonServer1<br/>Numfilesopenforinsert      | 打开已进行写入 HDFS 文件数_NumFilesOpenForInsert               | 次数总和(Count) | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonServer2<br/>Scanrangestotal            | 进程生命周期内读取的扫描范围_ScanRangesTotal                 | 次数总和(Count) | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonServer3<br/>Numopenbeeswaxsessions     | 打开 Beeswax 会话数量_NumOpenBeeswaxSessions                   | 次数总和(Count) | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonServer4<br/>Numfragments               | 进程生命周期内处理查询 fragment 总数_NumFragments              | 次数总和(Count) | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonServer14<br/>Hedgedreadops             | Hedgedreads 尝试次数_HedgedReadOps                            | 次数总和(Count) | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonServer5<br/>Numqueries                 | 在进程生命周期内处理查询总数_NumQueries                      | 次数总和(Count) | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonServer6<br/>Resultsetcachetotalnumrows | 支持缓存 HS2FETCH_FIRST 的总行数_ResultSetCacheTotalNumRows    | 次数总和(Count) | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonServer8<br/>Numqueriesregistered       | 此 Impala 服务器上注册的查询总数_NumQueriesRegistered          | 次数总和(Count) | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonServer9<br/>Numqueriesexecuted         | be 查询总数_NumQueriesExecuted                                | 次数总和(Count) | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonServer10<br/>Numsessionsexpired        | 非活动状态而终止会话数_NumSessionsExpired                    | 次数总和(Count) | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonServer11<br/>Numqueriesexpired         | 非活动状态而终止查询数_NumQueriesExpired                     | 次数总和(Count) | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonServer12<br/>Numopenhs2sessions        | 打开 HS2 会话数_NumOpenHS2Sessions                             | 次数总和(Count) | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonCatalog1Numtables                      | Catalog 里面表数量_NumTables                                  | 次数总和(Count) | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonCatalog2<br/>Numdatabases              | Catalog 里面数据库数量_NumDatabases                           | 次数总和(Count) | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonServerIo<br/>Mgr2Byteswritten          | IO 管理器写入磁盘的字节数_BytesWritten                        | 字节数(Bytes)   | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonServerIo<br/>Mgr3Numopenfiles          | IO 管理器打开的文件数_NumOpenFiles                            | 次数总和(Count) | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonServerIo<br/>Mgr5Localbytesread        | 读取的本地字节数_LocalBytesRead                              | 字节数(Bytes)   | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonBeeswax<br/>FrSvcThWaitTimeP20         | Beeswax_API 客户端等待服务线程建立时间_P20                    | us              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonBeeswax<br/>FrSvcThWaitTimeP50         | Beeswax_API 客户端等待服务线程建立时间_P50                    | us              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonBeeswax<br/>FrSvcThWaitTimeP70         | Beeswax_API 客户端等待服务线程建立时间_P70                    | us              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonBeeswax<br/>FrSvcThWaitTimeP90         | Beeswax_API 客户端等待服务线程建立时间_P90                    | us              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonBeeswax<br/>FrSvcThWaitTimeP95         | Beeswax_API 客户端等待服务线程建立时间_P95                    | us              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemon<br/>ExDsClassChMisses                 | 外部数据源缓存类中缓存未命中数_Misses                        | 个              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonH2<br/>FrConnSetupTimeP20              | HS2_API 客户端等待建立连接时间_P20                            | us              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonH2<br/>FrConnSetupTimeP50              | HS2_API 客户端等待建立连接时间_P50                            | us              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonH2<br/>FrConnSetupTimeP70              | HS2_API 客户端等待建立连接时间_P70                            | us              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonH2<br/>FrConnSetupTimeP90              | HS2_API 客户端等待建立连接时间_P90                            | us              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonH2<br/>FrConnSetupTimeP95              | HS2_API 客户端等待建立连接时间_P95                            | us              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonH2<br/>FrSvcThWaitTimeCount            | HS2_API 客户端等待服务线程建立时间_Count                      | us              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonH2<br/>FrSvcThWaitTimeP20              | HS2_API 客户端等待服务线程建立时间_P20                        | us              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonH2<br/>FrSvcThWaitTimeP50              | HS2_API 客户端等待服务线程建立时间_P50                        | us              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonH2<br/>FrSvcThWaitTimeP70              | HS2_API 客户端等待服务线程建立时间_P70                        | us              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemon<br/>H2FrSvcThWaitTimeP90              | HS2_API 客户端等待服务线程建立时间_P90                        | us              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemon<br/>H2FrSvcThWaitTimeP95              | HS2_API 客户端等待服务线程建立时间_P95                        | us              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemon<br/>H2FrSvcThWaitTimeSum              | HS2_API 客户端等待服务线程建立时间_Sum                        | us              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonMem<br/>TrCsrvCurrentusagebytes        | ControlService 使用字节数_CurrentUsageBytes                   | Bytes           | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonMem<br/>TrCsrvPeakusagebytes           | ControlService 使用字节数_PeakUsageBytes                      | Bytes           | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonMem<br/>TrDssrvCurrentusagebytes       | DataStreamService 使用字节数_currentusagebytes                | Bytes           | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonMem<br/>TrDssrvPeakusagebytes          | DataStreamService 使用字节数_PeakUsageBytes                   | Bytes           | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonRpc<br/>CsrvRpcsqueueoverflow          | ControlStreamService 服务队列溢被拒绝数_RpcsQueueOverflow     | 个              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonRpc<br/>DssrvRpcsqueueoverflow         | DataStreamService 服务队列溢被拒绝数_RpcsQueueOverflow        | 个              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonServer<br/>BaConnSetupTimeCount        | Impala_be 的客户端等待连接建立所花费的时间_Count              | us              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonServer<br/>BaConnSetupTimeP20          | Impala_be 的客户端等待连接建立所花费的时间_P20                | us              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonServer<br/>BaConnSetupTimeP50          | Impala_be 的客户端等待连接建立所花费的时间_P50                | us              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonServer<br/>BaConnSetupTimeP70          | Impala_be 的客户端等待连接建立所花费的时间_P70                | us              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonServer<br/>BaConnSetupTimeP90          | Impala_be 的客户端等待连接建立所花费的时间_P90                | us              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonServer<br/>BaConnSetupTimeP95          | Impala_be 的客户端等待连接建立所花费的时间_P95                | us              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonServer<br/>BaConnSetupTimeSum          | Impala_be 的客户端等待连接建立所花费的时间_Sum                | us              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonServer<br/>BaSvcThWaitTimeCount        | Impala_be 的客户端等待服务线程所花费的时间_Count              | us              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonServer<br/>BaSvcThWaitTimeP20          | Impala_be 的客户端等待服务线程所花费的时间_P20                | us              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonServer<br/>BaSvcThWaitTimeP50          | Impala_be 的客户端等待服务线程所花费的时间_P50                | us              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonServer<br/>BaSvcThWaitTimeP70          | Impala_be 的客户端等待服务线程所花费的时间_P70                | us              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonServer<br/>BaSvcThWaitTimeP90          | Impala_be 的客户端等待服务线程所花费的时间_P90                | us              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonServer<br/>BaSvcThWaitTimeP95          | Impala_be 的客户端等待服务线程所花费的时间_P95                | us              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonServer<br/>BaSvcThWaitTimeSum          | Impala_be 的客户端等待服务线程所花费的时间_sum                | us              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonServer<br/>QueryDurationsMsP20         | 查询延迟发布_P20                                             | ms              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonServer<br/>QueryDurationsMsP50         | 查询延迟发布_P50                                             | ms              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonServer<br/>QueryDurationsMsP70         | 查询延迟发布_P70                                             | ms              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonServer<br/>QueryDurationsMsP90         | 查询延迟发布_P90                                             | ms              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonServer<br/>QueryDurationsMsP95         | 查询延迟发布_P95                                             | ms              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonSrvIoMgr<br/>Numfilehandlesoutstanding | 使用的 HDFS 文件句柄数_NumFileHandlesOutstanding               | 个              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonSrvScanran<br/>gesnummissingvolumid    | 在无 volum 元数据的进程生命周期内读取的扫描范围总数_ScanRangesNumMissingVolumId | 个              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonH2<br/>HttpFrSvcThWaitTimeCount        | HS2_HTTP_API 客户端等待服务线程建立时间_Count                 | us              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonH2<br/>HttpFrSvcThWaitTimeP20          | HS2_HTTP_API 客户端等待服务线程建立时间_P20                   | us              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonH2<br/>HttpFrSvcThWaitTimeP50          | HS2_HTTP_API 客户端等待服务线程建立时间_P50                   | us              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonH2<br/>HttpFrSvcThWaitTimeP70          | HS2_HTTP_API 客户端等待服务线程建立时间_P70                   | us              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonH2<br/>HttpFrSvcThWaitTimeP90          | HS2_HTTP_API 客户端等待服务线程建立时间_P90                   | us              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonH2<br/>HttpFrSvcThWaitTimeP95          | HS2_HTTP_API 客户端等待服务线程建立时间_P95                   | us              | host4impaladaemon、id4impaladaemon |
| ImpalaDaemonH2<br/>HttpFrSvcThWaitTimeSum          | HS2_HTTP_API 客户端等待服务线程建立时间_Sum                   | us              | host4impaladaemon、id4impaladaemon |

## 各维度对应参数总览

| 参数名称                       | 维度名称              | 维度解释                     | 格式                                                         |
| :----------------------------- | :-------------------- | :--------------------------- | :----------------------------------------------------------- |
| Instances.N.Dimensions.0.Name  | host4impalacatalog    | EMR 实例中节点 IP 的维度名称 | 输入 String 类型维度名称：host4impalacatalog                 |
| Instances.N.Dimensions.0.Value | host4impalacatalog    | EMR 实例中具体节点 IP        | 输入具体节点  IP ，可从控制台获取，登录<b> [腾讯云 MapReduce 控制台](https://console.cloud.tencent.com/emr) > 单击实例 > 集群资源 > 资源管理 > 节点内网 IP</b>。也可通过 [查询节点信息](https://cloud.tencent.com/document/product/589/41707) API 获取。 |
| Instances.N.Dimensions.1.Name  | id4impalacatalog      | EMR 实例 ID 的维度名称       | 输入 String 类型维度名称：id4impalacatalog                   |
| Instances.N.Dimensions.1.Value | id4impalacatalog      | EMR 实例中节点 IP 的维度名称 | 输入 EMR 具体实例 ID，例如：emr-mm8bs222                     |
| Instances.N.Dimensions.0.Name  | host4impalastatestore | EMR 实例 ID 的维度名称       | 输入 String 类型维度名称：host4impalastatestore              |
| Instances.N.Dimensions.0.Value | host4impalastatestore | EMR 实例具体 ID              | 输入具体节点  IP ，可从控制台获取，登录 <b>[腾讯云 MapReduce 控制台](https://console.cloud.tencent.com/emr) > 单击实例 > 集群资源 > 资源管理 > 节点内网 IP</b>。也可通过 [查询节点信息](https://cloud.tencent.com/document/product/589/41707) API 获取。 |
| Instances.N.Dimensions.1.Name  | id4impalastatestore   | EMR 实例 ID 的维度名称       | 输入 String 类型维度名称：id4impalastatestore                |
| Instances.N.Dimensions.1.Value | id4impalastatestore   | EMR 实例 ID 的维度名称       | 输入 EMR 具体实例 ID，例如：emr-mm8bs222                     |
| Instances.N.Dimensions.0.Name  | host4impaladaemon     | EMR 实例 ID 的维度名称       | 输入 String 类型维度名称：host4impaladaemon                  |
| Instances.N.Dimensions.0.Value | host4impaladaemon     | EMR 实例具体 ID              | 输入具体节点  IP ，可从控制台获取，登录<b> [腾讯云 MapReduce 控制台](https://console.cloud.tencent.com/emr) > 单击实例 > 集群资源 > 资源管理 > 节点内网 IP</b>。也可通过 [查询节点信息](https://cloud.tencent.com/document/product/589/41707) API 获取。 |
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



