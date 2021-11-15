IPv6（Internet Protocol version 6），相对于 IPv4 的使用32位 bit 进行地址标识，IPv6 使用128位 bit 来标识地址，极大的扩展了地址空间，可以解决 IPv4 地址枯竭问题，当前黑石负载均衡已完成对 IPv6 的支持，用户购买黑石 IPv6 负载均衡实例后，会分配一个 IPv6 公网地址（即 IPv6 版的 VIP），可以用该 IPv6 地址解决 IPv6 客户端的请求。


## 优势
腾讯云黑石负载均衡在助力业务快速接入 IPv6 时具有如下优势：

#### 快速接入
秒级接入 IPv6，随买随用快速上线。

#### 平滑过渡
业务仅需改造客户端，无需改造后端服务。IPv6 负载均衡将来自 IPv6 客户端的访问报文转换成 IPv4 报文再送给后端服务器，后端云服务器上的应用程序无需感知 IPv6，仍以原有形式部署工作。

#### 易于使用
IPv6 负载均衡兼容原 IPv4 负载均衡的操作流程，零学习成本，低门槛使用。

<dx-alert infotype="notice" title="">
- 当前只支持黑石公网普通型负载均衡实例。
- 当前只在上海、北京两个地域开放。
</dx-alert>





## 使用限制
- IPv6 LB 不支持会话保持。
- IPv6 LB 不支持 TOA，无法获取 client IP。

## 计费模式
黑石 IPv6 负载均衡与黑石 IPv4 负载均衡计费模式一样，可以参考 [黑石 IPv4 负载均衡计费](https://cloud.tencent.com/document/product/1027/33207)。

## 操作指南
1. 登录腾讯云官网，进入 [黑石负载均衡购买页](https://buy.cloud.tencent.com/lbbm)。
2. 实例类型选择**公网普通型** ，IP 协议选择 IPv6 ，其他资源按需选择。
3. 单击**立即购买**，即可完成黑石 IPv6 LB 的购买。
4. 购买完成后，返回至 [黑石负载均衡实例列表页](https://console.cloud.tencent.com/lbbm/lb)，即可查看已购的 IPv6 负载均衡。



<dx-alert infotype="explain" title="">
后续的创建四层、七层监听器以及绑定后端服务器与普通 IPv4 负载均衡方法相同。
</dx-alert>


