## 现象描述
使用VPN连接建立 VPC 与 IDC 的通信，VPN 通道显示为【已联通】状态，但内网无法联通，现象如下：
VPN 通道状态为【已联通】：
![](https://main.qcloudimg.com/raw/f4b080f601219303fab74ad4aa4ddc40.png)
VPC 侧服务器 ping IDC侧内网 IP，无法 ping 通：
![](https://main.qcloudimg.com/raw/5a4bf0112e8a761e80a69ab05031303c.png)

## 可能原因
通道状态正常但内网却无法联通，可能原因如下：
+ VPC 子网路由表未添加指向 IDC 侧内网网段的路由
+ VPC/IDC 侧的安全策略未放通对应源 IP、目的 IP
+ VPC/IDC 侧的内网服务器操作系统的防火墙未放行对端网段
+ VPC/IDC 侧的 SPD 策略未包含该源 IP、目的 IP

## 处理步骤
1. 检查 VPC 子网路由表中，是否有目的地址为 IDC 侧内网网段，下一跳地址为对应 VPN 网关的路由，同时检查 IDC 侧是否有目的地址为 VPC 网段，下一跳地址为对应 VPN 隧道的路由。
    腾讯云侧可查看 [VPC 子网路由表](https://console.cloud.tencent.com/vpc/route?fromNav)：
	![](https://main.qcloudimg.com/raw/3cc1db15db0b2f669524a004087646ee.png)
  IDC 侧执行命令检查路由情况（以华为设备为例）：
	```plaintext
display ip routing-table     //查看是否有对应目的地址为云上 VPC 网段，下一跳为对应 VPN 隧道的路由
   ```
   + 是 => 请执行 [步骤3](#step3)。
   + 否 => 请根据业务需求，补全相应路由信息，再执行 [步骤2](#step2)。
2. [](id:step2)检查通信是否恢复正常，即登录 VPC/IDC 中的一台服务器，ping 对端服务器内网 IP。
>?登录VPC中云服务器请参考 [登录linux实例](https://cloud.tencent.com/document/product/213/5436) 或 [登录Windows实例](https://cloud.tencent.com/document/product/213/5435)。
>
    + 是 => 通信正常，问题解决，结束。
    + 否 => 请执行 [步骤3](#step3)。
3. [](id:step3)检查 VPC 中服务器关联的安全组和子网关联的网络 ACL 是否放通来自云下 IDC 的流量，同时检查 IDC 侧是否放通来自云上 VPC 的流量。
[VPC 中服务器安全组 ](https://console.cloud.tencent.com/vpc/securitygroup)检查：
![](https://main.qcloudimg.com/raw/b452e9b1e2047e8d20e817215253b636.png)
 [VPC 子网 ACL 规则 ](https://console.cloud.tencent.com/vpc/acl)检查：
 ![](https://main.qcloudimg.com/raw/c0692870dd748c5ce7990f7d3a189587.png)
 IDC 侧安全策略检查（此处以华为防火墙为例）：
   ```plaintext
display   current-configuration   configuration security-policy
   ```
  + 是 => 请执行 [步骤5](#step5)。
  + 否 => 请放通安全组/网络 ACL/IDC 侧安全设备需要互通的内网地址段，再执行 [步骤4](#step4)。
4. [](id:step4)检查通信是否恢复正常，即登录 VPC/IDC 中的一台服务器，ping 对端服务器内网 IP。
    + 是 => 通信正常，问题解决，结束。
    + 否 => 请执行 [步骤5](#step5)。
5. [](id:step5)分别检查 VPC 中云服务器和 IDC 侧内网服务器操作系统自带防火墙，是否有放通对端网段的策略。
   linux 服务器查看防火墙：`iptables  --list`
   Windows 服务器查看防火墙：控制面板\系统和安全\Windows 防火墙\允许的应用
   + 是 => 请执行 [步骤7](#step7)。
   + 否 => 请在内网机器防火墙中放通需要联通的业务网段，再执行 [步骤6](#step6)。
6. [](id:step6)检查通信是否恢复正常，即登录 VPC/IDC 中的一台服务器，ping 对端服务器内网 IP。
   + 是 => 通信正常，问题解决，结束。
   + 否 => 请执行 [步骤7](#step7)。
7. [](id:step7)分别检查 VPC 和 IDC 侧的 VPN 通道的感兴趣流（SPD 策略）是否包含需要互通的内网网段。
   [VPC 侧 SPD 策略 ](https://console.cloud.tencent.com/vpc/vpnConn?rid=1)检查：
	 ![](https://main.qcloudimg.com/raw/7be2d93e0b9384cf2761ecaadca54548.png)
  IDC 侧 SPD 策略检查（此处以华为防火墙为例）：
	```plaintext
display current-configuration configuration acl
   ```
   + 是 => 请执行 [步骤9](#step9) 。
   + 否 => 请补充缺失的 SPD 策略，再执行 [步骤8](#step8)。
8. [](id:step8)检查通信是否恢复正常，即登录 VPC/IDC 中的一台服务器，ping 对端服务器内网 IP。
   + 是 => 通信正常，问题解决，结束。
   + 否 => 请执行 [步骤9](#step9) 。
9. [](id:step9)请收集以上检查信息，并[ 提交工单 ](https://console.cloud.tencent.com/workorder/category)或联系设备厂商跟进处理。
