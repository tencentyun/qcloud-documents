负载均衡支持创建 IPv6 实例，腾讯云会给实例分配一个 IPv6 公网地址（即 IPv6 版的 vip），该 vip 转发来自 IPv6 客户端的请求。

## 什么是 IPv6
IPv6 指网际协议第6版（Internet Protocol version 6），是网际协议（IP）的最新版本。IPv6 是 IETF（互联网工程任务组，Internet Engineering Task Force）设计的用于替代现行版本 IP 协议（IPv4）的下一代 IP 协议。与 IPv4 相比，IPv6 的主要特点：
- IPv6 具有更大的地址空间。当前 IPv4 采用的是32位地址，网络地址资源有限，严重制约了互联网的应用和发展。而 IPv6 采用128位的地址，即 IPv6 支持2<sup>128</sup>（约3.4\*10<sup>38</sup>）个地址，比 IPv4 增加了约7.9\*10<sup>28</sup>个地址。使用 IPv6，可以让全世界的每一粒沙子都能分配到一个 IP 地址。
- IPv6 使用更小的路由表，提高了路由器转发数据包的速度。
- IPv6 增强了对组播和流控的支持，为服务质量的控制提供了良好的网络平台。
- IPv6 具有更高的安全性。在 IPv6 中的加密与鉴别选项提供了分组的保密性与完整性，极大地增强了网络的安全性。

## IPv6 负载均衡架构
IPv6 负载均衡的架构如下图所示。
![](https://main.qcloudimg.com/raw/caae8ad5e6a49ce24aeaa3fc0a6fd0c7.svg)
通过 IPv6 网络访问 IPv6 负载均衡时，负载均衡能平滑地将 IPv6 地址转换为 IPv4 地址，适配原有的服务，快速实现 IPv6 的改造。

## IPv6 负载均衡优势
腾讯云负载均衡在助力业务快速接入 IPv6 时具有如下优势：
- **快速接入：**秒级接入 IPv6，随买随用快速上线。
- **业务平滑过渡：**业务仅需改造客户端，无需改造后端服务，便可平滑接入 IPv6。IPv6 负载均衡支持来自 IPv6 客户端的访问，并将 IPv6 报文转换成 IPv4 报文，后端云服务器上的应用程序无需感知 IPv6，仍以原有形式部署工作。
- **易于使用：**IPv6 负载均衡兼容原 IPv4 负载均衡的操作流量，零学习成本，低门槛使用。

>!
>- 当前 IPv6 负载均衡仅支持北京、上海、广州三个地域。
>- IPv6 负载均衡仅支持 **应用型** 负载均衡，不支持传统型负载均衡。
>- 互联网 IPv6 网络大环境还处于建设初期，如出现线路访问不通的情况，请填写 [工单](https://console.cloud.tencent.com/workorder/category) 反馈，同时在内测期间，不提供 SLA 保障。

## 操作指南
### 创建 IPv6 负载均衡
1. 登录腾讯云官网，进入 [负载均衡购买页](https://buy.cloud.tencent.com/lb)。
2. 实例类型选择 **应用型 CLB**，IP 类型选择 **IPv6**，其他配置和普通实例配置相同。
3. 购买完成后，返回至 [负载均衡实例列表页](https://console.cloud.tencent.com/loadbalance/index?rid=1&forward=1)，即可查看已购的 IPv6 负载均衡。
![](https://main.qcloudimg.com/raw/1b87146cc6b4e42417e2d323f4f6d00c.png)

### 使用 IPV6 负载均衡
登录 [负载均衡管理控制台](https://console.cloud.tencent.com/loadbalance/index?rid=1&forward=1)，单击实例 ID，进入详情页，在 **监听器管理** 页面配置监听器、转发规则、绑定云服务器，详情请参见 [应用型 LB 快速入门](https://cloud.tencent.com/document/product/214/8975)。
![](https://main.qcloudimg.com/raw/9802a8e3baeffccb1b1ba853594b0755.png)
