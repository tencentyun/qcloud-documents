本文主要介绍无法连接 Linux 实例时对问题进行排查的方法，以及可能导致无法连接 Linux 实例的主要原因，指导您排查、定位并解决问题。

## 可能原因
无法登录 Linux 实例的主要原因包括：
- [密码问题导致无法登录](#CryptographicProblem)
- [带宽利用率过高](#BandwidthUtilization)
- [服务器高负载](#HighServerLoad)
- [远程端口配置异常](#RemotePortConfiguration)
- [安全组规则不当](#SafetyGroupRule)

## 使用自助诊断工具
腾讯云提供自助诊断工具，可以帮助您判断是否由于带宽、防火墙以及安全组设置等常见问题引起。70%的故障可以通过工具定位，您可以根据检测到的原因，定位可能引起无法登录的故障问题。
1. 单击 [自助诊断](https://console.cloud.tencent.com/workorder/check)，打开自助诊断工具。
2. 输入需要诊断的云服务器 instance-id，单击【开始诊断】。如下图所示：
![](https://main.qcloudimg.com/raw/0bea1afc1d29eb4e59dab3f4c6e4eace.png)

如果您的问题无法通过故障排查工具检查，建议您 [通过 VNC 的方式登录](#VNC) 云服务器逐步排查故障。

## 故障处理
### 通过 VNC 方式登录
<span id="VNC"></span>
当您无法通过标准方式（Webshell）或者远程登录软件登录 Linux 实例时，您可以使用腾讯云 VNC 登录的方式登录，帮助您定位故障原因。
1. 登录 [腾讯云控制台](https://console.cloud.tencent.com/cvm/index)。
2. 在实例的管理页面，选择您需要登录的实例，单击【登录】。如下图所示：
![](https://main.qcloudimg.com/raw/b7f0594ddecad128707ee720502e10b0.png)
3. 在弹出的 “登录Linux实例” 窗口中，选择【其它方式（VNC）】，单击【立即登录】。
>? 登录过程中，如果忘记密码，可以在控制台中重置该实例的密码。具体操作可参考 [重置实例密码](https://cloud.tencent.com/document/product/213/16566)。
>
4. 在弹出的对话框中，输入用户名和密码登录，完成登录。

<span id="CryptographicProblem"></span>
### 密码问题导致无法登录
**故障现象**：密码输入错误、忘记密码或者密码重置失败导致登录不成功。
**解决方法**：请在 [腾讯云控制台](https://console.cloud.tencent.com/cvm/index) 重置该实例的密码，并重启实例。
**处理步骤**：重置实例密码的方法请参考 [重置实例密码](https://cloud.tencent.com/document/product/213/16566)。

<span id="BandwidthUtilization"></span>
### 带宽利用率过高
**故障现象**：通过自助诊断工具诊断，提示问题为带宽利用率过高。
**处理步骤**：
1. 通过 [VNC 登录](#VNC) 登录实例。
2. 参考 [带宽占用高导致无法登录](https://cloud.tencent.com/document/product/213/10334#.E9.92.88.E5.AF.B9-linux-.E6.9C.8D.E5.8A.A1.E5.99.A8)，查看实例的带宽使用情况和处理故障。

<span id="HighServerLoad"></span>
### 服务器高负载
**故障现象**：通过自助检查工具或者云监控，显示服务器 CPU 负载过高导致系统无法进行远程连接或者访问非常卡。
**可能原因**：病毒木马、第三方杀毒软件、应用程序异常、驱动异常或者软件后台的自动更新，会造成 CPU 占用率高，导致登录不上云服务器或者访问慢的问题。
**处理步骤**：
1. 通过 [VNC 登录](#VNC) 登录实例。
2. 参考 [Linux 实例：CPU 与内存占用率高导致无法登录](https://cloud.tencent.com/document/product/213/10310)，在 “任务管理器” 中定位高负载的进程。


<span id="RemotePortConfiguration"></span>
### 远程端口配置异常
**故障现象**：远程无法连接，远程访问端口非默认端口、被修改或者22端口没打开。
**定位思路**：是否能 ping 通实例的公网 IP，通过 telnet 命令检测端口是否打开。
**处理步骤**：具体操作可参考 [端口问题导致无法远程登录](https://cloud.tencent.com/document/product/213/10232)。

<span id="SafetyGroupRule"></span>
### 安全组规则不当
**故障现象**：通过自助检查工具检查，发现安全组规则设置不当导致无法登录。
**处理步骤**：通过 [安全组（端口）验通工具](https://console.cloud.tencent.com/vpc/helper) 进行检查。
![](https://main.qcloudimg.com/raw/9fc46a7133fdb07b631876cd9fa4c253.png)
如果确定为安全组端口设置问题，可通过工具中的【一键放通】功能放通端口。
![](https://main.qcloudimg.com/raw/c6a26565610a1360f187ee10db12a634.png)
如果您需要自定义设置安全组规则，请参考 [安全组操作](https://cloud.tencent.com/document/product/213/18197) 重新配置安全组规则。

## 其它解决方案
通过上述排查后，仍然不能连接 Linux 实例，请您保存自助诊断结果，[提交工单](https://console.cloud.tencent.com/workorder/category) 进行反馈。
