## 现象描述

使用VPN连接建立VPC与IDC的通信，完成配置后，发现VPN通道状态为【未联通】。
![](https://main.qcloudimg.com/raw/d37bb0a17e5b7ab17db816872ff5dfa5.png)

## 可能原因

通道状态异常，一般有如下可能原因：
+ 无流量激活通道
+ VPN网关公网IP不通
+ 安全策略配置不正确
+ 协商参数、协商模式不一致


## 处理步骤

1. 登录VPC中的一台服务器，ping 对端IDC侧服务器的内网IP来激活通道。
    + 如果ping通，表示通道已激活，查看VPN通道状态是否已联通，如已联通，则问题解决，结束；如未联通，则继续执行步骤2。
    + 如果ping不通，请直接执行[步骤2](#step2)。

2. <span id="step2">请登录IDC侧的VPN设备，ping 腾讯云侧VPN网关的公网IP（本例假设VPN网关公网IP为139.186.120.129），查看是否可以ping通。
    + 是 => 请执行[步骤4](step4)
    + 否 => 请执行[步骤3](step3)
		![](https://main.qcloudimg.com/raw/535e4d2303f75406fb7675ef52a7316a.png)

3. <span id="step3">请检查IDC侧公网网络连接状态，是否可以正常连接到互联网。
    + 是 => 请执行[步骤4](step4)
    + 否 =>请修复本地网络后，再查看VPN通道状态是否已联通，如已联通，则问题解决，结束；如未联通，则继续执行[步骤4](step4)

4. <span id="step4">查看IDC侧VPN设备的安全策略，是否允许腾讯云侧的VPN网关公网地址（端口号）以及需要互通的内网地址。
    display current-configuration configuration security-policy      //此处以华为防火墙为例
  + 是 => 请执行[步骤5](step5)
  + 否 => 请修改安全策略，放通腾讯云侧VPN网关的IP以及对应感兴趣流策略，再查看VPN通道状态是否已联通，如已联通，则问题解决，结束；如未联通，则继续执行[步骤5](step5)

5. <span id="step5">比对腾讯云侧VPN网关与对端IDC的VPN设备协商参数（IKE、IPsec配置）及协商模式（主模式main/野蛮模式aggressive）是否一致。
   腾讯云侧配置参数可在 [VPN通道控制台](https://console.cloud.tencent.com/vpc/vpnConn?rid=17) 相应通道详情的高级配置中查看：
   ![](https://main.qcloudimg.com/raw/003f674d04966acebd7b713a64743609.png)
	 IDC侧设备配置参数可通过如下命令获取（此处以华为防火墙为例）：
	 display   current-configuration   configuration ike profile   
   display   current-configuration   configuration ipsec  policy  
   + 是 => 请执行[步骤6](step6)
   + 否 => 请修改相应参数，确保两端配置一致，然后再查看VPN通道状态是否已联通，如已联通，则问题解决，结束；如未联通，则继续执行[步骤6](step6)

6. <span id="step6">请收集以上检查信息，并提交工单或联系设备厂商跟进处理。

