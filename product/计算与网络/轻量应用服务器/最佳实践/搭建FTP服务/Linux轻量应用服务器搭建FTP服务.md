## 操作场景
Vsftpd（very secure FTP daemon）是众多 Linux 发行版中默认的 FTP 服务器。本文以 CentOS 7.6 64位操作系统的轻量应用服务器为例，使用 vsftpd 软件搭建 Linux 轻量应用服务器的 FTP 服务。

## 示例软件版本
本文搭建 FTP 服务组成版本如下：
- Linux 操作系统：本文以系统镜像 CentOS 7.6 为例。
- Vsftpd：本文以 vsftpd 3.0.2 为例。


## 操作步骤
### 步骤1：登录轻量应用服务器
您可以 [使用 WebShell 方式登录 Linux 实例](https://cloud.tencent.com/document/product/1207/44642)。也可以根据实际操作习惯，选择其他不同的登录方式，详情请参见 [登录 Linux 实例](https://cloud.tencent.com/document/product/1207/44609)。


### 步骤2：安装 vsftpd
1. 执行以下命令，安装 vsftpd。
```
sudo yum install -y vsftpd
```
2. 执行以下命令，设置 vsftpd 开机自启动。
```
sudo systemctl enable vsftpd
```
3. 执行以下命令，启动 FTP 服务。
```
sudo systemctl start vsftpd
```
4. 执行以下命令，确认服务是否启动。
```
sudo netstat -antup | grep ftp
```
显示结果如下，则说明 FTP 服务已成功启动。
![](https://main.qcloudimg.com/raw/86f1992cc036513bc475c859cca90663.png)
此时，vsftpd 已默认开启匿名访问模式，无需通过用户名和密码即可登录 FTP 服务器。使用此方式登录 FTP 服务器的用户没有权修改或上传文件的权限。


### 步骤3：配置 vsftpd[](id:user)
1. 执行以下命令，为 FTP 服务创建用户，本文以 ftpuser 为例。
```
sudo useradd ftpuser
```
2. 执行以下命令，设置 ftpuser 用户的密码。
```
sudo passwd ftpuser
```
输入密码后请按 **Enter** 确认设置，密码默认不显示。
3. 执行以下命令，创建 FTP 服务使用的文件目录，本文以 `/var/ftp/test` 为例。
```
sudo mkdir /var/ftp/test
```
4. 执行以下命令，修改目录权限。
```
sudo chown -R ftpuser:ftpuser /var/ftp/test
```
5. 执行以下命令，打开 `vsftpd.conf` 文件。
```
sudo vim /etc/vsftpd/vsftpd.conf
```
6. 按 **i** 切换至编辑模式，根据实际需求选择 FTP 模式，修改配置文件 `vsftpd.conf`：[](id:config)
<dx-alert infotype="notice" title="">
FTP 可通过主动模式和被动模式与客户端机器进行连接并传输数据。由于大多数客户端机器的防火墙设置及无法获取真实 IP 等原因，建议您选择**被动模式**搭建 FTP 服务。如下修改以设置被动模式为例，您如需选择主动模式，请前往 [设置 FTP 主动模式](#port)。
</dx-alert>
 1. 修改以下配置参数，设置匿名用户和本地用户的登录权限，设置指定例外用户列表文件的路径，并开启监听 IPv4 sockets。
```
anonymous_enable=NO
local_enable=YES
chroot_local_user=YES
chroot_list_enable=YES
chroot_list_file=/etc/vsftpd/chroot_list
listen=YES
```
  2. 在行首添加 `#`，注释 `listen_ipv6=YES` 配置参数，关闭监听 IPv6 sockets。
```
#listen_ipv6=YES
```
  3.  添加以下配置参数，开启被动模式，设置本地用户登录后所在目录，以及云服务器建立数据传输可使用的端口范围值。
```
local_root=/var/ftp/test
allow_writeable_chroot=YES
pasv_enable=YES
pasv_address=xxx.xx.xxx.xx #请修改为您的轻量应用服务器公网 IP
pasv_min_port=40000
pasv_max_port=45000
```
7. 按 **Esc** 后输入 **:wq** 保存后退出。
8. 执行以下命令，创建并编辑 `chroot_list` 文件。<span id="create"></span>
```
sudo vim /etc/vsftpd/chroot_list
```
9. 按 **i** 进入编辑模式，输入用户名，一个用户名占据一行，设置完成后按 **Esc** 并输入 **:wq** 保存后退出。
您若没有设置例外用户的需求，可跳过此步骤，输入 **:wq** 退出文件。
10. 执行以下命令，重启 FTP 服务。
```
sudo systemctl restart vsftpd
```

### 步骤4：设置安全组
搭建好 FTP 服务后，您需要根据实际使用的 FTP 模式给 Linux 轻量应用服务器放通对应端口，详情请参见 [添加防火墙规则](https://cloud.tencent.com/document/product/1207/44577#.E6.B7.BB.E5.8A.A0.E9.98.B2.E7.81.AB.E5.A2.99.E8.A7.84.E5.88.99)。
大多数客户端机器在局域网中，IP 地址是经过转换的。如果您选择了 FTP 主动模式，请确保客户端机器已获取真实的 IP 地址，否则可能会导致客户端无法登录 FTP 服务器。
- 主动模式：放通端口21。
- 被动模式：放通端口21，及 [修改配置文件](#config) 中设置的 `pasv_min_port` 到 `pasv_max_port` 之间的所有端口，本文放通端口为40000 - 45000。

### 步骤5：验证 FTP 服务
您可通过 FTP 客户端软件、浏览器或文件资源管理器等工具验证 FTP 服务，本文以客户端的文件资源管理器为例。
1. 打开客户端的 IE 浏览器，选择**工具** > **Internet 选项** > **高级**，根据您选择的 FTP 模式进行修改：
 - 主动模式：取消勾选“使用被动 FTP”。
 - 被动模式：勾选“使用被动 FTP”。
2. 打开客户端的计算机，在路径栏中访问以下地址。如下图所示：
```
ftp://轻量应用服务器公网IP:21
```
![](https://main.qcloudimg.com/raw/01154cd3f3af8c0578e588c29a574216.png)
3. 在弹出的“登录身份”窗口中输入 [配置 vsftpd](#user) 中已设置的用户名及密码。
4. 成功登录后，即可上传及下载文件。


## 附录
### 设置 FTP 主动模式[](id:port)
主动模式需修改的配置如下，其余配置保持默认设置：
```
anonymous_enable=NO      #禁止匿名用户登录
local_enable=YES         #支持本地用户登录
chroot_local_user=YES    #全部用户被限制在主目录
chroot_list_enable=YES   #启用例外用户名单
chroot_list_file=/etc/vsftpd/chroot_list  #指定用户列表文件，该列表中的用户不被锁定在主目录
listen=YES               #监听IPv4 sockets
#在行首添加#注释掉以下参数
#listen_ipv6=YES         #关闭监听IPv6 sockets
#添加下列参数
allow_writeable_chroot=YES
local_root=/var/ftp/test #设置本地用户登录后所在的目录
```
按 **Esc** 后输入 **:wq** 保存后退出，并前往 [步骤8](#create) 完成 vsftpd 配置。

### FTP 客户端上传文件失败
#### 问题描述
Linux 系统环境下，通过 vsftp 上传文件时，提示如下报错信息。
```
553 Could not create file
```

#### 解决方法
1. 执行以下命令，检查服务器磁盘空间的使用率。
```
df -h
```
 - 如果磁盘空间不足，将会导致文件无法上传，建议删除磁盘容量较大的文件。
 - 如果磁盘空间正常，请执行下一步。
2. 执行以下命令，检查 FTP 目录是否有写的权限。
```
ls -l /home/test      
# /home/test 为 FTP 目录，请修改为您实际的 FTP 目录。
```
 - 若返回结果中没有 `w`，则表示该用户没有写的权限，请执行下一步。
 - 若返回结果中已有 `w`，请前往 [在线支持](https://cloud.tencent.com/online-service?from=doc_1207) 进行反馈。
3. 执行以下命令，对 FTP 目录加上写的权限。
```
sudo chmod +w /home/test 
# /home/test 为 FTP 目录，请修改为您实际的 FTP 目录。
```
4. 执行以下命令，重新检查写的权限是否设置成功。
```
ls -l /home/test   
# /home/test 为 FTP 目录，请修改为您实际的 FTP 目录。
``` 

