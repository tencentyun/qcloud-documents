
创建Windows实例后，您可以根据**本地操作系统**以及**是否有公网IP**来选择不同的登录方式登录Windows实例。登录方式可以参考以下表格：

| 本地操作系统 | 实例有公网IP                    | 实例没有公网IP |
| ------------ | --------------------------------- | ---------------------- |
| Windows      | 使用RDP文件登录（推荐）<br> 远程桌面登录         |         VNC登录               |
| Linux/Mac OS | 使用RDP文件登录（推荐）<br>        |         VNC登录          |

## 前提条件

1. 远程登录Windows实例需要使用实例的管理员账号和对应的密码。对于Windows实例的管理员账号统一为**Administrator**。

- 若您在购买实例时选择**自动生成密码**，您可以在[腾讯云控制台](https://cloud.tencent.com/login)的右上角**消息中心**查找初始密码。![](https://main.qcloudimg.com/raw/52034cac55d0a5fd77ac90def4393615.png)

- 若您在购买实例时选择**自定义密码**，登录密码为您在购买实例时设置的密码。如果您忘记密码，可以通过[重置实例密码](https://cloud.tencent.com/document/product/213/16566)对密码进行重置。![](https://main.qcloudimg.com/raw/f8b0d37083569624f689aca5f40191b4.png)

2. 确保请云服务器3389号端口已开放。您可以通过[检查网络连通性](https://cloud.tencent.com/document/product/213/10232#.E6.AD.A5.E9.AA.A4.E4.B8.80.EF.BC.9A.E6.A3.80.E6.9F.A5.E7.BD.91.E7.BB.9C.E8.BF.9E.E9.80.9A.E6.80.A7)检查3389号端口是否放通。如果端口不通，您可以在[配置安全组](https://cloud.tencent.com/document/product/213/15377)时设置端口的入站/出站规则。

## 使用RDP文件登录（推荐）

### 适用本地操作系统
Windows，Linux和Mac OS

### Windows系统使用RDP登录
1. 登录[云服务器控制台](https://cloud.tencent.com/login?s_url=https%3A%2F%2Fconsole.cloud.tencent.com%2F)。在顶部菜单中选择【云产品】>【云计算与网络】>【云服务器】。
2. 如图所示进入云服务器列表，在需要登录的 Windows 云服务器中单击【登录】按钮。![](https://main.qcloudimg.com/raw/837d367b6ea081827c727b2d8cac0ae4.png)
3. 在“登录Windows实例”对话框，选择使用RDP文件登录，点击【下载RDP文件】到本地。![](https://main.qcloudimg.com/raw/8847c7b1e41c75fe362fd46bbf21d729.png)
4. 双击下载到本地的RDP文件，远程连接到Windows云服务器。

### Linux系统使用RDP登录
您需要安装相应的远程桌面连接程序，这里推荐使用 rdesktop 进行连接。有关 rdesktop 的更多内容，请参考 [rdesktop官方说明](http://www.rdesktop.org/) 
1. 安装 rdesktop
运行 `rdesktop` 命令检查系统是否已经安装，若未安装则请 [转到 github 下载最新安装包](https://github.com/rdesktop/rdesktop/releases)。
或者单击以下链接直接下载 v1.8.3版本：
 - [rdesktop-1.8.3.tar.gz](https://mc.qcloudimg.com/static/archive/06483121ce067b537342687dd6a909d8/rdesktop-1.8.3.tar.gz)
 - [rdesktop-1.8.3.zip](https://mc.qcloudimg.com/static/archive/24adfd7586f55bd96cd6714a6078a4df/rdesktop-1.8.3.zip)

 并在相应目录下运行以下命令解压和安装
```
tar xvzf rdesktop-<x.x.x>.tar.gz ##替换x.x.x为下载的版本号 
cd rdesktop-1.8.3
./configure 
make 
make install
```

2. 连接远程 Windows 实例
运行以下命令（将示例中的参数改为您自己的参数）：
```
rdesktop -u Administrator -p <your-password> <hostname or IP address>
```
其中：-u 连接用户名即 `Administrator`，-p 连接在您设置的登录密码，&lt;hostname or IP address&gt;为您的 Windows 实例公网 IP 或 自定义域名。
 
###  MacOS系统使用RDP登录：
以Microsoft Remote Desktop for Mac为例介绍本地为 Mac OS 计算机时如何登录 Windows实例。

1. 下载[Microsoft Remote Desktop for Mac](https://rink.hockeyapp.net/apps/5e0c144289a51fca2d3bfa39ce7f2b06/) （该测试版本客户端由微软官方维护，我们推荐您优先使用该版本客户端。微软已于 2017 年取消其官网提供的下载链接，转而通过其子公司 HockeyApp 的页面进行 Beta 版本的发布）。
>! 您也可以从[Mac App Store](https://itunes.apple.com/us/app/microsoft-remote-desktop/id715768417)下载 Microsoft 远程桌面客户端。该客户端不面向中国地区用户开放，您需要有其他地区 AppleID 账号才可下载。


2. 打开客户端工具，点击【Add Deskop】。![](https://main.qcloudimg.com/raw/c0ec6b04c59e37e95f7b5eb84ffcb83b.png)
2. 在弹出的对话框中，输入框输入 Windows 实例的公网 IP后点击【Add】添加远程桌面。<img src="https://main.qcloudimg.com/raw/d0f1c1ce9574f3ce191267b3beaff557.png" width = "350" height = "400" alt="图片名称" align=center />

3. 双击新添加的远程桌面图标，在新打开的界面中输入实例的管理员账号（默认为Administrator）和对应的密码。如果忘记密码，可以通过控制台重置实例密码。![](https://main.qcloudimg.com/raw/f8b0d37083569624f689aca5f40191b4.png)


## 使用远程桌面登录
除了RDP的登录方式之外，本地为Windows的用户还可以通过远程桌面登录云服务器实例。
### 适用本地操作系统
Windows

### 操作步骤

1. 在本地 Windows 机器上，单击【开始菜单】-【Run】，输入 `mstsc` 命令，即可打开远程桌面连接对话框。
2. 在输入框输入 Windows 服务器的公网 IP（登录 [云服务器控制台](https://console.cloud.tencent.com) 可查看云服务器的公网 IP），如下图所示：
![](//mccdn.qcloud.com/img56b1a11a3c31f.png)
3. 单击【连接】，在新打开的界面中输入前提条件中获取的管理员账号和对应的密码，如下图所示：
![](//mccdn.qcloud.com/static/img/878a0e8ef1a0bcc51ad5de2bcce4e353/image.png)
![](//mccdn.qcloud.com/static/img/e140d3151ac8747014313b33e6413568/image.png)
4. 单击【确定】，即可登录到 Windows 实例。

## 使用VNC远程登录实例（不推荐，当没有公网IP时使用）

VNC 登录是腾讯云为用户提供的一种通过 Web 浏览器远程连接云服务器的方式。在没有安装远程登录客户端或者客户端远程登录无法使用的情况下，用户可以通过 VNC 登录连接到云服务器，观察云服务器状态，并且可通过云服务器账户进行基本的云服务器管理操作。

### 使用限制：

- 使用VNC登录暂时不支持复制粘贴功能、中文输入法以及文件的上传、下载。
- 要使用VNC登录，需要使用主流浏览器，如Chrome，Firefox以及IE10以上版本。
- 该终端为独享，即同一时间只有一个用户可以使用 VNC 登录。

### 适用本地操作系统：

Windows，Linux和MacOS系统


### 操作步骤：
1. 登录 [云服务器控制台](https://console.cloud.tencent.com) 。
2. 在 “云服务器” 页面中，选择需要登录的 Windows 云服务器，单击【登录】。如下图所示：
![](https://main.qcloudimg.com/raw/837d367b6ea081827c727b2d8cac0ae4.png)
3. 在弹出的 “登录Windows实例” 窗口中，选择 “其他方式（VNC）”，单击【立即登录】。如下图所示：
![](https://main.qcloudimg.com/raw/8daeaac7cc4a5b94e1a5e5b6aa73be63.png)

>! 
> - 该终端为独享，即同一时间只有一个用户可以使用 VNC 登录。
> - 要正常使用 VNC 登录，需要使用现代浏览器，如：Chrome，firefox，IE10及以上版本等。
> - 暂不支持文件上传下载。
