加速通道转发数据包时，数据包同时会做 SNAT 和 DNAT，即数据包的源地址和目标地址均修改。源站看到的数据包的源地址是加速通道转发 IP 地址，而并非是客户端的真实 IP。为了将客户端IP传给服务器，加速通道将客户端的 IP 和 Port 在转发时放入了自定义的 tcp option 字段中。如下：


```
#define TCPOPT_ADDR 200
#define TCPOLEN_ADDR 8   /* |opcode|size|ip+port| = 1 + 1 + 6 */

/*
	* insert client ip in tcp option,now only support IPV4,
	* must be 4 bytes alignment.
	*/
	
	struct ip_vs_tcpo_addr{
	    __u8 opcode;
			__u8 opsize;
			__u16 port;
			__u32 addr;
	};
```


Linux 内核在监听套接字收到三次握手的 ACK 包之后，会从 SYN_REVC 状态进入到 TCP_ESTABLISHED 状态。这时内核会调用 tcp_v4_syn_recv_sock 函数。 Hook 函数 tcp_v4_syn_recv_sock_toa首先调用原有的tcp_v4_syn_recv_sock函数，然后调用 get_toa_data 函数从 TCP OPTION 中提取出 TOA OPTION，并存储在 sk_user_data 字段中。再用 inet_getname_toa hook inet_getname，在获取源 IP 地址和端口时，首先调用原来的inet_getname，然后判断 sk_user_data 是否为空，如果有数据从其中提取真实的 IP 和 port，替换 inet_getname 的返回。
服务端程序在用户态调用 getpeername，返回的 IP 和 port 即为客户端的原始 IP。
