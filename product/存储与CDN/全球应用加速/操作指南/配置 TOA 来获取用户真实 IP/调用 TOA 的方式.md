Linux 内核在监听套接字收到三次握手的 ACK 包之后，会从 SYN_REVC 状态进入到 TCP_ESTABLISHED 状态。此时内核会调用 tcp_v4_syn_recv_sock 函数。
Hook 函数 tcp_v4_syn_recv_sock_toa 首先调用原有的 tcp_v4_syn_recv_sock 函数，然后调用 get_toa_data 函数从 TCP OPTION 中提取出 TOA OPTION，并存储在 sk_user_data 字段中。

上述调用完成后会调用 inet_getname_toa hook inet_getname，在获取源 IP 地址和端口时，首先调用原来的 inet_getname，然后判断 sk_user_data 是否为空，如果有数据从其中提取真实的 IP 和 port，替换 inet_getname 的返回。

服务端程序在用户态调用 getpeername，返回的 IP 和 port 即为客户端原始 IP 和 port。
