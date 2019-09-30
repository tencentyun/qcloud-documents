## 功能概述

COS FTP Server 支持通过 FTP 协议直接操作 COS 中的对象和目录，包括上传文件、下载文件、删除文件以及创建文件夹等。FTP Server 工具使用 Python 实现，使安装更加简单。

## 功能说明

**上传机制**：流式上传，不落本地磁盘，只要按照标准的 FTP 协议配置工作目录即可，不占用实际的磁盘存储空间。
**下载机制**：直接流式返回给客户端
**目录机制**：bucket 作为整个 FTP Server 的根目录，bucket 下面可以建立若干个子目录。
**多 bucket 绑定**：支持同时绑定多个 bucket。
>?多 bucket 绑定：通过不同的 FTP Server 工作路径（home_dir）来实现，因此，指定不同的 bucket 和用户信息时必须保证 home_dir 不同。

**删除操作限制**：在新的 FTP Server 中可以针对每个 ftp 用户配置 delete_enable 选项，以标识是否允许该 FTP 用户删除文件。
**支持的 FTP 命令：**put、mput、get、rename、delete、mkdir、ls、cd、bye、quite、size。
**不支持的 FTP 命令：**append、mget （不支持原生的 mget 命令，但在某些 Windows 客户端下，仍然可以批量下载，例如 FileZilla 客户端。）

>?FTP Server 工具暂时不支持断点续传功能。

## 开始使用

#### 系统环境

- 操作系统：Linux，推荐使用腾讯 CentOS 系列 [云服务器](https://cloud.tencent.com/document/product/213)，暂时不支持 Windows 系统。
- Python 解释器版本：Python 2.7，请参见 [Python 安装与配置](https://cloud.tencent.com/document/product/436/10866) 进行安装与配置。
- 依赖包：
 - [cos-python-sdk-v5](https://pypi.org/project/cos-python-sdk-v5/) （≥1.6.5）
 - [pyftpdlib](https://pypi.org/project/pyftpdlib/) （≥1.5.2）


#### 使用限制

适用于 COS XML 版本。

#### 安装运行

FTP Server 工具下载地址为：[cos-ftp-server](https://github.com/tencentyun/cos-ftp-server-V5)。安装步骤如下：

1. 进入 FTP Server 目录，运行 setup.py 安装 FTP Server 及其相关的依赖库（需要联网）：
```bash
python setup.py install   # 这里可能需要您的账号 sudo 或者拥有 root 权限。
```
2. 将配置示例文件`conf/vsftpd.conf.example`复制命名为`conf/vsftpd.conf`，参考本文 [配置文件](#conf) 章节 ，正确配置 bucket 和用户信息。
3. 运行 ftp_server.py 启动 FTP Server：
```bash
python ftp_server.py
```
此外还有两种方式启动 FTP Server，如下：
 - 使用 nohup 命令，以后台进程方式启动：
```bash
nohup python ftp_server.py >> /dev/null 2>&1 &
```
 - 使用 screen 命令放入后台运行（需要安装 screen 工具)：
```bash
screen -dmS ftp
screen -r ftp
python ftp_server.py
#使用快捷键，切回主 screen 即可：
Ctrl+A+D 
```

#### 停止运行

- 若您是直接运行，或 screen 方式放在后台运行的 FTP Server，您可以使用快捷键`Ctrl+C`停止 FTP Server 运行。 
- 若您是通过 nohup 命令启动，可以使用下面方式停止：
```bash
ps -ef | grep python | grep ftp_server.py | grep -v grep | awk '{print $2}' | xargs -I{} kill {}
```


<a id="conf"></a>
## 配置文件

FTP Server 工具的配置示例文件为`conf/vsftpd.conf.example`，请复制命名为 vsftpd.conf，并按照以下的配置项进行配置：
```conf
[COS_ACCOUNT_0]
cos_secretid = COS_SECRETID    # 替换为您的 SECRETID
cos_secretkey = COS_SECRETKEY  # 替换为您的 SECRETKEY
cos_bucket = examplebucket-1250000000
cos_region = region   # 替换为您的存储桶地域
cos_protocol = https
#cos_endpoint = region.myqcloud.com
home_dir = /home/user0
ftp_login_user_name=user0
ftp_login_user_password=pass0
authority=RW
delete_enable=true					# true 为允许该 ftp 用户进行删除操作(默认)，false 为禁止该用户进行删除操作

[COS_ACCOUNT_1]
cos_secretid = COS_SECRETID    # 替换为您的 SECRETID
cos_secretkey = COS_SECRETKEY  # 替换为您的 SECRETKEY
cos_bucket = examplebucket-1250000000
cos_region = region   # 替换为您的存储桶地域
cos_protocol = https
#cos_endpoint = region.myqcloud.com
home_dir = /home/user1
ftp_login_user_name=user1
ftp_login_user_password=pass1
authority=RW
delete_enable=false

[NETWORK]
masquerade_address = XXX.XXX.XXX.XXX        # 如果 FTP SERVER 处于某个网关或NAT后，可以通过该配置项将网关的IP 地址或域名指定给 FTP
listen_port = 2121					   # Ftp Server的监听端口，默认为2121，注意防火墙需要放行该端口

passive_port = 60000,65535             # passive_port 可以设置 passive 模式下，端口的选择范围，默认在(60000, 65535)区间上选择

[FILE_OPTION]
# 默认单文件大小最大支持到200G，不建议设置太大
single_file_max_size = 21474836480

[OPTIONAL]
# 以下设置，如无特殊需要，建议保留 default 设置  如需设置，请合理填写一个整数
min_part_size       = default
upload_thread_num   = default
max_connection_num  = 512
max_list_file       = 10000                # ls命令最大可列出的文件数目，建议不要设置太大，否则ls命令延时会很高
log_level           = INFO                 # 设置日志输出的级别
log_dir             = log                  # 设置日志的存放目录，默认是在ftp server目录下的log目录中
```


>?
>- 如果要将每个用户绑定到不同的 bucket 上，则只需要添加 [COS_ACCOUNT_X] 的 section 即可。
针对每个不同的 COS_ACCOUNT_X 的 section 有如下说明：
 - 每个 ACCOUNT 下的用户名（ftp_login_user_name）和用户的主目录（home_dir）必须各不相同，并且主目录必须是系统中真实存在的目录。
 - 每个 COS FTP Server 允许同时登录的用户数目不能超过100。
 - endpoint 和 region 不会同时生效，使用公有云 COS 服务只需要正确填写 region 字段即可，endpoint 常用于私有化部署环境中。当同时填写了 region 和 endpoint，则会 endpoint 会优先生效。
>- 配置文件中的 OPTIONAL 选项是提供给高级用户用于调整上传性能的可选项，根据机器的性能合理地调整上传分片的大小和并发上传的线程数，可以获得更好的上传速度，一般用户不需要调整，保持默认值即可。
同时，提供最大连接数的限制选项。 这里如果不想限制最大连接数，可以填写0，即表示不限制最大连接数目（不过需要根据您机器的性能合理评估）。


## 常见问题
如您在使用 FTP Server 工具过程中，有报错或对上传限制有疑问，请参见 [FTP Server 工具](https://cloud.tencent.com/document/product/436/30742) 常见问题。
