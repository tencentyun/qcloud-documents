### Alluxio-概览

| 指标名称                                     | 指标单位 | 指标含义                                                |
| -------------------------------------------- | -------- | ------------------------------------------------------- |
| 数据读写总量\_BytesReadAlluxio                | Bytes    | 所有 worker 上报的从 Alluxio 存储读取的总字节数             |
| 数据读写总量\_BytesReadUfsAll                 | Bytes    | 所有 worker 从所有 Alluxio UFSes 读取的字节总数            |
| 数据读写总量\_BytesReadDomain                 | Bytes    | 所有 worker 上报的通过域套接字从 Alluxio 存储读取的总字节数 |
| 数据读写总量\_BytesReadLocal                  | Bytes    | 所有客户端从本地存储中短路读取的字节总数                |
| 数据读写总量\_BytesReadPerUfs                 | Bytes    | 所有 worker 从特定 UFS 读取的总字节数                       |
| 数据读写总量\_BytesWrittenAlluxio             | Bytes    | 写入所有 worker 的 Alluxio 存储的总字节数                   |
| 数据读写总量\_BytesWrittenUfsAll              | Bytes    | 所有 worker 写入所有 Alluxio UFSes 的总字节数               |
| 数据读写总量\_BytesWrittenDomain              | Bytes    | 所有 worker 通过域套接字写入 Alluxio 存储的总字节数          |
| 数据读写总量\_BytesWrittenLocal               | Bytes    | 所有客户端短路写入本地存储的总字节数                    |
| 数据读写总量\_BytesWrittenPerUfs              | Bytes    | 所有 worker 写入特定 Alluxio UFS 的总字节数                 |
| 数据读写吞吐量\_BytesReadAlluxioThroughput    | Bytes    | 所有 worker 从 Alluxio 存储读取数据的吞吐量                 |
| 数据读写吞吐量\_BytesReadUfsThroughput        | Bytes    | 所有 worker 从所有 Alluxio UFSes 读取的吞吐量                |
| 数据读写吞吐量\_BytesReadDomainThroughput     | Bytes    | 所有 worker 通过域套接字从 Alluxio 存储读取的字节吞吐量     |
| 数据读写吞吐量\_BytesReadLocalThroughput      | Bytes    | 所有客户端从本地存储中短路读取的字节吞吐量              |
| 数据读写吞吐量\_BytesWrittenAlluxioThroughput | Bytes    | 所有 worker 写入 Alluxio 存储的吞吐量                       |
| 数据读写吞吐量\_BytesWrittenUfsThroughput     | Bytes    | 所有 worker 写入所有 Alluxio UFSes 的吞吐量                 |
| 数据读写吞吐量\_BytesWrittenDomainThroughput  | Bytes    | 所有 worker 通过域套接字写入 Alluxio 存储的字节吞吐量       |
| 数据读写吞吐量\_BytesWrittenLocalThroughput   | Bytes    | 所有客户端写入本地存储的字节吞吐量                      |
| worker 的层上容量\_CapacityFree                | Bytes    | 所有 worker 的所有层上的总可用字节                        |
| worker 的层上容量\_CapacityTotal               | Bytes    | 所有 worker 的所有层上的总容量                            |
| worker 的层上容量\_CapacityUsed                | Bytes    | 所有 worker 的所有层上的已用字节总数                      |
| worker 总数\_Workers                           | 个       | 群集中的 active worker 总数                               |


### Alluxio-Master

| 指标名称                                 | 指标单位 | 指标含义                                |
| ---------------------------------------- | -------- | --------------------------------------- |
| YGC                                      | 次       | Young GC 次数                          |
| FGC                                      | 次       | Full GC 次数                           |
| FGCT                                     | s        | Full GC 消耗时间                       |
| GCT                                      | s        | 垃圾回收时间消耗                        |
| YGCT                                     | s        | Young GC 消耗时间                      |
| S0                                       | %        | Survivor 0 区内存使用占比               |
| E                                        | %        | Eden 区内存使用占比                     |
| CCS                                      | %        | Compressed class space 区内存使用占比  |
| S1                                       | %        | Survivor 1 区内存使用占比               |
| O                                        | %        | Old 区内存使用占比                      |
| M                                        | %        | Metaspace 区内存使用占比               |
| MemNonHeapUsedM                          | MB       | JVM 当前已经使用的 NonHeapMemory 的数量 |
| MemNonHeapCommittedM                     | MB       | JVM 当前已经提交的 NonHeapMemory 的数量 |
| MemHeapUsedM                             | MB       | JVM 当前已经使用的 HeapMemory 的数量    |
| MemHeapCommittedM                        | MB       | JVM 当前已经提交的 HeapMemory 的数量    |
| MemHeapMaxM                              | MB       | JVM 配置的 HeapMemory 的数量            |
| MemHeapInitM                             | MB       | JVM 初始 HeapMem 的数量                 |
| MemNonHeapInitM                          | MB       | JVM 初始 NonHeapMem 的数量              |
| CompleteFile 操作\_CompleteFileOps         | 个       | CompleteFile 操作总数                    |
| CompleteFile 操作\_FilesCompleted          | 个       | 成功的 CompleteFile 操作总数              |
| CreateDirectory 操作\_CreateDirectoryOps   | 个       | CreateDirectory 操作总数                 |
| CreateDirectory 操作\_DirectoriesCreated   | 个       | 成功的 CreateDirectory 操作总数           |
| CreateFile 操作\_CreateFileOps             | 个       | CreateFile 操作总数                      |
| CreateFile 操作\_FilesCreated              | 个       | 成功的 CreateFile 操作总数                |
| Delete 操作\_DeletePathOps                 | 个       | Delete 操作总数                          |
| Delete 操作\_PathsDeleted                  | 个       | 成功 Delete 操作的总数                    |
| FreeFile 操作\_FreeFileOps                 | 个       | FreeFile 操作总数                        |
| FreeFile 操作\_FilesFreed                  | 个       | 成功的 FreeFile 操作总数                  |
| GetFileBlockInfo 操作\_GetFileBlockInfoOps | 个       | GetFileBlockInfo 操作总数                |
| GetFileBlockInfo 操作\_FileBlockInfosGot   | 个       | 成功的 GetFileBlockInfo 操作总数          |
| GetFileInfo 操作\_GetFileInfoOps           | 个       | GetFileInfo 操作总数                     |
| GetFileInfo 操作\_FileInfosGot             | 个       | 成功的 GetFileInfo 操作总数               |
| GetNewBlock 操作\_GetNewBlockOps           | 个       | GetNewBlock 操作总数                     |
| GetNewBlock 操作\_NewBlocksGot             | 个       | 成功的 GetNewBlock 操作总数               |
| Mount 操作\_MountOps                       | 个       | Mount 操作总数                           |
| Mount 操作\_PathsMounted                   | 个       | 成功 Mount 操作总数                       |
| Unmount 操作\_UnmountOps                   | 个       | Unmount 操作总数                         |
| Unmount 操作\_PathsUnmounted               | 个       | 成功 Unmount 操作的总数                   |
| Rename 操作\_RenamePathOps                 | 个       | Rename 操作总数                          |
| Rename 操作\_PathsRenamed                  | 个       | 成功的 Rename 操作总数                    |
| SetAcl 操作\_SetAclOps                     | 个       | SetAcl 操作总数                          |
| SetAttribute 操作\_SetAttributeOps         | 个       | SetAttribute 操作总数                    |
| 操作文件总数\_FilesPersisted              | 个       | 成功保存的文件总数                      |
| 操作文件总数\_FilesPinned                 | 个       | 当前固定的文件总数                      |
| 文件目录总数\_TotalPaths                  | 个       | Alluxio 命名空间中的文件和目录总数       |

### Alluxio-Worker

| 指标名称                                  | 指标单位 | 指标含义                                   |
| ----------------------------------------- | -------- | ------------------------------------------ |
| YGC                                       | 次       | Young GC 次数                             |
| FGC                                       | 次       | Full GC 次数                              |
| FGCT                                      | s        | Full GC 消耗时间                          |
| GCT                                       | s        | 垃圾回收时间消耗                           |
| YGCT                                      | s        | Young GC 消耗时间                         |
| S0                                        | %        | Survivor 0 区内存使用占比                  |
| E                                         | %        | Eden 区内存使用占比                        |
| CCS                                       | %        | Compressed class space 区内存使用占比     |
| S1                                        | %        | Survivor 1 区内存使用占比                  |
| O                                         | %        | Old 区内存使用占比                         |
| M                                         | %        | Metaspace 区内存使用占比                  |
| MemNonHeapUsedM                           | MB       | JVM 当前已经使用的 NonHeapMemory 的数量    |
| MemNonHeapCommittedM                      | MB       | JVM 当前已经提交的 NonHeapMemory 的数量    |
| MemHeapUsedM                              | MB       | JVM 当前已经使用的 HeapMemory 的数量       |
| MemHeapCommittedM                         | MB       | JVM 当前已经提交的 HeapMemory 的数量       |
| MemHeapMaxM                               | MB       | JVM 配置的 HeapMemory 的数量               |
| MemHeapInitM                              | MB       | JVM 初始 HeapMem 的数量                    |
| MemNonHeapInitM                           | MB       | JVM 初始 NonHeapMem 的数量                 |
| Async 缓存请求\_AsyncCacheDuplicateRequests | 个       | worker 接收的重复 async 缓存请求总数          |
| Async 缓存请求\_AsyncCacheRequests          | 个       | worker 接收的 async 缓存请求总数              |
| Async 缓存块数量\_AsyncCacheFailedBlocks    | 个       | worker async 缓存失败的块总数               |
| Async 缓存块数量\_AsyncCacheRemoteBlocks    | 个       | 需要从远程源进行 async 缓存的块总数          |
| Async 缓存块数量\_AsyncCacheSucceededBlocks | 个       | worker async 缓存成功的块总数               |
| Async 缓存块数量\_AsyncCacheUfsBlocks       | 个       | 需要从本地源进行 async 缓存的数据块总数      |
| BlocksAccessed                            | 个       | 访问此 worker 中任何一个块的总次数           |
| BlocksCached                              | 个       | 在 worker 中用于缓存数据的块总数             |
| BlocksCancelled                           | 个       | worker 中中止的临时块总数                   |
| BlocksDeleted                             | 个       | 按外部请求列出的此 worker 中已删除的块总数   |
| BlocksEvicted                             | 个       | worker 中逐出的块总数                       |
| BlocksLost                                | 个       | worker 中丢失的数据块总数                   |
| BlocksPromoted                            | 个       | worker 中的任何一个数据块移动到新层的总次数 |
| Worker 的层上容量\_CapacityFree             | Bytes    | worker 的所有层上的总可用字节               |
| Worker 的层上容量\_CapacityTotal            | Bytes    | worker 的所有层上的总容量                   |
| Worker 的层上容量\_CapacityUsed             | Bytes    | worker 的所有层上的已用字节总数             |

 
