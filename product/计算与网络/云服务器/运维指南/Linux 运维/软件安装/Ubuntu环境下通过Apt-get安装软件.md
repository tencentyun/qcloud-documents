## 操作场景

为提升用户在云服务器上的软件安装效率，减少下载和安装软件的成本，腾讯云提供了 Apt-get 下载源。在 Ubuntu 环境下，用户可通过 Apt-get 快速安装软件。对于 Apt-get 下载源，不需要添加软件源，可以直接安装软件包。

## 前提条件
已登录操作系统为 Ubuntu 的云服务器。

## 操作步骤
>?以下操作以安装 Nginx 为例。
>

### 查看可安装的软件
执行以下命令，查看可安装的软件。
```
sudo apt-cache search all
```

### 安装软件
执行以下命令，安装 Nginx。 
```
sudo apt-get install nginx
```
确认软件信息无误后，键入 `Y` ，同意安装，等待至软件安装完成即可。如下图所示：
![](https://mc.qcloudimg.com/static/img/d03f55bba1690ff30532b73148ccc1e9/45.png)

### 查看已安装软件信息
根据实际需求，执行不同的命令查看已安装的软件信息。
- 执行以下命令，查看软件包所在的目录以及该软件包中的所有文件。
``` 
sudo dpkg -L 软件名 
```
- 执行以下命令，查看软件包的版本信息。
``` 
sudo dpkg -l 软件名 
```

查看已安装的 Nginx 信息。如下图所示：
![](https://mc.qcloudimg.com/static/img/8bbc99d7a31e8463da36f3dc2221c028/46.png)



