1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc/vpc?rid=1)。
2. 在左侧目录中单击 **VPN 连接** > **VPN 通道**，进入管理页。
3. 选择对应的地域和私有网络，如示例中的**东京**和 `VPC1`，单击**+新建**。
4. VPN 通道基本参数配置。
基本配置包括输入通道名称，选择网关所在地域、网络类型、VPN 网关实例、对端网关实例、预共享密钥、协商类型和通信模式，具体参数含义请参见 [创建 VPN 通道](https://cloud.tencent.com/document/product/554/52864)。
本实例中通信模式为目的路由。
![](https://qcloudimg.tencent-cloud.cn/raw/bc11b74925a1c4d8396fc3b90fb95a9e.png)
5. 高级配置。
本步骤您可以配置 DPD、健康检查、IKE 和 IPSec 等高级参数，本实例使用默认参数。
>?配置 IKE 和 IPSec 时请确保云侧配置和本地配置一致、相匹配，以防因两端协议配置不一致而通道不通。
>
![](https://qcloudimg.tencent-cloud.cn/raw/dac2d681b2afbc62f92780d93839bc63.png)
8. 创建成功后，返回 VPN 通道列表页，单击**更多**，选择**下载配置文件**并完成下载。
 ![](https://qcloudimg.tencent-cloud.cn/raw/541935eddec97bd9fb3c4d180f55b711.png)
