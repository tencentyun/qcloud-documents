## 现象描述
无法删除 VPC 或子网。

## 可能原因
目前 VPC 和子网的删除条件为：
+ VPC：除空子网（指子网内无 IP 占用）、路由表、网络 ACL 之外，没有其他资源（对等连接、基础网络互通、NAT 网关、VPN 网关、专线网关、云联网、私有连接）时，可删除 VPC。
+ 子网：子网内无资源占用 IP。
>?目前子网中涉及 IP 占用的云资源包括：云服务器、内网负载均衡、弹性网卡、HAVIP、云函数 SCF、容器服务、云数据库（例如 MySQL、Redis、TDSQL）等。


基于以上删除条件的分析，VPC 和子网无法立即删除可能存在如下原因：
+ 存在未彻底删除的云资源，如数据库被销毁后，处于“隔离中”，该状态下的数据库资源未内彻底释放，会继续占用 VPC 的 IP 资源，导致不能立即删除 VPC 或子网。
+ 部分资源在控制台暂无跳转，导致无法准确释放资源。


## 处理步骤
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc/ccn)。
2. 单击 VPC ID 进入详情页，可查看 VPC 包含的云资源。
3. 单击对应的云资源，系统将跳转到对应的资源界面。
![](https://qcloudimg.tencent-cloud.cn/raw/13abd0d618b4452956935078b85904ef.png)
4. 在对应的云资源界面释放云资源，然后再 [删除 VPC](https://cloud.tencent.com/document/product/215/51961) 和 [删除子网](https://cloud.tencent.com/document/product/215/53533)。
 可能存在如下情况，例如：
 处于“隔离中”的 MySQL 数据库实际并未释放资源，需执行“立即下线”或等待至实例下线后，再删除 VPC。
>!此处执行“立即下线”操作为异步操作，部分资源的回收可能存在延迟，不能立即删除 VPC，请稍作等待。也可参考对应资源的产品文档了解更多信息，如 [下线隔离状态的云数据库实例](https://cloud.tencent.com/document/product/236/36197)。
>
 ![](https://qcloudimg.tencent-cloud.cn/raw/d422a4ca0b81bd62d4cbb662110de271.png)
6. 如存在部分资源无法跳转，请进入对应云资源控制台进行搜索，释放云资源后，再执行删除 VPC 操作，如依然无法删除，请联系 [售后在线支持](https://cloud.tencent.com/online-service)。
