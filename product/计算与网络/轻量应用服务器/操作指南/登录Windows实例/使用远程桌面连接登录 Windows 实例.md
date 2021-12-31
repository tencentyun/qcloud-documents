## 操作场景
本文介绍如何在 Windows 、Linux 及 Mac OS 系统的本地计算机中通过远程桌面登录 Windows 实例。

## 适用本地操作系统
Windows、Linux 和 Mac OS 都可以使用远程桌面登录轻量应用服务器。

## 前提条件

- 您已获取远程登录 Windows 实例需要使用实例的管理员帐号（Administrator）和对应的密码。
	- 如在创建实例时设置登录密码，则请使用该密码登录。如忘记密码，则请 [重置密码](https://cloud.tencent.com/document/product/1207/44575) 。
	- 如在创建实例时选择系统随机生成密码，则请往 [站内信](https://console.cloud.tencent.com/message) 获取初始密码。
- 请确认本地计算机与实例之间的网络连通正常，以及实例的防火墙已放行3389端口（创建实例时默认已开通3389端口）。

## 操作步骤
请对应本地操作系统，选择以下方式使用远程桌面登录 Windows 实例：

<dx-tabs>
::: Windows 系统
>? 以下操作步骤以 Windows 7 操作系统为例。
>
1. 在本地 Windows 计算机上，单击  <img src="https://main.qcloudimg.com/raw/370daffec54024ee262d1e5dbcd4bde2.png" style="margin: 0;width: 35px;">，在**搜索程序和文件**中，输入 **mstsc**，按 **Enter**，打开远程桌面连接对话框。如下图所示：
![](https://main.qcloudimg.com/raw/38e9d9ac0485bf8ad3a209092a1284ba.png)
2. 在“计算机”后面，输入 Windows 实例的公网 IP，单击**连接**。
3. 在弹出的 “Windows 安全” 窗口中，输入实例的管理员帐号和密码，如下图所示：
>? 若弹出 “是否信任此远程连接？” 对话框，可勾选 “不再询问我是否连接到此计算机”，单击**连接**。
>
![](https://main.qcloudimg.com/raw/3a9aa79200ace4a6ebd68a6e511a341d.png)
4. 单击**确定**，即可登录到 Windows 实例。

:::
::: Linux 系统
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
4. [](id:step04)执行以下命令，连接远程 Windows 实例。
>? 请将示例中的参数修改为您自己的参数。
>
```
rdesktop -u Administrator -p <your-password> <hostname or IP address>
```
 - `Administrator` 即为前提条件中获得的管理员帐号。
 - `<your-password>` 即为您设置的登录密码。
  如果您忘记密码，请 [重置密码](https://cloud.tencent.com/document/product/1207/44575)。
 - `<hostname or IP address>` 即为您的 Windows 实例公网 IP 或自定义域名。
:::
::: MacOS 系统
>?
>- 以下操作以 Microsoft Remote Desktop for Mac 为例。微软官方已于2017年停止提供 Remote Desktop 客户端的下载链接，转由其子公司 HockeyApp 进行 Beta 版本的发布。您可前往 [Microsoft Remote Desktop Beta](https://install.appcenter.ms/orgs/rdmacios-k2vy/apps/microsoft-remote-desktop-for-mac/distribution_groups/all-users-of-microsoft-remote-desktop-for-mac) 下载 Beta 版本。
>- 以下操作以连接 Windows Server 2012 R2 操作系统的轻量应用服务器为例。
>
1. 下载 Microsoft Remote Desktop for Mac 并在本地进行安装。
2. 启动 MRD，并单击 **Add Desktop**。如下图所示：
![](https://main.qcloudimg.com/raw/e69528d10e9a17dfa26119a090766c49.png)
3. 弹出的 “Add Desktop” 窗口，按以下步骤创建连接。如下图所示：
![](https://main.qcloudimg.com/raw/d8e20278dd7c8aed487be2c43986f5e4.png)
    1. 在 “PC name” 处输入实例公网 IP。
    2. 单击 **Add** 确认创建 。
    3. 其余选项保持默认设置，完成创建连接。
    即可在窗口中查看已成功创建的连接。如下图所示：
![](https://main.qcloudimg.com/raw/1c0eff28aa68a7f02e8f295917bb603b.png)
4. 双击打开新创建的连接，并在弹出的窗口中根据提示，输入在前提条件中获取的管理员帐号和密码，单击 **Continue**。
如果您忘记密码，请 [重置密码](https://cloud.tencent.com/document/product/1207/44575)。
5. 在弹出的窗口中单击 **Continue** 确认连接。如下图所示：
![](https://main.qcloudimg.com/raw/61b3d9566365183fcc1d92c2f6bc2e7b.png)
成功连接后将打开 Windows 实例界面。如下图所示：
![](https://main.qcloudimg.com/raw/5a524210acd13624af7263b6de3aea54.png)
:::
</dx-tabs>


