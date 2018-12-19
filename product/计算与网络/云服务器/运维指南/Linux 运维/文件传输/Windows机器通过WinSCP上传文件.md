WinSCP 是一个在 Windows 环境下使用 SSH 的开源图形化 SFTP 客户端，同时支持 SCP 协议。它的主要功能是在本地与远程计算机之间安全地复制文件。与使用 FTP 上传代码相比，通过 WinSCP 可以直接使用服务器账户密码访问服务器，无需在服务器端做任何配置。

### 操作步骤
1. 下载 WinSCP 客户端并安装。下载地址：[官方下载](http://winscp.net/eng/docs/lang:chs)。
2. 安装完成后启动 WinSCP，界面如下。按图示填写信息并登录。
![](https://mc.qcloudimg.com/static/img/98d96ee1c3b65a3d94e99bb447c8a294/22.png)
** 字段填写说明：**
 - 协议：选填 SFTP 或者 SCP 均可。
 - 主机名：云服务器的公网 IP。登录 [云服务器控制台](https://console.cloud.tencent.com/cvm) 即可查看对应云服务器的公网 IP。
 - 端口：默认 22。
 - 密码：云服务器的用户名对应的密码。
 - 用户名：云服务器的系统用户名。
	 - SUSE/CentOS/Debian 系统：root
	 - Ubuntu 系统：ubuntu
3. 信息填写完毕之后单击 **登录**，界面如下:
![](//mccdn.qcloud.com/img56b0272d4ed3a.png)
4. 登录成功之后，鼠标选中左侧本地文件，拖拽到右侧的远程站点，即可将文件上传到 Linux 云服务器。
![](https://mc.qcloudimg.com/static/img/397117dd956265d42b12f6bf9cacb296/23.png)
