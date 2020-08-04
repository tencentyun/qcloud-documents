## 简介

本文将为您介绍收到云服务器 “ping 不可达” 事件告警通知的排查方法和解决方案。您可以参考 [排查步骤](#.E6.8E.92.E6.9F.A5.E6.AD.A5.E9.AA.A4) 恢复告警，如告警通知打扰到您可以参考 [关闭告警功能](#.E5.85.B3.E9.97.AD.E5.91.8A.E8.AD.A6.E5.8A.9F.E8.83.BD)。

## 告警原因及处理方法

ping 不可达告警原因和处理方法对照表：

| 告警原因                                                     | 处理方法                                                     |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| 云服务器 CPU、内存、带宽高负载                                | 参考 [排查步骤1](#.E6.AD.A5.E9.AA.A41.EF.BC.9A.E6.A3.80.E6.9F.A5.E7.9B.91.E6.8E.A7-cpu.E3.80.81.E5.86.85.E5.AD.98.E3.80.81.E5.B8.A6.E5.AE.BD.E7.9B.B8.E5.85.B3.E6.8C.87.E6.A0.87.E7.9B.91.E6.8E.A7.E6.95.B0.E6.8D.AE) 排查并处理异常或 [关闭告警功能](#.E5.85.B3.E9.97.AD.E5.91.8A.E8.AD.A6.E5.8A.9F.E8.83.BD)。 |
| 云服务器处于关机状态                                         | 参考 [排查步骤2](#cvmstate) 排查并开启云服务器或 [关闭告警功能](#.E5.85.B3.E9.97.AD.E5.91.8A.E8.AD.A6.E5.8A.9F.E8.83.BD)。 |
| 云服务器实例关联的安全组限制 ICMP                            | 参考 [排查步骤3](#.E6.AD.A5.E9.AA.A43.EF.BC.9A.E6.A3.80.E6.9F.A5.E5.AE.89.E5.85.A8.E7.BB.84.E7.9A.84-icmp-.E8.AE.BE.E7.BD.AE) 排查并修改安全组 ICMP 配置 或 [关闭告警功能](#.E5.85.B3.E9.97.AD.E5.91.8A.E8.AD.A6.E5.8A.9F.E8.83.BD)。 |
| 云服务器 Windows 防火墙限制、<br>Linux 内核参数或 iptables 限制 ICMP | 参考 [排查步骤4](#.E6.AD.A5.E9.AA.A44.EF.BC.9A.E6.A3.80.E6.9F.A5.E9.98.B2.E7.81.AB.E5.A2.99.E6.88.96-linux-.E5.86.85.E6.A0.B8.E5.8F.82.E6.95.B0-.E5.92.8C-iptables-.E8.AE.BE.E7.BD.AE) 排查并关闭相关限制或 [关闭告警功能](#.E5.85.B3.E9.97.AD.E5.91.8A.E8.AD.A6.E5.8A.9F.E8.83.BD)。 |

> ?无论云服务器是否配置公网 IP 都会做 ping 不可达告警探测。

<span id="排查步骤"></span>

## 排查步骤

### 步骤1：检查监控 CPU、内存、带宽相关指标监控数据

1. 登录 [云监控控制台](https://console.cloud.tencent.com/monitor)。 
2. 单击【云服务器】>告警相关的【实例名称】，查看 CPU 利用率、内存利用率是否达到100%、外网出带宽是否过高或者是否有监控数据断点。
   - 若 CPU 利用率、内存利用率是达到100%或监控数据断点，则说明机器高负载导致的 “ping不可达” 告警，您可以参考 [云服务器 CPU 或内存占用过高]( https://cloud.tencent.com/document/product/248/44698  )  或 [云服务器带宽使用率过高 ]( https://cloud.tencent.com/document/product/248/44701 ) 处理机器高负载故障。
   - 若没有异常请进行下一步骤：[检查云服务器实例状态是否异常](#cvmstate)。
![](https://main.qcloudimg.com/raw/daaa0bcbf567ca455256997f91445cc9.png)
![](https://main.qcloudimg.com/raw/6880845d6a445a8716919832d93e9118.png)

<span id="cvmstate"></span>

### 步骤2：检查云服务器状态

1. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/index)。 
2. 在“实例列表”页面中 ,查看“ping 不可达”告警相关的实例状态是否正常。
- 若状态显示已关机，则说明手动关机导致的 “ping 不可达” 告警。您可以点击【更多】>【实例状态】>【开机】，重启实例，若实例状态已显示运行中，仍未解决问题。可进行下一步：[检查云服务器实例关联的安全组是否允许 ICMP](#.E6.AD.A5.E9.AA.A43.EF.BC.9A.E6.A3.80.E6.9F.A5.E5.AE.89.E5.85.A8.E7.BB.84.E7.9A.84-icmp-.E8.AE.BE.E7.BD.AE)。
![](https://main.qcloudimg.com/raw/a311287dc25eb7ce7a7d445dfa6c0dbe.png)
- 若状态显示运行中可进行下一步：[检查云服务器实例关联的安全组是否允许 ICMP](#.E6.AD.A5.E9.AA.A43.EF.BC.9A.E6.A3.80.E6.9F.A5.E5.AE.89.E5.85.A8.E7.BB.84.E7.9A.84-icmp-.E8.AE.BE.E7.BD.AE)。
![](https://main.qcloudimg.com/raw/f14faddbe07238b82aa889caf2e56396.png)



### 步骤3：检查安全组的 ICMP 设置

1. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/index)。
2. 在“实例列表”页面中，选择产生 “ping 不可达” 告警的实例 ID/实例名，进入该实例的详情页面。
3. 选择【安全组】页签，进入该实例的安全组管理页面。如下图所示，查看该实例所在的安全组的入站规则和出站规则是否允许 ICMP端口协议。
   ![](https://main.qcloudimg.com/raw/e413734149ef1a4d09bfb5d3c6fc47f2.png)
   - 若未允许 ICMP端口协议或列表中没有 ICMP 端口协议，则说明安全组的 ICMP 导致的“ping 不可达” 告警。您可以点击右上角的【编辑规则】，在安全组规则管理页添加/编辑” ICMP 端口协议“，如下图所示。
     ![](https://main.qcloudimg.com/raw/da9f2a4498ba1a1f355a77273e3703e1.png)
   - 若安全组的 “ICMP 端口协议”限制已修改，仍未解决问题。请进行下一步：[检查云服务器 Windows 防火墙或 Linux 内核参数、 iptables 是否有限制](#.E6.AD.A5.E9.AA.A44.EF.BC.9A.E6.A3.80.E6.9F.A5.E9.98.B2.E7.81.AB.E5.A2.99.E6.88.96-linux-.E5.86.85.E6.A0.B8.E5.8F.82.E6.95.B0-.E5.92.8C-iptables-.E8.AE.BE.E7.BD.AE) 。

### 步骤4：检查防火墙或 Linux 内核参数 和 iptables 设置

#### Windows 操作系统 

1. 登录 [云服务器实例](https://cloud.tencent.com/document/product/213/35697)。
2. 打开【控制面板】，选择查看方式为 “小图标” ，单击【Windows 防火墙】。如下图所示：
   ![](https://mc.qcloudimg.com/static/img/e5e6a914dbdaf1f0dab5e89440d7662e/image.png)
3. 在 “Windows 防火墙”界面，选择【高级设置】。如下图所示：
   ![](https://mc.qcloudimg.com/static/img/247440c6c79697133685cbf16544d2cc/image.png)
4. 在弹出的 “高级安全 Windows 防火墙” 窗口中，查看 ICMP 有关的出、入站规则是否被限制。
如下图所示，若出、入站规则中的 Windows 远程管理被禁用，则说明 Windows 防火墙限制导致的 “ping 不可达” 告警，您可以单击鼠标右键启用该规则。
  ![](https://main.qcloudimg.com/raw/f7bda2c5c59f5f66163502c8e1807131.png)

#### Linux 操作系统 

>? Linux 系统是否允许 ping 由内核和 iptables 设置两个共同决定，任何一个限制，都会造成 “ping 不可达” 告警。

**检查内核参数**

1. 登录 [云服务器实例](https://cloud.tencent.com/document/product/213/16515)。
2. 执行以下命令，查看系统 icmp_echo_ignore_all 设置。
```plaintext
cat /proc/sys/net/ipv4/icmp_echo_ignore_all
```
- 若返回结果为0，表示系统允许所有的 ICMP Echo 请求，请 [检查 iptables 设置](#CheckLinuxIptables)。
- 若返回结果为1，表示系统限制所有的 ICMP Echo 请求，则说明 Linux 内核参数限制，导致的 “ping不可达” 告警，请执行 [步骤3](#Linux_step03) 关闭限制。
3. <span id="Linux_step03"></span>执行以下命令，修改内核参数 icmp_echo_ignore_all 的设置。
```plaintext
echo "0" >/proc/sys/net/ipv4/icmp_echo_ignore_all
```

<span id="CheckLinuxIptables"></span>

**检查 iptables 设置**

1. 执行以下命令，查看当前云服务器的防火墙规则以及 ICMP 对应规则是否被限制。
```plaintext
iptables -L
```
	- 若返回结果如下图所示，则表示 iptables 的 ICMP未限制。
		![](https://main.qcloudimg.com/raw/4edec2beb0d2cc175dddadd64ca6c51f.png)
	- 若返回如下图所示，则表示 iptables的 ICMP 被限制。说明  Linux iptables的 ICMP 限制到导致的 “ping不可达” 告警。请参考下文步骤2关闭 iptables 的 ICMP 限制。
	![](https://main.qcloudimg.com/raw/b4ac8726529d4d40a80b2f2c9c87954d.png)
<span id="LinuxIptables"></span>
2. 请执行以下命令，关闭 iptables 的 ICMP 限制。
```plaintext
#Chain INPUT
iptables -A INPUT -p icmp --icmp-type echo-request -j ACCEPT
#Chain OUTPUT
iptables -A OUTPUT -p icmp --icmp-type echo-reply -j ACCEPT
```

若上述步骤无法解决问题，请 [提交工单](https://console.cloud.tencent.com/workorder/category)。

<span id="关闭告警功能"></span>

## 关闭告警功能

### 关闭告警策略

若该告警策略的指标告警和事件告警打扰到您，您可以参考以下步骤关闭该告警策略。

1. 进入 [云监控控制台-告警策略]( https://console.cloud.tencent.com/monitor/policylist)。
2. 找到产生告警策略名称，在“告警启停”一列下，单击 “告警启停” 开关，再单击【确认】即可关闭该策略的告警功能。
   ![](https://main.qcloudimg.com/raw/65fce402b3695e3260e042f3b4d79457.png)

### 仅关闭事件告警

若您还需要该告警策略的指标告警功能，可以参考以下下步骤关闭事件告警功能。

1. 进入 [云监控控制台-告警策略]( https://console.cloud.tencent.com/monitor/policylist )。
2. 找到产生告警策略名称，单击该告警策略名称，进入管理告警策略页。
3. 单击告警触发条件右上角的【编辑】，如下图所示在弹框中取消事件告警的勾选，单击【保存】即可。
   ![](https://main.qcloudimg.com/raw/652a4abb4d42412d043c50a0eb058001.png)





