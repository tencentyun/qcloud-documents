### HIVE-HiveMetaStore

| 指标名称 | 指标单位 | 指标含义                              |
| -------- | -------- | ------------------------------------- |
| YGC      | 次       | Young GC 次数                         |
| FGC      | 次       | Full GC 次数                          |
| FGCT     | s        | Full GC 消耗时间                      |
| GCT      | s        | 垃圾回收时间消耗                      |
| YGCT     | s        | Young GC 消耗时间                     |
| S0       | %        | Survivor 0区内存使用占比              |
| E        | %        | Eden 区内存使用占比                   |
| CCS      | %        | Compressed class space 区内存使用占比 |
| S1       | %        | Survivor 1区内存使用占比              |
| O        | %        | Old 区内存使用占比                    |
| M        | %        | Metaspace 区内存使用占比              |

### HIVE-HiveServer2

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
| S1                      | %        | Survivor 1区内存使用占比                |
| O                       | %        | Old 区内存使用占比                      |
| M                       | %        | Metaspace 区内存使用占比                |
| MemNonHeapUsedM         | MB       | JVM 当前已经使用的 NonHeapMemory 的数量 |
| MemNonHeapCommittedM    | MB       | JVM 当前已经提交的 NonHeapMemory 的数量 |
| MemHeapUsedM            | MB       | JVM 当前已经使用的 HeapMemory 的数量    |
| MemHeapCommittedM       | MB       | JVM 当前已经提交的 HeapMemory 的数量    |
| MemHeapMaxM             | MB       | JVM 配置的 HeapMemory 的数量            |
| MemHeapInitM            | MB       | JVM 初始 HeapMem 的数量                 |
| MemNonHeapInitM         | MB       | JVM 初始 NonHeapMem 的数量              |
| ProcessCpuLoad          | %        | CPU 利用率                              |
| MaxFileDescriptorCount  | 个       | 最大文件描述符数                        |
| OpenFileDescriptorCount | 个       | 已打开文件描述符数                      |
| ProcessCpuTime          | ms       | CPU 累计使用时间                        |
| Uptime                  | s        | 进程运行时长                            |
| DaemonThreadCount       | 个       | Daemon 线程数                           |
| ThreadCount             | 个       | 总线程数                                |

### HIVE-HiveWebHcat

| 指标名称 | 指标单位 | 指标含义                              |
| -------- | -------- | ------------------------------------- |
| YGC      | 次       | Young GC 次数                         |
| FGC      | 次       | Full GC 次数                          |
| FGCT     | s        | Full GC 消耗时间                      |
| GCT      | s        | 垃圾回收时间消耗                      |
| YGCT     | s        | Young GC 消耗时间                     |
| S0       | %        | Survivor 0 区内存使用占比             |
| E        | %        | Eden 区内存使用占比                   |
| CCS      | %        | Compressed class space 区内存使用占比 |
| S1       | %        | Survivor 1 区内存使用占比             |
| O        | %        | Old 区内存使用占比                    |
| M        | %        | Metaspace 区内存使用占比              |
