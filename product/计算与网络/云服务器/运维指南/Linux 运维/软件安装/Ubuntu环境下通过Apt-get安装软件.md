为提升用户在云服务器上的软件安装效率，减少下载和安装软件的成本，腾讯云提供了 Apt-get 下载源。在 Ubuntu 环境下，用户可通过 Apt-get 快速安装软件。对于 Apt-get 下载源，不需要添加软件源，可以直接安装软件包。为了加速软件安装，目前系统已经在内网预先配置了 Ubuntu 的镜像，这是官方 x86_64 的完全镜像，与官网源一致。

### 安装步骤
1. 登录操作系统为 Ubuntu 的云服务器。
2. 通过以下命令安装软件： 
```
sudo apt-get install 软件名称
```
![](https://mc.qcloudimg.com/static/img/d03f55bba1690ff30532b73148ccc1e9/45.png)
3. 确认软件信息无误后，键入`Y`进行安装，等待至软件安装完成即可。

### 查看已安装软件信息

软件安装完成后：
- 可通过命令` sudo dpkg -L 软件名 `查看软件包所在的目录以及该软件包中的所有文件。
- 可通过命令` sudo dpkg -l 软件名 `查看软件包的版本信息。

以 nginx 为例：
![](https://mc.qcloudimg.com/static/img/8bbc99d7a31e8463da36f3dc2221c028/46.png)