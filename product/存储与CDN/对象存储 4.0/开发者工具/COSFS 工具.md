## 功能说明 
COSFS 工具支持将 COS 存储桶挂载到本地，像使用本地文件系统一样直接操作腾讯云对象存储中的对象， COSFS 提供的主要功能包括：
- 支持 POSIX 文件系统的大部分功能，如：文件读写、目录操作、链接操作、权限管理、uid/gid 管理等功能。
- 大文件分块传输功能。
- MD5 数据校验功能。

## 安装和使用 
### 适用操作系统版本 
主流的 Ubuntu、CentOS、MacOS 系统。

### 安装流程

#### 1. 获取源码 
您首先需要从 GitHub 上将 [COSFS 源码](https://github.com/tencentyun/cosfs) 下载到指定目录，下面以目录 `/usr/cosfs` 为例：
```shell
git clone https://github.com/tencentyun/cosfs /usr/cosfs
```

#### 2. 安装依赖软件 
COSFS 的编译安装依赖于 automake、git、libcurl-devel、libxml2-devel、fuse-devel、make、openssl-devel 等软件包，Ubuntu 、CentOS 和 MacOS 的依赖软件安装过程如下：

- Ubuntu 系统下安装依赖软件：

```shell
sudo apt-get install automake autotools-dev g++ git libcurl4-gnutls-dev libfuse-dev libssl-dev libxml2-dev make pkg-config fuse
```

- CentOS 系统下安装依赖软件：

```shell
sudo yum install automake gcc-c++ git libcurl-devel libxml2-devel fuse-devel make openssl-devel fuse
```

- MacOS 系统下安装依赖软件：

```shell
brew install automake git curl libxml2 make pkg-config openssl 
brew cask install osxfuse
```
<a id="compile"> </a>
#### 3. 编译和安装 COSFS 
进入安装目录，执行如下命令进行编译和安装：
```shell
cd /usr/cosfs
./autogen.sh
./configure
make
sudo make install
cosfs --version
```

根据操作系统的不同，进行 configure 操作时会出现不同的提示，主要分为以下方面：
- 在 CentOS 6.5 及更低版本的操作系统进行 configure 操作时，可能会因 fuse 版本太低而出现如下提示：
```
checking for common_lib_checking... configure: error: Package requirements (fuse >= 2.8.4 libcurl >= 7.0 libxml-2.0 >= 2.6) were not met:
  Requested 'fuse >= 2.8.4' but version of fuse is 2.8.3 
```
此时，您需要手动安装 fuse 2.8.4 及以上版本，安装命令示例如下：
```shell
yum -y remove fuse-devel
wget https://github.com/libfuse/libfuse/releases/download/fuse_2_9_4/fuse-2.9.4.tar.gz
tar -zxvf fuse-2.9.4.tar.gz
cd fuse-2.9.4
./configure
make
make install
export PKG_CONFIG_PATH=/usr/lib/pkgconfig:/usr/lib64/pkgconfig/:/usr/local/lib/pkgconfig
modprobe fuse
echo "/usr/local/lib" >> /etc/ld.so.conf
ldconfig
pkg-config --modversion fuse 
#当您看到 “2.9.4” 时，表示fuse安装成功  
```

- 在 MacOS 进行 configure 操作时，可能会出现如下提示：
```shell
configure: error: Package requirements (fuse >= 2.7.3 libcurl >= 7.0 libxml-2.0 >2.6 libcrypto >= 0.9) were not met
No package 'libcrypto' found
```
此时，您需要设置 PKG_CONFIG_PATH 变量，以使得 pkg-config 工具能找到 openssl，命令如下：
```shell
brew info openssl 
export PKG_CONFIG_PATH=/usr/local/opt/openssl/lib/pkgconfig #您可能需要根据上一条命令的提示信息修改这条命令
```

### COSFS 使用方法

#### 1. 配置密钥文件
在文件 /etc/passwd-cosfs 中，写入您的存储桶名称 &lt;Name&gt;-&lt;Appid&gt;，以及该存储桶对应的 &lt;SecretId&gt; 和 &lt;SecretKey&gt;，三项之间使用半角冒号隔开， 并为密钥文件设置权限 640。命令如下：
```shell
echo <Name>-<Appid>:<SecretId>:<SecretKey> > /etc/passwd-cosfs
chmod 640 /etc/passwd-cosfs
```
>**注意：**
>您需要将 &lt;Name&gt;、&lt;Appid&gt;、&lt;SecretId&gt; 和 &lt;SecretKey&gt; 替换为您的信息。 在 test-1253972369 这个 Bucket 中，&lt;Name&gt; 为 test， &lt;Appid&gt; 为 1253972369， Bucket 命名规范，请参见 [存储桶命名规范](https://cloud.tencent.com/document/product/436/13312)。&lt;SecretId&gt; 和 &lt;SecretKey&gt; 请前往访问管理控制台的 [云 API 密钥管理](https://console.cloud.tencent.com/cam/capi) 中获取。

**示例：**

```shell
echo test-123456789:AKID8ILGzYjHMG8zhGtnlX7Vi4KOGxRqg1aa:LWVJqIagbFm8IG4sNlrkeSn5DLI3dCYi > /etc/passwd-cosfs
chmod 640 /etc/passwd-cosfs
```

#### 2. 运行工具
将已经在密钥文件中配置好信息的存储桶挂载到指定目录，可以使用如下命令行：

```shell
cosfs <Name>-<Appid> <MountPoint> -ourl=<CosDomainName> -odbglevel=info
```
其中：
- &lt;MountPoint&gt; 为本地挂载目录（如 /mnt）。
- &lt;CosDomainName&gt; 为存储桶对应的访问域名，形式为 `http://cos.<Region>.myqcloud.com` （适用于XML API），其中&lt;Region&gt; 为地域简称， 如： ap-guangzhou 、 eu-frankfurt 等。更多地域信息，请查阅 [可用地域](https://cloud.tencent.com/document/product/436/6224)。
- -odbglevel 指定日志级别。

**示例：**

```shell
mkdir /mnt
cosfs test-1253972369 /mnt -ourl=http://cos.ap-guangzhou.myqcloud.com -odbglevel=info -onoxattr
```
>**注意：** 
>v1.0.5 之前版本 COSFS 的挂载命令如下：
```shell
cosfs <Appid>:<Name> <MountPoint> -ourl=<CosDomainName>
```
v1.0.5 之前版本 COSFS 的配置文件格式是：
```shell
<Name>:<SecretId>:<SecretKey>
```

#### 3. 卸载存储桶

卸载存储桶示例：

```shell
fusermount -u /mnt 或者 umount -l /mnt
```

## 常用挂载选项

### 1. -omultipart_size=[size]
用来指定分块上传时单个分块的大小（单位： MB），默认是 10 MB。 由于分块上传对单个文件块的数目有最大限制（10000 块），所以对于超出 10 MB * 10000 (100 GB) 大小的文件，需要根据具体情况调整该参数。

### 2. -oallow_other
如果要允许其他用户访问挂载文件夹，可以在运行 cosfs 的时候指定该参数。

### 3. -odel_cache
默认情况下， COSFS 为了优化性能，在 umount 后，不会清除本地的缓存数据。 如果需要在 COSFS 退出时，自动清除缓存，可以在挂载时加入该选项。

### 4. -onoxattr
禁用 getattr/setxattr 功能， 当前版本的 COSFS 不支持该功能，如果在挂载的时候使用了 use_xattr 选项，可能会导致 mv 文件到 Bucket 失败。

### 5. -ouse_cache=[path]
使用缓存目录缓存文件，path 为本地缓存目录路径，该选项可以在文件缓存下来后，加速文件的读写（非第一次读写），如果不需要本地缓存或本地磁盘容量有限，可不指定该选项。

### 6. -opasswd_file=[path]
该选项可以指定 COSFS 密钥文件的所在路径，该选项设定的密钥文件需要设置权限为 600。

### 7. -odbglevel=[info|dbg]

设置 COSFS 日志记录级别，可选 info、dbg，生产环境中建议设置为 info，调试时可以设置为 dbg。

### 8. -oumask=[perm]

该选项可以去除给定类型用户，对挂载目录内文件的操作权限，例如-oumask=007，可以去除其他用户对文件的读写执行权限。

## 局限性
COSFS 提供的功能、性能和本地文件系统相比，存在一些局限性。例如：
- 随机或者追加写文件会导致整个文件的重写，您可以使用与 Bucket 在同一个园区的 CVM 加速文件的上传下载。
- 多个客户端挂载同一个 COS 存储桶时，依赖用户自行协调各个客户端的行为。例如避免多个客户端写同一个文件等。
- 不支持 hard link，不适合高并发读/写的场景。
- 不可以同时在一个挂载点上挂载、和卸载文件。您可以先 cd 切换到其他目录，再对挂载点进行挂载、卸载操作。

## 常见问题

### 1. 如何查看 COSFS 提供的挂载参数选项和版本号？
使用 cosfs --help 命令，可以查看 COSFS 提供的参数选项；使用 cosfs --version 命令，可以查看 COSFS 版本号。

### 2. 如何查看 COSFS 所产生的日志？
在 CentOS 中，COSFS 产生的日志存储在 /var/log/messages 中；在 Ubuntu 中，COSFS 日志存储在 /var/log/syslog 中。如果您在使用中有遇到问题，请将对应时间段的该日志发送给我们。

### 3.  使用 COSFS 过程中，突然显示 "unable to access MOUNTPOINT /path/to/mountpoint: Transport endpoint is not connected"，并且无法再访问?
您可以使用 `ps ax|grep cosfs` 命令查看 COSFS 进程是否存在，如果 COSFS 进程是由于误操作而挂掉，您可以执行如下命令进行重新挂载：
```shell
umount -l /path/to/mnt_dir
cosfs test-1253972369:/my-dir /tmp/cosfs -ourl=http://cos.ap-guangzhou.myqcloud.com -odbglevel=info -ouse_cache=/path/to/local_cache
```
如果 COSFS 进程不是由于误操作挂掉，可以检查机器上的 fuse 版本是否低于 2.9.4，libfuse 在低于 2.9.4 版本的情况下可能会导致 COSFS 进程异常退出。此时，建议您按照本文 [编译和安装 COSFS](#compile)  部分更新 fuse 版本或安装最新版本的 COSFS。

### 4. 如何挂载 Bucket 下的一个目录？
您在执行挂载命令的时候，可以指定 Bucket 下的一个目录，命令如下：
```shell
cosfs test-1253972369:/my-dir /tmp/cosfs -ourl=http://cos.ap-guangzhou.myqcloud.com -odbglevel=info -ouse_cache=/path/to/local_cache
```
>**注意：**
> my-dir 必须以 `/` 开头。

如使用 v1.0.5 之前版本，则挂载命令为：
```shell
cosfs 1253972369:test:/my-dir /tmp/cosfs -ourl=http://cos.ap-guangzhou.myqcloud.com -odbglevel=info -ouse_cache=/path/to/local_cache
```

### 5. 通过 COSFS 上传的文件 Content-Type 被变为 "application/octet-stream"？
COSFS 是根据 /etc/mime.types 和上传文件的后缀进行比对，自动设置上传到 COS 上文件的 Content-Type。出现 Content-Type 问题时，建议检查系统上是否存在该配置文件。对于 Ubuntu， 可以通过 sudo apt-get install mime-support 来添加。对于 CentOS，可以通过 sudo yum install mailcap 来添加。您也可以手动创建该文件，每种文件格式添加一行，例如：
```shell
image/jpeg                                      jpg jpeg
image/jpm                                       jpm jpgm
image/jpx                                       jpx jpf
```
### 6. 非 root 用户如何挂载 COSFS？
非 root 用户建议在个人 Home 目录下建立 .passwd-cosfs 文件，并且设置权限为 600，按照正常命令挂载即可，此外，可以通过 -opasswd_file=path 选项指定密钥文件的路径。

### 7. COSFS 是否支持 https 进行挂载?
COSFS 支持 https，http 和 https 的使用形式分别为：
```shell
-ourl=http://cos.ap-guangzhou.myqcloud.com
-ourl=https://cos.ap-guangzhou.myqcloud.com
```
在 libcurl 所依赖的 NSS 库为 3.12.3 及其以上版本的系统（ 使用 `curl -V` 命令查看 NSS 版本），使用 https 方式挂载 Bucket，需要执行如下命令：
```shell
echo "export NSS_STRICT_NOFORK=DISABLED" >> ~/.bashrc
source ~/.bashrc
```
### 8. 挂载时显示 Bucket not exist?
请检查参数 -ourl，确保 url 中不要携带 Bucket 部分，正确的形式为：
```shell
-ourl=http://cos.ap-guangzhou.myqcloud.com
```

### 9. 如何设定 COSFS 开机自动挂载?
在 /etc/fstab 文件中添加如下的内容，其中，_netdev 选项使得网络准备好后再执行当前命令：
```shell
cosfs#test-1253972369 /mnt/cosfs-remote fuse _netdev,allow_other,url=http：//cos.ap-guangzhou.myqcloud.com,dbglevel=info
```

### 10. 为什么之前可用写文件，突然不能写了?
由于 COS 鉴权产品策略调整，所以使用 V1.0.0 之前版本的 COSFS 工具会导致策略校验不通过，您可以安装最新的 COSFS 工具重新挂载。

### 11. 如何挂载多个存储桶?

您如有多个 Bucket 需要同时挂载，可以在 /etc/passwd-cosfs 配置文件中，为每一个需要挂载的 Bucket 写一行。每一行的内容形式，与单个 Bucket 挂载信息相同，例如：

```shell
echo data-123456789:AKID8ILGzYjHMG8zhGtnlX7Vi4KOGxRqg1aa:LWVJqIagbFm8IG4sNlrkeSn5DLI3dCYi >> /etc/passwd-cosfs
echo log-123456789:AKID8ILGzYjHMG8zhGtnlX7Vi4KOGxRqg1aa:LWVJqIagbFm8IG4sNlrkeSn5DLI3dCYi >> /etc/passwd-cosfs
```

### 12. 使用 /etc/fstab 设定 COSFS 开机自动挂载，但是执行 mount -a, 却报错 "wrong fs type, bad option, bad superblock on cosfs"?
由于您的机器上缺乏 fuse 库，导致报此错误。建议您执行下列命令安装 fuse 库：
```shell
sudo yum install fuse #CentOS
sudo apt-get install fuse #Ubuntu
```
