腾讯云提供 VPN 连接和专线接入服务，可连接您的企业数据中心和私有网络，您可根据需求进行选择，二者的主要区别如下：
- **[VPN 连接](https://cloud.tencent.com/product/vpn.html)**
VPN 连接可利用公网和 IPsec 协议，在您的数据中心和私有网络之间建立加密的网络连接，但是 VPN 连接可能会受到 Internet 抖动、阻塞等公网质量问题而中断。VPN 连接所需的 VPN 网关的购买、生效和配置可以在几分钟内完成。当用户业务对网络连接质量要求不高时，VPN 连接是一种快速部署的高性价比选择。
- **[专线接入](https://cloud.tencent.com/product/dc.html)**
专线接入为您提供一个专用的专线网络连接方案，施工时间较长，但可以提供高质量、高可靠的网络连接服务。当您的业务对网络质量和网络安全要求较高时，可以选择此方案进行部署。

下面将为您介绍如何使用 VPN 连接部署混合云。
## 应用场景
- VPN 连接（VPN Connections）是一款通过 IPsec 加密通道，连接您的企业数据中心和腾讯云私有网络（VPC）的服务，为您提供安全、可靠的加密通信。
- 目前 VPN 通道支持 IKE / IPesec 加密协议，最大支持100M带宽，如您有特殊需求，可以提交 [工单](https://console.cloud.tencent.com/workorder/category/create?level1_id=6&level2_id=168&level1_name=%E8%AE%A1%E7%AE%97%E4%B8%8E%E7%BD%91%E7%BB%9C&level2_name=%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%20VPC) 申请，我们会为您提供定制化 VPN 接入服务。
- VPN 通道的网络质量依赖于公网连接的网络质量，建议您在选择部署私有网络的地域时，优先测试一下自有 IT 资源与腾讯云不同地域的网络时延，从而获得最优的混合云部署架构。

>**注意：**
>您需要为 VPN 通道占用的公网带宽付费，如果您的混合云互通带宽要求大于200M，建议您选择 [专线接入的混合云部署](https://cloud.tencent.com/document/product/215/7543) 方案。

## 解决方案
- **云上数据中心：**在腾讯云创建的某个私有网络，部署云上数据中心。
- **连接方式：**VPN 连接。
- **网段规划：**物理数据中心与需要连接的私有网络之间**网段不可重叠**。

## 操作步骤
在腾讯云创建的某个私有网络部署云上数据中心，详情请参见 [私有网络-操作总览](https://cloud.tencent.com/document/product/215/20188)，本文不重复说明。
VPN 连接可以在控制台实现全自助配置，操作步骤如下：
1. [创建 VPN 网关](https://cloud.tencent.com/document/product/554/18989)。
2. [创建对端网关](https://cloud.tencent.com/document/product/554/18990)。
3. [创建 VPN 通道](https://cloud.tencent.com/document/product/554/18991)。
4. 在自有 IPsec VPN 网关中 [加载配置文件](https://cloud.tencent.com/document/product/554/18992)。
5. [配置路由表](https://cloud.tencent.com/document/product/554/18993)。
6. [激活 VPN 隧道](https://cloud.tencent.com/document/product/554/18994)。

更多 VPN 连接操作详情，请参见 [操作指南](https://cloud.tencent.com/document/product/554/18996)。
