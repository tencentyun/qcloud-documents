### YARN-概览

| 指标名称                     | 指标单位 | 指标含义         |
| :--------------------------- | :------- | ---------------- |
| NumActiveNMs                 | 个       | 节点个数         |
| NumDecommissionedNMs         | 个       | 节点个数         |
| NumLostNMs                   | 个       | 节点个数         |
| NumUnhealthyNMs              | 个       | 节点个数         |
| AllocatedVCores              | 核       | CPU 核数         |
| ReservedVCores               | 核       | CPU 核数         |
| AvailableVCores              | 核       | CPU 核数         |
| PendingVCores                | 核       | CPU 核数         |
| AppsSubmitted                | 个       | 应用总数         |
| AppsRunning                  | 个       | 应用总数         |
| AppsPending                  | 个       | 应用总数         |
| AppsCompleted                | 个       | 应用总数         |
| AppsKilled                   | 个       | 应用总数         |
| AppsFailed                   | 个       | 应用总数         |
| ActiveApplications           | 个       | 应用总数         |
| running_0                    | 个       | 应用总数         |
| running_60                   | 个       | 应用总数         |
| running_300                  | 个       | 应用总数         |
| running_1440                 | 个       | 应用总数         |
| AllocatedMB                  | MB       | 内存大小         |
| AvailableMB                  | MB       | 内存大小         |
| PendingMB                    | MB       | 内存大小         |
| ReservedMB                   | MB       | 内存大小         |
| AllocatedContainers          | 个       | 容器个数         |
| PendingContainers            | 个       | 容器个数         |
| ReservedContainers           | 个       | 容器个数         |
| AggregateContainersAllocated | 个       | 容器分配释放总数 |
| AggregateContainersReleased  | 个       | 容器分配释放总数 |
| ActiveUsers                  | 个       | 用户数           |
| AMLaunchDelayNumOps    | 个   | AM 启动数量           |
| AMLaunchDelayAvgTime   | ms   | RM 启动 AM 的平均时间   |
| AMRegisterDelayNumOps  | 个   | 注册的 AM 总数         |
| AMRegisterDelayAvgTime | ms   | AM 注册到 RM 的平均时间 |


### YARN-ResourceManager

| 指标名称                   | 指标单位 | 指标含义           |
| :------------------------- | :------- | ------------------ |
| RpcAuthenticationFailures  | 个       | RPC 认证授权数     |
| RpcAuthenticationSuccesses | 个       | RPC 认证授权数     |
| RpcAuthorizationFailures   | 个       | RPC 认证授权数     |
| RpcAuthorizationSuccesses  | 个       | RPC 认证授权数     |
| ReceivedBytes              | bytes/s  | RPC 接收发送数据量 |
| SentBytes                  | bytes/s  | RPC 接收发送数据量 |
| NumOpenConnections         | 个       | RPC 连接数         |
| RpcProcessingTimeNumOps    | 次       | RPC 请求次数       |
| RpcQueueTimeNumOps         | 次       | RPC 请求次数       |
| CallQueueLength            | 个       | RPC 队列长度       |
| RpcProcessingTimeAvgTime   | s        | RPC 平均处理时间   |
| RpcQueueTimeAvgTime        | s        | RPC 平均处理时间   |
| RpcAuthenticationFailures  | 个       | RPC 认证授权数     |
| RpcAuthenticationSuccesses | 个       | RPC 认证授权数     |
| RpcAuthorizationFailures   | 个       | RPC 认证授权数     |
| RpcAuthorizationSuccesses  | 个       | RPC 认证授权数     |
| ReceivedBytes              | bytes/s  | RPC 接收发送数据量 |
| SentBytes                  | bytes/s  | RPC 接收发送数据量 |
| NumOpenConnections         | 个       | RPC 连接数         |
| RpcProcessingTimeNumOps    | 次       | RPC 请求次数       |
| RpcQueueTimeNumOps         | 次       | RPC 请求次数       |
| CallQueueLength            | 个       | RPC 队列长度       |
| RpcProcessingTimeAvgTime   | s        | RPC 平均处理时间   |
| RpcQueueTimeAvgTime        | s        | RPC 平均处理时间   |
| RpcAuthenticationFailures  | 个       | RPC 认证授权数     |
| RpcAuthenticationSuccesses | 个       | RPC 认证授权数     |
| RpcAuthorizationFailures   | 个       | RPC 认证授权数     |
| RpcAuthorizationSuccesses  | 个       | RPC 认证授权数     |
| ReceivedBytes              | bytes/s  | RPC 接收发送数据量 |
| SentBytes                  | bytes/s  | RPC 接收发送数据量 |
| NumOpenConnections         | 个       | RPC 连接数         |
| RpcProcessingTimeNumOps    | 次       | RPC 请求次数       |
| RpcQueueTimeNumOps         | 次       | RPC 请求次数       |
| CallQueueLength            | 个       | RPC 队列长度       |
| RpcProcessingTimeAvgTime   | s        | RPC 平均处理时间   |
| RpcQueueTimeAvgTime        | s        | RPC 平均处理时间   |
| RpcAuthenticationFailures  | 个       | RPC 认证授权数     |
| RpcAuthenticationSuccesses | 个       | RPC 认证授权数     |
| RpcAuthorizationFailures   | 个       | RPC 认证授权数     |
| RpcAuthorizationSuccesses  | 个       | RPC 认证授权数     |
| ReceivedBytes              | bytes/s  | RPC 接收发送数据量 |
| SentBytes                  | bytes/s  | RPC 接收发送数据量 |
| NumOpenConnections         | 个       | RPC 连接数         |
| RpcProcessingTimeNumOps    | 次       | RPC 请求次数       |
| RpcQueueTimeNumOps         | 次       | RPC 请求次数       |
| CallQueueLength            | 个       | RPC 队列长度       |
| RpcProcessingTimeAvgTime   | s        | RPC 平均处理时间   |
| RpcQueueTimeAvgTime        | s        | RPC 平均处理时间   |
| YGC                        | 次       | GC 次数            |
| FGC                        | 次       | GC 次数            |
| FGCT                       | s        | GC 时间            |
| GCT                        | s        | GC 时间            |
| YGCT                       | s        | GC 时间            |
| S0                         | %        | 内存区域占比       |
| E                          | %        | 内存区域占比       |
| CCS                        | %        | 内存区域占比       |
| S1                         | %        | 内存区域占比       |
| O                          | %        | 内存区域占比       |
| M                          | %        | 内存区域占比       |
| ThreadsNew                 | 个       | JVM 线程数量       |
| ThreadsRunnable            | 个       | JVM 线程数量       |
| ThreadsBlocked             | 个       | JVM 线程数量       |
| ThreadsWaiting             | 个       | JVM 线程数量       |
| ThreadsTimedWaiting        | 个       | JVM 线程数量       |
| ThreadsTerminated          | 个       | JVM 线程数量       |
| LogFatal                   | 次       | JVM 日志数量       |
| LogError                   | 次       | JVM 日志数量       |
| LogWarn                    | 次       | JVM 日志数量       |
| LogInfo                    | 次       | JVM 日志数量       |
| MemNonHeapUsedM            | MB       | JVM 内存           |
| MemNonHeapCommittedM       | MB       | JVM 内存           |
| MemNonHeapMaxM             | MB       | JVM 内存           |
| MemHeapUsedM               | MB       | JVM 内存           |
| MemHeapCommittedM          | MB       | JVM 内存           |
| MemHeapMaxM                | MB       | JVM 内存           |
| MemMaxM                    | MB       | JVM 内存           |
| ProcessCpuLoad             | %        | CPU 利用率         |
| ProcessCpuTime             | ms       | CPU 累计使用时间   |
| MaxFileDescriptorCount     | 个       | 文件描述符数       |
| OpenFileDescriptorCount    | 个       | 文件描述符数       |
| Uptime                     | s        | 进程运行时长       |
| DaemonThreadCount          | 个       | 工作线程数         |
| ThreadCount                | 个       | 工作线程数         |

### YARN-JobHistoryServer

| 指标名称                           | 指标单位 | 指标含义          |
| :--------------------------------- | :------- | ----------------- |
ThreadsNew                         | 个       | JVM 线程数量       |
| ThreadsRunnable                    | 个       | JVM 线程数量       |
| ThreadsBlocked                     | 个       | JVM 线程数量       |
| ThreadsWaiting                     | 个       | JVM 线程数量       |
| ThreadsTimedWaiting                | 个       | JVM 线程数量       |
| ThreadsTerminated                  | 个       | JVM 线程数量       |
| LogFatal                           | 次       | JVM 日志数量       |
| LogError                           | 次       | JVM 日志数量       |
| LogWarn                            | 次       | JVM 日志数量       |
| LogInfo                            | 次       | JVM 日志数量       |
| MemNonHeapUsedM                    | MB       | JVM 内存           |
| MemNonHeapCommittedM               | MB       | JVM 内存           |
| MemNonHeapMaxM                     | MB       | JVM 内存           |
| MemHeapUsedM                       | MB       | JVM 内存           |
| MemHeapCommittedM                  | MB       | JVM 内存           |
| MemHeapMaxM                        | MB       | JVM 内存           |
| MemMaxM                            | MB       | JVM 内存           |
| YGC                                | 次       | GC 次数            |
| FGC                                | 次       | GC 次数            |
| FGCT                               | s        | GC 时间            |
| GCT                                | s        | GC 时间            |
| YGCT                               | s        | GC 时间            |
| S0                                 | %        | 内存区域占比      |
| E                                  | %        | 内存区域占比      |
| CCS                                | %        | 内存区域占比      |
| S1                                 | %        | 内存区域占比      |
| O                                  | %        | 内存区域占比      |
| M                                  | %        | 内存区域占比      |
| ProcessCpuLoad                     | %        | CPU 利用率         |
| ProcessCpuTime                     | ms       | CPU 累计使用时间   |
| MaxFileDescriptorCount             | 个       | 文件描述符数      |
| OpenFileDescriptorCount            | 个       | 文件描述符数      |
| Uptime                             | s        | 进程运行时长      |
| DaemonThreadCount                  | 个       | 工作线程数        |
| ThreadCount                        | 个       | 工作线程数        |

### YARN-NodeManager

| 指标名称                       | 指标单位 | 指标含义         |
| :----------------------------- | :------- | ---------------- |
| YGC                            | 次       | GC 次数          |
| FGC                            | 次       | GC 次数          |
| FGCT                           | s        | GC 时间          |
| GCT                            | s        | GC 时间          |
| YGCT                           | s        | GC 时间          |
| S0                             | %        | 内存区域占比     |
| E                              | %        | 内存区域占比     |
| CCS                            | %        | 内存区域占比     |
| S1                             | %        | 内存区域占比     |
| O                              | %        | 内存区域占比     |
| M                              | %        | 内存区域占比     |
| ThreadsNew                     | 个       | JVM 线程数量     |
| ThreadsRunnable                | 个       | JVM 线程数量     |
| ThreadsBlocked                 | 个       | JVM 线程数量     |
| ThreadsWaiting                 | 个       | JVM 线程数量     |
| ThreadsTimedWaiting            | 个       | JVM 线程数量     |
| ThreadsTerminated              | 个       | JVM 线程数量     |
| LogFatal                       | 次       | JVM 日志数量     |
| LogError                       | 次       | JVM 日志数量     |
| LogWarn                        | 次       | JVM 日志数量     |
| LogInfo                        | 次       | JVM 日志数量     |
| MemNonHeapUsedM                | MB       | JVM 内存         |
| MemNonHeapCommittedM           | MB       | JVM 内存         |
| MemNonHeapMaxM                 | MB       | JVM 内存         |
| MemHeapUsedM                   | MB       | JVM 内存         |
| MemHeapCommittedM              | MB       | JVM 内存         |
| MemHeapMaxM                    | MB       | JVM 内存         |
| MemMaxM                        | MB       | JVM 内存         |
| ContainersLaunched             | 个       | 容器总数         |
| ContainersCompleted            | 个       | 容器总数         |
| ContainersFailed               | 个       | 容器总数         |
| ContainersKilled               | 个       | 容器总数         |
| ContainersIniting              | 个       | 容器总数         |
| ContainersRunning              | 个       | 容器总数         |
| AllocatedContainers            | 个       | 容器总数         |
| ContainerLaunchDurationAvgTime | ms       | 容器启动平均耗时 |
| ContainerLaunchDurationNumOps  | 个       | 容器启动操作数   |
| AvailableVCores                | 核       | CPU 核数         |
| AllocatedVCores                | 核       | CPU 核数         |
| AllocatedGB                    | GB       | 内存大小         |
| AvailableGB                    | GB       | 内存大小         |
| ProcessCpuLoad                 | %        | CPU 利用率       |
| ProcessCpuTime                 | ms       | CPU 累计使用时间 |
| MaxFileDescriptorCount         | 个       | 文件描述符数     |
| OpenFileDescriptorCount        | 个       | 文件描述符数     |
| Uptime                         | s        | 进程运行时长     |
| DaemonThreadCount              | 个       | 工作线程数       |
| ThreadCount                    | 个       | 工作线程数       |
