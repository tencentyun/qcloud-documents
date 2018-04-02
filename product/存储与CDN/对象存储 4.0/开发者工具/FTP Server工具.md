COS FTP Server 工具支持通过 FTP 协议直接操作 COS 中的对象和目录，包括上传文件、下载文件、删除文件以及创建文件夹等。FTP Server 工具使用 Python 实现，使安装更加简单。
## 使用环境
### 系统环境
操作系统：Linux，推荐使用腾讯云 CentOS 7 系列 CVM，暂不支持 Windows 系统。

Python 解释器版本：Python 2.7，可参考 [Python 安装与配置](https://cloud.tencent.com/document/product/436/10866) 进行安装与配置。

依赖库：
- requests
- argparse

### 下载与安装
GitHub 链接：[COS FTP Server 工具](https://github.com/tencentyun/cos-ftp-server-V5)。

下载完成后，直接运行`cos ftp server`目录下的`setup.py`即可，需要联网安装依赖库。
```
python setup.py install   # 这里可能需要sudo或者root权限
```

### 特别说明
本工具使用 COS XML 接口开发

## 功能说明
#### 上传机制
流式上传，不落本地磁盘，只要按照标准的 FTP 协议配置工作目录即可，不占用实际的磁盘存储空间。

#### 下载机制
直接流式返回给客户端。

#### 目录机制
Bucket 作为整个 FTP Server 的根目录，Bucket 下面可以建立若干个子目录。

#### 说明
- 目前只支持操作一个 Bucket，后期可能会支持同时操作多个 Bucket。
- FTP Server 工具暂不支持断点续传功能。
- 不支持上传空文件（0B），支持的最大文件为 200 GB。

## 支持的 FTP 命令
- put
- mput
- get
- rename
- delete
- mkdir
- ls
- cd
- bye
- quite
- size

## 不支持的 FTP 命令
- append
- mget （不支持原生的 mget 命令，但在某些 Windows 客户端下，仍然可以批量下载，如 FileZilla。）


## 配置文件
`conf/vsftpd.conf`为 FTP Server 工具的配置文件，相关配置项的说明如下：
```conf
[COS_ACCOUNT]
cos_secretid = XXXXXX
cos_secretkey = XXXXXX
# SecretId 和 SecretKey 可以在以下地址获取：https://console.cloud.tencent.com/cam/capi
cos_bucket = BucketName-appid
# 要操作的bucket，bucket的格式为：bucektname-appid组成。示例：cos_bucket = mybucket-125888888888。
cos_region = ap-xxx
# Bucket 所在的地域，目前支持的地域请参照【可用地域-适用于 XML API 部分】：https://cloud.tencent.com/document/product/436/6224
cos_user_home_dir = /home/cos_ftp/data
# FTP Server 的工作目录。
[FTP_ACCOUNT]
login_users = user1:pass1:RW;user2:pass2:RW
# FTP 账户配置。配置格式为<用户名:密码:读写权限>，多个账户用分号分割。

[NETWORK]
masquerade_address = XXX.XXX.XXX.XXX
# 当 FTP Server 处于某个网关或 NAT 后时，可以通过该配置项将网关的 IP 地址或域名指定给 FTP Server。一般情况下，无需配置。
listen_port = 2121
# Ftp Server 的监听端口，默认为 2121，请注意防火墙需要放行该端口。
passive_ports = 60000,65535             
# passive_port 可以设置 passive 模式下，端口的选择范围，默认在(60000, 65535)区间上选择。

[FILE_OPTION]
single_file_max_size = 21474836480
# 默认单文件大小最大支持到 200 GB，不建议设置太大。

[OPTIONAL]
# 以下设置，如无特殊需要，建议保留default设置。如需设置，请填写一个合理的整数。
min_part_size       = default
upload_thread_num   = default
max_connection_num  = 512
max_list_file       = 10000                # ls命令最大可列出的文件数目，建议不要设置太大，否则ls命令延时会很高
log_level           = INFO                 # 设置日志输出的级别
log_dir             = log                  # 设置日志的存放目录，默认是在ftp server目录下的log目录中
```
配置中OPTIONAL选项是用于调整上传性能的可选项，一般情况下保持默认值即可。根据机器的性能合理地调整上传分片的大小和并发上传的线程数，可以获得更好的上传速度。 max_connection_num 为最大连接数的限制选项，设置为0表示不限制最大连接数，可以根据机器情况进行调整。 
## 运行
正确填写配置文件后，直接通过 Python 运行根目录下的`ftp_server.py`即可启动 FTP Server。也可以配合screen 的命令将 FTP Server 放到后台运行。
```
python ftp_server.py
```
运行命令后，见到如下图示，即代表 FTP Server 服务启动成功，您可以开始使用 FTP 客户端对配置的 IP 和端口进行访问了。
![运行成功](//mc.qcloudimg.com/static/img/7bbb20b2ba2c6cf9678a47d8753499cc/image.png)

## 停止
`Ctrl + C`即可取消 FTP Server 运行（直接运行，或 screen 方式放在后台运行）。
## FAQ

### 配置文件中的masquerade_address这个选项有何作用？何时需要配置masquerade_address
当FTP Server运行在一个多网卡的Server上，并且FTP Server采用了PASSIVE模式时（一般地，FTP客户端位于一个NAT网关之后时，都需要启用PASSIVE模式），此时需要使用masquerade_address选项来唯一绑定一个passive模式下用于reply的IP。 例如，FTP Server有多个IP地址，如内网IP为10.XXX.XXX.XXX，外网IP为123.XXX.XXX.XXX。 客户端通过外网IP连接到FTP Server，同时客户端使用的是PASSIVE模式传输，此时，若FTP Server未指定masquerade_address具体绑定到外网IP地址，则Server在PASSIVE模式下，reply时，有可能会走内网地址。就会出现客户端能连接上Ftp server，但是不能从Server端获取任何数据回复的问题。

如果需要配置masquerade_address，建议指定为客户端连接Server所使用的那个IP地址。

#### 上传大文件的时候，中途取消，为什么 COS 上会留有已上传的文件？
由于适用于 COS V5 版本的 FTP Server 提供了完全的流式上传特性，用户文件上传的取消或断开，都会触发大文件的上传完成操作。因此，COS 会认为用户数据流已经上传完成，并将已经上传的数据组成一个完整的文件。 如果用户希望重新上传，可以直接以原文件名上传覆盖；也可手动删除不完整的文件，重新上传。

#### 为什么 FTP Server 配置中要设置最大上传文件的限制？
COS 的分片上传数目最大只能为 10000 块，且每个分片的大小限制为 1 MB ~ 5 G。 这里设置最大上传文件的限制是为了合理计算一个上传分片的大小。
FTP Server 默认支持 200 GB 以内的单文件上传，但是不建议用户设置过大，因为单文件大小设置越大，上传时的分片缓冲区也会相应的增大，这可能会耗费用户的内存资源。因此，建议用户根据自己的实际情况，合理设置单文件的大小限制。

#### 如果上传的文件超过最大限制，会怎么样？
当实际上传的单文件大小超过了配置文件中的限制，系统会返回一个 IOError 的异常，并且在日志中标注错误信息。

#### 其他问题，请 [提交工单](https://console.cloud.tencent.com/workorder/category)，并在工单上附上完整的`cos_v5.log`日志，便于我们进一步排查和解决问题。
