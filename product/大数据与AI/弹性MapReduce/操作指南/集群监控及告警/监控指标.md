## 主机监控指标

### 主机-CPU

| 指标名称  | 单位 | 指标含义                       |
| --------- | ---- | ------------------------------ |
| idle      | %    | CPU IDLE 时间占比              |
| irq       | %    | 中断占比                       |
| nice      | %    | NICE 优先级使用 CPU 占比       |
| steal     | %    | 虚拟 CPU 等待实际 CPU 时间占比 |
| softirq   | %    | CPU 软中断占比                 |
| guest     | %    | 运行虚拟处理器所用的时间百分比 |
| system    | %    | 内核态 CPU 占用比              |
| user      | %    | 用户态 CPU 占用比              |
| iowait    | %    | 进程等待 IO CPU 空闲占比       |
| 1m        | 1/s  | 1分钟负载                      |
| 5m        | 1/s  | 5分钟负载                      |
| 15m       | 1/s  | 15分钟负载                     |
| cpu_count | 个   | CPU 核数                       |

### 主机-MEMORY

| 指标名称          | 单位 | 指标含义                       |
| ----------------- | ---- | ------------------------------ |
| MemTotal          | GB   | 内存总量                       |
| MemFree           | GB   | 空闲内存总量                 |
| MemAvailable      | GB   | 可用内存总量                   |
| Buffers           | GB   | BUFFER 缓存占用内存总量        |
| Cached            | GB   | 文件缓存占用内存总量           |
| SwapCached        | GB   | 匿名页写入交换区内存总量       |
| SwapFree          | GB   | 可用交换区总量                 |
| AnonPages         | GB   | 未映射内存总量                 |
| SwapTotal         | GB   | 交换区总量                     |
| Dirty             | GB   | 需要写入磁盘的内存总量         |
| Writeback         | GB   | 正在被写回磁盘的内存总量       |
| HardwareCorrupted | GB   | 内存硬件故障导致不可用内存总量 |
| Shmem             | GB   | 共享内存占用的内存总量         |
| available_percent | %    | 可用内存占总内存百分比         |
| used_percent      | %    | 已使用内存占总内存百分比       |

### 主机-NETWORK

| 指标名称               | 单位     | 指标含义                                                     |
| ---------------------- | -------- | ------------------------------------------------------------ |
| ListenDrops            | 次/s     | 任何原因导致的丢弃传入连接（SYN 包）的次数                   |
| ListenOverflows        | 次/s     | 三次握手最后一步完成之后，Accept 队列超过上限的次数          |
| SyncookiesFailed       | 次/s     | 收到携带无效 SYN Cookie 信息的包的个数                       |
| SyncookiesRecv         | 次/s     | 收到携带有效 SYN Cookie 信息的包的个数                       |
| SyncookiesSent         | 次/s     | 使用 SYN Cookie 发送的 SYN/ACK 包个数                        |
| TCPAbortOnTimeout      | 次/s     | 因各种计时器（RTO/PTO/keepalive）的重传次数超过上限而关闭连接的 |
| TCPAbortOnData         | 次/s     | socket 收到未知数据导致被关闭的次数                          |
| TCPAbortOnClose        | 次/s     | 用户态程序在缓冲区内还有数据时关闭 socket 的次数             |
| TCPAbortOnMemory       | 次/s     | 因内存问题关闭连接的次数                                     |
| TCPAbortOnLinger       | 次/s     | 关闭后，在徘徊状态中止的连接的次数                           |
| TCPAbortFailed         | 次/s     | 尝试结束连接失败的次数                                       |
| ActiveOpens            | 个/s     | 主动建立 TCP 连接数量                                        |
| CurrEstab              | 个/s     | 当前已建立 TCP 连接数量                                      |
| PassiveOpens           | 个/s     | 被动建立 TCP 连接数量                                        |
| AttemptFails           | 个/s     | 建立连接失败数量                                             |
| EstabResets            | 个/s     | 连接被 REST 的数量                                           |
| InSegs                 | 个/s     | 收到的数据包个数，包括有错误的包个数                         |
| OutSegs                | 个/s     | 发送的数据包个数                                             |
| RetransSegs            | 个/s     | TCP 接收报文数量                                             |
| InErrs                 | 个/s     | 重传的包个数                                                 |
| OutRsts                | 个/s     | 发出 RST 包个数                                              |
| RetransSegsRate        | %        | TCP 层重传率                                                 |
| ResetRate              | %        | RESET 发送频率                                               |
| InErrRate              | %        | 错误包占比                                                   |
| TW                     | 个/s     | 经过正常的超时结束 TIME_WAIT 状态的 socket 数量            |
| TWKilled               | 个/s     | 通过 tcp_tw_recycle 机制结束 TIME_WAIT 状态的 socket 数量    |
| TCPTimeWaitOverflow    | 个/s     | 因为超过限制而无法分配的 TIME_WAIT socket 数量               |
| TWRecycled             | 个/s     | 通过 tcp_tw_reuse 机制结束 TIME_WAIT 状态的 socket 数量      |
| TCPTimeouts            | 次/s     | RTO timer 第一次超时次数                                     |
| TCPSpuriousRTOs        | 次/s     | 通过 F-RTO 机制发现的虚假超时次数                            |
| TCPLossProbes          | 次/s     | Probe Timeout(PTO) 导致发送 Tail Loss Probe(TLP) 包的次数      |
| TCPLossProbeRecovery   | 次/s     | 丢失包刚好被 TLP 探测包修复的次数                            |
| TCPRenoRecoveryFail    | 次/s     | 先进入 Recovery 阶段，然后又 RTO 的次数，对端不支持 SACK 选项 |
| TCPSackRecoveryFail    | 次/s     | 先进入 Recovery 阶段，然后又 RTO 的次数，对端支持 SACK 选项  |
| TCPRenoFailures        | 次/s     | 先进 TCP_CA_Disorder 阶段，然后又 RTO 超时的次数，对端不支持 SACK 选项 |
| TCPSackFailures        | 次/s     | 先进 TCP_CA_Disorder 阶段，然后又 RTO 超时的次数，对端支持 SACK 选项 |
| TCPLossFailures        | 次/s     | 先进 TCP_CA_Loss 阶段，然后又 RTO 超时的次数                 |
| RtoAlgorithm           | 1/s      | 转发未答复对象的延时的算法的数                               |
| RtoMax                 | 1/s      | TCP 延迟重发的最大值                                         |
| RtoMin                 | 1/s      | TCP 延迟重发的最小值                                         |
| TCPLostRetransmit      | 次/s     | 丢失重传 SKB 的次数                                          |
| TCPFastRetrans         | 次/s     | 快重传 SKB 次数                                              |
| TCPForwardRetrans      | 次/s     | 一般重传 SKB 次数                                            |
| TCPSlowStartRetrans    | 次/s     | 成功慢启动重传 SKB 数量                                      |
| TCPRetransFail         | 次/s     | 尝试重传失败次数                                             |
| OutDatagrams           | 个/s     | 发送 UDP 数据报文数量                                        |
| InDatagrams            | 个/s     | 接收 UDP 数据报文数量                                        |
| eth0-receive_bytes     | MB/s     | 网卡接收数据量                                               |
| eth0-transmit_bytes    | MB/s     | 网卡发送数据量                                               |
| eth0-receive_drop      | packet/s | 网卡接收丢弃数据量                                           |
| eth0-receive_errs      | packet/s | 网卡接收异常数量                                             |
| eth0-transmit_drop     | packet/s | 网卡发送丢弃数据量                                           |
| eth0-transmit_errs     | packet/s | 网卡发送异常数据量                                           |
| eth0-transmit_packetsl | packet/s | 网卡发送包数量                                               |
| TCP_inuse              | 个       | 在使用（正在侦听）的 TCP 套接字数量                          |
| TCP_orphan             | 个       | 等待关闭的 TCP 连接数                                        |
| TCP_tw                 | 个       | 待销毁的 TCP socket 数                                       |
| TCP_alloc              | 个       | 已分配（已建立、已申请到 sk_buff）的 TCP 套接字数量          |
| ESTABLISHED            | 个       | Established 状态的 TCP 链接数量                              |
| SYN-SENT               | 个       | SYN-SENT 状态的 TCP 链接数量                                 |
| SYN-RECV               | 个       | SYN-RECV 状态的 TCP 链接数量                                 |
| FIN-WAIT1              | 个       | FIN-WAIT1 状态的 TCP 链接数量                                |
| FIN-WAIT2              | 个       | FIN-WAIT2 状态的 TCP 链接数量                                |
| TIME-WAIT              | 个       | TIME-WAIT 状态的 TCP 链接数量                                |
| CLOSE                  | 个       | CLOSE 状态的 TCP 链接数量                                    |
| CLOSE-WAIT             | 个       | CLOSE-WAIT 状态的 TCP 链接数量                               |
| LAST-ACK               | 个       | LAST-ACK 状态的 TCP 链接数量                                 |
| LISTEN                 | 个       | LISTEN 状态的 TCP 链接数量                                   |
| CLOSEING               | 个       | CLOSEING 状态的 TCP 链接数量                                 |

### 主机-磁盘

| 指标名称    | 单位 | 指标含义                        |
| ----------- | ---- | ------------------------------- |
| Read        | MB/s | 每秒读数据量                    |
| Write       | MB/s | 每秒写数据量                    |
| vd-         | 次   | 当前设备上正在进行的 IO 操作      |
| Read        | ms   | 平均每次设备 I/O 读操作的等待时间 |
| Write       | ms   | 平均每次设备 I/O 写操作的等待时间 |
| IO          | ms   | 平均每次 IO 请求的处理时间        |
| Read        | 次/s | 读操作 QPS                      |
| Write       | 次/s | 写操作 QPS                      |
| Merge-Read  | 次/s | 合并读操作 QPS                  |
| Merge-Write | 次/s | 合并写操作 QPS                  |
| vd-         | %    | 磁盘繁忙程度                    |
| Free        | GB   | 磁盘剩余空间                    |
| Used        | GB   | 磁盘已使用空间                  |
| Total       | GB   | 磁盘总空间                      |
| Used        | %    | 磁盘使用率                      |
| Free        | 个   | 磁盘剩余 INODES 数量            |
| Total       | 个   | 磁盘 INODES 总数量              |
| Used        | %    | 磁盘 INODES 使用率              |

### 主机-文件句柄

| 指标名称  | 单位 | 指标含义           |
| --------- | ---- | ------------------ |
| allocated | 个   | 已分配文件句柄数量 |
| maximum   | 个   | 最大文件句柄数量   |

### 主机-PROCESS

| 指标名称               | 单位    | 指标含义           |
| ---------------------- | ------- | ------------------ |
| intr_total             | 次/s    | 系统中断数量       |
| context_switches_total | 次/s    | 系统上下文切换数量 |
| forks_total            | 个/s    | 系统新建进程数量   |
| procs_running          | 个/s    | 系统运行进程数量   |
| procs_blocked          | 个/s    | 系统阻塞进程数量   |
| procs_total            | 个/s    | 系统总进程数量     |
| AgentVersionl          | version | agent 的版本       |

## HDFS 监控指标

### HDFS-概览

| 指标名称                     | 指标单位 | 指标含义                                      |
| ---------------------------- | -------- | --------------------------------------------- |
| CapacityTotal                | GB       | 集群存储总容量                                |
| CapacityUsed                 | GB       | 集群存储已使用容量                            |
| CapacityRemaining            | GB       | 集群存储剩余容量                              |
| CapacityUsedNonDFS           | GB       | 集群非 HDFS 使用容量                          |
| TotalLoad                    | 1        | 当前连接数                                    |
| FilesTotal                   | 个       | 总文件数量                                    |
| BlocksTotal                  | 个       | 总 BLOCK 数量                                 |
| PendingReplicationBlocks     | 个       | 等待被备份的块数量                            |
| UnderReplicatedBlocks        | 个       | 副本数不够的块数量                            |
| CorruptBlocks                | 个       | 坏块数量                                      |
| ScheduledReplicationBlocks   | 个       | 安排要备份的块数量                            |
| PendingDeletionBlocks        | 个       | 等待被删除的块数量                            |
| ExcessBlocks                 | 个       | 多于的块数量                                  |
| PostponedMisreplicatedBlocks | 个       | 被推迟处理的异常块数量                        |
| BlockCapacity                | 个       | BLOCK 容量                                    |
| NumLiveDataNodes             | 个       | 活的数据节点数量                              |
| NumDeadDataNodes             | 个       | 已经标记为 Dead 状态的数据节点数量            |
| NumDecomLiveDataNodes        | 个       | 下线且 Live 的节点数量                        |
| NumDecomDeadDataNodes        | 个       | 下线且 Dead 的节点数量                        |
| NumDecommissioningDataNodes  | 个       | 正在下线的节点数量                            |
| NumStaleDataNodes            | 个       | 由于心跳延迟而标记为过期的 DataNodes 当前数量 |
| Snapshots                    | 个       | Snapshots 数量                                |
| VolumeFailuresTotal          | 次       | 所有 Datanodes 的全故障总数                   |

### HDFS-NameNode

| 指标名称                                      | 指标单位 | 指标含义                                             |
| --------------------------------------------- | -------- | ---------------------------------------------------- |
| ReceivedBytes                                 | Bytes/s  | 接收数据速率                                         |
| SentBytes                                     | Bytes/s  | 发送数据速率                                         |
| RpcQueueTimeNumOps                            | 1/s      | RPC 调用速率                                         |
| RpcQueueTimeAvgTime                           | ms       | RPC 平均延迟时间                                     |
| RpcAuthenticationFailures                     | 次     | RPC 验证失败次数                                     |
| RpcAuthenticationSuccesses                    | 次     | RPC 验证成功次数                                     |
| RpcAuthorizationFailures                      | 次     | RPC 授权失败次数                                     |
| RpcAuthorizationSuccesses                     | 次     | RPC 授权成功次数                                     |
| NumOpenConnections                            | 个     | 当前链接数量                                         |
| CallQueueLength                               | 个     | 当前 RPC 处理队列长度                                |
| MemNonHeapUsedM                               | MB       | JVM 当前已经使用的 NonHeapMemory 的大小              |
| MemNonHeapCommittedM                          | MB       | JVM 内存                                             |
| MemHeapUsedM                                  | MB       | JVM 当前已经使用的 HeapMemory 的大小                 |
| MemHeapCommittedM                             | MB       | JVM HeapMemory 提交大小                              |
| MemHeapMaxM                                   | MB       | JVM 配置的 HeapMemory 的大小                         |
| MemMaxM                                       | MB       | JVM 运行时的可以使用的最大的内存的大小               |
| BlockReportAvgTime                            | 次/s     | 每秒处理 DataNode Blcok 平均延迟                     |
| FGC                                           | 1/s      | Full GC 次数                                         |
| YGC                                           | 2/s      | Young GC 次数                                        |
| YGCT                                          | ms       | Young GC 消耗时间                                    |
| FGCT                                          | ms       | Full GC 消耗时间                                     |
| GCT                                           | ms       | 垃圾回收时间消耗                                     |
| ThreadsNew                                    | 个       | 处于新建状态的线程数量                               |
| ThreadsRunnable                               | 个       | 处于可运行状态的线程数量                             |
| ThreadsBlocked                                | 个       | 处于阻塞状态的线程数量                               |
| ThreadsWaiting                                | 个       | 处于 WAITING 状态的线程数量                          |
| ThreadsTimedWaiting                           | 个       | 处于 TIMED WAITING 状态的线程数量                    |
| ThreadsTerminated                             | 个       | 处于 Terminated 状态的线程数量                       |
| LogFatal                                      | 个       | Fatal 日志数量                                       |
| LogError                                      | 个       | Error 日志数量                                       |
| LogWarn                                       | 个       | Warn 日志数量                                        |
| LogInfo                                       | 个       | Info 日志数量                                        |
| S0                                            | %        | Survivor 0区内存使用占比                             |
| S1                                            | %        | Survivor 1区内存使用占比                             |
| E                                             | %        | Eden 区内存使用占比                                  |
| O                                             | %        | Old 区内存使用占比                                   |
| M                                             | %        | Metaspace 区内存使用占比                             |
| CCS                                           | %        | Compressed class space 区内存使用占比                |
| NumStaleStorages                              | 个       | 由于心跳延迟而标记为过期的 DataNodes 当前数目        |
| PendingDataNodeMessageCount                   | 个/s     | DATANODE 的请求被 QUEUE 在 standby namenode 中的个数 |
| NumberOfMissingBlocks                         | 个       | 缺失的数据块数量                                     |
| NumberOfMissingBlocksWithReplicationFactorOne | 个       | 缺失的数据库数量（rf = 1）                           |
| AllowSnapshotOps                              | 次/s     | 每秒执行 AllowSnapshot 操作的次数                    |
| DisallowSnapshotOps                           | 次/s     | 每秒执行 DisallowSnapshot 操作的次数                 |
| CreateSnapshotOps                             | 次/s     | 每秒执行 CreateSnapshot 操作的次数                   |
| DeleteSnapshotOps                             | 次/s     | 每秒执行 DeleteSnapshot 操作的次数                   |
| ListSnapshottableDirOps                       | 次/s     | 每秒执行 ListSnapshottableDir 操作次数               |
| SnapshotDiffReportOps                         | 次/s     | 每秒执行 SnapshotDiffReportOps 的次数                |
| RenameSnapshotOps                             | 次/s     | 每秒执行 RenameSnapshotOps 的次数                    |
| CreateFileOps                                 | 次/s     | 每秒执行 CreateFile 操作的次数                       |
| GetListingOps                                 | 次/s     | 每秒执行 GetListing 操作的次数                       |
| TotalFileOps                                  | 次/s     | 每秒执行 TotalFileOps 的次数                         |
| DeleteFileOps                                 | 次/s     | 每秒执行 DeleteFile 操作的次数                       |
| FileInfoOps                                   | 次/s     | 每秒执行 FileInfo 操作的次数                         |
| GetAdditionalDatanodeOps                      | 次/s     | 每秒执行 GetAdditionalDatanode 操作的次数            |
| CreateSymlinkOps                              | 次/s     | 每秒执行 CreateSymlink 操作的次数                    |
| GetLinkTargetOps                              | 次/s     | 每秒执行 GetLinkTarget 操作的次数                    |
| FilesInGetListingOps                          | 次/s     | 每秒执行 FilesInGetListing 操作的次数                |
| TransactionsNumOps                            | 次/s     | 每秒处理 Journal transaction 操作的次数              |
| TransactionsBatchedInSync                     | 次/s     | 每秒批量处理 Journal transaction 操作次数            |
| GetEditNumOps                                 | 次/s     | 每秒执行 GetEditNumOps 的次数                        |
| GetImageNumOps                                | 次/s     | 每秒执行 GetImageNumOps 的次数                       |
| PutImageNumOps                                | 次/s     | 每秒执行 PutImageNumOps 的次数                       |
| SyncsNumOps                                   | 次/s     | 每秒处理 Journal syncs 操作的次数                    |
| BlockReceivedAndDeletedOps                    | 次/s     | 每秒执行 BlockReceivedAndDeletedOps 的次数           |
| BlockOpsQueued                                | 次/s     | 处理 DataNode Block 上报操作的延迟                   |
| CacheReportNumOps                             | 次/s     | 每秒处理 CacheReport 操作的次数                      |
| BlockReportNumQps                             | 次/s     | 每秒处理 DataNode Blcok 上报操作的次数               |
| SyncsAvgTime                                  | ms       | 处理 Journal syncs 操作的平均延迟                    |
| CacheReportAvgTime                            | ms       | 缓存上报动作平均延迟                                 |
| GetEditAvgTime                                | ms       | 读取 Edit 文件操作平均延迟                           |
| GetImageAvgTime                               | ms       | 读取镜像文件平均延迟                                 |
| PutImageAvgTime                               | ms       | 写入镜像文件平均延迟                                 |
| TransactionsAvgTime                           | ms       | 处理 Journal transaction 操作的平均延迟              |
| StartTime                                     | ms       | 进程启动时间                                         |
| State                                         | 1        | NN 状态                                              |
| PeakThreadCount                               | 个       | 峰值线程数                                           |
| ThreadCount                                   | 个       | 线程数量                                             |
| DaemonThreadCount                             | 个       | 后台线程数量                                         |

### HDFS-DataNode

| 指标名称                                | 指标单位 | 指标含义                                   |
| --------------------------------------- | -------- | ------------------------------------------ |
| XceiverCount                            | 个       | Xceiver 数量                               |
| BytesWrittenMB                          | Bytes/s  | 写入 DN 的字节速率                         |
| BytesReadMB                             | Bytes/s  | 读取 DN 的字节速率                         |
| RemoteBytesReadMB                       | Bytes/s  | 远程客户端读取字节速率                     |
| RemoteBytesWrittenMB                    | Bytes/s  | 远程客户端写入字节速率                     |
| WritesFromRemoteClient                  | 个       | 来自远程客户端写操作 QPS                   |
| WritesFromLocalClient                   | 个       | 来自本地客户端写操作 OPS                   |
| ReadsFromRemoteClient                   | 个       | 来自远程客户端读操作 QPS                   |
| ReadsFromLocalClient                    | 个       | 来自本地客户端读操作 QPS                   |
| BlockVerificationFailures               | 次/s     | BLOCK 校验失败数量                         |
| VolumeFailures                          | 次/s     | 磁盘故障次数                               |
| DatanodeNetworkErrors                   | 次/s     | 网络错误统计                               |
| HeartbeatsAvgTime                       | ms       | 心跳接口平均时间                           |
| HeartbeatsNumOps                        | 次/s     | 心跳接口 QPS                               |
| SendDataPacketTransferNanosAvgTime      | ms       | 发送数据包平均时间                         |
| ReadBlockOpNumOps                       | 次/s     | 从 DataNode 读取 Block OPS                 |
| WriteBlockOpNumOps                      | 次/s     | 向 DataNode 写入 Block OPS                 |
| BlockChecksumOpNumOps                   | 次/s     | DataNode 进行 Checksum 操作的 OPS          |
| CopyBlockOpNumOps                       | 次/s     | 复制 Block 操作的 OPS                      |
| ReplaceBlockOpNumOps                    | 次/s     | Replace Block 操作的 OPS                   |
| BlockReportsNumOps                      | 次/s     | BLOCK 汇报动作的 OPS                       |
| IncrementalBlockReportsNumOps           | 次/s     | BLOCK 增量汇报的 OPS                       |
| CacheReportsNumOps                      | 次/s     | 缓存汇报的 OPS                             |
| PacketAckRoundTripTimeNanosNumOps       | 次/s     | 每秒处理 ACK ROUND TRIP 次数               |
| FsyncNanosOps                           | 次/s     | FSYNC 次数                                 |
| FlushNanosNumOps                        | 次/s     | 每秒处理 Flush 操作次数                    |
| ReadBlockOpAvgTime                      | ms       | 读取 Block 操作平均时间                    |
| WriteBlockOpAvgTime                     | ms       | 写 Blcok 操作平均时间                      |
| BlockChecksumOpAvgTime                  | ms       | 块校验操作平均时间                         |
| CopyBlockOpAvgTime                      | ms       | 复制块操作平均时间                         |
| ReplaceBlockOpAvgTime                   | ms       | Replace Block 操作平均时间                 |
| BlockReportsAvgTime                     | ms       | 块汇报平均时间                             |
| IncrementalBlockReportsAvgTime          | ms       | 增量块汇报平均时间                         |
| CacheReportsAvgTime                     | ms       | 缓存汇报平均时间                           |
| PacketAckRoundTripTimeNanosAvgTime      | ms       | 处理 ACK ROUND TRIP 平均时间               |
| FlushNanosAvgTime                       | ms       | Flush 操作平均时间                         |
| FsyncNanosAvgTime                       | ms       | Fsync 操作平均时间                         |
| RamDiskBlocksWrite                      | 块/s     | 写入内存的块的总数                         |
| RamDiskBlocksWriteFallback              | 块/s     | 写入内存但未成功的块总数（故障转移到磁盘） |
| RamDiskBlocksDeletedBeforeLazyPersisted | 块/s     | 应用程序在被保存到磁盘之前被删除的块的总数 |
| RamDiskBlocksReadHits                   | 块/s     | 内存中的块被读取的总次数                   |
| RamDiskBlocksEvicted                    | 块/s     | 内存中被清除的块总数                       |
| RamDiskBlocksEvictedWithoutRead         | 块/s     | 从内存中取出的内存块总数          |
| RamDiskBlocksLazyPersisted              | 块/s     | 惰性写入器写入磁盘的总数                   |
| RamDiskBytesLazyPersisted               | Bytes/s  | 由懒惰写入器写入磁盘的总字节数             |
| RamDiskBytesWrite                       | Bytes/s  | 写入内存的总字节数                         |
| MemNonHeapUsedM                         | MB       | JVM 当前已经使用的 NonHeapMemory 的大小    |
| MemNonHeapCommittedM                    | MB       | JVM 配置的 NonHeapCommittedM 的大小        |
| MemHeapUsedM                            | MB       | JVM 当前已经使用的 HeapMemory 的大小       |
| MemHeapCommittedM                       | MB       | JVM HeapMemory 提交大小                    |
| MemHeapMaxM                             | MB       | JVM 配置的 HeapMemory 的大小               |
| MemMaxM                                 | MB       | JVM 运行时的可以使用的最大的内存的大小     |
| ThreadsNew                              | 个       | 处于新建状态的线程数量                     |
| ThreadsRunnable                         | 个       | 处于可运行状态的线程数量                   |
| ThreadsBlocked                          | 个       | 处于阻塞状态的线程数量                     |
| ThreadsWaiting                          | 个       | 处于 WAITING 状态的线程数量                |
| ThreadsTimedWaiting                     | 个       | 处于 TIMED WAITING 状态的线程数量          |
| ThreadsTerminated                       | 个       | 处于 Terminated 状态的线程数量             |
| LogFatal                                | 个       | Fatal 日志数量                             |
| LogError                                | 个       | Error 日志数量                             |
| LogWarn                                 | 个       | Warn 日志数量                              |
| LogInfo                                 | 个       | Info 日志数量                              |
| S0                                      | %        | Survivor 0区内存使用占比                   |
| S1                                      | %        | Survivor 1区内存使用占比                   |
| E                                       | %        | Eden 区内存使用占比                        |
| O                                       | %        | Old 区内存使用占比                         |
| M                                       | %        | Metaspace 区内存使用占比                   |
| CCS                                     | %        | Compressed class space 区内存使用占比      |
| FGC                                     | 次       | Full GC 次数                               |
| YGC                                     | ms       | Young GC 次数                              |
| YGCT                                    | s        | Young GC 消耗时间                          |
| FGCT                                    | s        | Full GC 消耗时间                           |
| GCT                                     | s        | 垃圾回收时间消耗                           |
| ReceivedBytes                           | Bytes/s  | 接收数据速率                               |
| SentBytes                               | Bytes/s  | 发送数据速率                               |
| RpcQueueTimeNumOps                      | 次/s     | RPC 调用速率                               |
| RpcQueueTimeAvgTime                     | ms       | RPC 平均延迟时间                           |
| RpcAuthenticationFailures               | 次/s     | RPC 验证失败次数                           |
| RpcAuthenticationSuccesses              | 次/s     | RPC 验证成功次数                           |
| RpcAuthorizationFailures                | 次/s     | RPC 授权失败次数                           |
| RpcAuthorizationSuccesses               | 次/s     | RPC 授权成功次数                           |
| NumOpenConnections                      | 个       | 当前链接数量                               |
| CallQueueLength                         | 1        | 当前 RPC 处理队列长度                      |
| CurrentThreadSystemTime                 | ms       | 系统时间                                   |
| CurrentThreadUserTime                   | ms       | 用户时间                                   |
| StartTime                               | s        | 进程启动时间                               |
| PeckThreadCount                         | 个       | 峰值线程数量                               |
| DaemonThreadCount                       | 个       | 后台线程数量                               |
| write                                   | MB/s     | 磁盘写速率                                 |
| read                                    | 次/s     | 读操作 QPS                                 |
| FsyncNanosOps                           | 次/s     | Fsync 操作平均次数                         |
| DataPacketOps                           | 次/s     | 包传输操作 QPS                              |

### HDFS-Journal Node 

| 指标名称                   | 指标单位 | 指标含义                                |
| -------------------------- | -------- | --------------------------------------- |
| MemNonHeapUsedM            | MB       | JVM 当前已经使用的 NonHeapMemory 的大小 |
| MemNonHeapCommittedM       | MB       | JVM 内存                                |
| MemHeapUsedM               | MB       | JVM 当前已经使用的 HeapMemory 的大小    |
| MemHeapCommittedM          | MB       | JVM HeapMemory 提交大小                 |
| MemHeapMaxM                | MB       | JVM 配置的 HeapMemory 的大小            |
| MemMaxM                    | MB       | JVM 运行时的可以使用的最大的内存的大小  |
| ThreadsNew                 | 个       | 处于新建状态的线程数量                  |
| ThreadsRunnable            | 个       | 处于可运行状态的线程数量                |
| ThreadsBlocked             | 个       | 处于阻塞状态的线程数量                  |
| ThreadsWaiting             | 个       | 处于 WAITING 状态的线程数量             |
| ThreadsTimedWaiting        | 个       | 处于 TIMED WAITING 状态的线程数量       |
| ThreadsTerminated          | 个       | 处于 Terminated 状态的线程数量          |
| LogFatal                   | 个       | Fatal 日志数量                          |
| LogError                   | 个       | Error 日志数量                          |
| LogWarn                    | 个       | Warn 日志数量                           |
| LogInfo                    | 个       | Info 日志数量                           |
| S0                         | %        | Survivor 0区内存使用占比                |
| S1                         | %        | Survivor 1区内存使用占比                |
| E                          | %        | Eden 区内存使用占比                     |
| O                          | %        | Old 区内存使用占比                      |
| M                          | %        | Metaspace 区内存使用占比                |
| CCS                        | %        | Compressed class space 区内存使用占比   |
| FGC                        | 次       | Full GC 次数                            |
| YGC                        | 次       | Young GC 次数                           |
| YGCT                       | s        | Young GC 消耗时间                       |
| FGCT                       | s        | Full GC 消耗时间                        |
| GCT                        | s        | 垃圾回收时间消耗                        |
| ReceivedBytes              | Bytes/s  | 接收数据速率                            |
| SentBytes                  | Bytes/s  | 发送数据速率                            |
| RpcQueueTimeNumOps         | 次/s     | RPC 调用速率                            |
| RpcQueueTimeAvgTime        | ms       | RPC 平均延迟时间                        |
| RpcAuthenticationFailures  | 次/s     | RPC 验证失败次数                        |
| RpcAuthenticationSuccesses | 次/s     | RPC 验证成功次数                        |
| RpcAuthorizationFailures   | 次/s     | RPC 授权失败次数                        |
| NumOpenConnections         | 个       | 当前链接数量                            |
| CallQueueLength            | 1        | 当前 RPC 处理队列长度                   |
| CurrentThreadSystemTime    | ms       | 系统时间                                |
| CurrentThreadUserTime      | ms       | 用户时间                                |
| StartTime                  | s        | 进程启动时间                            |
| ThreadCount                | 个       | 线程数量                                |
| PeckThreadCount            | 个       | 峰值线程数量                            |
| DaemonThreadCount          | 个       | 后台线程数量                            |

### HDFS-ZKFC

| 指标名称 | 指标单位 | 指标含义                              |
| -------- | -------- | ------------------------------------- |
| S0       | %        | Survivor 0区内存使用占比              |
| S1       | %        | Survivor 1区内存使用占比              |
| E        | %        | Eden 区内存使用占比                   |
| O        | %        | Old 区内存使用占比                    |
| M        | %        | Metaspace 区内存使用占比              |
| CCS      | %        | Compressed class space 区内存使用占比 |
| FGC      | 次       | Full GC 次数                          |
| YGC      | 次       | Young GC 次数                         |
| YGCT     | s        | Young GC 消耗时间                     |
| FGCT     | s        | Full GC 消耗时间                      |
| GCT      | s        | 垃圾回收时间消耗                      |

## YARN 监控指标

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



## HBASE 监控指标

### HBASE-概览

| 指标名称                | 指标单位 | 指标含义                   |
| ----------------------- | -------- | -------------------------- |
| ritCount                | 个       | 集群处于 RIT Region 个数   |
| ritCountOverThreshold   | 个       | 集群处于 RIT Region 个数   |
| ritOldestAge            | ms       | 集群 RIT 时间              |
| averageLoad             | 个       | 每个 RS 平均 REGION 数     |
| numRegionServers        | 个       | 集群 RS 数量               |
| numDeadRegionServers    | 个       | 集群 RS 数量               |
| receivedBytes           | bytes/s  | 集群读写数量               |
| sentBytes               | bytes/s  | 集群读写数量               |
| clusterRequests         | 个/s     | 集群总请求数量             |
| Assign_num_ops          | 次       | 集群 Assignment 管理器操作 |
| BulkAssign_num_ops      | 次       | 集群 Assignment 管理器操作 |
| BalancerCluster_num_ops | 次       | 集群负载均衡次数           |
| mergePlanCount          | 个       | 集群 Plan                  |
| splitPlanCount          | 个       | 集群 Plan                  |

### HBASE-HMaster

| 指标名称                       | 指标单位 | 指标含义       |
| ------------------------------ | -------- | -------------- |
| YGC                            | 次       | GC 次数        |
| FGC                            | 次       | GC 次数        |
| FGCT                           | s        | GC 时间        |
| GCT                            | s        | GC 时间        |
| YGCT                           | s        | GC 时间        |
| S0                             | %        | 内存区域占比   |
| E                              | %        | 内存区域占比   |
| CCS                            | %        | 内存区域占比   |
| S1                             | %        | 内存区域占比   |
| O                              | %        | 内存区域占比   |
| M                              | %        | 内存区域占比   |
| LogFatal                       | 次       | JVM 日志数量   |
| LogError                       | 次       | JVM 日志数量   |
| LogWarn                        | 次       | JVM 日志数量   |
| LogInfo                        | 次       | JVM 日志数量   |
| MemNonHeapUsedM                | MB       | JVM 内存       |
| MemNonHeapCommittedM           | MB       | JVM 内存       |
| MemNonHeapMaxM                 | MB       | JVM 内存       |
| MemHeapUsedM                   | MB       | JVM 内存       |
| MemHeapCommittedM              | MB       | JVM 内存       |
| MemHeapMaxM                    | MB       | JVM 内存       |
| MemMaxM                        | MB       | JVM 内存       |
| ThreadsNew                     | 个       | JVM 线程数量   |
| ThreadsRunnable                | 个       | JVM 线程数量   |
| ThreadsBlocked                 | 个       | JVM 线程数量   |
| ThreadsWaiting                 | 个       | JVM 线程数量   |
| ThreadsTimedWaiting            | 个       | JVM 线程数量   |
| ThreadsTerminated              | 个       | JVM 线程数量   |
| numOpenConnections             | 个       | RPC 连接数     |
| FailedSanityCheckException     | 次       | RPC 异常次数   |
| NotServingRegionException      | 次       | RPC 异常次数   |
| OutOfOrderScannerNextException | 次       | RPC 异常次数   |
| RegionMovedException           | 次       | RPC 异常次数   |
| RegionTooBusyException         | 次       | RPC 异常次数   |
| UnknownScannerException        | 次       | RPC 异常次数   |
| numCallsInPriorityQueue        | 个       | RPC 队列请求数 |
| numCallsInReplicationQueue     | 个       | RPC 队列请求数 |
| masterActiveTime               | s        | 进程启动时间   |
| masterStartTime                | s        | 进程启动时间   |

### HBASE-RegionServer

| 指标名称                          | 指标单位 | 指标含义           |
| --------------------------------- | -------- | ------------------ |
| YGC                               | 次       | GC 次数            |
| FGC                               | 次       | GC 次数            |
| FGCT                              | s        | GC 时间            |
| GCT                               | s        | GC 时间            |
| YGCT                              | s        | GC 时间            |
| S0                                | %        | 内存区域占比       |
| E                                 | %        | 内存区域占比       |
| CCS                               | %        | 内存区域占比       |
| S1                                | %        | 内存区域占比       |
| O                                 | %        | 内存区域占比       |
| M                                 | %        | 内存区域占比       |
| LogFatal                          | 次       | JVM 日志数量       |
| LogError                          | 次       | JVM 日志数量       |
| LogWarn                           | 次       | JVM 日志数量       |
| LogInfo                           | 次       | JVM 日志数量       |
| MemNonHeapUsedM                   | MB       | JVM 内存           |
| MemNonHeapCommittedM              | MB       | JVM 内存           |
| MemNonHeapMaxM                    | MB       | JVM 内存           |
| MemHeapUsedM                      | MB       | JVM 内存           |
| MemHeapCommittedM                 | MB       | JVM 内存           |
| MemHeapMaxM                       | MB       | JVM 内存           |
| MemMaxM                           | MB       | JVM 内存           |
| ThreadsNew                        | 个       | JVM 线程数量       |
| ThreadsRunnable                   | 个       | JVM 线程数量       |
| ThreadsBlocked                    | 个       | JVM 线程数量       |
| ThreadsWaiting                    | 个       | JVM 线程数量       |
| ThreadsTimedWaiting               | 个       | JVM 线程数量       |
| ThreadsTerminated                 | 个       | JVM 线程数量       |
| averageRegionSize                 | Byte     | Region 平均大小    |
| regionCount                       | 个       | Region 个数        |
| percentFilesLocalSecondaryRegions | %        | Region 副本本地化  |
| authenticationFailures            | 次       | RPC 认证次数       |
| authenticationSuccesses           | 次       | RPC 认证次数       |
| numOpenConnections                | 个       | RPC 连接数         |
| FailedSanityCheckException        | 次       | RPC 异常次数       |
| NotServingRegionException         | 次       | RPC 异常次数       |
| OutOfOrderScannerNextException    | 次       | RPC 异常次数       |
| RegionMovedException              | 次       | RPC 异常次数       |
| RegionTooBusyException            | 次       | RPC 异常次数       |
| UnknownScannerException           | 次       | RPC 异常次数       |
| numActiveHandler                  | 个       | RPC 句柄数         |
| numCallsInPriorityQueue           | 个       | RPC 队列请求数     |
| numCallsInReplicationQueue        | 个       | RPC 队列请求数     |
| numCallsInGeneralQueue            | 个       | RPC 队列请求数     |
| hlogFileCount                     | 个       | WAL 文件数量       |
| hlogFileSize                      | Byte     | WAL 文件大小       |
| memStoreSize                      | MB       | Memstore 大小      |
| storeCount                        | 个       | Store 个数         |
| storeFileCount                    | 个       | Storefile 个数     |
| storeFileSize                     | MB       | Storefile 大小     |
| flushedCellsSize                  | bytes/s  | 写磁盘速率         |
| Append_mean                       | ms       | 平均延时           |
| Replay_mean                       | ms       | 平均延时           |
| Get_mean                          | ms       | 平均延时           |
| updatesBlockedTime                | ms       | 平均延时           |
| FlushTime_num_ops                 | 次       | RS 写磁盘次数      |
| splitQueueLength                  | 个       | 操作队列请求数     |
| compactionQueueLength             | 个       | 操作队列请求数     |
| flushQueueLength                  | 个       | 操作队列请求数     |
| Replay_num_ops                    | 次       | Replay 操作次数    |
| slowAppendCount                   | 次       | 慢操作次数         |
| slowDeleteCount                   | 次       | 慢操作次数         |
| slowGetCount                      | 次       | 慢操作次数         |
| slowIncrementCount                | 次       | 慢操作次数         |
| slowPutCount                      | 次       | 慢操作次数         |
| splitRequestCount                 | 次       | split 请求         |
| splitSuccessCount                 | 次       | split 请求         |
| blockCacheCount                   | 个       | 缓存块数量         |
| blockCacheHitCount                | 个       | 缓存块数量         |
| blockCacheMissCount               | 个       | 缓存块数量         |
| blockCacheExpressHitPercent       | %        | 读缓存命中率       |
| blockCacheSize                    | Byte     | 缓存块内存占用大小 |
| staticBloomSize                   | Byte     | 索引大小           |
| staticIndexSize                   | Byte     | 索引大小           |
| storeFileIndexSize                | Byte     | 索引大小           |
| receivedBytes                     | bytes/s  | 读写流量           |
| sentBytes                         | bytes/s  | 读写流量           |
| Total                             | 个/s     | 读写请求量         |
| Read                              | 个/s     | 读写请求量         |
| Write                             | 个/s     | 读写请求量         |
| Append_num_ops                    | 个/s     | 读写请求量         |
| mutationsWithoutWALCount          | 个       | mutation 个数       |
| mutationsWithoutWALSize           | Byte     | mutation 大小      |
| regionServerStartTime             | s        | 进程启动时间       |

## HIVE 监控指标

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

## ZOOKEEPER 监控指标

### Zookeeper

| 指标名称                      | 指标单位              | 指标含义                                |
| ----------------------------- | --------------------- | --------------------------------------- |
| YGC                           | 次                    | Young GC 次数                           |
| FGC                           | 次                    | Full GC 次数                            |
| FGCT                          | s                     | Full GC 消耗时间                        |
| GCT                           | s                     | 垃圾回收时间消耗                        |
| YGCT                          | s                     | Young GC 消耗时间                       |
| S0                            | %                     | Survivor 0区内存使用占比               |
| E                             | %                     | Eden 区内存使用占比                     |
| CCS                           | %                     | Compressed class space 区内存使用占比 |
| S1                            | %                     | Survivor 1区内存使用占比               |
| O                             | %                     | Old 区内存使用占比                      |
| M                             | %                     | Metaspace 区内存使用占比                |
| MemNonHeapUsedM               | MB                    | JVM 当前已经使用的 NonHeapMemory 的数量 |
| MemNonHeapCommittedM          | MB                    | JVM 当前已经提交的 NonHeapMemory 的数量 |
| MemHeapUsedM                  | MB                    | JVM 当前已经使用的 HeapMemory 的数量    |
| MemHeapCommittedM             | MB                    | JVM 当前已经提交的 HeapMemory 的数量    |
| MemHeapMaxM                   | MB                    | JVM 配置的 HeapMemory 的数量            |
| MemHeapInitM                  | MB                    | JVM 初始 HeapMem 的数量                 |
| MemNonHeapInitM               | MB                    | JVM 初始 NonHeapMem 的数量              |
| ProcessCpuLoad                | %                     | CPU 利用率                              |
| MaxFileDescriptorCount        | 个                    | 最大文件描述符数                        |
| OpenFileDescriptorCount       | 个                    | 已打开文件描述符数                      |
| zk_max_file_descriptor_count  | 个                    | 最大文件描述符数                        |
| zk_open_file_descriptor_count | 个                    | 已打开文件描述符数                      |
| ProcessCpuTime                | ms                    | CPU 累计使用时间                        |
| Uptime                        | s                     | 进程运行时长                            |
| DaemonThreadCount             | 个                    | Daemon 线程数                           |
| ThreadCount                   | 个                    | 总线程数                                |
| zk_num_alive_connections      | 个                    | 当前连接数                              |
| zk_avg_latency                | ms                    | zk 处理平均延迟                         |
| zk_max_latency                | ms                    | zk 处理最大时延                         |
| zk_min_latency                | ms                    | zk 处理最小时延                         |
| zk_watch_count                | 个                    | zk 的 watch 数目                        |
| zk_znode_count                | 个                    | zk 的 znode 数量                        |
| zk_ephemerals_count           | 个                    | zk 的临时节点数目                       |
| zk_approximate_data_size      | Byte                  | zk 存储数据量                           |
| zk_server_state               | 1：主，0：备，2：单机 | zk 节点类型                             |
| zk_packets_received           | 个/s                  | zk 接收的数据包速率                     |
| zk_packets_sent               | 个/s                  | zk 发送的数据包速率                     |
| zk_outstanding_requests       | 个                    | 排队请求数                              |

## SPARK 监控指标

### SPARK-SparkJobHistory 

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

## PRESTO 监控指标

### PRESTO-概览

| 指标名称                         | 指标单位 | 指标含义           |
| -------------------------------- | -------- | ------------------ |
| Active                           | 个       | 活跃节点数量       |
| Total                            | 个       | 总节点数量         |
| Failed                           | 个       | 失败节点数量       |
| RunningQueries                   | 个       | 正在运行的查询总数 |
| QueuedQueries                    | 个       | 等待状态的查询总数 |
| FailedQueries.OneMinute.Count    | 个/min   | 失败的查询总数     |
| AbandonedQueries.OneMinute.Count | 个/min   | 放弃的查询总数     |
| CanceledQueries.OneMinute.Count  | 个/min   | 取消的查询总数     |
| CompletedQueries.OneMinute.Count | 个/min   | 完成的查询总数     |
| StartedQueries.OneMinute.Count   | 个/min   | 已启动的查询总数   |
| SubmittedQueries.OneMinute.Count | 个/min   | 已提交的查询总数   |
| InputDataSize.OneMinute.Rate     | GB/min   | 输入数据速率       |
| OutputDataSize.OneMinute.Rate    | GB/min   | 输出数据速率       |

### PRESTO-Worker

| 指标名称                      | 指标单位 | 指标含义                                |
| ----------------------------- | -------- | --------------------------------------- |
| YGC                           | 次       | Young GC 次数                           |
| FGC                           | 次       | Full GC 次数                            |
| FGCT                          | s        | Full GC 消耗时间                        |
| GCT                           | s        | 垃圾回收时间消耗                        |
| YGCT                          | s        | Young GC 消耗时间                       |
| S0                            | %        | Survivor 0区内存使用占比               |
| E                             | %        | Eden 区内存使用占比                     |
| CCS                           | %        | Compressed class space 区内存使用占比   |
| S1                            | %        | Survivor 1区内存使用占比               |
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
| ThreadCount                   | 个       | 线程数量                                |
| DaemonThreadCount             | 个       | 后台线程数量                            |
| Uptime                        | s        | 进程运行时间                            |
| StartTime                     | s        | 进程启动时间                            |
| MaxFileDescriptorCount        | 个       | 最大文件描述符数                        |
| OpenFileDescriptorCount       | 个       | 已打开文件描述符数                      |

### PRESTO-Coordinator

| 指标名称                | 指标单位 | 指标含义                                |
| ----------------------- | -------- | --------------------------------------- |
| YGC                     | 次       | Young GC 次数                           |
| FGC                     | 次       | Full GC 次数                            |
| FGCT                    | s        | Full GC 消耗时间                        |
| GCT                     | s        | 垃圾回收时间消耗                        |
| YGCT                    | s        | Young GC 消耗时间                       |
| S0                      | %        | Survivor 0区内存使用占比               |
| E                       | %        | Eden 区内存使用占比                     |
| CCS                     | %        | Compressed class space 区内存使用占比   |
| S1                      | %        | Survivor 1区内存使用占比               |
| O                       | %        | Old 区内存使用占比                      |
| M                       | %        | Metaspace 区内存使用占比                |
| MemNonHeapUsedM         | MB       | JVM 当前已经使用的 NonHeapMemory 的数量 |
| MemNonHeapCommittedM    | MB       | JVM 当前已经提交的 NonHeapMemory 的数量 |
| MemHeapUsedM            | MB       | JVM 当前已经使用的 HeapMemory 的数量    |
| MemHeapCommittedM       | MB       | JVM 当前已经提交的 HeapMemory 的数量    |
| MemHeapMaxM             | MB       | JVM 配置的 HeapMemory 的数量            |
| MemHeapInitM            | MB       | JVM 初始 HeapMem 的数量                 |
| MemNonHeapInitM         | MB       | JVM 初始 NonHeapMem 的数量              |
| PeakThreadCount         | 个       | 峰值线程数                              |
| ThreadCount             | 个       | 线程数量                                |
| DaemonThreadCount       | 个       | 后台线程数量                            |
| Uptime                  | s        | 进程运行时间                            |
| StartTime               | s        | 进程启动时间                            |
| MaxFileDescriptorCount  | 个       | 最大文件描述符数                        |
| OpenFileDescriptorCount | 个       | 已打开文件描述符数                      |
