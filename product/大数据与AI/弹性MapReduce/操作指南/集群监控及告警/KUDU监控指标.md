| 指标名称                      | 单位  | 指标含义                                                     |
| ----------------------------- | ----- | ------------------------------------------------------------ |
| BlockCacheHit                 | 次    | 预期并命中块的查找数。当确定缓存的效率时，使用此值代替 cache_hits |
| BlockCacheMiss                | 次    | 预期但未命中块的查找数。当确定缓存的效率时，使用此值代替 cache_misses |
| ActiveScanners                | 个    | 当前处于活动状态的 scanner 个数                                |
| ExpiredScanners               | 个    | 自服务启动后由于不活动而过期的 scanner 个数                    |
| OpenClientSessions            | 个    | 此服务器上当前打开的 tablet 复制客户端 session 个数              |
| OpemSourceSessions            | 个    | 此服务器上当前打开的 tablet 复制源 session 个数                  |
| TabletBootstrapping           | 个    | 当前正在 bootstrap 的 tablet 个数                                |
| TabletFailed                  | 个    | 失败的 tablet 个数                                             |
| TabletInitialized             | 个    | 当前初始化过的 tablet 个数                                     |
| TabletNotInitialized          | 个    | 当前未初始化过的 tablet 个数                                   |
| TabletRunning                 | 个    | 当前正在运行的 tablet 个数/当前正在运行的线程数                |
| TabletShutdown                | 个    | 当前关闭的 tablet 个数                                         |
| TabletStopped                 | 个    | 当前停止的 tablet 个数                                         |
| TabletStopping                | 个    | 当前正在停止的 tablet 个数                                     |
| TotalCount                    | 个    | 总操作数                                                     |
| Min                           | 个    | 队列中最小等待任务数/最小运行时间/最小等待时间/最小处理时间  |
| Max                           | 个    | 队列中最大等待任务数/最大运行时间/最大等待时间/最大处理时间  |
| Mean                          | 个    | 队列中平均等待任务数/平均运行时间/平均等待时间/平均处理时间  |
| Percentile_99_9               | 个    | 队列中等待任务数的99.9分位数/运行时间的99.9分位数/等待时间的99.9分位数/处理时间的99.9分位数 |
| BlockCacheUsage               | bytes | 块缓存占用的内存                                             |
| FileCacheHit                  | 次    | 预期并命中文件描述符的查找数。当确定缓存的效率时，使用此值代替 cache_hits |
| FileCacheMiss                 | 次    | 预期但未命中文件描述符的查找数。当确定缓存的效率时，使用此值代替 cache_misses |
| FileCacheUsage                | 个    | 文件缓存中的条目数                                           |
| BlockUnderManagement          | 个    | 当前管理的数据块数                                           |
| BlockOpenReading              | 个    | 当前打开供读取的数据块数                                     |
| BlockOpenWriting              | 个    | 当前打开进行写入的数据块数                                   |
| BytesUnderManagement          | bytes | 当前管理的数据块字节数                                       |
| ContainersUnderManagement     | 个    | 日志块容器数                                                 |
| FullContainersUnderManagement | 个    | 完整日志块容器数                                             |
| CpuStime                      | 毫秒  | 进程的总系统 CPU 时间                                          |
| CpuUtime                      | 毫秒  | 进程的用户 CPU 总时间                                          |
| DataDirsFailed                | 个    | 磁盘当前处于故障状态的数据目录数                             |
| DataDirsFull                  | 个    | 磁盘当前已满的数据目录数                                     |
| AllocatedBytes                | 个    | 应用程序使用的字节数。这通常与操作系统报告的内存使用情况不匹配，因为它不包括 TCMalloc 开销或内存碎片 |
| ErrorMessages                 | 个    | 应用程序发出的 ERROR 级日志消息数                              |
| WarningMessages               | 个    | 应用程序发出的 WARNING 级日志消息数                            |
| InvoluntarySwitches           | 次    | 非自发的上下文切换                                           |
| VoluntarySwitches              | 次    | 自发的上下文切换                                             |
| SpinlockContentionTime        | 微秒  | 自服务器启动后，内部自旋锁上的争用所消耗的时间量             |
| OversizedWriteRequests        | 个    | 启动后拒绝的对 system catalog tablet 的过大写请求数           |
| HybridClockError              | 微秒  | 服务器时钟最大错误；无法读取基础时钟时返回2^64-1             |
| HybridClockTimestamp          | 微秒  | 混合时钟时间戳；无法读取基础时钟时返回2^64-1                 |
| ClusterReplicaSkew            | 个    | 承载最多副本的 tablet 服务器上的副本数与承载最少副本的 tablet 服务器上的副本数之间的差异 |
| NumRaftLeaders                | 个    | Raft leaders 的 tablet 副本数量                                 |
| HeapSize                      | bytes | TCMalloc 保留的系统内存字节                                   |
| CurrentThreadCacheBytes       | bytes | TCMalloc 正在使用的内存的度量（对于小对象）                   |
| TotalThreadCacheBytes         | bytes | TCMalloc 用于小对象的内存限制                                 |
| FreeBytes                     | bytes | 页堆中可用的映射页的字节数                                   |
| UnMappedBytes                 | bytes | 页堆中空闲的未映射页的字节数                                 |
| ConnectionsAccepted           | 个    | 到 RPC 服务器的连入 TCP 连接数                                   |
| QueueOverflow                  | 个    | 由于服务队列已满而丢弃的 RPC 数                                |
| TimesOutInQueue               | 个    | 在服务队列中等待时超时并因此未被处理的 RPC 数                  |
| ThreadsRunning                | 个    | 所有 tablet server 中当前正在运行的线程数/所有 master 中当前正在运行的线程数 |

