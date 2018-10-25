为了提升用户在云服务器上的软件安装效率，减少下载和安装软件的成本，腾讯云提供了Apt-get下载源。操作系统为Ubuntu12.04的云服务器，用户可通过Apt-get快速安装软件。

对于apt-get下载源，不需要添加软件源，可以直接安装软件包。为了加速软件安装，目前系统已经在内网预先配置了Ubuntu的mirror，这个mirror是官方x86_64的完全镜像，与官网源一致。 

## 1. 安装步骤
1) 登录操作系统为Ubuntu12.04的云服务器

2) 通过以下命令安装软件：

```
sudo apt-get install
```
示例如下：

```
sudo apt-get install nginx php5-cli php5-cgi php5-fpm php5-mcrypt php5-mysql mysql-client-core-5.5 mysql-server-core-5.5
```

结果：

![](//mccdn.qcloud.com/img56af4dfeb631a.png)

3) 输入“Y”确认后，开始安装软件，直至软件安装完成。

##  2. 查看安装的软件信息
软件安装完成后，可通过以下命令查看软件包所在的目录，及该软件包中的所有文件：

```
sudo dpkg -L 
```

可通过以下命令查看软件包的版本信息：

```
sudo dpkg -l 
```

示例如下：

```
sudo dpkg -L nginx 
sudo dpkg -l nginx
```

结果如下（实际的版本可能和此版本不一致，请以实际查询到的版本为准）：
![](//mccdn.qcloud.com/img56af4f1d9e433.png)
![](//mccdn.qcloud.com/img56af4f7f57949.png)
