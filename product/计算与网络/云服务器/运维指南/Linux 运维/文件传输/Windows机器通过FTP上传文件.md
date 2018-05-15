用户可使用 FTP 通道，将应用程序从本地服务器上传到云服务器中。
### 操作步骤
#### 步骤一：在云服务器配置 FTP 服务
以 CentOS 系统为例。
1. 在 root 权限下，通过命令 `yum install vsftpd` 安装 vsftp。
2. 启动 vsftpd 服务之前，需要登录云服务器修改配置文件，禁用匿名登录。
   使用 `vim /etc/vsftpd/vsftpd.conf` 打开配置文件，将配置文件中第 11 行的 `anonymous_enable=YES` 改为`anonymous_enable=NO` 即可禁用匿名登录。
3. 使用 ` cat /etc/vsftpd/vsftpd.conf |grep ^[^#] ` 命令读取生效配置。
   返回结果为：
	```
		    local_enable=YES
			write_enable=YES
			local_umask=022
			anon_upload_enable=YES
			anon_mkdir_write_enable=YES
			anon_umask=022
			dirmessage_enable=YES
			xferlog_enable=YES
			connect_from_port_20=YES
			xferlog_std_format=YES
			listen=YES
			pam_service_name=vsftpd
			userlist_enable=YES
			tcp_wrappers=YES
		```
4. 使用 `service vsftpd start ` 命令启动 vsftpd 服务。
5. 设置 FTP 用户帐号。
	1）. 使用命令 ` useradd `设置 FTP 用户帐号。
	例如，设置账号为 “ftpuser1”，目录为 /home/ftpuser1，且设置不允许通过 SSH 登录的命令为：
	`useradd -m -d /home/ftpuser1 -s /sbin/nologin ftpuser1`。
	2）. 使用命令 ` password` 设置帐号对应密码。
	例如，设置上述帐号密码为“ftpuser1” 的命令为：
	`passwd ftpuser1`。
	设置成功后，即可通过该账号及密码登录 FTP 服务器。
6. 修改 vsftpd 的 pam 配置，使用户可以通过自己设置的 FTP 用户帐号和密码连接到云服务器。
使用命令 ` vim /etc/pam.d/vsftpd` 修改 pam 配置。
将 pam 配置内容修改为：
```
#%PAM-1.0 
auth required /lib64/security/pam_listfile.so item=user sense=deny file=/etc/ftpusers onerr=succeed 
auth required /lib64/security/pam_unix.so shadow nullok 
auth required /lib64/security/pam_shells.so 
account required /lib64/security/pam_unix.so 
session required /lib64/security/pam_unix.so 
```
通过命令 `cat /etc/pam.d/vsftpd` 确认修改后的文件是否正确。正确的返回结果应为：
```
auth required /lib64/security/pam_listfile.so item=user sense=deny file=/etc/ftpusers onerr=succeed 
auth required /lib64/security/pam_unix.so shadow nullok 
auth required /lib64/security/pam_shells.so 
account required /lib64/security/pam_unix.so 
session required /lib64/security/pam_unix.so 
```
完成修改后，使用命令 `service vsftpd restart`  重启 vsftpd 服务，使修改生效。
结果为：
```
Shutting down vsftpd: [ OK ]
Starting vsftpd for vsftpd: [ OK ]
```

#### 步骤二：上传文件到 Linux 云服务器
1. 下载并安装开源软件 FileZilla。
请使用 FileZilla 的 3.5.1 或 3.5.2 版本（使用 3.5.3 版本的 FileZilla 进行 FTP 上传会有问题）。
由于 FileZilla 官网上只提供了最新的 3.5.3 版本下载，因此建议用户自行搜索 3.5.1 或 3.5.2 的下载地址。
[单击此处](http://www.oldapps.com/filezilla.php?old_filezilla=6350) 可直达腾讯云建议的 3.5.1 下载地址。
2. 连接 FTP。
运行 FileZilla，进行主机、用户名、密码和端口配置，配置完成后单击 **快速链接**。
![](https://mc.qcloudimg.com/static/img/dc603f912adf94a33749155c69ddddd2/24.png)
**配置信息说明：**
 - 主机：云服务器的公网 IP（登录 [云服务器控制台](https://console.cloud.tencent.com/cvm) 页面即可查看对应云服务器的公网 IP）。
 - 用户名：在步骤一中设置的 FTP 用户的账号。图中以 “ftpuser1” 为例。
 - 密码：在步骤一中设置的 FTP 用户账号对应的密码。
 - 端口：FTP 监听端口，默认为 **21**。

3. 上传文件到 Linux 云服务器
上传文件时，鼠标选中本地文件，拖拽到远程站点，即可将文件上传到 Linux 云服务器。
![](//mccdn.qcloud.com/img56b05a11b4b80.png)
>**注意：**
>云服务器 FTP 通道不支持上传 tar 压缩包后自动解压，以及删除 tar 包功能。




		   