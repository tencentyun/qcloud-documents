1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc/vpc?rid=1)。
2. 在左侧目录中单击 **VPN 连接** > **VPN 通道**，进入管理页。
3. 选择对应的地域和私有网络，如示例中的**东京**和 `VPC1`，单击**+新建**。
4. 输入通道名称（如：tunnel1），选择 VPN 网关 VPN1 与对端网关 `UserGw1`，并输入预共享密钥（如：`123456`），然后单击**下一步**。
>?可选择是否开启健康检查，如开启，请输入本端地址和对端地址，本端地址为 VPC 主 CIDR 之外的可用 IP，对端地址为 IDC 内可用 IP 地址。默认不开启。
>
![](https://qcloudimg.tencent-cloud.cn/raw/9242378316b6df29091b9f87a2388fbe.png)
5. 选择通信模式为目的路由，并单击**下一步**。
![](https://qcloudimg.tencent-cloud.cn/raw/c349ff82a020df73928929a047e102e7.png)
6. 配置 IKE 参数，需要与本地 IDC 侧配置一致，参数具体信息请参见 [创建 VPN 通道](https://cloud.tencent.com/document/product/554/52864)。本示例中默认的 IKE 参数已与 IDC 侧相匹配。
7. 配置 IPSec 参数，需要与本地 IDC 侧配置一致，参数具体信息请参见 [创建 VPN 通道](https://cloud.tencent.com/document/product/554/52864)。本示例中默认的 IPSec 参数已与 IDC 侧相匹配。
8. 创建成功后，返回 VPN 通道列表页，单击**更多**，选择**下载配置文件**并完成下载。
 ![](https://qcloudimg.tencent-cloud.cn/raw/541935eddec97bd9fb3c4d180f55b711.png)
