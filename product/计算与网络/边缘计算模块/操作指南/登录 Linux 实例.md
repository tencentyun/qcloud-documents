## 操作场景

登录 Linux 实例的远程登录软件有很多种，例如 PuTTY、Xshell 等软件。本文以 Xshell 6 软件为例，介绍如何在 Windows 系统的本地计算机中使用远程登录软件登录 Linux 实例。
您如需使用 PuTTY 软件进行登录，请参考 [使用远程登录软件登录 Linux 实例](https://cloud.tencent.com/document/product/213/35699) 文档。

## 前提条件

- 已创建边缘计算实例，及获取公网 IP。
- 已获取登录实例的管理员帐号及密码。
如果您忘记密码，请 [重置密码](https://cloud.tencent.com/document/product/1108/44898)。
- 本地计算机中已安装 Xshell 软件。

## 操作步骤

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

