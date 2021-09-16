### HBASE-概览

| 指标名称                | 指标单位 | 指标含义                   |
| ----------------------- | -------- | -------------------------- |
| ritCount                | 个       | 集群处于 RIT Region 个数   |
| ritCountOverThreshold   | 个       | 集群处于 RIT Region 个数   |
| ritOldestAge            | ms       | 集群 RIT 时间              |
| averageLoad             | 个       | 每个 RS 平均 REGION 数     |
| numRegionServers        | 个       | 集群 RS 数量               |
| numDeadRegionServers    | 个       | 集群 RS 数量               |
| receivedBytes           | bytes/s  | 集群读写数量               |
| sentBytes               | bytes/s  | 集群读写数量               |
| clusterRequests         | 个/s     | 集群总请求数量             |
| Assign_num_ops          | 次       | 集群 Assignment 管理器操作 |
| BulkAssign_num_ops      | 次       | 集群 Assignment 管理器操作 |
| BalancerCluster_num_ops | 次       | 集群负载均衡次数           |
| mergePlanCount          | 个       | 集群 Plan                  |
| splitPlanCount          | 个       | 集群 Plan                  |

### HBASE-HMaster

| 指标名称                       | 指标单位 | 指标含义       |
| ------------------------------ | -------- | -------------- |
| YGC                            | 次       | GC 次数        |
| FGC                            | 次       | GC 次数        |
| FGCT                           | s        | GC 时间        |
| GCT                            | s        | GC 时间        |
| YGCT                           | s        | GC 时间        |
| S0                             | %        | 内存区域占比   |
| E                              | %        | 内存区域占比   |
| CCS                            | %        | 内存区域占比   |
| S1                             | %        | 内存区域占比   |
| O                              | %        | 内存区域占比   |
| M                              | %        | 内存区域占比   |
| LogFatal                       | 次       | JVM 日志数量   |
| LogError                       | 次       | JVM 日志数量   |
| LogWarn                        | 次       | JVM 日志数量   |
| LogInfo                        | 次       | JVM 日志数量   |
| MemNonHeapUsedM                | MB       | JVM 内存       |
| MemNonHeapCommittedM           | MB       | JVM 内存       |
| MemNonHeapMaxM                 | MB       | JVM 内存       |
| MemHeapUsedM                   | MB       | JVM 内存       |
| MemHeapCommittedM              | MB       | JVM 内存       |
| MemHeapMaxM                    | MB       | JVM 内存       |
| MemMaxM                        | MB       | JVM 内存       |
| ThreadsNew                     | 个       | JVM 线程数量   |
| ThreadsRunnable                | 个       | JVM 线程数量   |
| ThreadsBlocked                 | 个       | JVM 线程数量   |
| ThreadsWaiting                 | 个       | JVM 线程数量   |
| ThreadsTimedWaiting            | 个       | JVM 线程数量   |
| ThreadsTerminated              | 个       | JVM 线程数量   |
| numOpenConnections             | 个       | RPC 连接数     |
| FailedSanityCheckException     | 次       | RPC 异常次数   |
| NotServingRegionException      | 次       | RPC 异常次数   |
| OutOfOrderScannerNextException | 次       | RPC 异常次数   |
| RegionMovedException           | 次       | RPC 异常次数   |
| RegionTooBusyException         | 次       | RPC 异常次数   |
| UnknownScannerException        | 次       | RPC 异常次数   |
| numCallsInPriorityQueue        | 个       | RPC 队列请求数 |
| numCallsInReplicationQueue     | 个       | RPC 队列请求数 |
| masterActiveTime               | s        | 进程启动时间   |
| masterStartTime                | s        | 进程启动时间   |

### HBASE-RegionServer

| 指标名称                          | 指标单位 | 指标含义           |
| --------------------------------- | -------- | ------------------ |
| YGC                               | 次       | GC 次数            |
| FGC                               | 次       | GC 次数            |
| FGCT                              | s        | GC 时间            |
| GCT                               | s        | GC 时间            |
| YGCT                              | s        | GC 时间            |
| S0                                | %        | 内存区域占比       |
| E                                 | %        | 内存区域占比       |
| CCS                               | %        | 内存区域占比       |
| S1                                | %        | 内存区域占比       |
| O                                 | %        | 内存区域占比       |
| M                                 | %        | 内存区域占比       |
| LogFatal                          | 次       | JVM 日志数量       |
| LogError                          | 次       | JVM 日志数量       |
| LogWarn                           | 次       | JVM 日志数量       |
| LogInfo                           | 次       | JVM 日志数量       |
| MemNonHeapUsedM                   | MB       | JVM 内存           |
| MemNonHeapCommittedM              | MB       | JVM 内存           |
| MemNonHeapMaxM                    | MB       | JVM 内存           |
| MemHeapUsedM                      | MB       | JVM 内存           |
| MemHeapCommittedM                 | MB       | JVM 内存           |
| MemHeapMaxM                       | MB       | JVM 内存           |
| MemMaxM                           | MB       | JVM 内存           |
| ThreadsNew                        | 个       | JVM 线程数量       |
| ThreadsRunnable                   | 个       | JVM 线程数量       |
| ThreadsBlocked                    | 个       | JVM 线程数量       |
| ThreadsWaiting                    | 个       | JVM 线程数量       |
| ThreadsTimedWaiting               | 个       | JVM 线程数量       |
| ThreadsTerminated                 | 个       | JVM 线程数量       |
| averageRegionSize                 | Byte     | Region 平均大小    |
| regionCount                       | 个       | Region 个数        |
| percentFilesLocalSecondaryRegions | %        | Region 副本本地化  |
| authenticationFailures            | 次       | RPC 认证次数       |
| authenticationSuccesses           | 次       | RPC 认证次数       |
| numOpenConnections                | 个       | RPC 连接数         |
| FailedSanityCheckException        | 次       | RPC 异常次数       |
| NotServingRegionException         | 次       | RPC 异常次数       |
| OutOfOrderScannerNextException    | 次       | RPC 异常次数       |
| RegionMovedException              | 次       | RPC 异常次数       |
| RegionTooBusyException            | 次       | RPC 异常次数       |
| UnknownScannerException           | 次       | RPC 异常次数       |
| numActiveHandler                  | 个       | RPC 句柄数         |
| numCallsInPriorityQueue           | 个       | RPC 队列请求数     |
| numCallsInReplicationQueue        | 个       | RPC 队列请求数     |
| numCallsInGeneralQueue            | 个       | RPC 队列请求数     |
| hlogFileCount                     | 个       | WAL 文件数量       |
| hlogFileSize                      | Byte     | WAL 文件大小       |
| memStoreSize                      | MB       | Memstore 大小      |
| storeCount                        | 个       | Store 个数         |
| storeFileCount                    | 个       | Storefile 个数     |
| storeFileSize                     | MB       | Storefile 大小     |
| flushedCellsSize                  | bytes/s  | 写磁盘速率         |
| Append_mean                       | ms       | 平均延时           |
| Replay_mean                       | ms       | 平均延时           |
| Get_mean                          | ms       | 平均延时           |
| updatesBlockedTime                | ms       | 平均延时           |
| FlushTime_num_ops                 | 次       | RS 写磁盘次数      |
| splitQueueLength                  | 个       | 操作队列请求数     |
| compactionQueueLength             | 个       | 操作队列请求数     |
| flushQueueLength                  | 个       | 操作队列请求数     |
| Replay_num_ops                    | 次       | Replay 操作次数    |
| slowAppendCount                   | 次       | 慢操作次数         |
| slowDeleteCount                   | 次       | 慢操作次数         |
| slowGetCount                      | 次       | 慢操作次数         |
| slowIncrementCount                | 次       | 慢操作次数         |
| slowPutCount                      | 次       | 慢操作次数         |
| splitRequestCount                 | 次       | split 请求         |
| splitSuccessCount                 | 次       | split 请求         |
| blockCacheCount                   | 个       | 缓存块数量         |
| blockCacheHitCount                | 个       | 缓存块数量         |
| blockCacheMissCount               | 个       | 缓存块数量         |
| blockCacheExpressHitPercent       | %        | 读缓存命中率       |
| blockCacheSize                    | Byte     | 缓存块内存占用大小 |
| staticBloomSize                   | Byte     | 索引大小           |
| staticIndexSize                   | Byte     | 索引大小           |
| storeFileIndexSize                | Byte     | 索引大小           |
| receivedBytes                     | bytes/s  | 读写流量           |
| sentBytes                         | bytes/s  | 读写流量           |
| Total                             | 个/s     | 读写请求量         |
| Read                              | 个/s     | 读写请求量         |
| Write                             | 个/s     | 读写请求量         |
| Append_num_ops                    | 个/s     | 读写请求量         |
| mutationsWithoutWALCount          | 个       | mutation 个数       |
| mutationsWithoutWALSize           | Byte     | mutation 大小      |
| regionServerStartTime             | s        | 进程启动时间       |
| 99th_percentile   | ms   | 99%请求处理时延   |
| 99.9th_percentile | ms   | 99.9%请求处理时延 |
| 99th_percentile   | ms   | 99%请求排队时延   |
| 99.9th_percentile | ms   | 99.9%请求排队时延 |


