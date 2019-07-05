## 操作场景

本文以 PuTTY 软件为例，介绍如何在 Windows 系统的本地电脑中使用远程登录软件登录 Linux 实例。


## 适用本地操作系统

Windows

## 鉴权方式

**密码**或**密钥**

## 前提条件
- 已获取登录实例的管理员帐号及密码（或密钥）。
   对于不同类型的 Linux 实例，默认帐号不同。如下表所示：
<table>
<tr><th>实例操作系统</th><th>默认帐号</th><th>密码/密钥</th></tr>
<tr><td><ul><li>SUSE</li><li>CentOS</li><li>Debian</li></ul></td><td>root</td><td rowspan="2"><ul><li>如果您在购买实例时选择自动生成密码，则可登录腾讯云控制台，单击右上角的 <img src="https://main.qcloudimg.com/raw/60e7d0de182a973d69fb82b69d01f52a.png" style="margin: 0;"></img>，进入站内消息页面，获取云服务器登录管理员帐号及初始密码。</li><li>如果您在购买实例时选择自定义密码，则登录密码为您在购买云服务器实例时指定的密码。</li><li>如果您在购买实例时选择密钥登录，请牢记密钥存放在本地的绝对路径。</li><li>如果您忘记登录云服务器的密码或密钥，请参考 <a href="https://cloud.tencent.com/document/product/213/16566">重置实例密码</a> 或者 <a href="https://cloud.tencent.com/document/product/213/16691#.E5.88.9B.E5.BB.BA-ssh-.E5.AF.86.E9.92.A5">创建 SSH 密钥</a> 进行重置。</li></ul></td></tr>
<tr><td>Ubuntu</td><td>ubuntu</td></tr>
</table>
- 已打开云服务器实例的22号端口。
您可以通过 [检查网络连通性](https://cloud.tencent.com/document/product/213/10232#.E6.AD.A5.E9.AA.A4.E4.B8.80.EF.BC.9A.E6.A3.80.E6.9F.A5.E7.BD.91.E7.BB.9C.E8.BF.9E.E9.80.9A.E6.80.A7) 检查22号端口是否放通。如果端口不通，您可以在 [配置安全组](https://cloud.tencent.com/document/product/213/15377) 时设置端口的入站/出站规则。
- 云服务器实例已购买公网 IP 并获取到公网 IP。
实例的公网 IP 可登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/index) 进行查看。

## 操作步骤

### 使用密码登录

1. 下载 Windows 远程登录软件，即 PuTTY。
PuTTY 的获取方式：[点此获取](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html)
2. 双击【putty.exe】，打开 PuTTY 客户端。
3. 在 PuTTY Configuration 窗口中，输入以下内容。如下图所示：
![](https://main.qcloudimg.com/raw/7ac87da9721ef7d64fe8cac81a3dab33.png)
参数举例说明如下：
 - Host Name（or IP address）：云服务器的公网 IP（登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/index)，可在列表页及详情页中获取公网 IP）。
 - Port：云服务器的端口，必须设置为22。
 - Connect type：选择 “SSH”。
 - Saved Sessions：填写会话名称，例如 test。
 配置 “Host Name” 后，再配置 “Saved Sessions” 并保存，则后续使用时您可直接双击 “Saved Sessions” 下保存的会话名称即可登录服务器。
3. 单击【Open】，进入 “PuTTY” 的运行界面，提示 “login as:”。
4. 在 “login as” 后输入用户名，按 **Enter**。
5. 在 “Password” 后输入密码，按 **Enter**。
登录完成后，命令提示符左侧将显示当前登录云服务器的信息。如下图所示：
![](https://main.qcloudimg.com/raw/9e7ddc631de2a27bfd35f9225de85506.png)

### 使用密钥登录

1. 下载 Windows 远程登录软件，即 PuTTy。
请分别下载 putty.exe 和 puttygen.exe 软件，PuTTy 的获取方式：[点此获取](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html)。
2. 双击【puttygen.exe】，打开 PuTTy Key 客户端。
3. 单击【Load】，选择并打开已下载的私钥存储路径。如下图所示：
例如，选择并打开文件名为 david 的私钥文件。
![](https://main.qcloudimg.com/raw/0110ba722331fb2892a8e6822ec3f709.png)
4. 在 PuTTY Key Generator 窗口中，输入密钥名和加密私钥的密码，单击【Save private key】。如下图所示：
![](https://main.qcloudimg.com/raw/58a250d3f3d1b78eff3edaab64cd01c0.png)
5. 在弹出的窗口中，选择您存放密钥的路径，并在文件名栏输入“密钥名.ppk”，单击【保存】。例如，将 david 私钥文件另存为 david.ppk 密钥文件。如下图所示：
![](https://main.qcloudimg.com/raw/d0fa9fd8aad7d2259bd8a0ce48ae5160.png)
6. 双击【putty.exe】，打开 PuTTY 客户端。
7. 在左侧导航栏中，选择【Connection】>【SSH】>【Auth】，进入 Auth 配置界面。
8. 单击【Browse】，选择并打开密钥的存储路径。如下图所示：
![](https://main.qcloudimg.com/raw/61993f3977ff681b8b2d78beac55f2ca.png)
8. 切换至 Session 配置界面，配置服务器的 IP、端口，以及连接类型。如下图所示：
![](https://main.qcloudimg.com/raw/ddfd58429288ce0e195e86a6cb1c9cd6.png)
 - Host Name (IP address)：云服务器的公网 IP。登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/index)，可在列表页及详情页中获取公网 IP。
 - Port：云服务器的端口，必须填 22 。
 - Connect type：选择 “SSH”。
 - Saved Sessions：填写会话名称，例如 test。
 配置 “Host Name” 后，再配置 “Saved Sessions” 并保存，则后续使用时您可直接双击 “Saved Sessions” 下保存的会话名称即可登录服务器。
9. 单击【Open】，发起登录请求。

## 后续操作

当您成功登录云服务器后，您可以在腾讯云服务器上搭建个人站点，论坛或者使用其他操作，相关操作可参考：
- [搭建 WordPress 个人站点](https://cloud.tencent.com/document/product/213/34064)
- [搭建 Discuz! 论坛](https://cloud.tencent.com/document/product/213/34065)

