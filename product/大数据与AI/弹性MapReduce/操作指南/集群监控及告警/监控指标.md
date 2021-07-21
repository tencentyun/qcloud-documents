### 节点-CPU

| 指标名称          | 单位 | 指标含义                       |
| ----------------- | ---- | ------------------------------ |
| CPU使用率_idle    | %    | CPU 空闲时间占比               |
| CPU使用率_irq     | %    | 中断占比                       |
| CPU使用率_nice    | %    | NICE 优先级使用 CPU 占比       |
| CPU使用率_steal   | %    | 虚拟 CPU 等待实际 CPU 时间占比 |
| CPU使用率_softirq | %    | CPU 软中断占比                 |
| CPU使用率_guest   | %    | 运行虚拟处理器所用的时间百分比 |
| CPU使用率_system  | %    | 内核态 CPU 占用比              |
| CPU使用率_user    | %    | 用户态 CPU 占用比              |
| CPU使用率_iowait  | %    | 进程等待 IO CPU 空闲占比       |
| 负载_1m           | 1/s  | 1分钟负载                      |
| 负载_5m           | 1/s  | 5分钟负载                      |
| 负载_15m          | 1/s  | 15分钟负载                     |
| 核数_cpu_count    | 个   | CPU 核数                       |

 

### 节点-MEMORY

| 指标名称                       | 单位 | 指标含义                       |
| ------------------------------ | ---- | ------------------------------ |
| 内存使用情况_MemTotal          | GB   | 内存总量                       |
| 内存使用情况_MemFree           | GB   | 空闲内存总量                   |
| 内存使用情况_MemAvailable      | GB   | 可用内存总量                   |
| 内存使用情况_Buffers           | GB   | BUFFER 缓存占用内存总量        |
| 内存使用情况_Cached            | GB   | 文件缓存占用内存总量           |
| 内存使用情况_SwapCached        | GB   | 匿名页写入交换区内存总量       |
| 内存使用情况_SwapFree          | GB   | 可用交换区总量                 |
| 内存使用情况_AnonPages         | GB   | 未映射内存总量                 |
| 内存使用情况_SwapTotal         | GB   | 交换区总量                     |
| 内存使用情况_Dirty             | GB   | 需要写入磁盘的内存总量         |
| 内存使用情况_Writeback         | GB   | 正在被写回磁盘的内存总量       |
| 内存使用情况_HardwareCorrupted | GB   | 内存硬件故障导致不可用内存总量 |
| 内存使用情况_Shmem             | GB   | 共享内存占用的内存总量         |
| 内存使用占比_available_percent | %    | 可用内存占总内存百分比         |
| 内存使用占比_used_percent      | %    | 已使用内存占总内存百分比       |

### 节点-NETWORK

| 指标名称                             | 单位     | 指标含义                                                     |
| ------------------------------------ | -------- | ------------------------------------------------------------ |
| TCPLISTEN异常_ListenDrops            | 次/s     | 任何原因导致的丢弃传入连接（SYN 包）的次数                   |
| TCPLISTEN异常_ListenOverflows        | 次/s     | 三次握手最后一步完成之后，Accept 队列超过上限的次数          |
| TCPSyncookies_SyncookiesFailed       | 次/s     | 收到携带无效 SYN Cookie 信息的包的个数                       |
| TCPSyncookies_SyncookiesRecv         | 次/s     | 收到携带有效 SYN Cookie 信息的包的个数                       |
| TCPSyncookies_SyncookiesSent         | 次/s     | 使用 SYN Cookie 发送的 SYN/ACK 包个数                        |
| TCP链接异常Abort_TCPAbortOnTimeout   | 次/s     | 因各种计时器（RTO/PTO/keepalive）的重传次数超过上限而关闭连接的 |
| TCP链接异常Abort_TCPAbortOnData      | 次/s     | socket 收到未知数据导致被关闭的次数                          |
| TCP链接异常Abort_TCPAbortOnClose     | 次/s     | 用户态程序在缓冲区内还有数据时关闭 socket 的次数             |
| TCP链接异常Abort_TCPAbortOnMemory    | 次/s     | 因内存问题关闭连接的次数                                     |
| TCP链接异常Abort_TCPAbortOnLinger    | 次/s     | 关闭后，在徘徊状态中止的连接的次数                           |
| TCP链接异常Abort_TCPAbortFailed      | 次/s     | 尝试结束连接失败的次数                                       |
| TCP建立链接_ActiveOpens              | 个/s     | 主动建立 TCP 连接数量                                        |
| TCP建立链接_CurrEstab                | 个/s     | 当前已建立 TCP 连接数量                                      |
| TCP建立链接_PassiveOpens             | 个/s     | 被动建立 TCP 连接数量                                        |
| TCP建立链接_AttemptFails             | 个/s     | 建立连接失败数量                                             |
| TCP建立链接_EstabResets              | 个/s     | 连接被 REST 的数量                                           |
| TCP数据包_InSegs                     | 个/s     | 收到的数据包个数，包括有错误的包个数                         |
| TCP数据包_OutSegs                    | 个/s     | 发送的数据包个数                                             |
| TCP数据包_RetransSegs                | 个/s     | TCP 接收报文数量                                             |
| TCP数据包_InErrs                     | 个/s     | 重传的包个数                                                 |
| TCP数据包_OutRsts                    | 个/s     | 发出 RST 包个数                                              |
| TCP重传率_RetransSegsRate            | %        | TCP 层重传率                                                 |
| TCP重传率_ResetRate                  | %        | RESET 发送频率                                               |
| TCP重传率_InErrRate                  | %        | 错误包占比                                                   |
| TCP TIME-WAIT_TW                     | 个/s     | 经过正常的超时结束 TIME_WAIT 状态的 socket 数量              |
| TCP TIME-WAIT_TWKilled               | 个/s     | 通过 tcp_tw_recycle 机制结束 TIME_WAIT  状态的 socket 数量   |
| TCP TIME-WAIT_TWRecycled             | 个/s     | 通过 tcp_tw_reuse 机制结束 TIME_WAIT 状态的 socket 数量      |
| TCP RTO_TCPTimeouts                  | 次/s     | RTO timer 第一次超时次数                                     |
| TCP RTO_TCPSpuriousRTOs              | 次/s     | 通过 F-RTO 机制发现的虚假超时次数                            |
| TCP RTO_TCPLossProbes                | 次/s     | Probe Timeout(PTO) 导致发送 Tail Loss Probe(TLP) 包的次数    |
| TCP RTO_TCPLossProbeRecovery         | 次/s     | 丢失包刚好被 TLP 探测包修复的次数                            |
| TCP RTO_TCPRenoRecoveryFail          | 次/s     | 先进入 Recovery 阶段，然后又 RTO 的次数，对端不支持 SACK 选项 |
| TCP RTO_TCPSackRecoveryFail          | 次/s     | 先进入 Recovery 阶段，然后又 RTO 的次数，对端支持 SACK 选项  |
| TCP RTO_TCPRenoFailures              | 次/s     | 先进 TCP_CA_Disorder 阶段，然后又 RTO 超时的次数，对端不支持 SACK 选项 |
| TCP RTO_TCPSackFailures              | 次/s     | 先进 TCP_CA_Disorder 阶段，然后又 RTO 超时的次数，对端支持 SACK 选项 |
| TCP RTO_TCPLossFailures              | 次/s     | 先进 TCP_CA_Loss 阶段，然后又 RTO 超时的次数                 |
| TCP RTO常数_RtoAlgorithm             | 1/s      | 转发未答复对象的延时的算法的数                               |
| TCP RTO常数_RtoMax                   | 1/s      | TCP 延迟重发的最大值                                         |
| TCP RTO常数_RtoMin                   | 1/s      | TCP 延迟重发的最小值                                         |
| TCP重传_TCPLostRetransmit            | 次/s     | 丢失重传 SKB 的次数                                          |
| TCP重传_TCPFastRetrans               | 次/s     | 快重传 SKB 次数                                              |
| TCP重传_TCPForwardRetrans            | 次/s     | 一般重传 SKB 次数                                            |
| TCP重传_TCPSlowStartRetrans          | 次/s     | 成功慢启动重传 SKB 数量                                      |
| TCP重传_TCPRetransFail               | 次/s     | 尝试重传失败次数                                             |
| UDP数据报_OutDatagrams               | 个/s     | 发送 UDP 数据报文数量                                        |
| UDP数据报_InDatagrams                | 个/s     | 接收 UDP 数据报文数量                                        |
| 网卡收发数据速率_eth0-receive_bytes  | MB/s     | 网卡接收数据量                                               |
| 网卡收发数据速率_eth0-transmit_bytes | MB/s     | 网卡发送数据量                                               |
| 网卡数据包率_eth0-receive_drop       | packet/s | 网卡接收丢弃数据量                                           |
| 网卡数据包率_eth0-receive_errs       | packet/s | 网卡接收异常数量                                             |
| 网卡数据包率_eth0-transmit_drop      | packet/s | 网卡发送丢弃数据量                                           |
| 网卡数据包率_eth0-transmit_errs      | packet/s | 网卡发送异常数据量                                           |
| 网卡数据包率_eth0-transmit_packetsl  | packet/s | 网卡发送包数量                                               |
| TCP套接字_TCP_inuse                  | 个       | 在使用（正在侦听）的 TCP 套接字数量                          |
| TCP套接字_TCP_orphan                 | 个       | 等待关闭的 TCP 连接数                                        |
| TCP套接字_TCP_tw                     | 个       | 待销毁的 TCP socket 数                                       |
| TCP套接字_TCP_alloc                  | 个       | 已分配（已建立、已申请到 sk_buff）的 TCP 套接字数量          |
| TCP链接状态_ESTABLISHED              | 个       | Established 状态的 TCP 链接数量                              |
| TCP链接状态_SYN-SENT                 | 个       | SYN-SENT 状态的 TCP 链接数量                                 |
| TCP链接状态_SYN-RECV                 | 个       | SYN-RECV 状态的 TCP 链接数量                                 |
| TCP链接状态_CLOSE                    | 个       | CLOSE 状态的 TCP 链接数量                                    |
| TCP链接状态_CLOSE-WAIT               | 个       | CLOSE-WAIT 状态的 TCP 链接数量                               |
| TCP链接状态_LISTEN                   | 个       | LISTEN 状态的 TCP 链接数量                                   |


### 节点-磁盘

| 指标名称                         | 单位 | 指标含义                          |
| -------------------------------- | ---- | --------------------------------- |
| 设备读写速率_read_all            | MB/s | 每秒读数据量                      |
| 设备读写速率_write_all           | MB/s | 每秒写数据量                      |
| 设备IOPS_all                     | 次   | 当前设备上正在进行的 IO 操作      |
| IO操作时间_read_all              | ms   | 平均每次设备 I/O 读操作的等待时间 |
| IO操作时间_write_all             | ms   | 平均每次设备 I/O 写操作的等待时间 |
| IO操作时间_io_all                | ms   | 平均每次 IO 请求的处理时间        |
| 设备读写请求QPS_read_all         | 次/s | 读操作 QPS                        |
| 设备读写请求QPS_write_all        | 次/s | 写操作 QPS                        |
| 设备读写请求QPS_merged_read_all  | 次/s | 合并读操作 QPS                    |
| 设备读写请求QPS_merged_write_all | 次/s | 合并写操作 QPS                    |
| IO设备使用率_all                 | %    | 磁盘繁忙程度                      |
| 磁盘空间_free_all                | GB   | 磁盘剩余总空间                    |
| 磁盘空间使用率_used_all          | GB   | 磁盘已使用总空间                  |
| 磁盘空间_total_all               | GB   | 磁盘总空间                        |
| 磁盘空间使用率_used_all          | %    | 磁盘总使用率                      |
| INODES值_free_all                | 个   | 磁盘剩余 INODES 数量              |
| INODES值_total_all               | 个   | 磁盘 INODES 总数量                |
| INODES使用率_used_all            | %    | 磁盘 INODES 使用率                |

 

### 节点-文件句柄

| 指标名称           | 单位 | 指标含义           |
| ------------------ | ---- | ------------------ |
| 文件句柄_allocated | 个   | 已分配文件句柄数量 |
| 文件句柄_maximum   | 个   | 最大文件句柄数量   |

### 节点-PROCESS

| 指标名称                              | 单位    | 指标含义           |
| ------------------------------------- | ------- | ------------------ |
| 系统中断_intr_total                   | 次/s    | 系统中断数量       |
| 系统上下文切换_context_switches_total | 次/s    | 系统上下文切换数量 |
| 系统进程_forks_total                  | 个/s    | 系统新建进程数量   |
| 系统进程_procs_running                | 个/s    | 系统运行进程数量   |
| 系统进程_procs_blocked                | 个/s    | 系统阻塞进程数量   |
| 系统进程_procs_total                  | 个/s    | 系统总进程数量     |
| Agent版本_AgentVersionl               | version | agent 的版本       |

 

 
