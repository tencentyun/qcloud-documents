>! 目前 Windows 实例登录方式默认为**标准登录方式（WebRDP）**，您可通过控制台一键登录 Windows 实例，无需下载本地登录客户端。登录方法介绍请参见 [使用标准方式登录 Windows 实例（推荐）](https://cloud.tencent.com/document/product/213/57778)。
>

## 操作场景
RDP 是 Remote Desktop Protocol 的缩写，是微软开发的一个多通道的协议，帮助您的本地计算机连上远程计算机。RDP 作为腾讯云推荐登录您 Windows 云服务器的方式。本文介绍如何使用 RDP 文件登录 Windows 实例。

## 适用本地操作系统
Windows，Linux 和 Mac OS 都可以使用 RDP 方式登录云服务器。

## 前提条件

- 已获取远程登录 Windows 实例需要使用实例的管理员帐号和对应的密码。
 - 如在创建实例时选择系统随机生成密码，则请往 [站内信](https://console.cloud.tencent.com/message) 获取。
 - 如已设置登录密码，则请使用该密码登录。如忘记密码，则请 [重置实例密码](https://cloud.tencent.com/document/product/213/16566)。
- 您的云服务器实例已购买公网 IP，且已在实例关联的安全组中放通来源为 WebRDP 代理 IP 的远程登录端口（默认为3389）。
 - 如通过快速配置购买云服务器，则默认已开通。
 - 如通过自定义配置购买云服务器，则可参考 [允许 RDP 远程连接 Windows 云服务器](https://cloud.tencent.com/document/product/213/34601#.E5.9C.BA.E6.99.AF.E4.BA.8C.EF.BC.9A.E5.85.81.E8.AE.B8-rdp-.E8.BF.9C.E7.A8.8B.E8.BF.9E.E6.8E.A5-windows-.E4.BA.91.E6.9C.8D.E5.8A.A1.E5.99.A8) 手动放通。
- 请确保您实例的公网带宽 ≥ 5Mbit/s，否则会引起远程桌面卡顿。如需调整网络带宽，请参见 [调整网络配置](https://cloud.tencent.com/document/product/213/15517)。
 

## 操作步骤
<dx-tabs>
::: Windows\s系统使用\sRDP\s登录[](id:windowsRDP)
1. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/index)。
2. 在实例的管理页面，选择需要登录的 Windows 云服务器，单击**登录**。如下图所示：
![](https://main.qcloudimg.com/raw/b590c38d3b0b64048098f2848abbf162.png)
3. 在打开的“标准登录 | Windows 实例”窗口中，选择 **RDP文件下载**，将 RDP 文件下载到本地。
>?若您已修改远程登录端口，则需修改 RDP 文件，在 IP 地址后增加`:端口`。
>
![](https://main.qcloudimg.com/raw/615e0149171bcd4c9ead4c8174c772d4.png)
4. 双击打开已下载到本地的 RDP 文件，输入密码，单击**确定**，即可远程连接到 Windows 云服务器。
 - 如果您使用系统默认密码登录实例，请前往 [站内信](https://console.cloud.tencent.com/message) 获取。
 - 如果您忘记密码，请 [重置实例密码](https://cloud.tencent.com/document/product/213/16566)。
:::
::: Linux\s系统使用\sRDP\s登录[](id:LinuxRDP)
>?您需要安装相应的远程桌面连接程序，推荐使用 rdesktop 进行连接。更多详情请参考 [rdesktop 官方说明](http://www.rdesktop.org/)。
>
1. 执行以下命令，检查系统是否已安装 rdesktop。
```
rdesktop
``` 
 - 若已安装 rdesktop，请执行 [步骤4](#step04)。
 - 若提示 command not found，则表示未安装 rdesktop，请执行 [步骤2](#step02)。
2. [](id:step02)在终端执行以下命令，下载 rdesktop 安装包，此步骤以 rdesktop 1.8.3 版本为例。
```
wget https://github.com/rdesktop/rdesktop/releases/download/v1.8.3/rdesktop-1.8.3.tar.gz
``` 如果您需要最新的安装包，可以前往 [GitHub rdesktop页面](https://github.com/rdesktop/rdesktop/releases) 查找最新安装包，并在命令行中替换为最新安装路径。
3. 在待安装 rdesktop 的目录下，依次执行以下命令，解压和安装 rdesktop。
```
tar xvzf rdesktop-<x.x.x>.tar.gz ##替换x.x.x为下载的版本号 
cd rdesktop-1.8.3
./configure 
make 
make install
```
4. [](id:step04)执行以下命令，连接远程 Windows 实例。</span>
>? 请将示例中的参数修改为您自己的参数。
>
```
rdesktop -u Administrator -p <your-password> <hostname or IP address>
```
 - `Administrator` 即为前提条件中获得的管理员帐号。
 - `<your-password>` 即为您设置的登录密码。
   如果您使用系统默认密码登录实例，请前往 [站内信](https://console.cloud.tencent.com/message) 获取。如果您忘记密码，请 [重置实例密码](https://cloud.tencent.com/document/product/213/16566)。
 - `<hostname or IP address>` 即为您的 Windows 实例公网 IP 或自定义域名。实例公网 IP 获取方法请参见 [获取公网 IP 地址](https://cloud.tencent.com/document/product/213/17940)。
:::
::: MacOS\s系统使用\sRDP\s登录[](id:MacRDP)
>?
>- 以下操作以 Microsoft Remote Desktop for Mac 为例。微软官方已于2017年停止提供 Remote Desktop 客户端的下载链接，转由其子公司 HockeyApp 进行 Beta 版本的发布。您可前往 [Microsoft Remote Desktop Beta](https://install.appcenter.ms/orgs/rdmacios-k2vy/apps/microsoft-remote-desktop-for-mac/distribution_groups/all-users-of-microsoft-remote-desktop-for-mac) 下载 Beta 版本。
>- 以下操作以连接 Windows Server 2012 R2 操作系统的云服务器为例。
>
1. 下载 Microsoft Remote Desktop for Mac 并在本地进行安装。
2. 启动 MRD，并单击【Add Desktop】。如下图所示：
![](https://main.qcloudimg.com/raw/e69528d10e9a17dfa26119a090766c49.png)
3. 弹出的 “Add Desktop” 窗口，按以下步骤创建连接。如下图所示：
![](https://main.qcloudimg.com/raw/d8e20278dd7c8aed487be2c43986f5e4.png)
    1. 在 “PC name” 处输入云服务器公网 IP。获取方法请参见 [获取公网 IP 地址](https://cloud.tencent.com/document/product/213/17940)。
    2. 单击【Add】确认创建 。
    3. 其余选项保持默认设置，完成创建连接。
    即可在窗口中查看已成功创建的连接。如下图所示：
![](https://main.qcloudimg.com/raw/1c0eff28aa68a7f02e8f295917bb603b.png)
4. 双击打开新创建的连接，并在弹出的窗口中根据提示，输入云服务器的帐号和密码，单击【Continue】。
 - 如果您使用系统默认密码登录实例，请前往 [站内信](https://console.cloud.tencent.com/message) 获取。
 - 如果您忘记密码，请 [重置实例密码](https://cloud.tencent.com/document/product/213/16566)。
5. 在弹出的窗口中单击【Continue】确认连接。如下图所示：
![](https://main.qcloudimg.com/raw/61b3d9566365183fcc1d92c2f6bc2e7b.png)
成功连接后将打开 Windows 云服务器界面。如下图所示：
![](https://main.qcloudimg.com/raw/5a524210acd13624af7263b6de3aea54.png)
:::
</dx-tabs>

## RDP 带宽限制说明[](id:illustrate)
网络可用带宽将直接影响通过 RDP 登录及使用云服务器的体验，不同的应用程序和显示分辨率需要不同的网络配置。微软提出了不同应用场景下使用 RDP 时实例的最低带宽要求。请参考下表，确保实例的网络配置可满足您的业务需求，否则可能引起卡顿等问题。
>?如需调整实例带宽，请参见 [调整网络配置](https://cloud.tencent.com/document/product/213/15517)。
>
以下数据适用于采用1920 × 1080分辨率，并同时采用默认图形模式和 H.264/AVC 444 图形模式的单一监视器配置。

<table>
<tr>
<th width="15%">方案</th>
<th width="19%">默认模式</th>
<th width="19%">H.264/AVC 444 模式	</th>
<th width="47%">场景说明</th>
</tr>
<tr>
<td>闲置</td>
<td>0.3Kbps	</td>
<td>0.3Kbps</td>
<td>用户已暂停工作，未发生活跃的屏幕更新。</td>
</tr>
<tr>
<td>Microsoft Word</td>
<td>100 - 150 Kbps</td>
<td>200 - 300 Kbps</td>
<td>用户正在活跃使用 Microsoft Word、打字、粘贴图形，并在文档之间切换。</td>
</tr>
<tr>
<td>Microsoft Excel</td>
<td>150 - 200Kbps</td>
<td>400 - 500Kbps</td>
<td>用户正在活跃使用 Microsoft Excel，并同时更新多个包含公式和图表的单元格。</td>
</tr>
<tr>
<td>Microsoft PowerPoint</td>
<td>4 - 4.5Mbps</td>
<td>1.6 - 1.8Mbps</td>
<td>用户正在活跃使用 Microsoft PowerPoint、打字、粘贴。 另外，用户正在修改内容丰富的图形，并使用幻灯片过渡效果。</td>
</tr>
<tr>
<td>Web 浏览</td>
<td>6 - 6.5Mbps</td>
<td>0.9 - 1Mbps</td>
<td>用户正在活跃浏览一个图形内容丰富的网站（横向和纵向滚动页面），其中包含多个静态图像和动画图像。</td>
</tr>
<tr>
<td>图库</td>
<td>3.3 - 3.6Mbps	</td>
<td>0.7 - 0.8Mbps</td>
<td>用户正在活跃使用图库应用程序。浏览、缩放、调整大小和旋转图像。</td>
</tr>
<tr>
<td>视频播放</td>
<td>8.5 - 9.5Mbps</td>
<td>2.5 - 2.8Mbps</td>
<td>用户正在观看一段占用了半个屏幕的 30 FPS 视频。</td>
</tr>
<tr>
<td>全屏视频播放</td>
<td>7.5 - 8.5Mbps</td>
<td>2.5 - 3.1Mbps</td>
<td>用户正在观看一段已最大化为全屏的 30 FPS 视频。</td>
</tr>
</table>
