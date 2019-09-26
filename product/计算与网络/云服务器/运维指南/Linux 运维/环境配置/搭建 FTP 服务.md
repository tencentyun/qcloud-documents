## 操作场景
本文以 CentOS 7.2 64位系统为例，使用 vsftpd 作为 FTP 服务端，FileZilla 作为客户端。指导您如何在 Linux 云服务器上搭建 FTP 服务。

## 操作步骤
### 安装 vsftpd
1. 登录 Linux 云服务器。
2. 执行以下命令，安装 vsftpd。
``` 
yum install vsftpd -y
```

### 启动服务
1. 执行以下命令，启动服务。
```
systemctl start vsftpd
```
2. 执行以下命令，确认服务是否启动。
```
netstat -tunlp
```
返回类似如下信息，则表示 vsftpd 服务已经启动成功。
![](//mc.qcloudimg.com/static/img/6cc74de5689106ce763be98bfe7f5d24/image.png)

### （可选）验证 vsftpd 服务
>? 为了保证 FTP 服务端顺利完成配置，您还可以在本地计算机或其他云服务器上执行以下操作步骤，再次验证 vsftpd 服务是否启动成功。以下操作步骤以 Linux 操作系统的本地计算机为例。如果本地计算机为 Windows/Mac OS 操作系统，请确保该计算机已开启 telnet 功能。
>
1. 在本地计算机的操作系统界面，执行以下命令，安装 telnet 服务。
>? 如果您的本地计算机为 Windows/Mac OS 操作系统，请跳过此步骤。
>
```
yum -y install  telnet
```
3. 执行以下命令，测试 vsftpd 服务是否启动成功。
```
telnet + 云服务器公网 IP + 21
```
返回类似如下信息，即表示已经启动成功。
![](https://main.qcloudimg.com/raw/47ad66d7be133b6d69d60c3e5b719dbd.png)

<span id = "jump">  </span>

### 配置 vsftpd
1. 执行以下命令，打开 vsftpd 配置文件。
```
vi /etc/vsftpd/vsftpd.conf
```
2. 按 “**i**” 或 “**Insert**” 切换至编辑模式，将文件中的`anonymous_enable=YES`改为`anonymous_enable=NO`。如下图所示：
![](//mc.qcloudimg.com/static/img/4e7770981eae42e7b16a2a5a7866a6a6/image.png)
3. 按 “**Esc**”，输入 “**:wq**”，保存文件并返回。

### 添加 FTP 用户
1. 执行以下命令，添加用户`ftpuser1`。
``` 
useradd -m -d /home/ftpuser1 -s /sbin/nologin ftpuser1
```
2. 执行以下命令，设置用户`ftpuser1`的密码。
```
passwd ftpuser1
```
创建用户、用户密码设置成功。如下图所示：
![](https://main.qcloudimg.com/raw/eec9ba9d188bf8b82a846fed73e02b52.png)

## 常见问题
### FTP 客户端连接超时或者读取目录列表失败
#### 问题描述
部分用户在本地使用 FTP 客户端连接时可能遇到连接超时和读取目录列表失败的问题。如下图所示：
![](//mc.qcloudimg.com/static/img/eb7beaf8c5a6e683257e94dd754e3f25/image.jpg)
问题出现在 PASV 命令处。原因在于 FTP 协议在腾讯云网络架构上的不适。FTP 客户端默认被动模式传输，因此在通信过程中会去寻找服务器端的 IP 地址进行连接，但是由于腾讯云的公网 IP 不是直接配在网卡上，因此在被动模式下客户端无法找到有效 IP （只能找到云服务器内网 IP ，内网 IP 无法直接和公网通信），故无法建立连接。

#### 解决方法
1. 将客户端传输模式改为主动即可。
2. 如果客户端网络环境要求被动模式，那么需要在服务端 [配置 vsftpd](#jump) 中的配置文件中新增这些语句：
```
pasv_address=XXX.XXX.XXX.XXX     //(公网 IP)
pasv_enable=YES
pasv_min_port=1024
pasv_max_port=2048
```

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
 - 若返回结果中已有 `w`，请 [提交工单](https://console.cloud.tencent.com/workorder/category) 进行反馈。
3. 执行以下命令，对 FTP 目录加上写的权限。
```
chmod +w /home/test 
# /home/test 为 FTP 目录，请修改为您实际的 FTP 目录。
```
4. 执行以下命令，重新检查写的权限是否设置成功。
```
ls -l /home/test   
# /home/test 为 FTP 目录，请修改为您实际的 FTP 目录。
``` 




