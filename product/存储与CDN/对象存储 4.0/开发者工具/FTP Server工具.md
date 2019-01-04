COS FTP Server 支持通过FTP协议直接操作COS中的对象和目录，包括上传文件、下载文件、删除文件以及创建文件夹等。FTP Server 工具使用 Python 实现，使安装更加简单。

## 开始使用

### 系统环境

操作系统：Linux，推荐使用腾讯CentOS系列CVM，暂时不支持Windows系统

Python解释器版本：Python 2.7，可参考 [Python 安装与配置](https://cloud.tencent.com/document/product/436/10866) 进行安装与配置。

依赖包：

- cos-python-sdk-v5 (>=1.6.5)
- pyftpdlib (>=1.5.2)


### 使用限制

适用于COS XML版本


### 安装运行

首先，运行setup.py安装ftp server及其相关的依赖库（需要联网）：

```bash
python setup.py install   # 这里可能需要sudo或者root权限
```

然后，拷贝conf/vsftpd.conf.example 到 conf/vsftpd.conf，参考**配置文件**章节，正确配置bucket和用户信息；

最后，运行ftp_server.py启动cos-ftp-server：

```bash
python ftp_server.py
```

也可以使用nohup命令，以后台进程方式启动：

```bash
nohup python ftp_server.py >> /dev/null 2>&1 &
```

或使用screen命令放入后台运行(需要安装screen工具)：

```bash
screen -dmS ftp
screen -r ftp
python ftp_server.py

Ctrl+A+D 			# 切回主screen即可

```

### 停止

Ctrl + C 即可取消server运行（直接运行，或screen方式放在后台运行）

如果使用nohup启动，可以使用下面方式停止：

```bash
ps -ef | grep python | grep ftp_server.py | grep -v grep | awk '{print $2}' | xargs -I{} kill {}
```


## 功能说明

**上传机制**：流式上传，不落本地磁盘，只要按照标准的FTP协议配置工作目录即可，不占用实际的磁盘存储空间。

**下载机制**：直接流式返回给客户端

**目录机制**：bucket作为整个FTP SERVER的根目录，bucket下面可以建立若干个子目录。

**多bucket绑定<sup>*</sup>**：支持同时绑定多个bucket。

**删除操作限制**：在新的ftp-server中可以针对每个ftp用户配置`delete_enable`选项，以标识是否允许该ftp用户删除文件。


*：多bucket绑定是通过不同的ftp server工作路径（`home_dir`）来实现，因此，指定不同的bucket和用户信息时必须保证`home_dir`不同。


### 支持的FTP命令

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

### 不支持FTP命令

- append
- mget (不支持原生的mget命令，但在某些Windows客户端下，仍然可以批量下载，如FileZilla)

**说明**：Ftp Server工具暂时不支持断点续传功能


## 配置文件

conf/vsftpd.conf.example为Ftp Server工具的配置文件示例，请copy为vsftpd.conf，并按照以下的配置项进行配置：

``` conf
[COS_ACCOUNT_0]
cos_secretid = XXXXXX
cos_secretkey = XXXXXX
cos_bucket = {bucket name}-123
cos_region = ap-xxx
#cos_endpoint = ap-xxx.myqcloud.com
home_dir = /home/user0
ftp_login_user_name=user0
ftp_login_user_password=pass0
authority=RW
delete_enable=true					# true为允许该ftp用户进行删除操作(默认)，false为禁止该用户进行删除操作

[COS_ACCOUNT_1]
cos_secretid = XXXX
cos_secretkey = XXXXX
cos_bucket = {bucket name}-123
cos_region = ap-xxx
#cos_endpoint = ap-xxx.myqcloud.com
home_dir = /home/user1
ftp_login_user_name=user1
ftp_login_user_password=pass1
authority=RW
delete_enable=false

[NETWORK]
masquerade_address = XXX.XXX.XXX.XXX        # 如果FTP SERVER处于某个网关或NAT后，可以通过该配置项将网关的IP地址或域名指定给FTP
listen_port = 2121					   # Ftp Server的监听端口，默认为2121，注意防火墙需要放行该端口

passive_port = 60000,65535             # passive_port可以设置passive模式下，端口的选择范围，默认在(60000, 65535)区间上选择

[FILE_OPTION]
# 默认单文件大小最大支持到200G，不建议设置太大
single_file_max_size = 21474836480

[OPTIONAL]
# 以下设置，如无特殊需要，建议保留default设置  如需设置，请合理填写一个整数
min_part_size       = default
upload_thread_num   = default
max_connection_num  = 512
max_list_file       = 10000                # ls命令最大可列出的文件数目，建议不要设置太大，否则ls命令延时会很高
log_level           = INFO                 # 设置日志输出的级别
log_dir             = log                  # 设置日志的存放目录，默认是在ftp server目录下的log目录中

```

如果要将每个用户绑定到不同的bucket上，则只需要添加`[COS_ACCOUNT_X]`的section即可。

针对每个不同的`COS_ACCOUNT_X`的section有如下说明：

1. 每个ACCOUNT下的用户名（`ftp_login_user_name`）和用户的主目录（`home_dir`）必须各不相同，并且主目录必须是系统中真实存在的目录；
2. 每个COS FTP SERVER允许同时登录的用户数目不能超过100；
3. `endpoint`和`region`不会同时生效，使用公有云COS服务只需要正确填写`region`字段即可，`endpoint`常用于私有化部署环境中。当同时填写了`region`和`endpoint`，则会`endpoint`会优先生效。

配置文件中的OPTIONAL选项是提供给高级用户用于调整上传性能的可选项，根据机器的性能合理地调整上传分片的大小和并发上传的线程数，可以获得更好的上传速度，一般用户不需要调整，保持默认值即可。
同时，提供最大连接数的限制选项。 这里如果不想限制最大连接数，可以填写0，即表示不限制最大连接数目（不过需要根据您机器的性能合理评估）。


## 常见问题
如您在使用 FTP Server 工具过程中，有报错或对上传限制有疑问，请参阅 [FTP Server 工具类常见问题](https://cloud.tencent.com/document/product/436/30742)。
