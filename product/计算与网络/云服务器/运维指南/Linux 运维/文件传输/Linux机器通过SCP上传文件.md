## 操作场景
本文档以 CentOS 7.6 操作系统的腾讯云云服务器（CVM）为例，通过 SCP 向 Linux 云服务器上传或下载文件。


## 前提条件
已购买 Linux 云服务器。

## 操作步骤
### 获取公网 IP
登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/index)，在实例列表页面记录需上传文件云服务器的公网 IP。如下图所示：
![](https://main.qcloudimg.com/raw/61e6078d313fecda9ffeb8f37b127a42.png)


### 上传文件
1. 在 Linux 操作系统的计算机上，执行以下命令，向 Linux 云服务器上传文件。
```
scp 本地文件地址 云服务器帐号@云服务器实例公网 IP/域名:云服务器文件地址
```
例如，您需要将本地文件 `/home/lnmp0.4.tar.gz` 上传至 IP 地址为 `129.20.0.2` 的云服务器对应目录下，则执行的命令如下：
```
scp /home/Inmp0.4.tar.gz root@129.20.0.2:/home/Inmp0.4.tar.gz
```
2. 输入 **yes** 后按 **Enter** 确认上传，并输入登录密码，即可完成上传。
 - 如果您使用系统默认密码登录实例，请前往 [站内信](https://console.cloud.tencent.com/message) 获取。
 - 如果您忘记密码，请 [重置实例密码](https://cloud.tencent.com/document/product/213/16566)。

### 下载文件
1. 在 Linux 操作系统的计算机上，执行以下命令，将 Linux 云服务器上的文件下载至本地。
```
scp 云服务器帐号@云服务器实例公网 IP/域名:云服务器文件地址 本地文件地址 
```
例如，您需要将 IP 地址为 `129.20.0.2` 的云服务器文件 `/home/lnmp0.4.tar.gz` 下载至本地对应目录下，则执行的命令如下：
```
scp root@129.20.0.2:/home/Inmp0.4.tar.gz /home/Inmp0.4.tar.gz
```


