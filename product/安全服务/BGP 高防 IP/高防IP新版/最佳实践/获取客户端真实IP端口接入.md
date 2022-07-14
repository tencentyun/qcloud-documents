本文档将介绍如何使用 TOA 模块获取客户端的真实 IP。

## 背景信息
DDoS 高防 IP 使用非网站业务转发规则时，源站需使用 TOA 模块获取客户端的真实 IP。
业务请求经过高防 IP 的 4 层转发后，业务服务器端接收到报文后，其看到的源 IP 地址是高防 IP 的出口 IP 地址。为了让服务器端能够获取到用户端实际的 IP 地址，可以使用如下 TOA 的方案。在业务服务的 Linux 服务器上，安装对应的 TOA 内核包。业务侧就可以获取到用户端实际的 IP 地址。

## TOA 原理
高防转发后，数据包同时会做 SNAT 和 DNAT，数据包的源地址和目标地址均修改。
TCP 协议下，为了将客户端 IP 传给服务器，会将客户端的 IP，port 在转发时放入了自定义的 tcp option 字段。
		
    #define TCPOPT_ADDR	200  
    #define TCPOLEN_ADDR 8	/* |opcode|size|ip+port| = 1 + 1 + 6 */

    /*
    *insert client ip in tcp option, now only support IPV4,
    *must be 4 bytes alignment.
    */
    struct ip_vs_tcpo_addr {
    __u8 opcode;
    __u8 opsize;
    __u16 port;
    __u32 addr;
    }; 
Linux 内核在监听套接字收到三次握手的 ACK 包之后，会从 `SYN_REVC` 状态进入到 `TCP_ESTABLISHED` 状态。这时内核会调用 `tcp_v4_syn_recv_sock` 函数。 Hook 函数 `tcp_v4_syn_recv_sock_toa `首先调用原有的` tcp_v4_syn_recv_sock `函数，然后调用 `get_toa_data` 函数从 TCP OPTION 中提取出 TOA OPTION，并存储在 `sk_user_data` 字段中。

然后用 `inet_getname_toa hook inet_getname`，在获取源 IP 地址和端口时，首先调用原来的`inet_getname`，然后判断 `sk_user_data` 是否为空，如果有数据从其中提取真实的 IP 和 port，替换 `inet_getname` 的返回。

程序在用户态调用 getpeername，返回的 IP 和 port 即为客户端的原始 IP。

## TOA 模块安装步骤
下面将介绍不同的内核版本，TOA 的安装方法：
>!
>- TOA 安装依赖内核版本，环境需要具备相应版本的内核代码，根据内核代码进行编译内核插件。
>- 建议客户灰度升级，内核插件影响较大。
>- 本篇文章主要介绍解析 TOA 插件的安装，插入 TOA 一般集成在转发引擎中本文不做介绍。
			
			
1. 下载源码包。
	- **内核版本 2.X**
下载源码包：[toa_kernel_2.x.tar.gz](https://daaa-1254383475.cos.ap-shanghai.myqcloud.com/toa_kernel_2.x.tar.gz)
	- **内核版本 3.X**
下载源码包：[toa_kernel_3.x.tar.gz](https://daaa-1254383475.cos.ap-shanghai.myqcloud.com/toa_kernel_3.x.tar.gz)
	- **内核版本 4.X**
下载源码包：[toa_kernel_4.x.tar.gz](https://daaa-1254383475.cos.ap-shanghai.myqcloud.com/toa_kernel_4.x.tar.gz)
2. 安装编译环境。
```plaintext
yum install gcc kernel-headers kernel-devel –y
```
3. 解压源码包。
```plaintext
tar zxf toa_kernel_*.tar.gz
```
4. 进入 TOA 目录。
```plaintext
cd toa
```
5. 执行脚本 toa.sh(3.x 和 4.x 跳过此步)。
>?3.x 内核和 4.x 内核无需执行 toa.sh。
>
```plaintext
toa.sh
```
5. 编译 make。
```plaintext
make
```
6. 移动并加载模块。
```plaintext
mv toa.ko /lib/modules/`uname -r`/kernel/net/netfilter/ipvs/toa.ko
insmod /lib/modules/`uname -r`/kernel/net/netfilter/ipvs/toa.ko
```
7. 查看是否加载成功。
>?如需临时关闭 TOA ：rmmod 路径/模块名。
>
```plaintext
# lsmod | grep toa
toa 12886 0
```

