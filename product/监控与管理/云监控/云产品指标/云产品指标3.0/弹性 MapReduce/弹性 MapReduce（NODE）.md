## 命名空间

Namespace=QCE/TXMR_NODE

## 监控指标

### 主机-CPU

| 指标英文名           | 指标中文名         | 单位 | 指标含义                       | 维度                      |
| :------------------- | :----------------- | :--- | :----------------------------- | :------------------------ |
| NodeCpuIdle          | CPU 使用率_idle    | %    | CPU IDLE 时间占比              | id4nodecpu、 host4nodecpu |
| NodeCpuIrq           | CPU 使用率_irq     | %    | 中断占比                       | id4nodecpu、 host4nodecpu |
| NodeCpuNice          | CPU 使用率_nice    | %    | NICE 优先级使用 CPU 占比       | id4nodecpu、 host4nodecpu |
| NodeCpuSteal         | CPU 使用率_steal   | %    | 虚拟 CPU 等待实际 CPU 时间占比 | id4nodecpu、 host4nodecpu |
| NodeCpuSoftirq       | CPU 使用率_softirq | %    | CPU 软中断占比                 | id4nodecpu、 host4nodecpu |
| NodeCpuGuest         | CPU 使用率_guest   | %    | 运行虚拟处理器所用的时间百分比 | id4nodecpu、 host4nodecpu |
| NodeCpuSystem        | CPU 使用率_system  | %    | 内核态 CPU 占用比              | id4nodecpu、 host4nodecpu |
| NodeCpuUser          | CPU 使用率_user    | %    | 用户态 CPU 占用比              | id4nodecpu、 host4nodecpu |
| NodeCpuIowait        | CPU 使用率_iowait  | %    | 进程等待 IO CPU 空闲占比       | id4nodecpu、 host4nodecpu |
| NodeCpuLoad1m        | 负载_1m            | -    | 1分钟负载                      | id4nodecpu、 host4nodecpu |
| NodeCpuLoad5m        | 负载_5m            | -    | 5分钟负载                      | id4nodecpu、 host4nodecpu |
| NodeCpuLoad15m       | 负载_15m           | -    | 15分钟负载                     | id4nodecpu、 host4nodecpu |
| NodeCpuCountCpuCount | 核数_cpu_count     | 个   | CPU 核数                       | id4nodecpu、 host4nodecpu |

### 主机-内存

| 指标英文名                          | 指标中文名                     | 单位 | 指标含义                       | 维度                            |
| :---------------------------------- | :----------------------------- | :--- | :----------------------------- | :------------------------------ |
| NodeMemMemtotal                     | 内存使用情况_MemTotal          | GB   | 内存总量                       | host4nodememory、 id4nodememory |
| NodeMemMemfree                      | 内存使用情况_MemFree           | GB   | 空闲内存总量                   | host4nodememory、 id4nodememory |
| NodeMemBuffers                      | 内存使用情况_Buffers           | GB   | BUFFER 缓存占用内存总量        | host4nodememory、 id4nodememory |
| NodeMemCached                       | 内存使用情况_Cached            | GB   | 文件缓存占用内存总量           | host4nodememory、 id4nodememory |
| NodeMemSwapcached                   | 内存使用情况_SwapCached        | GB   | 匿名页写入交换区内存总量       | host4nodememory、 id4nodememory |
| NodeMemSwapfree                     | 内存使用情况_SwapFree          | GB   | 可用交换区总量                 | host4nodememory、 id4nodememory |
| NodeMemAnonpages                    | 内存使用情况_AnonPages         | GB   | 未映射内存总量                 | host4nodememory、 id4nodememory |
| NodeMemSwaptotal                    | 内存使用情况_SwapTotal         | GB   | 交换区总量                     | host4nodememory、 id4nodememory |
| NodeMemDirty                        | 内存使用情况_Dirty             | GB   | 需要写入磁盘的内存总量         | host4nodememory、 id4nodememory |
| NodeMemWriteback                    | 内存使用情况_Writeback         | GB   | 正在被写回磁盘的内存总量       | host4nodememory、 id4nodememory |
| NodeMemHard<br/>warecorrupted       | 内存使用情况_HardwareCorrupted | GB   | 内存硬件故障导致不可用内存总量 | host4nodememory、 id4nodememory |
| NodeMemShmem                        | 内存使用情况_Shmem             | GB   | 共享内存占用的内存总量         | host4nodememory、 id4nodememory |
| NodeMemPercent<br/>AvailablePercent | 内存使用占比_available_percent | %    | 可用内存占总内存百分比         | host4nodememory、 id4nodememory |
| NodeMemPercent<br/>UsedPercent      | 内存使用占比_used_percent      | %    | 已使用内存占总内存百分比       | host4nodememory、 id4nodememory |

### 主机-网络

| 指标英文名                                     | 指标中文名                            | 单位  | 指标含义                                                     | 维度                              |
| :--------------------------------------------- | :------------------------------------ | :---- | :----------------------------------------------------------- | :-------------------------------- |
| NodeNetworkTcp<br/>ListenExtListendrops        | TCPLISTEN 异常_ListenDrops            | 次/秒 | 任何原因导致的丢弃传入连接（SYN 包）的次数                   | host4nodenetwork、 id4nodenetwork |
| NodeNetworkTcpListen<br/>ExtListenoverflows    | TCPLISTEN 异常_ListenOverflows        | 次/秒 | 三次握手最后一步完成之后，Accept 队列超过上限的次数          | host4nodenetwork、 id4nodenetwork |
| NodeNetworkTcpSyncookies<br/>Syncookiesfailed  | TCPSyncookies_Syn cookiesFailed       | 次/秒 | 收到携带无效 SYN Cookie 信息的包的个数                       | host4nodenetwork、 id4nodenetwork |
| NodeNetworkTcpSyncookies<br/>Syncookiesrecv    | TCPSyncookies_Syn cookiesRecv         | 次/秒 | 收到携带有效 SYN Cookie 信息的包的个数                       | host4nodenetwork、 id4nodenetwork |
| NodeNetworkTcpSyncookies<br/>Syncookiessent    | TCPSyncookies_Syn cookiesSent         | 次/秒 | 使用 SYN Cookie 发送的 SYN/ACK 包个数                        | host4nodenetwork、 id4nodenetwork |
| NodeNetworkTcpAbort<br/>Tcpabortontimeout      | TCP 链接异常 Abort_TCPAbort OnTimeout | 次/秒 | 因各种计时器（RTO/PTO/keepalive）的重传次数超过上限而关闭连接的 | host4nodenetwork、 id4nodenetwork |
| NodeNetworkTcpAbort<br/>Tcpabortondata         | TCP 链接异常 Abort_TCPAbort OnData    | 次/秒 | socket 收到未知数据导致被关闭的次数                          | host4nodenetwork、 id4nodenetwork |
| NodeNetworkTcpAbort<br/>Tcpabortonclose        | TCP 链接异常 Abort_TCPAbort OnClose   | 次/秒 | 用户态程序在缓冲区内还有数据时关闭 socket 的次数             | host4nodenetwork、 id4nodenetwork |
| NodeNetworkTcpAbort<br/>Tcpabortonmemory       | TCP 链接异常 Abort_TCPAbort OnMemory  | 次/秒 | 因内存问题关闭连接的次数                                     | host4nodenetwork、 id4nodenetwork |
| NodeNetworkTcpAbort<br/>Tcpabortonlinger       | TCP 链接异常 Abort_TCPAbort OnLinger  | 次/秒 | 关闭后，在徘徊状态中止的连接的次数                           | host4nodenetwork、 id4nodenetwork |
| NodeNetworkTcpAbort<br/>Tcpabortfailed         | TCP 链接异常 Abort_TCPAbortFailed     | 次/秒 | 尝试结束连接失败的次数                                       | host4nodenetwork、 id4nodenetwork |
| NodeNetworkTcpState<br/>Activeopens            | TCP 建立链接 _ActiveOpens             | 个/s  | 主动建立 TCP 连接数量                                        | host4nodenetwork、 id4nodenetwork |
| NodeNetworkTcp<br/>StateCurrestab              | TCP 建立链接 _CurrEstab               | 个/s  | 当前已建立 TCP 连接数量                                      | host4nodenetwork、 id4nodenetwork |
| NodeNetworkTcpState<br/>Passiveopens           | TCP 建立链接 _PassiveOpens            | 个/s  | 被动建立 TCP 连接数量                                        | host4nodenetwork、 id4nodenetwork |
| NodeNetworkTcp<br/>StateAttemptfails           | TCP 建立链接 _AttemptFails            | 个/s  | 建立连接失败数量                                             | host4nodenetwork、 id4nodenetwork |
| NodeNetworkTcp<br/>StateEstabresets            | TCP 建立链接 _EstabResets             | 个/s  | 连接被 REST 的数量                                           | host4nodenetwork、 id4nodenetwork |
| NodeNetworkTcp<br/>PacketStatInsegs            | TCP 数据包 _InSegs                    | 个/s  | 收到的数据包个数，包括有错误的包个数                         | host4nodenetwork、 id4nodenetwork |
| NodeNetworkTcp<br/>PacketStatOutsegs           | TCP 数据包 _OutSegs                   | 个/s  | 发送的数据包个数                                             | host4nodenetwork、 id4nodenetwork |
| NodeNetworkTcp<br/>PacketStatRetranssegs       | TCP 数据包 _RetransSegs               | 个/s  | TCP 接收报文数量                                             | host4nodenetwork、 id4nodenetwork |
| NodeNetworkTcp<br/>PacketStatInerrs            | TCP 数据包 _InErrs                    | 个/s  | 重传的包个数                                                 | host4nodenetwork、 id4nodenetwork |
| NodeNetworkTcp<br/>PacketStatOutrsts           | TCP 数据包 _OutRsts                   | 个/s  | 发出 RST 包个数                                              | host4nodenetwork、 id4nodenetwork |
| NodeNetworkTcpPacketRate Retranssegsrate       | TCP 重传率 _RetransSegsRate           | %     | TCP 层重传率                                                 | host4nodenetwork、 id4nodenetwork |
| NodeNetworkTcp<br/>PacketRateResetrate         | TCP 重传率 _ResetRate                 | %     | RESET 发送频率                                               | host4nodenetwork、 id4nodenetwork |
| NodeNetworkTcpPacket<br/>RateInerrrate         | TCP 重传率 _InErrRate                 | %     | 错误包占比                                                   | host4nodenetwork、 id4nodenetwork |
| NodeNetworkTcp<br/>TimeWaitTw                  | TCPTIME-WAIT_TW                       | 个/s  | 经过正常的超时结束 TIME_WAIT 状态的 socket 数量              | host4nodenetwork、 id4nodenetwork |
| NodeNetworkTcp<br/>TimeWaitTwkilled            | TCPTIME-WAIT_TWKilled                 | 个/s  | 通过 tcp_tw_recycle 机制结束 TIME_WAIT 状态的 socket 数量    | host4nodenetwork、 id4nodenetwork |
| NodeNetworkTcpTime<br/>WaitTwrecycled          | TCPTIME-WAIT_TWRecycled               | 个/s  | 通过 tcp_tw_reuse 机制结束 TIME_WAIT 状态的 socket 数量      | host4nodenetwork、 id4nodenetwork |
| NodeNetworkTcpRtoStat<br/>Tcptimeouts          | TCPRTO_TCPTimeouts                    | 次/秒 | RTO timer 第一次超时次数                                     | host4nodenetwork、 id4nodenetwork |
| NodeNetworkTcpRtoStat<br/>Tcpspuriousrtos      | TCPRTO_TCPSpur iousRTOs               | 次/秒 | 通过 F-RTO 机制发现的虚假超时次数                            | host4nodenetwork、 id4nodenetwork |
| NodeNetworkTcpRtoStat<br/>Tcplossprobes        | TCPRTO_TCPLoss Probes                 | 次/秒 | Probe Timeout(PTO) 导致发送 Tail Loss Probe(TLP) 包的次数    | host4nodenetwork、 id4nodenetwork |
| NodeNetworkTcpRtoStat<br/>Tcplossproberecovery | TCPRTO_TCPLoss ProbeRecovery          | 次/秒 | 丢失包刚好被 TLP 探测包修复的次数                            | host4nodenetwork、 id4nodenetwork |
| NodeNetworkTcpRtoStat<br/>Tcprenorecoveryfail  | TCPRTO_TCPReno RecoveryFail           | 次/秒 | 先进入 Recovery 阶段，然后又 RTO 的次数，对端不支持 SACK 选项 | host4nodenetwork、 id4nodenetwork |
| NodeNetworkTcpRtoStat<br/>Tcprenorecoveryfail  | TCPRTO_TCPReno RecoveryFail           | 次/秒 | 先进入 Recovery 阶段，然后又 RTO 的次数，对端支持 SACK 选项  | host4nodenetwork、 id4nodenetwork |
| NodeNetworkTcpRtoStat<br/>Tcprenofailures      | TCPRTO_TCPReno Failures               | 次/秒 | 先进 TCP_CA_Disorder 阶段，然后又 RTO 超时的次数，对端不支持 SACK 选项 | host4nodenetwork、 id4nodenetwork |
| NodeNetworkTcpRtoStat<br/>Tcpsackfailures      | TCPRTO_TCPSack Failures               | 次/秒 | 先进 TCP_CA_Disorder 阶段，然后又 RTO 超时的次数，对端支持 SACK 选项 | host4nodenetwork、 id4nodenetwork |
| NodeNetworkTcp<br/>RtoStatTcplossfailures      | TCPRTO_TCPLoss Failures               | 次/秒 | 先进 TCP_CA_Loss 阶段，然后又 RTO 超时的次数                 | host4nodenetwork、 id4nodenetwork |
| NodeNetworkTcpRto<br/>ConstRtoalgorithm        | TCPRTO 常数_RtoAlgorithm              | 1/s   | 转发未答复对象的延时的算法的数                               | host4nodenetwork、 id4nodenetwork |
| NodeNetworkTcp<br/>RtoConstRtomax              | TCPRTO 常数_RtoMax                    | 1     | TCP 延迟重发的最大值                                         | host4nodenetwork、 id4nodenetwork |
| NodeNetworkTcp<br/>RtoConstRtomin              | TCPRTO 常数_RtoMin                    | 1     | TCP 延迟重发的最小值                                         | host4nodenetwork、 id4nodenetwork |
| NodeNetworkTcpRetrans<br/>Tcplostretransmit    | TCP 重传 _TCPLostRetransmit           | 次/秒 | 丢失重传 SKB 的次数                                          | host4nodenetwork、 id4nodenetwork |
| NodeNetworkTcpRetrans<br/>Tcpfastretrans       | TCP 重传 _TCPFastRetrans              | 次/秒 | 快重传 SKB 次数                                              | host4nodenetwork、 id4nodenetwork |
| NodeNetworkTcpRetrans<br/>Tcpforwardretrans    | TCP 重传 _TCPForwardRetrans           | 次/秒 | 一般重传 SKB 次数                                            | host4nodenetwork、 id4nodenetwork |
| NodeNetworkTcpRetrans<br/>Tcpslowstartretrans  | TCP 重传 _TCPSlowStart Retrans        | 次/秒 | 成功慢启动重传 SKB 数量                                      | host4nodenetwork、 id4nodenetwork |
| NodeNetworkTcpRetrans<br/>Tcpretransfail       | TCP 重传 _TCPRetransFail              | 次/秒 | 尝试重传失败次数                                             | host4nodenetwork、 id4nodenetwork |
| NodeNetworkUdp<br/>DgIndatagrams               | UDP 数据报 _InDatagrams               | 个/s  | 发送 UDP 数据报文数量                                        | host4nodenetwork、 id4nodenetwork |
| INodeNetworkUdpDg<br/>Outdatagrams             | UDP 数据报 _OutDatagrams              | 个/s  | 接收 UDP 数据报文数量                                        | host4nodenetwork、 id4nodenetwork |
| NodeNetworkRwBytes<br/> Eth0TransmitBytes      | 网卡收发数据速率 _eth0-transmit_bytes | MB/s  | 网卡发送数据量                                               | host4nodenetwork、 id4nodenetwork |
| NodeNetworkPackets<br/>Eth0ReceiveDrop         | 网卡数据包率 _eth0-receive_drop       | 个/s  | 网卡接收丢弃数据量                                           | host4nodenetwork、 id4nodenetwork |
| NodeNetworkPackets<br/>Eth0ReceiveErrs         | 网卡数据包率 _eth0-receive_errs       | 个/s  | 网卡接收异常数量                                             | host4nodenetwork、 id4nodenetwork |
| NodeNetworkPackets<br/>Eth0TransmitDrop        | 网卡数据包率 _eth0-transmit_drop      | 个/s  | 网卡发送丢弃数据量                                           | host4nodenetwork、 id4nodenetwork |
| NodeNetworkPackets<br/>Eth0TransmitErrs        | 网卡数据包率 _eth0-transmit_errs      | 个/s  | 网卡发送异常数据量                                           | host4nodenetwork、 id4nodenetwork |
| NodeNetworkPackets<br/>Eth0TransmitPackets     | 网卡数据包率 _eth0_transmit_packet    | 个/s  | 网卡发送包数量                                               | host4nodenetwork、 id4nodenetwork |
| NodeNetworkTcp<br/>SocketTcpInuse              | TCP 套接字 _TCP_inuse                 | 个    | 在使用（正在侦听）的 TCP 套接字数量                          | host4nodenetwork、 id4nodenetwork |
| NodeNetworkTcp<br/> SocketTcpOrphan            | TCP套接字 _TCP_orphan                 | 个    | 等待关闭的 TCP 连接数                                        | host4nodenetwork、 id4nodenetwork |
| NodeNetwork<br/>TcpSocketTcpTw                 | TCP 套接字 _TCP_tw                    | 个    | 待销毁的 TCP socket 数                                       | host4nodenetwork、 id4nodenetwork |
| NodeNetworkTcp<br/>SocketSocketsUsed           | TCP 套接字 _sockets_used              | 个    | 使用 CP 套接字的用户数                                       | host4nodenetwork、 id4nodenetwork |
| NodeNetworkTcp<br/>SocketTcpAlloc              | TCP 套接字 _TCP_alloc                 | 个    | 已分配（已建立、已申请到 sk_buff）的 TCP 套接字数量          | host4nodenetwork、 id4nodenetwork |
| NodeNetworkTcp<br/>ConnectionStateEstablished  | TCP 链接状态 _ESTABLISHED             | 个    | Established 状态的 TCP 链接数量                              | host4nodenetwork、 id4nodenetwork |
| NodeNetworkTcp<br/>ConnectionStateSynSent      | TCP 链接状态 _SYN-SENT                | 个    | SYN-SENT 状态的 TCP 链接数量                                 | host4nodenetwork、 id4nodenetwork |
| NodeNetworkTcp<br/> ConnectionStateSynRecv     | TCP 链接状态 _SYN-RECV                | 个    | SYN-RECV 状态的 TCP 链接数量                                 | host4nodenetwork、 id4nodenetwork |
| NodeNetworkTcp<br/>ConnectionStateClose        | TCP 链接状态 _CLOSE                   | 个    | CLOSE 状态的 TCP 链接数量                                    | host4nodenetwork、 id4nodenetwork |
| NodeNetworkTcp ConnectionStateCloseWait        | TCP 链接状态 _CLOSE-WAIT              | 个    | CLOSE-WAIT 状态的 TCP 链接数量                               | host4nodenetwork、 id4nodenetwork |
| NodeNetworkTcp<br/>ConnectionStateListen       | TCP 链接状态 _LISTEN                  | 个    | LISTEN 状态的 TCP 链接数量                                   | host4nodenetwork、 id4nodenetwork |
| NodeNetworkTcp<br/>ConnectionStateClosing      | TCP 链接状态 _CLOSING                 | 个    | CLOSEING 状态的 TCP 链接数量                                 | host4nodenetwork、 id4nodenetwork |
| NodeNetworkRwBytes<br/>Eth0ReceiveBytes        | 网卡收发数据速率_eth0-receive_bytes   | MB/s  | -                                                            | host4nodenetwork、id4nodenetwork  |

### 磁盘

| 指标英文名                            | 指标中文名                       | 指标单位 | 指标含义                               | 维度                       |
| :------------------------------------ | :------------------------------- | :------- | -------------------------------------- | :------------------------- |
| NodeDiskInodesFreeAll                 | INODES_free_all                  | 个       | 磁盘剩余 INODES 数量                   | host4nodedisk、id4nodedisk |
| NodeDiskInodesTotalAll                | INODES_total_all                 | 个       | 磁盘总 INODES 数量                     | host4nodedisk、id4nodedisk |
| NodeDiskInodes<br/>UsedPercentUsedAll | INODES使用率_used_all            | %        | 磁盘 INODES 使用率                     | host4nodedisk、id4nodedisk |
| NodeDiskIoNowAll                      | 设备IOPS_all                     | 次/秒    | 设备IOPS，当前设备上正在进行的 IO 操作 | host4nodedisk、id4nodedisk |
| NodeDiskIoOps<br/>MergedReadAll       | 设备读写请求QPS_merged_read_all  | MB/s     | 设备读写速率，每秒读数据量             | host4nodedisk、id4nodedisk |
| NodeDiskIoOps<br/>MergedWriteAll      | 设备读写请求QPS_merged_write_all | MB/s     | 设备读写速率，每秒写数据量             | host4nodedisk、id4nodedisk |
| NodeDiskIoOpsReadAll                  | 设备读写请求QPS_read_all         | 次/秒    | 读操作 QPS                             | host4nodedisk、id4nodedisk |
| NodeDiskIoOpsWriteAll                 | 设备读写请求QPS_write_all        | 次/秒    | 写操作 QPS                             | host4nodedisk、id4nodedisk |
| NodeDiskIoRateReadAll                 | 设备读写速率_read_all            | MB/s     | 合并读操作 QPS                         | host4nodedisk、id4nodedisk |
| NodeDiskIoRateWriteAll                | 设备读写速率_write_all           | MB/s     | 合并写操作 QPS                         | host4nodedisk、id4nodedisk |
| NodeDiskIoTimeIoAll                   | IO操作时间_io_all                | ms       | 平均每次 IO 请求的处理时间             | host4nodedisk、id4nodedisk |
| NodeDiskIoTimeReadAll                 | IO操作时间_read_all              | ms       | 平均每次设备 I/O 读操作的等待时间      | host4nodedisk、id4nodedisk |
| NodeDiskIoTimeWriteAll                | IO操作时间_write_all             | ms       | 平均每次设备 I/O 写操作的等待时间      | host4nodedisk、id4nodedisk |
| NodeDiskSpace<br/>GbAvaliableAll      | 磁盘空间_avaliable_all           | GB       | 磁盘可用存储空间(非特权用户)           | host4nodedisk、id4nodedisk |
| NodeDiskSpaceGbFreeAll                | 磁盘空间_free_all                | GB       | 磁盘空闲存储空间                       | host4nodedisk、id4nodedisk |
| NodeDiskSpaceGbTotalAll               | 磁盘空间_total_all               | GB       | 磁盘总存储空间                         | host4nodedisk、id4nodedisk |
| NodeDiskSpace<br/>UsedPercentUsedAll  | 磁盘空间使用率_used_all          | %        | 磁盘空间使用率                         | host4nodedisk、id4nodedisk |
| NodeDiskUtilPercentAll                | IO设备使用率_all                 | %        | IO 设备使用率，磁盘繁忙程度            | host4nodedisk、id4nodedisk |

### 主机-Filehandle

| 指标英文名            | 指标中文名         | 单位 | 指标含义           |                                         |
| :-------------------- | :----------------- | :--- | :----------------- | :-------------------------------------- |
| NodeFdFilefdAllocated | 文件句柄_allocated | 个   | 已分配文件句柄数量 | host4nodefilehandle、 id4nodefilehandle |
| NodeFdFilefdMaximum   | 文件句柄_maximum   | 个   | 最大文件句柄数量   | host4nodefilehandle、 id4nodefilehandle |

### 主机-PROCESS

| 指标英文名                        | 指标中文名                            | 单位    | 指标含义           | 维度                              |
| :-------------------------------- | :------------------------------------ | :------ | :----------------- | :-------------------------------- |
| NodeIntrIntrTotal                 | 系统中断_intr_total                   | 次/秒   | 系统中断数量       | host4nodeprocess、 id4nodeprocess |
| NodeSwitchesContext SwitchesTotal | 系统上下文切换_context_switches_total | 次/秒   | 系统上下文切换数量 | host4nodeprocess、 id4nodeprocess |
| NodeProcsForksTotal               | 系统进程_forks_total                  | 个      | 系统新建进程数量   | host4nodeprocess、 id4nodeprocess |
| NodeProcsProcsRunning             | 系统进程_procs_running                | 个      | 系统运行进程数量   | host4nodeprocess、 id4nodeprocess |
| NodeProcsProcsBlocked             | 系统进程_procs_blocked                | 个      | 系统阻塞进程数量   | host4nodeprocess、 id4nodeprocess |
| NodeProcsProcsTotal               | 系统进程_procs_total                  | 个      | 系统总进程数量     | host4nodeprocess、 id4nodeprocess |
| NodeAgentVersion<br>Agentversion  | Agent 版本_AgentVersion               | version | agent 的版本       | host4nodeprocess、 id4nodeprocess |

## 各维度对应参数总览

| 参数名称                       | 维度名称            | 维度解释                     | 格式                                                         |
| :----------------------------- | :------------------ | :--------------------------- | :----------------------------------------------------------- |
| Instances.N.Dimensions.0.Name  | id4nodecpu          | EMR 实例 ID 的维度名称       | 输入 String 类型维度名称：id4nodecpu                         |
| Instances.N.Dimensions.0.Value | id4nodecpu          | EMR 实例具体 ID              | 输入具体实例 ID，例如：emr-abcdef88                          |
| Instances.N.Dimensions.1.Name  | host4nodecpu        | EMR 实例中节点 IP 的维度名称 | 输入String 类型维度名称：host4nodecpu                        |
| Instances.N.Dimensions.1.Name  | host4nodecpu        | EMR 实例中具体节点 IP        | 输入具体节点 IP ，可从控制台获取，登录 [腾讯云 MapReduce 控制台](https://console.cloud.tencent.com/emr) > 单击实例 > 集群资源 > 资源管理 > 节点内网 IP。也可通过 [查询节点信息](https://cloud.tencent.com/document/product/589/41707) API 获取。 |
| Instances.N.Dimensions.0.Name  | id4nodememory       | EMR 实例 ID 的维度名称       | 输入 String 类型维度名称：id4nodememory                      |
| Instances.N.Dimensions.0.Value | id4nodememory       | EMR 实例具体 ID              | 输入具体实例 ID，例如：emr-abcdef88                          |
| Instances.N.Dimensions.1.Name  | host4nodememory     | EMR 实例中节点 IP 的维度名称 | 输入String 类型维度名称：host4nodememory                     |
| Instances.N.Dimensions.1.Name  | host4nodememory     | EMR 实例中具体节点 IP        | 输入具体节点 IP ，可从控制台获取，登录 [腾讯云 MapReduce 控制台](https://console.cloud.tencent.com/emr) > 单击实例 > 集群资源 > 资源管理 > 节点内网 IP。也可通过 [查询节点信息](https://cloud.tencent.com/document/product/589/41707) API 获取。 |
| Instances.N.Dimensions.0.Name  | id4nodenetwork      | EMR 实例 ID 的维度名称       | 输入 String 类型维度名称： id4nodenetwork                    |
| Instances.N.Dimensions.0.Value | id4nodenetwork      | EMR 实例具体 ID              | 输入具体实例 ID，例如：emr-abcdef88                          |
| Instances.N.Dimensions.1.Name  | host4nodenetwork    | EMR 实例中节点 IP 的维度名称 | 输入String 类型维度名称：host4nodenetwork                    |
| Instances.N.Dimensions.1.Name  | host4nodenetwork    | EMR 实例中具体节点 IP        | 输入具体节点 IP ，可从控制台获取，登录 [腾讯云 MapReduce 控制台](https://console.cloud.tencent.com/emr) > 单击实例 > 集群资源 > 资源管理 > 节点内网 IP。也可通过 [查询节点信息](https://cloud.tencent.com/document/product/589/41707) API 获取。 |
| Instances.N.Dimensions.0.Name  | id4nodefilehandle   | EMR 实例 ID 的维度名称       | 输入 String 类型维度名称：id4nodefilehandle                  |
| Instances.N.Dimensions.0.Value | id4nodefilehandle   | EMR 实例具体 ID              | 输入具体实例 ID，例如：emr-abcdef88                          |
| Instances.N.Dimensions.1.Name  | host4nodefilehandle | EMR 实例中节点 IP 的维度名称 | 输入String 类型维度名称：host4nodefilehandle                 |
| Instances.N.Dimensions.1.Name  | host4nodefilehandle | EMR 实例中具体节点 IP        | 输入具体节点 IP ，可从控制台获取，登录 [腾讯云 MapReduce 控制台](https://console.cloud.tencent.com/emr) > 单击实例 > 集群资源 > 资源管理 > 节点内网 IP。也可通过 [查询节点信息](https://cloud.tencent.com/document/product/589/41707) API 获取。 |
| Instances.N.Dimensions.0.Name  | id4nodeprocess      | EMR 实例 ID 的维度名称       | 输入 String 类型维度名称： id4nodeprocess                    |
| Instances.N.Dimensions.0.Value | id4nodeprocess      | EMR 实例具体 ID              | 输入具体实例 ID，例如：emr-abcdef88                          |
| Instances.N.Dimensions.1.Name  | host4nodeprocess    | EMR 实例中节点 IP 的维度名称 | 输入String 类型维度名称：host4nodeprocess                    |
| Instances.N.Dimensions.1.Name  | host4nodeprocess    | EMR 实例中具体节点 IP        | 输入具体节点 IP ，可从控制台获取，登录 [腾讯云 MapReduce 控制台](https://console.cloud.tencent.com/emr) > 单击实例 > 集群资源 > 资源管理 > 节点内网 IP。也可通过 [查询节点信息](https://cloud.tencent.com/document/product/589/41707) API 获取。 |
| Instances.N.Dimensions.0.Name  | id4nodedisk         | EMR 实例 ID 的维度名称       | 输入 String 类型维度名称： id4nodedisk                       |
| Instances.N.Dimensions.0.Value | id4nodedisk         | EMR 实例具体 ID              | 输入具体实例 ID，例如：emr-abcdef88                          |
| Instances.N.Dimensions.1.Name  | host4nodedisk       | EMR 实例中节点 IP 的维度名称 | 输入String 类型维度名称：host4nodedisk                       |
| Instances.N.Dimensions.1.Name  | host4nodedisk       | EMR 实例中具体节点 IP        | 输入具体节点 IP ，可从控制台获取，登录 [腾讯云 MapReduce 控制台](https://console.cloud.tencent.com/emr) > 单击实例 > 集群资源 > 资源管理 > 节点内网 IP。也可通过 [查询节点信息](https://cloud.tencent.com/document/product/589/41707) API 获取。 |

## 入参说明

弹性 MapReduce（NODE）支持以下五种维度组合的查询方式，五种入参取值如下：

**1. 查询主机-CPU 的指标监控数据，入参取值如下：**
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

**4. 查询主机-磁盘的指标监控数据，入参取值如下：**
&Namespace=QCE/TXMR_NODE
&Instances.N.Dimensions.0.Name= id4nodedisk
&Instances.N.Dimensions.0.Value=EMR 实例 ID
&Instances.N.Dimensions.1.Name=host4nodedisk
&Instances.N.Dimensions.1.Value=EMR 实例中具体节点 IP

**5. 查询主机-Filehandle 的指标监控数据，入参取值如下：**
&Namespace=QCE/TXMR_NODE
&Instances.N.Dimensions.0.Name=id4nodefilehandle
&Instances.N.Dimensions.0.Value=EMR 实例 ID
&Instances.N.Dimensions.1.Name=host4nodefilehandle
&Instances.N.Dimensions.1.Value=EMR 实例中具体节点 IP

**6. 查询主机-PROCESS 的指标监控数据，入参取值如下：**
&Namespace=QCE/TXMR_NODE
&Instances.N.Dimensions.0.Name= id4nodeprocess
&Instances.N.Dimensions.0.Value=EMR 实例 ID
&Instances.N.Dimensions.1.Name=host4nodeprocess
&Instances.N.Dimensions.1.Value=EMR 实例中具体节点 IP
