在 VPN 通道创建前，需要创建对端网关：
1. 登录 [腾讯云控制台](https://console.cloud.tencent.com/)，选择【云产品】>【私有网络】进入私有网络控制台。
2. 在左侧目录中单击【VPN 连接】>【VPN 通道】，进入管理页。
3. 选择私有网络所在的地域和私有网络，如示例中的**广州**和`TomVPC`，单击【新建】。
 ![](https://main.qcloudimg.com/raw/ad0f45003e1423b7e6bb8da4bd10a26f.png)
4. 输入通道名称（如：TomVPNConn），选择 VPN 网关`TomVPNGw`与对端网关`TomVPNUserGw`，并输入预共享密钥（如：`123456`），单击【下一步】。
![](https://main.qcloudimg.com/raw/0cb99e940e537500f4c3c8ca16cb535c.png)
5. 输入 SPD 策略来限制本段哪些网段和对端哪些网段通信，在本例中本端网段即为子网 A 的网段`192.168.1.0/24`，对端网段为`10.0.1.0/24`，单击【下一步】。
 ![](https://main.qcloudimg.com/raw/3136826f025a8ce8d3d8dc722d4e0394.png)
6. （可选）配置 IKE 参数，如果不需要高级配置，可直接单击【下一步】。
 ![](https://main.qcloudimg.com/raw/c370884071d8dd5424be80bbef1e9aec.png)
7. （可选）配置 IPsec 参数，如果不需要配置，可直接单击【完成】。
 ![](https://main.qcloudimg.com/raw/6c67f435c015fb6d2e03ed96dc61b7f7.png)
8. 创建成功后，返回 VPN 通道列表页，单击【下载配置文件】并完成下载。
 ![](https://main.qcloudimg.com/raw/3ee49248be8efe8d6910cb85461ef641.png)
