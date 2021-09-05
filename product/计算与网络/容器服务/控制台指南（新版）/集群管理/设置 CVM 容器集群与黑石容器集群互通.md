## 操作场景
对等连接（Peering Connection）是一种大带宽、高质量的云上资源互通服务，可以打通腾讯云上的资源通信链路。您可以通过对等连接实现同地域不同 VPC 下的间的集群互通。本文主要介绍黑石私有网络与公有云私有网络之间建立对等连接，黑石物理机与容器间的互通。

>! 
- 本文档以已在公有云创建集群并已添加节点为例。关于如何创建集群，您可以参考 [创建集群](https://cloud.tencent.com/document/product/457/11741) 进行创建。
- 请先确保对黑石公有云对等连接成功建立，子机与黑石间能互通。若对等连接建立有问题，请排查**控制台路由表项、安全组、子网 ACL** 的设置是否有问题。
- 原理上，黑石容器集群用的 bgp 协议，确认 CVM 的容器集群能和黑石物理机互通， 即可与黑石容器集群互通。

## 操作步骤

[](id:ObtainInformation)
### 获取信息
1. 登录 [黑石私有网络控制台](https://console.cloud.tencent.com/vpcbm/vpc)。
2. 在私有网络管理页面中，记录需要建立黑石 VPC 的 **CIDR**。如下图所示：
![](https://main.qcloudimg.com/raw/5ae8641abe14861597d01ebbe9a2bac3.png)
3. 切换至 [容器服务控制台](https://console.cloud.tencent.com/tke2)。
4. 在左侧导航栏中，单击 **[集群](https://console.cloud.tencent.com/tke2/cluster)**，进入集群管理页面。
5. 单击需要设置互通的集群 ID/名称，进入该集群的管理页面。如下图所示：
![](https://main.qcloudimg.com/raw/d87f3d03f6c97313927eb93ddc885518.png)
6. 在左侧导航栏中，选择 “基本信息”，进入“基本信息” 页面。如下图所示：
![](https://main.qcloudimg.com/raw/ff32de50dadbee103621862412ae08cc.png)
7. 记录 “基本信息” 中 “所在地域”、“节点网络” 和 “容器网络” 的信息。
8. 单击右上方的**账号** > **[账号信息](https://console.cloud.tencent.com/developer)**，记录当前账号的 APPID。如下图所示：
![](https://main.qcloudimg.com/raw/a9057017451dbe67837a0867cf6022ab.png)
9. 切换至 [私有网络控制台](https://console.cloud.tencent.com/vpc/vpc)。
10. 在左侧导航栏中，单击 **[对等连接](https://console.cloud.tencent.com/vpc/conn)**，进入对等连接管理页面，并记录对等连接的 ID/名称。如下图所示：
![](https://main.qcloudimg.com/raw/cdd10b18030ba60e2d73414dfbc24118.png)

### 申请对等连接
[在线咨询](https://console.cloud.tencent.com/workorder)，并在工单中填写在 [获取信息](#ObtainInformation) 中记录的 “所在地域”、“节点网络”、“容器网络” 和 当前账号的 APPID 信息。

### 预期结果

容器与黑石机器之间可以互通，公有云集群容器的登录方法请参考  [远程终端基本操作](https://cloud.tencent.com/document/product/457/9120)。
1. 登录公有云集群容器，并在公有云集群容器中访问黑石机器。如下图所示：
![容器 to 黑石物理机](https://main.qcloudimg.com/raw/108c2b400d84a7880c59645200348a1e.png)
2. 登录黑石机器，并在黑石机器中访问公有云集群容器。如下图所示：
![黑石物理机 to 容器](https://main.qcloudimg.com/raw/2dfad41e746e6affbd76664f39a0f465.png)
