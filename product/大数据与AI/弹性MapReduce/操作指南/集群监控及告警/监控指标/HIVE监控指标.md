### HIVE-HiveMetaStore

| 指标名称                                           | 指标单位 | 指标含义                                |
| -------------------------------------------------- | -------- | --------------------------------------- |
| GC次数_YGC                                         | 次       | Young GC 次数                           |
| GC次数_FGC                                         | 次       | Full GC 次数                            |
| GC时间_FGCT                                        | s        | Full GC 消耗时间                        |
| GC时间_GCT                                         | s        | 垃圾回收时间消耗                        |
| GC时间_YGCT                                        | s        | Young GC 消耗时间                       |
| 内存区域占比_S0                                    | %        | Survivor 0区内存使用占比                |
| 内存区域占比_E                                     | %        | Eden 区内存使用占比                     |
| 内存区域占比_CCS                                   | %        | Compressed class space 区内存使用占比   |
| 内存区域占比_S1                                    | %        | Survivor 1区内存使用占比                |
| 内存区域占比_O                                     | %        | Old 区内存使用占比                      |
| 内存区域占比_M                                     | %        | Metaspace 区内存使用占比                |
| HiveMetaStore_JVM内存_MemHeapUsedM                 | MB       | JVM 当前已经使用的 HeapMemory 的数量    |
| HiveMetaStore_JVM内存_MemHeapCommittedM            | MB       | JVM 已经提交的 HeapMemory 的数量        |
| HiveMetaStore_JVM内存_MemHeapMaxM                  | MB       | JVM 配置的 HeapMemory 的数量             |
| HiveMetaStore_JVM内存_MemHeapInitM                 | MB       | JVM 初始 HeapMemory 的数量               |
| HiveMetaStore_JVM内存_MemNonHeapUsedM              | MB       | JVM 当前已经使用的 NonHeapMemory 的数量 |
| HiveMetaStore_JVM内存_MemNonHeapCommittedM         | MB       | JVM 已经提交的 NonHeapMemory 的数量     |
| HiveMetaStore_JVM内存_MemNonHeapInitM              | MB       | JVM 初始 NonHeapMemory 的数量            |
| HiveMetaStore_文件描述符数_MaxFileDescriptorCount  | 个       | 已打开文件描述符数量                    |
| HiveMetaStore_文件描述符数_OpenFileDescriptorCount | 个       | 最大文件描述符数                        |
| HiveMetaStore_CPU利用率_ProcessCpuLoad             | %        | 进程 CPU 利用率                          |
| HiveMetaStore_CPU利用率_SystemCpuLoad              | %        | 系统 CPU 利用率                          |
| HiveMetaStore_工作线程数_DaemonThreadCount         | 个       | Daemon 线程数                           |
| HiveMetaStore_工作线程数_ThreadCount               | 个       | 总线程数                                |
| HiveMetaStore_CPU累计使用时间_ProcessCpuTime       | ms       | CPU 累计使用时间                         |
| HiveMetaStore_进程运行时长_Uptime                  | s        | 进程运行时长                            |
| HiveMetaStore_GC额外每秒睡眠时间_ExtraSleepTime    | ms       | GC 额外暂停时间每秒                      |
| HiveMetaStore_每秒CPU使用时间_CPURate              | s        | CPU 使用时间占比                         |

### HIVE-HiveServer2

| 指标名称                             | 指标单位 | 指标含义                                                     |
| ------------------------------------ | -------- | ------------------------------------------------------------ |
| GC次数_YGC                           | 次       | Young GC 次数                                                |
| GC次数_FGC                           | 次       | Full GC 次数                                                 |
| GC时间_FGCT                          | s        | Full GC 消耗时间                                             |
| GC时间_GCT                           | s        | 垃圾回收时间消耗                                             |
| GC时间_YGCT                          | s        | Young GC 消耗时间                                            |
| 内存区域占比_S0                      | %        | Survivor 0区内存使用占比                                     |
| 内存区域占比_E                       | %        | Eden 区内存使用占比                                          |
| 内存区域占比_CCS                     | %        | Compressed class space 区内存使用占比                        |
| 内存区域占比_S1                      | %        | Survivor 1区内存使用占比                                     |
| 内存区域占比_O                       | %        | Old 区内存使用占比                                           |
| 内存区域占比_M                       | %        | Metaspace 区内存使用占比                                     |
| JVM内存_MemNonHeapUsedM              | MB       | JVM 当前已使用的 NonHeapMemory 的数量                        |
| JVM内存_MemNonHeapCommittedM         | MB       | JVM 当前已提交的 NonHeapMemory 的数量                        |
| JVM内存_MemHeapUsedM                 | MB       | JVM 当前已使用的 HeapMemory 的数量                           |
| JVM内存_MemHeapCommittedM            | MB       | JVM 当前已提交的 HeapMemory 的数量                           |
| JVM内存_MemHeapMaxM                  | MB       | JVM 配置的 HeapMemory 的数量                                 |
| JVM内存_MemHeapInitM                 | MB       | JVM 初始 HeapMem 的数量                                      |
| JVM内存_MemNonHeapInitM              | MB       | JVM 初始 NonHeapMem 的数量                                   |
| CPU利用率_ProcessCpuLoad             | %        | CPU 利用率                                                   |
| 文件描述符数_MaxFileDescriptorCount  | 个       | 最大文件描述符数                                             |
| 文件描述符数_OpenFileDescriptorCount | 个       | 已打开文件描述符数                                           |
| CPU累计使用时间_ProcessCpuTime       | ms       | CPU 累计使用时间                                             |
| 进程运行时长_Uptime                  | s        | 进程运行时长                                                 |
| 工作线程数_DaemonThreadCount         | 个       | Daemon 线程数                                                |
| 工作线程数_ThreadCount               | 个       | 总线程数                                                     |
| H2_Driver执行时延_99th_percentile    | ms       | Driver 执行99%的时延                                          |
| H2_Driver执行时延_Avg                | ms       | Driver 执行平均执行时延                                       |
| H2_进程打开连接数_NumOpenConnections | 个       | 打开连接数量                                                 |
| H2_异步线程池大小_PoolSize           | 个       | hs2 异步线程池当前大小                                        |
| H2_异步操作队列大小_QueueSize        | 个       | hs2 异步操作队列当前大小                                      |
| H2_GC额外每秒睡眠时间_ExtraSleepTime | ms/s     | GC 额外暂停时间每秒                                           |
| MaxFileDescriptorCount               | 个       | 最大文件描述符数                                             |
| 文件描述符数_OpenFileDescriptorCount | 个       | 已打开文件描述符数                                           |
| H2_完成关闭的操作数量_Closed         | 个/s     | 关闭的操作数量                                               |
| H2_完成的操作数量_Finished           | 个/s     | 完成的操作数量                                               |
| H2_取消的操作数量_Canceled           | 个/s     | 取消的操作数量                                               |
| H2_出错的操作数量_Error              | 个/s     | 出错的操作数量                                               |
| H2_JVM堆内存使用率_MemHeapUsedRate   | %        | JVM 当前已经使用的 HeapMemory 的数量所占 JVM 配置的 HeapMemory 的数量的百分比 |
| H2_每秒CPU使用时间_CPURate           | s        | CPU 使用时间占比                                              |

### HIVE-HiveWebHcat

| 指标名称         | 指标单位 | 指标含义                              |
| ---------------- | -------- | ------------------------------------- |
| GC次数_YGC       | 次       | Young GC 次数                         |
| GC次数_FGC       | 次       | Full GC 次数                          |
| GC时间_FGCT      | s        | Full GC 消耗时间                      |
| GC时间_GCT       | s        | 垃圾回收时间消耗                      |
| GC时间_YGCT      | s        | Young GC 消耗时间                     |
| 内存区域占比_S0  | %        | Survivor 0 区内存使用占比             |
| 内存区域占比_E   | %        | Eden 区内存使用占比                   |
| 内存区域占比_CCS | %        | Compressed class space 区内存使用占比 |
| 内存区域占比_S1  | %        | Survivor 1 区内存使用占比             |
| 内存区域占比_O   | %        | Old 区内存使用占比                    |
| 内存区域占比_M   | %        | Metaspace 区内存使用占比              |

 
