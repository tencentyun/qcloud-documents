负载均衡支持创建 Anycast 负载均衡（下文也叫 Anycast CLB）实例，Anycast CLB 是支持全球动态加速的负载均衡服务，CLB 的 VIP 会发布在全球多个地域，客户端接入最近的 POP 接入点，通过腾讯云数据中心高速互联网转发到云服务器上。
Anycast CLB 能实现网络传输的质量优化和多入口就近接入，减少网络传输的抖动、丢包，最终提升云上应用的服务质量，扩大服务范围，精简后端部署。
>?本功能内测中，如需使用，请提交 [内测申请](https://cloud.tencent.com/act/apply/aia)。

## 什么是 Anycast
Anycast 又称为任播或泛播，指同一个 IP 在多个地域同时发布路由，路由算法会把用户流量送达到最近的路由器。
Anycast CLB 有以下优势：
- **低时延**
Anycast CLB 用 Anycast 的方式把 VIP 同时发布到多个地域，请求包根据传输协议会到达最优的 VIP 发布地域，优先进入腾讯云，通过腾讯云内网到达云服务器，避开公网的拥堵，减少时延。
- **降低抖动和丢包**
公网链路的传输性能不稳定，如南北问题、跨境问题等，会导致网络的抖动和丢包，影响服务体验。而 Anycast CLB 的传输性能稳定，它将客户端请求就近接入腾讯云后，通过腾讯云的内网专线进行跨地域传输，解决了公网抖动和丢包的问题。
- **高可靠**
公网传输是不可靠的传输，而运营商线路中断，导致服务不可访问，一般用户只能等待恢复。使用 Anycast CLB 后，腾讯云内网、运营商网络、腾讯云 POP 接入点能实现网络多路径和多入口，屏蔽单地域和单线路的故障，提高网络稳定性。
- **简化部署**
客户分散在多地又需要就近接入的服务，需要多地部署机器且配置 DNS 实现负载均衡，且不同地域的 IP 不同，部署繁琐。使用 Anycast CLB 后，在 IP 层面收敛了地域属性，无需每个地域都配置 IP，且后端维护一套逻辑即可，各地域请求直接用内网加速到后端机器。

## Anycast CLB 架构
Anycast CLB 的架构如下图所示。
![](https://main.qcloudimg.com/raw/246a76b59853740089f012832c0a5fb0.svg)
Anycast CLB 的 VIP 会发布在全球多个地域，客户端接入最近的 POP 接入点，通过腾讯云内网将访问流量极速转发至云服务器。

### Anycast 发布域
Anycast 发布域是加速 IP 地址发布的地域，即 Anycast CLB 的 VIP 所发布的 POP 接入点，客户端接入最近的 POP 接入点。目前 Anycast CLB 支持以下发布域：
- 发布域 A：主要是中国和欧美地区，VIP 将同时在在北京、上海、广州、中国香港、多伦多、硅谷、法兰克福、弗吉尼亚和莫斯科发布。
- 发布域 B：主要是中国和东南亚地区，VIP 将同时在北京、上海、广州、中国香港、新加坡、首尔、孟买、曼谷和东京发布。

### Anycast CLB 所属地域
与普通负载均衡的地域概念一致，Anycast CLB 所属地域是购买 Anycast CLB 时选择的地域，也指后端云服务器所在的地域。目前 Anycast CLB 已覆盖绝大部分地域。
- 中国：北京、上海、广州、香港。
- 欧美：多伦多、硅谷、法兰克福、弗吉尼亚、莫斯科。
- 东南亚：新加坡、首尔、孟买、曼谷、东京。
>!
>- Anycast CLB 仅支持 **应用型** 负载均衡，不支持传统型负载均衡。
>- Anycast CLB 当前仅支持 **四层协议（TCP/UDP）**，暂不支持七层协议（HTTP/HTTPS）。
>- Anycast CLB 暂不支持 S4、SN3ne、S2ne、M4、GN6s 云服务器。

## Anycast CLB 使用场景
### 全球同服
游戏客户希望全球多个地域玩家在同一区内（或者企业在全球各地的分公司希望使用同一个数据中心），可以把后端服务部署在一个地域（如广州），购买一个广州地域的 Anycast CLB，根据需要选择发布域，全球玩家（或员工）将就近接入，并访问同一套后端服务。
![](https://main.qcloudimg.com/raw/052fa943c9cdfa90c98a4f84ec0976e0.svg)

### 游戏加速
Anycast CLB 在游戏加速中的应用也非常广泛，游戏请求就近接入腾讯云，通过腾讯云的内网到达游戏服务器，极大缩短经过的公网路径，减少了延时、抖动、丢包等问题的发生。跟传统加速比，入口无需额外部署流量接收设备，且无需区分地域，简化了 DNS 部署。
![](https://main.qcloudimg.com/raw/345252f99a6dd42eb3d4033d39d8f6f6.svg)


## 操作指南
### 创建 Anycast CLB 实例
1. [内测申请](https://cloud.tencent.com/act/apply/aia) ，登录腾讯云官网，进入 [负载均衡购买页](https://buy.cloud.tencent.com/lb)。
2. 实例类型选择【应用型 CLB】，加速 IP 处勾选【启用 Anycast 加速 IP】，其他配置和 [普通实例配置](https://cloud.tencent.com/document/product/214/8975#2.-.E8.B4.AD.E4.B9.B0.E5.B9.B6.E9.85.8D.E7.BD.AE.E5.85.AC.E7.BD.91.E5.BA.94.E7.94.A8.E5.9E.8Blb) 相同。
3. 购买完成后，返回至 [负载均衡实例列表页](https://console.cloud.tencent.com/loadbalance/index?rid=1&forward=1)，即可查看已购的 Anycast 负载均衡。
![](https://main.qcloudimg.com/raw/4eac4325d24c4138daf2c46704672851.png)

### 使用 Anycast CLB
1. 登录 [负载均衡管理控制台](https://console.cloud.tencent.com/loadbalance/index?rid=1&forward=1)，进入 “LB 实例列表”。
2. 单击实例 ID，进入详情页。
3. 在 **监听器管理** 页面，可以配置监听器、设置转发规则、绑定云服务器，详情请参见 [应用型 LB 快速入门](https://cloud.tencent.com/document/product/214/8975)。
![](https://main.qcloudimg.com/raw/a884a2e0a51cecf5056ca6053c9c2da5.png)
