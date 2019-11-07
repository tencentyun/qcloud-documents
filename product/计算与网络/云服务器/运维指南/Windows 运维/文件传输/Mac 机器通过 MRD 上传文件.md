## 操作场景
Microsoft Remote Desktop（以下简称 MRD） 是微软推出的适用于 Mac 机器的远程桌面应用程序， 本文档介绍 Mac 机器通过 MRD 快速上传文件至 Windows 2012 操作系统的腾讯云云服务器（CVM）。 


## 前提条件
- 本地计算机已下载并安装 MRD。如果您的 Apple 账号不具备下载权限，可前往 [MRD 测试版](https://rink.hockeyapp.net/apps/5e0c144289a51fca2d3bfa39ce7f2b06/) 进行下载。
- MRD 支持 Mac OS 10.10 及以上版本，请确保使用支持的操作系统。
- 已购买 Windows 云服务器。


## 操作步骤
### 获取公网 IP
登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/index)，在实例列表页面记录需上传文件云服务器的公网 IP。如下图所示：
![](https://main.qcloudimg.com/raw/ea509a3a924e9cafc54af146acaa03d7.png)

### 上传文件
1. 启动 RD Beta，并单击【Add Desktop】。如下图所示：
![](https://main.qcloudimg.com/raw/b7d077ef17157254a04fc2c1f15cb3ae.png)
2. 在弹出的 “Add Desktop” 窗口中，按以下步骤选择需上传的文件夹并创建连接。如下图所示：
![](https://main.qcloudimg.com/raw/fc241ce8e4744bde57476ea823fcef72.png)
  1. 在 “PC name” 处输入已获取的云服务器公网 IP。
  2. 单击【Folders】切换到选择文件夹列表。
  3. 单击左下角的<img src="https://main.qcloudimg.com/raw/6f36e46cc0d87e9aadb735328d426e91.png" style="margin:-3px 0px">，并在弹出窗口中选择需上传的文件夹。
  4. 完成选择后，可查看需上传文件夹列表，并单击【Add】确认创建。
  其余选项保持默认设置。
3. 可在窗口中查看已成功创建的连接。如下图所示：
![](https://main.qcloudimg.com/raw/1c0eff28aa68a7f02e8f295917bb603b.png)
4. 双击此连接，在弹出窗口中根据以下提示输入登录名及密码，并单击【Continue】。如下图所示：
![](https://main.qcloudimg.com/raw/b04e8e0433b50ac0f3996dd02dcc1340.png)
 - **Username**：云服务器的用户名，请输入 `Administrator`。
 - **Password**：云服务器的登录密码。
     - 如果您使用系统默认密码登录实例，请前往 [站内信](https://console.cloud.tencent.com/message) 获取。
    - 如果您忘记密码，请 [重置实例密码](https://cloud.tencent.com/document/product/213/16566)。
5. 在弹出的窗口中单击【Continue】确认连接。如下图所示：
![](https://main.qcloudimg.com/raw/61b3d9566365183fcc1d92c2f6bc2e7b.png)
6. 成功连接后弹出 Windows 云服务器界面，如下图所示：
![](https://main.qcloudimg.com/raw/5a524210acd13624af7263b6de3aea54.png)
7. 选择左下角的<img src="https://main.qcloudimg.com/raw/2407190440fabdddc10c70c4df56a656.png" style="margin:-3px 0px">>【这台电脑】，即可看到已共享的文件夹。如下图所示：
![](https://main.qcloudimg.com/raw/b6a9fc9ef75131fab3549533187d24e3.png)
8. 双击打开文件夹，并将需要上传的文件复制到 Windows 云服务器的其他硬盘中，即完成文件上传操作。
