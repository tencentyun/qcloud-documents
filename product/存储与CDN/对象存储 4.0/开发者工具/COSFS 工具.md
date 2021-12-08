## 功能说明 

COSFS 工具支持将对象存储（Cloud Object Storage，COS）存储桶挂载到本地，像使用本地文件系统一样直接操作腾讯云对象存储中的对象， COSFS 提供的主要功能包括：
- 支持 POSIX 文件系统的大部分功能，如：文件读写、目录操作、链接操作、权限管理、uid/gid 管理等功能。
- 大文件分块传输功能。
- MD5 数据校验功能。
- 将本机数据上传至 COS，建议使用 [COS Migration 工具](https://cloud.tencent.com/document/product/436/15392) 或 [COSCMD 工具](https://cloud.tencent.com/document/product/436/10976)。

## 局限性
**COSFS 基于 S3FS 构建， 读取和写入操作都经过磁盘中转，仅适合挂载后对文件进行简单的管理，不支持本地文件系统的一些功能用法，性能方面也无法代替云硬盘 CBS 或文件存储 CFS。** 需注意以下不适用的场景，例如：

- 随机或者追加写文件会导致整个文件的下载以及重新上传，您可以使用与 Bucket 在同一个地域的 CVM 加速文件的上传下载。
- 多个客户端挂载同一个 COS 存储桶时，依赖用户自行协调各个客户端的行为。例如避免多个客户端写同一个文件等。
- 文件/文件夹的 rename 操作不是原子的。
- 元数据操作，例如 list directory，性能较差，因为需要远程访问 COS 服务器。
- 不支持 hard link，不适合高并发读/写的场景。
- 不可以同时在一个挂载点上挂载、和卸载文件。您可以先使用 cd 命令切换到其他目录，再对挂载点进行挂载、卸载操作。

## 使用环境
支持主流的 Ubuntu、CentOS、SUSE、macOS 系统。


## 安装方式
COSFS 主要提供两种安装方式：通过安装包方式安装和通过编译源码方式安装。


### 方式一：通过安装包方式安装
>? 该方式支持主流的 Ubuntu、CentOS 系统。
>

#### Ubuntu 系统

1. 根据系统版本选择对应的安装包，目前支持的 Ubuntu 发行版包括 Ubuntu14.04、Ubuntu16.04、Ubuntu18.04、Ubuntu20.04。
```plaintext
#Ubuntu14.04
wget https://github.com/tencentyun/cosfs/releases/download/v1.0.19/cosfs_1.0.19-ubuntu14.04_amd64.deb
#Ubuntu16.04
wget https://github.com/tencentyun/cosfs/releases/download/v1.0.19/cosfs_1.0.19-ubuntu16.04_amd64.deb
#Ubuntu18.04
wget https://github.com/tencentyun/cosfs/releases/download/v1.0.19/cosfs_1.0.19-ubuntu18.04_amd64.deb
#Ubuntu20.04
wget https://github.com/tencentyun/cosfs/releases/download/v1.0.19/cosfs_1.0.19-ubuntu20.04_amd64.deb
```
2. 安装。以 Ubuntu16.04 为例：
```shell
sudo dpkg -i cosfs_1.0.19-ubuntu16.04_amd64.deb
```

#### CentOS 系统

1. 安装依赖
```plaintext
sudo yum install libxml2-devel libcurl-devel -y
```
2. 根据系统版本选择对应的安装包，目前支持的 CentOS 发行版包括 CentOS6.5、CentOS7.0。
```plaintext
#CentOS6.5
wget https://github.com/tencentyun/cosfs/releases/download/v1.0.19/cosfs-1.0.19-centos6.5.x86_64.rpm
#CentOS7.0
wget https://github.com/tencentyun/cosfs/releases/download/v1.0.19/cosfs-1.0.19-centos7.0.x86_64.rpm
```
3. 安装。以 CentOS7.0为例：
```shell
sudo rpm -ivh cosfs-1.0.19-centos7.0.x86_64.rpm
```
>? 如果安装时报错，提示`conflicts with file from package fuse-libs-*`，则加`--force`参数再次安装。
>

### 方式二：通过编译源码方式安装

>? 该方式支持主流的 Ubuntu、CentOS、SUSE、macOS 系统。
>


#### 1. 安装依赖软件 
COSFS 的编译安装依赖于 automake、git、libcurl-devel、libxml2-devel、fuse-devel、make、openssl-devel 等软件包，Ubuntu 、CentOS、SUSE 和 macOS 的依赖软件安装过程如下：

- Ubuntu 系统下安装依赖软件：
```shell
sudo apt-get install automake autotools-dev g++ git libcurl4-gnutls-dev libfuse-dev libssl-dev libxml2-dev make pkg-config fuse
```
- CentOS 系统下安装依赖软件：
```shell
sudo yum install automake gcc-c++ git libcurl-devel libxml2-devel fuse-devel make openssl-devel fuse
```
- SUSE 系统下安装依赖软件：
```shell
sudo zypper install gcc-c++ automake make libcurl-devel libxml2-devel openssl-devel pkg-config
```
- macOS 系统下安装依赖软件：
```shell
brew install automake git curl libxml2 make pkg-config openssl 
brew cask install osxfuse
```

#### 2. 获取源码 

您需要从 GitHub 上将 [COSFS 源码](https://github.com/tencentyun/cosfs) 下载到指定目录，下面以目录`/usr/cosfs`为例（实际操作下，建议您根据具体操作环境选择目录）：
```shell
git clone https://github.com/tencentyun/cosfs /usr/cosfs
```


#### 3. 编译和安装 COSFS 
进入安装目录，执行如下命令进行编译和安装：
```shell
cd /usr/cosfs
./autogen.sh
./configure
make
sudo make install
cosfs --version  #查看 cosfs 版本号
```

#### 4. Configure 操作问题处理

根据操作系统的不同，进行 configure 操作时会出现不同的提示，在 fuse 版本低于 2.8.4 的操作系统上，进行 configure 操作时会出现以下报错提示：
```shell
checking for common_lib_checking... configure: error: Package requirements (fuse >= 2.8.4 libcurl >= 7.0 libxml-2.0 >= 2.6) were not met:
  Requested 'fuse >= 2.8.4' but version of fuse is 2.8.3 
```
此时，您需要手动安装 fuse 2.8.4及以上版本，安装命令示例如下：
```shell
yum -y remove fuse-devel
wget https://github.com/libfuse/libfuse/releases/download/fuse_2_9_4/fuse-2.9.4.tar.gz
tar -zxvf fuse-2.9.4.tar.gz
cd fuse-2.9.4
./configure
make
make install
export PKG_CONFIG_PATH=/usr/lib/pkgconfig:/usr/lib64/pkgconfig/:/usr/local/lib/pkgconfig
modprobe fuse   #挂载 fuse 内核模块
echo "/usr/local/lib" >> /etc/ld.so.conf
ldconfig   #更新动态链接库
pkg-config --modversion fuse  #查看 fuse 版本号，当看到 “2.9.4” 时，表示 fuse 2.9.4 安装成功 
```
- SUSE 系统下手动安装 fuse 2.8.4及以上版本，安装命令示例如下：
>! 安装时，需要注释掉`example/fusexmp.c`文件下第222行内容，否则 make 将报错。注释方法为`/*content*/` 。
>
```shell
zypper remove fuse libfuse2
wget https://github.com/libfuse/libfuse/releases/download/fuse_2_9_4/fuse-2.9.4.tar.gz
tar -zxvf fuse-2.9.4.tar.gz
cd fuse-2.9.4
./configure
make 
make install
export PKG_CONFIG_PATH=/usr/lib/pkgconfig:/usr/lib64/pkgconfig/:/usr/local/lib/pkgconfig
modprobe fuse   #挂载 fuse 内核模块
echo "/usr/local/lib" >> /etc/ld.so.conf
ldconfig   #更新动态链接库
pkg-config --modversion fuse   #查看 fuse 版本号，当看到 “2.9.4” 时，表示 fuse2.9.4 安装成功 
```
- 在 macOS 进行 configure 操作时，可能会出现如下提示：
```shell
configure: error: Package requirements (fuse >= 2.7.3 libcurl >= 7.0 libxml-2.0 >2.6 libcrypto >= 0.9) were not met
No package 'libcrypto' found
```
 此时，您需要设置 PKG_CONFIG_PATH 变量，以使得 pkg-config 工具能找到 openssl，命令如下：
```shell
brew info openssl 
export PKG_CONFIG_PATH=/usr/local/opt/openssl/lib/pkgconfig #您可能需要根据上一条命令的提示信息修改这条命令
```


## 使用方法

### 1. 配置密钥文件
在文件`/etc/passwd-cosfs`中，写入您的存储桶名称（格式为 BucketName-APPID），以及该存储桶对应的 &lt;SecretId&gt; 和 &lt;SecretKey&gt;，三项之间使用半角冒号隔开。为了防止密钥泄露，COSFS 要求您将密钥文件的权限值设置为640，配置`/etc/passwd-cosfs`密钥文件的命令格式如下：
```shell
sudo su  # 切换到 root 身份，以修改 /etc/passwd-cosfs 文件；如果已经为 root 用户，无需执行该条命令。
echo <BucketName-APPID>:<SecretId>:<SecretKey> > /etc/passwd-cosfs
chmod 640 /etc/passwd-cosfs
```

>? 您需要将 &lt;&gt; 的参数替换为您的信息。
> - &lt;BucketName-APPID&gt;为存储桶名称格式，关于存储桶命名规范，请参见 [存储桶命名规范](https://cloud.tencent.com/document/product/436/13312#.E5.AD.98.E5.82.A8.E6.A1.B6.E5.91.BD.E5.90.8D.E8.A7.84.E8.8C.83)。
> - &lt;SecretId&gt; 和 &lt;SecretKey&gt;为密钥信息，您可前往访问管理控制台的 [云 API 密钥管理](https://console.cloud.tencent.com/cam/capi) 中查看和创建。
> - 您也可以将密钥配置在文件 $HOME/.passwd-cosfs 中，或通过 -opasswd_file=[path] 指定密钥文件路径，同时您需要将密钥文件的权限值设置为600。
> 

**示例：**

```shell
echo examplebucket-1250000000:AKIDHTVVaVR6e3****:PdkhT9e2rZCfy6**** > /etc/passwd-cosfs
chmod 640 /etc/passwd-cosfs
```

>! V1.0.5及较早版本的 COSFS，配置文件格式为&lt;BucketName>:&lt;SecretId>:&lt;SecretKey>。
>


### 2. 运行工具
将密钥文件中配置的存储桶挂载到指定目录，可以使用如下命令行：

```shell
cosfs <BucketName-APPID> <MountPoint> -ourl=http://cos.<Region>.myqcloud.com -odbglevel=info -oallow_other
```
其中：
- &lt;MountPoint&gt; 为本地挂载目录（例如`/mnt`）。
- &lt;Region&gt; 为地域简称， 例如 ap-guangzhou 、 eu-frankfurt 等。更多地域简称信息，请参见 [可用地域](https://cloud.tencent.com/document/product/436/6224)。
- -odbglevel 指定日志级别，默认为crit，可选值为crit、error、warn、info、debug。
- -oallow_other 允许非挂载用户访问挂载文件夹。

**示例：**

```shell
mkdir -p /mnt/cosfs
cosfs examplebucket-1250000000 /mnt/cosfs -ourl=http://cos.ap-guangzhou.myqcloud.com -odbglevel=info -onoxattr -oallow_other
```

>!
>- COSFS 工具为提升性能，默认使用系统盘存放上传、下载的临时缓存，文件关闭后会释放空间。在并发打开的文件数较多或者读写大文件的时候，COSFS 工具会尽量多的使用硬盘来提高性能，默认只保留 100MB 硬盘可用空间给其他程序使用，可以通过选项 oensure_diskfree=[size] 设置 COSFS 工具保留可用硬盘空间的大小，单位为 MB。例如`-oensure_diskfree=1024`，COSFS 工具会保留1024MB剩余空间。
>- V1.0.5及较早版本的 COSFS，挂载命令为 cosfs &lt;APPID>:&lt;BucketName> &lt;MountPoint> -ourl=&lt;CosDomainName> -oallow_other。
>


### 3. 卸载存储桶

卸载存储桶示例：

```shell
方式1：fusermount -u /mnt, fusermount 命令专用于卸载 FUSE 文件系统 
方式2：umount -l /mnt, 当有程序引用文件系统中文件时，进行卸载不会报错，并在没程序引用时完成卸载
方式3：umount /mnt， 当有程序引用文件系统中的文件时，进行卸载会报错
```

## 常用挂载选项

#### -omultipart_size=[size]
用来指定分块上传时单个分块的大小（单位： MB），默认是10MB。 由于分块上传对单个文件块的数目有最大限制（10000块），所以对于超出100GB（10MB \* 10000）大小的文件，需要根据具体情况调整该参数。

#### -oallow_other
如果要允许其他用户访问挂载文件夹，可以在运行 COSFS 的时候指定该参数。

#### -odel_cache
默认情况下，COSFS 工具为了优化性能，在 umount 后，不会清除本地的缓存数据。 如果需要在 COSFS 退出时，自动清除缓存，可以在挂载时加入该选项。

####  -onoxattr
禁用 getattr/setxattr 功能，在1.0.9之前版本的 COSFS 不支持设置和获取扩展属性，如果在挂载时使用了 use_xattr 选项，可能会导致 mv 文件到 Bucket 失败。

#### -opasswd_file=[path]
该选项可以指定 COSFS 密钥文件的所在路径，该选项设定的密钥文件需要设置权限为600。

#### -odbglevel=[dbg|info|warn|err|crit]

设置 COSFS 日志记录级别，可选 info、dbg、warn、err 和 crit。生产环境中建议设置为 info，调试时可以设置为 dbg。如果您的系统日志，未定期清理且由于访问量很大，生成大量日志，您可以设置为 err 或者 crit。

#### -oumask=[perm]

该选项可以去除给定类型用户，对挂载目录内文件的操作权限。例如，-oumask=755，对应挂载目录的权限变为022。

#### -ouid=[uid]
该选项允许用户 id 为 [uid] 的用户不受挂载目录中文件权限位的限制，可以访问挂载目录中的所有文件。
获取用户 uid 可以使用 id 命令，格式` id -u username`。例如执行`id -u user_00`，可获取到用户 user_00 的 uid。

#### -oensure_diskfree=[size]

COSFS 工具为提升性能，默认使用系统盘存放上传、下载的临时缓存，文件关闭后会释放空间。在并发打开的文件数较多或者读写大文件的时候，COSFS 工具会尽量多的使用硬盘来提高性能，默认只保留 100MB 硬盘可用空间给其他程序使用，可以通过选项 oensure_diskfree=[size] 设置 COSFS 工具保留可用硬盘空间的大小，单位为 MB。例如`-oensure_diskfree=1024`，COSFS 工具会保留1024MB剩余空间。


## 常见问题
如果您在使用 COSFS 工具过程中有相关的疑问，请参见 [COSFS 工具类常见问题](https://cloud.tencent.com/document/product/436/30743)。
