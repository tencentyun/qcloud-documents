## 操作场景

对等连接（Peering Connection）是一种大带宽、高质量的云上资源互通服务，可以打通腾讯云上的资源通信链路。您可以通过对等链接实现同地域不同 VPC 下的间的集群互通。关于如何建立对等连接，您可以参考 [创建对等连接](https://cloud.tencent.com/document/product/553/18836)。

>! 
> - 本文档以已创建集群并已添加节点为例。关于如何创建集群，您可以参考 [创建集群](https://cloud.tencent.com/document/product/457/11741) 进行创建。
> - 请先确保对等连接间成功建立，子机间能互通。若对等连接建立有问题，请排查**控制台路由表项、CVM 安全组、子网 ACL** 的设置是否有问题。
> - 暂时仅支持**同地域对等连接**间容器互通。若需要跨地域间容器互通，请提交工单咨询。

## 操作步骤


### 获取容器的基本信息

1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)。
2. 在左侧导航栏中，单击【[集群](https://console.cloud.tencent.com/tke2/cluster?rid=1)】，进入集群管理页面。
3. <span id="step3">单击需要设置同地域集群间互通的集群 ID/名称，进入该集群的管理页面。如下图所示：</span>
例如，进入 A 集群的管理页面。
![](https://main.qcloudimg.com/raw/d87f3d03f6c97313927eb93ddc885518.png)
4. 在左侧导航栏中，选择 “基本信息”，进入“基本信息” 页面。如下图所示：
![](https://main.qcloudimg.com/raw/ff32de50dadbee103621862412ae08cc.png)
5. <span id="step5">记录 “基本信息” 中 “容器网络” 的网段和掩码。</span>
6. 重复执行 [步骤3](#step3) - [步骤5](#step5)，记录另一个集群容器网络的网段和掩码。
例如，记录 B 集群容器网络的网段和掩码。

### 配置路由表

1. 切换至 [私有网络控制台](https://console.cloud.tencent.com/vpc/vpc)。
2. <span id="VPCStep2">在左侧导航栏中，单击【[子网](https://console.cloud.tencent.com/vpc/subnet)】，进入子网管理页面。</span>
3. 单击对等连接本端指定子网的关联路由表。如下图所示：
![](https://main.qcloudimg.com/raw/472c8ef4d50f463d84652ebabb42e4c4.png)
4. 在关联路由表的 “默认详情” 页面，单击【+新增路由策略】。
5. 在弹出的 “新增路由” 窗口中，设置路由信息。主要参数信息如下：
 - 目的端：输入 B 集群容器的网段。
 - 下一跳类型：选择 “**对等连接**”。
 - 下一跳：选择已建立的对等连接。
6. <span id="VPCStep6">单击【确定】，完成本端路由表的配置。</span>
7. 重复执行 [步骤2](#VPCStep2) - [步骤6](#VPCStep6)，完成对端路由表的配置。

### 预期结果

容器之间可以互通，容器的登录方法请参考  [远程终端基本操作](https://cloud.tencent.com/document/product/457/9120)。
1. 登录集群 A 的容器，并在集群 A 的容器中访问集群 B 的容器。如下图所示：
![](https://main.qcloudimg.com/raw/61f44f2ffc028a4000282a6e1ca24fb0.png)
2. 登录集群 B 的容器，并在集群 B 的容器中访问集群 A 的容器。如下图所示：
![](https://main.qcloudimg.com/raw/5c7302cec8b1199bf2ef6cded48c2a95.png)

