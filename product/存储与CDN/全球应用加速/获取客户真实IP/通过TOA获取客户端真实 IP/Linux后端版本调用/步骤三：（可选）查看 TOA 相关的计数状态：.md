为保障 TOA 内核模块运行的稳定性，TOA 内核模块还提供了监控功能。在插入 toa.ko 内核模块后，可以通过以下两种方式监控 TOA 模块的工作状态。

执行以下命令查看 TOA 相关的计数状态。
```
cat /proc/net/toa_stats
```
![](https://qcloudimg.tencent-cloud.cn/raw/7c6cc32285f861d87f3d4ecd3ae5d9a9.png)

其中主要的监控指标对应的含义如下所示：

| 指标名称             | 说明                                                         |
| -------------------- | ------------------------------------------------------------ |
| syn_recv_sock_toa    | 接收带有 TOA 信息的连接个数。                                |
| syn_recv_sock_no_toa | 接收并不带有 TOA 信息的连接个数。                            |
| getname_toa_ok       | 调用 getsockopt 获取源 IP 成功即会增加此计数，另外调用 accept 函数接收客户端请求时也会增加此计数。 |
| getname_toa_mismatch | 调用 getsockopt 获取源 IP 时，当类型不匹配时，此计数增加。例如某条客户端连接内存放的是 IPv4 源 IP，并非为 IPv6 地址时，此计数便会增加。 |
| getname_toa_empty    | 对某一个不含有 TOA 的客户端文件描述符调用 getsockopt 函数时，此计数便会增加。 |
| ip6_address_alloc    | 当 TOA 内核模块获取 TCP 数据包中保存的源 IP、源 Port 时，会申请空间保存信息。 |
| ip6_address_free     | 当连接释放时，toa 内核模块会释放先前用于保存源 IP、源 port 的内存，在所有连接都关闭的情况下，所有 CPU 的此计数相加应等于 ip6_address_alloc 的计数。 |
