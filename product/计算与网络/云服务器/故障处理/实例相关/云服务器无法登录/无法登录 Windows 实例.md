以下视频介绍了无法登录 Windows 实例时的排查方法：
<div class="doc-video-mod"><iframe src="https://cloud.tencent.com/edu/learning/quick-play/3399-60001?source=gw.doc.media&withPoster=1&notip=1"></iframe></div>

本文主要介绍无法连接 Windows 实例时对问题进行排查的方法，以及可能导致无法连接 Windows 实例的主要原因，指导您排查、定位并解决问题。

## 可能原因
无法登录 Windows 实例的主要原因包括：
- [密码问题导致无法登录](#CryptographicProblem)
- [带宽利用率过高](#BandwidthUtilization)
- [服务器高负载](#HighServerLoad)
- [远程端口配置异常](#RemotePortConfiguration)
- [安全组规则不当](#SafetyGroupRule)
- [防火墙或者安全软件导致登录异常](#LoginSecuritySoftware)
- [远程桌面连接出现身份验证错误](#AuthenticationError)

## 使用自助诊断工具

腾讯云提供自助诊断工具，可以帮助您判断是否由于带宽、防火墙以及安全组设置等常见问题导致无法连接 Windows 实例。70%的故障可以通过工具定位，您可以根据检测到的原因，定位可能引起无法登录的故障问题。
1. 单击 [自助诊断](https://console.cloud.tencent.com/workorder/check)，打开自助诊断工具。
2. 根据工具界面提示，选择需要诊断的云服务器，单击【开始检测】。如下图所示：
![](https://main.qcloudimg.com/raw/169825c8602f00f5cc867e8f73db269c.png)

如果您的问题无法通过故障排查工具检查，建议您 [通过 VNC 的方式登录](#VNC) 云服务器逐步排查故障。

<span id="TroubleshootingIdeas"></span>
## 故障处理

<span id="VNC"></span>
### 通过 VNC 方式登录

当您无法通过 RDP 或者远程登录软件登录 Windows 实例时，您可以使用腾讯云 VNC 登录的方式登录，帮助您定位故障原因。
1. 登录 [腾讯云控制台](https://console.cloud.tencent.com/cvm/index)。
2. 在实例的管理页面，选择您需要登录的实例，单击【登录】。如下图所示：
![](https://main.qcloudimg.com/raw/038fce530c6c6827796e51d896306a93.png)
3. 在弹出的 “登录Windows实例” 窗口中，选择【其它方式（VNC）】，单击【立即登录】。
>? 登录过程中，如果忘记密码，可以在控制台中重置该实例的密码。具体操作可参考 [重置实例密码](https://cloud.tencent.com/document/product/213/16566)。
>
4. 在弹出的登录窗口中，选择左上角的 “发送远程命令”，单击 Ctrl-Alt-Delete 进入系统登录界面。如下图所示：
![](https://main.qcloudimg.com/raw/2dec43fa6ddb5e442da59c75f7a34b0f.png)


<span id="CryptographicProblem"></span>
### 密码问题导致无法登录

**故障现象**：密码输入错误、忘记密码或者密码重置失败导致登录不成功。
**处理步骤**：请在 [腾讯云控制台](https://console.cloud.tencent.com/cvm/index) 重置该实例的密码，并重启实例。详情请参见 [重置实例密码](https://cloud.tencent.com/document/product/213/16566)。


<span id="BandwidthUtilization"></span>
### 带宽利用率过高

**故障现象**：通过自助诊断工具诊断，提示问题为带宽利用率过高。
**处理步骤**：
1. 通过 [VNC 登录](#VNC) 登录实例。
2. 参考 [带宽占用高导致无法登录](https://cloud.tencent.com/document/product/213/10334#.E9.92.88.E5.AF.B9-windows-.E6.9C.8D.E5.8A.A1.E5.99.A8)，查看实例的带宽使用情况和处理故障。

<span id="HighServerLoad"></span>
### 服务器高负载

**故障现象**：通过自助检查工具或者云监控，显示服务器 CPU 负载过高导致系统无法进行远程连接或者访问非常卡。
**可能原因**：病毒木马、第三方杀毒软件、应用程序异常、驱动异常或者软件后台的自动更新，会造成 CPU 占用率高，导致登录不上云服务器或者访问慢的问题。
**处理步骤**：
1. 通过 [VNC 登录](#VNC) 登录实例。
2. 参考 [Windows 实例：CPU 与内存占用率高导致无法登录](https://cloud.tencent.com/document/product/213/10233)，在 “任务管理器” 中定位高负载的进程。

<span id="RemotePortConfiguration"></span>
### 远程端口配置异常

**故障现象**：远程无法连接，远程访问端口非默认端口、被修改或者3389端口没打开。
**定位思路**：是否能 ping 通实例的公网 IP，通过 telnet 命令检测端口是否打开。
**处理步骤**：具体操作可参考 [端口问题导致无法远程登录](https://cloud.tencent.com/document/product/213/10232)。

<span id="SafetyGroupRule"></span>
### 安全组规则不当

**故障现象**：通过自助检查工具检查，发现安全组规则设置不当导致无法登录。
**处理步骤**：通过 [安全组（端口）验通工具](https://console.cloud.tencent.com/vpc/helper) 进行检查。
>! 远程登录的 Windows 实例需要放通3389端口。
> 
![](https://main.qcloudimg.com/raw/9fc46a7133fdb07b631876cd9fa4c253.png)
如果确定为安全组端口设置问题，可通过工具中的【一键放通】功能放通端口。
![](https://main.qcloudimg.com/raw/c6a26565610a1360f187ee10db12a634.png)
如果您需要自定义设置安全组规则，请参考 [添加安全组规则](https://cloud.tencent.com/document/product/213/39740) 重新配置安全组规则。


<span id="LoginSecuritySoftware"></span>
### 防火墙或者安全软件导致登录异常

**故障现象**：由于云服务器防火墙的配置或者安全软件导致登录异常。
**定位思路**：通过 VNC 登录的方式登录 Windows 实例，检查服务器内部是否开启防火墙，是否有安装360、安全狗等安全软件。
>! 此操作涉及关闭云服务器防火墙，您需要确认自己是否有权限执行此操作。
>
**处理步骤**：关闭防火墙或者安装的安全软件，再次尝试远程连接，确认是否能远程登录成功。以下操作以关闭 Windows Server 2016 实例的防火墙为例。
1. 通过 [VNC 登录](#VNC) 登录实例。
2. 在操作系统界面，单击 <img src="https://main.qcloudimg.com/raw/6e36af2ceb4604b81de13cb42f30e859.png" style="margin: 0;">，选择【控制面板】，打开控制面板窗口。
3. 单击【Windows 防火墙】，进入“Windows 防火墙” 界面。
4. 单击左侧的【启用或关闭 Windows 防火墙】，进入 “自定义设置” 界面。
5. 将【专用网络设置】和【公用网络设置】设置为【关闭 Windows 防火墙】，单击【确定】。
6. 重启实例，再次尝试远程连接，确认是否能远程登录成功。

<span id="AuthenticationError"></span>
### 远程桌面连接出现身份验证错误

**故障现象**：通过远程桌面连接登录 Windows 实例时，出现 “发生身份验证错误，给函数提供标志无效” 或 “发生身份验证错误。要求的函数不受支持” 的报错。
**问题原因**：微软于2018年3月发布了一个安全更新，此更新通过更正凭据安全支持提供程序协议（CredSSP）在身份验证过程中验证请求的方式来修复 CredSSP 存在的远程执行代码漏洞。客户端和服务器都需要安装此更新，否则可能出现问题描述中的情况。
**处理步骤**：推荐通过安装安全更新的方式解决，具体可参考 [Windows 实例：发生身份验证错误](https://cloud.tencent.com/document/product/213/30813)。

## 其它解决方案
通过上述排查后，仍然不能连接 Windows 实例，请您保存自助诊断结果，通过 [在线支持](https://cloud.tencent.com/online-service?from=doc_213
) 进行反馈。
