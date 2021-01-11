## 操作场景
WinSCP 是一个在 Windows 环境下使用 SSH 的开源图形化 SFTP 客户端，同时支持 SCP 协议。它的主要功能是在本地与远程计算机之间安全地复制文件。与使用 FTP 上传代码相比，通过 WinSCP 可以直接使用服务器账户密码访问服务器，无需在服务器端做任何配置。

## 前提条件
本地计算机已下载并安装 WinSCP 客户端（获取途径：建议从 [官方网站](http://winscp.net/eng/docs/lang:chs) 获取最新版本）。

## 操作步骤

### 登录 WinSCP

1. 打开 WinSCP，弹出“WinSCP 登录”对话框。如下图所示：
![](https://mc.qcloudimg.com/static/img/98d96ee1c3b65a3d94e99bb447c8a294/22.png)
2. 设置登录参数：
 - 协议：选填 SFTP 或者 SCP 均可。
 - 主机名：云服务器的公网 IP。登录 [云服务器控制台](https://console.cloud.tencent.com/cvm) 即可查看对应云服务器的公网 IP。
 - 端口：默认为22。
 - 密码：云服务器的用户名对应的密码。
 - 用户名：云服务器的系统用户名。
	 - SUSE/CentOS/Debian 系统：root
	 - Ubuntu 系统：ubuntu
3. 单击【登录】，进入 “WinSCP” 文件传输界面。如下图所示：
![](https://main.qcloudimg.com/raw/6434c5c5e622db6eff83af85d6bd1d16.png)

### 上传文件
1. 在 “WinSCP” 文件传输界面的右侧窗格中，选择文件在服务器中待存放的目录，如“/user”。
2. 在 “WinSCP” 文件传输界面的左侧窗格中，选择本地计算机存放文件的目录，如“F:\SSL证书\Nginx”，选中待传输的文件。
3. 在 “WinSCP” 文件传输界面的左侧菜单栏中，单击【上传】。如下图所示：
![上传](https://main.qcloudimg.com/raw/3d0ed8cf62d43bc2b5ece58ae9b513a6.png)
4. 在弹出的“上传”对话框中，确认需要上传的文件及远程目录，单击【确定】，即可从本地计算机将文件上传到云服务器中。

### 下载文件
1. 在 “WinSCP” 文件传输界面的左侧窗格中，选择待下载至本地计算机的存放目录，如“F:\SSL证书\Nginx”。
2. 在 “WinSCP” 文件传输界面是右侧窗格中，选择服务器存放文件的目录，如“/user”，选中待传输的文件。
3. 在 “WinSCP” 文件传输界面的右侧菜单栏中，单击【下载】。如下图所示：
![下载](https://main.qcloudimg.com/raw/b287a5507406fc97a4718f3e314e2aaf.png)
4. 在弹出的“下载”对话框中，确认需要下载的文件及远程目录，单击【确定】，即可从云服务器将文件下载到本地计算机中。



