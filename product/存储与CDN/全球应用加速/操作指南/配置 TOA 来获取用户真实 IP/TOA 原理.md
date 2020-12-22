## 通过 TOA 获取客户端真实 IP
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

## 通过 Proxy Protocol 获取客户端真实 IP
Proxy Protocol 是通过为 TCP 添加一个头部信息，来方便的传递客户端信息（协议栈、源 IP、目的 IP、源端口、目的端口等），在网络情况复杂又需要获取用户真实 IP 时非常有用。其本质是在三次握手结束后由代理在连接中插入一个携带了原始连接四元组信息的数据包。

Proxy Protocol 方式获取客户端 IP 需要在控制台配置使用(当前仅支持协议为 TCP 的监听器使用)，加速服务在和源站建立连接后，会在传输的第一个 payload 的报文前插入Proxy Protocol 协议文本。

当前 Nginx 和 HaProxy 都已经支持 Proxy Protocol 协议，如下，Nginx 配置支持 Proxy Protocol 协议只需要将参数 proxy_protocol 添加在 server 块中的 listen 指令后：
```
http {
    #...
    server {
        listen 80   proxy_protocol;
        listen 443  ssl proxy_protocol;
        #...
    }
}
```

 不支持 Proxy Protocol 的应用程序, 需要在 TCP 连接建立后，读取 Proxy Protocol 的文本行并进行字符串解析来获取客户端 IP, 字符示例如下所示：
 ```
 PROXY TCP4 1.1.1.2 2.2.2.2 12345 80\r\n
 ```
