
## 操作场景

本文介绍如何在 Windows 系统的本地计算机中通过远程桌面登录 Windows 实例。

## 前提条件

- 已创建边缘计算实例，及获取公网 IP。
- 已获取远程登录 Windows 实例需要使用实例的管理员帐号和对应的密码。
如果您忘记密码，请 [重置密码](https://cloud.tencent.com/document/product/1108/44898)。

## 操作步骤

>? 以下操作步骤以 Windows 10 操作系统为例。
>
1. 在本地 Windows 计算机上，右键单击 <img src="https://main.qcloudimg.com/raw/6e36af2ceb4604b81de13cb42f30e859.png" style="margin: 0;"></img>，选择【运行】。
2. 在打开的运行窗口中，输入 **mstsc**，按 **Enter**，打开远程桌面连接对话框。如下图所示：
![](https://main.qcloudimg.com/raw/249d8c278ba187ea7481d11d6b5def34.png)
3. 在【计算机】后面，输入 Windows 实例的公网 IP，单击【连接】。
4. 在弹出的 “Windows 安全” 窗口中，输入实例的管理员帐号和密码，如下图所示：
![](https://main.qcloudimg.com/raw/0efb58f20870ea0ec2007747d7912694.png)
>? 若弹出 “是否信任此远程连接？” 对话框，可勾选 “不再询问我是否连接到此计算机”，单击【连接】。
>
5. 单击【确定】，即可登录到 Windows 实例。

