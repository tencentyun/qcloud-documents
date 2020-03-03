加速通道转发数据包时，数据包同时会做 SNAT 和 DNAT，即数据包的源地址和目标地址均修改。源站看到的数据包的源地址是加速通道转发 IP 地址，而并非是客户端的真实 IP。为了将客户端IP传给服务器，加速通道将客户端的 IP 和 Port 在转发时放入了自定义的 tcp option 字段中。如下：
```
#define TCPOPT_ADDR  200    
#define TCPOLEN_ADDR 8      /* |opcode|size|ip+port| = 1 + 1 + 6 */

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
