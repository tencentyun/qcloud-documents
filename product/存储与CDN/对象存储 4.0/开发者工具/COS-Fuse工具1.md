## 功能说明

### 简介

cosfs 能让您在Linux/Mac OS X 系统中把Tencent COS bucket 挂载到本地文件 系统中，您能够便捷的通过本地文件系统操作COS 上的对象，实现数据的共享。

### 功能

cosfs 基于s3fs 构建，具有s3fs 的全部功能。主要功能包括：

- 支持POSIX 文件系统的大部分功能，包括文件读写，目录，链接操作，权限，uid/gid
- 通过COS 的multipart 功能上传大文件。
- MD5 校验保证数据完整性。

## 使用环境

### 系统环境

Linux



## 使用方法
### 获取程序包  
当前版本：COSFS-V4.2.1  
[GitHub下载地址](https://github.com/tencentyun/cosfs-v4.2.1)  
[本地下载地址](https://mc.qcloudimg.com/static/archive/144302cd3e6afb2bf2758a8c0c1d9bb9/cosfs-v4.2.1-master.zip)

### 编译安装
#### 安装依赖库
如果没有找到对应的安装包，您也可以自行编译安装。编译前请先安装下列依赖库：  
Ubuntu 14.04:

```
sudo apt-get install automake autotools-dev g++ git libcurl4-gnutls-dev \
                     libfuse-dev libssl-dev libxml2-dev make pkg-config
```

CentOS 7.0:
```
sudo yum install automake gcc-c++ git libcurl-devel libxml2-devel \
                 fuse-devel make openssl-devel
```
#### 安装源码

然后您可以在github上下载源码并编译安装：
```
git clone https://github.com/XXX/cosfs.git
cd cosfs
./autogen.sh
./configure
make
sudo make install
```

### 配置运行

设置bucket name, access key/id信息，将其存放在/etc/passwd-cosfs 文件中， 注意这个文件的权限必须正确设置，建议设为640。
```
echo my-bucket:my-access-key-id:my-access-key-secret > /etc/passwd-cosfs
chmod 640 /etc/passwd-cosfs
```
将cos bucket mount到指定目录,注意 需要在bucke前面指定appid
```
cosfs my-appid:my-bucket my-mount-point -ourl=my-cos-endpoint
```
#### 示例

将my-bucket这个bucket挂载到/tmp/cosfs目录下，AccessKeyId是faint， AccessKeySecret是123，cos endpoint是http://cn-south.myqcloud.com cn-south 对应华南广州地域 cn-north 对应华北天津地域 cn-east 对应华东上海地域

```
echo my-bucket:faint:123 > /etc/passwd-cosfs
chmod 640 /etc/passwd-cosfs
mkdir /tmp/cosfs
cosfs appid:my-bucket /tmp/cosfs -ourl=http://cn-south.myqcloud.com -odbglevel=info -ouse_cache=/path/to/local_cache
```
**说明：**-ouse_cache 指定了使用本地cache来缓存临时文件，进一步提高性能，如果不需要本地cache或者本地磁盘容量有限，可不指定该选项

### 卸载
卸载bucket:
```
fusermount -u /tmp/cosfs # non-root user
```

## 常见问题
### 局限性

cosfs提供的功能和性能和本地文件系统相比，具有一些局限性。具体包括：

- 随机或者追加写文件会导致整个文件的重写。
- 元数据操作，例如list directory，性能较差，因为需要远程访问COS服务器。
- 文件/文件夹的rename操作不是原子的。
- 多个客户端挂载同一个COS bucket时，依赖用户自行协调各个客户端的行为。例如避免多个客户端写同一个文件等等。
- 不支持hard link。
- 不适合用在高并发读/写的场景，这样会让系统的load升高
