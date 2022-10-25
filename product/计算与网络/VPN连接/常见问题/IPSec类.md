<dx-tabs>
::: VPN 网关
  
[](id:01)
### 网关为什么删除不了？
删除前需要将其下关联的 VPN 通道资源删除，详情请参见[ 删除 SSL VPN 网关](https://cloud.tencent.com/document/product/554/63713)。

[](id:02)
### 网关规格是50Mbps，它的带宽上限怎么理解？
VPN 网关界面中的带宽上限指的是公网出带宽上限，即从 VPN 网关流出的带宽。

[](id:03)
### 网关带宽是50Mbps，上传云数据时只有2m/s，为什么？
50Mbps是您购买的带宽，数据上传速度依赖您的公网网速。

[](id:04)
### IPSec 型 VPN 网关支持切换成 SSL VPN 网关吗？
不支持，IPSec VPN 和 SSL VPN 是两种不同形态的 VPN，不能互相切换。

[](id:05)
### VPN 网关是否支持升降配？
目前仅支持部分范围内升级，【20,100】、【200,1000】，跨范围升降配暂不支持。例如：50M升级到100M可以升配，100M升级到200M需要新建200规格的网关。

[](id:06)
### 如何查看网关流量？
您可以配置网关流控功能，详情请参见 [开启网关流控明细](https://cloud.tencent.com/document/product/554/19001)。


  
[](id:07)
### 为什么 VPN 网关与 VPN 通道显示的监控数据有时不一致？
目前 VPN 网关与 VPN 通道的数据采集位置与上报间隔存在区别，其中 VPN 网关的统计粒度为1分钟，VPN 通道的统计粒度为10秒，统计粒度不一致。因此在监控页进行数据聚合的时候，会造成 VPN 网关与 VPN 通道的展示数据不一致的情况。

[](id:08)
### VPN 网关是如何实现的，可用性如何？
VPN 网关是通过网络功能虚拟化（NFV）实现的，采用双机热备的策略，单台故障时自动切换，不会影响业务正常运行。
VPN 通道在公网中运行，公网网络出现阻塞、抖动、延迟等问题都会对 VPN 网络质量产生影响。如果业务对网络传输的延迟、抖动容忍度较低，建议使用 [专线接入](https://cloud.tencent.com/document/product/216)。

[](id:09)
### 如何查看 VPN 网关详细信息？
用户可以进入[ 私有网络控制台](https://console.cloud.tencent.com/vpc/vpc?rid=1) 查看 VPN 网关详细信息，详情请参见 [查看 VPN 网关详细信息](https://cloud.tencent.com/document/product/554/18999)。






:::
::: VPN 通道
[](id:10)
### VPN 通道显示联通，为什么 Ping 不通？
通道状态正常但内网却无法联通，可能原因如下：
- VPC 子网路由表未添加指向 IDC 侧内网网段的路由。
- VPC/IDC 侧的安全策略未放通对应源 IP、目的 IP。
- VPN 网关未添加指向 IDC 侧内网网段的通道（路由型）。
- VPC/IDC 侧的内网服务器操作系统的防火墙未放行对端网段。
- VPC/IDC 侧的 SPD 策略未包含该源 IP、目的 IP。
- VPN 网关未配置路由策略。

详情请参见 [VPN 通道已联通但实际内网不通](https://cloud.tencent.com/document/product/554/53173)。

[](id:11)
### VPN 通道显示未联通？
可能原因如下：
- 无流量激活通道。
- VPN 网关公网 IP 不通。
- 安全策略配置不正确。
- 协商参数、协商模式不一致。

详情请参见：[VPN 通道未联通](https://cloud.tencent.com/document/product/554/53161)。

[](id:12)
### 通道协商失败报错码，如何解析？
通道协商失败报错码详情请参见 [IPSec VPN 协商失败报错说明](https://cloud.tencent.com/document/product/554/79960)。

[](id:13)
### 一直使用中，突然中断会是什么原因？
可能原因：
- 您的公网 IP 是境外 IP，访问云上云主机时因合规问题被禁隔离。
- 您本地配置进行了修改，如协议变更，或者本地升级默认开启了新的协议参数，而腾讯侧未配置。
- VPN 通道被删除。

[](id:14)
### 为什么要 SPD 策略？
SPD 策略指定了 VPN 网关所属网络内哪些网段可以和 IDC 中哪些网段通信。
>?同一个 VPN 网关下所有通道内的规则不能重叠。
>

[](id:15)
### 健康检查怎么配置？
1. 首先确保与 VPN 相连的对端是否为路由型网关，需要进行路由型做对接。
2. 在腾讯云控制台侧配置健康检查，具体请参见 [配置健康检查](https://cloud.tencent.com/document/product/554/70209)。
>?
>- 在进行健康检查配置前，请做好隧道主备，以防业务受到影响。
>- 需要确保两端 IP 不冲突，如果两端 IP 在同一网段，则不需要单独配置路由来指定对端。
>
3. 配置 VPN 网关路由并设置优先级。

[](id:16)
### 通道健康状态为“不健康”，是什么原因？
您配置的健康检查 IP Ping 失败，请检查健康检查配置。




[](id:17)
### VPN 支持野蛮模式吗？
不支持。

[](id:18)
### SPD 策略怎么配置，对端网段可以随便填吗？
SPD 策略指定了 VPN 网关所属网络内哪些网段可以和 IDC 中哪些网段通信，对端网段是您本地访问公网的网段的子集，不可重叠。





[](id:21)
### SPD 策略型VPN通道，SPD 策略中本端和对端有顺序要求吗？
同一条 SPD 策略中本端和对端连接没有顺序规则。

[](id:22)
### 如何修改 VPN 通道配置？
用户可以进入 [私有网络控制台](https://console.cloud.tencent.com/vpc/vpc?rid=1) 修改 VPN 通道配置，详情请参见 [修改 VPN 通道配置](https://cloud.tencent.com/document/product/554/19000)。


[](id:23)
### 如何创建 VPN 通道？
用户可以进入 [私有网络控制台](https://console.cloud.tencent.com/vpc/vpc?rid=1) 创建 VPN 通道，详情请参见 [创建 VPN 通道](https://cloud.tencent.com/document/product/554/18991)。

[](id:24)
### SPD 策略中本端和对端匹配关系是怎么样的？
匹配关系请参考[ SPD 策略](https://cloud.tencent.com/document/product/554/52864#ipsecvpnspd)。
:::
</dx-tabs>

