## 操作场景

RDP 为腾讯云推荐的登录方式。无论您的本地系统为 Windows，Linux 或者 Mac OS，都可以通过 RDP 登录。本文介绍如何使用 RDP 文件登录 Windows 实例。

## 适用本地操作系统
Windows，Linux 和 Mac OS

## 前提条件

- 已获取远程登录 Windows 实例需要使用实例的管理员帐号和对应的密码。
 - Windows 实例的管理员帐号统一为 **Administrator**。
 - 如果您在购买实例时选择**自动生成密码**，则可登录 [腾讯云控制台](https://console.cloud.tencent.com/)，单击右上角的 <img src="https://main.qcloudimg.com/raw/60e7d0de182a973d69fb82b69d01f52a.png" style="margin: 0;"></img>，进入“【腾讯云】请查收您新购买的云服务器”页面，查看初始密码。
 - 如果您在购买实例时选择**自定义密码**，则登录密码为您在购买云服务器实例时指定的密码。
 - 如果您忘记登录云服务器的密码，请参考 [重置实例密码](https://cloud.tencent.com/document/product/213/16566) 进行重置。
- 已打开云服务器实例的3389号端口。
您可以通过 [检查网络连通性](https://cloud.tencent.com/document/product/213/10232#.E6.AD.A5.E9.AA.A4.E4.B8.80.EF.BC.9A.E6.A3.80.E6.9F.A5.E7.BD.91.E7.BB.9C.E8.BF.9E.E9.80.9A.E6.80.A7) 检查3389号端口是否放通。如果端口不通，您可以在 [配置安全组](https://cloud.tencent.com/document/product/213/15377) 时设置端口的入站/出站规则。
- 云服务器实例已购买公网 IP 并获取到公网 IP。
实例的公网 IP 可登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/index) 进行查看。

## 操作步骤

### Windows 系统使用 RDP 登录
1. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/index)。
2. 在实例列表中，选择需要登录的 Windows 云服务器，单击【登录】。如下图所示：
![](https://main.qcloudimg.com/raw/bc452fce3b682d24933e73f4d15c0d7b.png)
3. 在弹出的【登录Windows实例】窗口中，选择【使用 RDP 文件登录】，单击【下载 RDP 文件】到本地。
![](https://main.qcloudimg.com/raw/bfbdf813684e34b236b90b9e1a19009b.png)
4. 双击下载到本地的 RDP 文件，远程连接到 Windows 云服务器。

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
3. 在待安装 rdesktop 的目录下，执行以下命令，解压和安装 rdesktop。
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
>! Remote Desktop 客户端为测试版客户端，由微软官方维护，推荐您优先使用此版本客户端。微软官方已于2017年停止提供 Remote Desktop 客户端的下载链接，转由其子公司 HockeyApp 进行 Beta 版本的发布。您也可以从 [Mac App Store](https://itunes.apple.com/us/app/microsoft-remote-desktop/id715768417) 下载 Microsoft Remote Desktop 客户端。但该客户端不面向中国地区用户开放，您需要拥有其他地区 AppleID 账号才可下载。
>
2. 打开客户端工具，单击【Add Deskop】。如下图所示：
![](https://main.qcloudimg.com/raw/d310a22009134182def49929625e6f1d.png)
3. 在弹出的对话框中，输入 Windows 实例的公网 IP，单击【Add】，添加远程桌面。如下图所示：
![](https://main.qcloudimg.com/raw/57d7f343e8d52d9365fcd4f4ada5d090.png)
4. 双击打开新添加的远程桌面，输入实例的管理员帐号和对应的密码，远程连接到 Windows 云服务器。

