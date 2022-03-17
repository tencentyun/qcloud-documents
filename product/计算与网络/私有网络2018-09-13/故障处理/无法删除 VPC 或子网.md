## 现象描述
无法删除 VPC 或子网。

## 可能原因
目前 VPC 和子网的删除条件为：
+ VPC：除空子网（指子网内无 IP 占用）、路由表、网络 ACL 之外，没有其他资源（对等连接、基础网络互通、NAT 网关、VPN 网关、专线网关、云联网、私有连接）时，可删除 VPC。
+ 子网：子网内无资源占用 IP。
>?目前子网中涉及 IP 占用的云资源包括：云服务器、内网负载均衡、弹性网卡、HAVIP、云函数 SCF、容器服务、云数据库（例如 MySQL、Redis、TDSQL）等。

基于以上删除条件的分析，VPC 和子网无法立即删除可能存在如下原因：
+ 存在未彻底删除的云资源，如数据库被销毁后，处于**隔离中**，该状态下的数据库资源未彻底释放，会继续占用 VPC 的 IP 资源，导致不能立即删除 VPC 或子网。
+ 部分资源在控制台暂无跳转，导致无法准确释放资源。


## 处理步骤
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc/vpc?rid=1)。
2. 首先单击待删除 VPC 右侧的**删除**，查看弹框中提示 VPC 包含的云资源。
>?此处负载均衡仅为内网负载均衡，公网负载均衡不占用 VPC 内资源。
>
<img  src="https://qcloudimg.tencent-cloud.cn/raw/69b837cee7c6196ad772f733cbefdead.png" width="70%">   
3. 单击 **VPC ID** 进入详情页，单击对应的云资源，跳转到对应的资源界面，并释放云资源。
    + 如果资源无法跳转，请在腾讯云控制台搜索对应产品，前往对应资源控制台，搜索该 VPC ID 下的对应资源，进行资源释放。
    +  如果是云数据库实例，在实例销毁后一定时间实例处于**隔离中**，该状态的实例实际并未释放资源，需执行**立即下线**或等待至实例自动下线后，才可执行删除 VPC 或子网操作。
   <dx-alert infotype="explain" title="">
+ 云数据库中**立即下线**操作为异步操作，部分资源的回收可能存在延迟，不能立即删除 VPC，请稍作等待。
+ 此处列举部分常用资源的释放指导，可参考：[删除云服务器](https://cloud.tencent.com/document/product/213/52425)、[删除负载均衡](https://cloud.tencent.com/document/product/214/15369) 、[删除弹性网卡](https://cloud.tencent.com/document/product/576/18536)、[删除对等连接](https://cloud.tencent.com/document/product/553/18848)、[删除基础网络互通](https://cloud.tencent.com/document/product/215/57840#.E5.88.A0.E9.99.A4.E5.9F.BA.E7.A1.80.E7.BD.91.E7.BB.9C.E4.BA.92.E9.80.9A.3Ca-id.3D.22release.22.3E.3C.2Fa.3E)、[删除 NAT 网关](https://cloud.tencent.com/document/product/552/18183)、[删除 VPN 网关](https://cloud.tencent.com/document/product/554/59292)、[删除专线网关](https://cloud.tencent.com/document/product/216/19258)、[删除流日志](https://cloud.tencent.com/document/product/682/18968)、[删除网络探测](https://cloud.tencent.com/document/product/215/20091#.E5.88.A0.E9.99.A4.E7.BD.91.E7.BB.9C.E6.8E.A2.E6.B5.8B)、[删除 HAVIP](https://cloud.tencent.com/document/product/215/53709)、[销毁云数据库 Redis](https://cloud.tencent.com/document/product/239/30898)、[销毁云数据库 MySQL](https://cloud.tencent.com/document/product/236/30305)。
</dx-alert>
4. 资源完全释放后，执行 [删除 VPC](https://cloud.tencent.com/document/product/215/51961) 和 [删除子网](https://cloud.tencent.com/document/product/215/53533) 验证是否可以删除成功。
   + 删除成功，结束。
   + 依然无法删除，请联系 [售后在线支持](https://cloud.tencent.com/online-service)。
