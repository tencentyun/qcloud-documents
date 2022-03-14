## 操作场景
Rdesktop 是远程桌面协议（RDP）的开源客户端，用于进行连接 Windows 云服务器等操作。本文介绍本地 Linux 机器通过 rdesktop 快速上传文件至 Windows Server 2012 R2 操作系统的腾讯云云服务器（CVM）。
>? 
>- 本地 Linux 机器需搭建可视化界面，否则无法使用 rdesktop。
>- 本文 Linux 机器操作系统以 CentOS 7.6 为例，不同版本的操作系统步骤可能有一定区别，请您结合实际业务情况参考文档进行操作。  
>

## 前提条件
已购买 Windows 云服务器。

## 操作步骤
### 获取公网 IP
登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/index)，在实例列表页面记录需上传文件云服务器的公网 IP。如下图所示：
![](https://main.qcloudimg.com/raw/ea509a3a924e9cafc54af146acaa03d7.png)

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
1. 执行以下命令，指定共享给云服务器的文件夹。
```
rdesktop 云服务器公网IP  -u 云服务器帐号 -p 云服务器登录密码 -r disk:指定共享文件夹名=本地文件夹路径
```
>?
>- 云服务器的帐号默认为 `Administrator`。
>- 如果您使用系统默认密码登录实例，请前往 [站内信](https://console.cloud.tencent.com/message) 获取。
>- 如果您忘记密码，请 [重置实例密码](https://cloud.tencent.com/document/product/213/16566)。
>
例如，执行以下命令，将本地计算机的 `/home` 文件夹共享至指定云服务器中，并将共享文件夹重命名为 `share`。
```
rdesktop 118.xx.248.xxx  -u Administrator -p 12345678 -r disk:share=/home
```
成功共享后将打开 Windows 云服务器界面。
选择左下角的<img src="https://main.qcloudimg.com/raw/87d894e564b7e837d9f478298cf2e292.png" style="margin:-3px 0px"> > 【这台电脑】，您可在云服务器系统界面查看已共享的文件夹。如下图所示：
![](https://main.qcloudimg.com/raw/85bbb5408d198b3ee2efc52cee86a639.png)
2. 双击打开共享文件夹，并将需要上传的本地文件复制到 Windows 云服务器的其他硬盘中，即完成文件上传操作。
例如，将 `share` 文件夹中的 A 文件复制到 Windows 云服务器的 C: 盘中。

### 下载文件
如需将 Windows 云服务器中的文件下载至本地计算机，也可以参照上传文件的操作，将所需文件从 Windows 云服务器中复制到共享文件夹中，即可完成文件下载操作。
