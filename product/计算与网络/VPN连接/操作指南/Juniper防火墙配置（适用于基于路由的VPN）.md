使用 IPsec VPN 建立腾讯云 VPC 到用户 IDC 的连接时，在配置完腾讯云 VPN 网关后，您还需在用户 IDC 本地站点的网关设备中进行 VPN 配置。本文以 Juniper 防火墙为例介绍如何在本地站点中进行 VPN 配置。


## 前提条件
请确保您已经在腾讯云 VPC 内创建 VPN，并完成 VPN 通道配置。

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
<td>159.75.41.242</td>
</tr>
<tr>
<td rowspan="2">IDC 信息 </td>
<td>内网 CIDR</td>
<td>172.16.0.0/16</td>
</tr>
<tr>
<td>网关公网IP</td>
<td>120.235.225.76</td>
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
<td>IP Address：120.235.225.76</td>
</tr>
<tr>
<td>远端标识</td>
<td>IP Address：159.75.41.242</td>
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
1. 登录防火墙设备的命令行配置界面。
```
 ssh -p 22 root@172.16.0.1    # 通过 SSH 命令登录防火墙命令行界面
    root@SRX1> configure 
    Entering configuration mode    # 登录之后为操作模式，键入“configure”进入配置模式
    [edit]
    root@SRX1#                   # “#” 表示已经进入配置模式
    root@SRX1# commit 
    commit complete           # 在配置模式下面修改配置，不会直接生效，通过“commit”命令，修改的配置才会保存并生效
```
2. 配置防火墙网络接口、安全域、地址簿信息，以及自定义服务。
```
set interfaces ge-0/0/2 unit 0 family inet address 172.16.0.1/16  
# 为内部接口 ge-0/0/2定义 IP 地址
set interfaces ge-0/0/3 unit 0 family inet address 120.235.225.76/30  
# 为外部接口 ge-0/0/3定义 IP 地址
set interfaces st0 unit 0 family inet     
# 定义通道接口，默认不设置 IP 地址，通道接口的 unit 后的参数需要指定，一个 unit 号可以绑定一个 VPN 通道，序号范围：0-16385
set security zones security-zone trust interfaces ge-0/0/2.0  
# 绑定 ge-0/0/0/2 为内部安全区(trust)，对接内部业务区
set security zones security-zone untrust interfaces ge-0/0/3.0  host-inbound-traffic system-services ike
# 绑定ge-0/0/3为外部安全区(untrust)，对接外部广域网，并启用 ike 服务，表示该区域可以建立 VPN
set security zones security-zone vpn interfaces st0.0     
# 绑定通道接口到 vpn 区域(vpn)，作为连接 IPSEC VPN 的逻辑通道,用于后续的路由策略以及访问策略
set security zones security-zone vpn address-book address vpn-peer_subnet 10.1.1.0/24   
# 定义要访问的 VPN 对端的业务地址簿，用于后续的访问策略调用，命名可以自定义
set security zones security-zone trust address-book address vpn-local_subnet 172.16.0.0/16   
# 定义本地的业务地址簿，用于后续的访问策略调用，命名可以自定义
set applications application tcp_2020 source-port 0-65535 destination-port 2020 protocol tcp inactivity-timeout 1800 description vpn-HR-system
# 定义要访问的业务端口，通常 SRX 系列防火墙内置了大部分常用的协议端口，可以直接在策略中调用，以”junos-“字段开头，例如“junos-ssh” 对应 ssh 协议，本例采用自定义协议端口，如定义一个 TCP 类服务，使用目的端口为 TCP 2020，服务超时时间为1800
```
3. 配置 IKE 策略。
```
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
```
4. 配置 IKE 网关、出接口和协议版本。
```
set security ike gateway ike-gate-cfgr ike-policy ike-policy-cfgr
# 调用之前定义的 IKE 策略命名
set security ike gateway ike-gate-cfgr address 159.75.41.242
# 定义 IKE 的网关地址信息（对端 VPN 的公网地址）
set security ike gateway ike-gate-cfgr local-identity inet 120.235.225.76
set security ike gateway ike-gate-cfgr remote-identity inet 159.75.41.242
#定义 VPN 标记，可以使用 FQDN 或者 IP 地址等（本实例使用远端及本端 IP 地址）
set security ike gateway ike-gate-cfgr external-interface ge-0/0/3
# 绑定 VPN 的接口，即本地的公网出口
set security ike gateway ike-gate-cfgr version v1-only
# 定义 IKE 的版本，v1
```
5. 配置 IPsec 策略。
```
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
set security ipsec vpn-monitor-options interval 4
set security ipsec vpn-monitor-options threshold 3
set security ipsec vpn ipsec-vpn-cfgr vpn-monitor
# 以上3项为建议配置，设置通道状态监控参数以及调用（实例设置为4s一次 ping 间隔，3次丢失判断通道异常）可根据实际情况选择阈值
```
6. 应用 IPsec 策略。
```
set security ipsec vpn ipsec-vpn-cfgr ike gateway ike-gate-cfgr
# 调用之前定义的 IPsec 策略配置
set security ipsec vpn ipsec-vpn-cfgr establish-tunnels immediately
# 配置 VPN 直接建立通道，而不是等待流量触发
set routing-options static route 10.1.1.0/24 next-hop st0.0
# 配置远端的业务 IP 网段，通过虚拟通道接口进行转发
```
7. 配置出站策略。
```
set security policies from-zone trust to-zone vpn policy trust-to-vpn_tcp-2020_permit match source-address vpn-local_subnet
set security policies from-zone trust to-zone vpn policy trust-to-vpn_tcp-2020_permit match destination-address vpn-peer_subnet
set security policies from-zone trust to-zone vpn policy trust-to-vpn_tcp-2020_permit match application tcp_2020
set security policies from-zone trust to-zone vpn policy trust-to-vpn_tcp-2020_permit then permit
# 定义访问策略，本策略为本地网段访问 VPN 对端业务网段方向的策略（trust to vpn）。具体的访问权限根据实际业务访问情况来设置
```
8. 配置入站策略。
```

set security policies from-zone vpn to-zone trust policy vpn-to-trust_tcp-2020_permit match source-address vpn-peer_subnet
set security policies from-zone vpn to-zone trust policy vpn-to-trust_tcp-2020_permit match destination-address vpn-local_subnet
set security policies from-zone vpn to-zone trust policy vpn-to-trust_tcp-2020_permit match application tcp_2020
set security policies from-zone vpn to-zone trust policy vpn-to-trust_tcp-2020_permit then permit
# 定义访问策略，本策略为对端 VPN 网段访问本地业务网段方向的策略（vpn to trust）。具体的访问权限根据实际业务访问情况来设置
```
9. 保存配置
```
root@SRX1# commit 
commit complete
#在配置模式下面修改配置，不会直接生效，通过“commit”命令，修改的配置才会保存并生效
```
