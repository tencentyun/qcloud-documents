### 如何开通 FTP 功能？

对象存储是一种支持 Web 方式请求的持久化存储，不提供原生的 FTP 访问方式。使用 FTP 协议必须通过中转，**推荐您根据腾讯云官方提供的 [FTP Server 工具](https://www.qcloud.com/document/product/436/7214 ) ，自行搭建服务使用。**
由于 FTP 协议老旧，无法校验数据完整性以及保障传输安全性，也无法与CAM权限系统对接，因此强烈不建议继续使用 FTP 协议访问，腾讯云亦不会对 FTP 协议和中转软件提供后续支持。 
如需数据同步建议直接使用 [COS Migration 工具  ](https://www.qcloud.com/document/product/436/7133)或 [COSCMD 工具](https://www.qcloud.com/document/product/436/10976)。

### 配置文件中的 masquerade_address 这个选项有何作用？何时需要配置 masquerade_address？

当 FTP Server 运行在一个多网卡的 Server 上，并且 FTP Server 采用了 PASSIVE 模式时（一般地，FTP 客户端位于一个 NAT 网关之后时，都需要启用 PASSIVE 模式），此时需要使用 masquerade_address 选项来唯一绑定一个 passive 模式下用于 reply 的 IP。 

例如，FTP Server 有多个 IP 地址，如内网 IP 为 10.XXX.XXX.XXX，外网 IP 为 123.XXX.XXX.XXX。 客户端通过外网 IP 连接到 FTP Server，同时客户端使用的是 PASSIVE 模式传输，此时，若 FTP Server 未指定 masquerade_address 具体绑定到外网 IP 地址，则 Server 在 PASSIVE 模式下，reply 时，有可能会走内网地址。这时就会出现客户端能连接上 Ftp server，但是不能从 Server 端获取任何数据回复的问题。

如果需要配置 masquerade_address，建议指定为客户端连接 Server 所使用的那个 IP 地址。

### 正确配置了 masquerade_address 选项以后，ftp server 可以正常登录，但是执行 FTP 命令：list 或者 get 等数据取回命令时，提示“服务器返回不可路由的地址”或“ftp: connect: No route to host”等错误，该如何处理？

这个 case 多半是因为 ftp server 机器 iptables 或防火墙策略配置 reject 或者 drop 掉所有 ICMP 协议包，而 FTP 客户端在拿到 FTP Server 被动模式下返回的数据连接 IP 后，会首先发送一个 ICMP 包探测 IP 的连通性，所以客户端会提示“服务器返回不可路由的地址”等错误。

建议解决方案是：将 iptables 策略按需配置为只 reject 或 drop 希望限制的 ICMP 包类型，如只想禁掉外部 ping 类型的 ICMP 包，可以将策略修改为：iptables -A INPUT -p icmp --icmp-type 8 -s 0/0 -j [REJECT/DROP]
或者单独放开要访问 ftp server 的客户端的 IP。

### 上传大文件的时候，中途取消，为什么 COS 上会留有已上传的文件？

由于适用于 COS 最新版本的 FTP Server 提供了完全的流式上传特性，用户文件上传的取消或断开，都会触发大文件的上传完成操作。因此，COS 会认为用户数据流已经上传完成，并将已经上传的数据组成一个完整的文件。 如果用户希望重新上传，可以直接以原文件名上传覆盖；也可手动删除不完整的文件，重新上传。

### 为什么 FTP Server 配置中要设置最大上传文件的限制？

COS 的分片上传数目最大只能为 10000 块，且每个分片的大小限制为 1 MB ~ 5 G。 这里设置最大上传文件的限制是为了合理计算一个上传分片的大小。
FTP Server 默认支持 200 GB 以内的单文件上传，但是不建议用户设置过大，因为单文件大小设置越大，上传时的分片缓冲区也会相应的增大，这可能会耗费用户的内存资源。因此，建议用户根据自己的实际情况，合理设置单文件的大小限制。

### 如果上传的文件超过最大限制，会怎么样？

当实际上传的单文件大小超过了配置文件中的限制，系统会返回一个 IOError 的异常，并且在日志中标注错误信息。

如遇有其他问题，请 [提交工单](https://console.cloud.tencent.com/workorder/category)，并在工单上附上完整的`cos_v5.log`日志，便于我们进一步排查和解决问题。
