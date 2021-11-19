## 操作场景
本文介绍如何在 Windows 系统的本地电脑中通过远程桌面登录 Windows 实例。

## 适用本地操作系统

Windows

## 前提条件

- 已获取远程登录 Windows 实例需要使用实例的管理员帐号和对应的密码。
 - 如果您使用系统默认密码登录实例，请前往 [站内信](https://console.cloud.tencent.com/message) 获取。
 - 如果您忘记密码，请 [重置实例密码](https://cloud.tencent.com/document/product/213/16566)。
- 您的云服务器实例已购买公网 IP，且该实例已开通云服务器实例的3389号端口（对于通过快速配置购买的云服务器实例已默认开通）。

## 操作步骤
>? 以下操作步骤以 Windows 7 操作系统为例。
>
1. 在本地 Windows 计算机上，单击 <img src="https://main.qcloudimg.com/raw/370daffec54024ee262d1e5dbcd4bde2.png" style="margin: -5px 0px;width: 35px;">，在**搜索程序和文件**中，输入 **mstsc**，按 **Enter**，打开远程桌面连接对话框。如下图所示：
![](https://main.qcloudimg.com/raw/38e9d9ac0485bf8ad3a209092a1284ba.png)
2. 在“计算机”后输入 Windows 服务器的公网 IP，单击**连接**。您可参考 [获取公网 IP 地址](https://cloud.tencent.com/document/product/213/17940) 获取服务器公网 IP。
3. 在弹出的 “Windows 安全” 窗口中，输入实例的管理员帐号和密码，如下图所示：
<dx-alert infotype="explain" title="">
 若弹出 “是否信任此远程连接？” 对话框，可勾选 “不再询问我是否连接到此计算机”，单击**连接**。
</dx-alert>
<img src="https://main.qcloudimg.com/raw/3a9aa79200ace4a6ebd68a6e511a341d.png"/>
4. 单击**确定**，即可登录到 Windows 实例。

