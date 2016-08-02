## 功能说明

该工具支持从 COS 1.0 将文件下载至本地。

> 下载前后案例：
>
> COS 1.0 的 AccessID 为 1000247，BucketName 为 test，本地目录为 download。
>
> 源文件路径为 `http://cos.myqcloud.com/1000247/test/file`
>
> 下载访问路径为 `download/file`

迁移完成后您需要修改文件的访问路径，修改您原先管理使用的 API 或 SDK，更多关于 COS 3.x 的信息请从左边目录中了解。

## 准备工作

### 所需信息

您需要有 COS 1.0 的 AppID、AccessKey、SecretKey、Bucket。

### 系统配置

```
系统要求：建议 CentOS、Ubuntu、Debian 等 64 位操作系统
网络要求：建议 腾讯云 CVM 或在较为稳定的电信、联通网络下使用
内存要求：512MB 以上
磁盘要求：至少保留大于需要迁移的 COS 1.0 的存储容量
```

### 安装方法

以 CentOS 为例，需先下载安装 PHP 和 libcurl。

```shell
yum -y install php nano wget libcurl-devel gcc-c++
```

通过以下地址下载迁移工具压缩包，并执行解压缩。

```shell
wget http://mccdn.qcloud.com/static/archive/1ba6d3a325d0a82852403178c4efc927/old_cos_backup_to_local.tar.gz

tar zxvf old_cos_backup_to_local.tar.gz
```

如果您使用的是 32 位的系统，可能需要重新编译安装，编译方法如下。

```shell
cd old_cos_backup_to_local/code/old_cos_code/migrate_tool
make
```

## 使用方法

### 配置权限

```shell
chmod u+x code/*
```

### 修改配置

配置文件位于 old_cos_backup_to_local/conf/config.ini，您需要修改它。

```shell
nano old_cos_backup_to_local/conf/config.ini
```

源数据配置信息如下：

```
[SrcStorageInfo]
SrcStorageStart=0
SrcStorageBucket=老cos上的空间名称
SrcStorageAppId=老cos上的appid
SrcStorageAccessKey=老cos的secretId
SrcStorageSecretKey=老cos的secretKey
SrcStorageDomain=cos.myqcloud.com
```

为加快下载速度，可以设置并发数，若带宽在 20Mbps 以上，可以设置为 100 并发上传，带宽较小应适当调小。

```
[ToolConfig]
Concurrency=100
```

### 执行迁移

运行工具放置在安装包的 bin 目录下，所以进入目录运行程序。

```shell
cd old_cos_backup_to_local/bin

./start.sh cos &
```

执行完启动的命令，因为指定了&符号，即会后台运行。

工具会首先从源存储获取所有文件列表，然后按照配置的并发数，将任务拆分，并发执行下载和上传。任务拆分完，界面会输出：start task down. use ./stat.sh to see task status，注意，此条输出只表示任务启动完毕，此时迁移任务还很有可能正在进行。

### 查看进度

如需查看详细日志输出，可以输入以下命令：

```shell
tail -f output/detail_log 
```

如需退出，可以在键盘上按下 `Ctrl-C` 退出工具。

### 获取失败信息

```shell
./get_failed_info.sh
```

