## 功能说明 
COSFS 工具支持将 COS 存储桶挂载到本地，像使用本地文件系统一样直接操作腾讯云对象存储。COSFS 的主要功能包括：
- 支持 POSIX 文件系统的大部分功能，如：文件读写、目录操作、链接操作、权限管理、uid/gid 管理等功能；
- 大文件传输功能；
- MD5 数据校验功能。

## 使用限制 
本工具可以支持对COS V4、V5 版本存储的访问，但是域名均需使用 COS V5 域名。
## 使用环境 
### 系统环境 
主流 Linux 系统

### 软件环境 
本工具编译需要 C++ 编译环境。依赖于 automake、git 、libcurl-devel、libxml2-devel、fuse-devel、make、openssl-devel 等软件，安装方法参考 [环境安装](#环境安装)。
<span id="环境安装"></span>
### 环境安装 
#### Ubuntu 系统下安装环境依赖包方法：
```
sudo apt-get install automake autotools-dev g++ git libcurl4-gnutls-dev libfuse-dev libssl-dev libxml2-dev make pkg-config
```

#### CentOS 系统下安装环境依赖包方法：
```
sudo yum install automake gcc-c++ git libcurl-devel libxml2-devel fuse-devel make openssl-devel
```

注意在centos6.5及较低版本，可能会提示fuse版本太低，在安装过程的configure操作时返回
```
 checking for common_lib_checking... configure: error: Package requirements (fuse >= 2.8.4 libcurl >= 7.0 libxml-2.0 >=    2.6) were not met:
  Requested 'fuse >= 2.8.4' but version of fuse is 2.8.3 
```
此时，你需要来手动安装fuse版本，具体步骤
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
### 获取工具 
Github 获取地址： [COSFS 工具](https://github.com/tencentyun/cosfs-v4.2.1)

### 安装工具 
您可以直接将下载的源码上传至指定目录，也可以使用 GitHub 下载到指定目录，下面以使用 GitHub 将源码目录下载到 `/usr/cosfs` 为例：
```
git clone https://github.com/tencentyun/cosfs-v4.2.1 /usr/cosfs
```
进入到该目录，编译安装：
```
cd /usr/cosfs
./autogen.sh
./configure
make
sudo make install
```
### 配置文件
在 `/etc/passwd-cosfs`文件中，配置您的存储桶的名称，以及该存储桶对应的 SecretId 和 SecretKey，相关概念参见 [对象存储基本概念](https://cloud.tencent.com/document/product/436/6225)。使用冒号隔开，注意冒号为半角符号。 并为 `/etc/passwd-cosfs` 设置可读权限。命令格式如下：
```
echo <bucketname>:<SecretId>:<SecretKey> > /etc/passwd-cosfs
chmod 640 /etc/passwd-cosfs
```
其中：
bucketname/ SecretId/ SecretKey 需要替换为用户的真实信息。
#### 示例：
```
echo buckettest:AKID8ILGzYjHMG8zhGtnlX7Vi4KOGxRqg1aa:LWVJqIagbFm8IG4sNlrkeSn5DLI3dCYi > /etc/passwd-cosfs
chmod 640 /etc/passwd-cosfs
```
### 运行工具 
将配置好的存储桶挂载到指定目录，命令行如下：
```
cosfs your-APPID:your-bucketname your mount-point -ourl=cos-domain-name -odbglevel=info
```
其中：
- your-APPID/ your-bucketname 需要替换为用户真实的信息；
- your-mount-point 替换为本地需要挂载的目录（如 /mnt）；
- cos-domain-name 为存储桶所属地域对应域名，形式为 `http://cos.<Region>.myqcloud.com` ，其中 Region 为 [可用地域](https://cloud.tencent.com/document/product/436/6224) 中适用于 XML API 的地域简称，如：`http://cos.ap-guangzhou.myqcloud.com` 、`http://cos.eu-frankfurt.myqcloud.com` 等。
- -odbglevel 参数表示信息级别，照写即可。
#### 示例：
```
cosfs 1253972369:buckettest /mnt -ourl=http://cos.ap-guangzhou.myqcloud.com -odbglevel=info -onoxattr
```
另外，如果对性能有要求，可以使用本地磁盘缓存文件，命令中加入 -ouse_cache 参数，示例如下：
```
mkdir /local_cache_dir
cosfs 1253972369:buckettest /mnt -ourl=http://cos.ap-guangzhou.myqcloud.com -odbglevel=info -onoxattr -ouse_cache=/local_cache_dir
```
`/local_cache_dir`为本地缓存目录，如果不需要本地缓存或本地磁盘容量有限，可不指定该选项。

卸载存储桶：
```
fusermount -u /mnt
```
或者

```
umount -l /mnt
```

## 常用挂载选项

1. -omultipart_size=[size]
`multipart_size`用来指定分块上传时，每个分块的大小，默认是 10 MB。 由于分块上传对块的数目有最大限制（10000 块），所以对于大文件，例如超出10 MB * 10000 (100 GB) 大小的文件，需要根据具体情况调整该参数。该参数单位是 MB。

2. -oallow_other
如果要允许其他用户访问挂载文件夹，可以在运行 COSFS 的时候指定`allow_other`参数。

3. -odel_cache
默认情况下，cosfs 为了优化性能，在 umount 后，不会清除本地的缓存数据。 如果需要在 COSFS 退出时，自动清除缓存，可以在挂载时加入该选项。

4. -noxattr
禁用get/setxattr功能， 当前版本的cosfs不支持该功能，如果本地文件所在磁盘在挂载的时候使用了use_xattr选项，可能会导致mv文件到 bucket 失败。

## 注意事项 
- COSFS 提供的功能和性能和本地文件系统相比，具有一些局限性。具体包括：随机或者追加写文件会导致整个文件的重写。
- 多个客户端挂载同一个 COS 存储桶时，依赖用户自行协调各个客户端的行为。例如避免多个客户端写同一个文件等。
- 不支持 hard link 。不适合高并发读/写的场景。
- 挂载、卸载文件时，不要同时在挂载点上。可以先 cd 到其他目录，再对挂载点进行挂载、卸载操作。


### 常见问题
* 如何挂载目录
   在挂载命令的时候，可以指定目录，如
   
  `cosfs appid:my-bucket:/my-dir /tmp/cosfs -ourl=http://cn-south.myqcloud.com -odbglevel=info -ouse_cache=/path/to/local_cache`
   注意，my-dir必须以/开头
   
   
* 为什么之前可用写文件，突然不能写了？

   由于cos鉴权产品策略调整，所以老版本的cosfs工具会导致策略校验不过，因此需要拉取最新的cosfs工具重新mount


* 在centos6.5及较低版本，提示fuse版本太低，该如何解决？

  如在configure操作时，提示
  ```
    hecking for common_lib_checking... configure: error: Package requirements (fuse >= 2.8.4 libcurl >= 7.0 libxml-2.0 >=    2.6) were not met:
    Requested 'fuse >= 2.8.4' but version of fuse is 2.8.3 
    ```

   此时，你需要来手动安装fuse版本，具体步骤

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

* 为什么cosfs在正常使用过程中，突然退出了，重新挂载显示"unable to access MOUNTPOINT /path/to/mountpoint: Transport endpoint is not connected"

  如果cosfs不是被强制Kill掉，那么检查机器上的fuse版本是否低于2.9.4，libfuse在低于2.9.4版本的情况下可能会导致cosfs异常退出。
  建议更新fuse版本，或下载cosfs V1.0.2及以上版本。下载地址: https://github.com/tencentyun/cosfs/releases

* 为什么通过cosfs上传的文件Content-Type全是"application/octet-stream"?

  
  cosfs是根据/etc/mime.types和上传的文件后缀进行比对，自动设置Content-Type，建议查看机器上是否存在该文件。

  对于ubuntu可以通过sudo apt-get install mime-support来添加

  对于centos可以通过sudo yum install mailcap来添加

  或者手动添加，每种格式一行，例如：image/png png
