## 操作场景
本文档以 CentOS 7.6 操作系统的腾讯云轻量应用服务器为例，通过 SCP 向 Linux 轻量应用服务器上传或下载文件。


<dx-alert infotype="explain" title="">
在参考文档操作前，请确保您已设置轻量应用服务器的管理员帐户及密码。如果您未设置或忘记密码，则请 [重置密码](https://cloud.tencent.com/document/product/1207/44575)。
</dx-alert>


## 操作步骤
### 获取公网 IP
登录 [轻量应用服务器控制台](https://console.cloud.tencent.com/lighthouse/instance/index)，在“服务器”页面中获取需上传文件轻量应用服务器的公网 IP。


### 上传文件
1. 在本地机器执行以下命令，向 Linux 轻量应用服务器上传文件。
```shellsession
scp 本地文件地址 轻量应用服务器用户名@轻量应用服务器实例公网 IP/域名:轻量应用服务器文件地址
```
例如，您需要将本地文件 `/home/lnmp0.4.tar.gz` 上传至公网IP地址为 `129.20.0.2` 的轻量应用服务器对应目录下，则执行的命令如下：
```shellsession
scp /home/Inmp0.4.tar.gz root@129.20.0.2:/home/Inmp0.4.tar.gz
```
2. 输入 **yes** 后按 **Enter** 确认上传，并输入登录密码，即可完成上传。


### 下载文件
1. 在本地机器执行以下命令，将 Linux 轻量应用服务器上的文件下载至本地。
```shellsession
scp 轻量应用服务器用户名@轻量应用服务器实例公网 IP/域名:轻量应用服务器文件地址 本地文件地址 
```
例如，您需要将 IP 地址为 `129.20.0.2` 的轻量应用服务器文件 `/home/lnmp0.4.tar.gz` 下载至本地对应目录下，则执行的命令如下：
```shellsession
scp root@129.20.0.2:/home/Inmp0.4.tar.gz /home/Inmp0.4.tar.gz
```
