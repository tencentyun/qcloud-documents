## 操作场景
以下视频介绍了如何使用远程登录软件，登录 Linux 实例：
<div class="doc-video-mod"><iframe src="https://cloud.tencent.com/edu/learning/quick-play/3401-60027?source=gw.doc.media&withPoster=1&notip=1"></iframe></div>
本文以 PuTTY 软件为例，介绍如何在 Windows 系统的本地计算机中使用远程登录软件登录 Linux 实例。

## 适用本地操作系统
Windows
<dx-alert infotype="explain" title="">
如果您的本地计算机为 Linux 或者 MacOS 操作系统，请 [使用 SSH 登录 Linux 实例](https://cloud.tencent.com/document/product/1207/44643)。
</dx-alert>



## 鉴权方式
**密码**或**密钥**

## 前提条件

- 您已获取登录实例的用户名及密码（或密钥）。
<dx-alert infotype="notice" title="">
首次通过本地远程登录软件登录 Linux 实例之前，您需要重置用户名（如 `root`、`ubuntu`）的密码，或者绑定密钥。具体操作请参考 [重置密码](https://cloud.tencent.com/document/product/1207/44575) 或 [管理密钥](https://cloud.tencent.com/document/product/1207/44573) 文档。
</dx-alert>
- 请确认本地计算机与实例之间的网络连通正常，以及实例的防火墙已放行22端口（创建实例时默认已开通22端口）。

## 注意事项

使用 Ubuntu 镜像创建的实例默认禁用 `root` 用户名通过密码的方式登录实例。如需开启，请参考 [Ubuntu 系统如何使用 root 用户登录实例？](https://cloud.tencent.com/document/product/1207/44569#ubuntu-.E7.B3.BB.E7.BB.9F.E5.A6.82.E4.BD.95.E4.BD.BF.E7.94.A8-root-.E7.94.A8.E6.88.B7.E7.99.BB.E5.BD.95.E5.AE.9E.E4.BE.8B.EF.BC.9F)。

## 操作步骤

### 使用密码登录

1. 下载 Windows 远程登录软件，即 PuTTY。
PuTTY 的获取方式：[点此获取](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html)
2. 双击 **putty.exe**，打开 PuTTY 客户端。
3. 在 PuTTY Configuration 窗口中，输入以下内容。如下图所示：
![](https://main.qcloudimg.com/raw/7ac87da9721ef7d64fe8cac81a3dab33.png)
参数举例说明如下：
 - Host Name（or IP address）：轻量应用服务器的公网 IP（登录 [轻量应用服务器控制台](https://console.cloud.tencent.com/lighthouse/instance/index)，可在服务器列表页中获取公网 IP）。
 - Port：轻量应用服务器的连接端口，必须设置为22。
 - Connect type：选择 “SSH”。
 - Saved Sessions：填写会话名称，例如 test。
配置 “Host Name” 后，再配置 “Saved Sessions” 并保存，则后续使用时您可直接双击 “Saved Sessions” 下保存的会话名称即可登录服务器。
4. 单击 **Open**，进入 “PuTTY” 的运行界面，提示 “login as:”。
5. 在 “login as” 后输入用户名，如 `root`，按 **Enter**。
<dx-alert infotype="explain" title="">
若您使用了除 Ubuntu 系统镜像外的其他 Linux 系统镜像创建实例，则均可使用 `root` 作为用户名。Ubuntu 系统的默认用户名是 ubuntu，如需使用 `root` 用户名登录，则请参考 [Ubuntu 系统如何使用 root 用户登录实例？](https://cloud.tencent.com/document/product/1207/44569#ubuntu-.E7.B3.BB.E7.BB.9F.E5.A6.82.E4.BD.95.E4.BD.BF.E7.94.A8-root-.E7.94.A8.E6.88.B7.E7.99.BB.E5.BD.95.E5.AE.9E.E4.BE.8B.EF.BC.9F)。
</dx-alert>
6. 在 “Password” 后输入密码，按 **Enter**。
输入的密码默认不显示，如下图所示：
![](https://main.qcloudimg.com/raw/9e7ddc631de2a27bfd35f9225de85506.png)
登录完成后，命令提示符左侧将显示当前登录轻量应用服务器的信息。

### 使用密钥登录

1. 下载 Windows 远程登录软件，即 PuTTy。
请分别下载 putty.exe 和 puttygen.exe 软件，PuTTy 的获取方式：[点此获取](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html)。
2. 双击 **puttygen.exe**，打开 PuTTy Key 客户端。
3. 单击 **Load**，选择并打开已下载的私钥存储路径。如下图所示：
例如，选择并打开文件名为 david 的私钥文件。
![](https://main.qcloudimg.com/raw/0110ba722331fb2892a8e6822ec3f709.png)
4. [](id:Step4)在 PuTTY Key Generator 窗口中，输入密钥名，并创建加密私钥的密码（可选）。设置完成后单击 **Save private key**，如下图所示：
![](https://main.qcloudimg.com/raw/58a250d3f3d1b78eff3edaab64cd01c0.png)
5. 在弹出的窗口中，选择您存放密钥的路径，并在文件名栏输入“密钥名.ppk”，单击**保存**。例如，将 david 私钥文件另存为 david.ppk 密钥文件。如下图所示：
![](https://main.qcloudimg.com/raw/d0fa9fd8aad7d2259bd8a0ce48ae5160.png)
6. 双击 **putty.exe**，打开 PuTTY 客户端。
7. 在左侧导航栏中，选择 **Connection** > **SSH** > **Auth**，进入 Auth 配置界面。
8. 单击 **Browse**，选择并打开密钥的存储路径。如下图所示：
![](https://main.qcloudimg.com/raw/61993f3977ff681b8b2d78beac55f2ca.png)
9. 切换至 Session 配置界面，配置服务器的 IP、端口，以及连接类型。如下图所示：
![](https://main.qcloudimg.com/raw/ddfd58429288ce0e195e86a6cb1c9cd6.png)
 - Host Name (IP address)：轻量应用服务器的公网 IP（登录 [轻量应用服务器控制台](https://console.cloud.tencent.com/lighthouse/instance/index)，可在服务器列表页中获取公网 IP）。
 - Port：轻量应用服务器的连接端口，必须设置为22。
 - Connect type：选择 “SSH”。
 - Saved Sessions：填写会话名称，例如 test。
配置 “Host Name” 后，再配置 “Saved Sessions” 并保存，则后续使用时您可直接双击 “Saved Sessions” 下保存的会话名称即可登录服务器。
10. 单击 **Open**，进入 “PuTTY” 的运行界面，提示 “login as:”。
11. 在 “login as” 后输入用户名，如 `root`，按 **Enter**。
12. 若按照 [步骤4](#Step4) 设置了加密私钥的密码，则请输入后按 **Enter**，密码默认不显示。如下图所示：
![](https://main.qcloudimg.com/raw/401da3ef001f103115aa8ba8c54d6ec8.png)
登录完成后，命令提示符左侧将显示当前登录轻量应用服务器的信息。



