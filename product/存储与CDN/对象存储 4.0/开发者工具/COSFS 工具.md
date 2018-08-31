## 功能说明 
COSFS 工具支持将 COS 存储桶挂载到本地，像使用本地文件系统一样直接操作腾讯云对象存储。COSFS 的主要功能包括：
- 支持 POSIX 文件系统的大部分功能，如：文件读写、目录操作、链接操作、权限管理、uid/gid 管理等功能；
- 大文件传输功能；
- MD5 数据校验功能。

## 使用环境 
### 系统环境 
主流 Linux 系统。

### 软件环境 
本工具编译需要 C++ 编译环境。依赖于 automake、git 、libcurl-devel、libxml2-devel、fuse-devel、make、openssl-devel 等软件，安装方法参考 [环境安装](#环境安装)。
<span id="环境安装"></span>
### 环境安装 
#### Ubuntu 系统下安装环境依赖包方法：
```
sudo apt-get install automake autotools-dev g++ git libcurl4-gnutls-dev libfuse-dev libssl-dev libxml2-dev make pkg-config fuse
```

#### CentOS 系统下安装环境依赖包方法：
```
sudo yum install automake gcc-c++ git libcurl-devel libxml2-devel fuse-devel make openssl-devel
```

注意在 centos6.5 及较低版本，可能会提示 fuse 版本太低，在安装过程的 configure 操作时返回
```
 checking for common_lib_checking... configure: error: Package requirements (fuse >= 2.8.4 libcurl >= 7.0 libxml-2.0 >=    2.6) were not met:
  Requested 'fuse >= 2.8.4' but version of fuse is 2.8.3 
```
此时，您需要来手动安装 fuse 版本，具体命令如下：
```
 # yum remove -y fuse-devel
  # wget https://github.com/libfuse/libfuse/releases/download/fuse_2_9_4/fuse-2.8.4.tar.gz
  # tar -zxvf fuse-2.8.4.tar.gz
  # cd fuse-2.8.4
  # ./configure
  # make
  # make install
  # export PKG_CONFIG_PATH=/usr/lib/pkgconfig:/usr/lib64/pkgconfig/:/usr/local/lib/pkgconfig
  # modprobe fuse
  # echo "/usr/local/lib" >> /etc/ld.so.conf
  # ldconfig
  # pkg-config --modversion fuse   
  2.8.4   //看到版本表示安装成功  
```

## 使用方法 
### 1. 获取工具 
Github 下载地址： [COSFS 工具](https://github.com/tencentyun/cosfs)。

### 2. 安装工具 
您可以直接将下载的源码上传至指定目录，也可以使用 GitHub 下载到指定目录，下面以使用 GitHub 将源码目录下载到 `/usr/cosfs` 为例：
```
git clone https://github.com/tencentyun/cosfs /usr/cosfs
```
进入到该目录，编译安装：
```
cd /usr/cosfs
./autogen.sh
./configure
make
sudo make install
```
### 3. 配置文件
在 `/etc/passwd-cosfs`文件中，配置您的存储桶的名称，以及该存储桶对应的 SecretId 和 SecretKey，相关概念参见 [对象存储基本概念](https://cloud.tencent.com/document/product/436/6225)。使用冒号隔开，注意冒号为半角符号。 并为 `/etc/passwd-cosfs` 设置可读权限。命令格式如下：
```
echo <bucketname>:<SecretId>:<SecretKey> > /etc/passwd-cosfs
chmod 640 /etc/passwd-cosfs
```
其中：
bucketname/ SecretId/ SecretKey 需要替换为用户的真实信息。

bucketname 形如 bucketprefix-123456789, 更多关于 bucketname 的命名规范，请参见 [存储桶命名规范](https://cloud.tencent.com/document/product/436/13312#.E5.AD.98.E5.82.A8.E6.A1.B6.E5.91.BD.E5.90.8D.E8.A7.84.E8.8C.83)。

#### 示例：
```
echo bucketprefix-123456789:AKID8ILGzYjHMG8zhGtnlX7Vi4KOGxRqg1aa:LWVJqIagbFm8IG4sNlrkeSn5DLI3dCYi > /etc/passwd-cosfs
chmod 640 /etc/passwd-cosfs
```
### 4. 运行工具
将配置好的存储桶挂载到指定目录，命令行如下：
```
cosfs your-bucketname your-mount-point -ourl=cos-domain-name -odbglevel=info
```
其中：
- your-bucketname 需要替换为用户真实的信息；
- your-mount-point 替换为本地需要挂载的目录（如 /mnt）；
- cos-domain-name 为存储桶对应的访问域名，形式为 `http://cos.<Region>.myqcloud.com` （适用于XML API），其中 <Region> 为地域简称，如： `ap-guangzhou` 、 `eu-frankfurt` 等。更多地域信息，请查阅 [可用地域](https://cloud.tencent.com/document/product/436/6224)。
- -odbglevel 参数表示信息级别，可选 info、dbg，建议参照示例设置为“info”。

注意： 

v1.0.5 版本之前的 cosfs 挂载命令：
```
cosfs bucketname_suffix:bucketname_prefix my-mount-point -ourl=my-cos-endpoint
```

v1.0.5 版本之前的配置文件格式是：
```
bucketname_prefix:<SecretId>:<SecretKey>
```
其中 `bucketname_suffix` 指的是 bucket 名称中的数字后缀, `bucketname_prefix` 指的是除数字后缀外的其他部分。
例如 bucketprefix-1253972369 的 `bucketname_suffix` 为 1253972369，`bucketname_prefix` 为 bucketprefix。

#### 示例：
```
cosfs bucketprefix-1253972369 /mnt -ourl=http://cos.ap-guangzhou.myqcloud.com -odbglevel=info -onoxattr
```
另外，如果对性能有要求，可以使用本地磁盘缓存文件，命令中加入 -ouse_cache 参数，示例如下：
```
mkdir /local_cache_dir
cosfs bucketprefix-1253972369 /mnt -ourl=http://cos.ap-guangzhou.myqcloud.com -odbglevel=info -onoxattr -ouse_cache=/local_cache_dir
```

>`/local_cache_dir` 为本地缓存目录，如果不需要本地缓存或本地磁盘容量有限，可不指定该选项。

卸载存储桶示例：
```
fusermount -u /mnt
```
或者

```
umount -l /mnt
```

## 常用挂载选项

1. -omultipart_size=[size]
`multipart_size` 用来指定分块上传时，每个分块的大小，默认是 10 MB。 由于分块上传对块的数目有最大限制（10000 块），所以对于大文件，例如超出 10 MB * 10000 (100 GB) 大小的文件，需要根据具体情况调整该参数。该参数单位是 MB。

2. -oallow_other
如果要允许其他用户访问挂载文件夹，可以在运行 COSFS 的时候指定 `allow_other` 参数。

3. -odel_cache
默认情况下，cosfs 为了优化性能，在 umount 后，不会清除本地的缓存数据。 如果需要在 COSFS 退出时，自动清除缓存，可以在挂载时加入该选项。

4. -onoxattr
禁用 get/setxattr 功能， 当前版本的 cosfs 不支持该功能，如果本地文件所在磁盘在挂载的时候使用了 use_xattr 选项，可能会导致 mv 文件到 bucket 失败。

## 局限性
COSFS 提供的功能、性能和本地文件系统相比，存在一些局限性。例如：
- 随机或者追加写文件会导致整个文件的重写。
- 多个客户端挂载同一个 COS 存储桶时，依赖用户自行协调各个客户端的行为。例如避免多个客户端写同一个文件等。
- 不支持 hard link，不适合高并发读/写的场景。
- 不可以同时在一个挂载点上挂载、和卸载文件。您可以先 cd 切换到其他目录，再对挂载点进行挂载、卸载操作。

## 常见问题
**1. 如何挂载目录？**
您在挂载命令的时候，可以指定目录，命令如下：
```
cosfs my-bucket-name:/my-dir /tmp/cosfs -ourl=http://cn-south.myqcloud.com -odbglevel=info -ouse_cache=/path/to/local_cache
```
> 注意：my-dir 必须以 `/` 开头。

如使用 v1.0.5 之前版本，则挂载命令为：
```
cosfs my-bucket-name-suffix:my-bucket-name-prefix:/my-dir /tmp/cosfs -ourl=http://cn-south.myqcloud.com -odbglevel=info -ouse_cache=/path/to/local_cache
```
**2. 为什么之前可用写文件，突然不能写了？**
由于 COS 鉴权产品策略调整，所以老版本的 cosfs 工具会导致策略校验不过，因此需要拉取最新的 cosfs 工具重新 mount。

**3. 在 centos6.5 及较低版本，提示 fuse 版本太低，该如何解决？**
如在 configure 操作时，提示
```
hecking for common_lib_checking... configure: error: Package requirements (fuse >= 2.8.4 libcurl >= 7.0 libxml-2.0 >=    2.6) were not met:Requested 'fuse >= 2.8.4' but version of fuse is 2.8.3 
```

此时，您需要来手动安装 fuse 版本，具体命令如下：
```
# yum remove -y fuse-devel
# wget https://github.com/libfuse/libfuse/releases/download/fuse_2_9_4/fuse-2.8.4.tar.gz
# tar -zxvf fuse-2.8.4.tar.gz
# cd fuse-2.8.4
# ./configure
# make
# make install
# export PKG_CONFIG_PATH=/usr/lib/pkgconfig:/usr/lib64/pkgconfig/:/usr/local/lib/pkgconfig
# modprobe fuse
# echo "/usr/local/lib" >> /etc/ld.so.conf
# ldconfig
# pkg-config --modversion fuse   
2.8.4   //看到版本表示安装成功
```

**4. 为什么 cosfs 在正常使用过程中，突然退出了，重新挂载显示"unable to access MOUNTPOINT /path/to/mountpoint: Transport endpoint is not connected"？**
如果 cosfs 不是被强制退掉，那么检查机器上的 fuse 版本是否低于 2.9.4，libfuse 在低于 2.9.4 版本的情况下可能会导致 cosfs 异常退出。建议更新 fuse 版本，或下载 [cosfs V1.0.2](https://github.com/tencentyun/cosfs/releases) 及以上版本。

**5. 为什么通过 cosfs 上传的文件 Content-Type 全是"application/octet-stream"？**
cosfs 是根据 /etc/mime.types 和上传的文件后缀进行比对，自动设置 Content-Type，建议查看机器上是否存在该文件。对于 ubuntu， 可以通过 sudo apt-get install mime-support 来添加。对于 centos，可以通过 sudo yum install mailcap 来添加。或者手动添加，每种格式一行，例如：image/png png。
