当用户业务分别部署于云下数据中心和云上 VPC 中时，可通过专线接入或 VPN 连接实现云上云下业务互通，为提升业务高可用性，可同时创建专线接入和 VPN 连接服务，结合 VPC 路由优先级功能，配置两条链路为主备链路，来实现冗余通信。本文指导您如何配置专线和 VPC 主备链路来实现云上云下混合通信。
>?
>+ 路由优先级功能目前处于内测中，如有需要，请 [在线咨询](https://cloud.tencent.com/online-service?from=sales&source=PRESALE)。
>+ VPC 路由表中根据不同的下一跳类型定义了不同的优先级，目前默认路由优先级为：云联网 > 专线网关 > VPN 网关 > 其他。
>+ 暂不支持控制台修改路由优先级，如需调整，请 [在线咨询](https://cloud.tencent.com/online-service?from=sales&source=PRESALE)。



## 业务场景
如下图所示，用户在 VPC 和 IDC 中部署了业务，为了实现云上与云下业务交互，用户需要部署网络连接服务来实现业务互通，为实现高可用通信，部署方案如下：
+ 专线接入（主）：本地 IDC 通过物理专线，接入 VPC 的专线网关实现云下云上业务通信。在物理专线链路正常时，本地 IDC 与 VPC 之间所有的通信流量都通过物理专线进行转发。
+ VPN 连接（备）：本地 IDC 与云上 VPC 通过建立 VPN 安全隧道来实现云上云下业务通信，当专线链路出现异常时，可将流量切换至该链路，确保业务可用性。
![](https://main.qcloudimg.com/raw/57f25f54abfeb75710a3c82a11d2e30f.png)

## 前提条件
+ 用户本地 IDC 网关设备具有 IPsec VPN 功能，可同时作为用户侧 VPN 网关设备，与 VPC 侧 VPN 设备建立 IPsec 隧道通信。
+ 用户 IDC 侧网关设备已配置静态 IP。
+ 数据准备如下：
  <table>
  <th colspan="3">配置项</th>
   <th>示例值</th>
  <tr>
  <td rowspan="4">网络配置 </td>
  <td rowspan="2">VPC 信息 </td>
  <td>子网 CIDR</td>
  <td>192.168.1.0/24 </td>
  </tr>
  <tr>
  <td>VPN 网关公网 IP</td>
  <td>203.xx.xx.82</td>
  </tr>
  <tr>
  <td rowspan="2">IDC 信息 </td>
  <td>子网 CIDR</td>
  <td>10.0.1.0/24</td>
  </tr>
<tr>
<td>网关公网 IP</td>
<td>202.xx.xx.5</td>
</tr>
</table>
	

## 操作流程
<dx-steps>
- [配置 IDC 通过专线接入上云](#step1)
- [配置 IDC 通过VPN连接上云](#step2)
- [配置网络探测](#step3)
- [配置告警](#step4)
- [切换主备路由](#step5)
  </dx-steps>

## 操作步骤

### [](id:step1)步骤一： 配置 IDC 通过专线接入上云
1. 登录 [专线接入控制台](https://console.cloud.tencent.com/dc/dc) ，单击左侧导航栏的【物理专线】创建物理专线。
2. 单击左侧导航栏的【专线网关】创建专线网关，本例选择接入私有网络，标准型的专线网关，如果 IDC 和 VPC 通信网段冲突也可以选择 NAT 型。
3. 单击左侧导航栏的【专用通道】创建专用通道，此处需要配置通道名称、选择专线类型、已创建的专线网关、腾讯云侧和用户侧的互联 IP、路由方式选择静态路由、填写 IDC 通信网段等，配置完成后下载配置指引并在 IDC 设备完成配置。
4. 在 VPC 通信子网关联的路由表中配置下一跳为专线网关、目的端为 IDC 通信网段的路由策略。
>?更多详细配置可参考 [专线接入快速入门](https://cloud.tencent.com/document/product/216/7557)。
>


###  [](id:step2)步骤二：配置 IDC 通过 VPN 连接上云
1. 登录 [VPN 网关控制台](https://console.cloud.tencent.com/vpc/vpnGw?rid=1) ，单击【新建】创建 VPN 网关，本例关联网络选择私有网络。
2. 单击左侧导航栏的【对端网关】，配置对端网关（即 IDC 侧 VPN 网关的逻辑对象），填写 IDC 侧 VPN 网关的公网 IP 地址，例如202.xx.xx.5。
3. 单击左侧导航栏的【VPN 通道】，请配置 SPD 策略、IKE、IPsec 等配置。
4. 在 IDC 本地网关设备上配置 VPN 通道信息，此处配置需要和步骤3中的 VPN 通道信息一致，否则 VPN 隧道无法正常连通。
5. 在 VPC 通信子网关联的路由表中配置下一跳为 VPN 网关、目的端为 IDC 通信网段的路由策略。
>?更多详细配置请参考[ 建立 VPC 到 IDC 的连接（路由表）](https://cloud.tencent.com/document/product/554/52853)。
>

###  [](id:step3)步骤三：配置网络探测
>?如上两步配置完成后，VPC 去往 IDC 已经有两条路径，即下一跳为专线网关和 VPN 网关，根据路由默认优先级：专线网关 > VPN 网关，则专线网关为主路径，VPN 网关为备路径。

为了解主备路径的连接质量，需要分别配置两条路径的网络探测，实时监控到网络连接的时延、丢包率等关键指标，以探测主备路由的可用性。
1. 登录 [网络探测控制台](https://console.cloud.tencent.com/vpc/detection?rid=1)。
2. 单击【新建】，创建网络探测，填写网络探测名称，选择私有网络、子网、探测目的IP，并指定源端下一跳路由，如专线网关。
3. 请再次执行[ 步骤2](#step2)，指定源端下一跳路由为 VPN 网关。配置完成后，即可查看专线接入和VPN连接主备路径的网络探测时延和丢包率。
>?更多详细配置请参考 [网络探测](https://cloud.tencent.com/document/product/215/20091)。
>

### [](id:step4)步骤四：配置告警
为及时发现探测链路异常，可配置告警策略。当检测到链路异常时，告警信息将通过电子邮件和短信等形式发送到您，帮助您提前预警风险。
1. 登录云监控下的 [告警策略控制台](https://console.cloud.tencent.com/monitor/alarm2/policy)。
2. 单击【新建】，填写策略名称、策略类型选择【私有网络/网络探测】，告警对象选择具体的网络探测实例，配置触发条件和告警通知等信息，并单击【完成】即可。

### [](id:step5)步骤五：切换主备路由
当收到专线网关主路径的网络探测异常告警时，您需要手动禁用主路由，将流量切换至 VPN 网关备份路由上。
1. 登录 [路由表控制台](https://console.cloud.tencent.com/vpc/route?rid=1)。
2. 单击 VPC 通信子网关联路由表 ID，进入路由详情页，单击<img src="https://main.qcloudimg.com/raw/af79ad3ab5488ea94ead43a8fba3486f.png" width="3%" />禁用下一跳到专线网关的主路由，此时 VPC 去往 IDC 的流量将从专线网关切换至 VPN 网关。
