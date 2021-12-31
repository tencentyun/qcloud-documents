## 操作场景

本文介绍如何在 Linux 系统的本地机器上使用 FTP 服务，将文件从本地上传到云服务器中。

## 前提条件

已在云服务器中搭建 FTP 服务。
- 如果您的云服务器为 Linux 操作系统，具体操作请参考 [Linux 云服务器搭建 FTP 服务](https://cloud.tencent.com/document/product/213/10912)。
- 如果您的云服务器为 Windows 操作系统，具体操作请参考 [Windows 云服务器搭建 FTP 服务](https://cloud.tencent.com/document/product/213/10414)。

## 操作步骤

### 连接云服务器
1. 执行以下命令，安装 ftp。
>? 若 Linux 系统的本地机器已安装了 ftp，请跳过此步骤，执行下一步。
>
```
yum -y install ftp
```
2. 执行以下命令，在本地机器上连接云服务器，并根据界面提示，输入 FTP 服务的用户名和密码。
```
ftp 云服务器的 IP 地址
```
进入如下界面，即表示连接成功。
![](https://main.qcloudimg.com/raw/9d93f45167addf70e023a21543af59f8.png)

### 上传文件
执行以下命令，将本地文件上传至云服务器中。
```
put local-file [remote-file]
```
例如，将本地文件 `/home/1.txt` 上传到云服务器。
```
put /home/1.txt 1.txt
```

### 下载文件
执行以下命令，将云服务器中的文件下载至本地。
```
get [remote-file] [local-file]
```
例如，将云服务器中的 `A.txt` 文件下载到本地的 `/home` 目录下。
```
get A.txt /home/A.txt
```



