## 操作场景

本文介绍如何在 Windows 系统的本地电脑中通过远程桌面登录 Windows 实例。

## 适用本地操作系统

Windows

## 前提条件

- 已获取远程登录 Windows 实例需要使用实例的管理员帐号和对应的密码。
 - Windows 实例的管理员帐号统一为 **Administrator**。
 - 如果您在购买实例时选择**自动生成密码**，则可登录 [腾讯云控制台](https://console.cloud.tencent.com/)，单击右上角的 <img src="https://main.qcloudimg.com/raw/60e7d0de182a973d69fb82b69d01f52a.png" style="margin: 0;"></img>，进入“【腾讯云】请查收您新购买的云服务器”页面，查看初始密码。
 - 如果您在购买实例时选择**自定义密码**，则登录密码为您在购买云服务器实例时指定的密码。
 - 如果您忘记登录云服务器的密码，请参考 [重置实例密码](https://cloud.tencent.com/document/product/213/16566) 进行重置。
- 已打开云服务器实例的3389号端口。
您可以通过 [检查网络连通性](https://cloud.tencent.com/document/product/213/10232#.E6.AD.A5.E9.AA.A4.E4.B8.80.EF.BC.9A.E6.A3.80.E6.9F.A5.E7.BD.91.E7.BB.9C.E8.BF.9E.E9.80.9A.E6.80.A7) 检查3389号端口是否放通。如果端口不通，您可以在 [配置安全组](https://cloud.tencent.com/document/product/213/15377) 时设置端口的入站/出站规则。
- 云服务器实例已购买公网 IP 并获取到公网 IP。
实例的公网 IP 可登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/index) 进行查看。

## 操作步骤
>? 以下操作步骤以 Windows 7 操作系统为例。
>
1. 在本地 Windows 计算机上，单击 <img src="https://main.qcloudimg.com/raw/370daffec54024ee262d1e5dbcd4bde2.png" style="margin: 0;width: 35px;">，在【搜索程序和文件】中，输入 **mstsc**，按 **Enter**，打开远程桌面连接对话框。如下图所示：
![](https://main.qcloudimg.com/raw/38e9d9ac0485bf8ad3a209092a1284ba.png)
2. 在【计算机】后面，输入 Windows 服务器的公网 IP，单击【连接】。
3. 在弹出的 “Windows 安全” 窗口中，输入实例的管理员帐号和密码，如下图所示：
>? 若弹出 “是否信任此远程连接？” 对话框，可勾选 “不再询问我是否连接到此计算机”，单击【连接】。
>
![](https://main.qcloudimg.com/raw/3a9aa79200ace4a6ebd68a6e511a341d.png)
4. 单击【确定】，即可登录到 Windows 实例。

