1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc/vpc?rid=1)。
2. 在左侧目录中单击【VPN 连接】>【VPN 通道】，进入管理页。
3. 选择对应的地域和私有网络，如示例中的**东京**和 `VPC1`，单击【+新建】。
4. 输入通道名称（如：tunnel1），选择 VPN 网关 VPN1 与对端网关 `UserGw1`，并输入预共享密钥（如：`123456`），然后单击【下一步】。
>?可选择是否开启健康检查，如开启，请输入本端地址和对端地址，本端地址为 VPC 主 CIDR 之外的可用 IP，对端地址为 IDC 内可用 IP 地址。默认不开启。
   >
 ![](https://main.qcloudimg.com/raw/4f72443ea77271f2715a8f34f107c8ff.png)
5. 在 SPD 策略页面配置本端网段和对端网段为0.0.0.0/0，单击【下一步】。
   ![](https://main.qcloudimg.com/raw/645967d6df8fc75c452d884cf4f00fec.png)
6. （可选）配置 IKE 参数，如果不需要高级配置，可直接单击【下一步】。
7. （可选）配置 IPsec 参数，如果不需要配置，可直接单击【完成】。
8. 创建成功后，返回 VPN 通道列表页，单击【更多】，选择【下载配置文件】并完成下载。
![](https://main.qcloudimg.com/raw/41e26d888db90136ded5224544789a00.png)
   
