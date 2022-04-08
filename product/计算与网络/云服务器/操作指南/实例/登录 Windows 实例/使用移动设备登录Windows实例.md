## 操作场景
本文以 Microsoft Remote Desktop 客户端为例，介绍如何在不同系统的移动设备上登录 Windows 实例。

## 适用移动设备
iOS 及 Android 设备

## 前提条件
- 云服务器实例状态为“运行中”。
- 已获取登录实例的管理员帐号及密码。
 - 如果您使用系统默认密码登录实例，请前往 [站内信](https://console.cloud.tencent.com/message) 获取。
 - 如果您忘记密码，请 [重置实例密码](https://cloud.tencent.com/document/product/213/16566)。
- 您的云服务器实例已购买公网 IP，且该实例已开通云服务器实例的3389端口（对于通过快速配置购买的云服务器实例已默认开通）。

## 操作步骤


<dx-alert infotype="explain" title="">
本文操作步骤以 iOS 设备为例，Android 设备实际操作步骤与其无较大差异。
</dx-alert>


1. 下载 Microsoft 远程桌面，并启动 RD Client。
2. 在“电脑”页面中，选择右上角的 **+**，并在弹出菜单中单击**添加电脑**。
3. 在“添加电脑”页面，配置以下登录信息。如下图所示：
![](https://main.qcloudimg.com/raw/1f74914dc3567171ba64d91c2e4863e7.jpg)
 - **电脑名称**：云服务器的公网 IP。获取方式请参见 [获取公网 IP 地址](https://cloud.tencent.com/document/product/213/17940)。
 - **用户帐户**：默认选择“在需要时询问”。
4. 填写完成后，单击页面右上角的**存储**。
5. 在“电脑”页面，选择需登录的实例，并在弹出窗口中输入登录实例的管理员帐号及密码。如下图所示：
![](https://main.qcloudimg.com/raw/7498f0b0e551c6f976b12218422d577b.jpg)
 - **管理员帐号**：Windows 实例管理员帐号为 `Administrator`。
 - **密码**：输入实例登录密码。
6. 单击**继续**，若显示如下图所示界面，则表示已成功登录 Windows 实例。
 ![](https://main.qcloudimg.com/raw/60abc6a9f51ae33ea95aa11edc53e009.jpg)
