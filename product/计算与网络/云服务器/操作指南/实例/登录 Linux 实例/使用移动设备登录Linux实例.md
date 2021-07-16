## 操作场景
本文介绍如何在不同系统的移动设备上登录 Linux 实例。本文使用的连接工具如下：
 - iOS 设备：本文以使用 Termius-SSH client 为例。
 - Android 设备：本文以使用 JuiceSSH 为例。

## 适用移动设备
iOS 及 Android 设备

## 前提条件
- 云服务器实例状态为“运行中”。
- 已获取登录实例的管理员帐号及密码（或密钥）。
 - 如果您使用系统默认密码登录实例，请前往 [站内信](https://console.cloud.tencent.com/message) 获取。
 - 如果您忘记密码，请 [重置实例密码](https://cloud.tencent.com/document/product/213/16566)。
- 您的云服务器实例已购买公网 IP，且该实例已开通云服务器实例的22端口（对于通过快速配置购买的云服务器实例已默认开通）。

## 操作步骤
请对应您实际使用的移动设备，通过以下方式登录实例：

<dx-tabs>
::: iOS\s设备
1. 前往 App Store 下载 Termius-SSH client，并按照提示注册账户。
2. 在主页面中，单击【New Host】。
3. 进入 “New Host” 页面，配置以下登录信息。如下图所示：
![](https://main.qcloudimg.com/raw/b0a672d2fae5ed3cb8e08be6492987cd.jpg)
 - **Hostname**：云服务器的公网 IP。获取方式请参见 [获取公网 IP 地址](https://cloud.tencent.com/document/product/213/17940)。
 - **Use SSH**：默认打开，启动 SSH 登录配置。
 - **Username**：输入管理员帐号 root。若您使用 Ubuntu 操作系统，则管理员帐户为 ubuntu。
 - **Password**：输入实例登录密码。
4. 单击页面右上角的【Save】，保存登录配置。
5. 在 “Hosts” 页面，选择该项，并单击页面底部弹出窗口中的【Continue】确认登录。如下图所示：
![](https://main.qcloudimg.com/raw/2c1e0518f8bf4377c36ce92d0d484b57.jpg)
6. 显示如下图所示界面，则表示已成功登录 Linux 实例。
![](https://main.qcloudimg.com/raw/54a7fde256f500b32a2b0753c0966b2d.jpg)
:::
::: Android\s设备
#### 新建认证信息[](id:newAuthentication)
1. 下载并安装 JuiceSSH。
2. 在主页面中，选择“连接”，并单击“认证”页签。
3. 在“认证”页签中，单击页面右下角的【+】。
4. 在“新建认证”页面，配置登录帐户与密码。如下图所示：
![](https://main.qcloudimg.com/raw/9c16a7ff7d7658440d6675667bad531e.jpg)
 - **昵称**：自定义认证名称，可选填。
 - **用户名**：输入管理员帐号 root。若您使用 Ubuntu 操作系统，则管理员帐户为 ubuntu。
 - **密码**：选择“密码”后的【设置（可选）】，并在弹出窗口中输入实例登录密码。
5. 单击页面右上角的【✔】，即可新建认证。

#### 新建连接
1. 在主页面中，选择“连接” ，并单击“连接”页面中右下角的【+】。
2. 在“新建连接”页面，配置以下登录信息。如下图所示：
![](https://main.qcloudimg.com/raw/33446183637fc466f4b5aa2ae0ef27c8.jpg)
 - **昵称**：自定义连接名称，可选填。
 - **类型**：选择 “SSH”。
 - **地址**：云服务器的公网 IP。获取方式请参见 [获取公网 IP 地址](https://cloud.tencent.com/document/product/213/17940)。
 - **认证**：选择已在步骤 [新建认证信息](#newAuthentication) 中添加的认证信息。
 - **端口**：填写22端口。
 其余参数请保持默认设置。
3. 单击页面下方的【添加到组】，保存登录配置。

#### 登录实例
1. 在“连接”页面中，选择需登录的实例，并在弹出窗口中单击【接受】。如下图所示：
![](https://main.qcloudimg.com/raw/3b5503ea1422ee345b6b27a166f5e9b4.jpg)
2. 显示如下图所示界面，则表示已成功登录 Linux 实例。
![](https://main.qcloudimg.com/raw/a07b70fa518c0d474073515147487264.jpg)

:::
</dx-tabs>

