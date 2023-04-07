本文为您介绍如何创建 VPN 通道，您可通过如下视频了解 VPN 通道的相关操作。
<div class="doc-video-mod"><iframe src="https://cloud.tencent.com/edu/learning/quick-play/1786-20144?source=gw.doc.media&withPoster=1&notip=1"></iframe></div>


## 操作步骤
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc/vpc?rid=1)。
2. 在左侧目录中单击 **VPN 连接** > **VPN 通道**，进入管理页。
3. 选择对应的地域和私有网络，如示例中的**广州**和 `TomVPC`，单击**+新建**。
 ![](https://main.qcloudimg.com/raw/736f88fd2bbf5e75033d77fcf372586f.png)
4. VPN 通道基本参数配置。
基本配置包括输入通道名称，选择网关所在地域、网络类型、VPN 网关实例、对端网关实例、预共享密钥、协商类型和通信模式，具体参数含义请参见 [创建 VPN 通道](https://cloud.tencent.com/document/product/554/52864)。
本实例中通信模式为 SPD 策略，本端网段即为子网 A 的网段`192.168.1.0/24`，对端网段为`10.0.1.0/24`。
![](https://qcloudimg.tencent-cloud.cn/raw/9eb2fbf60166422660453ea22ff69503.png)
5. 高级配置。
本步骤您可以配置 DPD、健康检查、IKE 和 IPSec 等高级参数，本实例使用默认参数。
>?配置 IKE 和 IPSec 时请确保云侧配置和本地配置一致、相匹配，以防因两端协议配置不一致而通道不通。
>
![](https://qcloudimg.tencent-cloud.cn/raw/b865a4fa32b6e6b2bcd78328430d2d54.png)
6. 检查您的配置内容然后单击“创建”。创建成功后，返回 VPN 通道列表页，单击**更多**，选择下载配置文件并完成下载。
