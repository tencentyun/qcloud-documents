## 操作场景
当资产（例如 CVM）分布在多个 VPC 时，需要通过堡垒机统一进行管理，本文为您详细介绍如何实现跨 VPC 的资产管理。

## 操作步骤
1. 进入 [SaaS 型堡垒机控制台](https://console.cloud.tencent.com/bh)，在左侧导航选择**开通服务**，进入开通服务页面。
2. 在开通服务页面，单击**购买**，进入购买页面，选择合适的规格进行购买。	
![](https://qcloudimg.tencent-cloud.cn/raw/14fb23ee325573cb1c5d23619083daad.png)
3. 购买完成之后，返回开通服务页面，找到新购买的堡垒机服务，单击**开通**。
4. 在开通服务弹窗中，配置地域、VPC 和子网信息后，单击**确定**，完成开通服务。
 - 地域：请选择堡垒机纳管的主机的所属地域，可选择广州、上海、南京、北京、 成都和重庆。
 - VPC：请选择堡垒机纳管的主机的所属 VPC。
 - 子网：选择任意子网均可，但完成初始化操作后，该子网不能被销毁。建议选择主机数量较多的子网。
![](https://qcloudimg.tencent-cloud.cn/raw/5cc20e356cf9222eb50b82e085d2d792.png)
5. 开通多个服务之后，不同 VPC 的资产可由对应 VPC 内的堡垒机进行管理，网络连接链路最短，并且可通过统一的管理入口和运维入口进行管理和维护工作。
![](https://qcloudimg.tencent-cloud.cn/raw/05d7e5e0dcc41c26887068eca84b648b.png)
>?
>- 管理和维护工作操作详情请参见 SaaS 型堡垒机的 [快速入门](https://cloud.tencent.com/document/product/1025/55181)。
>- 除开通堡垒机服务外，还可以通过 [对等连接](https://cloud.tencent.com/document/product/553) 和 [云联网](https://cloud.tencent.com/document/product/215/53884) 来打通堡垒机与 CVM 之间的网络。
