本文指导您通过专线接入 + CCN 多路由表 + 私有 NAT 网关的 SNAT 和 DNAT 功能，实现远程数据中心 IDC（Internet Data Center）与云上资源的访问。

## 业务场景
用户使用专线 + 云联网打通腾讯云和客户远程 IDC 实现资源访问，同时期望指定访问 IP 地址并无 IP 冲突，可以通过私网 NAT + 专线方案来实现。
**场景限制：云上业务 VPC未关联云联网实例**。
![](https://qcloudimg.tencent-cloud.cn/raw/d656aae3f47cfe86baea39f22f43ff10.png)

## 操作流程
1. [创建支持多路由表的云联网实例，云联网实例绑定 VPC](#step1)。
2. [创建云联网型私网 NAT 实例，NAT 实例中完成规则设置](#step2)。
3. [创建云联网型专线网关，与云联网实例关联](#step3)。
4. [配置本端/对端 VPC 路由，并发布到云联网上](#step4)。
5. [专线资源：端口资源建设、专用通道创建](#step5)。

## 实操指引
### 前提条件
- 云联网多路由表需开通白名单使用，请 [提交工单](https://console.cloud.tencent.com/workorder/category) 进行反馈。
- 私网 NAT 网关需要开通白名单使用，请 [提交工单](https://console.cloud.tencent.com/workorder/category) 进行反馈。
- 您已经 [申请物理专线](https://cloud.tencent.com/document/product/216/48586)。

### 操作步骤
1. [](id:step1)创建 CCN 资源，将 VPC 关联到新建的 CCN 上，同时该 CCN 实例需开启多路由表功能。
1.1 登录 [云联网控制台](https://console.cloud.tencent.com/vpc/ccn)，单击**新建**，并关联用户原始业务 VPC，详情可参见 [新建云联网实例](https://cloud.tencent.com/document/product/877/18752)。
![](https://qcloudimg.tencent-cloud.cn/raw/954245107aa863a6cd5911d476ecb9df.png)
1.2 开启多路由表功能（需提前加入云联网多路由表白名单，请 [提交工单](https://console.cloud.tencent.com/workorder/category) 申请开通），单击创建好的云联网 ID ，在云联网详情页，单击**路由表**页签，创建两个路由表。
![](https://qcloudimg.tencent-cloud.cn/raw/f594f54fa368c95dd78c106377794963.png)
1.3 用户业务 VPC 加入云联网路由表1，绑定用户业务 VPC 实例，设置路由接受策略。
![](https://qcloudimg.tencent-cloud.cn/raw/af244de76c9b04b961701cb835df3654.png)
![](https://qcloudimg.tencent-cloud.cn/raw/24c657239e40bcb62a7bb8140574f609.png)
2. [](id:step2)创建云联网型私网 NAT 实例，并将私网 NAT 的附属 VPC 关联到云联网多路由表中。
2.1 登录 [私网 NAT 网关控制台](https://console.cloud.tencent.com/vpc/intranat?rid=1) ，在页面上方选择**地域**和**私有网络**后，单击**新建**，创建成功后得到本端 VPC 和对端 VPC 实例。
>?创建 CCN 型私网 NAT 实例（跨城 NAT 能力需开白名单使用，请提交请提交 [工单申请](https://console.cloud.tencent.com/workorder/category)）。
>
![](https://qcloudimg.tencent-cloud.cn/raw/005d0aae3c0a2b8705da78592d9cc756.png)
![](https://qcloudimg.tencent-cloud.cn/raw/e0d7e0ed36b0bd98bd851e365ced2b10.png)
2.2 将 NAT 实例的本端 VPC 绑定到 [第1步](#step1) 创建的云联网实例的路由表1中，同时云联网路由表1中设置路由接受策略。
![](https://qcloudimg.tencent-cloud.cn/raw/f11b4450fca8d4688c158a328135ba94.png)
![](https://qcloudimg.tencent-cloud.cn/raw/f28d7d75d397ef90cc517a2f7bd4c354.png)
2.3 将 NAT 实例的对端 VPC 绑定到 [第1步](#step1) 创建的云联网实例的路由表2中，同时云联网路由表2中设置路由接受策略。
![](https://qcloudimg.tencent-cloud.cn/raw/aee5e86c5aaa7411790b8dd9fae6b927.png)
![](https://qcloudimg.tencent-cloud.cn/raw/1170a7cacb9f43f47ee34b538e22627e.png)
2.4 编辑 NAT 规则：在第三步创建的 NAT 实例中添加本端四层 SNAT 规则（以本端四层规则为例）。
![](https://qcloudimg.tencent-cloud.cn/raw/b3ce400e5273d32b48c9f598964f3295.png)
3. [](id:step3)创建云联网型专线网关，并将该专线网关关联到云联网多路由表中。
3.1 登录 [专线网关控制台](https://console.cloud.tencent.com/vpc/dcgw?rid=1)，选择地域和私有网络后，单击**新建**。创建云联网型专线网关，并且关联 [第1步](#step1) 创建的云联网实例。
![](https://qcloudimg.tencent-cloud.cn/raw/0e20170dd59d8f1e763cfab694542223.png)
3.2 将专线网关加入云联网路由表2中，绑定专线网关实例，同时设置路由接收策略。
![](https://qcloudimg.tencent-cloud.cn/raw/946231dc48e099aef0874f41b5d7ae26.png)
![](https://qcloudimg.tencent-cloud.cn/raw/818373feb4f2cff80c84547941b34198.png)
3.3 专线网关发布 IDC 网段，如果采用自定义方式发布则需要手动新增 IDC 网段。如果需要采用自动传递方式，请 [提交工单](https://console.cloud.tencent.com/workorder/category) 进行反馈。
![](https://qcloudimg.tencent-cloud.cn/raw/c7c8ec096a180c85354d1bcee4206f42.png)
4. [](id:step4)配置本端/对端 VPC 路由，并发布到云联网上。
4.1 本端 VPC 默认路由表增加路由条目如下。目的是 IDC 网段，下一跳为私网 NAT 网关。并且发布到云联网。
![](https://qcloudimg.tencent-cloud.cn/raw/abe3b31eae900b8034beb103b9091b4b.png)
4.2 对端 VPC 默认路由表添加条目如下。目的是 NAT IP 网段，下一跳为私网 NAT 网关。并且发布到云联网。
![](https://qcloudimg.tencent-cloud.cn/raw/0d3576689af1453d360f5cac542c1c07.png)
5. [](id:step5)专线资源创建，可参见：
 - [申请接入物理专线](https://cloud.tencent.com/document/product/216/48586)。
 - [独享专用通道](https://cloud.tencent.com/document/product/216/74769)。
