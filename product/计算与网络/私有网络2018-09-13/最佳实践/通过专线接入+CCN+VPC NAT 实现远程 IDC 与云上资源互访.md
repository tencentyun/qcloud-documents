本文指导您通过专线接入 + CCN 多路由表 + 私有 NAT 网关的 SNAT 和 DNAT 功能，实现远程数据中心 IDC（Internet Data Center）与云上资源的访问。

## 业务场景
用户使用专线 + 云联网打通腾讯云和客户远程 IDC 实现资源访问，同时期望指定访问 IP 地址并无 IP 冲突，可以通过私网 NAT + 专线方案来实现。
**场景限制：云上业务 vpc 未关联云联网实例**。
![](https://qcloudimg.tencent-cloud.cn/raw/096c8ed8f0e5102b98e0dd5d0ab7217e.png)

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

## 操作步骤
1. [](id:step1)创建 CCN 资源，将VPC关联到新建的CCN上，同时该CCN实例需开启多路由表功能。
1.1 新建云联网实例，并绑定用户原始业务VPC，详情请参见 [新建云联网实例](https://cloud.tencent.com/document/product/877/18752)。
![](https://qcloudimg.tencent-cloud.cn/raw/954245107aa863a6cd5911d476ecb9df.png)
1.2 开启多路由表功能（需提前加入云联网多路由表白名单，请 [提交工单](https://console.cloud.tencent.com/workorder/category) 申请开通），单击创建好的云联网 ID ，在云联网详情页，单击**路由表**页签，创建两个路由表。
![](https://qcloudimg.tencent-cloud.cn/raw/f594f54fa368c95dd78c106377794963.png)
2. [](id:step2)创建云联网型私网NAT，并将私网NAT的附属VPC关联到云联网多路由表中。
2.1 在 [私网 NAT 创建页面](https://console.cloud.tencent.com/vpc/intranat?rid=1) 创建 CCN 型私网 NAT 实例（跨城NAT能力需开白名单使用，请提交请提交 [工单申请](https://console.cloud.tencent.com/workorder/category)），创建成功后得到本端vpc和对端vpc实例。
![](https://qcloudimg.tencent-cloud.cn/raw/005d0aae3c0a2b8705da78592d9cc756.png)
![](https://qcloudimg.tencent-cloud.cn/raw/e0d7e0ed36b0bd98bd851e365ced2b10.png)
2.2 NAT 实例的本端 vpc 绑定到 [第1步](#step1) 创建的云联网实例的路由表1中，同时云联网路由表1中设置路由接受策略。
![](https://qcloudimg.tencent-cloud.cn/raw/f11b4450fca8d4688c158a328135ba94.png)
![](https://qcloudimg.tencent-cloud.cn/raw/f28d7d75d397ef90cc517a2f7bd4c354.png)
2.3 将NAT实例的对端vpc加到第1步创建的云联网实例的路由表2中，同时云联网路由表2中设置路由接受策略。
![](https://qcloudimg.tencent-cloud.cn/raw/aee5e86c5aaa7411790b8dd9fae6b927.png)
![](https://qcloudimg.tencent-cloud.cn/raw/1170a7cacb9f43f47ee34b538e22627e.png)
2.4 编辑 NAT 规则：在第三步创建的NAT实例中添加本端四层SNAT规则（以本端四层规则为例）。
3. [](id:step3)创建云联网型专线网关，并将该专线网关关联到云联网多路由表中。
3.1 在 [专线网关创建页](https://console.cloud.tencent.com/vpc/dcgw?rid=1) 面创建云联网型专线网关,并且关联第1步创建的云联网实例。
![](https://qcloudimg.tencent-cloud.cn/raw/0e20170dd59d8f1e763cfab694542223.png)
3.2 把专线网关加入云联网路由表2中，绑定vpc实例，同时设置路由接收策略。
![](https://qcloudimg.tencent-cloud.cn/raw/063920cddc8bd96738a4d22c8bd1d589.png)
![](https://qcloudimg.tencent-cloud.cn/raw/8c9d7aa450b6e4756be540401200a791.png)
3.3 专线网关发布IDC网段，如果采用自定义方式发布则需要手动新增IDC网段。如果需要采用自动传递方式，请 [提交工单](https://console.cloud.tencent.com/workorder/category) 进行反馈。
4. [](id:step4)配置本端/对端VPC路由，并发布到云联网上。
4.1 本端VPC默认路由表增加路由条目如下。目的是IDC网段，下一跳为私网NAT网关。并且发布到云联网。
![](https://qcloudimg.tencent-cloud.cn/raw/abe3b31eae900b8034beb103b9091b4b.png)
4.2 对端VPC默认路由表添加条目如下。目的是NAT IP网段，下一跳为私网NAT网关。并且发布到云联网。
![](https://qcloudimg.tencent-cloud.cn/raw/0d3576689af1453d360f5cac542c1c07.png)
5. [](id:step5)专线资源创建，可参见：
- [申请接入物理专线](https://cloud.tencent.com/document/product/216/48586)。
- [独享专用通道](https://cloud.tencent.com/document/product/216/74769)。