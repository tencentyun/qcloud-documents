# 登录Windows实例

创建Windows实例后，您可以根据**本地操作系统**以及**是否是否有公网IP**来选择不同的登录方式连接并登录CVM实例。登录方式可以参考以下表格：

| 本地操作系统 | 实例有公网IP                    | 实例没有公网IP |
| ------------ | --------------------------------- | ---------------------- |
| Windows      | 使用RDP登录<br> 远程桌面登录         |         VNC登录（不推荐）               |
| Linux<br>Mac OS | 使用RDP登录<br>rdesktop登录        |         VNC登录（不推荐）          |


## 前提条件

1. 远程登录Windows实例需要使用实例的管理员账号和对应的密码。对于Windows实例的管理员账号统一为**Administrator**。

- 若您在购买实例时选择**自动生成密码**，您可以在[腾讯云控制台](https://cloud.tencent.com/login)的右上角**消息中心**查找初始密码。

- 若您在购买实例时选择**自定义密码**，登录密码为您在购买实例时设置的密码。如果您忘记密码，可以通过[重置实例密码](https://cloud.tencent.com/document/product/213/16566)对密码进行重置。

2. 确保请云服务器3389号端口已开放，详见查看[安全组](https://cloud.tencent.com/doc/product/213/5221)及[网络ACL](https://cloud.tencent.com/doc/product/215/5132)。

## 使用RDP方式登录

方式待补充！需要与产品确认这个是否为推荐？之前的文档没有这部分内容。

## 本地为 Windows 计算机

### 登录工具

**在本地 Windows 机器上，使用远程桌面连接登录 Windows 实例。**

### 操作步骤

1. 在本地 Windows 机器上，单击【开始菜单】-【Run】，输入 `mstsc` 命令，即可打开远程桌面连接对话框。
2. 在输入框输入 Windows 服务器的公网 IP（登录 [云服务器控制台](https://console.cloud.tencent.com) 可查看云服务器的公网 IP），如下图所示：
![](//mccdn.qcloud.com/img56b1a11a3c31f.png)
3. 单击【连接】，在新打开的界面中输入前提条件中获取的管理员账号和对应的密码，如下图所示：
![](//mccdn.qcloud.com/static/img/878a0e8ef1a0bcc51ad5de2bcce4e353/image.png)
![](//mccdn.qcloud.com/static/img/e140d3151ac8747014313b33e6413568/image.png)
4. 单击【确定】，即可登录到 Windows 实例。

>! 如果登录失败，请检查您的云服务器实例是否允许 3389 端口的入流量。端口的查看请参考 [安全组](/doc/product/213/5221)，若您的云服务器处于 [私有网络](/doc/product/213/5227) 环境下，请同时查看相关子网的 [网络ACL](/doc/product/215/5132) 。 

## 本地为 Linux 计算机

### 登录工具

**本地 Linux 计算机登录 Windows 实例时，使用 rdesktop 登录。**
您需要安装相应的远程桌面连接程序，这里推荐使用 rdesktop 进行连接。有关 rdesktop 的更多内容，请参考 [rdesktop官方说明](http://www.rdesktop.org/) 。

### 操作步骤

1. 安装 rdesktop
运行 `rdesktop` 命令检查系统是否已经安装，若未安装则请 [转到 github 下载最新安装包 >>](https://github.com/rdesktop/rdesktop/releases)。
或者单击以下链接直接下载 v1.8.3版本：
 - [rdesktop-1.8.3.tar.gz](https://mc.qcloudimg.com/static/archive/06483121ce067b537342687dd6a909d8/rdesktop-1.8.3.tar.gz)
 - [rdesktop-1.8.3.zip](https://mc.qcloudimg.com/static/archive/24adfd7586f55bd96cd6714a6078a4df/rdesktop-1.8.3.zip)

 并在相应目录下运行以下命令解压和安装
```
tar xvzf rdesktop-<x.x.x>.tar.gz ##替换x.x.x为下载的版本号 
cd rdesktop-1.8.3
./configure 
make 
make install
```

2. 连接远程 Windows 实例
运行以下命令（将示例中的参数改为您自己的参数）：
```
rdesktop -u Administrator -p <your-password> <hostname or ip address>
```
其中：-u 连接用户名即 `Administrator`，-p 连接在先决条件中获得的密码，&lt;hostname or ip address&gt;为您的 Windows 实例公网 IP 或 自定义域名。
>! 如果登录失败，请检查您的云服务器实例是否允许 3389 端口的入流量。端口的查看请参考 [安全组](/doc/product/213/5221)，若您的云服务器处于 [私有网络](/doc/product/213/5227) 环境下，请同时查看相关子网的 [网络ACL](/doc/product/215/5132) 。 

## 本地为 Mac OS 计算机

### 登录工具

**当本地为 Mac OS 计算机时，使用 Microsoft Remote Desktop for Mac 登录 Windows 实例。**
Microsoft Remote Desktop for Mac 下载指引参见 [用于 Mac OS 的远程登录客户端下载指引](/document/product/213/12444)。

### 操作步骤

1. 打开客户端工具。
2. 在输入框输入 Windows 服务器的公网 IP。
3. 单击【连接】，在新打开的界面中输入前提条件中获取的管理员账号和对应的密码。

>! 如果登录失败，请检查您的云服务器实例是否允许 3389 端口的入流量。端口的查看请参考 [安全组](/doc/product/213/5221) ,若您的云服务器处于 [私有网络](/doc/product/213/5227) 环境下，请同时查看相关子网的 [网络ACL](/doc/product/215/5132) 。  



## 使用VNC远程登录实例（不推荐，当没有公网IP时使用）

VNC 登录是腾讯云为用户提供的一种通过 Web 浏览器远程连接云服务器的方式。在没有安装远程登录客户端或者客户端远程登录无法使用的情况下，用户可以通过 VNC 登录连接到云服务器，观察云服务器状态，并且可通过云服务器账户进行基本的云服务器管理操作。

### 使用限制：

- 使用VNC登录暂时不支持复制粘贴功能、中文输入法以及文件的上传、下载。
- 要使用VNC登录，需要使用主流浏览器，如Chrome，Firefox以及IE10以上版本。
- 该终端为独享，即同一时间只有一个用户可以使用 VNC 登录。

### 适用本地操作系统：

Windows，Linux和MacOS系统


### 操作步骤：

1. 登录[云服务器控制台](https://console.cloud.tencent.com/cvm/index)。

2. 在【云主机】页面中，选择需要登录的云服务器，单击【登录】。

3. 在弹出的【登录Windows云服务器】窗口中，选择【浏览器 VNC 方式登录】，单击【立即登录】。

4. 登录成功后，出现远程登录的界面。

## 远程连接出现问题？

如果登录失败，请检查您的云服务器实例是否允许 3389 端口的入流量。端口的查看请参考 [安全组](https://cloud.tencent.com/doc/product/213/5221)，若您的云服务器处于 [私有网络](https://cloud.tencent.com/doc/product/213/5227) 环境下，请同时查看相关子网的 [网络ACL](https://cloud.tencent.com/doc/product/215/5132) 。
