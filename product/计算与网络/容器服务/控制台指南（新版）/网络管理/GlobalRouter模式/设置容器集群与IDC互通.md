## 操作场景

目前容器集群与用户 IDC 互通主要通过两种方式：**专线**和 **IPsec VPN**。
>! 
> - 本文档以已创建集群并已添加节点为例。关于如何创建集群，您可以参考 [创建集群](https://cloud.tencent.com/document/product/457/11741) 进行创建。
> - 请先确保容器服务所在的 VPC 和您 IDC 机房已通过专线或 VPN 成功连接。若通道未连接，您可以参考 [VPN 通道未连通如何处理？](https://cloud.tencent.com/document/product/554/18904)。

## 操作步骤

### 通过专线方式互通

1. 参考 [申请物理专线](https://cloud.tencent.com/document/product/216/19244)，申请物理专线。
2. 参考 [申请通道](https://cloud.tencent.com/document/product/216/19250)，申请通道。
3. 参考 [创建专线网关](https://cloud.tencent.com/document/product/216/19256)，创建专线网关。
4. 验证容器节点与 IDC 互通。
>! 执行此步骤时，请保证容器节点与 IDC 互通，验证通过。
6. 准备地域，appID，集群 ID，vpcID，专线网关 ID 信息，[在线咨询](https://console.qcloud.com/workorder/category?level1_id=6&level2_id=350&source=0&data_title=%E5%AE%B9%E5%99%A8%E6%9C%8D%E5%8A%A1TKE&step=1) 打通容器网络。
7. 根据 IDC 使用的协议类型，选择操作方式。
 - 若 IDC 使用的是 BGP 协议，容器网段路由将自动同步。
 - 若是其他协议，需在 IDC 内配置访问容器网段下一跳路由到专线网关。
8. 验证容器与 IDC 互通。

### 通过 VPN 方式互通

#### 配置 SPD 策略

1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc/vpc)。
2. 在左侧导航栏中，单击**VPN链接** > **[VPN通道](https://console.cloud.tencent.com/vpc/vpnConn)**，进入VPN 通道管理页面。
3. [](id:step3)单击需要配置 SPD 策略的本端 VPN 通道的 ID/名称。如下图所示：
![](https://main.qcloudimg.com/raw/515b950b0ec3a540ee4668a36de3575c.png)
4. 在 VPN 通道的详情页面，单击 “SPD策略” 栏下的**编辑**，添加容器网段。如下图所示：
![配置SPD策略](https://main.qcloudimg.com/raw/69255905b783ea74a3c2f984be7aa247.png)
5. [](id:step5)单击**保存**。
6. 重复执行 [步骤3](#step3) - [步骤5](#step5)，配置对端 VPN 通道的 SPD 策略。

#### 添加容器网段

>! 一个子网只能绑定一个路由表，若关联多个路由表，将被替换成最后一个绑定的路由表。
>
1. 在左侧导航栏中，单击 **[路由表](https://console.cloud.tencent.com/vpc/route)**，进入路由表管理页面。
2. [](id:addCIDRStep2)找到 [设置同地域集群间互通](https://cloud.tencent.com/document/product/457/32197) 或者 [设置跨地域集群间互通](https://cloud.tencent.com/document/product/457/32198) 时配置的路由表，单击该路由表的 ID/名称，进入路由表的详情页面。
3. 单击**+新增路由策略**，追加容器网段。
4. [](id:addCIDRStep4)选择**关联子网**页签，单击**新建关联子网**，关联子机所在的子网。
5. 重复执行 [步骤2](#addCIDRStep2) - [步骤4](#addCIDRStep4)，在您对端的路由设备上，添加腾讯云容器所在网段。

#### 预期结果

容器和对端子机可以互通。如下图所示：
![](https://main.qcloudimg.com/raw/118676ef1a435f250ad1a92f11f4cf96.png)
容器间与 VPN 对端子机已经实现互通。
>? 如需云上容器与 IDC 机房通过 IPsec VPN 互通，主要需要设置 **SPD策略**和**路由表**。





