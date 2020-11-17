### 节点-CPU

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

### 节点-MEMORY

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

### 节点-NETWORK

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

### 节点-磁盘

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

### 节点-文件句柄

| 指标名称  | 单位 | 指标含义           |
| --------- | ---- | ------------------ |
| allocated | 个   | 已分配文件句柄数量 |
| maximum   | 个   | 最大文件句柄数量   |

### 节点-PROCESS

| 指标名称               | 单位    | 指标含义           |
| ---------------------- | ------- | ------------------ |
| intr_total             | 次/s    | 系统中断数量       |
| context_switches_total | 次/s    | 系统上下文切换数量 |
| forks_total            | 个/s    | 系统新建进程数量   |
| procs_running          | 个/s    | 系统运行进程数量   |
| procs_blocked          | 个/s    | 系统阻塞进程数量   |
| procs_total            | 个/s    | 系统总进程数量     |
| AgentVersionl          | version | agent 的版本       |
