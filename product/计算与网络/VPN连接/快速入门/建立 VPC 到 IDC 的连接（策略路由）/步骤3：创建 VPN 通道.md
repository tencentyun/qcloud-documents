本文为您介绍如何创建 VPN 通道，您可通过如下视频了解 VPN 通道的相关操作。
<div class="doc-video-mod"><iframe src="https://cloud.tencent.com/edu/learning/quick-play/1786-20144?source=gw.doc.media&withPoster=1&notip=1"></iframe></div>


## 操作步骤
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc/vpc?rid=1)。
2. 在左侧目录中单击 **VPN 连接** > **VPN 通道**，进入管理页。
3. 选择对应的地域和私有网络，如示例中的**广州**和 `TomVPC`，单击**+新建**。
 ![](https://main.qcloudimg.com/raw/736f88fd2bbf5e75033d77fcf372586f.png)
4. 输入通道名称（如：TomVPNConn），选择 VPN 网关`TomVPNGw`与对端网关`TomVPNUserGw`，并输入预共享密钥（如：`123456`），单击**下一步**。
>?标签为选配，请保持默认。
>
![](https://main.qcloudimg.com/raw/654520f6843ba2888a1c9b186a1827af.png)
5. 输入 SPD 策略来限制本端哪些网段和对端哪些网段通信，在本例中本端网段即为子网 A 的网段`192.168.1.0/24`，对端网段为`10.0.1.0/24`，单击**下一步**。
![](https://main.qcloudimg.com/raw/0e9c6f49beb02c8db1b8dc2f0456431b.png)
6. （可选）配置 IKE 参数，如果不需要高级配置，可直接单击**下一步**。
 ![](https://main.qcloudimg.com/raw/c370884071d8dd5424be80bbef1e9aec.png)
7. （可选）配置 IPsec 参数，如果不需要配置，可直接单击**完成**。
 ![](https://main.qcloudimg.com/raw/6c67f435c015fb6d2e03ed96dc61b7f7.png)
8. 创建成功后，返回 VPN 通道列表页，单击**更多**，选择**下载配置文件**并完成下载。
 ![](https://main.qcloudimg.com/raw/970810f4cedff81c64e62534680a504d.png)
