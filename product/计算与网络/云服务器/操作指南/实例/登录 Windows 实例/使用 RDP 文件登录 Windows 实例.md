## 操作场景

RDP 是 Remote Desktop Protocol 的缩写，是微软开发的一个多通道的协议，帮助您的本地计算机连上远程计算机。RDP 作为腾讯云推荐登录您 Windows 云服务器的方式。本文介绍如何使用 RDP 文件登录 Windows 实例。

## 适用本地操作系统
Windows，Linux 和 Mac OS 都可以使用 RDP 方式登录云服务器。

## 前提条件

- 已获取远程登录 Windows 实例需要使用实例的管理员帐号和对应的密码。
 - 如果您使用系统默认密码登录实例，请前往 [站内信](https://console.cloud.tencent.com/message) 获取。
 - 如果您忘记密码，请 [重置实例密码](https://cloud.tencent.com/document/product/213/16566)。
- 您的云服务器实例已购买公网 IP，且该实例已开通云服务器实例的3389号端口（对于通过快速配置购买的云服务器实例已默认开通）。

## 操作步骤

### Windows 系统使用 RDP 登录
1. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/index)。
2. 在实例的管理页面，选择需要登录的 Windows 云服务器，单击【登录】。如下图所示：
![](https://main.qcloudimg.com/raw/038fce530c6c6827796e51d896306a93.png)
3. 在弹出的【登录Windows实例】窗口中，选择【使用 RDP 文件登录】，单击【下载RDP文件】，将 RDP 文件下载到本地。
![](https://main.qcloudimg.com/raw/9bcfe6774b483261d61f648968efe5ee.png)
4. 双击打开已下载到本地的 RDP 文件，输入密码，单击【确定】，即可远程连接到 Windows 云服务器。
 - 如果您使用系统默认密码登录实例，请前往 [站内信](https://console.cloud.tencent.com/message) 获取。
 - 如果您忘记密码，请 [重置实例密码](https://cloud.tencent.com/document/product/213/16566)。

### Linux 系统使用 RDP 登录

>?您需要安装相应的远程桌面连接程序，推荐使用 rdesktop 进行连接。更多详情请参考 [rdesktop 官方说明](http://www.rdesktop.org/)。
>
1. 执行以下命令，检查系统是否已安装 rdesktop。
```
rdesktop
```
 - 若已安装 rdesktop，请执行 [步骤4](#step04)。
 - 若提示 command not found，则表示未安装 rdesktop，请执行 [步骤2](#step02)。
2. <span id="step02"></span>在终端执行以下命令，下载 rdesktop 安装包，此步骤以 rdesktop 1.8.3 版本为例。
```
wget https://github.com/rdesktop/rdesktop/releases/download/v1.8.3/rdesktop-1.8.3.tar.gz
```
如果您需要最新的安装包，可以前往 [GitHub rdesktop页面](https://github.com/rdesktop/rdesktop/releases) 查找最新安装包，并在命令行中替换为最新安装路径。
3. 在待安装 rdesktop 的目录下，依次执行以下命令，解压和安装 rdesktop。
```
tar xvzf rdesktop-<x.x.x>.tar.gz ##替换x.x.x为下载的版本号 
cd rdesktop-1.8.3
./configure 
make 
make install
```
4. <span id="step04">执行以下命令，连接远程 Windows 实例。</span>
>? 请将示例中的参数修改为您自己的参数。
>
```
rdesktop -u Administrator -p <your-password> <hostname or IP address>
```
 - `Administrator` 即为前提条件中获得的管理员帐号。
 - `<your-password>` 即为您设置的登录密码。
   如果您使用系统默认密码登录实例，请前往 [站内信](https://console.cloud.tencent.com/message) 获取。如果您忘记密码，请 [重置实例密码](https://cloud.tencent.com/document/product/213/16566)。
 - `<hostname or IP address>` 即为您的 Windows 实例公网 IP 或自定义域名。
 
###  MacOS 系统使用 RDP 登录

>?
>- 以下操作以 Microsoft Remote Desktop for Mac 为例。微软官方已于2017年停止提供 Remote Desktop 客户端的下载链接，转由其子公司 [HockeyApp](https://appcenter.ms/apps) 进行 Beta 版本的发布。
>- 以下操作以连接 Windows Server 2012 R2 操作系统的云服务器为例。
>
1. 下载 Microsoft Remote Desktop for Mac 并在本地进行安装。
2. 启动 MRD，并单击【Add Desktop】。如下图所示：
![](https://main.qcloudimg.com/raw/e69528d10e9a17dfa26119a090766c49.png)
3. 弹出的 “Add Desktop” 窗口，按以下步骤创建连接。如下图所示：
![](https://main.qcloudimg.com/raw/d8e20278dd7c8aed487be2c43986f5e4.png)
    1. 在 “PC name” 处输入云服务器公网 IP。
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
