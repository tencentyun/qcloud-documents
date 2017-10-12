## 功能说明
COS FTP Server 工具是依赖 COS V4 的 FTP 服务端工具。使用 FTP Server 工具可以通过 FTP 协议从 COS 上传和下载文件。
### 实现机制
#### 上传机制
上传先落地 FTP 的本地磁盘, 上传 COS 后删除，返回给客户端成功（后期版本流式上传 COS，不落本地磁盘）。
#### 下载机制
下载直接流式返回给客户端
### 支持的 FTP 命令
<table>
    <tr>
        <th>put</th> 
        <th>get</th> 
				<th>mput</th> 
        <th>mget</th> 
				<th>delete</th> 
        <th>mkdir</th> 
				<th>ls</th> 
        <th>cd </th> 
				<th>bye</th> 
        <th>quit</th>
				<th>size</th>
   </tr>
</table>

> <font color="#0000cc">**注意：** </font>
暂不支持 append、rename 等命令。

## 使用限制
适用于 COS V4 版本
## 使用环境
### 系统环境
Linux 系统 (推荐腾讯云 CentOS 系列 CVM)
### 依赖库
针对 CentOS 等使用 yum 安装的系统，build.sh 会自动下载以下依赖。其他系统请自行安装。
```
cmake
boost
openssl-devel
asio-devel
libidn-devel
```
## 使用方法
### 获取程序包
GitHub 下载地址：[FTP Server 工具](https://github.com/tencentyun/cos_ftp_v4)
### 源码结构
| 目录       | 说明                            |
| -------- | ----------------------------- |
| bin      | 编译后生成的可执行程序                   |
| conf     | 配置文件目录                        |
| data     | 上传时存储临时数据的目录，上传成功或失败后删除       |
| dep      | FTP Server 所依赖的 COS V4 CPP SDK |
| include  | 头文件所在的目录                      |
| lib      | 依赖的库目录                        |
| log      | 日志目录                          |
| opbin    | 有关清理日志, 自动拉起的脚本               |
| src      | FTP 源码目录                       |
| build.sh | 编译脚本                          |
| start.sh | 启动 FTP Server 的脚本               |
| stop.sh  | 停止程序的脚本                       |
### 配置
配置文件`conf/vsftpd.conf`中的是 vsftpd 的相关配置,可以参考以下配置说明：
1. COS 账户信息配置。
```
cos_appid=1000000000                                                   
cos_secretid=xxxxxxxxxxxxxxxxxxxxxxxxx                              
cos_secretkey=xxxxxxxxxxxxxxxxxx
// 设置 APPID、API 密钥信息。                                                   
cos_bucket=test                                                     
cos_region=gz     
// bucket 信息，包括 bucket 的名字，以及 bucket 所在的区域。所在地域枚举值为 [可用地域](https://cloud.tencent.com/document/product/436/6224) 中适用于 JSON API 的地域简称，如 sh, gz, sgp 等。
cos_download_domain=cos    
// domain 设置为 cos 表示通过 COS 源站下载(推荐服务器为腾讯云机器用户设置)。
// domain 设置为 cdn 表示通过 CDN 下载(推荐服务器为非腾讯云机器用户设置)。
cos_user_home_dir=/home/test/cosftp_data/                                                  
// 此项不用设置, build.sh 脚本会自动设置。                                           
```
2. FTP 账户配置。配置格式为“用户名:密码:读写权限”，多个账户用分号分割，示例如下：
```
login_users=user1:pass1:RW;user2:pass2:RW 
```
3. 控制端口与数据端口设置，可使用默认设置。建议端口在 1025 ~ 65535，并保证未被防火墙 iptables 过滤。
```
listen_port=2121
```

### 编译
> <font color="#0000cc">**注意：** </font>
>  FTP 需要使用本地磁盘，因此请将 FTP 源码程序放在一个存储空间较大的盘。腾讯云初始的机器购买的数据盘需要手动格式化并挂载，请参考 [分区与格式化数据盘](/doc/product/213/2936#.E6.AD.A5.E9.AA.A4.E5.9B.9B.EF.BC.9A.E5.88.86.E5.8C.BA.E4.B8.8E.E6.A0.BC.E5.BC.8F.E5.8C.96.E6.95.B0.E6.8D.AE.E7.9B.98)。

以 root 身份运行 build.sh 脚本。build.sh 会调用 yum 自动安装依赖库，推荐使用腾讯云主流的 CentOS 系列系统。如果是其他系列系统，如 Ubuntu，请修改`opbin/env_init.sh`。

### 运行
1. 切换到 cos_ftp 账户（该账户是在 build.sh 脚本里建立的）。
```
su cos_ftp
```
2. 启动 FTP 进程和 monitor 程序，以及安装自动清理日志的 CT 脚本。
```
sh start.sh 
```
3. 使用 FTP 客户端连接 Server 的控制端口（默认是 2121），为避免客户机限制端口，建议使用 pasv 模式连接。推荐先用服务器本机的 FTP 命令`FTP 127.0.0.1 2121 `进行测试（此客户端程序可通过`yum install ftp`安装）。
4. 执行 FTP 的上传下载等命令。

### 停止
```
sh  stop.sh
```
## 问题与帮助
### 常见问题
#### 连接不上 FTP Server，如何处理？
请检查账户密码端口号，连接模式是否正确，以及服务器上进程是否已启动（netstat -tulnp | grep vsftpd）。
#### 为什么并发上传文件，只能成功上传一个文件？
FTP 不支持并发上传文件，会对文件进行加锁，导致只有一个会成功。
#### 上传文件过大，本地磁盘不足导致失败，如何处理？
通过 FTP 上传会先临时存放在 FTP 服务器磁盘（存放在 FTP 服务的 data 目录下），然后上传至 COS，上传成功后会删除本地文件。下载不存放本地，不受磁盘空间限制，因此建议把 FTP 服务部署在空间较大的分区上。
#### 为什么使用 FileZilla 等客户端上传大文件会失败？
当前版本的 FTP Server 工具不支持 append 模式，而 FileZilla 等客户端在上传一些大文件时，会通过 append 操作。
### 其他错误
请 [提交工单](https://console.cloud.tencent.com/workorder/category)，腾讯云技术支持将协助您解决问题。
