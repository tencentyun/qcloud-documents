COS FTP V4 用于通过FTP协议往COS上传和下载文件.

## 功能说明

COS FTP v4是依赖COS 4.X的FTP服务端工具。通过COS FTP工具可以通过FTP协议从COS上传和下载文件。

**上传机制**：上传先落地FTP的本地磁盘, 上传COS后删除，返回给客户端成功。（后期版本流式上传COS，不落本地磁盘）

**下载机制**：下载直接流式返回给客户端

## 支持FTP命令

- put
- get
- mput
- mget
- delete
- mkdir
- ls
- cd
- bye
- quit
- size

## 不支持FTP命令

- append



## 适用COS版本 

4.x

### 系统要求

Linux (推荐腾讯云Centos系列CVM)

### 依赖库

针对Centos等使用yum安装的系统，build.sh会自动下载以下依赖。其他系统请自行安装。

```
cmake
boost
openssl-devel
asio-devel
libidn-devel
```

## 使用方法

### 获取程序包

下载地址：[COS FTP V4 github](https://github.com/tencentyun/cos_ftp_v4)

### 源码结构

|    目录    |              说明               |
| :------: | :---------------------------: |
|   bin    |          编译后生成的可执行程序          |
|   conf   |            配置文件目录             |
|   data   |    上传时存储临时数据的目录，上传成功或失败后删除    |
|   dep    | FTP Server所依赖的COS 4.X CPP SDK |
| include  |           头文件所在的目录            |
|   lib    |            依赖的库目录             |
|   log    |             日志目录              |
|  opbin   |        有关清理日志, 自动拉起的脚本        |
|   src    |            FTP源码目录            |
| build.sh |             编译脚本              |
| start.sh |        启动FTP server的脚本        |
| stop.sh  |            停止程序的脚本            |

### 配置

配置文件conf/vsftpd.conf中的是vsftpd的相关配置,可以参考以下配置说明

```ini
1. COS账户信息配置
    #cos, set your app info in cos                                                   
    cos_appid=1000000                                                   
    cos_secretid=xxxxxxxxxxxxxxxxxxxxxxxxx                              
    cos_secretkey=xxxxxxxxxxxxxxxxxx 
    # bucket信息，包括bucket的名字，以及bucket所在的区域。目前有效值华南广州(gz), 华东上海(sh), 华北天津(tj)
    cos_bucket=test                                                     
    cos_region=gz
    # domain设置为cos表示通过cos源站下载(推荐服务器为腾讯云机器用户设置)
    # domain设置为cdn表示通过cdn下载(推荐服务器为非腾讯云机器用户设置)
    cos_download_domain=cos                                             
    # 此项不用设置, build.sh脚本会自动设置
    cos_user_home_dir=/home/test/cosftp_data/                                        

2. FTP账户配置(格式-用户名:密码:读写权限. 多个账户用分号分割)
    login_users=user1:pass1:RW;user2:pass2:RW  
    
3. 外网IP设置, 把外网IP设置服务器的外网IP(仅针对通过外网IP访问FTP服务的用户，如客户机和FTP服务器均在腾讯云CVM机器上，通过内网IP访问，则不用设置)
	pasv_address=115.115.115.115
	
4. 控制端口与数据端口设置, 可以使用默认设置(建议端口在1025 ~ 65535， 并保证未被防火墙iptables过滤)
	listen_port=2121
```
## 编译

1. 因为FTP需要使用本地磁盘，因此请将FTP源码程序放在一个存储空间较大的盘。(腾讯云初始的机器购买的数据盘需要手动格式化并挂载, 请参考 [https://www.qcloud.com/doc/product/213/2974](https://www.qcloud.com/doc/product/213/2974)
2. 以**root 身份运行build.sh**(因为build.sh里会调用yum进行安装依赖库，推荐使用腾讯云主流的Centos系列系统，如果是其他系列系统，如ubuntu，请修改opbin/env_init.sh )

## 运行

```
1. 切换到cos_ftp账户(这个账户是在build.sh脚本里建立的), su cos_ftp
2. sh start.sh (会启动FTP进程和monitor程序,以及安装自动清理日志的CT脚本)
3. 使用FTP客户端连接server的控制端口(默认是2121)，为避免客户机限制端口，建议使用pasv模式连接。
可以先用服务器本机的FTP命令进行测试(此客户端程序可通过yum install ftp安装)。 通过执行FTP 127.0.0.1 2121来测试。
4. 执行FTP的上传下载等命令
```

## 停止

```
sh  stop.sh
```

##  常见问题

```
1. 连接不上，请查看账户密码端口号，连接模式是否正确，以及服务器上进程是否起来(netstat -tulnp | grep vsftpd)
2. 并发上传一个文件失败，FTP不支持并发上传文件，会对文件进行加锁，导致只有一个会成功。
3. 上传文件过大，本地磁盘不足导致失败。通过FTP上传会先临时落FTP服务器磁盘(存放在FTP服务的data目录下)，然后上传COS，上传成功后会删除本地文件。下载不落本地，不受磁盘空间限制，因此建议把FTP服务部署在空间较大的分区上。
4. 使用FileZilla等客户端上传大文件失败, 第一版本的FTP服务器不支持append模式，而FileZilla等客户端在上传一些大文件时，会通过append操作。
5. 其他问题，请提供log目录的压缩包。
```

 

 
