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
><pre><code class="language-shell">chmod 600 /tmp/passwd-sts</code></pre>
>
步骤二：执行 COSFS 命令，使用命令选项 -ocam_role=[role] 指定角色为 sts、-opasswd_file=[path] 指定密钥文件路径，示例如下：
```shell
cosfs examplebucket-1250000000 /mnt/cosfs -ourl=http://cos.ap-guangzhou.myqcloud.com -odbglevel=info -oallow_other -ocam_role=sts -opasswd_file=/tmp/passwd-sts
```

### 如何查看 COSFS 提供的挂载参数选项和版本号？

使用`cosfs --help`命令，可以查看 COSFS 提供的参数选项；使用`cosfs --version` 命令，可以查看 COSFS 版本号。

### 如何查看 COSFS 所产生的日志？

在 CentOS 中，COSFS 产生的日志存储在 /var/log/messages 中；在 Ubuntu 中，COSFS 日志存储在 /var/log/syslog 中。如果您在使用过程中出现问题，请将对应时间段的该日志发送给我们。

### 如何挂载 Bucket 下的一个目录？

您在执行挂载命令的时候，可以指定 Bucket 下的一个目录，命令如下：
```shell
cosfs examplebucket-1250000000:/my-dir /mnt/cosfs -ourl=http://cos.ap-guangzhou.myqcloud.com -odbglevel=info
```
>! my-dir 必须以 `/` 开头。
>
如使用 v1.0.5之前版本，则挂载命令为：
```shell
cosfs 1250000000:examplebucket:/my-dir /mnt/cosfs -ourl=http://cos.ap-guangzhou.myqcloud.com -odbglevel=info
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
cosfs#examplebucket-1250000000 /mnt/cosfs fuse _netdev,allow_other,url=http://cos.ap-guangzhou.myqcloud.com,dbglevel=info
```

### 如何挂载多个存储桶？

您如有多个 Bucket 需要同时挂载，可以在 /etc/passwd-cosfs 配置文件中，为每一个需要挂载的 Bucket 写一行。每一行的内容形式，与单个 Bucket 挂载信息相同，例如：

```shell
echo examplebucket-1250000000:AKIDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX:GYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY >> /etc/passwd-cosfs
echo log-1250000000:AKIDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX:GYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY >> /etc/passwd-cosfs
```

### 挂载后，如何能让机器上其他账户来访问已挂载的目录？

如果要开放权限，需要在挂载的时候，指定`-oallow_other`。

### 在 COSFS 挂载目录中，对创建的文件名称有什么限制吗？

在 COSFS 挂载目录中，您能创建除`/`字符以外名称的文件。在类 Unix 系统上，`/`字符为目录分隔符，因此您无法在 COSFS 挂载目录中，创建包含`/`字符的文件。此外在创建包含特殊字符的文件时，您还需要避免特殊字符被 shell 使用，而导致创建文件失败。

### COSFS 如何判断文件是否存在？

在 COSFS 内部逻辑中，会以 Head 请求去判断父目录和文件是否存在。


### COSFS 如何查看已使用的存储容量？
COSFS 不支持直接查看已使用的存储容量。如果您想要统计 COS 存储桶的存储量，对于数据量较小的场景，请登录 COS 控制台进行查看；对于数据量大的场景，请使用 [清单](https://cloud.tencent.com/document/product/436/33703) 功能。



## 故障排查

### 使用 COSFS 过程中，突然显示 "unable to access MOUNTPOINT /path/to/mountpoint: Transport endpoint is not connected"，并且无法再访问？

您可以使用 `ps ax|grep cosfs` 命令查看 COSFS 进程是否存在，如果 COSFS 进程是由于误操作而挂掉，您可以执行如下命令进行重新挂载：

```shell
umount -l /path/to/mnt_dir
cosfs examplebucket-1250000000:/my-dir /mnt/cosfs -ourl=http://cos.ap-guangzhou.myqcloud.com -odbglevel=info
```

如果 COSFS 进程不是由于误操作挂掉，可以检查机器上的 fuse 版本是否低于 2.9.4，libfuse 在低于 2.9.4 版本的情况下可能会导致 COSFS 进程异常退出。此时，建议您参见 [COSFS 工具](https://cloud.tencent.com/document/product/436/6883#.E5.AE.89.E8.A3.85.E5.92.8C.E4.BD.BF.E7.94.A8) 文档更新 fuse 版本或安装最新版本的 COSFS。

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
3. 如果您使用 cp 命令进行拷贝，并且携带了 -p 或 -a 参数，建议您去掉该参数后执行该命令。

确认以上配置正确，请打开机器 `/var/log/messages` 日志文件，找到 s3fs 相关的日志，日志可以帮助您定位问题原因。如果无法解决，请 [联系我们](https://cloud.tencent.com/document/product/436/37708)，协助您解决问题。

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

### 在系统日志 /var/log/messages 中，看到大量404错误码，正常吗？
COSFS 内部逻辑中，会 Head 请求去判断父目录和文件是否存在，出现404并不意味着程序运行出错。

### 为什么在 COS 上看到的文件大小为0？
一般情况下，往 COSFS 中写入数据时，会首先在 COS 上创建一个0大小的文件，并将数据写入本地缓存文件。
在写入的过程中，该挂载点 ls 命令的结果会显示文件大小的变化。当关闭文件时，COSFS 会把写入到本地缓存文件中的数据上传到 COS 中。如果上传失败，您可能只能看到一个0大小的文件，该情况下可尝试重新拷贝失败的文件。

### COSFS 缓存目录中的文件和 COS 上的文件是否一致，可以直接使用吗？
不可以直接使用，缓存目录中的文件为 COSFS 内部加速读写所用，可能只存在 COS 上文件的一部分。

### 使用 rsync 命令拷贝一个文件到 COSFS 中，进度已经显示100%，但是服务器上只看到一个临时文件，这是怎么回事？
rsync 命令会在挂载目录中，创建一个临时文件，进度显示100%只表示该临时文件在本地写入100%，临时文件写入完毕后，还会将其上传到 COS 中，并进行重命名拷贝操作。
通常，往 COSFS 挂载目录中拷贝数据，使用 rsync 命令会比 cp 命令耗费更多时间。

### COSFS 将磁盘空间写满了，该如何处理？
COSFS 的上传下载都会使用磁盘文件缓存，当上传下载大文件时，若不指定 -oensure_diskfree=[size] 参数，会写满缓存文件所在的磁盘。您可以通过 -oensure_diskfree 参数指定，当缓存文件所在磁盘剩余空间不足 [size] MB 大小时，COSFS 将尽量减少使用磁盘空间（单位： MB）。 如果指定 -ouse_cache=[path] 参数，缓存文件位于 path 目录下，否则，在 /tmp 目录下。

示例：指定剩余磁盘空间少于10GB时，COSFS 运行减少使用磁盘空间，命令如下。
```shell
cosfs examplebucket-1250000000 /mnt/cosfs -ourl=http://cos.ap-guangzhou.myqcloud.com -odbglevel=info -oensure_diskfree=10240
```

### 使用 docker 挂载 COSFS 时，报错显示：fuse: failed to open /dev/fuse: Operation not permitted，该如何处理？
启动 docker 镜像时，您需要添加参数 --privileged。

### 是否可以使用某一个目录，作为多个挂载点的共用缓存目录？
不建议多个挂载点共用缓存目录，缓存目录中包含 COSFS 使用的元信息，共用可能会导致 COSFS 使用的元信息混乱。

### 使用 COSFS 挂载时出现报错 /bin/mount:unrecognized option --no-canonicalize，该如何处理？

较低版本的 mount 不支持 `--no-canonicalize` 选项，请更新 mount 工具（推荐版本为 v2.17，[前往下载](https://cdn.kernel.org/pub//linux/utils/util-linux/v2.17/)），更新后重新挂载。安装命令如下。

```shell
tar -jxvf util-linux-ng-2.17.tar.bz2
cd util-linux-ng-2.17
./configure --prefix=/usr/local/util-linux-ng
make && make install
mv /bin/mount{,.off}
ln -s /usr/local/util-linux-ng/bin/mount /bin
```

### 挂载失败该如何处理？

步骤一：根据日志文件和提示信息，检查挂载命令、密钥配置文件内容是否正确，以及网络是否可以访问 COS 服务。

步骤二：使用 date 命令，检查机器时间是否正确，如果不正确 ，用 date 命令修正时间后，重新挂载。例如：`date -s '2014-12-25 12:34:56'`。

### 使用 `ls -l --time-style=long-iso` 命令，挂载目录的时间变为1970-01-01 08:00，是否正常？

挂载目录时间变为1970-01-01 08:00是正常的，当您卸载挂载点后，挂载目录的时间会恢复为挂载前的时间。

 ### 挂载目录能否为非空？

可以使用`-ononempty`参数挂载到非空目录，但不建议您挂载到非空目录，当挂载点中和原目录中存在相同路径的文件时，可能出现问题。

### 在 COSFS 的目录中执行 ls 命令，为什么命令返回需要很久的时间？
在挂载目录中有很多文件的情况下，执行 ls 命令需要对目录中的每一个文件执行 HEAD 操作，因此，会耗费较多时间读取目录系统调用才会返回。
>! 建议您不要开启 IO hung，导致不必要的重启。
>


### 使用 info 级别的日志，生成的系统日志文件，占用大量存储空间，该怎么处理？
您可以定期清理生成的系统日志文件，或者调高日志级别，例如使用`-odbglevel=crit`挂载。


### COSFS 适用于哪些场景，读取和写入性能如何？
COSFS 读取和写入都经过磁盘中转，适用于要求 POSIX 语义访问 COS 的场景，例如共享数据集的机器学习算法读取共享数据，简单的日志备份等。COSFS 会使用多线程并发上传、下载进行加速，同地域走内网顺序读取一个6GB的文件，约耗时80s左右。顺序写入一个6GB的文件，约耗时160s左右。通常，您可通过 SDK 和多线程等技术，实现更好的性能。

>! 文件读写产生的大量系统调用，伴随着大量的日志，会在一定程度影响 COSFS 读写性能，如果您对性能有较高要求，您可以指定 -odbglevel=warn 或更高的日志级别。
>

### 安装 COSFS RPM 包后，提示找不到 COSFS，怎么办？

cosfs 安装路径为/usr/local/bin，如果提示找不到 cosfs，则可能是因为该路径不在 PATH 环境变量中，需先在 `~/.bashrc` 中添加一行配置：
```shell
export PATH=/usr/local/bin:$PATH
```
再执行命令：
```shell
source ~/.bashrc
```

### 安装 COSFS RPM 包时，提示 conflicts with file from package fuse-libs-\*，怎么办？

安装 COSFS RPM 包时，增加选项`--force`：
```shell
rpm -ivh cosfs-1.0.19-centos7.0.x86_64.rpm --force
```

###  COSFS 授权某个目录只读之后，单独挂载对应的目录提示无权限？

COSFS 需要有根目录的 GetBucket 权限，因此您需要加上根目录的 GetBucket 权限以及对应目录的读权限授权，这样可以列出其它目录但是没有操作权限。


### 为什么执行 df 显示 COSFS 的 Size 和 Available 为256T？
COS 存储桶的空间是无限大的，这里的 Available 为256T，仅作为展示 df 结果，实际上 COS 存储桶能存储的数据量远不止256T。

### 为什么执行 df 显示 COSFS 的 Used 为0？
COSFS 不占用本地存储空间，为了兼容 df 等工具，COSFS 显示的 Size Used Avaliable 都不是真实值。

### 为什么执行 df -i 显示 Inode/IUsed/IFree 都为0？
COSFS 不是基于硬盘的文件系统，所以不会有 inode。

### SUSE 12 SP3安装依赖包报"No provider of xxx found."错误，怎么办？
请参考 [SUSE系统无法安装COSFS的解决方案](https://cloud.tencent.com/developer/article/1868019)。

