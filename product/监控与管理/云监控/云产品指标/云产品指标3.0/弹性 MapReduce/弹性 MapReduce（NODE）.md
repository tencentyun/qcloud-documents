## 命名空间

Namespace=QCE/TXMR_NODE

## 监控指标

### 主机-CPU

| 指标英文名           | 指标中文名         | 单位    | 指标含义                       | 维度                          |
| -------------------- | ------------------ | ------- | ------------------------------ | ----------------------------- |
| NodeCpuIdle          | CPU 使用率_idle    | %       | CPU IDLE 时间占比              | id4nodecpu、<br/>host4nodecpu |
| NodeCpuIrq           | CPU 使用率_irq     | %       | 中断占比                       | id4nodecpu、<br/>host4nodecpu |
| NodeCpuNice          | CPU 使用率_nice    | %       | NICE 优先级使用 CPU 占比       | id4nodecpu、<br/>host4nodecpu |
| NodeCpuSteal         | CPU 使用率_steal   | %       | 虚拟 CPU 等待实际 CPU 时间占比 | id4nodecpu、<br/>host4nodecpu |
| NodeCpuSoftirq       | CPU 使用率_softirq | %       | CPU 软中断占比                 | id4nodecpu、<br/>host4nodecpu |
| NodeCpuGuest         | CPU 使用率_guest   | %       | 运行虚拟处理器所用的时间百分比 | id4nodecpu、<br/>host4nodecpu |
| NodeCpuSystem        | CPU 使用率_system  | %       | 内核态 CPU 占用比              | id4nodecpu、<br/>host4nodecpu |
| NodeCpuUser          | CPU 使用率_user    | %       | 用户态 CPU 占用比              | id4nodecpu、<br/>host4nodecpu |
| NodeCpuIowait        | CPU 使用率_iowait  | %       | 进程等待 IO CPU 空闲占比       | id4nodecpu、<br/>host4nodecpu |
| NodeCpuLoad1m        | 负载_1m            | 1分钟/s | 1分钟负载                      | id4nodecpu、<br/>host4nodecpu |
| NodeCpuLoad5m        | 负载_5m            | -       | 5分钟负载                      | id4nodecpu、<br/>host4nodecpu |
| NodeCpuLoad15m       | 负载_15m           | -       | 15分钟负载                     | id4nodecpu、<br/>host4nodecpu |
| NodeCpuCountCpuCount | 核数\_cpu_count    | 个      | CPU 核数                       | id4nodecpu、<br/>host4nodecpu |

### 主机-内存

| 指标英文名                         | 指标中文名                       | 单位 | 指标含义                       | 维度                                |
| ---------------------------------- | -------------------------------- | ---- | ------------------------------ | ----------------------------------- |
| NodeMemMemtotal                    | 内存使用情况_MemTotal            | GB   | 内存总量                       | host4nodememory、<br/>id4nodememory |
| NodeMemMemfree                     | 内存使用情况_MemFree             | GB   | 空闲内存总量                   | host4nodememory、<br/>id4nodememory |
| NodeMemBuffers                     | 内存使用情况_Buffers             | GB   | BUFFER 缓存占用内存总量        | host4nodememory、<br/>id4nodememory |
| NodeMemCached                      | 内存使用情况_Cached              | GB   | 文件缓存占用内存总量           | host4nodememory、<br/>id4nodememory |
| NodeMemSwapcached                  | 内存使用情况_SwapCached          | GB   | 匿名页写入交换区内存总量       | host4nodememory、<br/>id4nodememory |
| NodeMemSwapfree                    | 内存使用情况_SwapFree            | GB   | 可用交换区总量                 | host4nodememory、<br/>id4nodememory |
| NodeMemAnonpages                   | 内存使用情况_AnonPages           | GB   | 未映射内存总量                 | host4nodememory、<br/>id4nodememory |
| NodeMemSwaptotal                   | 内存使用情况_SwapTotal           | GB   | 交换区总量                     | host4nodememory、<br/>id4nodememory |
| NodeMemDirty                       | 内存使用情况_Dirty               | GB   | 需要写入磁盘的内存总量         | host4nodememory、<br/>id4nodememory |
| NodeMemWriteback                   | 内存使用情况_Writeback           | GB   | 正在被写回磁盘的内存总量       | host4nodememory、<br/>id4nodememory |
| NodeMemHard<br>warecorrupted       | 内存使用情况_HardwareCorrupted   | GB   | 内存硬件故障导致不可用内存总量 | host4nodememory、<br/>id4nodememory |
| NodeMemShmem                       | 内存使用情况_Shmem               | GB   | 共享内存占用的内存总量         | host4nodememory、<br/>id4nodememory |
| NodeMemPercen<br>tAvailablePercent | 内存使用占比\_available\_percent | %    | 可用内存占总内存百分比         | host4nodememory、<br/>id4nodememory |
| NodeMemPercent<br>UsedPercent      | 内存使用占比\_used\_percent      | %    | 已使用内存占总内存百分比       | host4nodememory、<br/>id4nodememory |

### 主机-网络

| 指标英文名                                    | 指标中文名                                | 单位     | 指标含义                                                     | 维度                                  |
| --------------------------------------------- | ----------------------------------------- | -------- | ------------------------------------------------------------ | ------------------------------------- |
| NodeNetworkTcp<br>ListenExtListendrops        | TCPLISTEN<br>异常_ListenDrops            | 次/s     | 任何原因导致的丢弃传入连接（SYN 包）的次数                   | host4nodenetwork、<br>id4nodenetwork  |
| NodeNetworkTcpListen<br>ExtListenoverflows    | TCPLISTEN<br>异常_ListenOverflows        | 次/s     | 三次握手最后一步完成之后，Accept 队列超过上限的次数          | host4nodenetwork、<br/>id4nodenetwork |
| NodeNetworkTcpSyncookies<br>Syncookiesfailed  | TCPSyncookies_Syn<br/>cookiesFailed       | 次/s     | 收到携带无效 SYN Cookie 信息的包的个数                       | host4nodenetwork、<br/>id4nodenetwork |
| NodeNetworkTcpSyncookies<br>Syncookiesrecv    | TCPSyncookies_Syn<br/>cookiesRecv         | 次/s     | 收到携带有效 SYN Cookie 信息的包的个数                       | host4nodenetwork、<br/>id4nodenetwork |
| NodeNetworkTcpSyncookies<br>Syncookiessent    | TCPSyncookies_Syn<br/>cookiesSent         | 次/s     | 使用 SYN Cookie 发送的 SYN/ACK 包个数                        | host4nodenetwork、<br/>id4nodenetwork |
| NodeNetworkTcpAbort<br>Tcpabortontimeout      | TCP 链接异常 Abort_TCPAbort<br>OnTimeout  | 次/s     | 因各种计时器（RTO/PTO/keepalive）的重传次数超过上限而关闭连接的 | host4nodenetwork、<br/>id4nodenetwork |
| NodeNetworkTcpAbort<br>Tcpabortondata         | TCP 链接异常 Abort_TCPAbort<br>OnData     | 次/s     | socket 收到未知数据导致被关闭的次数                          | host4nodenetwork、<br/>id4nodenetwork |
| NodeNetworkTcpAbort<br>Tcpabortonclose        | TCP 链接异常 Abort_TCPAbort<br>OnClose    | 次/s     | 用户态程序在缓冲区内还有数据时关闭 socket 的次数             | host4nodenetwork、<br/>id4nodenetwork |
| NodeNetworkTcpAbort<br>Tcpabortonmemory       | TCP 链接异常 Abort_TCPAbort<br>OnMemory   | 次/s     | 因内存问题关闭连接的次数                                     | host4nodenetwork、<br/>id4nodenetwork |
| NodeNetworkTcpAbort<br>Tcpabortonlinger       | TCP 链接异常 Abort_TCPAbort<br>OnLinger   | 次/s     | 关闭后，在徘徊状态中止的连接的次数                           | host4nodenetwork、<br/>id4nodenetwork |
| NodeNetworkTcpAbort<br>Tcpabortfailed         | TCP 链接异常 Abort_TCPAbortFailed         | 次/s     | 尝试结束连接失败的次数                                       | host4nodenetwork、<br/>id4nodenetwork |
| NodeNetworkTcpState<br>Activeopens            | TCP 建立链接<br/>_ActiveOpens             | 个/s     | 主动建立 TCP 连接数量                                        | host4nodenetwork、<br/>id4nodenetwork |
| NodeNetworkTcp<br>StateCurrestab              | TCP 建立链接<br/>_CurrEstab               | 个/s     | 当前已建立 TCP 连接数量                                      | host4nodenetwork、<br/>id4nodenetwork |
| NodeNetworkTcpState<br>Passiveopens           | TCP 建立链接<br/>_PassiveOpens            | 个/s     | 被动建立 TCP 连接数量                                        | host4nodenetwork、<br/>id4nodenetwork |
| NodeNetworkTcp<br>StateAttemptfails           | TCP 建立链接<br/>_AttemptFails            | 个/s     | 建立连接失败数量                                             | host4nodenetwork、<br/>id4nodenetwork |
| NodeNetworkTcp<br>StateEstabresets            | TCP 建立链接<br/>_EstabResets             | 个/s     | 连接被 REST 的数量                                           | host4nodenetwork、<br/>id4nodenetwork |
| NodeNetworkTcp<br>PacketStatInsegs            | TCP 数据包<br/>_InSegs                    | 个/s     | 收到的数据包个数，包括有错误的包个数                         | host4nodenetwork、<br/>id4nodenetwork |
| NodeNetworkTcp<br/>PacketStatOutsegs          | TCP 数据包<br/>_OutSegs                   | 个/s     | 发送的数据包个数                                             | host4nodenetwork、<br/>id4nodenetwork |
| NodeNetworkTcp<br>PacketStatRetranssegs       | TCP 数据包<br/>_RetransSegs               | 个/s     | TCP 接收报文数量                                             | host4nodenetwork、<br/>id4nodenetwork |
| NodeNetworkTcp<br>PacketStatInerrs            | TCP 数据包<br/>_InErrs                    | 个/s     | 重传的包个数                                                 | host4nodenetwork、<br/>id4nodenetwork |
| NodeNetworkTcp<br>PacketStatOutrsts           | TCP 数据包<br/>_OutRsts                   | 个/s     | 发出 RST 包个数                                              | host4nodenetwork、<br/>id4nodenetwork |
| NodeNetworkTcpPacketRate<br>Retranssegsrate   | TCP 重传率<br/>_RetransSegsRate           | %        | TCP 层重传率                                                 | host4nodenetwork、<br/>id4nodenetwork |
| NodeNetworkTcp<br>PacketRateResetrate         | TCP 重传率<br/>_ResetRate                 | %        | RESET 发送频率                                               | host4nodenetwork、<br/>id4nodenetwork |
| NodeNetworkTcpPacket<br>RateInerrrate         | TCP 重传率<br/>_InErrRate                 | %        | 错误包占比                                                   | host4nodenetwork、<br/>id4nodenetwork |
| NodeNetworkTcpTimeWaitTw                      | TCPTIME-WAIT_TW                           | 个/s     | 经过正常的超时结束 TIME_WAIT 状态的 socket 数量              | host4nodenetwork、<br/>id4nodenetwork |
| NodeNetworkTcp<br>TimeWaitTwkilled            | TCPTIME-WAIT_TWKilled                     | 个/s     | 通过 tcp_tw_recycle 机制结束 TIME_WAIT 状态的 socket 数量    | host4nodenetwork、<br/>id4nodenetwork |
| NodeNetworkTcpTime<br>WaitTwrecycled          | TCPTIME-WAIT_TWRecycled                   | 个/s     | 通过 tcp_tw_reuse 机制结束 TIME_WAIT 状态的 socket 数量      | host4nodenetwork、<br/>id4nodenetwork |
| NodeNetworkTcpRtoStat<br>Tcptimeouts          | TCPRTO_TCPTimeouts                        | 次/s     | RTO timer 第一次超时次数                                     | host4nodenetwork、<br/>id4nodenetwork |
| NodeNetworkTcpRtoStat<br>Tcpspuriousrtos      | TCPRTO_TCPSpur<br/>iousRTOs               | 次/s     | 通过 F-RTO 机制发现的虚假超时次数                            | host4nodenetwork、<br/>id4nodenetwork |
| NodeNetworkTcpRtoStat<br>Tcplossprobes        | TCPRTO_TCPLoss<br/>Probes                 | 次/s     | Probe Timeout(PTO) 导致发送 Tail Loss Probe(TLP) 包的次数    | host4nodenetwork、<br/>id4nodenetwork |
| NodeNetworkTcpRtoStat<br>Tcplossproberecovery | TCPRTO_TCPLoss<br/>ProbeRecovery          | 次/s     | 丢失包刚好被 TLP 探测包修复的次数                            | host4nodenetwork、<br/>id4nodenetwork |
| NodeNetworkTcpRtoStat<br>Tcprenorecoveryfail  | TCPRTO_TCPReno<br>RecoveryFail            | 次/s     | 先进入 Recovery 阶段，然后又 RTO 的次数，对端不支持 SACK 选项 | host4nodenetwork、<br/>id4nodenetwork |
| NodeNetworkTcpRtoStat<br>Tcprenorecoveryfail  | TCPRTO_TCPReno<br>RecoveryFail            | 次/s     | 先进入 Recovery 阶段，然后又 RTO 的次数，对端支持 SACK 选项  | host4nodenetwork、<br/>id4nodenetwork |
| NodeNetworkTcpRtoStat<br>Tcprenofailures      | TCPRTO_TCPReno<br>Failures                | 次/s     | 先进 TCP_CA_Disorder 阶段，然后又 RTO 超时的次数，对端不支持 SACK 选项 | host4nodenetwork、<br/>id4nodenetwork |
| NodeNetworkTcpRtoStat<br>Tcpsackfailures      | TCPRTO_TCPSack<br>Failures                | 次/s     | 先进 TCP_CA_Disorder 阶段，然后又 RTO 超时的次数，对端支持 SACK 选项 | host4nodenetwork、<br/>id4nodenetwork |
| NodeNetworkTcp<br>RtoStatTcplossfailures      | TCPRTO_TCPLoss<br>Failures                | 次/s     | 先进 TCP_CA_Loss 阶段，然后又 RTO 超时的次数                 | host4nodenetwork、<br/>id4nodenetwork |
| NodeNetworkTcpRto<br>ConstRtoalgorithm        | TCPRTO <br/>常数_RtoAlgorithm             | 1/s      | 转发未答复对象的延时的算法的数                               | host4nodenetwork、<br/>id4nodenetwork |
| NodeNetworkTcp<br>RtoConstRtomax              | TCPRTO <br/>常数_RtoMax                   | 1/s      | TCP 延迟重发的最大值                                         | host4nodenetwork、<br/>id4nodenetwork |
| NodeNetworkTcp<br>RtoConstRtomin              | TCPRTO <br/>常数_RtoMin                   | 1/s      | TCP 延迟重发的最小值                                         | host4nodenetwork、<br/>id4nodenetwork |
| NodeNetworkTcpRetrans<br>Tcplostretransmit    | TCP 重传<br/>_TCPLostRetransmit           | 次/s     | 丢失重传 SKB 的次数                                          | host4nodenetwork、<br/>id4nodenetwork |
| NodeNetworkTcpRetrans<br>Tcpfastretrans       | TCP 重传<br/>_TCPFastRetrans              | 次/s     | 快重传 SKB 次数                                              | host4nodenetwork、<br/>id4nodenetwork |
| NodeNetworkTcpRetrans<br>Tcpforwardretrans    | TCP 重传<br/>_TCPForwardRetrans           | 次/s     | 一般重传 SKB 次数                                            | host4nodenetwork、<br/>id4nodenetwork |
| NodeNetworkTcpRetrans<br>Tcpslowstartretrans  | TCP 重传<br/>_TCPSlowStart<br>Retrans     | 次/s     | 成功慢启动重传 SKB 数量                                      | host4nodenetwork、<br/>id4nodenetwork |
| NodeNetworkTcpRetrans<br>Tcpretransfail       | TCP 重传<br/>_TCPRetransFail              | 次/s     | 尝试重传失败次数                                             | host4nodenetwork、<br/>id4nodenetwork |
| NodeNetworkUdp<br>DgIndatagrams               | UDP 数据报<br/>_InDatagrams               | 个/s     | 发送 UDP 数据报文数量                                        | host4nodenetwork、<br/>id4nodenetwork |
| INodeNetworkUdpDg<br>Outdatagrams             | UDP 数据报<br/>_OutDatagrams              | 个/s     | 接收 UDP 数据报文数量                                        | host4nodenetwork、<br/>id4nodenetwork |
| NodeNetworkRwBytes<br>Eth0TransmitBytes       | 网卡收发数据速率<br>\_eth0-transmit_bytes | MB/s     | 网卡发送数据量                                               | host4nodenetwork、<br/>id4nodenetwork |
| NodeNetworkPackets<br>Eth0ReceiveDrop         | 网卡数据包率<br>\_eth0-receive_drop       | packet/s | 网卡接收丢弃数据量                                           | host4nodenetwork、<br/>id4nodenetwork |
| NodeNetworkPackets<br>Eth0ReceiveErrs         | 网卡数据包率<br>\_eth0-receive_errs       | packet/s | 网卡接收异常数量                                             | host4nodenetwork、<br/>id4nodenetwork |
| NodeNetworkPackets<br>Eth0TransmitDrop        | 网卡数据包率<br>\_eth0-transmit_drop      | packet/s | 网卡发送丢弃数据量                                           | host4nodenetwork、<br/>id4nodenetwork |
| NodeNetworkPackets<br>Eth0TransmitErrs        | 网卡数据包率<br>\_eth0-transmit_errs      | packet/s | 网卡发送异常数据量                                           | host4nodenetwork、<br/>id4nodenetwork |
| NodeNetworkPackets<br>Eth0TransmitPackets     | 网卡数据包率<br>\_eth0_transmit_packets   | packet/s | 网卡发送包数量                                               | host4nodenetwork、<br/>id4nodenetwork |
| NodeNetworkTcp<br>SocketTcpInuse              | TCP 套接字<br/>\_TCP_inuse                | 个       | 在使用（正在侦听）的 TCP 套接字数量                          | host4nodenetwork、<br/>id4nodenetwork |
| NodeNetworkTcp<br>SocketTcpOrphan             | TCP套接字<br/>\_TCP_orphan                | 个       | 等待关闭的 TCP 连接数                                        | host4nodenetwork、<br/>id4nodenetwork |
| NodeNetwork<br>TcpSocketTcpTw                 | TCP 套接字<br/>\_TCP_tw                   | 个       | 待销毁的 TCP socket 数                                       | host4nodenetwork、<br/>id4nodenetwork |
| NodeNetworkTcp<br>SocketSocketsUsed           | TCP 套接字<br/>\_sockets_used             | 个       | 使用 CP 套接字的用户数                                       | host4nodenetwork、<br/>id4nodenetwork |
| NodeNetworkTcp<br>SocketTcpAlloc              | TCP 套接字<br/>\_TCP_alloc                | 个       | 已分配（已建立、已申请到 sk_buff）的 TCP 套接字数量          | host4nodenetwork、<br/>id4nodenetwork |
| NodeNetworkTcp<br>ConnectionStateEstablished  | TCP 链接状态<br/>_ESTABLISHED             | 个       | Established 状态的 TCP 链接数量                              | host4nodenetwork、<br/>id4nodenetwork |
| NodeNetworkTcp<br>ConnectionStateSynSent      | TCP 链接状态<br/>_SYN-SENT                | 个       | SYN-SENT 状态的 TCP 链接数量                                 | host4nodenetwork、<br/>id4nodenetwork |
| NodeNetworkTcp<br>ConnectionStateSynRecv      | TCP 链接状态<br/>\_SYN-RECV               | 个       | SYN-RECV 状态的 TCP 链接数量                                 | host4nodenetwork、<br/>id4nodenetwork |
| NodeNetworkTcp<br>ConnectionStateClose        | TCP 链接状态<br/>\_CLOSE                  | 个       | CLOSE 状态的 TCP 链接数量                                    | host4nodenetwork、<br/>id4nodenetwork |
| NodeNetworkTcp<br>ConnectionStateCloseWait    | TCP 链接状态<br/>\_CLOSE-WAIT             | 个       | CLOSE-WAIT 状态的 TCP 链接数量                               | host4nodenetwork、<br/>id4nodenetwork |
| NodeNetworkTcp<br>ConnectionStateListen       | TCP 链接状态<br/>\_LISTEN                 | 个       | LISTEN 状态的 TCP 链接数量                                   | host4nodenetwork、<br/>id4nodenetwork |
| NodeNetworkTcp<br>ConnectionStateClosing      | TCP 链接状态<br/>\_CLOSING                | 个       | CLOSEING 状态的 TCP 链接数量                                 | host4nodenetwork、<br/>id4nodenetwork |

### 主机-Filehandle 

| 指标英文名            | 指标中文名         | 单位 | 指标含义           |                                             |
| --------------------- | ------------------ | ---- | ------------------ | ------------------------------------------- |
| NodeFdFilefdAllocated | 文件句柄_allocated | 个   | 已分配文件句柄数量 | host4nodefilehandle、<br>id4nodefilehandle  |
| NodeFdFilefdMaximum   | 文件句柄_maximum   | 个   | 最大文件句柄数量   | host4nodefilehandle、<br/>id4nodefilehandle |

### 主机-PROCESS

| 指标英文名                           | 指标中文名                             | 单位    | 指标含义           | 维度                                  |
| ------------------------------------ | -------------------------------------- | ------- | ------------------ | ------------------------------------- |
| NodeIntrIntrTotal                    | 系统中断\_intr_total                   | 次/s    | 系统中断数量       | host4nodeprocess、<br>id4nodeprocess  |
| NodeSwitchesContext<br>SwitchesTotal | 系统上下文切换\_context_switches_total | 次/s    | 系统上下文切换数量 | host4nodeprocess、<br/>id4nodeprocess |
| NodeProcsForksTotal                  | 系统进程\_forks_total                  | 个/s    | 系统新建进程数量   | host4nodeprocess、<br/>id4nodeprocess |
| NodeProcsProcsRunning                | 系统进程\_procs_running                | 个/s    | 系统运行进程数量   | host4nodeprocess、<br/>id4nodeprocess |
| NodeProcsProcsBlocked                | 系统进程\_procs_blocked                | 个/s    | 系统阻塞进程数量   | host4nodeprocess、<br/>id4nodeprocess |
| NodeProcsProcsTotal                  | 系统进程\_procs_total                  | 个/s    | 系统总进程数量     | host4nodeprocess、<br/>id4nodeprocess |
| NodeAgentVersion<br>Agentversion     | Agent 版本\_AgentVersion               | version | agent 的版本       | host4nodeprocess、<br/>id4nodeprocess |

## 各维度对应参数总览

| 参数名称                       | 维度名称            | 维度解释                      | 格式                                                         |
| ------------------------------ | ------------------- | ----------------------------- | ------------------------------------------------------------ |
| Instances.N.Dimensions.0.Name  | id4nodecpu          | EMR 实例 ID 的维度名称        | 输入 String 类型维度名称：id4nodecpu                         |
| Instances.N.Dimensions.0.Value | id4nodecpu          | EMR 实例具体 ID               | 输入具体实例 ID，例如：emr-abcdef88                          |
| Instances.N.Dimensions.1.Name  | host4nodecpu        | EMR 实例中节点 IP 的维度名称  | 输入String 类型维度名称：host4nodecpu                        |
| Instances.N.Dimensions.1.Name  | host4nodecpu        | EMR 实例中具体节点 IP         | 输入具体节点  IP ，可从控制台获取，登录 [腾讯云 MapReduce 控制台](https://console.cloud.tencent.com/emr) > 单击实例 > 集群资源 > 资源管理 > 节点内网 IP。也可通过 [查询节点信息](https://cloud.tencent.com/document/product/589/41707) API 获取。 |
| Instances.N.Dimensions.0.Name  | id4nodememory       | EMR  实例 ID 的维度名称       | 输入 String 类型维度名称：id4nodememory                      |
| Instances.N.Dimensions.0.Value | id4nodememory       | EMR  实例具体 ID              | 输入具体实例  ID，例如：emr-abcdef88                         |
| Instances.N.Dimensions.1.Name  | host4nodememory     | EMR  实例中节点 IP 的维度名称 | 输入String 类型维度名称：host4nodememory                     |
| Instances.N.Dimensions.1.Name  | host4nodememory     | EMR  实例中具体节点 IP        | 输入具体节点  IP ，可从控制台获取，登录 [腾讯云 MapReduce 控制台](https://console.cloud.tencent.com/emr) > 单击实例 > 集群资源 > 资源管理 > 节点内网 IP。也可通过 [查询节点信息](https://cloud.tencent.com/document/product/589/41707) API 获取。 |
| Instances.N.Dimensions.0.Name  | id4nodenetwork      | EMR  实例 ID 的维度名称       | 输入 String 类型维度名称： id4nodenetwork                    |
| Instances.N.Dimensions.0.Value | id4nodenetwork      | EMR  实例具体 ID              | 输入具体实例 ID，例如：emr-abcdef88                          |
| Instances.N.Dimensions.1.Name  | host4nodenetwork    | EMR 实例中节点 IP 的维度名称  | 输入String 类型维度名称：host4nodenetwork                    |
| Instances.N.Dimensions.1.Name  | host4nodenetwork    | EMR 实例中具体节点 IP         | 输入具体节点  IP ，可从控制台获取，登录 [腾讯云 MapReduce 控制台](https://console.cloud.tencent.com/emr) > 单击实例 > 集群资源 > 资源管理 > 节点内网 IP。也可通过 [查询节点信息](https://cloud.tencent.com/document/product/589/41707) API 获取。 |
| Instances.N.Dimensions.0.Name  | id4nodefilehandle   | EMR 实例 ID 的维度名称        | 输入 String 类型维度名称：id4nodefilehandle                  |
| Instances.N.Dimensions.0.Value | id4nodefilehandle   | EMR 实例具体 ID               | 输入具体实例  ID，例如：emr-abcdef88                         |
| Instances.N.Dimensions.1.Name  | host4nodefilehandle | EMR 实例中节点 IP 的维度名称  | 输入String 类型维度名称：host4nodefilehandle                 |
| Instances.N.Dimensions.1.Name  | host4nodefilehandle | EMR 实例中具体节点 IP         | 输入具体节点  IP ，可从控制台获取，登录 [腾讯云 MapReduce 控制台](https://console.cloud.tencent.com/emr) > 单击实例 > 集群资源 > 资源管理 > 节点内网 IP。也可通过 [查询节点信息](https://cloud.tencent.com/document/product/589/41707) API 获取。 |
| Instances.N.Dimensions.0.Name  | id4nodeprocess      | EMR 实例 ID 的维度名称        | 输入 String 类型维度名称： id4nodeprocess                    |
| Instances.N.Dimensions.0.Value | id4nodeprocess      | EMR 实例具体 ID               | 输入具体实例  ID，例如：emr-abcdef88                         |
| Instances.N.Dimensions.1.Name  | host4nodeprocess    | EMR 实例中节点 IP 的维度名称  | 输入String 类型维度名称：host4nodeprocess                    |
| Instances.N.Dimensions.1.Name  | host4nodeprocess    | EMR 实例中具体节点 IP         | 输入具体节点  IP ，可从控制台获取，登录 [腾讯云 MapReduce 控制台](https://console.cloud.tencent.com/emr) > 单击实例 > 集群资源 > 资源管理 > 节点内网 IP。也可通过 [查询节点信息](https://cloud.tencent.com/document/product/589/41707) API 获取。 |


## 入参说明

弹性 MapReduce（NODE）支持以下五种维度组合的查询方式，五种入参取值如下： 

**1. 查询主机-CPU  的指标监控数据，入参取值如下：**
&Namespace=QCE/TXMR_NODE
&Instances.N.Dimensions.0.Name=id4nodecpu
&Instances.N.Dimensions.0.Value=EMR 实例 ID 
&Instances.N.Dimensions.1.Name=host4nodecpu
&Instances.N.Dimensions.1.Value=EMR 实例中具体节点 IP

**2. 查询主机-内存 的指标监控数据，入参取值如下：**
&Namespace=QCE/TXMR_NODE
&Instances.N.Dimensions.0.Name=id4nodememory
&Instances.N.Dimensions.0.Value=EMR 实例 ID
&Instances.N.Dimensions.1.Name=host4nodememory
&Instances.N.Dimensions.1.Value=EMR 实例中具体节点 IP 

**3. 查询主机-网络的指标监控数据，入参取值如下：**
&Namespace=QCE/TXMR_NODE
&Instances.N.Dimensions.0.Name=id4nodenetwork
&Instances.N.Dimensions.0.Value=EMR 实例 ID 
&Instances.N.Dimensions.1.Name=host4nodenetwork
&Instances.N.Dimensions.1.Value=EMR 实例中具体节点 IP

**4. 查询主机-Filehandle  的指标监控数据，入参取值如下：**
&Namespace=QCE/TXMR_NODE
&Instances.N.Dimensions.0.Name=id4nodefilehandle
&Instances.N.Dimensions.0.Value=EMR 实例 ID 
&Instances.N.Dimensions.1.Name=host4nodefilehandle
&Instances.N.Dimensions.1.Value=EMR 实例中具体节点 IP

**5. 查询主机-PROCESS  的指标监控数据，入参取值如下：**
&Namespace=QCE/TXMR_NODE
&Instances.N.Dimensions.0.Name= id4nodeprocess
&Instances.N.Dimensions.0.Value=EMR 实例 ID 
&Instances.N.Dimensions.1.Name=host4nodeprocess
&Instances.N.Dimensions.1.Value=EMR 实例中具体节点 IP
