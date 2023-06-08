使用 VPN 打通 IDC/第三方云商和腾讯云进行资源互访，通常会出现 IP 冲突问题，重新规划网段耗时耗力。本文指导您通过 VPN + CCN 多路由表 + 私有 NAT 网关解决该问题。

## 业务场景
用户使用 VPN 打通腾讯云和客户远程 IDC /第三方云商，实现资源访问，同时期望指定访问 IP 地址并无 IP 冲突，可以通过私网 VPN + NAT + CCN 方案来实现。
![](https://qcloudimg.tencent-cloud.cn/raw/2a8be56cc4bb75019c3c355214998603.png)

## 操作流程
1. 创建支持多路由表的 CCN 实例，并绑定 VPC实例。
2. 创建 CCN 型私网 NAT 实例，并完成规则设置。
3. 配置本端/对端 VPC 路由，并发布到 CCN。
4. 配置 NAT IP 映射规则。
5. 创建 CCN 型 VPN 网关及其资源，并关联与 CCN 实例。

## 前提条件
- 已开启 CCN 多路由表，如需开通，请 [提交工单](https://console.cloud.tencent.com/workorder/category)。
- 已开启私网 NAT 网关特性，如需开通，请 [提交工单](https://console.cloud.tencent.com/workorder/category)。

## 操作步骤
### [](id:step1)步骤一：创建 CCN 实例，并关联业务 VPC
1. 登录 [云联网控制台](https://console.cloud.tencent.com/vpc/ccn)，单击**新建**，并关联业务 VPC，详情可参见 [新建云联网实例](https://cloud.tencent.com/document/product/877/18752)。
![](https://qcloudimg.tencent-cloud.cn/raw/5fcd371c81242f9c1d0ffa5b3efcf5a0.png)
2. 在 CCN 实例列表页面，单击已创建好的**云联网 ID**，然后在 CCN 实例详情页的**路由表**页签，单击**新建路由表**创建两个 CCN 路由表。
>?请确保您已开启 CCN 多路由表功能，如未开启，请 [提交工单](https://console.cloud.tencent.com/workorder/category) 开通。
>
![](https://qcloudimg.tencent-cloud.cn/raw/81fbf24e0f2eff390dbc36b986477b25.png)
[](id:step1-3)3. 将业务 VPC 添加至 CCN 网路由表1。
	1. 在左侧 CCN 路由表列表中选择路由表1，单击**绑定实例**将业务 VPC 实例绑定。
![](https://qcloudimg.tencent-cloud.cn/raw/e5b6a048839ba3a3dc64bb52c42cfcef.png)
	2. 在**路由接收策略**页签，单击**添加网络实例**，然后在**选择网络实例**页面，选择业务 VPC 实例并单击**确定**。
![](https://qcloudimg.tencent-cloud.cn/raw/a617b151d1238032cc56115b7be5f515.png)
添加完成如下：
![](https://qcloudimg.tencent-cloud.cn/raw/1eeb4fc7e3c28e8b2317852d9c95b195.png)

### [](id:step2)步骤二：创建 CCN 型私网 NAT，并添加至 CCN 多路由表。
本步骤您需要在 NAT 侧创建 CCN 型私网 NAT 实例，并将私网 NAT 的附属 VPC 关联到云联网多路由表中。
1. 登录 [私网 NAT 网关控制台](https://console.cloud.tencent.com/vpc/intranat?rid=1)，在页面上方选择地域和私有网络后，单击**新建**。
2. 在私网 NAT 购买页依据界面提示完成创建。创建成功后，自动展示本端 VPC 实例和对端 VPC 实例。
>?请确保已开启私网 NAT 功能，如未开启，请 [提交工单](https://console.cloud.tencent.com/workorder/category) 开通。
>
![](https://qcloudimg.tencent-cloud.cn/raw/5e99927da169c681ba79b05152aefd72.png)
3. 在 [云联网控制台](https://console.cloud.tencent.com/vpc/ccn) 找到步骤一中创建的 CCN 实例，并在其详情页的**路由表**页签，将 NAT 实例的本端 VPC 绑定到 CCN 实例的路由表1中。
![](https://qcloudimg.tencent-cloud.cn/raw/432500f3986db4c1a500ee37e0e409d8.png)
4. 在 CCN 路由表1中设置路由接收策略，详情请参见 [步骤一的步骤3](#step1-3)。
![](https://qcloudimg.tencent-cloud.cn/raw/61c6882e6102e6ca22b5602f9070f466.png)
5. 同理，将 NAT 实例的对端 VPC 绑定到 CCN 实例的路由表2中，并配置路由接收策略。
![](https://qcloudimg.tencent-cloud.cn/raw/0e816f352c077a1e6f3f0974ee887dd6.png)


### 步骤三：配置 IP 映射规则
1. 在 [私网 NAT 网关](https://console.cloud.tencent.com/vpc/intranat?rid=1) 实例详情页，单击 [步骤二](#step2) 中创建的私网 NAT 实例 ID，然后在其详情页单击 **SNAT**。
2. [](id:step3-2)在 SNAT 页签中，单击**新建**依据界面提示进行配置。本处以本端四层规则为例，详情查看 [NAT 网关文档](https://cloud.tencent.com/document/product/552) 或者 [提交工单](https://console.cloud.tencent.com/workorder/category) 咨询。
![](https://qcloudimg.tencent-cloud.cn/raw/28a8800a98aa2320f7510e59a1b3bf97.png)


### 步骤四：配置及发布 VPC 至 CCN 的路由策略
本步骤您需要在 VPC 侧配置本端/对端的 VPC 路由，并发布到云联网。
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc/vpc?rid=1)，找到业务 VPC 并单击 **VPC实例**。
2. 在 VPC 实例详情页面，单击**路由表**，在本端 VPC 默认路由表的基本信息页，单击新增路由策略。
3. 在新增路由页面，配置目的端是 IDC 网段、下一跳类型为私网 NAT 网关。并且发布到云联网。
![](https://qcloudimg.tencent-cloud.cn/raw/2e20ba6ce4238038665216a4b621f6ff.png)
4. 同理，对端 VPC 默认路由表添加条目如下，目的端为 [步骤三里的步骤2](#step3-2) 中创建的 NAT 规则映射 IP 路由，下一跳为私网 NAT 网关，然后发布到云联网。
![](https://qcloudimg.tencent-cloud.cn/raw/a4027974fe74d1ea1290789180bead73.png)

### 步骤五：创建 CCN 型 VPN 网关及其资源，并关联至 CCN 多路由表。
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc/vpc?rid=1)，在左侧导航栏，单击 **VPN 连接** > **VPN 网关**，选择地域和私有网络后，单击**新建**，关联网络选择“云联网”，依据界面提示，完成创建 CCN 型 VPN 网关。详细操作可参考 [创建 VPN 网关](https://cloud.tencent.com/document/product/554/52861)。
![](https://qcloudimg.tencent-cloud.cn/raw/fc125cfe6ea9e24110d2f3fe7aa53946.png)
2. 在 VPN 网关详情页绑定 [步骤一](#step1) 创建的 CCN 实例。
![](https://qcloudimg.tencent-cloud.cn/raw/5a3c4fa52a48c04f4aaa6e132d030042.png)
3. 在 CCN 实例 > 路由表页签，将 VPN 网关加入云联网路由表2中，并绑定 VPN 网关实例，同时设置路由接收策略，详细操作可参考 [步骤一中的步骤3](#step1-3)。
4. 在 VPN 侧 [创建对端网关](https://cloud.tencent.com/document/product/554/52865) 和 [创建 VPN 通道](https://cloud.tencent.com/document/product/554/52864)。
5. （可选）发布路由至 CCN，仅当 VPN 通道为 SPD 策略型时，需要在 VPN 网关手动将路由发布至 CCN。
6. 在用户 IDC 侧配置防火墙或者本地 VPN。

