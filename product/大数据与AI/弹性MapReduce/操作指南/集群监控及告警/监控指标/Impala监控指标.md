>!Impala 指标目前仅支持 Impala3.4.0 及以上版本。


### Impala-Catalog

| 指标名称                | 指标单位 | 指标含义                                   |
| ----------------------- | -------- | ------------------------------------------ |
| RSS                     | bytes    | 常驻内存集                                 |
| MemHeapInitM            | MB       | JVM 初始 HeapMemory 的数量峰值             |
| MemHeapCommittedM       | MB       | JVM 当前已经提交的 HeapMemory 的数量       |
| MemHeapMaxM             | MB       | JVM 配置的 HeapMemory 的数量               |
| MemHeapUsedM            | MB       | JVM 当前已经使用的 HeapMemory 的数量       |
| MemNonHeapInitM         | MB       | JVM 初始 NonHeapMemory的数量               |
| MemNonHeapCommittedM    | MB       | JVM 当前已经提交的 NonHeapMemory 的数量    |
| MemNonHeapUsedM         | MB       | JVM 当前已经使用的 NonHeapMemory 的数量    |
| Last                    | s        | 守护进程到 StateStore 的最近心跳间隔       |
| Max                     | s        | 守护进程到 StateStore 的最大心跳间隔       |
| Mean                    | s        | 守护进程到 StateStore 的平均心跳间隔       |
| Min                     | s        | 守护进程到 StateStore 的最小心跳间隔       |
| Stddev                  | s        | 守护进程到 StateStore 的心跳之间的标准偏差 |
| TCMalloc_Used                    | bytes    | 程序使用的字节数                           |
| PageheapFreeBytes       | bytes    | 页堆中空闲映射页的字节数                   |
| PageheapUnmappedBytes   | bytes    | 页堆中空闲、未映射页的字节数               |
| PhysicalBytesReserved   | bytes    | 计算进程使用的物理内存量                   |
| TotalBytesReserved      | bytes    | TCMalloc 保留的系统内存字节数              |
| Thrift_Server_Connections_Used                    | 个       | 活跃连接数                                 |
| Uptime                  | s        | 进程运行时间                               |
| MaxFileDescriptorCount  | 个       | 最大文件描述符数                           |
| OpenFileDescriptorCount | 个       | 已打开文件描述符数                         |
| ThreadCount             | 个       | 总线程数量                                 |
| DaemonThreadCount       | 个       | Daemon 线程数                              |

### Impala-Daemon

| 指标名称                | 指标单位 | 指标含义                                |
| ----------------------- | -------- | --------------------------------------- |
| MemHeapInitM            | MB       | JVM 初始 HeapMemory 的数量峰值          |
| MemHeapCommittedM       | MB       | JVM 当前已经提交的 HeapMemory 的数量    |
| MemHeapMaxM             | MB       | JVM 配置的 HeapMemory 的数量            |
| MemHeapUsedM            | MB       | JVM 当前已经使用的 HeapMemory 的数量    |
| MemNonHeapInitM         | MB       | JVM 初始 NonHeapMemory 的数量           |
| MemNonHeapCommittedM    | MB       | JVM 当前已经提交的 NonHeapMemory 的数量 |
| MemNonHeapUsedM         | MB       | JVM 当前已经使用的 NonHeapMemory 的数量 |
| TCMalloc_Used                    | bytes    | 应用程序使用的字节数                    |
| PageheapFreeBytes       | bytes    | 页堆中空闲映射页的字节数                |
| PageheapUnmappedBytes   | bytes    | 页堆中空闲、未映射页的字节数            |
| PhysicalBytesReserved   | bytes    | 计算进程使用的物理内存量                |
| TotalBytesReserved      | bytes    | TCMalloc 保留的系统内存字节数           |
| ThreadCount             | 个       | 总线程数量                              |
| DaemonThreadCount       | 个       | Daemon 线程数                           |
| Uptime                  | s        | 进程运行时间                            |
| MaxFileDescriptorCount  | 个       | 最大文件描述符数                        |
| OpenFileDescriptorCount | 个       | 已打开文件描述符数                      |


### Impala-StateStore

| 指标名称              | 指标单位 | 指标含义                      |
| --------------------- | -------- | ----------------------------- |
| RSS                   | bytes    | 常驻内存集                    |
| TCMalloc_Used                  | bytes    | 应用程序使用的字节数          |
| PageheapFreeBytes     | bytes    | 页堆中空闲映射页的字节数      |
| PageheapUnmappedBytes | bytes    | 页堆中空闲、未映射页的字节数  |
| PhysicalBytesReserved | bytes    | 计算进程使用的物理内存量      |
| TotalBytesReserved    | bytes    | TCMalloc 保留的系统内存字节数 |
|Thrift_Server_Connections_Used                  | 个       | 活跃连接数                    |
| Running_Threads_Count                 | 个       | 运行线程数                    |
| StateStore_Live_Backends_Count                 | 个       | StateStore 订阅者数量         |

 
