## 操作场景
本文介绍如何在 Linux 及 Mac OS 系统的本地机器上使用 FTP 服务，将文件从本地上传到腾讯云轻量应用服务器中。

## 前提条件
已在轻量应用服务器中搭建 FTP 服务。具体操作请参考 [Linux 轻量应用服务器搭建 FTP 服务](https://cloud.tencent.com/document/product/1207/47638)。

## 操作步骤
### 获取公网 IP
登录 [轻量应用服务器控制台](https://console.cloud.tencent.com/lighthouse/instance/index)，在“服务器”页面中获取需上传文件轻量应用服务器的公网 IP。

### Linux 系统使用 FTP 服务
1. 执行以下命令，安装 ftp。
<dx-alert infotype="explain" title="">
若 Linux 系统的本地机器已安装了 ftp，请跳过此步骤，执行下一步。
</dx-alert>
```shellsession
yum -y install ftp
```
2. 执行以下命令，在本地机器上连接轻量应用服务器，并根据界面提示，输入 FTP 服务的用户名和密码。
```shellsession
ftp 轻量应用服务器的 IP 地址
```
进入如下界面，即表示连接成功。
![](https://main.qcloudimg.com/raw/9d93f45167addf70e023a21543af59f8.png)

#### 上传及下载文件
<dx-tabs>
::: 上传文件
执行以下命令，将本地文件上传至轻量应用服务器中。
```shellsession
put local-file [remote-file]
```
例如，将本地文件 `/home/1.txt` 上传到轻量应用服务器。
```shellsession
put /home/1.txt 1.txt
```
:::
::: 下载文件
执行以下命令，将轻量应用服务器中的文件下载至本地。
```shellsession
get [remote-file] [local-file]
```
例如，将轻量应用服务器中的 `A.txt` 文件下载到本地的 `/home` 目录下。
```shellsession
get A.txt /home/A.txt
```
:::
</dx-tabs>

### Mac OS 系统使用 FTP 服务

#### MacOS 本地终端
1. 打开 MacOS 终端。
2. 执行以下命令，安装 FTP。
```Plaintext
brew install telnet 
brew install inetutils 
brew link --overwrite inetutils
```
<dx-alert infotype="explain" title="">
若 MacOS 系统的本地机器已安装了 FTP，请跳过此步骤，执行下一步。
</dx-alert>
3. 执行以下命令，在本地机器上连接轻量应用服务器，并根据界面提示，输入 FTP 服务的用户名和密码：
```Plaintext
 	FTP 轻量应用服务器公网 IP。
```
4. 进入如下界面，即表示连接成功。

 <img style="width:600px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/3e011bb9c5f06656502739d8b62a1508.png" />

### FileZilla
1. 下载并安装 FileZilla。
	- 关于 FileZilla 的下载与安装请查看官方文档。
2. 创建一个新的连接，填写FTP服务器的 IP 地址、端口（不填默认为21）、FTP 用户名和密码。
 <img style="width:600px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/8df124b600e2c7ade5896ba19a25b8eb.png" />
3. 登录成功，可以开始传输文件。

 <img style="width:600px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/47b2d11cae4e434eb6953cef53cf9b74.png" />
 

