## 操作场景
Rdesktop 是远程桌面协议（RDP）的开源客户端，用于进行连接 Windows 云服务器等操作。本文介绍 Linux 机器通过 rdesktop 快速上传文件至 Windows Server 2012 R2 操作系统的腾讯云轻量应用服务器。

## 前提条件
已获取登录轻量应用服务器的管理员帐户及密码。
- Windows 轻量应用服务器默认管理员帐户为 Administrator。
- 如果您忘记了登录密码，请 [重置密码](https://cloud.tencent.com/document/product/1207/44575)。

## 操作步骤
### 获取公网 IP
登录 [轻量应用服务器控制台](https://console.cloud.tencent.com/lighthouse/instance/index)，在“服务器”页面中获取需上传文件轻量应用服务器的公网 IP。

### 安装 rdesktop
1. 在终端执行以下命令，下载 rdesktop 安装包，此步骤以 rdesktop 1.8.3 版本为例。
```
wget https://github.com/rdesktop/rdesktop/releases/download/v1.8.3/rdesktop-1.8.3.tar.gz
```
如果您需要最新的安装包，可以前往 [GitHub rdesktop 页面](https://github.com/rdesktop/rdesktop/releases) 查找最新安装包，并在命令行中替换为最新安装路径。
2. 依次执行以下命令，解压安装包并进入安装目录。
```
tar xvzf rdesktop-1.8.3.tar.gz
```
```
cd rdesktop-1.8.3
```
3. 依次执行以下命令，编译安装 rdesktop。
```
./configure 
```
```
make
```
```
make install
```
4. 安装完成后，可执行以下命令查看是否成功安装。
```
rdesktop
```

### 上传文件
1. 执行以下命令，指定共享给轻量应用服务器的文件夹。
```
rdesktop 轻量应用服务器公网IP  -u 轻量应用服务器帐号 -p 轻量应用服务器登录密码 -r disk:指定共享文件夹名=本地文件夹路径
```
例如，执行以下命令，将本地计算机的 `/home` 文件夹共享至指定轻量应用服务器中，并将共享文件夹重命名为 `share`。
```
rdesktop 118.xx.248.xxx  -u Administrator -p 12345678 -r disk:share=/home
```
成功共享后将打开 Windows 轻量应用服务器界面。
选择左下角的<img src="https://main.qcloudimg.com/raw/87d894e564b7e837d9f478298cf2e292.png" style="margin:-3px 0px"> > 【这台电脑】，您可在轻量应用服务器系统界面查看已共享的文件夹。如下图所示：
![](https://main.qcloudimg.com/raw/85bbb5408d198b3ee2efc52cee86a639.png)
2. 双击打开共享文件夹，并将需要上传的本地文件复制到 Windows 轻量应用服务器的其他硬盘中，即完成文件上传操作。
例如，将 `share` 文件夹中的 A 文件复制到 Windows 轻量应用服务器的 C: 盘中。

### 下载文件
如需将 Windows 轻量应用服务器中的文件下载至本地计算机，也可以参照上传文件的操作，将所需文件从 Windows 轻量应用服务器中复制到共享文件夹中，即可完成文件下载操作。
