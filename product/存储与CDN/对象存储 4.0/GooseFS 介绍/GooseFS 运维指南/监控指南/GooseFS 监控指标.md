## 监控指标概述

Goosefs 监控指标记录了客户端、集群、Master 节点、 Worker 节点、进程的运行状态。

1. 按照统计维度，监控指标可以分成以下四大类：
 - **Gauge**：记录一个事件的瞬时数值，该数值可增可减，一般用来反映系统运行状态。
 - **Meter**：统计事件频率，即固定时间周期内事件的发生次数，如每分钟、每5分钟，每15分钟内的请求数。
 - **Counter**：统计事件发生的总次数，与 Gauge 不同的点在于该数值只增不减，一般用来记录访问请求次数等数据。
 - **Timer**：统计事件的频率和分布情况，该指标可以认为 Histogram 指标和 Meter 指标的结合，Histogram 指标用于统计耗时分布，Meter 指标用于统计 QPS；如果需要同时统计频率和耗时的时候可以使用该指标。

>!更多监控指标分类可参见 [Metrics Library 文档](https://metrics.dropwizard.io/3.1.0/getting-started)。GooseFS 目前提供的监控指标只有上述4种类型。
>

2. 按照数据采集来源，监控指标可以分为以下两大类：
 - **集群状态指标**：集群状态指标包括了 Cluster、Master 和 Worker 维度的监控数据，这些监控指标可以反应整个集群及集群下的每个节点的运行状态。这类指标的记录格式如下：
```plaintext
Master.[metricName].[tag1].[tag2]...
[Worker_ip].[metricName].[tag1].[tag2]...
```
 - **进程处理指标**：进程处理指标用于详细记录集群中的请求次数、延迟、CPU 消耗、RPC 调用次数等信息，这类指标可以推送到第三方监控工具中展示。这类指标的记录格式如下：
```plaintext
[processType].[metricName].[tag1].[tag2]...[hostName]
```

## Cluster 监控指标

GooseFS 集群化部署时，客户端和 Worker 节点会周期性地通过心跳将监控指标发送到 Master 节点，可以通过 goosefs.master.worker.heartbeat.interval 和 goosefs.user.metrics.heartbeat.interval 分别设置 Worker 节点和客户端监控指标的心跳周期。

Cluster 级别的监控指标列表如下：

| **指标名称**                         | **指标类型** | **指标描述**                                                 |
| ------------------------------------ | ------------ | ------------------------------------------------------------ |
| Cluster.BytesReadDomain              | COUNTER      | Total number of bytes read from GooseFS storage via domain socket reported by all workers |
| Cluster.BytesReadDomainThroughput    | GAUGE        | Bytes read throughput from GooseFS storage via domain socket by all workers |
| Cluster.BytesReadLocal               | COUNTER      | Total number of bytes short-circuit read from local storage by all clients |
| Cluster.BytesReadLocalThroughput     | GAUGE        | Bytes throughput short-circuit read from local storage by all clients |
| Cluster.BytesReadPerUfs              | COUNTER      | Total number of bytes read from a specific UFS by all workers |
| Cluster.BytesReadRemote              | COUNTER      | Total number of bytes read from GooseFS storage or underlying UFS if data does not exist in GooseFS storage reported by all workers. This does not include short-circuit local reads and domain socket reads |
| Cluster.BytesReadRemoteThroughput    | GAUGE        | Bytes read throughput from GooseFS storage or underlying UFS if data does not exist in GooseFS storage reported by all workers. This does not include short-circuit local reads and domain socket reads |
| Cluster.BytesReadUfsAll              | COUNTER      | Total number of bytes read from a all GooseFS UFSes by all workers |
| Cluster.BytesReadUfsThroughput       | GAUGE        | Bytes read throughput from all GooseFS UFSes by all workers  |
| Cluster.BytesWrittenDomain           | COUNTER      | Total number of bytes written to GooseFS storage via domain socket by all workers |
| Cluster.BytesWrittenDomainThroughput | GAUGE        | Throughput of bytes written to GooseFS storage via domain socket by all workers |
| Cluster.BytesWrittenLocal            | COUNTER      | Total number of bytes short-circuit written to local storage by all clients |
| Cluster.BytesWrittenLocalThroughput  | GAUGE        | Bytes throughput written to local storage by all clients     |
| Cluster.BytesWrittenPerUfs           | COUNTER      | Total number of bytes written to a specific GooseFS UFS by all workers | 
| Cluster.BytesWrittenRemote           | COUNTER      | Total number of bytes written to GooseFS storage in all workers or the underlying UFS. This does not include short-circuit local writes and domain socket writes. |
| Cluster.BytesWrittenRemoteThroughput | GAUGE        | Bytes write throughput to GooseFS storage in all workers or the underlying UFS. This does not include short-circuit local writes and domain socket writes. |
| Cluster.BytesWrittenUfsAll           | COUNTER      | Total number of bytes written to all GooseFS UFSes by all workers |
| Cluster.BytesWrittenUfsThroughput    | GAUGE        | Bytes write throughput to all GooseFS UFSes by all workers   |
| Cluster.CapacityFree                 | GAUGE        | Total free bytes on all tiers, on all workers of GooseFS     |
| Cluster.CapacityTotal                | GAUGE        | Total capacity (in bytes) on all tiers, on all workers of GooseFS |
| Cluster.CapacityUsed                 | GAUGE        | Total used bytes on all tiers, on all workers of GooseFS     |
| Cluster.RootUfsCapacityFree          | GAUGE        | Free capacity of the GooseFS root UFS in bytes               |
| Cluster.RootUfsCapacityTotal         | GAUGE        | Total capacity of the GooseFS root UFS in bytes              |
| Cluster.RootUfsCapacityUsed          | GAUGE        | Used capacity of the GooseFS root UFS in bytes               |
| Cluster.Workers                      | GAUGE        | Total number of active workers inside the cluster            |


## Master 监控指标

Master 监控指标有两大类，其一是默认指标，Master 运行过程中会默认记录这些指标；其二是动态监控指标。默认的 Master 监控指标如下：

| **指标名称**                         | **指标类型** | **指标描述**                                                 |
| ------------------------------------ | ------------ | ------------------------------------------------------------ |
| Master.CompleteFileOps               | COUNTER      | Total number of the CompleteFile operations                  |
| Master.CreateDirectoryOps            | COUNTER      | Total number of the CreateDirectory operations               |
| Master.CreateFileOps                 | COUNTER      | Total number of the CreateFile operations                    |
| Master.DeletePathOps                 | COUNTER      | Total number of the Delete operations                        |
| Master.DirectoriesCreated            | COUNTER      | Total number of the succeed CreateDirectory operations       |
| Master.EdgeCacheEvictions            | GAUGE        | Total number of edges (inode metadata) that was evicted from cache. The edge cache is responsible for managing the mapping from (parentId, childName) to childId. |
| Master.EdgeCacheHits                 | GAUGE        | Total number of hits in the edge (inode metadata) cache. The edge cache is responsible for managing the mapping from (parentId, childName) to childId. |
| Master.EdgeCacheLoadTimes            | GAUGE        | Total load times in the edge (inode metadata) cache. The edge cache is responsible for managing the mapping from (parentId, childName) to childId. |
| Master.EdgeCacheMisses               | GAUGE        | Total number of misses in the edge (inode metadata) cache. The edge cache is responsible for managing the mapping from (parentId, childName) to childId. |
| Master.EdgeCacheSize                 | GAUGE        | Total number of edges (inode metadata) cached. The edge cache is responsible for managing the mapping from (parentId, childName) to childId. |
| Master.EdgeLockPoolSize              | GAUGE        | The size of master edge lock pool                            |
| Master.FileBlockInfosGot             | COUNTER      | Total number of succeed GetFileBlockInfo operations          |
| Master.FileInfosGot                  | COUNTER      | Total number of the succeed GetFileInfo operations           |
| Master.FilesCompleted                | COUNTER      | Total number of the succeed CompleteFile operations          |
| Master.FilesCreated                  | COUNTER      | Total number of the succeed CreateFile operations            |
| Master.FilesFreed                    | COUNTER      | Total number of succeed FreeFile operations                  |
| Master.FilesPersisted                | COUNTER      | Total number of successfully persisted files                 |
| Master.FilesPinned                   | GAUGE        | Total number of currently pinned files                       |
| Master.FreeFileOps                   | COUNTER      | Total number of FreeFile operations                          |
| Master.GetFileBlockInfoOps           | COUNTER      | Total number of GetFileBlockInfo operations                  |
| Master.GetFileInfoOps                | COUNTER      | Total number of the GetFileInfo operations                   |
| Master.GetNewBlockOps                | COUNTER      | Total number of the GetNewBlock operations                   |
| Master.InodeCacheEvictions           | GAUGE        | Total number of inodes that was evicted from the cache.      |
| Master.InodeCacheHits                | GAUGE        | Total number of hits in the inodes (inode metadata) cache.   |
| Master.InodeCacheLoadTimes           | GAUGE        | Total load times in the inodes (inode metadata) cache.       |
| Master.InodeCacheMisses              | GAUGE        | Total number of misses in the inodes (inode metadata) cache. |
| Master.InodeCacheSize                | GAUGE        | Total number of inodes (inode metadata) cached.              |
| Master.InodeLockPoolSize             | GAUGE        | The size of master inode lock pool                           |
| Master.JournalFlushFailure           | COUNTER      | Total number of failed journal flush                         |
| Master.JournalFlushTimer             | TIMER        | The timer statistics of journal flush                        |
| Master.JournalGainPrimacyTimer       | TIMER        | The timer statistics of journal gain primacy                 |
| Master.LastBackupEntriesCount        | GAUGE        | The total number of entries written in the last leading master metadata backup |
| Master.LastBackupRestoreCount        | GAUGE        | The total number of entries restored from backup when a leading master initializes its metadata |
| Master.LastBackupRestoreTimeMs       | GAUGE        | The process time of the last restore from backup             |
| Master.LastBackupTimeMs              | GAUGE        | The process time of the last backup                          |
| Master.ListingCacheSize              | GAUGE        | The size of master listing cache                             |
| Master.MountOps                      | COUNTER      | Total number of Mount operations                             |
| Master.NewBlocksGot                  | COUNTER      | Total number of the succeed GetNewBlock operations           |
| Master.PathsDeleted                  | COUNTER      | Total number of the succeed Delete operations                |
| Master.PathsMounted                  | COUNTER      | Total number of succeed Mount operations                     |
| Master.PathsRenamed                  | COUNTER      | Total number of succeed Rename operations                    |
| Master.PathsUnmounted                | COUNTER      | Total number of succeed Unmount operations                   |
| Master.RenamePathOps                 | COUNTER      | Total number of Rename operations                            |
| Master.SetAclOps                     | COUNTER      | Total number of SetAcl operations                            |
| Master.SetAttributeOps               | COUNTER      | Total number of SetAttribute operations                      |
| Master.TotalPaths                    | GAUGE        | Total number of files and directory in Goosefs namespace     |
| Master.UfsJournalCatchupTimer        | TIMER        | The timer statistics of journal catchup                      |
| Master.UfsJournalFailureRecoverTimer | TIMER        | The timer statistics of ufs journal failure recover          |
| Master.UfsJournalInitialReplayTimeMs | GAUGE        | The process time of the ufs journal initial replay           |
| Master.UnmountOps                    | COUNTER      | Total number of Unmount operations                           |

动态指标如下：

| **指标名称**                 | **指标类型** | **指标描述**                                                 |
| ---------------------------- | ------------ | ------------------------------------------------------------ |
| Master.CapacityTotalTier     | GAUGE        | Total capacity in tier of the Goosefs file system in bytes   |
| Master.CapacityUsedTier      | GAUGE        | Used capacity in tier of the Goosefs file system in bytes    |
| Master.CapacityFreeTier      | GAUGE        | Free capacity in tier of the Goosefs file system in bytes    |
| Master.UfsSessionCount-Ufs:  | COUNTER      | The total number of currently opened UFS sessions to connect to the given |
| Master..UFS:.UFS_TYPE:.User: | GAUGE        | The details UFS rpc operation done by the current master     |
| Master.PerUfsOp.UFS:         | TIMER        | The aggregated number of UFS operation ran on UFS by leading master |
| Master.                      | TIMER        | The duration statistics of RPC calls exposed on leading master |


## Worker 监控指标

Worker 监控指标有两大类，其一是默认指标，Worker 运行过程中会默认记录这些指标；其二是动态监控指标。默认的 Worker 监控指标如下：

| **指标名称**                            | **指标类型** | **指标描述**                                                 |
| --------------------------------------- | ------------ | ------------------------------------------------------------ |
| Worker.AsyncCacheDuplicateRequests      | COUNTER      | Total number of duplicated async cache request received by this worker |
| Worker.AsyncCacheFailedBlocks           | COUNTER      | Total number of async cache failed blocks in this worker     |      |
| Worker.AsyncCacheRemoteBlocks           | COUNTER      | Total number of blocks that need to be async cached from remote source |
| Worker.AsyncCacheRequests               | COUNTER      | Total number of async cache request received by this worker  |
| Worker.AsyncCacheSucceededBlocks        | COUNTER      | Total number of async cache succeeded blocks in this worker  |
| Worker.AsyncCacheUfsBlocks              | COUNTER      | Total number of blocks that need to be async cached from local source |
| Worker.BlockRemoverBlocksToRemovedCount | COUNTER      | The total number of blocks removed from this worker by asynchronous block remover. |
| Worker.BlockRemoverRemovingBlocksSize   | GAUGE        | The size of blocks is removing from this worker by asynchronous block remover. |
| Worker.BlockRemoverTryRemoveBlocksSize  | GAUGE        | The size of blocks to be removed from this worker by asynchronous block remover. |
| Worker.BlockRemoverTryRemoveCount       | COUNTER      | The total number of blocks tried to be removed from this worker by asynchronous block remover. |
| Worker.BlocksAccessed                   | COUNTER      | Total number of times any one of the blocks in this worker is accessed. |
| Worker.BlocksCached                     | GAUGE        | Total number of blocks used for caching data in an goosefs worker |
| Worker.BlocksCancelled                  | COUNTER      | Total number of aborted temporary blocks in this worker.     |
| Worker.BlocksDeleted                    | COUNTER      | Total number of deleted blocks in this worker by external requests. |
| Worker.BlocksEvicted                    | COUNTER      | Total number of evicted blocks in this worker.               |
| Worker.BlocksLost                       | COUNTER      | Total number of lost blocks in this worker.                  |
| Worker.BlocksPromoted                   | COUNTER      | Total number of times any one of the blocks in this worker moved to a new tier. |
| Worker.BytesReadDomain                  | COUNTER      | Total number of bytes read from goosefs storage via domain socket by this worker |
| Worker.BytesReadDomainThroughput        | METER        | Bytes read throughput from goosefs storage via domain socket by this worker |
| Worker.BytesReadPerUfs                  | COUNTER      | Total number of bytes read from a specific goosefs UFS by this worker |
| Worker.BytesReadRemote                  | COUNTER      | Total number of bytes read from goosefs storage managed by this worker and underlying UFS if data cannot be found in the goosefs storage. This does not include short-circuit local reads and domain socket reads. |
| Worker.BytesReadRemoteThroughput        | METER        | Total number of bytes read from goosefs storage managed by this worker and underlying UFS if data cannot be found in the goosefs storage. This does not include short-circuit local reads and domain socket reads. |
| Worker.BytesReadUfsThroughput           | METER        | Bytes read throughput from all goosefs UFSes by this worker  |
| Worker.BytesWrittenDomain               | COUNTER      | Total number of bytes written to goosefs storage via domain socket by this worker |
| Worker.BytesWrittenDomainThroughput     | METER        | Throughput of bytes written to goosefs storage via domain socket by this worker |
| Worker.BytesWrittenPerUfs               | COUNTER      | Total number of bytes written to a specific goosefs UFS by this worker |
| Worker.BytesWrittenRemote               | COUNTER      | Total number of bytes written to goosefs storage or the underlying UFS by this worker. This does not include short-circuit local writes and domain socket writes. |
| Worker.BytesWrittenRemoteThroughput     | METER        | Bytes write throughput to goosefs storage or the underlying UFS by this workerThis does not include short-circuit local writes and domain socket writes. |
| Worker.BytesWrittenUfsThroughput        | METER        | Bytes write throughput to all goosefs UFSes by this worker   |
| Worker.CapacityFree                     | GAUGE        | Total free bytes on all tiers of a specific goosefs worker   |
| Worker.CapacityTotal                    | GAUGE        | Total capacity (in bytes) on all tiers of a specific goosefs worker |
| Worker.CapacityUsed                     | GAUGE        | Total used bytes on all tiers of a specific goosefs worker   |

动态监控指标如下：

| **指标名称**               | **指标类型** | **指标描述**                                                 |
| -------------------------- | ------------ | ------------------------------------------------------------ |
| Worker.UfsSessionCount-Ufs | GAUGE        | The total number of currently opened UFS sessions to connect to the given |
| Worker.                    | TIMER        | The duration statistics of RPC calls exposed on workers      |


## 客户端监控指标

客户端监控指标会通过指定的用户 ID 或者客户端的 IP 维度汇聚，如果已经在 GooseFS 中注册好用户 ID，则会优先按照用户 ID 维度汇聚。用户 ID 可以通过 goosefs.user.app.id 指定。客户端监控指标如下：

| **指标名称**                            | **指标类型** | **指标描述**                                                 |
| --------------------------------------- | ------------ | ------------------------------------------------------------ |
| Client.BytesReadLocal                   | COUNTER      | Total number of bytes short-circuit read from local storage by this client |
| Client.BytesReadLocalThroughput         | METER        | Bytes throughput short-circuit read from local storage by this client |
| Client.BytesWrittenLocal                | COUNTER      | Total number of bytes short-circuit written to local storage by this client |
| Client.BytesWrittenLocalThroughput      | METER        | Bytes throughput short-circuit written to local storage by this client |
| Client.BytesWrittenUfs                  | COUNTER      | Total number of bytes write to goosefs UFS by this client    |
| Client.CacheBytesEvicted                | METER        | Total number of bytes evicted from the client cache.         |
| Client.CacheBytesReadCache              | METER        | Total number of bytes read from the client cache.            |
| Client.CacheBytesReadExternal           | METER        | Total number of bytes read from external storage due to a cache miss on the client cache. |
| Client.CacheBytesRequestedExternal      | METER        | Total number of bytes the user requested to read which resulted in a cache miss. This number may be smaller than Client.CacheBytesReadExternal due to chunk reads. |
| Client.CacheBytesWrittenCache           | METER        | Total number of bytes written to the client cache.           |
| Client.CacheCleanupGetErrors            | COUNTER      | Number of failures when cleaning up a failed cache read.     |
| Client.CacheCleanupPutErrors            | COUNTER      | Number of failures when cleaning up a failed cache write.    |
| Client.CacheCreateErrors                | COUNTER      | Number of failures when creating a cache in the client cache. |
| Client.CacheDeleteErrors                | COUNTER      | Number of failures when deleting cached data in the client cache. |
| Client.CacheDeleteNonExistingPageErrors | COUNTER      | Number of failures when deleting pages due to absence.       |
| Client.CacheDeleteNotReadyErrors        | COUNTER      | Number of failures when when cache is not ready to delete pages. |
| Client.CacheDeleteStoreDeleteErrors     | COUNTER      | Number of failures when deleting pages due to failed delete in page stores. |
| Client.CacheGetErrors                   | COUNTER      | Number of failures when getting cached data in the client cache. |
| Client.CacheGetNotReadyErrors           | COUNTER      | Number of failures when cache is not ready to get pages.     |
| Client.CacheGetStoreReadErrors          | COUNTER      | Number of failures when getting cached data in the client cache due to failed read from page stores. |
| Client.CacheHitRate                     | GAUGE        | Cache hit rate: (# bytes read from cache) / (# bytes requested). |
| Client.CachePages                       | COUNTER      | Total number of pages in the client cache.                   |
| Client.CachePagesEvicted                | METER        | Total number of pages evicted from the client cache.         |
| Client.CachePutAsyncRejectionErrors     | COUNTER      | Number of failures when putting cached data in the client cache due to failed injection to async write queue. |
| Client.CachePutBenignRacingErrors       | COUNTER      | Number of failures when adding pages due to racing eviction. This error is benign. |
| Client.CachePutErrors                   | COUNTER      | Number of failures when putting cached data in the client cache. |
| Client.CachePutEvictionErrors           | COUNTER      | Number of failures when putting cached data in the client cache due to failed eviction. |
| Client.CachePutInsufficientSpaceErrors  | COUNTER      | Number of failures when putting cached data in the client cache due to insufficient space made after eviction. |      |
| Client.CachePutNotReadyErrors           | COUNTER      | Number of failures when cache is not ready to add pages.     |
| Client.CachePutStoreDeleteErrors        | COUNTER      | Number of failures when putting cached data in the client cache due to failed deletes in page store. |      |
| Client.CachePutStoreWriteErrors         | COUNTER      | Number of failures when putting cached data in the client cache due to failed writes to page store. |      |
| Client.CacheSpaceAvailable              | GAUGE        | Amount of bytes available in the client cache.               |
| Client.CacheSpaceUsed                   | GAUGE        | Amount of bytes used by the client cache.                    |
| Client.CacheSpaceUsedCount              | COUNTER      | Amount of bytes used by the client cache as a counter.       |
| Client.CacheState                       | COUNTER      | State of the cache: 0 (NOT_IN_USE), 1 (READ_ONLY) and 2 (READ_WRITE) |
| Client.CacheStoreDeleteTimeout          | COUNTER      | Number of timeouts when deleting pages from page store.      |
| Client.CacheStoreGetTimeout             | COUNTER      | Number of timeouts when reading pages from page store.       |
| Client.CacheStorePutTimeout             | COUNTER      | Number of timeouts when writing new pages to page store.     |
| Client.CacheStoreThreadsRejected        | COUNTER      | Number of rejection of I/O threads on submitting tasks to thread pool, likely due to unresponsive local file system. |
| Client.CacheUnremovableFiles            | COUNTER      | Amount of bytes unusable managed by the client cache.        |


## 进程监控指标

进程监控指标可以在 Cluster、Master 和 Worker 中收集并汇聚。主要包括 JVM 信息、垃圾回收信息、内存占用信息三大类。

JVM 信息包括以下内容：

| **指标名称** | **指标描述**           |
| ------------ | ---------------------- |
| name         | The name of the JVM    |
| uptime       | The uptime of the JVM  |
| vendor       | The current JVM vendor |

垃圾回收监控指标包括以下内容：

| **指标名称**       | **指标描述**                    |
| ------------------ | ------------------------------- |
| PS-MarkSweep.count | Total number of mark and sweep  |
| PS-MarkSweep.time  | The time used to mark and sweep |
| PS-Scavenge.count  | Total number of scavenge        |
| PS-Scavenge.time   | The time used to scavenge       |

内存占用监控指标记录了内存使用情况的概述和详情信息，部分监控指标如下：

| **指标名称**                      | **指标描述**                                                 |
| --------------------------------- | ------------------------------------------------------------ |
| total.committed                   | The amount of memory in bytes that is guaranteed to be available for use by the JVM |
| total.init                        | The amount of the memory in bytes that is available for use by the JVM | 
| total.max                         | The maximum amount of memory in bytes that is available for use by the JVM | 
| total.used                        | The amount of memory currently used in bytes                 |
| heap.committed                    | The amount of memory from heap area guaranteed to be available |
| heap.init                         | The amount of memory from heap area available at initialization |
| heap.max                          | The maximum amount of memory from heap area that is available |
| heap.usage                        | The amount of memory from heap area currently used in GB     |
| heap.used                         | The amount of memory from heap area that has been used       |
| pools.Code-Cache.used             | Used memory of collection usage from the pool from which memory is used for compilation and storage of native code |
| pools.Compressed-Class-Space.used | Used memory of collection usage from the pool from which memory is use for class metadata |
| pools.PS-Eden-Space.used          | Used memory of collection usage from the pool from which memory is initially allocated for most objects |
| pools.PS-Survivor-Space.used      | Used memory of collection usage from the pool containing objects that have survived the garbage collection of the Eden spac |
