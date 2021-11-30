
## 简介

本文将为您介绍收到云服务器 “ping 不可达” 事件告警通知的排查方法和解决方案。您可以参考 [排查步骤](#paichabuzhou) 恢复告警，如告警通知打扰到您可以参考 [关闭告警功能](#guanbi)。

## 告警原因及处理方法

ping 不可达告警原因和处理方法对照表：

| 告警原因                                                     | 处理方法                                                     |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| 云服务器宕机、内核故障或带宽高负载                           | 参考 [排查步骤一](#buzhou1) 排查并处理异常或 [关闭告警功能](#guanbi)。 |
| 云服务器处于关机状态                                         | 参考 [排查步骤二](#buzhou2) 排查并开启云服务器或 [关闭告警功能](#guanbi)。 |
| 云服务器实例关联的安全组限制 ICMP                            | 参考 [排查步骤三](#buzhou3) 排查并修改安全组 ICMP 配置或 [关闭告警功能](#guanbi)。 |
| 云服务器 Windows 防火墙限制、<br>Linux 内核参数或 iptables 限制 ICMP | 参考 [排查步骤四](#buzhou4) 排查并关闭相关限制或 [关闭告警功能](#guanbi)。 |

>?
>- 云服务器 ping 网络状态由云监控告警系统自动监测，与您是否配置云服务器公网 IP 无关。
>- 如果您的云服务器 iptables 禁止了 Ping 操作，则需要使用非固定 IP 才能 Ping 通。

[](id:paichabuzhou)

## 排查步骤

[](id:buzhou1)

### 步骤一：检查云服务器监控数据

1. 登录 [云监控控制台](https://console.cloud.tencent.com/monitor)。 
2. 单击**云服务器**> 告警相关的**实例名称**，查看云服务器监控数据是否有监控数据断点、监控数据过高异常。
	- 若监控数据出现断点或监控数据过高，可能是云服务器内核故障、宕机或带宽高负载引起，您可以参考 [云服务器—实例相关故障]( https://cloud.tencent.com/document/product/213/17144 ) 进行排查。
	![](https://main.qcloudimg.com/raw/74e937123ed49778ab308e4bf9d67d6c.png)
	- 若无异常请进行下一步骤：[检查云服务器实例状态是否异常](#cvmstate)。

[](id:buzhou2)

### 步骤二：检查云服务器状态


 1. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/index)。 
 2. 在“实例列表”页面中，查看“ping 不可达”告警相关的实例状态是否正常。
- 若状态显示已关机，则说明手动关机导致的 “ping 不可达” 告警。您可以单击**更多** > **实例状态** > **开机**，重启实例，若实例状态已显示运行中，仍未解决问题。可进行下一步：[检查云服务器实例关联的安全组是否允许 ICMP](#buzhou3)。
 ![](https://main.qcloudimg.com/raw/a311287dc25eb7ce7a7d445dfa6c0dbe.png)
- 若状态显示运行中可进行下一步：[检查云服务器实例关联的安全组是否允许 ICMP](#buzhou3)。


>?云监控事件告警暂未过滤手动关机导致的 “ping 不可达”告警，后期我们将对该功能进行优化。

[](id:buzhou3)

### 步骤三：检查安全组的 ICMP 设置

1. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/index)。
2. 在“实例列表”页面中，选择产生 “ping 不可达” 告警的实例 ID/实例名，进入该实例的详情页面。
3. 选择**安全组**页签，进入该实例的安全组管理页面。如下图所示，查看该实例所在的安全组的入站规则和出站规则是否拒绝 ICMP 端口协议或是否添加 ICMP 端口协议。
   ![](https://main.qcloudimg.com/raw/18d39ee7f63505628982a23c3a87add6.png)
   - 系统默认的安全组允许 ICMP 端口协议，若您手动拒绝默认安全组 ICMP 协议或自定义的安全组没有添加 ICMP 协议，都会导致“ping 不可达”告警。您可以单击右上角的**编辑规则**，在安全组规则管理页添加/编辑” ICMP 端口协议“，如下图所示。
     ![](https://main.qcloudimg.com/raw/d1970b158c79c23f4f0307f715f9076e.png)
   - 若安全组的 “ICMP 端口协议” 限制已修改，仍未解决问题。请进行下一步：[检查云服务器 Windows 防火墙或 Linux 内核参数、 iptables 是否有限制](#buzhou4) 。

[](id:buzhou4)

### 步骤四：检查防火墙或 Linux 内核参数和 iptables 设置

#### Windows 操作系统 

1. 登录 [云服务器实例](https://cloud.tencent.com/document/product/213/35697)。
2. 打开**控制面板**，选择查看方式为 “小图标” ，单击**Windows 防火墙**。如下图所示：
   ![](https://mc.qcloudimg.com/static/img/e5e6a914dbdaf1f0dab5e89440d7662e/image.png)
3. 在 “Windows 防火墙”界面，选择**高级设置**。如下图所示：
   ![](https://mc.qcloudimg.com/static/img/247440c6c79697133685cbf16544d2cc/image.png)
4. 在弹出的 “高级安全 Windows 防火墙”窗口中，查看 ICMP 有关的出、入站规则是否被限制。
如下图所示，若出、入站规则中的 Windows  Agent：ICMP 被禁用，则说明 Windows 防火墙限制导致的 “ping 不可达” 告警，您可以单击鼠标右键启用该规则。
  ![](https://main.qcloudimg.com/raw/c4516f61a764456a3d48c289116904d1.png)

#### Linux 操作系统 

>? Linux 系统是否允许 ping 由内核和 iptables 设置两个共同决定，任何一个限制，都会造成 “ping 不可达“告警。

**检查内核参数**

1. 登录 [云服务器实例](https://cloud.tencent.com/document/product/213/16515)。
2. 执行以下命令，查看系统 icmp_echo_ignore_all 设置。
```plaintext
cat /proc/sys/net/ipv4/icmp_echo_ignore_all
```
 - 若返回结果为0，表示系统允许所有的 ICMP Echo 请求，请 [检查 iptables 设置](#CheckLinuxIptables)。
 - 若返回结果为1，表示系统限制所有的 ICMP Echo 请求，则说明 Linux 内核参数限制，导致的 “ping 不可达” 告警，请执行下文关闭限制。
3. [](id:Linux_step03)使用拥有 root 权限的账户执行以下命令，修改内核参数 icmp_echo_ignore_all 的设置。
```plaintext
echo "0" >/proc/sys/net/ipv4/icmp_echo_ignore_all
```

[](id:CheckLinuxIptables)

**检查 iptables 设置**

1. 执行以下命令，查看当前云服务器的防火墙规则以及 ICMP 对应规则是否被限制。
```plaintext
iptables -L
```
	- 若返回结果如下图所示，则表示 iptables 的 ICMP 未限制。
		![](https://main.qcloudimg.com/raw/4edec2beb0d2cc175dddadd64ca6c51f.png)
	- 若返回如下图所示，则表示 iptables 的 ICMP 被限制。说明  Linux iptables 的 ICMP 限制到导致的 “ping 不可达” 告警。请参见下文关闭 iptables 的 ICMP 限制。
	![](https://main.qcloudimg.com/raw/004ce1d45e02a4dc5faa2ad0d3c56a9d.png)
[](id:LinuxIptables)
2. 请执行以下命令，关闭 iptables 的 ICMP 限制。
```plaintext
#Chain INPUT
iptables -A INPUT -p icmp --icmp-type echo-request -j ACCEPT
#Chain OUTPUT
iptables -A OUTPUT -p icmp --icmp-type echo-reply -j ACCEPT
```

若上述步骤仍无法解决问题，请 [提交工单](https://console.cloud.tencent.com/workorder/category) 联系我们。

[](id:guanbi)

## 关闭告警功能

### 关闭告警策略

若该告警策略的指标告警和事件告警打扰到您，您可以参考以下步骤关闭该告警策略。

1. 进入 [云监控控制台-告警策略]( https://console.cloud.tencent.com/monitor/policylist)。
2. 找到产生告警策略名称，在**告警启停**一列下，单击 “告警启停” 开关，再单击**确认**即可关闭该策略的告警功能。
   ![](https://main.qcloudimg.com/raw/65fce402b3695e3260e042f3b4d79457.png)

### 仅关闭事件告警

若您还需要该告警策略的指标告警功能，可以参考以下步骤关闭事件告警功能。

1. 进入 [云监控控制台-告警策略]( https://console.cloud.tencent.com/monitor/policylist )。
2. 找到产生告警策略名称，单击该告警策略名称，进入管理告警策略页。
3. 单击告警触发条件右上角的**编辑**，如下图所示在弹框中取消事件告警的勾选，单击**保存**即可。
   ![](https://main.qcloudimg.com/raw/652a4abb4d42412d043c50a0eb058001.png)


