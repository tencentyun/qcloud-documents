### Druid-broker

| 指标名称                       | 单位 | 指标含义                                                     |
| ------------------------------ | ---- | ------------------------------------------------------------ |
| YGC                            | 次   | Young GC 次数                                                |
| FGC                            | 次   | Full GC 次数                                                 |
| FGCT                           | s    | Full GC 消耗时间                                             |
| GCT                            | s    | 垃圾回收时间消耗                                             |
| YGCT                           | s    | Young GC 消耗时间                                            |
| S0                             | %    | Survivor 0 区内存使用占比                                    |
| E                              | %    | Eden 区内存使用占比                                          |
| CCS                            | %    | Compressed class space 区内存使用占比                        |
| S1                             | %    | Survivor 1 区内存使用占比                                    |
| O                              | %    | Old 区内存使用占比                                           |
| M                              | %    | Metaspace 区内存使用占比                                     |
| MemHeapInitM                   | MB   | JVM 初始 HeapMem 的数量                                      |
| MemNonHeapInitM                | MB   | JVM 初始 NonHeapMem 的数量                                   |
| MemHeapMaxM                    | MB   | JVM 配置的 HeapMemory 的数量                                 |
| MemHeapCommittedM              | MB   | JVM 当前已经提交的  HeapMemory 的数量                        |
| MemHeapUsedM                   | MB   | JVM 当前已经使用的  HeapMemory 的数量                        |
| MemNonHeapCommittedM           | MB   | JVM 当前已经提交的  NonHeapMemory 的数量                     |
| MemNonHeapUsedM                | MB   | JVM 当前已经使用的  NonHeapMemory 的数量                     |
| ThreadsNew                     | 个   | 当前 NEW 状态线程数量                                          |
| ThreadsRunnable                | 个   | 当前 RUNNABLE 状态线程数量                                     |
| ThreadsBlocked                 | 个   | 当前 BLOCKED 状态线程数量                                      |
| ThreadsWaiting                 | 个   | 当前 WAITING 状态线程数量                                      |
| ThreadsTimedWaiting            | 个   | 当前 TIMED_WAITING 状态线程数量                                |
| ThreadsTerminated              | 个   | 当前 TERMINATED 状态线程数量                                   |
| LogFatal                       | 次   | FATAL 级别日志数量                                            |
| LogError                       | 次   | ERROR 级别日志数量                                            |
| LogWarn                        | 次   | WARN 级别日志数量                                             |
| LogInfo                        | 次   | INFO 级别日志数量                                             |
| jetty.numOpenConnections       | 个   | 开启的 Jetty 连接数                                            |
| segment.scan.pending           | 个   | Number of segments in queue waiting to be  scanned           |
| broker.query.count             | 次   | number of total queries                                      |
| broker.query.success.count     | 次   | number of queries successfully processed                     |
| broker.query.failed.count      | 次   | number of failed queries                                     |
| broker.query.interrupted.count | 次   | number of queries interrupted due to cancellation  or timeout |
| normal.count                   | 个   | 查询延迟 < 1s的次数                                            |
| abnormal.count                 | 个   | 查询延迟 >= 1s的次数                                           |

### Druid- coordinator

| 指标名称                      | 单位  | 指标含义                                                     |
| ----------------------------- | ----- | ------------------------------------------------------------ |
| segment.assigned.count        | 个    | 被加载到 Druid 集群的 Segment 数量                             |
| segment.moved.count           | 个    | 在 Druid 集群中被移动的 Segment 数量                           |
| segment.dropped.count         | 个    | 在 Druid 集群中由于过期而被删除的 Segment 数量                 |
| segment.deleted.count         | 个    | 在 Druid 集群中由于规则设置而被删除的 Segment 数量             |
| segment.unneeded.count        | 个    | 在 Druid 集群中由于被设置为不再使用而被删除的 Segment 数量     |
| segment.cost.raw              | ms    | Used in cost balancing. The raw cost of  hosting segments.   |
| segment.cost.normalization    | ms    | Used in cost balancing. The normalization  of hosting segments. |
| segment.cost.normalized       | ms    | Used in cost balancing. The normalized  cost of hosting segments. |
| segment.loadQueue.size        | bytes | Size in bytes of segments to load.                           |
| segment.loadQueue.failed      | 个    | Number of segments that failed to load.                      |
| segment.loadQueue.count       | 个    | Number of segments to load.                                  |
| segment.dropQueue.count       | 个    | Number of segments to drop.                                  |
| segment.overshadowed.count    | 个    | Number of overshadowed segments.                             |
| tier.historical.count         | 个    | Number of available historical nodes in  each tier.          |
| tier.replication.factor       | 个    | Configured maximum replication factor in  each tier.         |
| tier.required.capacity        | bytes | Total capacity in bytes required in each  tier.              |
| tier.total.capacity           | bytes | Total capacity in bytes available in each  tier.             |
| compact.task.count            | 个    | Compact 任务数                                              |
| YGC                           | 次    | Young GC 次数                                                |
| FGC                           | 次    | Full GC 次数                                                 |
| FGCT                          | s     | Full GC 消耗时间                                             |
| GCT                           | s     | 垃圾回收时间消耗                                             |
| YGCT                          | s     | Young GC 消耗时间                                            |
| S0                            | %     | Survivor 0 区内存使用占比                                    |
| E                             | %     | Eden 区内存使用占比                                          |
| CCS                           | %     | Compressed class space 区内存使用占比                        |
| S1                            | %     | Survivor 1 区内存使用占比                                    |
| O                             | %     | Old 区内存使用占比                                           |
| M                             | %     | Metaspace 区内存使用占比                                     |
| MemHeapInitM                  | MB    | JVM 初始 HeapMem 的数量                                      |
| MemNonHeapInitM               | MB    | JVM 初始 NonHeapMem 的数量                                   |
| MemHeapMaxM                   | MB    | JVM 配置的 HeapMemory 的数量                                 |
| MemHeapCommittedM             | MB    | JVM 当前已经提交的  HeapMemory 的数量                        |
| MemHeapUsedM                  | MB    | JVM 当前已经使用的  HeapMemory 的数量                        |
| MemNonHeapCommittedM          | MB    | JVM 当前已经提交的  NonHeapMemory 的数量                     |
| MemNonHeapUsedM               | MB    | JVM 当前已经使用的  NonHeapMemory 的数量                     |
| ThreadsNew                    | 个    | 当前 NEW 状态线程数量                                          |
| ThreadsRunnable               | 个    | 当前 RUNNABLE 状态线程数量                                     |
| ThreadsBlocked                | 个    | 当前 BLOCKED 状态线程数量                                      |
| ThreadsWaiting                | 个    | 当前 WAITING 状态线程数量                                      |
| ThreadsTimedWaiting           | 个    | 当前 TIMED_WAITING 状态线程数量                                |
| ThreadsTerminated             | 个    | 当前 TERMINATED 状态线程数量                                   |
| LogFatal                      | 次    | FATAL 级别日志数量                                            |
| LogError                      | 次    | ERROR 级别日志数量                                            |
| LogWarn                       | 次    | WARN 级别日志数量                                             |
| LogInfo                       | 次    | INFO 级别日志数量                                             |
| segment.size                  | bytes | Total size of used segments in a data  source. Emitted only for data sources to which at least one used segment  belongs. |
| segment.count                 | 个    | Number of used segments belonging to a  data source. Emitted only for data sources to which at least one used segment  belongs. |
| segment.unavailable.count     | 个    | Number of segments (not including  replicas) left to load until segments that should be loaded in the cluster  are available for queries. |
| segment.underReplicated.count | 个    | Number of segments (including replicas)  left to load until segments that should be loaded in the cluster are  available for queries. |
| jetty.numOpenConnections      | 个    | 开启的 Jetty 连接数                                            |

 

### Druid- historical

| 指标名称                           | 单位  | 指标含义                                                     |
| ---------------------------------- | ----- | ------------------------------------------------------------ |
| YGC                                | 次    | Young GC 次数                                                |
| FGC                                | 次    | Full GC 次数                                                 |
| FGCT                               | s     | Full GC 消耗时间                                             |
| GCT                                | s     | 垃圾回收时间消耗                                             |
| YGCT                               | s     | Young GC 消耗时间                                            |
| S0                                 | %     | Survivor 0 区内存使用占比                                    |
| E                                  | %     | Eden 区内存使用占比                                          |
| CCS                                | %     | Compressed class space 区内存使用占比                        |
| S1                                 | %     | Survivor 1 区内存使用占比                                    |
| O                                  | %     | Old 区内存使用占比                                           |
| M                                  | %     | Metaspace 区内存使用占比                                     |
| MemHeapInitM                       | MB    | JVM 初始 HeapMem 的数量                                      |
| MemNonHeapInitM                    | MB    | JVM 初始 NonHeapMem 的数量                                   |
| MemHeapMaxM                        | MB    | JVM 配置的 HeapMemory 的数量                                 |
| MemHeapCommittedM                  | MB    | JVM 当前已经提交的  HeapMemory 的数量                        |
| MemHeapUsedM                       | MB    | JVM 当前已经使用的  HeapMemory 的数量                        |
| MemNonHeapCommittedM               | MB    | JVM 当前已经提交的  NonHeapMemory 的数量                     |
| MemNonHeapUsedM                    | MB    | JVM 当前已经使用的  NonHeapMemory 的数量                     |
| ThreadsNew                         | 个    | 当前 NEW 状态线程数量                                          |
| ThreadsRunnable                    | 个    | 当前 RUNNABLE 状态线程数量                                     |
| ThreadsBlocked                     | 个    | 当前 BLOCKED 状态线程数量                                      |
| ThreadsWaiting                     | 个    | 当前 WAITING 状态线程数量                                      |
| ThreadsTimedWaiting                | 个    | 当前 TIMED_WAITING 状态线程数量                                |
| ThreadsTerminated                  | 个    | 当前 TERMINATED 状态线程数量                                   |
| LogFatal                           | 次    | FATAL 级别日志数量                                            |
| LogError                           | 次    | ERROR 级别日志数量                                            |
| LogWarn                            | 次    | WARN 级别日志数量                                             |
| LogInfo                            | 次    | INFO 级别日志数量                                             |
| jetty.numOpenConnections           | 个    | 开启的 Jetty 连接数                                            |
| segment.scan.pending               | 个    | Number of segments in queue waiting to be  scanned           |
| segment.max                        | bytes | Maximum byte limit available for segments                    |
| segment.pendingdelete              | bytes | On-disk size in bytes of segments that  are waiting to be cleared out |
| historical.query.count             | 次    | historical 查询总次数                                         |
| historical.query.success.count     | 次    | historical 查询成功次数                                       |
| historical.query.failed.count      | 次    | historical 查询失败次数                                       |
| historical.query.interrupted.count | 次    | historical 查询被中断次数                                     |
| normal.count                       | 个    | 查询延迟 < 1s的次数                                            |
| abnormal.count                     | 个    | 查询延迟 >= 1s的次数                                           |

### Druid- middleManager

| 指标名称                 | 单位 | 指标含义                                 |
| ------------------------ | ---- | ---------------------------------------- |
| YGC                      | 次   | Young GC 次数                            |
| FGC                      | 次   | Full GC 次数                             |
| FGCT                     | s    | Full GC 消耗时间                         |
| GCT                      | s    | 垃圾回收时间消耗                         |
| YGCT                     | s    | Young GC 消耗时间                        |
| S0                       | %    | Survivor 0 区内存使用占比                |
| E                        | %    | Eden 区内存使用占比                      |
| CCS                      | %    | Compressed class space 区内存使用占比    |
| S1                       | %    | Survivor 1 区内存使用占比                |
| O                        | %    | Old 区内存使用占比                       |
| M                        | %    | Metaspace 区内存使用占比                 |
| MemHeapInitM             | MB   | JVM 初始 HeapMem 的数量                  |
| MemNonHeapInitM          | MB   | JVM 初始 NonHeapMem 的数量               |
| MemHeapMaxM              | MB   | JVM 配置的 HeapMemory 的数量             |
| MemHeapCommittedM        | MB   | JVM 当前已经提交的 HeapMemory 的数量    |
| MemHeapUsedM             | MB   | JVM 当前已经使用的 HeapMemory 的数量    |
| MemNonHeapCommittedM     | MB   | JVM 当前已经提交的 NonHeapMemory 的数量 |
| MemNonHeapUsedM          | MB   | JVM 当前已经使用的 NonHeapMemory 的数量 |
| ThreadsNew               | 个   | 当前 NEW 状态线程数量                      |
| ThreadsRunnable          | 个   | 当前 RUNNABLE 状态线程数量                 |
| ThreadsBlocked           | 个   | 当前 BLOCKED 状态线程数量                  |
| ThreadsWaiting           | 个   | 当前 WAITING 状态线程数量                  |
| ThreadsTimedWaiting      | 个   | 当前 TIMED_WAITING 状态线程数量            |
| ThreadsTerminated        | 个   | 当前 TERMINATED 状态线程数量               |
| LogFatal                 | 次   | FATAL 级别日志数量                        |
| LogError                 | 次   | ERROR 级别日志数量                        |
| LogWarn                  | 次   | WARN 级别日志数量                         |
| LogInfo                  | 次   | INFO 级别日志数量                         |
| jetty.numOpenConnections | 个   | 开启的 Jetty 连接数                        |

 

### Druid- overlord

 

| 指标名称                 | 单位 | 指标含义                                 |
| ------------------------ | ---- | ---------------------------------------- |
| YGC                      | 次   | Young GC 次数                            |
| FGC                      | 次   | Full GC 次数                             |
| FGCT                     | s    | Full GC 消耗时间                         |
| GCT                      | s    | 垃圾回收时间消耗                         |
| YGCT                     | s    | Young GC 消耗时间                        |
| S0                       | %    | Survivor 0 区内存使用占比                |
| E                        | %    | Eden 区内存使用占比                      |
| CCS                      | %    | Compressed class space 区内存使用占比    |
| S1                       | %    | Survivor 1 区内存使用占比                |
| O                        | %    | Old 区内存使用占比                       |
| M                        | %    | Metaspace 区内存使用占比                 |
| MemHeapInitM             | MB   | JVM 初始 HeapMem 的数量                  |
| MemNonHeapInitM          | MB   | JVM 初始 NonHeapMem 的数量               |
| MemHeapMaxM              | MB   | JVM 配置的 HeapMemory 的数量             |
| MemHeapCommittedM        | MB   | JVM 当前已经提交的 HeapMemory 的数量    |
| MemHeapUsedM             | MB   | JVM 当前已经使用的 HeapMemory 的数量    |
| MemNonHeapCommittedM     | MB   | JVM 当前已经提交的 NonHeapMemory 的数量 |
| MemNonHeapUsedM          | MB   | JVM 当前已经使用的 NonHeapMemory 的数量 |
| ThreadsNew               | 个   | 当前 NEW 状态线程数量                      |
| ThreadsRunnable          | 个   | 当前 RUNNABLE 状态线程数量                 |
| ThreadsBlocked           | 个   | 当前 BLOCKED 状态线程数量                  |
| ThreadsWaiting           | 个   | 当前 WAITING 状态线程数量                  |
| ThreadsTimedWaiting      | 个   | 当前 TIMED_WAITING 状态线程数量            |
| ThreadsTerminated        | 个   | 当前 TERMINATED 状态线程数量               |
| LogFatal                 | 次   | FATAL 级别日志数量                        |
| LogError                 | 次   | ERROR 级别日志数量                        |
| LogWarn                  | 次   | WARN 级别日志数量                         |
| LogInfo                  | 次   | INFO 级别日志数量                         |
| jetty.numOpenConnections | 个   | 开启的 Jetty 连接数                        |

### Druid- router

| 指标名称                 | 单位 | 指标含义                                 |
| ------------------------ | ---- | ---------------------------------------- |
| YGC                      | 次   | Young GC 次数                            |
| FGC                      | 次   | Full GC 次数                             |
| FGCT                     | s    | Full GC 消耗时间                         |
| GCT                      | s    | 垃圾回收时间消耗                         |
| YGCT                     | s    | Young GC 消耗时间                        |
| S0                       | %    | Survivor 0 区内存使用占比                |
| E                        | %    | Eden 区内存使用占比                      |
| CCS                      | %    | Compressed class space 区内存使用占比    |
| S1                       | %    | Survivor 1 区内存使用占比                |
| O                        | %    | Old 区内存使用占比                       |
| M                        | %    | Metaspace 区内存使用占比                 |
| MemHeapInitM             | MB   | JVM 初始 HeapMem 的数量                  |
| MemNonHeapInitM          | MB   | JVM 初始 NonHeapMem 的数量               |
| MemHeapMaxM              | MB   | JVM 配置的 HeapMemory 的数量             |
| MemHeapCommittedM        | MB   | JVM 当前已经提交的 HeapMemory 的数量    |
| MemHeapUsedM             | MB   | JVM 当前已经使用的 HeapMemory 的数量    |
| MemNonHeapCommittedM     | MB   | JVM 当前已经提交的 NonHeapMemory 的数量 |
| MemNonHeapUsedM          | MB   | JVM 当前已经使用的 NonHeapMemory 的数量 |
| ThreadsNew               | 个   | 当前 NEW 状态线程数量                      |
| ThreadsRunnable          | 个   | 当前 RUNNABLE 状态线程数量                 |
| ThreadsBlocked           | 个   | 当前 BLOCKED 状态线程数量                  |
| ThreadsWaiting           | 个   | 当前 WAITING 状态线程数量                  |
| ThreadsTimedWaiting      | 个   | 当前 TIMED_WAITING 状态线程数量            |
| ThreadsTerminated        | 个   | 当前 TERMINATED 状态线程数量               |
| LogFatal                 | 次   | FATAL 级别日志数量                        |
| LogError                 | 次   | ERROR 级别日志数量                        |
| LogWarn                  | 次   | WARN 级别日志数量                         |
| LogInfo                  | 次   | INFO 级别日志数量                         |
| jetty.numOpenConnections | 个   | 开启的 Jetty 连接数                        |

 
