使用 IPsec VPN 建立腾讯云 VPC 到用户 IDC 的连接时，在配置完腾讯云 VPN 网关后，您还需在用户 IDC 本地站点的网关设备中进行 VPN 配置。本文以 Juniper 防火墙为例介绍如何在本地站点中进行 VPN 配置。

>?
> + 支持 Juniper SRX 系列防火墙以及 vSRX 系列虚拟防火墙，所有版本均支持。
> + 本文所有 IP、接口等参数取值均仅用于举例，请具体配置时，使用实际值进行替换。
## 前提条件
请确保您已经在腾讯云 VPC 内[ 创建 VPN](https://cloud.tencent.com/document/product/554/52861)，并完成 并完成 [VPN 通道配置](https://cloud.tencent.com/document/product/554/52864)。

## 数据准备
本文 IPsec VPN 配置数据举例如下：
<table>
<th colspan="3">配置项</th>
<th>示例值</th>
<tr>
<td rowspan="4">网络配置 </td>
<td rowspan="2">VPC 信息 </td>
<td>子网 CIDR</td>
<td>10.1.1.0/24 </td>
</tr>
<tr>
<td>VPN 网关公网 IP</td>
<td>159.xx.xx.242</td>
</tr>
<tr>
<td rowspan="2">IDC 信息 </td>
<td>内网 CIDR</td>
<td>172.16.0.0/16</td>
</tr>
<tr>
<td>网关公网IP</td>
<td>120.xx.xx.76</td>
</tr>
<tr>
<td rowspan="16">IPsec 连接配置 </td>
<td rowspan="9">IKE 配置 </td>
<td>版本</td>
<td>IKEV1 </td>
</tr>
<tr>
<td>身份认证方法</td>
<td>预共享密钥</td>
</tr>
<tr>
<td>加密算法</td>
<td>AES-128</td>
</tr>
<tr>
<td>认证算法</td>
<td>MD5</td>
</tr>
<tr>
<td>协商模式</td>
<td>main</td>
</tr>
<tr>
<td>本端标识</td>
<td>IP Address：120.xx.xx.76</td>
</tr>
<tr>
<td>远端标识</td>
<td>IP Address：159.xx.xx.242</td>
</tr>
<tr>
<td>DH group</td>
<td>DH2</td>
</tr>
<tr>
<td>IKE SA Lifetime</td>
<td>86400</td>
</tr>
<tr>
<td rowspan="6">IPsec 配置</td>
<td>加密算法</td>
<td>AES-128</td>
</tr>
<tr>
<td>认证算法</td>
<td>MD5</td>
</tr>
<tr>
<td>报文封装模式</td>
<td>Tunnel</td>
</tr>
<tr>
<td>安全协议</td>
<td>ESP</td>
</tr>
<tr>
<td>PFS</td>
<td>disable</td>
</tr>
<tr>
<td>IPsec sa Lifetime</td>
<td>3600s</td>
</tr>
</table>

## 操作步骤
<dx-tabs>
::: 适用于基于&nbsp;SPD&nbsp;策略转发的&nbsp;VPN
1. 登录防火墙设备的命令行配置界面。
<dx-codeblock>
:::sh
ssh -p 22 root@172.16.0.1   
# 通过 SSH 命令登录防火墙命令行界面
root@SRX1> configure 
Entering configuration mode    
# 登录之后为操作模式，键入“configure”进入配置模式
[edit]
root@SRX1#                   
# “#” 表示已经进入配置模式
root@SRX1# commit 
commit complete           
# 在配置模式下面修改配置，不会直接生效，通过“commit”命令，修改的配置才会保存并生效
:::
</dx-codeblock>
2. 配置防火墙网络接口、安全域、地址簿信息。
<dx-codeblock>
:::sh
set interfaces ge-0/0/x unit 0 family inet address 172.16.0.1/16  
# 为内部接口ge-0/0/x定义IP地址，请更换为实际接口和IP
set interfaces ge-0/0/y unit 0 family inet address 120.xx.xx.76/30  
# 为外部接口ge-0/0/y定义IP地址，请更换为实际接口和IP
set security zones security-zone trust interfaces ge-0/0/x.0   
# 绑定ge-0/0/x为内部安全区(trust)，对接内部业务区，请更换为实际接口
set security zones security-zone untrust interfaces ge-0/0/y.0  host-inbound-traffic system-services ike  
# 绑定ge-0/0/y为外部安全区(untrust)，对接外部广域网，并启用ike服务，表示该区域可以建立VPN
set security zones security-zone untrust address-book address vpn-peer_subnet 10.1.1.0/24  
# 定义要访问的VPN对端的业务地址簿，用于后续的访问策略调用，命名可以自定义
set security zones security-zone trust address-book address vpn-local_subnet 172.16.0.0/16  
# 定义本地的业务地址簿，用于后续的访问策略调用，命名可以自定义
:::
</dx-codeblock>
3. 配置 IKE 策略。
<dx-codeblock>
:::sh
set security ike proposal ike-proposal-cfgr authentication-method pre-shared-keys
# 定义IPSEC VPN 认证方式（本实例使用共享密钥模式：pre-shared-keys），注意“ike-proposal-cfgr”为定义的命名，后续设置需要调用该命名
set security ike proposal ike-proposal-cfgr dh-group group2
# 定义IKE的dh-group
set security ike proposal ike-proposal-cfgr authentication-algorithm md5
# 定义IKE认证算法 
set security ike proposal ike-proposal-cfgr encryption-algorithm aes-128-cbc
# 定义IKE加密算法
set security ike proposal ike-proposal-cfgr lifetime-seconds 86400
# 定义IKE生存时间， 范围：(180～86400 seconds)
set security ike policy ike-policy-cfgr mode main
# 指定IKE模式
set security ike policy ike-policy-cfgr proposals ike-proposal-cfgr
# 定义IKE策略，需要调用上面步骤中的算法定义命名定义
set security ike policy ike-policy-cfgr pre-shared-key ascii-text "TestPassword"
# 定义密钥，注意密钥不能包含：“@“，”+“，”-“，”=“ 字符
:::
</dx-codeblock>
4. 配置 IKE 网关、出接口和协议版本。
<dx-codeblock>
:::sh
set security ike gateway ike-gate-cfgr ike-policy ike-policy-cfgr
# 调用之前定义的IKE策略命名
set security ike gateway ike-gate-cfgr address 159.xx.xx.242
# 定义IKE的网关地址信息（对端VPN的公网地址）
set security ike gateway ike-gate-cfgr local-identity inet 120.xx.xx.76
set security ike gateway ike-gate-cfgr remote-identity inet 159.xx.xx.242
# 定义VPN标记，可以使用FQDN或者IP地址等，本实例使用本端及远端IP地址
set security ike gateway ike-gate-cfgr external-interface ge-0/0/y
# 绑定VPN的接口，即本地的公网出口
set security ike gateway ike-gate-cfgr version v1-only
# 定义IKE的版本，v1
:::
</dx-codeblock>
5. 配置 IPsec 策略。
<dx-codeblock>
:::sh
set security ipsec proposal ipsec-proposal-cfgr protocol esp
# 定义IPSEC阶段的加密协议
set security ipsec proposal ipsec-proposal-cfgr authentication-algorithm hmac-md5-96
# 定义IPSEC阶段的认证算法
set security ipsec proposal ipsec-proposal-cfgr encryption-algorithm aes-128-cbc
# 定义IPSEC阶段的加密算法
set security ipsec proposal ipsec-proposal-cfgr lifetime-seconds 3600
# 定义IPSEC阶段生存时间（范围：180～86400）
set security ipsec policy ipsec-policy-cfgr proposals ipsec-proposal-cfgr
# 调用之前定义的IPSEC算法定义
:::
</dx-codeblock>
6. 应用 IPsec 策略。
<dx-codeblock>
:::sh
set security ipsec vpn ipsec-vpn-cfgr ike gateway ike-gate-cfgr
# 调用之前定义的IKE网关配置
set security ipsec vpn ipsec-vpn-cfgr ike ipsec-policy ipsec-policy-cfgr
# 调用之前定义的 IPsec 策略配置
set security ipsec vpn ipsec-vpn-cfgr establish-tunnels immediately
# 配置VPN直接建立通道，而不是等待流量触发
set routing-options static route 10.1.1.0/24 next-hop x.x.x.x
# 基于策略的VPN需要将远端的网段配置路由从公网接口发出，x.x.x.x为设备的公网接口下一跳地址
:::
</dx-codeblock>
7. 配置出站策略。
<dx-codeblock>
:::sh
set security policies from-zone trust to-zone vpn policy trust-to-untrust_any_permit match source-address vpn-local_subnet
set security policies from-zone trust to-zone vpn policy trust-to-untrust_any_permit match destination-address vpn-peer_subnet
set security policies from-zone trust to-zone vpn policy trust-to-untrust_any_permit match application any
set security policies from-zone untrust to-zone trust policy trust-to-untrust_any_permit then permit tunnel ipsec-vpn ipsec-vpn-cfgr
set security policies from-zone untrust to-zone trust policy trust-to-untrust_any_permit then permit tunnel pair-policy untrust-to-trust_any_permit
# 定义访问策略，本策略为本地网段访问VPN对端业务网段方向的策略（trust to untrust），指定调用IPSEC VPN 通道。具体的访问权限根据实际业务访问情况来设置
:::
</dx-codeblock>
8. 配置入站策略。
<dx-codeblock>
:::sh
set security policies from-zone vpn to-zone trust policy untrust-to-trust_any_permit match source-address vpn-peer_subnet
set security policies from-zone vpn to-zone trust policy untrust-to-trust_any_permit match destination-address vpn-local_subnet
set security policies from-zone vpn to-zone trust policy untrust-to-trust_any_permit match application any
set security policies from-zone vpn to-zone trust policy untrust-to-trust_any_permit then permit tunnel ipsec-vpn ipsec-vpn-cfgr
set security policies from-zone vpn to-zone trust policy untrust-to-trust_any_permit then permit tunnel pair-policy trust-to-untrust_any_permit
# 定义访问策略，本策略为对端VPN网段访问本地业务网段方向的策略（untrust to trust），指定调用IPSEC VPN 通道。具体的访问权限根据实际业务访问情况来设置
:::
</dx-codeblock>
9. 保存配置。
<dx-codeblock>
:::sh
root@SRX1# commit 
commit complete
# 在配置模式下面修改配置，不会直接生效，通过“commit”命令，修改的配置才会保存并生效
:::
</dx-codeblock>

:::
::: 适用于基于路由转发的&nbsp;VPN
1. 登录防火墙设备的命令行配置界面。
<dx-codeblock>
:::sh
ssh -p 22 root@172.16.0.1    
# 通过 SSH 命令登录防火墙命令行界面
root@SRX1> configure 
Entering configuration mode    
# 登录之后为操作模式，键入“configure”进入配置模式
[edit]
root@SRX1#                   
# “#” 表示已经进入配置模式
root@SRX1# commit 
commit complete           
# 在配置模式下面修改配置，不会直接生效，通过“commit”命令，修改的配置才会保存并生效
:::
</dx-codeblock>
2. 配置防火墙网络接口、安全域、地址簿信息。
<dx-codeblock>
:::sh
set interfaces ge-0/0/x unit 0 family inet address 172.16.0.1/16  
# 为内部接口 ge-0/0/x定义 IP 地址，请更换为实际接口和IP
set interfaces ge-0/0/y unit 0 family inet address 120.xx.xx.76/30  
# 为外部接口 ge-0/0/y定义 IP 地址，请更换为实际接口和IP
set interfaces st0 unit 0 family inet mtu 1398
# 定义通道接口，默认不设置 IP 地址，通道接口的 unit 后的参数需要指定，一个 unit 号可以绑定一个 VPN 通道，序号范围：0-16385，同时设置通道接口MTU为1398
set security zones security-zone trust interfaces ge-0/0/x.0  
# 绑定 ge-0/0/x 为内部安全区(trust)，对接内部业务区
set security zones security-zone untrust interfaces ge-0/0/y.0  host-inbound-traffic system-services ike
# 绑定ge-0/0/y为外部安全区(untrust)，对接外部广域网，并启用 ike 服务，表示该区域可以建立 VPN
set security zones security-zone vpn interfaces st0.0     
# 绑定通道接口到 vpn 区域(vpn)，作为连接 IPSEC VPN 的逻辑通道,用于后续的路由策略以及访问策略
set security zones security-zone vpn address-book address vpn-peer_subnet 10.1.1.0/24   
# 定义要访问的 VPN 对端的业务地址簿，用于后续的访问策略调用，命名可以自定义
set security zones security-zone trust address-book address vpn-local_subnet 172.16.0.0/16   
# 定义本地的业务地址簿，用于后续的访问策略调用，命名可以自定义
:::
</dx-codeblock>
3. 配置 IKE 策略。
<dx-codeblock>
:::sh
set security ike proposal ike-proposal-cfgr authentication-method pre-shared-keys
# 定义 IPSEC VPN 认证方式（本实例使用共享密钥模式：pre-shared-keys），注意“ike-proposal-cfgr”为定义的命名，后续设置需要调用该命名
set security ike proposal ike-proposal-cfgr dh-group group2
# 定义 IKE 的 dh-group
set security ike proposal ike-proposal-cfgr authentication-algorithm md5
# 定义 IKE 认证算法
set security ike proposal ike-proposal-cfgr encryption-algorithm aes-128-cbc
# 定义 IKE 加密算法
set security ike proposal ike-proposal-cfgr lifetime-seconds 86400
# 定义 IKE 生存时间， 范围：(180-86400 seconds)
set security ike policy ike-policy-cfgr mode main
set security ike policy ike-policy-cfgr proposals ike-proposal-cfgr
set security ike policy ike-policy-cfgr pre-shared-key ascii-text "TestPassword"
# 定义 IKE 策略，指定模式以及密钥，需要调用上面步骤中的算法定义命名，注意密钥不能包含：“@“，”+“，”-“，”=“ 字符
:::
</dx-codeblock>
4. 配置 IKE 网关、出接口和协议版本。
<dx-codeblock>
::: sh
set security ike gateway ike-gate-cfgr ike-policy ike-policy-cfgr
# 调用之前定义的 IKE 策略命名
set security ike gateway ike-gate-cfgr address 159.xx.xx.242
# 定义 IKE 的网关地址信息（对端 VPN 的公网地址）
set security ike gateway ike-gate-cfgr local-identity inet 120.xx.xx.76
set security ike gateway ike-gate-cfgr remote-identity inet 159.xx.xx.242
#定义 VPN 标记，可以使用 FQDN 或者 IP 地址等（本实例使用远端及本端 IP 地址）
set security ike gateway ike-gate-cfgr external-interface ge-0/0/y
# 绑定 VPN 的接口，即本地的公网出口
set security ike gateway ike-gate-cfgr version v1-only
# 定义 IKE 的版本，v1
:::
</dx-codeblock>
5. 配置 IPsec 策略。
<dx-codeblock>
:::sh
set security ipsec proposal ipsec-proposal-cfgr protocol esp
# 定义 IPSEC 阶段的加密协议
set security ipsec proposal ipsec-proposal-cfgr authentication-algorithm hmac-md5-96
# 定义 IPSEC 阶段的认证算法
set security ipsec proposal ipsec-proposal-cfgr encryption-algorithm aes-128-cbc
# 定义 IPSEC 阶段的加密算法
set security ipsec proposal ipsec-proposal-cfgr lifetime-seconds 3600
# 定义 IPSEC 阶段的生存时间
set security ipsec policy ipsec-policy-cfgr proposals ipsec-proposal-cfgr
# 调用之前定义的 IPSEC 算法定义
set security ipsec vpn ipsec-vpn-cfgr ike proxy-identity local 172.16.0.0/16
set security ipsec vpn ipsec-vpn-cfgr ike proxy-identity remote 10.1.1.0/24
#设置 TS（Traffic Selector）或者 SPD 配置，默认为0.0.0.0/0，如果对端也指定了网段，则需要和对端匹配
set security ipsec vpn ipsec-vpn-cfgr bind-interface st0.0
# 绑定 VPN 通道接口
:::
</dx-codeblock>
6. 应用 IPsec 策略。
<dx-codeblock>
:::sh
set security ipsec vpn ipsec-vpn-cfgr ike gateway ike-gate-cfgr
# 调用之前定义的IKE网关配置
set security ipsec vpn ipsec-vpn-cfgr ike ipsec-policy ipsec-policy-cfgr
# 调用之前定义的 IPsec 策略配置
set security ipsec vpn ipsec-vpn-cfgr establish-tunnels immediately
# 配置 VPN 直接建立通道，而不是等待流量触发
set routing-options static route 10.1.1.0/24 next-hop st0.0
# 配置远端的业务 IP 网段，通过虚拟通道接口进行转发
:::
</dx-codeblock>
7. 配置出站策略。
<dx-codeblock>
:::sh
set security policies from-zone trust to-zone vpn policy trust-to-vpn_any_permit match source-address vpn-local_subnet
set security policies from-zone trust to-zone vpn policy trust-to-vpn_any_permit match destination-address vpn-peer_subnet
set security policies from-zone trust to-zone vpn policy trust-to-vpn_any_permit match application any
set security policies from-zone trust to-zone vpn policy trust-to-vpn_any_permit then permit
# 定义访问策略，本策略为本地网段访问 VPN 对端业务网段方向的策略（trust to vpn）。具体的访问权限根据实际业务访问情况来设置
:::
</dx-codeblock>
8. 配置入站策略。
<dx-codeblock>
:::sh
set security policies from-zone vpn to-zone trust policy vpn-to-trust_any_permit match source-address vpn-peer_subnet
set security policies from-zone vpn to-zone trust policy vpn-to-trust_any_permit match destination-address vpn-local_subnet
set security policies from-zone vpn to-zone trust policy vpn-to-trust_any_permit match application any
set security policies from-zone vpn to-zone trust policy vpn-to-trust_any_permit then permit
# 定义访问策略，本策略为对端 VPN 网段访问本地业务网段方向的策略（vpn to trust）。具体的访问权限根据实际业务访问情况来设置
:::
</dx-codeblock>
9. 保存配置
<dx-codeblock>
:::sh
root@SRX1# commit 
commit complete
#在配置模式下面修改配置，不会直接生效，通过“commit”命令，修改的配置才会保存并生效
:::
</dx-codeblock>
:::
</dx-tabs>

