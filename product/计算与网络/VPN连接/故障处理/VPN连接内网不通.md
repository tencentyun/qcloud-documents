## 现象描述

使用VPN连接建立VPC与IDC的通信，VPN通道显示为【已联通】状态，但内网无法联通，现象如下：
VPN通道状态为【已联通】：
![](https://main.qcloudimg.com/raw/f4b080f601219303fab74ad4aa4ddc40.png)
VPC侧服务器pingIDC侧内网IP，无法ping通：
![](https://main.qcloudimg.com/raw/5a4bf0112e8a761e80a69ab05031303c.png)

## 可能原因

通道状态正常但内网却无法联通，可能原因如下：

+ VPC子网路由表未添加指向IDC侧内网网段的路由
+ VPC/IDC侧的安全策略未放通对应源、目IP
+ VPC/IDC侧的内网服务器操作系统的防火墙未放行对端网段
+ VPC/IDC侧的SPD策略未包含该源目IP


## 处理步骤

1. 检查VPC子网路由表中，是否有目的地址为IDC侧内网网段，下一跳地址为对应VPN网关的路由，同时检查IDC侧是否有目的地址为VPC网段，下一跳地址为对应VPN隧道的路由。
    腾讯云侧可查看VPC子网路由表：
	![](https://main.qcloudimg.com/raw/3cc1db15db0b2f669524a004087646ee.png)
	
	IDC侧执行命令检查路由情况（以华为设备为例）：
	display ip routing-table     //查看是否有对应目的地址为云上VPC网段，下一跳为对应VPN隧道的路由
   + 是 => 请执行 [步骤3](#step3)
   + 否 => 请根据业务需求，补全相应路由信息，再执行 [步骤2](#step2)

2. <<span id="step2">检查通信是否恢复正常，即登录VPC/IDC中的一台服务器，ping 对端服务器内网IP。
    + 是 => 通信正常，结束
    + 否 => 请执行 [步骤3](#step3)

3. <span id="step3">检查VPC中服务器关联的安全组和子网关联的网络ACL是否放通来自云下IDC的流量，同时检查IDC侧是否放通来自云上VPC的流量。
VPC中服务器安全组检查：
![](https://main.qcloudimg.com/raw/b452e9b1e2047e8d20e817215253b636.png)
 VPC子网ACL规则检查：
 ![](https://main.qcloudimg.com/raw/c0692870dd748c5ce7990f7d3a189587.png)
 IDC侧安全策略检查（此处以华为防火墙为例）：
 display   current-configuration   configuration security-policy
  + 是 => 请执行 [步骤5](#step5)
  + 否 => 请放通安全组/网ACL/IDC侧安全设备需要互通的内网地址段，再执行 [步骤4](#step4)

4. <span id="step4">检查通信是否恢复正常，即登录VPC/IDC中的一台服务器，ping 对端服务器内网IP。
    + 是 => 通信正常，结束
    + 否 => 请执行 [步骤5](#step5)

5. <span id="step5">分别检查VPC中云服务器和IDC侧内网机器操作系统自带防火墙是否有放通对端网段的策略。
   linux机器查看防火墙：iptables  --list
   Windows机器查看防火墙：控制面板\系统和安全\Windows 防火墙\允许的应用
   + 是 => 请执行 [步骤7](#step7)
   + 否 => 请在内网机器防火墙中放通需要联通的业务网段，再执行 [步骤6](#step6)

6. <span id="step6">检查通信是否恢复正常，即登录VPC/IDC中的一台服务器，ping 对端服务器内网IP。
   + 是 => 通信正常，结束
   + 否 => 请执行 [步骤7](#step7)

7. <span id="step7">分别检查VPC和IDC侧的VPN通道的感兴趣流（SPD策略）是否包含需要互通的内网网段。
   VPC侧SPD策略检查：
	 ![](https://main.qcloudimg.com/raw/7be2d93e0b9384cf2761ecaadca54548.png)
  IDC侧SPD策略检查（此处以华为防火墙为例）：
	display current-configuration configuration acl
   + 是 => 请执行 [步骤9](#step9) 
   + 否 => 请补充缺失的SPD策略，再执行 [步骤8](#step8)

8. <span id="step8">检查通信是否恢复正常，即登录VPC/IDC中的一台服务器，ping 对端服务器内网IP。
   + 是 => 通信正常，结束
   + 否 => 请执行 [步骤9](#step9) 

9. <span id="step9">请收集以上检查信息提交工单或联系设备厂商跟进处理。