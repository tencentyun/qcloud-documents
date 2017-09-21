本文档介绍在 Linux 云服务器上搭建 FTP 服务的操作。本例使用 CentOS 7.2 64 位系统进行示例，使用 vsftpd 作为 FTP 服务端，FileZilla 作为客户端。

## 步骤一：安装 vsftpd
 1. 登录云服务器。
 
 2. 安装软件。输入命令：` yum install vsftpd -y `
 
 3. 界面出现“ Complete ! ”，表示已安装完成。

## 步骤二：启动 vsftpd 服务
 1. 启动服务。输入命令：`serverice vsftpd start`

 2. 命令确认是否启动。输入命令：`netstat -tunlp`，出现图中展示内容即表示已经启动。
![](//mc.qcloudimg.com/static/img/6cc74de5689106ce763be98bfe7f5d24/image.png)

 3. 公网访问确认是否启动。在其他联网计算机上，通过命令行：`telnet + 云服务器公网 IP + 21`进行测试。出现下图内容即表示已经启动。
![](//mc.qcloudimg.com/static/img/9707535a7b6b7df1989d41576c50e20a/image.png)

<span id = "jump">  </span>
## 步骤三：编辑 vsftpd 配置文件
 1. 在云服务器中，输入命令：`vi /etc/vsftpd/vsftpd.conf`
 
 2. 编辑内容，状态更改为不允许匿名登录。按下键盘【a】开启编辑，将文件中的`anonymous_enable=YES`改为 `anonymous_enable=NO` ，修改完成后按下键盘【Esc】，任意位置输入`：write`保存修改，输入`：quit`退出编辑。
 ![](//mc.qcloudimg.com/static/img/4e7770981eae42e7b16a2a5a7866a6a6/image.png)

## 步骤四：添加 FTP 用户
 1. 添加用户。本例添加名为 ftpuser1 的用户。输入命令：` useradd -m -d /home/ftpuser1 -s /sbin/nologin ftpuser1 `

 2. 设置用户登录密码。本例为 ftpuser1 用户设置登录密码。输入命令：`passwd ftpuser1`，输入密码并确认即可。
![](//mc.qcloudimg.com/static/img/f8912544914d11dfc1dd7e0a6db16f11/image.png)

## 常见问题
### 问题描述
部分用户在本地使用 FTP 客户端连接时可能遇到连接超时和读取目录列表失败的问题。如下图所示。
![](//mc.qcloudimg.com/static/img/eb7beaf8c5a6e683257e94dd754e3f25/image.jpg)
问题出现在 PASV 命令处。原因在于 FTP 协议在腾讯云网络架构上的不适。FTP 客户端默认被动模式传输，因此在通信过程中会去寻找服务器端的 IP 地址进行连接，但是由于腾讯云的外网 IP 不是直接配在网卡上，因此在被动模式下客户端无法找到有效 IP （只能找到云服务器内网 IP ，内网 IP 无法直接和外网通信），故无法建立连接。

### 解决途径
 - 将客户端传输模式改为主动即可；
 - 如果客户端网络环境要求被动模式，那么需要在服务端 [步骤三](#jump) 中配置文件中新增这些语句：
 ```
 pasv_address=XXX.XXX.XXX.XXX     //(外网 IP)
 pasv_enable=YES
 pasv_min_port=1024
 pasv_max_port=2048
 ```