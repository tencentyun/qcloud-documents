## 操作场景
边缘计算机器提供如下两种登录方式：
- [通过 VNC 方式登录](#ECM_VNCLoginLinux)
- [通过 SSH 方式登录](#ECM_SSHLoginLinux)

您可在创建边缘实例成功后，按照本文指引进行登录实例。

## 前提条件

- 已创建边缘计算实例，及获取公网 IP。
- 已获取登录实例的管理员帐号及密码。
如果您忘记密码，请 [重置密码](https://cloud.tencent.com/document/product/1108/44898)。
- 如选择通过 SSH 方式登录 Linux 实例，本地计算机中需已安装 Xshell 软件。

## 操作步骤

<span id="ECM_VNCLoginLinux"></span>
### 通过 VNC 方式登录

1. 登录 [边缘计算机器控制台](https://console.cloud.tencent.com/ecm/overview)，在左侧导航栏中选择【实例列表】。
2. 在【实例列表】，选择需要登录的 Linux 实例，单击【登录】。如下图所示： 
![](https://main.qcloudimg.com/raw/39c88030110b8e87a5f2bc2857596847.png)
3. 在弹出的【登录Linux实例】窗口中，选择【VNC登录】，单击【立即登录】。如下图所示：
![](https://main.qcloudimg.com/raw/344a4741252ffb89e9125c7c5c25be99.png)
4. 在弹出的对话框中，在 “login” 后输入用户名，按 **Enter**。
5. 在 “Password” 后输入密码，按 **Enter**。
输入的密码默认不显示，如下图所示：
![](https://main.qcloudimg.com/raw/bab14d0f56db2f3bc1ab949e08fcc0f0.png)

<span id="ECM_SSHLoginLinux"></span>
### 通过 SSH 方式登录
>? 登录 Linux 实例的远程登录软件有很多种，例如 PuTTY、Xshell 等软件。本操作以 Xshell 6 软件为例，介绍如何在 Windows 系统的本地计算机中使用远程登录软件登录 Linux 实例。
>

1. 打开 Xshell 客户端，单击【新建】。
2. 在打开的新建会话属性窗口中，输入以下内容。如下图所示：
![](https://main.qcloudimg.com/raw/a9687002f69254be9ef82204b2a9f5df.png)
 - 名称：填写会话名称，例如 test。
 - 主机：边缘计算机器实例的公网 IP（登录 [边缘计算机器控制台](https://console.cloud.tencent.com/ecm/instance)，可在实例列表页中获取公网 IP）。
 - 协议：选择 “SSH”。
 - 端口号：边缘计算机器实例的端口，必须设置为22。
3. 单击【连接】。
4. 输入登录的用户名（如 root），单击【确定】。如下图所示：
![](https://main.qcloudimg.com/raw/ca0f13ec931dca98f2150a86ac3f4b7d.png)
5. 输入登录的密码，单击【确定】。如下图所示：
![](https://main.qcloudimg.com/raw/ee835c4ed380a356188aec5023608087.png)
登录完成后，命令提示符左侧将显示当前登录边缘计算机器实例的信息。


