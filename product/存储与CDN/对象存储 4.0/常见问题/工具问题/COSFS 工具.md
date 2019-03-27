## 功能咨询
### 如何使用临时密钥挂载存储桶？

使用临时密钥（STS）挂载存储桶，需要执行如下两个步骤：

步骤一：创建临时密钥配置文件，例如为 /tmp/passwd-sts，用于 COSFS 命令选项 -opasswd-file=\[path\] 指定密钥配置文件。临时密钥相关概念可参考  [临时密钥生成及使用指引](https://cloud.tencent.com/document/product/436/14048) 文档。临时密钥配置文件示例如下：

```shell
COSAccessKeyId=AKIDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX  #以下为临时密钥的Id、Key和Token字段
COSSecretKey=GYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
COSAccessToken=109dbb14ca0c30ef4b7e2fc9612f26788cadbfac3
COSAccessTokenExpire=2017-08-29T20:30:00  #临时token过期时间，为GMT时间，格式需和例子中一致
```
其中，COSFS 会根据 COSAccessTokenExpire 中配置的时间，来判断是否需要重新从密钥文件中加载配置。

>!为防止密钥泄露，COSFS 要求您将密钥文件的权限设置成600，执行命令如下：
>```shell
>chmod 600 /tmp/passwd-sts
>```

步骤二：执行 COSFS 命令，使用命令选项 -ocam_role=[role] 指定角色为 sts、-opasswd_file=[path] 指定密钥文件路径，示例如下：

```shell
cosfs example-1253972369 /mnt/cosfs -ourl=http://cos.ap-guangzhou.myqcloud.com -odbglevel=info -oallow_other -ocam_role=sts -opasswd_file=/tmp/passwd-sts
```

### 如何查看 COSFS 提供的挂载参数选项和版本号？

使用`cosfs --help`命令，可以查看 COSFS 提供的参数选项；使用`cosfs --version` 命令，可以查看 COSFS 版本号。

### 如何查看 COSFS 所产生的日志？

在 CentOS 中，COSFS 产生的日志存储在 /var/log/messages 中；在 Ubuntu 中，COSFS 日志存储在 /var/log/syslog 中。如果您在使用过程中出现问题，请将对应时间段的该日志发送给我们。

### 如何挂载 Bucket 下的一个目录？

您在执行挂载命令的时候，可以指定 Bucket 下的一个目录，命令如下：

```shell
cosfs example-1253972369:/my-dir /mnt/cosfs -ourl=http://cos.ap-guangzhou.myqcloud.com -odbglevel=info
```

>!my-dir 必须以 `/` 开头。

如使用 v1.0.5之前版本，则挂载命令为：

```shell
cosfs 1253972369:example:/my-dir /mnt/cosfs -ourl=http://cos.ap-guangzhou.myqcloud.com -odbglevel=info
```

### 非 root 用户如何挂载 COSFS？

非 root 用户建议在个人 Home 目录下建立 .passwd-cosfs 文件，并且设置权限为600，按照正常命令挂载即可。此外，可以通过 -opasswd_file=path 选项指定密钥文件的路径，并将权限设置为600。

### COSFS 是否支持 HTTPS 进行挂载？

COSFS 支持 HTTPS，HTTP 和 HTTPS 的使用形式分别为：

```shell
-ourl=http://cos.ap-guangzhou.myqcloud.com
-ourl=https://cos.ap-guangzhou.myqcloud.com
```

在 libcurl 所依赖的 NSS 库为 3.12.3及其以上版本的系统（ 使用 `curl -V` 命令查看 NSS 版本），使用 HTTPS 方式挂载 Bucket，需要执行如下命令：

```shell
echo "export NSS_STRICT_NOFORK=DISABLED" >> ~/.bashrc
source ~/.bashrc
```

### 如何设定 COSFS 开机自动挂载？

在 /etc/fstab 文件中添加如下的内容，其中，_netdev 选项使得网络准备好后再执行当前命令：

```shell
cosfs#example-1253972369 /mnt/cosfs fuse _netdev,allow_other,url=http://cos.ap-guangzhou.myqcloud.com,dbglevel=info
```

### 如何挂载多个存储桶？

您如有多个 Bucket 需要同时挂载，可以在 /etc/passwd-cosfs 配置文件中，为每一个需要挂载的 Bucket 写一行。每一行的内容形式，与单个 Bucket 挂载信息相同，例如：

```shell
echo example-123456789:AKIDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX:GYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY >> /etc/passwd-cosfs
echo log-123456789:AKIDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX:GYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY >> /etc/passwd-cosfs
```

### 挂载后，如何能让机器上其他账户来访问已挂载的目录？

如果要开放权限，需要在挂载的时候，指定`-oallow_other`。

### 在 COSFS 挂载目录中，对创建的文件名称有什么限制吗？

在 COSFS 挂载目录中，您能创建除`/`字符以外名称的文件。在类 Unix 系统上，`/`字符为目录分隔符，因此您无法在 COSFS 挂载目录中，创建包含`/`字符的文件。此外在创建包含特殊字符的文件时，您还需要避免特殊字符被 shell 使用，而导致创建文件失败。


## 故障排查

### 使用 COSFS 过程中，突然显示 "unable to access MOUNTPOINT /path/to/mountpoint: Transport endpoint is not connected"，并且无法再访问？

您可以使用 `ps ax|grep cosfs` 命令查看 COSFS 进程是否存在，如果 COSFS 进程是由于误操作而挂掉，您可以执行如下命令进行重新挂载：

```shell
umount -l /path/to/mnt_dir
cosfs example-1253972369:/my-dir /mnt/cosfs -ourl=http://cos.ap-guangzhou.myqcloud.com -odbglevel=info
```

如果 COSFS 进程不是由于误操作挂掉，可以检查机器上的 fuse 版本是否低于 2.9.4，libfuse 在低于 2.9.4 版本的情况下可能会导致 COSFS 进程异常退出。此时，建议您按照本文 [编译和安装 COSFS](https://cloud.tencent.com/document/product/436/6883#compile) 部分更新 fuse 版本或安装最新版本的 COSFS。

### 通过 COSFS 上传的文件 Content-Type 被变为 "application/octet-stream"怎么办？

COSFS 是根据 /etc/mime.types 和上传文件的后缀进行比对，自动设置上传到 COS 上文件的 Content-Type。出现 Content-Type 问题时，建议检查系统上是否存在该配置文件。对于 Ubuntu， 可以通过 sudo apt-get install mime-support 来添加。对于 CentOS，可以通过 sudo yum install mailcap 来添加。您也可以手动创建该文件，每种文件格式添加一行，例如：

```shell
image/jpeg                                      jpg jpeg
image/jpm                                       jpm jpgm
image/jpx                                       jpx jpf
```

### 挂载时显示 Bucket not exist？

请检查参数 -ourl，确保 URL 中不携带 Bucket 部分，正确的形式为：

```shell
-ourl=http://cos.ap-guangzhou.myqcloud.com
```

### 为什么之前可用写文件，突然不能写了？

由于 COS 鉴权产品策略调整，所以使用 V1.0.0 之前版本的 COSFS 工具会导致策略校验不通过，您可以安装最新的 COSFS 工具重新挂载。

### 使用 COSFS 工具过程中，遇到 Input/Output ERROR 等错误，该如何调试？

请先按照以下步骤依次检查，确认问题。

1. 请检查机器是否能正常访问 COS 的域名。
2. 检查账号是否配置正确。 

确认以上配置正确，请打开机器 `/var/log/messages` 日志文件，找到 s3fs 相关的日志，日志可以帮助您定位问题原因。如果无法解决，请 [提交工单](https://console.cloud.tencent.com/workorder/category) 联系腾讯云技术支持，协助您解决问题。

### 使用 /etc/fstab 设定 COSFS 开机自动挂载，但是执行 mount -a, 却报错 "wrong fs type, bad option，bad superblock on cosfs"？
该错误通常是由于您的机器上缺乏 fuse 库所致，建议您执行下列命令安装 fuse 库：
- CentOS
```shell
sudo yum install fuse
```
- Ubuntu
```shell
sudo apt-get install fuse
```
