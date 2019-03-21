下列图示分别举例说明了单个和多个 IPsec VPN 通道，您需要在黑石私有网络创建 IPsec VPN 网关，以及在对端网络配置对端网关，以便启用 IPsec VPN 连接。

当您为一个黑石私有网络配置多个 IPsec VPN 通道时，您可以在黑石私有网络启用多个 IPsecVPN 网关，同时在对端网络启用多个对端网关对接不同 IPsec VPN 通道，您也可以在多个对端网络各自启用对端网关对接 IPsec VPN 通道。


## 单个 IPsec VPN 通道
![](https://main.qcloudimg.com/raw/8121937fe5355f1b61f2ceb9a4b93652.png)
黑石私有网络与用户网络之间只有一条 IPsec VPN 通道，该通道承载所有 VPN 加密流量。

## 多个 IPsec VPN 通道
![](https://main.qcloudimg.com/raw/815d4ad05c010b28530d40a40fa0a34e.png)
黑石私有网络与用户网络之间配置两条 IPsec VPN 通道，两条通道分别承载不同 VPN 加密流量。该场景不建议两条通道配置相同 SPD 策略做负载均衡及冗余，因为 IPsec VPN 仅支持静态路由，IPsec VPN 通道中断后相关路由策略并不撤销，因此会出现 VPN 流量中断故障。

## 多个 IPsec VPN 网关和通道
![](https://main.qcloudimg.com/raw/d398706e30612a028eeac44dd475f6a0.png)
黑石私有网络与用户多个网络各自建立 IPsec VPN 通道，每一条通道承载用户不同网络的 VPN 加密流量。当一个 IPsec VPN 网关的带宽能力（100Mbps）无法满足需求时，您可以创建第二个 IPsec VPN 网关连接至用户其它网络。
