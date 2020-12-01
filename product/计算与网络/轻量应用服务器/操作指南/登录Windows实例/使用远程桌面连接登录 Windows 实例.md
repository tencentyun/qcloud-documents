## 操作场景
本文介绍如何在 Windows 系统的本地计算机中通过远程桌面登录 Windows 实例。

## 适用本地操作系统
Windows

## 前提条件

- 您已获取远程登录 Windows 实例需要使用实例的管理员帐号（Administrator）和对应的密码。
>! 首次通过远程桌面登录 Windows 实例之前，您需要重置管理员帐号（Administrator）的密码。具体操作请参考 [重置密码](https://cloud.tencent.com/document/product/1207/44575) 文档。
>
- 请确认本地计算机与实例之间的网络连通正常，以及实例的防火墙已放行3389端口（创建实例时默认已开通3389端口）。

## 操作步骤

>? 以下操作步骤以 Windows 7 操作系统为例。
>

1. 在本地 Windows 计算机上，单击  <img src="https://main.qcloudimg.com/raw/370daffec54024ee262d1e5dbcd4bde2.png" style="margin: 0;width: 35px;">，在【搜索程序和文件】中，输入 **mstsc**，按 **Enter**，打开远程桌面连接对话框。如下图所示：
![](https://main.qcloudimg.com/raw/38e9d9ac0485bf8ad3a209092a1284ba.png)
2. 在【计算机】后面，输入 Windows 服务器的公网 IP，单击【连接】。
3. 在弹出的 “Windows 安全” 窗口中，输入实例的管理员帐号和密码，如下图所示：
>? 若弹出 “是否信任此远程连接？” 对话框，可勾选 “不再询问我是否连接到此计算机”，单击【连接】。
>
![](https://main.qcloudimg.com/raw/3a9aa79200ace4a6ebd68a6e511a341d.png)
4. 单击【确定】，即可登录到 Windows 实例。


