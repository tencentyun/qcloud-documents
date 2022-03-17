## 操作场景

本文以 PuTTY 软件为例，介绍如何在 Windows 系统的本地电脑中使用远程登录软件登录 Linux 实例。


## 适用本地操作系统

Windows

## 鉴权方式

**密码**或**密钥**

## 前提条件
- 已获取登录实例的管理员帐号及密码（或密钥）。
 - 如果您使用系统默认密码登录实例，请前往 [站内信](https://console.cloud.tencent.com/message) 获取。
 - 如果您忘记密码，请 [重置实例密码](https://cloud.tencent.com/document/product/213/16566)。
- 您的云服务器实例已购买及获取公网 IP，且该实例已开通云服务器实例的22号端口（对于通过快速配置购买的云服务器实例已默认开通）。


## 操作步骤
<dx-tabs>
::: 使用密码登录[](id:passwordLogin)
1. 下载 Windows 远程登录软件，即 PuTTY。
<div style="background-color:#00A4FF; width: 170px; height: 35px; line-height:35px; text-align:center;"><a href="https://the.earth.li/~sgtatham/putty/latest/w64/putty.exe" target="_blank" style="color: white; font-size:16px;">点此获取 PuTTY</a></div>
2. 双击 **putty.exe**，打开 PuTTY 客户端。
3. 在 PuTTY Configuration 窗口中，输入以下内容。如下图所示：
![](https://main.qcloudimg.com/raw/7ac87da9721ef7d64fe8cac81a3dab33.png)
参数举例说明如下：
 - **Host Name（or IP address）**：云服务器的公网 IP（登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/index)，可在列表页及详情页中获取公网 IP）。
 - **Port**：云服务器的端口，必须设置为22。
 - **Connect type**：选择 “SSH”。
 - **Saved Sessions**：填写会话名称，例如 test。
 配置 “Host Name” 后，再配置 “Saved Sessions” 并保存，则后续使用时您可直接双击 “Saved Sessions” 下保存的会话名称即可登录服务器。
4. 单击 **Open**，进入 “PuTTY” 的运行界面，提示 “login as:”。
5. 在 “login as” 后输入用户名，按 **Enter**。
6. 在 “Password” 后输入密码，按 **Enter**。
输入的密码默认不显示，如下图所示：
![](https://main.qcloudimg.com/raw/9e7ddc631de2a27bfd35f9225de85506.png)
登录完成后，命令提示符左侧将显示当前登录云服务器的信息。
:::
::: 使用密钥登录[](id:keyLogin)
1. 下载 Windows 远程登录软件，即 PuTTy。请分别下载 putty.exe 和 puttygen.exe 软件，获取方式：
<div style="background-color:#00A4FF; width: 170px; height: 35px; line-height:35px; text-align:center;margin:5px;"><a href="https://the.earth.li/~sgtatham/putty/latest/w64/putty.exe" target="_blank" style="color: white; font-size:16px;">点此获取 PuTTY</a></div><div style="background-color:#00A4FF; width: 170px; height: 35px; line-height:35px; text-align:center;margin:5px;"><a href="https://the.earth.li/~sgtatham/putty/latest/w64/puttygen.exe" target="_blank" style="color: white; font-size:16px;">点此获取 PuTTYgen</a></div>
2. 双击 **puttygen.exe**，打开 PuTTy Key 客户端。
3. 单击 **Load**，选择并打开已下载的私钥存储路径。私钥已在创建时下载并由您个人保管，详情请参见 [管理 SSH 密钥](https://cloud.tencent.com/document/product/213/16691)。
例如，选择并打开文件名为 david 的私钥文件。如下图所示：
![](https://main.qcloudimg.com/raw/0110ba722331fb2892a8e6822ec3f709.png)
4. [](id:Step4)在 PuTTY Key Generator 窗口中，输入密钥名，并设置 PuTTY 用于加密私钥的密码（可选）。设置完成后单击 **Save private key**。如下图所示：
![](https://main.qcloudimg.com/raw/58a250d3f3d1b78eff3edaab64cd01c0.png)
5. 在弹出的窗口中，选择您存放密钥的路径，并在文件名栏输入“密钥名.ppk”，单击**保存**。例如，将 david 私钥文件另存为 david.ppk 密钥文件。如下图所示：
![](https://main.qcloudimg.com/raw/d0fa9fd8aad7d2259bd8a0ce48ae5160.png)
6. 双击 **putty.exe**，打开 PuTTY 客户端。
7. 在左侧导航栏中，选择 **Connection** > **SSH** > **Auth**，进入 Auth 配置界面。
8. 单击 **Browse**，选择并打开密钥的存储路径。如下图所示：
![](https://main.qcloudimg.com/raw/61993f3977ff681b8b2d78beac55f2ca.png)
8. 切换至 Session 配置界面，配置服务器的 IP、端口，以及连接类型。如下图所示：
![](https://main.qcloudimg.com/raw/ddfd58429288ce0e195e86a6cb1c9cd6.png)
 - **Host Name (IP address)**：云服务器的公网 IP。登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/index)，可在列表页及详情页中获取公网 IP。
 - **Port**：云服务器的端口，必须填 22。
 - **Connect type**：选择 “SSH”。
 - **Saved Sessions**：填写会话名称，例如 test。
 配置 “Host Name” 后，再配置 “Saved Sessions” 并保存，则后续使用时您可直接双击 “Saved Sessions” 下保存的会话名称即可登录服务器。
9. 单击 **Open**，进入 “PuTTY” 的运行界面，提示 “login as:”。
10. 在 “login as” 后输入用户名，按 **Enter**。
11. 若按照 [步骤4](#Step4) 设置了加密私钥的密码，则请在 “Passphrase for key "imported-openssh-key":” 输入密码后按 **Enter**。
输入的密码默认不显示，如下图所示：
![](https://main.qcloudimg.com/raw/89b2ef5f04a6402f0b1832301fa811cb.png)
登录完成后，命令提示符左侧将显示当前登录云服务器的信息。
:::
</dx-tabs>

## 后续操作

当您成功登录云服务器后，您可以在腾讯云服务器上搭建个人站点，论坛或者使用其他操作。相关操作可参考：
- [搭建 WordPress 个人站点](https://cloud.tencent.com/document/product/213/34064)
- [搭建 Discuz! 论坛](https://cloud.tencent.com/document/product/213/34065)

