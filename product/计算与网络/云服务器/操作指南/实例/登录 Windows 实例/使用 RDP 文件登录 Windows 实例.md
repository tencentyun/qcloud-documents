## 操作场景

RDP 为腾讯云推荐的登录方式。无论您的本地系统为 Windows，Linux 或者 Mac OS，都可以通过 RDP 登录。本文介绍如何使用 RDP 文件登录 Windows 实例。

## 适用本地操作系统
Windows，Linux 和 Mac OS

## 前提条件

- 已获取远程登录 Windows 实例需要使用实例的管理员帐号和对应的密码。
 - 如果您使用系统默认密码登录实例，请前往 [站内信](https://console.cloud.tencent.com/message) 获取。
 - 如果您忘记密码，请 [重置实例密码](https://cloud.tencent.com/document/product/213/16566)。
- 您的云服务器实例已购买公网 IP，且该实例已开通云服务器实例的3389号端口（对于通过快速配置购买的云服务器实例已默认开通）。

## 操作步骤

### Windows 系统使用 RDP 登录
1. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/index)。
2. 在实例的管理页面，选择需要登录的 Windows 云服务器，单击【登录】。如下图所示：
![](https://main.qcloudimg.com/raw/3106cebfdeae7762d656ffc68732e130.png)
3. 在弹出的【登录Windows实例】窗口中，选择【使用 RDP 文件登录】，单击【下载RDP文件】，将 RDP 文件下载到本地。
![](https://main.qcloudimg.com/raw/9bcfe6774b483261d61f648968efe5ee.png)
4. 双击已下载到本地的 RDP 文件，即可远程连接到 Windows 云服务器。

### Linux 系统使用 RDP 登录

>? 您需要安装相应的远程桌面连接程序，推荐使用 rdesktop 进行连接。更多详情请参考 [rdesktop 官方说明](http://www.rdesktop.org/)。
>
1. 执行以下命令，检查系统是否已安装 rdesktop。
```
rdesktop
```
 - 若已安装 rdesktop，请执行 [步骤4](#step04)。
 - 若未安装 rdesktop，请执行 [步骤2](#step02)。
2. <span id="step02">[切换至 GitHub 下载最新安装包](https://github.com/rdesktop/rdesktop/releases)。</span>
您也可以通过单击以下链接，下载 v1.8.3 版本的 rdesktop。
 - [rdesktop-1.8.3.tar.gz](https://mc.qcloudimg.com/static/archive/06483121ce067b537342687dd6a909d8/rdesktop-1.8.3.tar.gz)
 - [rdesktop-1.8.3.zip](https://mc.qcloudimg.com/static/archive/24adfd7586f55bd96cd6714a6078a4df/rdesktop-1.8.3.zip)
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
 - `<hostname or IP address>` 即为您的 Windows 实例公网 IP 或自定义域名。
 
###  MacOS 系统使用 RDP 登录

>? 以下操作以 Microsoft Remote Desktop for Mac 为例。
>
1. 下载 [Microsoft Remote Desktop for Mac](https://rink.hockeyapp.net/apps/5e0c144289a51fca2d3bfa39ce7f2b06/)。
>! Remote Desktop 客户端为测试版客户端，由微软官方维护，推荐您优先使用此版本客户端。微软官方已于2017年停止提供 Remote Desktop 客户端的下载链接，转由其子公司 HockeyApp 进行 Beta 版本的发布。您也可以从 Mac App Store 下载 Microsoft Remote Desktop 客户端。但该客户端不面向中国地区用户开放，您需要拥有其他地区 AppleID 账号才可下载。
>
2. 打开客户端工具，单击【Add Deskop】。如下图所示：
![](https://main.qcloudimg.com/raw/d310a22009134182def49929625e6f1d.png)
3. 在弹出的对话框中，输入 Windows 实例的公网 IP，单击【Add】，添加远程桌面。如下图所示：
![](https://main.qcloudimg.com/raw/57d7f343e8d52d9365fcd4f4ada5d090.png)
4. 双击打开新添加的远程桌面，输入实例的管理员帐号和对应的密码，远程连接到 Windows 云服务器。

