# 登录Windows实例

创建Windows实例后，在实例列表中选择需要远程登录的实例，点击【登录】
![](https://main.qcloudimg.com/raw/876fcf96c4d24635906bd311f223a8a2.png)

您可以根据**本地操作系统**以及**是否是否有公网IP**来选择不同的登录方式连接并登录CVM实例。登录方式可以参考以下表格：

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

## 使用远程桌面登录

介绍如何通过远程桌面连接登录Windows实例

### 适用本地操作系统

Windows

### 操作步骤：

1. 在本地Windows机器上，单击【开始】-【运行】，输入<code>mstsc</code>，打开远程桌面连接对话框。
2. 输入您要登录的Windows实例的公网IP。您可以登录[云服务器控制台](https://console.cloud.tencent.com/cvm/index)查看云服务器的公网IP。
3. 点击【连接】，在打开的界面中输入管理员账号对应的密码。
4. 点击【确定】即可登录到Windows实例。



## 使用rdesktop登录

介绍如何使用rdesktop登录Windows实例。有关rdesktop的更多内容，请参考[rdesktop官方说明](http://www.rdesktop.org/)。

### 适用本地操作系统

Linux

### 操作步骤：

1. 下载并安装rdesktop。

   运行<code>rdesktop</code>命令检查rdesktop是否已经安装。若未安装 [转到 github 下载最新安装包](https://github.com/rdesktop/rdesktop/releases)。

   并在相应目录下运行以下命令解压和安装：

   ```
   tar xvzf rdesktop-<x.y.z>.tar.gz ##替换x.y.z为下载的版本号 
   cd rdesktop-x.y.z
     ./configure 
   make 
   make install
   ```

2. 远程连接Windows实例。

   ```
   rdesktop -u Administrator -p <your-password> <hostname or ip address>
   ```

   其中 <code>-u</code> 连接用户名即 `Administrator`，<code>-p</code> 连接在先决条件中获得的密码，<hostname or ip address>为您的 Windows实例公网IP或自定义域名。
  
## 使用Microsoft Remote Desktop for Mac登录

介绍如何使用Microsoft Remote Desktop for Mac远程登录Windows实例

### 适用本地操作系统

Mac OS

### 操作步骤

1. 下载[Microsoft Remote Desktop for Mac](https://rink.hockeyapp.net/apps/5e0c144289a51fca2d3bfa39ce7f2b06/)并打开下载后的客户端。

   该测试版本客户端由微软官方维护，我们推荐您优先使用该版本客户端（微软已于 2017 年取消其官网提供的下载链接，转而通过其子公司 HockeyApp 的页面进行 Beta 版本的发布）。

2. 在输入框输入Windows服务器的公网IP。

3. 单击【连接】，在新打开的界面中输入前提条件中获取的管理员账号和对应的密码。



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

2. 在 “云主机” 页面中，选择需要登录的 Linux 云服务器，单击【登录】。

3. 在弹出的 “登录Linux云服务器” 窗口中，选择 “浏览器 VNC 方式登录”，单击【立即登录】。如下图所示：
   

## 远程连接出现问题？

如果登录失败，请检查您的云服务器实例是否允许 3389 端口的入流量。端口的查看请参考 [安全组](https://cloud.tencent.com/doc/product/213/5221)，若您的云服务器处于 [私有网络](https://cloud.tencent.com/doc/product/213/5227) 环境下，请同时查看相关子网的 [网络ACL](https://cloud.tencent.com/doc/product/215/5132) 。
