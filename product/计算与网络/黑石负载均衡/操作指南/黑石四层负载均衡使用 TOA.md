## 操作场景
黑石公网普通型与内网负载均衡采用的是 FULLNAT 模式，源目 IP 都做了地址转换，后端物理服务器无法获取 Client IP，可以通过 TOA（Tcp Option Address）方式获取 Client IP。
公网增强型负载均衡采用 DNAT 模式，只做目的地址转换，后端物理服务器可以直接获取 Client IP。

## 使用限制
- 只支持公网普通型与内网负载均衡。
- 只支持四层 TCP 监听器。
- 只支持后端绑定的服务器为 Linux 系统。


## 操作步骤
开启 TOA 可通过以下两种方式进行配置，请根据实际需求进行配置。
- 新建 TCP 四层监听器时，勾选“Client IP 获取”的**开启**项。
- 修改现有监听器时，可以在修改配置界面中，勾选“Client IP 获取”的**开启**项。
![](https://main.qcloudimg.com/raw/c6e2cf7d97e97801403974789d2a6961.png)

