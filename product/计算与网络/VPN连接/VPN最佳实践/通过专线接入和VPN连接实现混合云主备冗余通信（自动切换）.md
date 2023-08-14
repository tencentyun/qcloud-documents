当用户业务分别部署于云下数据中心和云上 VPC 中时，可通过专线接入或 VPN 连接实现云上云下业务互通，为提升业务高可用性，可同时创建专线接入和 VPN 连接服务，结合 CCN 配置两条链路为主备链路，来实现冗余通信。
>?
>- 路由优先级功能目前处于内测中，如有需要，请 [在线咨询](https://cloud.tencent.com/online-service?from=sales&source=PRESALE)。
>- 暂不支持控制台修改路由优先级，如需调整，请 [在线咨询](https://cloud.tencent.com/online-service?from=sales&source=PRESALE)。
>- 配置主备路由时，专线网段掩码长度须大于 VPN 网段掩码长度。
>


## 业务场景
如下图所示，用户在 VPC 和 IDC 中部署了业务，为了实现云上与云下业务交互，用户需要部署网络连接服务来实现业务互通，为实现高可用通信，故障时业务自动切换，部署方案如下：
- 专线接入（主）：本地 IDC 通过物理专线，接入CCN型的专线网关实现云下云上业务通信。在物理专线链路正常时，本地 IDC 与 VPC 之间所有的通信流量都通过物理专线进行转发。
- VPN 连接（备）：本地 IDC 与云上 VPC 通过建立 CCN 型 VPN 安全隧道来实现云上云下业务通信，当专线链路出现异常时，自动将流量切换至该链路，确保业务可用性。
![](https://qcloudimg.tencent-cloud.cn/raw/8b6951724b8a924655fbdd72799320c1.png)

## 前提条件
- 用户本地 IDC 网关设备具有 IPsec VPN 功能，可同时作为用户侧 VPN 网关设备，与云侧 VPN 设备建立 IPsec 隧道通信。
- 用户 IDC 侧网关设备已配置静态 IP。
- 已创建 CCN 实例，并开启了 ECMP 和路由重叠特性，详情联系 [在线支持](https://cloud.tencent.com/online-service)。
- 专线侧已开启动态 BGP 传递特性，详情请联系 [在线支持](https://cloud.tencent.com/online-service)。

## 操作步骤
### 步骤一：配置 IDC 通过专线接入上云
1. 登录 [专线接入控制台](https://console.cloud.tencent.com/dc/dc)，单击左侧导航栏的物理专线，单击**+新建**，创建物理专线，详情可参见 [申请接入物理专线](https://cloud.tencent.com/document/product/216/48586)。
2. 单击左侧导航栏的专线网关，单击**新建**，创建 CCN 型专线网关，创建完成后在其详情发布指向 CCN 的网段，详细操作可参见 [创建专线网关](https://cloud.tencent.com/document/product/216/19256)、[发布网段至云联网](https://cloud.tencent.com/document/product/216/50956)。
3. 单击左侧导航栏的**专用通道** > **独享专用通道**，单击**+新建**，创建独享专用通道，此处需要配置通道名称、选择专线类型、已创建的专线网关、腾讯云侧和用户侧的互联 IP、路由方式选择静态路由、填写 IDC 通信网段等，配置完成后下载配置指引并在 IDC 设备完成配置。详细操作可参见 [独享专用通道](https://cloud.tencent.com/document/product/216/74769)。
>?更多详细配置可参考 [IDC 通过云联网上云](https://cloud.tencent.com/document/product/216/31638)。
>


### 步骤二：配置 IDC 通过 VPN 连接上云
1. 登录 [VPN 网关控制台](https://console.cloud.tencent.com/vpc/vpnGw?rid=1)，单击**+新建**，创建 CCN 型 VPN 网关可参见 [创建 VPN 网关](https://cloud.tencent.com/document/product/554/52861)，创建完成后，在其详情页关联 CCN 实例，详细操作可参见 [绑定云联网实例](https://cloud.tencent.com/document/product/554/71642)。
2. 单击左侧导航栏的对端网关，配置对端网关（即 IDC 侧 VPN 网关的逻辑对象），填写 IDC 侧 VPN 网关的公网 IP 地址，例如202.xx.xx.5。详细操作可参见 [创建对端网关](https://cloud.tencent.com/document/product/554/52865)。
3. [](id:step3-2)单击左侧导航栏的 VPN 通道，单击**新建**，创建 VPN 通道，请页面引导配置 SPD 策略、IKE、IPsec 等参数。详细配置信息可参见 [创建 VPN 通道](https://cloud.tencent.com/document/product/554/52864)。
在 IDC 本地网关设备上配置 VPN 通道信息，此处配置需要和 [步骤3](#step3-2) 中的 VPN 通道信息一致，否则 VPN 隧道无法正常连通。
在网关的路由表页签配置指向对端网关的路由。
>?更多详细配置请参考 [建立 IDC 到云联网的连接](https://cloud.tencent.com/document/product/554/44267)。
>


### 步骤三：配置告警
为及时发现探测链路异常，可配置告警策略。当检测到链路异常时，告警信息将通过电子邮件和短信等形式发送到您，帮助您提前预警风险。
1. 登录腾讯云可观测平台的 [告警策略控制台](https://console.cloud.tencent.com/monitor/alarm2/policy)。
2. 单击**新建**，填写策略名称、策略类型选择私有网络/网络探测，告警对象选择具体的网络探测实例，配置触发条件和告警通知等信息，并单击**完成**即可。

### 步骤四：切换主备路由
当收到专线网关主路径的网络探测异常告警时，自动会将您的流量切换至 VPN 网关备份路由上。
如果主路专线恢复正常后，您需要手动将流量切会至专线网关。

