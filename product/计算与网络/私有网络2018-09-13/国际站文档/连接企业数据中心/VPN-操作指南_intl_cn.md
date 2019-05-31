### 快速入门
IPsec VPN 可以在控制台实现全自助配置，您需要完成以下几步才能实现使 VPN 连接生效：
1. 创建 VPN 网关
2. 创建对端网关
3. 创建 VPN 通道
4. 在自有 IPsec VPN 网关中加载配置文件
5. 设置路由表
6. VPN 通道激活

**示例：**
通过 IPsec VPN 连接打通您在 广州 的私有网络 TomVPC 中子网 A `192.168.1.0/24` 与您的 IDC 中子网 `10.0.1.0/24`，而您 IDC 中 VPN 网关的公网 IP 是 `202.108.22.5`。
<div style="text-align:center">
![](//mc.qcloudimg.com/static/img/0cfc46cf11e4d53164219b1c386509a1/1.png)

</div>
您需要完成以下几个步骤：
#### 第一步：创建 VPN 网关
1)	登录 <a href="https://console.cloud.tencent.com/" target="_blank">腾讯云控制台</a> 点击导航条【私有网络】，进入 <a href="https://console.cloud.tencent.com/vpc/vpc?rid=8" target="_blank">私有网络控制台</a>。
2)	点击左导航栏中【 VPN 连接】-【 VPN 网关】选项卡。
3) 在列表的上端选择私有网络 myVPC 所在**广州**和私有网络`TomVPC`，点击【新建】。
4) 填写 VPN 网关名称（如：TomVPNGw）选择合适的带宽配置并付款后，VPN 网关创建完成之后，系统随机了分配公网 IP，如：`203.195.147.82`。

#### 第二步：创建对端网关
在 VPN 通道创建前，需要创建对端网关：
1)	登录 <a href="https://console.cloud.tencent.com/" target="_blank">腾讯云控制台</a> 点击导航条【私有网络】，进入 <a href="https://console.cloud.tencent.com/vpc/vpc?rid=8" target="_blank">私有网络控制台</a>。
2)	点击左导航栏中【 VPN 连接】-【对端网关】选项卡。
3)	在列表的上端选择地域：**广州**，点击【新建】。
4)	填写对端网关名称（如：TomVPNUserGw）和 IDC 的 VPN 网关的公网 IP `202.108.22.5 `。
5)	点击【创建】，即可在对端网关列表查看到新建的对端网关。

####  第三步：创建 VPN 通道
创建 VPN 通道分为以下几个步骤：

1)	登录 <a href="https://console.cloud.tencent.com/" target="_blank">腾讯云控制台</a> 点击导航条【私有网络】，进入 <a href="https://console.cloud.tencent.com/vpc/vpc?rid=8" target="_blank">私有网络控制台</a>。
2)  点击左导航栏中【 VPN 连接】-【 VPN 通道】选项卡。
3)  在列表的上端选择私有网络 myVPC 所在**广州**和私有网络`TomVPC`，点击【新建】。
4)  输入通道名称（如：TomVPNConn），选择 VPN 网关`TomVPNGw`与对端网关`TomVPNUserGw`，并输入预共享密钥（如：`123456`）。
5)  输入 SPD 策略来限制本段哪些网段和对端哪些网段通信，在本例中本端网段即为子网 A 的网段`192.168.1.0/24`，对端网段为`10.0.1.0/24`，点击【下一步】。
6) （可选）第三步配置 IKE 参数（可选），如果您不需要高级配置可直接点击【下一步】。
7) （可选）第四步配置 IPsec 参数（可选），如果您不需要配置，可直接点击【完成配置】。
8)  点击完成 VPN 通道，下载配置文件。

####  第四步：在自有 IPsec VPN 网关中加载配置文件
将第三步生成的配置文件在您 IDC 的 IPsec VPN 网关中加载配置，才可实现 VPN 通道的网络互通。

####  第五步：修改路由表
截止至第第四步，我们已经将一条VPN 通道配置成功，但是由于您还未将子网 A 中的流量路由至 VPN 网关上，子网 A 中的网段还不能与 IDC 中的网段通信。现在配置路由：
1)	登录 <a href="https://console.cloud.tencent.com/" target="_blank">腾讯云控制台</a> 点击导航条【私有网络】，进入 <a href="https://console.cloud.tencent.com/vpc/vpc?rid=8" target="_blank">私有网络控制台</a>。
2)	点击左导航栏中【子网】，在列表的上端选择私有网络 myVPC 所在**广州**和私有网络`TomVPC`，点击子网 A 所关联的路由表 ID 进入该路由表的详情页。
3)	点击【编辑按钮】，点击【新增一行】，输入目的端网段（`10.0.1.0/24`），下一跳类型选择【 VPN 网关】，再选择刚刚创建的 VPN 网关 `TomVPNGw`。
4)	点击【保存】，即完成需要通信的子网的出包路由设定。

####  第六步：VPN 通道激活
用 VPC 内的云服务器 ping 对端网段中的 IP 以激活 VPN 通道。如：`TomVPC`内的子网 A 中的云服务器 `ping 10.0.1.1`

### 查看监控数据
VPN 通道和 VPN 网关提供监控数据查看功能。
1)	登录 <a href="https://console.cloud.tencent.com/" target="_blank">腾讯云控制台</a> 点击导航条【私有网络】，进入 <a href="https://console.cloud.tencent.com/vpc/vpc?rid=8" target="_blank">私有网络控制台</a>。
2)	点击左导航栏中【 VPN 连接】-【 VPN 网关】或者【 VPN 通道】选项卡。
3)  点击列表页中监控一列的图标查看监控数据。

### 设置告警
VPN 通道提供告警功能：
1)	登录 <a href="https://console.cloud.tencent.com/" target="_blank">腾讯云控制台</a> 点击顶部导航条【云产品】-【监控与管理】-<a href="https://console.cloud.tencent.com/monitor/overview" target="_blank">【云监控】</a>，选择左导航栏内的【我的告警】-<a href="https://console.cloud.tencent.com/monitor/policylist" target="_blank">【告警策略】</a>，点击：新增告警策略。
2)	填写告警策略名称，在策略类型中选择【 VPN 通道】，然后添加告警触发条件。
3)	**关联告警对象**：选择告警接收组，保存后即可在告警策略列表中查看已设置的告警策略。
4)	**查看告警信息**：告警条件被触发后，您将接受到短信/邮件/站内信等通知，同时可以在左导航【我的告警】-【告警列表】中查看。有关告警的更多信息，请参考<a href="https://cloud.tencent.com/doc/product/248/1073" target="_blank">创建告警</a>。

### 查看 VPN 网关详细信息
1)	登录<a href="https://console.cloud.tencent.com/" target="_blank">腾讯云控制台</a>点击导航条【私有网络】，进入<a href="https://console.cloud.tencent.com/vpc/vpc?rid=8" target="_blank">私有网络控制台</a>。
2)	点击左导航栏中【 VPN 连接】-【 VPN 网关】选项卡。
3)  点击 VPN 网关 ID 即可进入 VPN 网关详情页查看 VPN 网关信息。

### 修改 VPN 通道配置
1)	登录 <a href="https://console.cloud.tencent.com/" target="_blank">腾讯云控制台</a> 点击导航条【私有网络】，进入 <a href="https://console.cloud.tencent.com/vpc/vpc?rid=8" target="_blank">私有网络控制台</a>。
2)	点击左导航栏中【 VPN 连接】-【 VPN 通道】选项卡。
3)  点击 VPN 网关 ID 即可进入 VPN 网关详情页查看 VPN 网关信息。
4)  您可以在基本信息页中修改基本信息和 SPD 策略，或者您可以在高级配置修改 IKE 和 Ipsec 配置。
 
