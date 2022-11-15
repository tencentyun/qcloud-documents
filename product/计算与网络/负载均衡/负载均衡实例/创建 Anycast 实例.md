Anycast CLB 是支持多地动态加速的负载均衡服务，Anycast CLB 的 VIP 会发布在多个地域，客户端接入最近的 POP 接入点，通过腾讯云数据中心高速互联网转发到云服务器上。Anycast
Anycast CLB 能实现网络传输的质量优化和多入口就近接入，减少网络传输的抖动、丢包，最终提升云上应用的服务质量，扩大服务范围，精简后端部署。
>?此功能处于内测阶段，如需使用，请提交 [内测申请](https://cloud.tencent.com/apply/p/47mdddtoc56)。


## Anycast CLB 架构
Anycast CLB 的 VIP 会发布在多个地域，客户端接入最近的 POP 接入点，通过腾讯云内网将访问流量极速转发至云服务器。Anycast CLB 支持的地域请参见[ Anycast 支持地域](https://cloud.tencent.com/document/product/644/12617#.3Ca-id.3D.22widthcost.22.3E.E5.85.AC.E7.BD.91.E7.BD.91.E7.BB.9C.E8.B4.B9.E7.94.A8.3C.2Fa.3E)。
![](https://qcloudimg.tencent-cloud.cn/raw/b8599852ac26f048208250cb12b3c216.svg)


## 限制说明
Anycast CLB 由内网负载均衡绑定 Anycast EIP 来提供 Anycast 能力，限制说明请参见 [内网 CLB 绑定 EIP 限制说明](https://cloud.tencent.com/document/product/214/65682#restriction)。

## 前提条件
本功能内测中，操作前请确保您的 [内测申请](https://cloud.tencent.com/apply/p/47mdddtoc56) 已通过。

## 操作指南
1. 登录 [公网 IP 控制台](https://console.cloud.tencent.com/cvm/eip?rid=1)，在“公网 IP”页面左上角选择地域，单击**申请**。
2. 在弹出的“申请 EIP”对话框中，IP 地址类型选择**加速 IP**，设置带宽上限，勾选“**同意《腾讯云 EIP 服务协议》、《欠费规则》**”后，单击**确定**。
3. 登录 [负载均衡控制台](https://console.cloud.tencent.com/clb)，在“实例管理”页面左上角选择地域，在实例列表选择目标内网负载均衡实例，选择操作列下的**更多** > **绑定弹性公网 IP**。
4. 在弹出的“绑定弹性公网 IP”对话框，选择刚才创建的加速 IP，单击**提交**。
![](https://qcloudimg.tencent-cloud.cn/raw/6be2e9622594a9cd93939f27fdfaeba1.png)
5. 内网负载均衡绑定 Anycast 加速 IP 后，该负载均衡即可提供 Anycast 负载均衡服务。更多负载均衡配置请参见 [负载均衡监听器概述](https://cloud.tencent.com/document/product/214/6151)。
![](https://main.qcloudimg.com/raw/dae5e2248aede6d523e7de28afbed0d5.png)


## 相关文档
- [Anycast 公网加速](https://cloud.tencent.com/document/product/644)
- [内网负载均衡实例绑定 EIP](https://cloud.tencent.com/document/product/214/65682)

