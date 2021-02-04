## 步骤3：创建VPN通道

1. 登录 [腾讯云控制台](https://console.cloud.tencent.com/)，选择【云产品】>【网络】>【私有网络】进入私有网络控制台。
2. 在左侧目录中单击【VPN 连接】>【VPN 通道】，进入管理页。
3. 选择对应的地域和私有网络，如示例中的**东京**和`VPC1`，单击【新建】。
4. 输入通道名称（如：tunnel1），选择 VPN 网关VPN1与对端网关`UserGw1`，并输入预共享密钥（如：`123456`）则需要输入单击【下一步】。
	>?可选择是否开启健康检查，如开启，请输入本端地址和对端地址，本端地址为VPC主CIDR之外的可用IP，对端地址为IDC内可用IP地址。默认不开启，本例使用默认值。
	>
![](https://main.qcloudimg.com/raw/4f72443ea77271f2715a8f34f107c8ff.png)
5. 在SPD策略页面配置本端网段和对端网段为0.0.0.0/0，单击【下一步】。
   ![](https://main.qcloudimg.com/raw/645967d6df8fc75c452d884cf4f00fec.png)
6. （可选）配置 IKE 参数，如果不需要高级配置，可直接单击【下一步】。
7. （可选）配置 IPsec 参数，如果不需要配置，可直接单击【完成】。
8. 重复如上步骤，为VPC2创建VPN通道。如下为VPC1和VPC2 的VPN通道。
   ![](https://main.qcloudimg.com/raw/127f06ce2d47a39d20ea62f1d9e12d64.png)