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

## 使用环境 

### 使用系统

Linux (推荐腾讯云Centos系列CVM)

### 依赖库

针对Centos等使用yum安装的系统，build.sh会自动下载以下依赖。其他系统请自行安装。

1 cmake

2 boost

2 openssl-devel

3 asio-devel

4 libidn-devel

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

### 编译

1. 因为FTP需要使用本地磁盘，因此请将FTP源码程序放在一个存储空间较大的盘。(腾讯云初始的机器购买的数据盘需要手动格式化并挂载, 请参考 [https://www.qcloud.com/doc/product/213/2974](https://www.qcloud.com/doc/product/213/2974)
2. 以root 身份运行build.sh(因为build.sh里会调用yum进行安装依赖库，推荐使用腾讯云主流的Centos系列系统，如果是其他系列系统，如ubuntu，请修改opbin/env_init.sh )

### 配置

配置文件conf/vsftd.conf中的是vsftpd的配置,可以参考以下配置说明, 需要改动的主要是以下两模块

1. COS账户信息配置

   ```ini
   #cos, set your app info in cos                                                   
   cos_appid=1000000                                                                
   cos_secretid=xxxxxxxxxxxxxxxxxxxxxxxxx                                           
   cos_secretkey=xxxxxxxxxxxxxxxxxx 
   # bucket信息，包括bucket的名字，以及bucket所在的区域。目前有效值华南广州(gz), 华东上海(sh), 华北天津(tj)
   cos_bucket=test                                                                  
   cos_region=gz                                                                                                                                    
   cos_download_domain=cos                                                          
   cos_user_home_dir=/home/test/cosftp_data/                                        
   ```


2. 设置FTP账户

   ```ini
   login_users=user:pass:RW
   ```

### 运行

1. 切换到非root身份(目前以root身份运行会存在一些问题),  编译过程会自动建立一个cos_ftp用户, 因此可以直接使用该用户,通过root切到cos_ftp. (su cos_ftp)
2. sh start.sh (会启动FTP进程和monitor程序,以及安装自动清理日志的脚本)
3. 可使用FTP客户端连接server，进行文件的上传与下载

### 停止

运行 sh  stop.sh

 

 

 
