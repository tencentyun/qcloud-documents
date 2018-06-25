Ubuntu 官方已经停止了 Ubuntu 10.04 LTS的维护，因此，现腾讯云也已将 Ubuntu 10.04 版本的公有镜像下线。

在最新的官方源仓库中已经删除了 Ubuntu10.04 LTS的相关目录树，腾讯云软件仓库与官方保持一致，因此不再在官方源目录树提供对Ubuntu 10.04 LTS的支持，建议用户更换更高版本的镜像。

如果存量用户希望继续使用 Ubuntu 10.04 的软件源，我们提供两种方式支持：

## 方法一：手动更新配置文件
为提高用户使用质量，腾讯云软件仓库拉取了Ubuntu 10.04 LTS的官方归档源`http://old-releases.ubuntu.com/ubuntu/`供用户使用，用户可通过手动修改配置文件正常使用该仓库：

打开apt源配置文件` vi /etc/apt/sources.list`,修改以下代码：

```
deb-src http://mirrors.tencentyun.com/old-archives/ubuntu lucid main restricted universe multiverse
deb-src http://mirrors.tencentyun.com/old-archives/ubuntu lucid-updates main restricted universe multiverse
deb-src http://mirrors.tencentyun.com/old-archives/ubuntu lucid-security main restricted universe multiverse
deb-src http://mirrors.tencentyun.com/old-archives/ubuntu lucid-backports main restricted universe multiverse
deb http://mirrors.tencentyun.com/old-archives/ubuntu lucid main restricted universe multiverse
deb http://mirrors.tencentyun.com/old-archives/ubuntu lucid-updates main restricted universe multiverse
deb http://mirrors.tencentyun.com/old-archives/ubuntu lucid-security main restricted universe multiverse
deb http://mirrors.tencentyun.com/old-archives/ubuntu lucid-backports main restricted universe multiverse
```

## 方法二：运行自动脚本
通过腾讯云提供的脚本 [old-archive.run](http://ubuntu10-10016717.cos.myqcloud.com/old-archive.run) 进行配置，将此文件下载至 Ubuntu 10.04 云服务器内部并执行以下命令：

```
chmod +x old-archive.run
./old-archive.run
```