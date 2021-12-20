### 如何开通 FTP 功能？

对象存储是一种支持 Web 方式请求的持久化存储，不提供原生的 FTP 访问方式。使用 FTP 协议必须通过中转，**推荐您根据腾讯云官方提供的 [FTP Server 工具](https://www.qcloud.com/document/product/436/7214 ) ，自行搭建服务使用。**
由于 FTP 协议老旧，无法校验数据完整性以及保障传输安全性，也无法与CAM权限系统对接，因此强烈不建议继续使用 FTP 协议访问，腾讯云亦不会对 FTP 协议和中转软件提供后续支持。 
如需数据同步建议直接使用 [COS Migration 工具 ](https://cloud.tencent.com/document/product/436/15392)或 [COSCMD 工具](https://www.qcloud.com/document/product/436/10976)。

### 配置文件中的 masquerade_address 这个选项有何作用？何时需要配置 masquerade_address？

masquerade_address 是配置提供给客户端的服务器地址。当 FTP server 运行在一个通过 NAT 映射到外网 IP 的主机上时，此时需要配置 masquerade_address 选项为客户端可以访问的 FTP Server 外网 IP，以通知客户端使用该 IP 与服务端完成数据通信。

例如，在 FTP Server 运行的机器上，执行 ifconfig，得到映射到外网的网卡 IP 为10.xxx.xxx.xxx，它映射的外网 IP 假设为119.xxx.xxx.xxx。此时，若 FTP Server 未显式配置 masquerade_address 为客户端访问 server 时的外网 IP（119.xxx.xxx.xxx），则 FTP Server 在 Passive 模式下，给客户端回包可能会使用内网地址（10.xxx.xxx.xxx）。这时就会出现客户端就能够连上 FTP Server，但是却不能正常给客户端返回数据包的情况。

因此，通常情况下，建议用户将 masquerade_address 都配置为客户端连接 Server 时所使用的那个 IP 地址。


### 正确配置了 masquerade_address 选项以后，ftp server 可以正常登录，但是执行 FTP 命令：list 或者 get 等数据取回命令时，提示“服务器返回不可路由的地址”或“ftp: connect: No route to host”等错误，该如何处理？

这个 case 多半是因为 ftp server 机器 iptables 或防火墙策略配置 reject 或者 drop 掉所有 ICMP 协议包，而 FTP 客户端在拿到 FTP Server 被动模式下返回的数据连接 IP 后，会首先发送一个 ICMP 包探测 IP 的连通性，所以客户端会提示“服务器返回不可路由的地址”等错误。

建议解决方案是：将 iptables 策略按需配置为只 reject 或 drop 希望限制的 ICMP 包类型，如只想禁掉外部 ping 类型的 ICMP 包，可以将策略修改为：`iptables -A INPUT -p icmp --icmp-type 8 -s 0/0 -j [REJECT/DROP]`
或者单独放开要访问 ftp server 的客户端的 IP。

### 上传大文件的时候，中途取消，为什么 COS 上会留有已上传的文件？

由于适用于 COS 最新版本的 FTP Server 提供了完全的流式上传特性，用户文件上传的取消或断开，都会触发大文件的上传完成操作。因此，COS 会认为用户数据流已经上传完成，并将已经上传的数据组成一个完整的文件。 如果用户希望重新上传，可以直接以原文件名上传覆盖；也可手动删除不完整的文件，重新上传。


### 如果上传的文件超过最大限制，会怎么样？

当实际上传的单文件大小超过了配置文件中的限制，系统会返回一个 IOError 的异常，并且在日志中标注错误信息。

如遇有其他问题，请 [联系我们](https://cloud.tencent.com/document/product/436/37708)，并附上完整的`cos_v5.log`日志，便于我们进一步排查和解决问题。

### 为什么 COS FTP Server 配置中要设置最大上传文件的限制？

COS 的分块上传数量最大只能为 10000 块，且每个分块的大小限制为 1MB - 5GB。这里设置最大上传文件大小是为了合理计算一个上传分块的大小。

FTP Server 默认支持 200GB 以内的单文件上传，但是不建议用户设置过大，因为单文件大小设置越大，上传时的分块缓冲区也会相应的增大，这可能会耗费用户的内存资源。因此，建议用户根据自己的实际情况，合理设置单文件的大小限制。



