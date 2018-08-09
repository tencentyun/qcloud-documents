
腾讯云云联网通过路由策略的即时停用启用，可以实现已使用对等连接的私有网络平滑迁移上云联网。
场景描述：
VPC1 和 VPC2 通过对等连接建立互联，现在需要将二者加入云联网以实现和其他 VPC 的全网互联。

网段 1：广州的 VPC1：192.168.0.0/16，子网 A：192.168.1.0/24。

网段 2：北京的 VPC2：10.0.0.0/16，子网 B：10.0.1.0/24。

![](
https://main.qcloudimg.com/raw/d009ba79874628cda87c03cef628ca37.png)

您需要完成以下步骤： 
1. 新建一个云联网实例（如果已有则不需要），操作见 [新建云联网实例](https://cloud.tencent.com/document/product/877/18752)
2. 将 VPC1、VPC2 与对应的云联网实例关联，操作见 [关联网络实例](https://cloud.tencent.com/document/product/877/18747)
3. 进入 VPC1 的子网 A 的路由表中，【启用】下一跳为该云联网的路由策略，【停用】下一跳为对等连接的路由策略。操作见 [启用路由](https://cloud.tencent.com/document/product/877/18750)、[停用路由](https://cloud.tencent.com/document/product/877/18746)。
4. 进入 VPC2 的子网 B 的路由表中，【启用】下一跳为该云联网的路由策略，【停用】下一跳为对等连接的路由策略。操作见 [启用路由](https://cloud.tencent.com/document/product/877/18750)、[停用路由](https://cloud.tencent.com/document/product/877/18746)。
5. 在该云联网实例的路由表中可以看到目的端为 VPC1、VPC2 中各子网的路由策略。
