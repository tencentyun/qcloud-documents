本文指导您通过专线接入 + CCN 多路由表 + 私有 NAT 网关的 SNAT 和 DNAT 功能，实现远程数据中心 IDC（Internet Data Center）与云上资源的访问。

## 业务场景
用户使用专线 + 云联网打通腾讯云和客户远程 IDC 实现资源访问，同时期望指定访问 IP 地址并无 IP 冲突，可以通过私网 NAT + 专线方案来实现。
**场景限制：云上业务 VPC未关联云联网实例**。
>?由于`169.254.0.215/32`地址已经被私网 NAT 网关内部使用，如果专用通道采用 BGP 路由方式，建议客户 IDC 不使用该地址，如有疑问，可 [提交工单](https://console.cloud.tencent.com/workorder/category) 咨询。
>
![](https://qcloudimg.tencent-cloud.cn/raw/d656aae3f47cfe86baea39f22f43ff10.png)

## 操作流程
1. [创建支持多路由表的云联网实例，云联网实例绑定 VPC](#step1)
2. [创建云联网型私网 NAT 实例，NAT 实例中完成规则设置](#step2)
3. [创建云联网型专线网关，与云联网实例关联](#step3)
4. [配置本端/对端 VPC 路由，并发布到云联网上](#step4)
5. [专线资源：端口资源建设、专用通道创建](#step5)

## 实操指引
### 前提条件
- 云联网多路由表需开通白名单使用，请 [提交工单](https://console.cloud.tencent.com/workorder/category) 进行反馈。
- 私网 NAT 网关需要开通白名单使用，请 [提交工单](https://console.cloud.tencent.com/workorder/category) 进行反馈。
- 您已经 [申请物理专线](https://cloud.tencent.com/document/product/216/48586)。

### 操作步骤
1. [](id:step1)创建 CCN 资源，将 VPC 关联到新建的 CCN 上，同时该 CCN 实例需开启多路由表功能。
	1. 登录 [云联网控制台](https://console.cloud.tencent.com/vpc/ccn)，单击**新建**，并关联用户原始业务 VPC，详情可参见 [新建云联网实例](https://cloud.tencent.com/document/product/877/18752)。
![](https://qcloudimg.tencent-cloud.cn/raw/954245107aa863a6cd5911d476ecb9df.png)
	2. 在云联网实例页面，单击上述步骤中创建好的**云联网 ID** ，在云联网实例详情页，单击**路由表**页签，创建两个路由表。
>?开启多路由表功能（需提前加入云联网多路由表白名单，请 [提交工单](https://console.cloud.tencent.com/workorder/category) 申请开通）。
>
![](https://qcloudimg.tencent-cloud.cn/raw/f594f54fa368c95dd78c106377794963.png)
	3. [](id:step1-3)用户需要将业务 VPC 加入云联网路由表1，在路由表页面，选择路由表1，单击页面右侧的**绑定实例**，绑定用户业务 VPC 实例。
![](https://qcloudimg.tencent-cloud.cn/raw/af244de76c9b04b961701cb835df3654.png)
	4. 在路由表1中，单击右侧路由表1详情中的**路由接受策略**。
	5. 单击**添加网络实例**，在选择网络实例页面，单击需要添加实例右侧的<img src="https://qcloudimg.tencent-cloud.cn/raw/07bff2616f12f826f2ad00c129d1706b.png" width=1%>，然后单击**完成**。
![](https://qcloudimg.tencent-cloud.cn/raw/5c45f22c6c682c91bea44fc4d4c417bf.png)
	6. 添加完成如下：
 ![](https://qcloudimg.tencent-cloud.cn/raw/24c657239e40bcb62a7bb8140574f609.png)
2. [](id:step2)创建云联网型私网 NAT 实例，并将私网 NAT 的附属 VPC 关联到云联网多路由表中。
	1. 登录 [私网 NAT 网关控制台](https://console.cloud.tencent.com/vpc/intranat?rid=1) ，在页面上方选择**地域**和**私有网络**后，单击**新建**，创建成功后得到本端 VPC 和对端 VPC 实例。
>?创建 CCN 型私网 NAT 实例（跨城 NAT 能力需开白名单使用，请提交 [工单申请](https://console.cloud.tencent.com/workorder/category)）。
>
![](https://qcloudimg.tencent-cloud.cn/raw/005d0aae3c0a2b8705da78592d9cc756.png)
	2. 完成创建后，展示如下：
![](https://qcloudimg.tencent-cloud.cn/raw/e0d7e0ed36b0bd98bd851e365ced2b10.png)
	3. 在 [云联网控制台](https://console.cloud.tencent.com/vpc/ccn) > [步骤1](#step1) 中新建的 CCN 实例 > **路由表**页签，单击将 NAT 实例的本端 VPC 绑定到 [第1步](#step1) 创建的云联网实例的路由表1中。
![](https://qcloudimg.tencent-cloud.cn/raw/f11b4450fca8d4688c158a328135ba94.png)
	4. 同时在云联网路由表1中设置路由接受策略，详细绑定步骤可参见 [步骤1.3](#step1-3)。
![](https://qcloudimg.tencent-cloud.cn/raw/f28d7d75d397ef90cc517a2f7bd4c354.png)
	5. 将 NAT 实例的对端 VPC 绑定到 [第1步](#step1) 创建的云联网实例的路由表2中。
![](https://qcloudimg.tencent-cloud.cn/raw/aee5e86c5aaa7411790b8dd9fae6b927.png)
	6. 同时在云联网路由表2中设置路由接受策略，详细绑定步骤可参见 [步骤1.3](#step1-3)。
![](https://qcloudimg.tencent-cloud.cn/raw/1170a7cacb9f43f47ee34b538e22627e.png)
	7. 在新建的 [私网 NAT 网关](https://console.cloud.tencent.com/vpc/intranat?rid=1) 实例详情页，单击 [步骤2](#step2) 中新建的私网 NAT 实例 ID，在私网 NAT 实例详情页，单击 **SNAT**。
	8. [](id:step2-8)在 **SNAT** 页签中，单击**新建**。在新建的 NAT 实例中添加本端四层 SNAT 规则（以本端四层规则为例）。
![](https://qcloudimg.tencent-cloud.cn/raw/b3ce400e5273d32b48c9f598964f3295.png)
3. [](id:step3)创建云联网型专线网关，并将该专线网关关联到云联网多路由表中。
	1. 登录 [专线网关控制台](https://console.cloud.tencent.com/vpc/dcgw?rid=1)，选择地域和私有网络后，单击**新建**。输入**专线网关名称**、**可用区**、并且关联 [第1步](#step1) 中创建的**云联网实例**，单击**确定**，完成创建云联网型专线网关。
![](https://qcloudimg.tencent-cloud.cn/raw/0e20170dd59d8f1e763cfab694542223.png)
	2. 在 [云联网控制台](https://console.cloud.tencent.com/vpc/ccn) > [步骤1](#step1) 中新建的 CCN 实例 > **路由表**页签，将专线网关加入云联网路由表2中，绑定专线网关实例，同时设置路由接收策略。详细操作可参考 [步骤1.3](#step1-3)。
![](https://qcloudimg.tencent-cloud.cn/raw/946231dc48e099aef0874f41b5d7ae26.png)
![](https://qcloudimg.tencent-cloud.cn/raw/818373feb4f2cff80c84547941b34198.png)
	3. 登录 [专线网关控制台](https://console.cloud.tencent.com/vpc/dcgw?rid=1)，单击在 [步骤3](#step3) 中创建的专线网关实例 ID，在专线网关实例详情页，单击**发布网段**页签，单击**网段详情**模块 的**新建**，以手动新增方式为专线网关发布自定义 IDC 网段。
>?如果需要采用自动传递方式，请 [提交工单](https://console.cloud.tencent.com/workorder/category) 进行反馈。
>
![](https://qcloudimg.tencent-cloud.cn/raw/c7c8ec096a180c85354d1bcee4206f42.png)
4. [](id:step4)在[ 路由表控制台](https://console.cloud.tencent.com/vpc/route?rid=1)，配置本端/对端 VPC 路由，并发布到云联网上。
	1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc/vpc?rid=1)，打开本端 VPC，单击 VPC 实例页。
	2. [](id:step4-2)在 VPC 实例资源模块，单击**路由表**，在本端 VPC 默认路由表的**基本信息**页，单击**新增路由策略**。在**新增路由**页面，配置目的端是 IDC 网段、下一跳类型为私网 NAT 网关。并且发布到云联网，操作可参考如下：
![](https://qcloudimg.tencent-cloud.cn/raw/abe3b31eae900b8034beb103b9091b4b.png)
	3. 对端 VPC 默认路由表添加条目如下，**目的端**为 [步骤2.8](#step2-8)  中创建的 NAT 规则映射 IP 路由，下一跳为私网 NAT 网关。并且发布到云联网，详细操作可参考 [步骤4.2](#step4-2)。
![](https://qcloudimg.tencent-cloud.cn/raw/0d3576689af1453d360f5cac542c1c07.png)
5. [](id:step5)专线资源创建，可参见：
 1. [申请接入物理专线](https://cloud.tencent.com/document/product/216/48586)
 2. 创建 [独享专用通道](https://cloud.tencent.com/document/product/216/74769) 时，绑定 [步骤3](#step3) 中创建的 CCN 型专线网关。
