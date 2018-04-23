加速通道转发数据包时，数据包同时会做 SNAT 和 DNAT，即数据包的源地址和目标地址均修改。如下图所示：
![](https://mc.qcloudimg.com/static/img/3106fdbb4cf4ce0aa3107bd735974a68/image.png)

为了将客户端 IP 传给服务器，加速通道将客户端的 IP 和 port 在转发时放入了自定义的 tcp option 字段。


```
# define TCPOPT_ADDR 200
# define TCPOLEN_ADDR 8 /* |opcode|size|ip+port| = 1 + 1 + 6 */
/*
* insert client ip in tcp option, now only support IPV4,
* must be 4 bytes alignment.
*/
struct ip_vs_tcpo_addr {
__u8 opcode;
__u8 opsize;
__u16 port;
__u32 addr;
};
```
Linux 内核在监听套接字收到三次握手的 ACK 包之后，会从 SYN_REVC 状态进入到
TCP_ESTABLISHED 状 态 。 这 时 内 核 会 调 用 tcp_v4_syn_recv_sock 函 数 。 Hook 函 数
tcp_v4_syn_recv_sock_toa 首先调用原有的 tcp_v4_syn_recv_sock 函数，然后调用 get_toa_data 函数从 TCP OPTION 中提取出 TOA OPTION，并存储在 sk_user_data 字段中。
然后用 inet_getname_toa hook inet_getname，在获取源 IP 地址和端口时，首先调用原来的
inet_getname，然后判断 sk_user_data 是否为空，如果有数据从其中提取真实的 ip 和 port，替换
inet_getname 的返回。
客户端程序在用户态调用 getpeername，返回的 IP 和 port 即为客户端的原始 IP。