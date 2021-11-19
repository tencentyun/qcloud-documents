以下视频介绍了无法登录 Linux 实例时的排查方法：
<div class="doc-video-mod"><iframe src="https://cloud.tencent.com/edu/learning/quick-play/3398-59999?source=gw.doc.media&withPoster=1&notip=1"></iframe></div>

本文主要介绍无法连接 Linux 实例时对问题进行排查的方法，以及可能导致无法连接 Linux 实例的主要原因，指导您排查、定位并解决问题。


## 问题定位
### 使用自助诊断工具
腾讯云提供自助诊断工具，可以帮助您判断是否由于带宽、防火墙以及安全组设置等常见问题引起。70%的故障可以通过工具定位，您可以根据检测到的原因，定位可能引起无法登录的故障问题。
1. 单击 [自助诊断](https://console.cloud.tencent.com/workorder/check)，打开自助诊断工具。
2. 根据工具界面提示，选择需要诊断的云服务器，单击**开始检测**。如下图所示：
![](https://main.qcloudimg.com/raw/169825c8602f00f5cc867e8f73db269c.png)


### 使用自动化助手发送命令
您可使用自动化助手向实例发送命令，进行问题排查及定位。使用步骤如下：
1. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/index)，在实例列表中单击实例 ID。
2. 在实例详情页中，选择**执行命令**页签，并单击**执行命令**。如下图所示：
![](https://main.qcloudimg.com/raw/ac7ea794c059aaea78281e2d112a3dac.png)
3. 在弹出的“执行命令”窗口中，您可按需选择命令，单击**执行命令**即可执行命令并查看命令结果。
例如，输入新命令 `df -TH` 并单击**执行命令**，即可在不登录实例的情况下查看其结果。如下图所示：
![](https://main.qcloudimg.com/raw/c26ed3d4fd9d6d781048d2aebd994a8a.png)
如需了解自动化助手的更多信息，请参见 [自动化助手](https://cloud.tencent.com/document/product/1340)。


<dx-alert infotype="explain" title="">
如果您的问题无法通过故障排查工具检查，建议您 [通过 VNC 的方式登录](#VNC) 云服务器逐步排查故障。
</dx-alert>




## 可能原因
无法登录 Linux 实例的主要原因包括：
- [SSH 问题导致无法登录](#UseSSHLogin)
- [密码问题导致无法登录](#CryptographicProblem)
- [带宽利用率过高](#BandwidthUtilization)
- [服务器高负载](#HighServerLoad)
- [安全组规则不当](#SafetyGroupRule)

## 故障处理
### 通过 VNC 方式登录[](id:VNC)

当您无法通过标准方式（Webshell）或者远程登录软件登录 Linux 实例时，您可以使用腾讯云 VNC 登录的方式登录，帮助您定位故障原因。
1. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/index)。
2. 在实例的管理页面，选择您需要登录的实例，单击**登录**。如下图所示：
![](https://main.qcloudimg.com/raw/b7f0594ddecad128707ee720502e10b0.png)
3. 在弹出的 “标准登录 | Linux 实例” 窗口中，选择 **VNC登录**。
<dx-alert infotype="explain" title="">
 登录过程中，如果忘记密码，可以在控制台中重置该实例的密码。具体操作可参考 [重置实例密码](https://cloud.tencent.com/document/product/213/16566)。
</dx-alert>
4. 输入用户名和密码登录，完成登录。


### SSH 问题导致无法登录[](id:UseSSHLogin)
**故障现象**：[使用 SSH 登录 Linux 实例](https://cloud.tencent.com/document/product/213/35700) 时，提示无法连接或者连接失败。
**处理步骤**：参考 [无法通过 SSH 方式登录 Linux 实例](https://cloud.tencent.com/document/product/213/37925) 进行排查。

<span id="CryptographicProblem"></span>
### 密码问题导致无法登录
**故障现象**：密码输入错误、忘记密码或者密码重置失败导致登录不成功。
**解决方法**：请在 [腾讯云控制台](https://console.cloud.tencent.com/cvm/index) 重置该实例的密码，并重启实例。
**处理步骤**：重置实例密码的方法请参考 [重置实例密码](https://cloud.tencent.com/document/product/213/16566)。


### 带宽利用率过高[](id:BandwidthUtilization)
**故障现象**：通过自助诊断工具诊断，提示问题为带宽利用率过高。
**处理步骤**：
1. 通过 [VNC 登录](#VNC) 登录实例。
2. 参考 [带宽占用高导致无法登录](https://cloud.tencent.com/document/product/213/10334#.E9.92.88.E5.AF.B9-linux-.E6.9C.8D.E5.8A.A1.E5.99.A8)，查看实例的带宽使用情况和处理故障。


### 服务器高负载[](id:HighServerLoad)
**故障现象**：通过自助检查工具或者云监控，显示服务器 CPU 负载过高导致系统无法进行远程连接或者访问非常卡。
**可能原因**：病毒木马、第三方杀毒软件、应用程序异常、驱动异常或者软件后台的自动更新，会造成 CPU 占用率高，导致登录不上云服务器或者访问慢的问题。
**处理步骤**：
1. 通过 [VNC 登录](#VNC) 登录实例。
2. 参考 [Linux 实例：CPU 与内存占用率高导致无法登录](https://cloud.tencent.com/document/product/213/10310)，在 “任务管理器” 中定位高负载的进程。


### 安全组规则不当[](id:SafetyGroupRule)
**故障现象**：通过自助检查工具检查，发现安全组规则设置不当导致无法登录。
**处理步骤**：通过 [安全组（端口）验通工具](https://console.cloud.tencent.com/vpc/helper) 进行检查。
![](https://main.qcloudimg.com/raw/9fc46a7133fdb07b631876cd9fa4c253.png)
如果确定为安全组端口设置问题，可通过工具中的**一键放通**功能放通端口。
![](https://main.qcloudimg.com/raw/c6a26565610a1360f187ee10db12a634.png)
如果您需要自定义设置安全组规则，请参考 [添加安全组规则](https://cloud.tencent.com/document/product/213/39740) 重新配置安全组规则。



## 其他解决方案
通过上述排查后，仍然不能连接 Linux 实例，请您保存自助诊断结果，通过 [在线支持](https://cloud.tencent.com/online-service?from=doc_213
) 进行反馈。
