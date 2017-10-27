COS FTP Server 工具支持通过 FTP 协议直接操作 COS 中的对象和目录，包括上传文件、下载文件、删除文件以及创建文件夹等。FTP Server 工具使用 Python 实现，使安装更加简单。
## 使用环境
### 系统环境
操作系统：Linux，推荐使用腾讯云 CentOS 7 系列 CVM，暂不支持 Windows 系统。

Python 解释器版本：Python 2.7，可参考 [Python 安装与配置](/doc/product/436/10866) 进行安装与配置。

依赖库：
- cos-python-sdk-v5（included），requests（not included），argparse（not included）
- pyftpdlib(included)

### 下载与安装
GitHub 链接：[COS FTP Server 工具](https://github.com/tencentyun/cos-ftp-server-V5)。

下载完成后，直接运行`cos ftp server`目录下的`setup.py`即可，需要联网安装依赖库。
```
python setup.py install   # 这里可能需要sudo或者root权限
```

### 使用限制
适用于 COS V5 版本 XML 接口

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
cos_appid = 12XXXXXX
# 用户自己的 APPID
cos_secretid = XXXXXX
cos_secretkey = XXXXXX
# SecretId 和 SecretKey 可以在以下地址获取：https://console.cloud.tencent.com/cam/capi
cos_bucket = XXXXX
# 要操作的 Bucket 名称，需要注意的是 COS V5 控制台上的 Bucket 采用了 <Bucket>-<APPID> 的命名方式，这里只填写 Bucket 即可。
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
passive_ports = 60000,65535             # #passive_port可以设置passive模式下，端口的选择范围，默认在(60000, 65535)区间上选择

[FILE_OPTION]
single_file_max_size = 21474836480
# 默认单文件大小最大支持到 200 GB，不建议设置太大。
```
## 运行
正确填写配置文件后，直接通过 Python 运行根目录下的`ftp_server.py`即可启动 FTP Server。也可以配合screen 的命令将 FTP Server 放到后台运行。
```
python ftp_server.py
```
## 停止
`Ctrl + C`即可取消 FTP Server 运行（直接运行，或 screen 方式放在后台运行）。
## FAQ
#### 上传大文件的时候，中途取消，为什么 COS 上会留有已上传的文件？
由于适用于 COS V5 版本的 FTP Server 提供了完全的流式上传特性，用户文件上传的取消或断开，都会触发大文件的上传完成操作。因此，COS 会认为用户数据流已经上传完成，并将已经上传的数据组成一个完整的文件。 如果用户希望重新上传，可以直接以原文件名上传覆盖；也可手动删除不完整的文件，重新上传。

#### 为什么 FTP Server 配置中要设置最大上传文件的限制？
COS 的分片上传数目最大只能为 10000 块，且每个分片的大小限制为 1 MB ~ 5 G。 这里设置最大上传文件的限制是为了合理计算一个上传分片的大小。
FTP Server 默认支持 200 GB 以内的单文件上传，但是不建议用户设置过大，因为单文件大小设置越大，上传时的分片缓冲区也会相应的增大，这可能会耗费用户的内存资源。因此，建议用户根据自己的实际情况，合理设置单文件的大小限制。

#### 如果上传的文件超过最大限制，会怎么样？
当实际上传的单文件大小超过了配置文件中的限制，系统会返回一个 IOError 的异常，并且在日志中标注错误信息。

#### 其他问题，请 [提交工单](https://console.cloud.tencent.com/workorder/category)，并在工单上附上完整的`cos_v5.log`日志，便于我们进一步排查和解决问题。
