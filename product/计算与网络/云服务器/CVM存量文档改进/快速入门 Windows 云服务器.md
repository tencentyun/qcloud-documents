本文主要介绍如何从零开始，以最简单的方式搭建一个 Windows 云服务器。

如果您之前没有搭建云服务器的经验，建议您按照本文介绍的方式来购买和配置您的第一台云服务器。

云服务器按照系统的版本分为 Windows 云服务器和 Linux 云服务器，如果您想了解如何从零开始搭建一台 Linux 云服务器，可以参考 [零基础配置 Linux 云服务器]([https://cloud.tencent.com/document/product/213/2936)。


## 步骤一：注册腾讯云账号
如果您已在腾讯云注册，可忽略此步骤。
<div style="background-color:#5291F8; width: 170px; height: 35px; line-height:35px; text-align:center;"><a href="https://cloud.tencent.com/register?s_url=https%3A%2F%2Fcloud.tencent.com%2F" target="_blank"  style="color: white; font-size:16px;">点此注册腾讯云账号</a></div>


## 步骤二：购买 Windows 云服务器

<div style="background-color:#5291F8; width: 190px; height: 35px; line-height:35px; text-align:center;"><a href="https://buy.cloud.tencent.com/cvm?tab=lite" target="_blank"  style="color: white; font-size:16px;">点此进入快速购买页面</a></div>
</br>

![](https://main.qcloudimg.com/raw/4e0ce6a41f857a82ae6387f4a5db208a.jpg)

- **地域**：选择与您最近的一个地区，例如我在 “深圳”，地域选择 “广州”。
- **机型**：选择您需要的云服务器机型配置。这里我们选择 “入门设置（1核1GB）”。 
- **镜像**：选择您需要的云服务器操作系统。这里我们选择 “Windows Server 2012 R2 数据中心版 64位中文版”。
- **公网带宽**：勾选后会为您分配公网 IP，默认为 “1Mbps”，您可以根据需求调整。
- **购买数量**：默认为 “1台”。
- **购买时长**：默认为 “1个月”。

当您付费完成后，即完成了云服务器的购买。云服务器可以作为个人虚拟机或者您建站的服务器。接下来，您可以登录您购买的这台服务器。

## 步骤三：登录云服务器

>! 通过快速配置购买的云服务器，系统将为您自动分配云服务器登录密码并发送到您的站内信中。此密码为登录云服务器的凭据。<div style="background-color:#5291F8; width: 160px; height: 35px; line-height:35px; text-align:center;"><a href="https://console.cloud.tencent.com/message" target="_blank"  style="color: white; font-size:16px;">点此获取初始密码</a></div>
>
 
1. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm)，在实例列表中找到您刚购买的云服务器，在右侧操作栏中单击【登录】。
![](https://main.qcloudimg.com/raw/25d5fed7a99dda8a738490b2f89f3044.jpg)
2. 根据您本地机器的操作系统类型，选择不同的登录方式：
	- 如果您的本地机器是 Windows 操作系统，请先下载 RDP 文件到本地，再双击打开刚下载的 RDP 文件，输入云服务器的帐号和密码登录。
	- 如果您的本地机器是 Linux 操作系统，推荐您首先安装 rdesktop 软件，并按照 [Linux 系统使用 RDP 登录](https://cloud.tencent.com/document/product/213/5435#linux-.E7.B3.BB.E7.BB.9F.E4.BD.BF.E7.94.A8-rdp-.E7.99.BB.E5.BD.95)。
	- 如果您的本地机器是 MacOS 操作系统，推荐您首先安装 Microsoft Remote Desktop for Mac 软件，并按照  [MacOS 系统使用 RDP 登录](https://cloud.tencent.com/document/product/213/5435#macos-.E7.B3.BB.E7.BB.9F.E4.BD.BF.E7.94.A8-rdp-.E7.99.BB.E5.BD.95)。
	>! 您可以在 [站内信](https://console.cloud.tencent.com/message) 查找云服务器的初始密码，也可以通过 [重置实例密码](https://cloud.tencent.com/document/product/213/16566) 后再登录。
3. 输入云服务器的用户名和密码，即可正常登录。

## 下一步操作：使用云服务器

当您登录云服务器后，即可在云服务器上进行您所需要的操作。常用的任务包括：
- [将您本地的文件上传到云服务器上](https://cloud.tencent.com/document/product/213/38221)
- [在云服务器上搭建网站](https://cloud.tencent.com/document/product/213/38248)

您可以根据需要，按照文档指引进行下一步操作。

## 出现问题？
非常抱歉您在使用时出现问题，您可以第一时间通过 [提交工单](https://console.cloud.tencent.com/workorder/category) 联系我们，也可以先参考相关文档进行问题定位和解决。
以下是用户在使用云服务器的时出现的常见问题，建议您先参考文档进行问题定位和解决。
- 忘记云服务器登录密码？
请参考 [重置密码](https://cloud.tencent.com/document/product/213/16566)。
- 登录不成功？如何定位问题？
请参考 [无法登录 Windows 实例](https://cloud.tencent.com/document/product/213/10339)。
