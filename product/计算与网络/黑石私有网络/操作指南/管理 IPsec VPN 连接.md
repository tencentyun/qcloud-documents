## 操作场景
IPsec VPN 可以在控制台实现全自助配置，您需要完成以下几步才能实现使 IPsec VPN 连接生效
1. 创建 IPsec VPN 网关；
2. 创建对端网关；
3. 创建 IPsec VPN 通道；
4. 在自有 IPsec VPN 网关中加载配置文件；
5. 设置路由表；
6. IPsec VPN 通道激活。

**示例：**
通过 IPsec VPN 连接打通您在广州的私有网络 TomVPC 中子网 A 192.168.1.0/24 与您的 IDC 中子网 10.0.1.0/24，而您 IDC 中 IPsec VPN 网关的公网 IP 是202.108.22.5。
![](https://main.qcloudimg.com/raw/c0d300f44c5b5538b5c264485bde52bc.png)

## 前提条件
已登录 [腾讯云控制台](https://console.cloud.tencent.com)。



## 操作步骤
### 第一步：创建 IPsec VPN 网关
1. 单击导航条【[黑石私有网络](https://console.cloud.tencent.com/vpcbm)】，进入私有网络控制台。
2. 单击左导航栏中【IPsec VPN】>【IPsec VPN 网关】选项卡。
3. 在列表的上端选择私有网络所在广州和私有网络 TomVPC，单击【新建】。
4. 填写 IPsec VPN 网关名称（如：TomVPNGw），IPsec VPN 网关创建完成之后，系统随机分配公网 IP，如：203.195.147.82。


### 第二步：创建对端网关
在 IPsec VPN 通道创建前，需要创建对端网关：
1. 单击导航条【[黑石私有网络](https://console.cloud.tencent.com/vpcbm)】，进入私有网络控制台。
2. 单击左导航栏中【IPsec VPN】>【对端网关】选项卡。
3. 在列表的上端选择地域：广州，单击【新建】。
4. 填写对端网关名称（如：TomVPNUserGw）和 IDC 的 VPN 网关的公网 IP 202.108.22.5。
5. 单击【创建】，即可在对端网关列表查看到新建的对端网关。
 
 


### 第三步：创建 IPsec VPN 通道
创建 IPsec VPN 通道分为以下几个步骤：
1. 单击导航条【[黑石私有网络](https://console.cloud.tencent.com/vpcbm)】，进入私有网络控制台。
2. 单击左导航栏中【IPsec VPN】>【IPsec VPN通道】选项卡。
3. 列表的上端选择私有网络所在广州和私有网络 TomVPC，单击【新建】。
4. 入通道名称（如：TomVPNConn），选择 IPsec VPN 网关 TomVPNGw 与对端网关 TomVPNUserGw，并输入预共享密钥（如：123456）。
5. SPD 策略来限制本段哪些网段和对端哪些网段通信，在本例中本端网段即为子网 A 的网段 192.168.1.0/24，对端网段为 10.0.1.0/24，单击【下一步】。
6. （可选）第三步配置 IKE 参数（可选），如果您不需要高级配置，直接单击【下一步】。
7. （可选）第四步配置 IPsec 参数（可选），如果您不需要配置，可直接单击【完成配置】。
8. 单击 IPsec VPN 通道，下载配置文件。

 


### 第四步：在自有 IPsec VPN 网关中加载配置文件
将第三步生成的配置文件在您 IDC 的 IPsec VPN 网关中加载配置，才可实现 IPsec VPN 通道的网络互通。

### 第五步：修改路由表
截止至第四步，我们已经将一条 IPsec VPN 通道配置成功，但是由于您还未将子网 A 中的流量路由至 IPsec VPN 网关上，子网 A 中的网段还不能与 IDC 中的网段通信。现在您可以开始配置路由：
1. 单击导航条【[黑石私有网络](https://console.cloud.tencent.com/vpcbm)】，进入私有网络控制台。
2. 单击左导航栏中【路由表】，在列表中选择私有网络 TomVPC 所在广州和私有网络 TomVPC，单击私有网络 TomVPC 所关联的路由表 ID 进入该路由表的详情页。
3. 单击【新增路由策略】，输入目的端网段（10.0.1.0/24），下一跳类型选择【IPsec VPN 网关】，再选择刚刚创建的 IPsec VPN 网关 TomVPNGw。
4. 单击【确定】，即完成需要通信的子网的出包路由设定。


### 第六步：IPsec VPN 通道激活
用 VPC 内的物理服务器 ping 对端网段中的 IP 以激活 IPsec VPN 通道。如：TomVPC 内的子网 A 中的物理服务器 ping 10.0.1.1。

#### 查看监控数据
IPsec VPN 通道和 IPsec VPN 网关提供监控数据查看功能。
1. 单击导航条【[黑石私有网络](https://console.cloud.tencent.com/vpcbm)】，进入私有网络控制台。
2. 单击左导航栏中【IPsec VPN】>【IPsec VPN 网关】或者【IPsec VPN 通道】选项卡。
3. 单击列表页中监控一列的图标查看监控数据。

>?IPsec VPN 通道丢包率监控数据反应的是通道探测数据丢包率，并不精确表示通道中的业务数据丢包率。



#### 设置告警
IPsec VPN 网关和 IPsec VPN 通道提供告警功能：
1. 单击顶部导航条【云产品】>【监控与管理】> [【云监控】](https://console.cloud.tencent.com/monitor/overview)，选择左导航栏内的【我的告警】> [【告警策略】](https://console.cloud.tencent.com/monitor/policylist)，单击【新增告警策略】。
2. 填写告警策略名称，在策略类型中选择【黑石私有网络】>【IPsec VPN 网关】或者【IPsec VPN 通道】，然后添加告警触发条件。
3. **关联告警对象**：选择告警接收组，保存后即可在告警策略列表中查看已设置的告警策略。
4. **查看告警信息**：告警条件被触发后，您将接受到短信/邮件/站内信等通知，同时可以在左导航【我的告警】>【告警列表】中查看。有关告警的更多信息，请参考 [创建告警](https://cloud.tencent.com/document/product/248/1073)。
 
 



#### 查看 IPsec VPN 网关详细信息
1. 单击导航条【[黑石私有网络](https://console.cloud.tencent.com/vpcbm)】，进入私有网络控制台。
2. 单击左导航栏中【IPsec VPN】>【IPsec VPN 网关】选项卡。
3. 单击 IPsec VPN 网关 ID 即可进入 IPsec VPN 网关详情页查看 IPsec VPN 网关信息。
 
 
#### 修改 IPsec VPN 通道配置
1. 单击导航条【[黑石私有网络](https://console.cloud.tencent.com/vpcbm)】，进入私有网络控制台。
2. 单击左导航栏中【IPsec VPN】>【IPsec VPN通道】选项卡。
3. 单击 IPsec VPN 通道 ID 即可进入 IPsec VPN 通道详情页查看 IPsec VPN 通道信息。
4. 您可以在基本信息页中修改基本信息和 SPD 策略，或者您可以在高级配置修改 IKE 和 IPsec 配置。


