在启动了 Windows 类型的实例后，您可以连接并登录它。根据您本地的操作系统和 CVM 实例是否可被 Internet 访问，不同情况下可以使用不同的登录方式，具体内容可参考下表：
<table><tbody>
<tr><th>本地操作系统类型</th><th> 实例有公网 IP</th><th> 实例没有公网 IP</th></tr>
<tr><td>Windows</td><td>VNC 登录<br>远程桌面连接</td><td rowspan="3">VNC登录</td></tr>
<tr><td>Linux</td><td>VNC 登录<br>rdesktop登录</td></tr>
<tr><td>Mac OS</td><td>VNC 登录<br>rdesktop登录</td></tr>
</tbody></table>

## 前提条件
登录到云服务器时，需要使用管理员帐号和对应的密码。
- 管理员账号：对于 Windows 类型的实例，管理员帐号统一为 **Administrator**。
- 密码：
  - 若用户在启动实例时选择【自动生成密码】，则初始密码由系统随机分配。您可以登录 [腾讯云控制台](https://cloud.tencent.com/login)，单击右上角的消息中心，查收新购买的服务器，页面中将包含云服务器登录管理员帐号及初始密码。如下图所示：
  ![](https://main.qcloudimg.com/raw/15029612c2710cbd55d97255bf36a840.png)
  - 若用户在启动实例时选择【自定义密码】，则密码为用户在购买云服务器实例时指定的密码。有关密码的更多内容，请参考 [登录密码](/doc/product/213/6093) 。

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

>**注意：**
>如果登录失败，请检查您的云服务器实例是否允许 3389 端口的入流量。端口的查看请参考 [安全组](/doc/product/213/5221) ,若您的云服务器处于 [私有网络](/doc/product/213/5227) 环境下，请同时查看相关子网的 [网络ACL](/doc/product/215/5132) 。 

## 本地为 Linux 计算机
### 登录工具
**本地 Linux 计算机登录 Windows 实例时，使用 rdesktop 登录。**
您需要安装相应的远程桌面连接程序，这里推荐使用 rdesktop 进行连接。有关 rdesktop 的更多内容，请参考 [rdesktop官方说明](http://www.rdesktop.org/) 。

### 操作步骤
1. 安装 rdesktop
 	运行 `rdesktop` 命令检查系统是否已经安装，若未安装则请 [转到 github 下载最新安装包 >>](https://github.com/rdesktop/rdesktop/releases)
 	或 单击以下链接直接下载 v1.8.3版本：
 	[rdesktop-1.8.3.tar.gz](https://mc.qcloudimg.com/static/archive/06483121ce067b537342687dd6a909d8/rdesktop-1.8.3.tar.gz)
 	[rdesktop-1.8.3.zip](https://mc.qcloudimg.com/static/archive/24adfd7586f55bd96cd6714a6078a4df/rdesktop-1.8.3.zip)

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
	
	其中：-u 连接用户名即 `Administrator`，-p 连接在先决条件中获得的密码， <hostname or ip address>为您的 Windows 实例公网 IP 或 自定义域名。

> **注意：**
>如果登录失败，请检查您的云服务器实例是否允许 3389 端口的入流量。端口的查看请参考 [安全组](/doc/product/213/5221)，若您的云服务器处于 [私有网络](/doc/product/213/5227) 环境下，请同时查看相关子网的 [网络ACL](/doc/product/215/5132) 。 

## 本地为 Mac OS 计算机
### 登录工具
**当本地为 Mac OS 计算机时，使用 Microsoft Remote Desktop for Mac 登录 Windows 实例。**
Microsoft Remote Desktop for Mac 下载指引参见 [用于 Mac OS 的远程登录客户端下载指引](/document/product/213/12444)。

### 操作步骤
1. 打开客户端工具。
2. 在输入框输入 Windows 服务器的公网 IP。
3. 单击【连接】，在新打开的界面中输入前提条件中获取的管理员账号和对应的密码。

> **注意：**
> 如果登录失败，请检查您的云服务器实例是否允许 3389 端口的入流量。端口的查看请参考 [安全组](/doc/product/213/5221) ,若您的云服务器处于 [私有网络](/doc/product/213/5227) 环境下，请同时查看相关子网的 [网络ACL](/doc/product/215/5132) 。  

## 使用 VNC 登录
### 登录工具
VNC 登录是腾讯云为用户提供的一种通过 Web 浏览器远程连接云服务器的方式。在没有安装远程登录客户端或者客户端远登录无法使用的情况下，用户可以通过 VNC 登录连接到云服务器，观察云服务器状态，并且可通过云服务器账户进行基本的云服务器管理操作。

VNC 登录的场景至少包括以下几种：
- 查看云服务器的启动进度。
- 无法通过客户端 SSH 或 mstsc 登录时，通过 VNC 登录来登录服务器。

### 操作步骤
1. 登录 [云服务器控制台](https://console.cloud.tencent.com) 。
2. 在云服务器列表的操作列，单击【登录】按钮即可通过 VNC 连接至  Windows 云服务器。
![](//mccdn.qcloud.com/img56b1a6cb7b3e8.png)
3. 通过在左上角单击 Ctrl - Alt - Del 命令进入系统登录界面：
![](//mccdn.qcloud.com/img56b1a6ff2e305.png)

> **注意：**
> - 该终端为独享，即同一时间只有一个用户可以使用 VNC 登录。
> - 要正常使用 VNC 登录，需要使用现代浏览器，如：chrome，firefox，IE10及以上版本等。
> - 暂不支持文件上传下载。
