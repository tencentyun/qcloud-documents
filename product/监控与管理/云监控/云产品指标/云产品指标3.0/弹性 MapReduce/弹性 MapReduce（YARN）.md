## 命名空间

Namespace=QCE/TXMR_YARN

## 监控指标

### Yarn-Overview

| 指标英文名                                    | 指标中文名                    | 指标单位 | 指标含义 | 维度                                    |
| --------------------------------------------- | ----------------------------- | -------- | -------- | --------------------------------------- |
| EmrYarnOverviewYarnRmNumsNumactivenms         | 节点个数_NumActiveNMs         | 个       | 节点个数 | host4yarnoverview、<br>id4yarnoverview  |
| EmrYarnOverviewYarnRmNumsNumdecommissionednms | 节点个数_NumDecommissionedNMs | 个       | 节点个数 | host4yarnoverview、<br/>id4yarnoverview |
| EmrYarnOverviewYarnRmNumsNumlostnms           | 节点个数_NumLostNMs           | 个       | 节点个数 | host4yarnoverview、<br/>id4yarnoverview |
| EmrYarnOverviewYarnRmNumsNumunhealthynms      | 节点个数_NumUnhealthyNMs      | 个       | 节点个数 | host4yarnoverview、<br/>id4yarnoverview |

### Yarn-OverviewAggregation

| 指标英文名                                               | 指标中文名                    | 指标单位 | 指标含义 | 维度            |
| -------------------------------------------------------- | ----------------------------- | -------- | -------- | --------------- |
| EmrYarnOverviewAggregationYarnRmNumsNumactivenms         | 节点个数_NumActiveNMs         | 个       | 节点个数 | id4yarnoverview |
| EmrYarnOverviewAggregationYarnRmNumsNumdecommissionednms | 节点个数_NumDecommissionedNMs | 个       | 节点个数 | id4yarnoverview |
| EmrYarnOverviewAggregationYarnRmNumsNumlostnms           | 节点个数_NumLostNMs           | 个       | 节点个数 | id4yarnoverview |
| EmrYarnOverviewAggregationYarnRmNumsNumunhealthynms      | 节点个数_NumUnhealthyNMs      | 个       | 节点个数 | id4yarnoverview |

### YARN-Cluster

| 指标英文名                                 | 指标中文名                     | 指标单位 | 指标含义         | 维度                                    |
| ------------------------------------------ | ------------------------------ | -------- | ---------------- | --------------------------------------- |
| YarnClusterResAppFailed                    | Applications_failed            | 个       | 应用总数         | host4yarnoverview、<br>id4yarnoverview  |
| YarnClusterResAppKilled                    | Applications_killed            | 个       | 应用总数         | host4yarnoverview、<br/>id4yarnoverview |
| YarnClusterResAppPending                   | Applications_pending           | 个       | 应用总数         | host4yarnoverview、<br/>id4yarnoverview |
| YarnClusterResAppRunning                   | Applications_running           | 个       | 应用总数         | host4yarnoverview、<br/>id4yarnoverview |
| YarnClusterResAppSubmitted                 | Applications_submitted         | 个       | 应用总数         | host4yarnoverview、<br/>id4yarnoverview |
| YarnClusterResContainerContainersallocated | Containers_containersAllocated | 个       | 容器分配释放总数 | host4yarnoverview、<br/>id4yarnoverview |
| YarnClusterResContainerContainerspending   | Containers_containersPending   | 个       | 容器分配释放总数 | host4yarnoverview、<br/>id4yarnoverview |
| YarnClusterResContainerContainersreserved  | Containers_containersReserved  | 个       | 容器分配释放总数 | host4yarnoverview、<br/>id4yarnoverview |
| YarnClusterResCpuAllocatedvirtualcores     | Cores_allocatedVirtualCores    | 个       | CPU 核数         | host4yarnoverview、<br/>id4yarnoverview |
| YarnClusterResCpuAvailablevirtualcores     | Cores_availableVirtualCores    | 个       | CPU 核数         | host4yarnoverview、<br/>id4yarnoverview |
| YarnClusterResCpuReservedvirtualcores      | Cores_reservedVirtualCores     | 个       | CPU 核数         | host4yarnoverview、<br/>id4yarnoverview |
| YarnClusterResCpuTotalvirtualcores         | Cores_totalVirtualCores        | 个       | CPU 核数         | host4yarnoverview、<br/>id4yarnoverview |
| YarnClusterResCpuUsageRatioUsageratio      | CPU使用率_usageRatio           | %        | 内存大小         | host4yarnoverview、<br/>id4yarnoverview |
| YarnClusterResMemAllocatedmb               | Memory_allocatedMB             | MB       | 内存大小         | host4yarnoverview、<br/>id4yarnoverview |
| YarnClusterResMemAvailablemb               | Memory_availableMB             | MB       | 内存大小         | host4yarnoverview、<br/>id4yarnoverview |
| YarnClusterResMemReservedmb                | Memory_reservedMB              | MB       | 内存大小         | host4yarnoverview、<br/>id4yarnoverview |
| YarnClusterResMemTotalmb                   | Memory_totalMB                 | MB       | 内存大小         | host4yarnoverview、<br/>id4yarnoverview |
| YarnClusterResMemUsageRatioUsageratio      | 内存使用率_usageRatio          | %        | 内存大小         | host4yarnoverview、<br/>id4yarnoverview |



### YARN-ResourceManager

| 指标英文名                                  | 指标中文名                               | 指标单位 | 指标含义           | 维度                                                  |
| ------------------------------------------- | ---------------------------------------- | -------- | ------------------ | ----------------------------------------------------- |
| YarnRmRpcAuth5000Rpcauthenticationfailures  | RPC认证授权数_RpcAuthenticationFailures  | 个       | RPC 认证授权数     | host4yarnresourcemanager、<br>id4yarnresourcemanager  |
| YarnRmRpcAuth5000Rpcauthenticationsuccesses | RPC认证授权数_RpcAuthorizationSuccesses  | 个       | RPC 认证授权数     | host4yarnresourcemanager、<br/>id4yarnresourcemanager |
| YarnRmRpcAuth5000Rpcauthorizationfailures   | RPC认证授权数_RpcAuthorizationFailures   | 个       | RPC 认证授权数     | host4yarnresourcemanager、<br/>id4yarnresourcemanager |
| YarnRmRpcAuth5000Rpcauthorizationsuccesses  | RPC认证授权数_RpcAuthenticationSuccesses | 个       | RPC 认证授权数     | host4yarnresourcemanager、<br/>id4yarnresourcemanager |
| YarnRmRpcBytes5000Receivedbytes             | RPC接收发送数据量_ReceivedBytes          | bytes/s  | RPC 接收发送数据量 | host4yarnresourcemanager、<br/>id4yarnresourcemanager |
| YarnRmRpcBytes5000Sentbytes                 | RPC接收发送数据量_SentBytes              | bytes/s  | RPC 接收发送数据量 | host4yarnresourcemanager、<br/>id4yarnresourcemanager |
| YarnRmRpcConnections5000Numopenconnections  | RPC连接数_NumOpenConnections             | 个       | RPC 连接数         | host4yarnresourcemanager、<br/>id4yarnresourcemanager |
| YarnRmRpcOps5000Rpcprocessingtimenumops     | RPC请求次数_RpcProcessingTimeNumOps      | 次       | RPC 请求次数       | host4yarnresourcemanager、<br/>id4yarnresourcemanager |
| YarnRmRpcOps5000Rpcqueuetimenumops          | RPC请求次数_RpcQueueTimeNumOps           | 次       | RPC 请求次数       | host4yarnresourcemanager、<br/>id4yarnresourcemanager |
| YarnRmRpcQueueLen5000Callqueuelength        | RPC队列长度_CallQueueLength              | 个       | RPC 队列长度       | host4yarnresourcemanager、<br/>id4yarnresourcemanager |
| YarnRmRpcTime5000Rpcprocessingtimeavgtime   | RPC平均处理时间_RpcProcessingTimeAvgTime | s        | RPC 平均处理时间   | host4yarnresourcemanager、<br/>id4yarnresourcemanager |
| YarnRmRpcTime5000Rpcqueuetimeavgtime        | RPC平均处理时间_RpcQueueTimeAvgTime      | s        | RPC 平均处理时间   | host4yarnresourcemanager、<br/>id4yarnresourcemanager |
| YarnRmRpcAuth5000Rpcauthenticationfailures  | RPC认证授权数_RpcAuthenticationFailures  | 个       | RPC 认证授权数     | host4yarnresourcemanager、<br/>id4yarnresourcemanager |
| YarnRmRpcAuth5000Rpcauthenticationsuccesses | RPC认证授权数_RpcAuthenticationSuccesses | 个       | RPC 认证授权数     | host4yarnresourcemanager、<br/>id4yarnresourcemanager |
| YarnRmRpcAuth5000Rpcauthorizationfailures   | RPC认证授权数_RpcAuthorizationFailures   | 个       | RPC 认证授权数     | host4yarnresourcemanager、<br/>id4yarnresourcemanager |
| YarnRmRpcAuth5000Rpcauthorizationsuccesses  | RPC认证授权数_RpcAuthorizationSuccesses  | 个       | RPC 认证授权数     | host4yarnresourcemanager、<br/>id4yarnresourcemanager |
| YarnRmRpcBytes5000Receivedbytes             | RPC接收发送数据量_ReceivedBytes          | bytes/s  | RPC 接收发送数据量 | host4yarnresourcemanager、<br/>id4yarnresourcemanager |
| YarnRmRpcBytes5000Sentbytes                 | RPC接收发送数据量_SentBytes              | bytes/s  | RPC 接收发送数据量 | host4yarnresourcemanager、<br/>id4yarnresourcemanager |
| YarnRmRpcConnections5000Numopenconnections  | RPC连接数_NumOpenConnections             | 个       | RPC 连接数         | host4yarnresourcemanager、<br/>id4yarnresourcemanager |
| YarnRmRpcOps5000Rpcprocessingtimenumops     | RPC请求次数_RpcProcessingTimeNumOps      | 次       | RPC 请求次数       | host4yarnresourcemanager、<br/>id4yarnresourcemanager |
| YarnRmRpcOps5000Rpcqueuetimenumops          | RPC请求次数_RpcQueueTimeNumOps           | 次       | RPC 请求次数       | host4yarnresourcemanager、<br/>id4yarnresourcemanager |
| YarnRmRpcQueueLen5000Callqueuelength        | RPC队列长度_CallQueueLength              | 个       | RPC 队列长度       | host4yarnresourcemanager、<br/>id4yarnresourcemanager |
| YarnRmRpcTime5000Rpcprocessingtimeavgtime   | RPC平均处理时间_RpcProcessingTimeAvgTime | s        | RPC 平均处理时间   | host4yarnresourcemanager、<br/>id4yarnresourcemanager |
| YarnRmRpcTime5000Rpcqueuetimeavgtime        | RPC平均处理时间_RpcQueueTimeAvgTime      | s        | RPC 平均处理时间   | host4yarnresourcemanager、<br/>id4yarnresourcemanager |
| YarnRmRpcAuth5000Rpcauthenticationfailures  | RPC认证授权数_RpcAuthenticationFailures  | 个       | RPC 认证授权数     | host4yarnresourcemanager、<br/>id4yarnresourcemanager |
| YarnRmRpcAuth5000Rpcauthenticationsuccesses | RPC认证授权数_RpcAuthenticationSuccesses | 个       | RPC 认证授权数     | host4yarnresourcemanager、<br/>id4yarnresourcemanager |
| YarnRmRpcAuth5000Rpcauthorizationfailures   | RPC认证授权数_RpcAuthorizationFailures   | 个       | RPC 认证授权数     | host4yarnresourcemanager、<br/>id4yarnresourcemanager |
| YarnRmRpcAuth5000Rpcauthorizationsuccesses  | RPC认证授权数_RpcAuthorizationSuccesses  | 个       | RPC 认证授权数     | host4yarnresourcemanager、<br/>id4yarnresourcemanager |
| YarnRmRpcBytes5000Receivedbytes             | RPC接收发送数据量_ReceivedBytes          | bytes/s  | RPC 接收发送数据量 | host4yarnresourcemanager<br/>id4yarnresourcemanager   |
| YarnRmRpcBytes5000Sentbytes                 | RPC接收发送数据量_SentBytes              | bytes/s  | RPC 接收发送数据量 | host4yarnresourcemanager<br/>id4yarnresourcemanager   |
| YarnRmRpcConnections5000Numopenconnections  | RPC连接数_NumOpenConnections             | 个       | RPC 连接数         | host4yarnresourcemanager<br/>id4yarnresourcemanager   |
| YarnRmRpcOps5000Rpcprocessingtimenumops     | RPC请求次数_RpcProcessingTimeNumOps      | 次       | RPC 请求次数       | host4yarnresourcemanager<br/>id4yarnresourcemanager   |
| YarnRmRpcOps5000Rpcqueuetimenumops          | RPC请求次数_RpcQueueTimeNumOps           | 次       | RPC 请求次数       | host4yarnresourcemanager<br/>id4yarnresourcemanager   |
| YarnRmRpcQueueLen5000Callqueuelength        | RPC队列长度_CallQueueLength              | 个       | RPC 队列长度       | host4yarnresourcemanager<br/>id4yarnresourcemanager   |
| YarnRmRpcTime5000Rpcprocessingtimeavgtime   | RPC平均处理时间_RpcProcessingTimeAvgTime | s        | RPC 平均处理时间   | host4yarnresourcemanager<br/>id4yarnresourcemanager   |
| YarnRmRpcTime5000Rpcqueuetimeavgtime        | RPC平均处理时间_RpcQueueTimeAvgTime      | s        | RPC 平均处理时间   | host4yarnresourcemanager<br/>id4yarnresourcemanager   |
| YarnRmRpcAuth5000Rpcauthenticationfailures  | RPC认证授权数_RpcAuthenticationFailures  | 个       | RPC 认证授权数     | host4yarnresourcemanager<br/>id4yarnresourcemanager   |
| YarnRmRpcAuth5000Rpcauthenticationsuccesses | RPC认证授权数_RpcAuthenticationSuccesses | 个       | RPC 认证授权数     | host4yarnresourcemanager<br/>id4yarnresourcemanager   |
| YarnRmRpcAuth500Rpcauthorizationfailures    | RPC认证授权数_RpcAuthorizationFailures   | 个       | RPC 认证授权数     | host4yarnresourcemanager<br/>id4yarnresourcemanager   |
| YarnRmRpcAuth5000Rpcauthorizationsuccesses  | RPC认证授权数_RpcAuthorizationSuccesses  | 个       | RPC 认证授权数     | host4yarnresourcemanager<br/>id4yarnresourcemanager   |
| YarnRmRpcBytes5000Receivedbytes             | RPC接收发送数据量_ReceivedBytes          | bytes/s  | RPC 接收发送数据量 | host4yarnresourcemanager<br/>id4yarnresourcemanager   |
| YarnRmRpcBytes5000Sentbytes                 | RPC接收发送数据量_SentBytes              | bytes/s  | RPC 接收发送数据量 | host4yarnresourcemanager<br/>id4yarnresourcemanager   |
| YarnRmRpcConnections5000Numopenconnections  | RPC连接数_NumOpenConnections             | 个       | RPC 连接数         | host4yarnresourcemanager<br/>id4yarnresourcemanager   |
| YarnRmRpcOps5000Rpcprocessingtimenumops     | RPC请求次数_RpcProcessingTimeNumOps      | 次       | RPC 请求次数       | host4yarnresourcemanager<br/>id4yarnresourcemanager   |
| YarnRmRpcOps5000Rpcqueuetimenumops          | RPC请求次数_RpcQueueTimeNumOps           | 次       | RPC 请求次数       | host4yarnresourcemanager<br/>id4yarnresourcemanager   |
| YarnRmRpcQueueLen5000Callqueuelength        | RPC队列长度_CallQueueLength              | 个       | RPC 队列长度       | host4yarnresourcemanager<br/>id4yarnresourcemanager   |
| YarnRmRpcTime5000Rpcprocessingtimeavgtime   | RPC平均处理时间_RpcProcessingTimeAvgTime | s        | RPC 平均处理时间   | host4yarnresourcemanager<br/>id4yarnresourcemanager   |
| YarnRmRpcTime5000Rpcqueuetimeavgtime        | RPC平均处理时间_RpcQueueTimeAvgTime      | s        | RPC 平均处理时间   | host4yarnresourcemanager<br/>id4yarnresourcemanager   |
| YarnRmGcUtilGcCountYgc                      | GC次数_YGC                               | 次       | GC 次数            | host4yarnresourcemanager<br/>id4yarnresourcemanager   |
| YarnRmGcUtilGcCountFgc                      | GC时间_FGC                               | 次       | GC 次数            | host4yarnresourcemanager<br/>id4yarnresourcemanager   |
| YarnRmGcUtilGcTimeFgct                      | GC时间_FGCT                              | s        | GC 时间            | host4yarnresourcemanager<br/>id4yarnresourcemanager   |
| YarnRmGcUtilGcTimeGct                       | GC时间_GCT                               | s        | GC 时间            | host4yarnresourcemanager<br/>id4yarnresourcemanager   |
| YarnRmGcUtilGcTimeYgct                      | GC时间_YGCT                              | s        | GC 时间            | host4yarnresourcemanager<br/>id4yarnresourcemanager   |
| YarnRmGcUtilMemoryS0                        | 内存区域占比_S0                          | %        | 内存区域占比       | host4yarnresourcemanager<br/>id4yarnresourcemanager   |
| YarnRmGcUtilMemoryE                         | 内存区域占比_E                           | %        | 内存区域占比       | host4yarnresourcemanager<br/>id4yarnresourcemanager   |
| YarnRmGcUtilMemoryCcs                       | 内存区域占比_CCS                         | %        | 内存区域占比       | host4yarnresourcemanager<br/>id4yarnresourcemanager   |
| YarnRmGcUtilMemoryS1                        | 内存区域占比_S1                          | %        | 内存区域占比       | host4yarnresourcemanager<br/>id4yarnresourcemanager   |
| YarnRmGcUtilMemoryO                         | 内存区域占比_O                           | %        | 内存区域占比       | host4yarnresourcemanager<br/>id4yarnresourcemanager   |
| YarnRmGcUtilMemoryM                         | 内存区域占比_M                           | %        | 内存区域占比       | host4yarnresourcemanager<br/>id4yarnresourcemanager   |
| YarnRmJvmJavaThreadsThreadsnew              | JVM线程数量_ThreadsNew                   | 个       | JVM 线程数量       | host4yarnresourcemanager<br/>id4yarnresourcemanager   |
| YarnRmJvmJavaThreadsThreadsrunnable         | JVM线程数量_ThreadsRunnable              | 个       | JVM 线程数量       | host4yarnresourcemanager<br/>id4yarnresourcemanager   |
| YarnRmJvmJavaThreadsThreadsblocked          | JVM线程数量_ThreadsBlocked               | 个       | JVM 线程数量       | host4yarnresourcemanager<br/>id4yarnresourcemanager   |
| YarnRmJvmJavaThreadsThreadswaiting          | JVM线程数量_ThreadsWaiting               | 个       | JVM 线程数量       | host4yarnresourcemanager<br/>id4yarnresourcemanager   |
| YarnRmJvmJavaThreadsThreadstimedwaiting     | JVM线程数量_ThreadsTimedWaiting          | 个       | JVM 线程数量       | host4yarnresourcemanager<br/>id4yarnresourcemanager   |
| YarnRmJvmJavaThreadsThreadsterminated       | JVM线程数量_ThreadsTerminated            | 个       | JVM 线程数量       | host4yarnresourcemanager<br/>id4yarnresourcemanager   |
| YarnRmJvmLogTotalLogfatal                   | JVM日志数量_LogFatal                     | 次       | JVM 日志数量       | host4yarnresourcemanager<br/>id4yarnresourcemanager   |
| YarnRmJvmLogTotalLogerror                   | JVM日志数量_LogError                     | 次       | JVM 日志数量       | host4yarnresourcemanager<br/>id4yarnresourcemanager   |
| YarnRmJvmLogTotalLogwarn                    | JVM日志数量_LogWarn                      | 次       | JVM 日志数量       | host4yarnresourcemanager<br/>id4yarnresourcemanager   |
| YarnRmJvmLogTotalLoginfo                    | JVM日志数量_LogInfo                      | 次       | JVM 日志数量       | host4yarnresourcemanager<br/>id4yarnresourcemanager   |
| YarnRmJvmMemMemnonheapusedm                 | JVM内存_MemNonHeapUsedM                  | MB       | JVM 内存           | host4yarnresourcemanager<br/>id4yarnresourcemanager   |
| YarnRmJvmMemMemnonheapcommittedm            | JVM内存_MemNonHeapCommittedM             | MB       | JVM 内存           | host4yarnresourcemanager<br/>id4yarnresourcemanager   |
| YarnRmJvmMemMemheapusedm                    | JVM内存_MemHeapUsedM                     | MB       | JVM 内存           | host4yarnresourcemanager<br/>id4yarnresourcemanager   |
| YarnRmJvmMemMemheapcommittedm               | JVM内存_MemHeapCommittedM                | MB       | JVM 内存           | host4yarnresourcemanager<br/>id4yarnresourcemanager   |
| YarnRmJvmMemMemheapmaxm                     | JVM内存_MemHeapMaxM                      | MB       | JVM 内存           | host4yarnresourcemanager<br/>id4yarnresourcemanager   |
| YarnRmJvmMemMemmaxm                         | JVM内存_MemMaxM                          | MB       | JVM 内存           | host4yarnresourcemanager<br/>id4yarnresourcemanager   |
| YarnRmOsCpuLoadProcesscpuload               | CPU利用率_ProcessCpuLoad                 | %        | CPU 利用率         | host4yarnresourcemanager<br/>id4yarnresourcemanager   |
| YarnRmOsCpuTimeProcesscputime               | CPU累计使用时间_ProcessCpuTime           | ms       | CPU 累计使用时间   | host4yarnresourcemanager<br/>id4yarnresourcemanager   |
| YarnRmOsFdCountMaxfiledescriptorcount       | 文件描述符数_MaxFileDescriptorCount      | 个       | 文件描述符数       | host4yarnresourcemanager<br/>id4yarnresourcemanager   |
| YarnRmOsFdCountOpenfiledescriptorcount      | 文件描述符数_OpenFileDescriptorCount     | 个       | 文件描述符数       | host4yarnresourcemanager<br/>id4yarnresourcemanager   |
| YarnRmRtUptimeUptime                        | 进程运行时长_Uptime                      | s        | 进程运行时长       | host4yarnresourcemanager<br/>id4yarnresourcemanager   |
| YarnRmThreadCountDaemonthreadcount          | 工作线程数_DaemonThreadCount             | 个       | 工作线程数         | host4yarnresourcemanager<br/>id4yarnresourcemanager   |
| YarnRmThreadCountThreadcount                | 工作线程数_ThreadCount                   | 个       | 工作线程数         | host4yarnresourcemanager<br/>id4yarnresourcemanager   |




### YARN-JobHistoryServer

| 指标英文名                              | 指标中文名                           | 指标单位 | 指标含义         | 维度                                                    |
| --------------------------------------- | ------------------------------------ | -------- | ---------------- | ------------------------------------------------------- |
| YarnJhJvmJavaThreadsThreadsnew          | JVM线程数量_ThreadsNew               | 个       | JVM 线程数量     | host4yarnjobhistoryserver、<br>id4yarnjobhistoryserver  |
| YarnJhJvmJavaThreadsThreadsrunnable     | JVM线程数量_ThreadsRunnable          | 个       | JVM 线程数量     | host4yarnjobhistoryserver、<br/>id4yarnjobhistoryserver |
| YarnJhJvmJavaThreadsThreadsblocked      | JVM线程数量_ThreadsBlocked           | 个       | JVM 线程数量     | host4yarnjobhistoryserver、<br/>id4yarnjobhistoryserver |
| YarnJhJvmJavaThreadsThreadswaiting      | JVM线程数量_ThreadsWaiting           | 个       | JVM 线程数量     | host4yarnjobhistoryserver、<br/>id4yarnjobhistoryserver |
| YarnJhJvmJavaThreadsThreadstimedwaiting | JVM线程数量_ThreadsTimedWaiting      | 个       | JVM 线程数量     | host4yarnjobhistoryserver、<br/>id4yarnjobhistoryserver |
| YarnJhJvmJavaThreadsThreadsterminated   | JVM线程数量_ThreadsTerminated        | 个       | JVM 线程数量     | host4yarnjobhistoryserver、<br/>id4yarnjobhistoryserver |
| YarnJhJvmLogTotalLogfatal               | JVM日志数量_LogFatal                 | 次       | JVM 日志数量     | host4yarnjobhistoryserver、<br/>id4yarnjobhistoryserver |
| YarnJhJvmLogTotalLogerror               | JVM日志数量_LogError                 | 次       | JVM 日志数量     | host4yarnjobhistoryserver、<br/>id4yarnjobhistoryserver |
| YarnJhJvmLogTotalLogwarn                | JVM日志数量_LogWarn                  | 次       | JVM 日志数量     | host4yarnjobhistoryserver、<br/>id4yarnjobhistoryserver |
| YarnJhJvmLogTotalLoginfo                | JVM日志数量_LogInfo                  | 次       | JVM 日志数量     | host4yarnjobhistoryserver、<br/>id4yarnjobhistoryserver |
| YarnJhJvmMemMemnonheapusedm             | JVM内存_MemNonHeapUsedM              | MB       | JVM 内存         | host4yarnjobhistoryserver、<br/>id4yarnjobhistoryserver |
| YarnJhJvmMemMemnonheapcommittedm        | JVM内存_MemNonHeapCommittedM         | MB       | JVM 内存         | host4yarnjobhistoryserver、<br/>id4yarnjobhistoryserver |
| YarnJhJvmMemMemheapusedm                | JVM内存_MemHeapUsedM                 | MB       | JVM 内存         | host4yarnjobhistoryserver、<br/>id4yarnjobhistoryserver |
| YarnJhJvmMemMemheapcommittedm           | JVM内存_MemHeapCommittedM            | MB       | JVM 内存         | host4yarnjobhistoryserver、<br/>id4yarnjobhistoryserver |
| YarnJhJvmMemMemheapmaxm                 | JVM内存_MemHeapMaxM                  | MB       | JVM 内存         | host4yarnjobhistoryserver、<br/>id4yarnjobhistoryserver |
| YarnJhJvmMemMemmaxm                     | JVM内存_MemMaxM                      | MB       | JVM 内存         | host4yarnjobhistoryserver、<br/>id4yarnjobhistoryserver |
| YarnJhsGcUtilGcCountYgc                 | GC次数_YGC                           | 次       | GC 次数          | host4yarnjobhistoryserver、<br/>id4yarnjobhistoryserver |
| YarnJhsGcUtilGcCountFgc                 | GC次数_FGC                           | 次       | GC 次数          | host4yarnjobhistoryserver、<br/>id4yarnjobhistoryserver |
| YarnJhsGcUtilGcTimeFgct                 | GC时间_FGCT                          | s        | GC 时间          | host4yarnjobhistoryserver、<br/>id4yarnjobhistoryserver |
| YarnJhsGcUtilGcTimeGct                  | GC时间_GCT                           | s        | GC 时间          | host4yarnjobhistoryserver、<br/>id4yarnjobhistoryserver |
| YarnJhsGcUtilGcTimeYgct                 | GC时间_YGCT                          | s        | GC 时间          | host4yarnjobhistoryserver、<br/>id4yarnjobhistoryserver |
| YarnJhsGcUtilMemoryS0                   | 内存区域占比_S0                      | %        | 内存区域占比     | host4yarnjobhistoryserver、<br/>id4yarnjobhistoryserver |
| YarnJhsGcUtilMemoryE                    | 内存区域占比_E                       | %        | 内存区域占比     | host4yarnjobhistoryserver、<br/>id4yarnjobhistoryserver |
| YarnJhsGcUtilMemoryCcs                  | 内存区域占比_CCS                     | %        | 内存区域占比     | host4yarnjobhistoryserver、<br/>id4yarnjobhistoryserver |
| YarnJhsGcUtilMemoryS1                   | 内存区域占比_S1                      | %        | 内存区域占比     | host4yarnjobhistoryserver、<br/>id4yarnjobhistoryserver |
| YarnJhsGcUtilMemoryO                    | 内存区域占比_O                       | %        | 内存区域占比     | host4yarnjobhistoryserver、<br/>id4yarnjobhistoryserver |
| YarnJhsGcUtilMemoryM                    | 内存区域占比_M                       | %        | 内存区域占比     | host4yarnjobhistoryserver、<br/>id4yarnjobhistoryserver |
| YarnJhOsCpuLoadProcesscpuload           | CPU 利用率_ProcessCpuLoad            | %        | CPU 利用率       | host4yarnjobhistoryserver、<br/>id4yarnjobhistoryserver |
| YarnJhOsCpuTimeProcesscputime           | CPU 累计使用时间_ProcessCpuTime      | ms       | CPU 累计使用时间 | host4yarnjobhistoryserver、<br/>id4yarnjobhistoryserver |
| YarnJhOsFdCountMaxfiledescriptorcount   | 文件描述符数_MaxFileDescriptorCount  | 个       | 文件描述符数     | host4yarnjobhistoryserver、<br/>id4yarnjobhistoryserver |
| YarnJhOsFdCountOpenfiledescriptorcount  | 文件描述符数_OpenFileDescriptorCount | 个       | 文件描述符数     | host4yarnjobhistoryserver、<br/>id4yarnjobhistoryserver |
| YarnJhRtUptimeUptime                    | 进程运行时长_Uptime                  | s        | 进程运行时长     | host4yarnjobhistoryserver、<br/>id4yarnjobhistoryserver |
| YarnJhThreadCountDaemonthreadcount      | 工作线程数_DaemonThreadCount         | 个       | 工作线程数       | host4yarnjobhistoryserver、<br/>id4yarnjobhistoryserver |
| YarnJhThreadCountThreadcount            | 工作线程数_ThreadCount               | 个       | 工作线程数       | host4yarnjobhistoryserver、<br/>id4yarnjobhistoryserver |

### YARN-NodeManager

| 指标英文名                              | 指标中文名                           | 指标单位 | 指标含义         | 维度                                           |
| --------------------------------------- | ------------------------------------ | -------- | ---------------- | ---------------------------------------------- |
| YarnNmGcUtilGcCountYgc                  | GC次数_YGC                           | 次       | GC 次数          | id4yarnnodemanager、<br>host4yarnnodemanager   |
| YarnNmGcUtilGcCountFgc                  | GC次数_FGC                           | 次       | GC 次数          | id4yarnnodemanager、<br/>host4yarnnodemanager  |
| YarnNmGcUtilGcTimeFgct                  | GC时间_FGCT                          | s        | GC 时间          | id4yarnnodemanager、<br/>host4yarnnodemanager  |
| YarnNmGcUtilGcTimeGct                   | GC时间_GCT                           | s        | GC 时间          | id4yarnnodemanager、<br/>host4yarnnodemanager  |
| YarnNmGcUtilGcTimeYgct                  | GC时间_YGCT                          | s        | GC 时间          | id4yarnnodemanager、<br/>host4yarnnodemanager  |
| YarnNmGcUtilMemoryS0                    | 内存区域占比_S0                      | %        | 内存区域占比     | id4yarnnodemanager、<br/>host4yarnnodemanager  |
| YarnNmGcUtilMemoryE                     | 内存区域占比_E                       | %        | 内存区域占比     | id4yarnnodemanager、<br/>host4yarnnodemanager  |
| YarnNmGcUtilMemoryCcs                   | 内存区域占比_CCS                     | %        | 内存区域占比     | id4yarnnodemanager、<br/>host4yarnnodemanager  |
| YarnNmGcUtilMemoryS1                    | 内存区域占比_S1                      | %        | 内存区域占比     | id4yarnnodemanager、<br/>host4yarnnodemanager  |
| YarnNmGcUtilMemoryO                     | 内存区域占比_O                       | %        | 内存区域占比     | id4yarnnodemanager、<br>host4yarnnodemanager   |
| YarnNmGcUtilMemoryM                     | 内存区域占比_M                       | %        | 内存区域占比     | id4yarnnodemanager、<br>host4yarnnodemanager   |
| YarnNmJvmJavaThreadsThreadsnew          | JVM线程数量_ThreadsNew               | 个       | JVM 线程数量     | id4yarnnodemanager、<br>host4yarnnodemanager   |
| YarnNmJvmJavaThreadsThreadsrunnable     | JVM线程数量_ThreadsRunnable          | 个       | JVM 线程数量     | id4yarnnodemanager、<br>host4yarnnodemanager   |
| YarnNmJvmJavaThreadsThreadsblocked      | JVM线程数量_ThreadsBlocked           | 个       | JVM 线程数量     | id4yarnnodemanager、<br>host4yarnnodemanager   |
| YarnNmJvmJavaThreadsThreadswaiting      | JVM线程数量_ThreadsWaiting           | 个       | JVM 线程数量     | id4yarnnodemanager、<br>host4yarnnodemanager   |
| YarnNmJvmJavaThreadsThreadstimedwaiting | JVM线程数量_ThreadsTimedWaiting      | 个       | JVM 线程数量     | id4yarnnodemanager、<br>host4yarnnodemanager   |
| YarnNmJvmJavaThreadsThreadsterminated   | JVM线程数量_ThreadsTerminated        | 个       | JVM 线程数量     | id4yarnnodemanager、<br>host4yarnnodemanager   |
| YarnNmJvmLogTotalLogfatal               | JVM日志数量_LogFatal                 | 次       | JVM 日志数量     | id4yarnnodemanager、<br>host4yarnnodemanager   |
| YarnNmJvmLogTotalLogerror               | JVM日志数量_LogError                 | 次       | JVM 日志数量     | id4yarnnodemanager、<br>host4yarnnodemanager   |
| YarnNmJvmLogTotalLogwarn                | JVM日志数量_LogWarn                  | 次       | JVM 日志数量     | id4yarnnodemanager、<br>host4yarnnodemanager   |
| YarnNmJvmLogTotalLoginfo                | JVM日志数量_LogInfo                  | 次       | JVM 日志数量     | id4yarnnodemanager、<br>host4yarnnodemanager   |
| YarnNmJvmMemMemnonheapusedm             | JVM内存_MemNonHeapUsedM              | MB       | JVM 内存         | id4yarnnodemanager、<br>host4yarnnodemanager   |
| YarnNmJvmMemMemnonheapcommittedm        | JVM内存_MemNonHeapCommittedM         | MB       | JVM 内存         | id4yarnnodemanager、<br>host4yarnnodemanager   |
| YarnNmJvmMemMemheapusedm                | JVM内存_MemHeapUsedM                 | MB       | JVM 内存         | id4yarnnodemanager、<br>host118yarnnodemanager |
| YarnNmJvmMemMemheapcommittedm           | JVM内存_MemHeapCommittedM            | MB       | JVM 内存         | id4yarnnodemanager、<br>host4yarnnodemanager   |
| YarnNmJvmMemMemheapmaxm                 | JVM内存_MemHeapMaxM                  | MB       | JVM 内存         | id4yarnnodemanager、<br>host4yarnnodemanager   |
| YarnNmJvmMemMemmaxm                     | JVM内存_MemMaxM                      | MB       | JVM 内存         | id4yarnnodemanager、<br>host4yarnnodemanager   |
| YarnNmVcoresAvailablevcores             | CPU核数_AvailableVCores              | 核       | CPU 核数         | id4yarnnodemanager、<br>host4yarnnodemanager   |
| YarnNmVcoresAllocatedvcores             | CPU核数_AllocatedVCores              | 核       | CPU 核数         | id4yarnnodemanager、<br>host4yarnnodemanager   |
| YarnNmMemAllocatedgb                    | 内存大小_AllocatedGB                 | GB       | 内存大小         | id4yarnnodemanager、<br>host4yarnnodemanager   |
| YarnNmMemAvailablegb                    | 内存大小_AvailableGB                 | GB       | 内存大小         | id4yarnnodemanager、<br>host4yarnnodemanager   |
| YarnNmOsCpuLoadProcesscpuload           | CPU利用率_ProcessCpuLoad             | %        | CPU 利用率       | id4yarnnodemanager、<br>host4yarnnodemanager   |
| YarnNmOsCpuTimeProcesscputime           | CPU累计使用时间_ProcessCpuTime       | ms       | CPU 累计使用时间 | id4yarnnodemanager、<br>host4yarnnodemanager   |
| YarnNmOsFdCountMaxfiledescriptorcount   | 文件描述符数_MaxFileDescriptorCount  | 个       | 文件描述符数     | id4yarnnodemanager、<br>host4yarnnodemanager   |
| YarnNmOsFdCountOpenfiledescriptorcount  | 文件描述符数_OpenFileDescriptorCount | 个       | 文件描述符数     | id4yarnnodemanager、<br>host4yarnnodemanager   |
| YarnNmRtUptimeUptime                    | 进程运行时长_Uptime                  | s        | 进程运行时长     | id4yarnnodemanager、<br>host4yarnnodemanager   |
| YarnNmThreadCountDaemonthreadcount      | 工作线程数_DaemonThreadCount         | 个       | 工作线程数       | id4yarnnodemanager、<br>host4yarnnodemanager   |
| YarnNmThreadCountThreadcount            | 工作线程数_ThreadCount               | 个       | 工作线程数       | id4yarnnodemanager、<br>host4yarnnodemanager   |

## 各维度对应参数总览

| 参数名称                       | 维度名称                  | 维度解释                      | 格式                                                         |
| ------------------------------ | ------------------------- | ----------------------------- | ------------------------------------------------------------ |
| Instances.N.Dimensions.0.Name  | id4yarnoverview           | EMR 实例 ID 的维度名称        | 输入  String 类型维度名称：id4yarnoverview                   |
| Instances.N.Dimensions.0.Value | id4yarnoverview           | EMR  实例具体 ID              | 输入  EMR 具体实例 ID，例如 ：emr-mm8bs222                   |
| Instances.N.Dimensions.1.Name  | host4yarnoverview         | EMR  实例中节点 IP 的维度名称 | 输入String  类型维度名称：host4yarnoverview                  |
| Instances.N.Dimensions.1.Value | host4yarnoverview         | EMR  实例中具体节点 IP        | 输入具体节点  IP ，可从控制台获取，登录 [腾讯云 MapReduce 控制台](https://console.cloud.tencent.com/emr) > 单击实例 > 集群资源 > 资源管理 > 节点内网 IP。您也可通过 [查询节点信息](https://cloud.tencent.com/document/product/589/41707) API 获取。 |
| Instances.N.Dimensions.0.Name  | id4yarnresourcemanager    | EMR 实例 ID 的维度名称        | 输入 String  类型维度名称：id4yarnresourcemanager            |
| Instances.N.Dimensions.0.Value | id4yarnresourcemanager    | EMR 实例具体 ID               | 输入 EMR 具体实例 ID，例如  ：emr-mm8bs222                   |
| Instances.N.Dimensions.1.Name  | host4yarnresourcemanager  | EMR 实例中节点 IP 的维度名称  | 输入String  类型维度名称：host4yarnresourcemanager           |
| Instances.N.Dimensions.1.Value | host4yarnresourcemanager  | EMR 实例中具体节点 IP         | 输入具体节点  IP ，可从控制台获取，登录 [腾讯云 MapReduce 控制台](https://console.cloud.tencent.com/emr) > 单击实例 > 集群资源 > 资源管理 > 节点内网 IP。您也可通过 [查询节点信息](https://cloud.tencent.com/document/product/589/41707) API 获取。 |
| Instances.N.Dimensions.0.Name  | id4yarnjobhistoryserver   | EMR  实例 ID 的维度名称       | 输入 String  类型维度名称：id4yarnjobhistoryserver           |
| Instances.N.Dimensions.0.Value | id4yarnjobhistoryserver   | EMR  实例具体 ID              | 输入 EMR 具体实例 ID，例如  ：emr-mm8bs222                   |
| Instances.N.Dimensions.1.Name  | host4yarnjobhistoryserver | EMR  实例中节点 IP 的维度名称 | 输入String  类型维度名称：host4yarnjobhistoryserver          |
| Instances.N.Dimensions.1.Value | host4yarnjobhistoryserver | EMR  实例中具体节点 IP        | 输入具体节点  IP ，可从控制台获取，登录 [腾讯云 MapReduce 控制台](https://console.cloud.tencent.com/emr) > 单击实例 > 集群资源 > 资源管理 > 节点内网 IP。您也可通过 [查询节点信息](https://cloud.tencent.com/document/product/589/41707) API 获取。 |
| Instances.N.Dimensions.0.Name  | id4yarnnodemanager        | EMR 实例 ID 的维度名称        | 输入 String  类型维度名称：id4yarnnodemanager                |
| Instances.N.Dimensions.0.Value | id4yarnnodemanager        | EMR 实例具体 ID               | 输入 EMR 具体实例 ID，例如  ：emr-mm8bs222                   |
| Instances.N.Dimensions.1.Name  | host4yarnnodemanager      | EMR 实例中节点 IP 的维度名称  | 输入String  类型维度名称：host4yarnnodemanager               |
| Instances.N.Dimensions.1.Value | host4yarnnodemanager      | EMR 实例中具体节点 IP         | 输入具体节点  IP ，可从控制台获取，登录 [腾讯云 MapReduce 控制台](https://console.cloud.tencent.com/emr) > 单击实例 > 集群资源 > 资源管理 > 节点内网 IP。您也可通过 [查询节点信息](https://cloud.tencent.com/document/product/589/41707) API 获取。 |

## 入参说明

弹性 MapReduce（YARN）支持以下五种维度组合的查询方式，五种入参取值如下： 

**1. 查询 Yarn-Overview Aggregation 、YARN-Cluster 的指标监控数据，入参取值如下：**&Namespace=QCE/TXMR_YARN
&Instances.N.Dimensions.0.Name=id4yarnoverview
&Instances.N.Dimensions.0.Value=EMR 实例 ID

**2. 查询 Yarn-Overview 的指标监控数据，入参取值如下：**
&Namespace=QCE/TXMR_YARN
&Instances.N.Dimensions.0.Name=id4yarnoverview
&Instances.N.Dimensions.0.Value=EMR 实例 ID
&Instances.N.Dimensions.1.Name=host4yarnoverview
&Instances.N.Dimensions.1.Value=EMR 实例中具体节点 IP 

**3. 查询 YARN-ResourceManager  的指标监控数据，入参取值如下：**
&Namespace=QCE/TXMR_YARN
&Instances.N.Dimensions.0.Name=id4yarnresourcemanager
&Instances.N.Dimensions.0.Value=EMR 实例 ID 
&Instances.N.Dimensions.1.Name=host4yarnresourcemanager
&Instances.N.Dimensions.1.Value=EMR 实例中具体节点 IP

**4. 查询 YARN-JobHistoryServer   的指标监控数据，入参取值如下：**
&Namespace=QCE/TXMR_YARN
&Instances.N.Dimensions.0.Name=id4yarnjobhistoryserver 
&Instances.N.Dimensions.0.Value=EMR 实例 ID 
&Instances.N.Dimensions.1.Name=host4yarnjobhistoryserver
&Instances.N.Dimensions.1.Value=EMR实例中具体节点 IP 

**5. 查询 YARN-NodeManager 的指标监控数据，入参取值如下：**
&Namespace=QCE/TXMR_YARN
&Instances.N.Dimensions.0.Name=id4yarnnodemanager 
&Instances.N.Dimensions.0.Value=EMR 实例 ID 
&Instances.N.Dimensions.1.Name=host4yarnnodemanager
&Instances.N.Dimensions.1.Value=EMR实例中具体节点 IP 
