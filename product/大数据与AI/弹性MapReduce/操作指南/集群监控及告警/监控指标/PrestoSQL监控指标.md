>!PrestoSQL 指标目前仅支持 PrestoSQL322 和 PrestoSQL350 及以上版本。


### PrestoSQL-概览

| 指标名称                | 指标单位 | 指标含义           |
| ----------------------- | -------- | ------------------ |
| Active                  | 个       | 活跃节点数量       |
| Total                   | 个       | 总节点数量         |
| Failed                  | 个       | 失败节点数量       |
| RunningQueries          | 个       | 正在运行的查询总数 |
| QueuedQueries           | 个       | 等待状态的查询总数 |
| FailedQueries           | 个/min   | 失败的查询总数     |
| AbandonedQueries        | 个/min   | 放弃的查询总数     |
| CanceledQueries         | 个/min   | 取消的查询总数     |
| SubmittedQueries        | 个/min   | 提交的查询的总数   |
| CompletedQueries        | 个/min   | 完成的查询总数     |
| StartedQueries          | 个/min   | 已启动的查询总数   |
| InputDataSizeOneMinute  | GB/min   | 输入数据速率       |
| OutputDataSizeOneMinute | GB/min   | 输出数据速率       |

### PrestoSQL-Coordinator

| 指标名称                | 指标单位 | 指标含义                                |
| ----------------------- | -------- | --------------------------------------- |
| YGC                     | 次       | Young GC 次数                           |
| FGC                     | 次       | Full GC 次数                            |
| FGCT                    | s        | Full GC 消耗时间                        |
| GCT                     | s        | 垃圾回收时间消耗                        |
| YGCT                    | s        | Young GC 消耗时间                       |
| S0                      | %        | Survivor 0区内存使用占比                |
| E                       | %        | Eden 区内存使用占比                     |
| CCS                     | %        | Compressed class space 区内存使用占比   |
| S1                      | %        | Survivor 1 区内存使用占比                |
| O                       | %        | Old 区内存使用占比                      |
| M                       | %        | Metaspace 区内存使用占比                |
| MemNonHeapUsedM         | MB       | JVM 当前已经使用的 NonHeapMemory 的数量 |
| MemNonHeapCommittedM    | MB       | JVM 当前已经提交的 NonHeapMemory 的数量 |
| MemHeapUsedM            | MB       | JVM 当前已经使用的 HeapMemory 的数量    |
| MemHeapCommittedM       | MB       | JVM 当前已经提交的 HeapMemory 的数量    |
| MemHeapMaxM             | MB       | JVM 配置的 HeapMemory 的数量            |
| MemHeapInitM            | MB       | JVM 初始 HeapMemory的数量               |
| MemNonHeapInitM         | MB       | JVM 初始 NonHeapMemory 的数量           |
| PeakThreadCount         | 个       | 峰值线程数                              |
| ThreadCount             | 个       | 总线程数量                              |
| DaemonThreadCount       | 个       | Daemon 线程数量                          |
| Uptime                  | s        | 进程运行时间                            |
| MaxFileDescriptorCount  | 个       | 最大文件描述符数                        |
| OpenFileDescriptorCount | 个       | 已打开文件描述符数                      |

### PrestoSQL-Worker

| 指标名称                      | 指标单位 | 指标含义                                |
| ----------------------------- | -------- | --------------------------------------- |
| YGC                           | 次       | Young GC 次数                           |
| FGC                           | 次       | Full GC 次数                            |
| FGCT                          | s        | Full GC 消耗时间                        |
| GCT                           | s        | 垃圾回收时间消耗                        |
| YGCT                          | s        | Young GC 消耗时间                       |
| S0                            | %        | Survivor 0 区内存使用占比                |
| E                             | %        | Eden 区内存使用占比                     |
| CCS                           | %        | Compressed class space 区内存使用占比   |
| S1                            | %        | Survivor 1 区内存使用占比                |
| O                             | %        | Old 区内存使用占比                      |
| M                             | %        | Metaspace 区内存使用占比                |
| MemNonHeapUsedM               | MB       | JVM 当前已经使用的 NonHeapMemory 的数量 |
| MemNonHeapCommittedM          | MB       | JVM 当前已经提交的 NonHeapMemory 的数量 |
| MemHeapUsedM                  | MB       | JVM 当前已经使用的 HeapMemory 的数量    |
| MemHeapCommittedM             | MB       | JVM 当前已经提交的 HeapMemory 的数量    |
| MemHeapMaxM                   | MB       | JVM 配置的 HeapMemory 的数量            |
| MemHeapInitM                  | MB       | JVM 初始 HeapMem 的数量                 |
| MemNonHeapInitM               | MB       | JVM 初始 NonHeapMem 的数量              |
| InputDataSize.OneMinute.Rate  | GB/min   | 输入数据速率                            |
| OutputDataSize.OneMinute.Rate | GB/min   | 输出数据速率                            |
| PeakThreadCount               | 个       | 峰值线程数                              |
| ThreadCount                   | 个       | 总线程数量                              |
| DaemonThreadCount             | 个       | Daemon 线程数量                          |
| Uptime                        | s        | 进程运行时间                            |
| MaxFileDescriptorCount        | 个       | 最大文件描述符数                        |
| OpenFileDescriptorCount       | 个       | 已打开文件描述符数                      |

 
