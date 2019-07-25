## 操作场景
创建 Windows 实例后，您可以根据**本地操作系统**以及**是否有公网 IP**来选择不同的登录方式登录 Windows 实例。登录方式可以参考以下表格：

<table>
<tr><th>本地操作系统</th><th>实例有公网 IP</th><th>实例没有公网 IP</th></tr>
<tr><td>Windows</td><td><ul style="margin: 0;"><li>使用 RDP 文件登录（推荐）</li><li>远程桌面登录</li></ul></td><td rowspan="3">VNC 登录</td></tr>
<tr><td>Linux</td><td rowspan="2">使用 RDP 文件登录（推荐）</td></tr>
<tr><td>Mac OS</td></tr>
</table>

## 前提条件

- 已获取远程登录 Windows 实例需要使用实例的管理员账号和对应的密码。
 - Windows 实例的管理员账号统一为 **Administrator**。
 - 若您在购买实例时选择**自动生成密码**，您可以登录 [腾讯云控制台](https://console.cloud.tencent.com/)，单击右上角的 <img src="https://main.qcloudimg.com/raw/60e7d0de182a973d69fb82b69d01f52a.png" style="margin: 0;"></img>，进入“【腾讯云】请查收您新购买的云服务器”页面，查看初始密码。如下图所示：
 ![](https://main.qcloudimg.com/raw/d6de356ffd4a25c5d6e5c750efcfc92f.png)
 - 若您在购买实例时选择**自定义密码**，则密码为您在购买云服务器实例时指定的密码。如果您忘记密码，可以通过 [重置实例密码](https://cloud.tencent.com/document/product/213/16566) 对密码进行重置。如下图所示：
![](https://main.qcloudimg.com/raw/3e1629f983de71cb1514e973533bb6c5.png)
- 已开放云服务器3389号端口。您可以通过 [检查网络连通性](https://cloud.tencent.com/document/product/213/10232#.E6.AD.A5.E9.AA.A4.E4.B8.80.EF.BC.9A.E6.A3.80.E6.9F.A5.E7.BD.91.E7.BB.9C.E8.BF.9E.E9.80.9A.E6.80.A7) 检查3389号端口是否放通。如果端口不通，您可以在 [配置安全组](https://cloud.tencent.com/document/product/213/15377) 时设置端口的入站/出站规则。


## 使用 RDP 文件登录（推荐）

### 适用本地操作系统
Windows，Linux 和 Mac OS

### Windows 系统使用 RDP 登录
1. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/index)。
2. 在实例列表中，选择需要登录的 Windows 云服务器，单击【登录】。如下图所示：
![](https://main.qcloudimg.com/raw/bc452fce3b682d24933e73f4d15c0d7b.png)
3. 在弹出的【登录Windows实例】窗口中，选择【使用 RDP 文件登录】，单击【下载 RDP 文件】到本地。
![](https://main.qcloudimg.com/raw/bfbdf813684e34b236b90b9e1a19009b.png)
4. 双击下载到本地的 RDP 文件，远程连接到 Windows 云服务器。

### Linux 系统使用 RDP 登录

您需要安装相应的远程桌面连接程序，这里推荐使用 rdesktop 进行连接。有关 rdesktop 的更多内容，请参考 [rdesktop官方说明](http://www.rdesktop.org/) 。
1. 执行以下命令，检查系统是否已安装 rdesktop。
```
rdesktop
```
若未安装，请 [转到 github 下载最新安装包](https://github.com/rdesktop/rdesktop/releases)。也可以单击以下链接，直接下载 v1.8.3 版本：
 - [rdesktop-1.8.3.tar.gz](https://mc.qcloudimg.com/static/archive/06483121ce067b537342687dd6a909d8/rdesktop-1.8.3.tar.gz)
 - [rdesktop-1.8.3.zip](https://mc.qcloudimg.com/static/archive/24adfd7586f55bd96cd6714a6078a4df/rdesktop-1.8.3.zip)

 并在相应目录下执行以下命令解压和安装。
```
tar xvzf rdesktop-<x.x.x>.tar.gz ##替换x.x.x为下载的版本号 
cd rdesktop-1.8.3
./configure 
make 
make install
```
2. 执行以下命令，连接远程 Windows 实例。（请将示例中的参数改为您自己的参数）
```
rdesktop -u Administrator -p <your-password> <hostname or IP address>
```
 - `-u` 连接用户名即 `Administrator`。
 - `-p` 连接在您设置的登录密码。
 - `<hostname or IP address>`为您的 Windows 实例公网 IP 或自定义域名。
 
###  MacOS 系统使用 RDP 登录
以 Microsoft Remote Desktop for Mac 为例，介绍本地为 Mac OS 计算机时如何登录 Windows 实例。

1. 下载 [Microsoft Remote Desktop for Mac](https://rink.hockeyapp.net/apps/5e0c144289a51fca2d3bfa39ce7f2b06/) 。（该测试版本客户端由微软官方维护，我们推荐您优先使用该版本客户端。微软已于 2017 年取消其官网提供的下载链接，转而通过其子公司 HockeyApp 的页面进行 Beta 版本的发布）。
>! 您也可以从 [Mac App Store](https://itunes.apple.com/us/app/microsoft-remote-desktop/id715768417) 下载 Microsoft 远程桌面客户端。该客户端不面向中国地区用户开放，您需要有其他地区 AppleID 账号才可下载。
2. 打开客户端工具，单击【Add Deskop】。如下图所示：
![](https://main.qcloudimg.com/raw/d310a22009134182def49929625e6f1d.png)
3. 在弹出的对话框中，输入 Windows 实例的公网 IP，并单击【Add】，添加远程桌面。如下图所示：
<img src="https://main.qcloudimg.com/raw/f37d19193aff614a8057566da1c59b6e.png" width = "350" height = "400" alt="图片名称" align=center />
4. 双击新添加的远程桌面图标，在新打开的界面中输入实例的管理员账号（默认为 Administrator）和对应的密码。如果您忘记密码，可以通过 [重置实例密码](https://cloud.tencent.com/document/product/213/16566) 对密码进行重置。如下图所示：
![](https://main.qcloudimg.com/raw/3e1629f983de71cb1514e973533bb6c5.png)

## 使用远程桌面登录

除了 RDP 的登录方式之外，本地为 Windows 的用户还可以通过远程桌面登录云服务器实例。

### 适用本地操作系统
Windows

### 操作步骤

1. 在本地 Windows 机器上，单击【开始菜单】>【Run】，输入 `mstsc` 命令，即可打开远程桌面连接对话框。
2. 在远程桌面连接对话框中，输入 Windows 服务器的公网 IP（登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/index) 可查看云服务器的公网 IP），单击【连接】，如下图所示：
![](https://main.qcloudimg.com/raw/d2bce1a25772f662b934173b02c1e92a.png)
3. 在新打开的界面中，输入实例的管理员账号和对应的密码，如下图所示：
![](https://main.qcloudimg.com/raw/54c1ec9ec62c2499686dd3f78ef4b11e.png)
4. 单击【确定】，即可登录到 Windows 实例。

## 使用 VNC 远程登录实例（不推荐，当没有公网 IP 时使用）

VNC 登录是腾讯云为用户提供的一种通过 Web 浏览器远程连接云服务器的方式。在没有安装远程登录客户端或者客户端远程登录无法使用的情况下，用户可以通过 VNC 登录连接到云服务器，观察云服务器状态，并且可通过云服务器账户进行基本的云服务器管理操作。

### 使用限制

- 使用 VNC 登录暂时不支持复制粘贴功能、中文输入法以及文件的上传、下载。
- 要使用 VNC 登录，需要使用主流浏览器，如 Chrome，Firefox 以及 IE 10 以上版本。
- 该终端为独享，即同一时间只有一个用户可以使用 VNC 登录。

### 适用本地操作系统

Windows，Linux 和 Mac OS

### 操作步骤

1. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/index) 。
2. 在实例列表中，选择需要登录的 Windows 云服务器，单击【登录】。如下图所示：
![](https://main.qcloudimg.com/raw/96689027b98d8fc6bfb00036de7a87f8.png)
3. 在弹出的 “登录Windows实例” 窗口中，选择【其他方式（VNC）】，单击【立即登录】。如下图所示：
![](https://main.qcloudimg.com/raw/bdfe5b286e7e0c388adfbc12d15cfad6.png)
4. 在弹出的对话框中，输入用户名和密码登录，即可完成登录。
