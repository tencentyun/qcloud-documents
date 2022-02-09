VPN 通道创建后，您可以修改通道基本信息中的名称、预共享密码、标签信息、SPD 策略，以及高级配置中的 IKE 配置和 IPsec 配置，也可以重置通道的所有配置。

## 对系统的影响
重置操作会中断现有 VPN 通道数据传输并重新建立连接，请提前做好网络变更准备。

## 操作步骤
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc/vpc?rid=1)。
2. 在左侧目录中单击 **VPN 连接** > **VPN 通道**，进入管理页。
3. 在“VPN 通道”管理页面，单击需要修改的 VPN 通道实例 ID，进入详情页。
4. 在“基本信息”页面，单击图中的编辑图标，可修改 VPN 通道名称、预共享密码、标签信息、以及 SPD 策略规则，修改后单击**保存**即可。
<img src="https://qcloudimg.tencent-cloud.cn/raw/7d73b1761518e3bec0063bd643c48c71.png" width="70%"> 
	其中，通道名称和预共享密钥也可以在 VPN 通道列表界面单击编辑图标直接修改，如下图所示。
![](https://qcloudimg.tencent-cloud.cn/raw/4237570474dd592fcc684b4118294f0d.png)
5. 单击**高级配置**选项卡，可在高级配置中修改 IKE 配置 和 IPsec 配置，修改后单击**保存**即可。
![](https://qcloudimg.tencent-cloud.cn/raw/d8e818813c87dee1d97269ca0716df4b.png)
6. 单击**重置**将重置所有通道配置，请知悉风险并谨慎操作。
![](https://qcloudimg.tencent-cloud.cn/raw/1fa1ebc07d3376aee3539cc11b556842.png)
