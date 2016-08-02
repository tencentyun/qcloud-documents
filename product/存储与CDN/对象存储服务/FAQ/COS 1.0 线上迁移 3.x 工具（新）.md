## 功能说明

该工具支持从 COS 1.0 将文件迁移至 COS 3.x，通过配置原存储的信息和新存储的信息，可以自动将旧文件迁移至新的对象存储服务中。

**工作机制：根据提供的线程数，将 COS 1.0 的数据同时下载一批文件到本地磁盘。其中一个线程的工作流程为：下载 COS 1.0 - 上传 COS 3.x - 删除本地文件，完成后释放该线程，并自动开启下一个线程下载。**

> 迁移前后案例：
>
> COS 1.0 的 AccessID 为 1000247，BucketName 为 test。
>
> 源文件路径为 `http://cos.myqcloud.com/1000247/test/file`
>
> COS 3.x 的 AppID 为 1000027，BucketName 为 newtest。
>
> 新访问路径为 `http://newtest-1000027.cos.myqcloud.com/file`

迁移完成后您需要修改文件的访问路径，修改您原先管理使用的 API 或 SDK，更多关于 COS 3.x 的信息请从左边目录中了解。

## 准备工作

### 所需信息

您需要有 COS 1.0 的 AppID、AccessKey、SecretKey、Bucket，并且在 https://console.qcloud.com/cos 开通 COS 3.x 并创建一个目的 Bucket。

您可以通过控制台左侧的密钥管理，获得新的 AppID、SecretID、SecretKey。

### 系统配置

```
系统要求：建议 CentOS、Ubuntu、Debian 等 64 位操作系统
网络要求：建议 腾讯云 CVM 或在较为稳定的电信、联通网络下使用
内存要求：512MB 以上
磁盘要求：根据线程数和文件大小，预留足够的容量。
```

### 安装方法

以 CentOS 为例，需先下载安装 PHP。

```shell
yum -y install php nano wget gcc-c++
```

通过以下地址下载迁移工具压缩包，并执行解压缩。

```shell
wget http://mccdn.qcloud.com/static/archive/7dcc8b030a078b70ba25be6a5d57fe34/cos_migration_tools.zip

tar zxvf cos_migration_tools.tar.gz
```

## 使用方法

### 配置权限

```shell
chmod u+x code/*
```

### 修改配置

配置文件位于 cos_migration_tools/conf/config.ini，您需要修改它。

```shell
nano cos_migration_tools/conf/config.ini
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

配置新存储信息如下：

```
[CosInfo]
CosAppId=新cos中的APP ID
CosSecretId=新cos中的secretID
CosSecretKey=新cos中的secretKey
CosBucket=新cos中的Bucket名称
```

为加快迁移速度，可以设置并发数，若带宽在 20Mbps 以上，可以设置为 100 并发上传，带宽较小应适当调小。

```
[ToolConfig]
Concurrency=100
```

### 执行迁移

运行工具放置在安装包的 bin 目录下，所以进入目录运行程序。

```shell
cd cos_migration_tools/bin

./start.sh cos &
```

执行完启动的命令，因为指定了&符号，即会后台运行。

工具会首先从源存储获取所有文件列表，然后按照配置的并发数，将任务拆分，并发执行下载和上传。

任务拆分完，界面会输出：start task down. use ./stat.sh to see task status，注意，此条输出只表示任务启动完毕，此时迁移任务还很有可能正在进行，判断迁移是否完成，可以使用询问任务是否结束工具。

### 查看进度

执行以下命令会，输出要迁移的文件总数，以及已经迁移成功和迁移失败的文件数。

```shell
./stat.sh
```

如需查看详细日志输出，可以输入以下命令：

```shell
./stat_detail.sh
```

如需退出，可以在键盘上按下 `Ctrl-C` 退出工具。

### 询问是否结束

```shell
./is_still_doing.sh
```

如果迁移已经完成会输出：no, task has been done

如果还在迁移会输出：yes, still doing download and upload...并且输出正在运行的进程信息。

### 停止迁移

```shell
./stop.sh
```

运行该脚本后，迁移任务就会停止，之后想再启动，可以重启迁移任务。

### 重启迁移

```shell
./stat.sh
```

如果有输出has migrate[0] files, will migrate[XX] files的信息，如下图，说明文件列表已经获取完毕，可以不再拉取文件列表重启。

```shell
./restart_not_get_file_list.sh cos & 
```

如果没有输出，说明列表没有获取完毕，运行启动迁移工具：

```shell
./start.sh cos &
```

### 获取失败信息

```shell
./get_failed_info.sh
```

### 失败处理

若中途异常，可以通过停止和重启迁移的方式进行。

如果看到迁移进度中有失败的迁移文件，无需立即操作，通过询问进程等待所有任务都完成后，使用重启迁移「不再拉取文件列表重启」就会直接执行失败的部分。