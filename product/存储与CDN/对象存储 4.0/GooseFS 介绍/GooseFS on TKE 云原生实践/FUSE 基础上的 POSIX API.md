GooseFS-FUSE 可以在一台 Unix 机器上的本地文件系统中挂载一个 GooseFS 分布式文件系统。通过使用该特性，一些标准的命令行工具（例如 ls、cat 以及 echo）可以直接访问 GooseFS 分布式文件系统中的数据。此外更重要的是使用不同语言实现的应用程序，例如 C、C++、Python、Ruby、Perl、Java 都可以通过标准的 POSIX 接口（例如 open、write、read）来读写 GooseFS，而不需要任何 GooseFS 的客户端整合与设置。

GooseFS-FUSE 是基于 [FUSE](http://fuse.sourceforge.net/) 这个项目，并且都支持大多数的文件系统操作。但是由于 GooseFS 固有的属性，例如它的一次写、不可改变的文件数据模型，该挂载的文件系统与 POSIX 标准不完全一致，尚有一定的局限性。因此，请先阅读 [局限性](https://docs.alluxio.io/os/user/stable/cn/api/POSIX-API.html?q=fuse#局限性)，从而了解该特性的作用以及局限。

## 安装要求

- JDK 1.8及以上
- Linux 系统：[libfuse](https://github.com/libfuse/libfuse) 2.9.3及以上（可以使用 2.8.3版本，但会提示一些警告）
- MAC 系统：[osxfuse](https://osxfuse.github.io/) 3.7.1及以上

## 用法

### 挂载 GooseFS-FUSE

完成配置以及启动 GooseFS 集群后，在需要挂载 GooseFS 的节点上启动 Shell，并进入 $GOOSEFS_HOME  目录执行以下命令：
```
$ integration/fuse/bin/goosefs-fuse mount mount_point [GooseFS_path]
```
该命令会启动一个后台 Java 进程，用于将对应的 GooseFS 路径挂载到 `<mount_point>` 指定的路径。例如以下命令，将 GooseFS 路径 /people 挂载到本地文件系统的 /mnt/people 目录下。
```
$ integration/fuse/bin/goosefs-fuse mount /mnt/people /people
Starting goosefs-fuse on local host.
goosefs-fuse mounted at /mnt/people. See /lib/GooseFS/logs/fuse.log for logs
```
当 GooseFS_path 没有给定时，GooseFS-FUSE 会默认挂载到 GooseFS 根目录下(/)。您可以多次调用该命令，将 GooseFS 挂载到不同的本地目录下。所有的 GooseFS-FUSE 会共享 $GOOSEFS_HOME\logs\fuse.log 日志文件。该日志文件对于错误排查很有帮助。
>! `<mount_point>` 必须是本地文件系统中的一个空文件夹，并且启动 GooseFS-FUSE 进程的用户拥有该挂载点及对其的读写权限。
>


### 卸载 GooseFS-FUSE

卸载 GooseFS-FUSE 时，需在该节点上启动 Shell，并进入$GOOSEFS_HOME 目录执行以下命令：
```
$ integration/fuse/bin/goosefs-fuse umount mount_point
```
该命令将终止 goosefs-fuse java 后台进程，并卸载该文件系统。例如：
```
$ integration/fuse/bin/goosefs-fuse umount /mnt/people
Unmount fuse at /mnt/people (PID: 97626).
```
默认情况下，如果有任何读写操作未完成，unmount 操作会等待最多120s。如果120s后读写操作仍未完成，那么 Fuse 进程会被强行结束，这会导致正在读写的文件失败，您可以添加 -s 参数来避免 Fuse 进程被强行结束。例如：
```
$ ${GOOSEFS_HOME}/integration/fuse/bin/goosefs-fuse unmount -s /mnt/people
```

### 检查 GooseFS-FUSE 是否在运行

罗列所有的挂载点，需在该节点上启动 Shell，并进入 $GOOSEFS_HOME 目录执行以下命令：
```
$ integration/fuse/bin/goosefs-fuse stat
```
该命令会输出包括 pid、mount_point、GooseFS_path 在内的信息。

例如输出可以是以下格式：
```
$ pid    mount_point     GooseFS_path
80846  /mnt/people     /people
80847  /mnt/sales       /sales
```
 

### Goosefs-FUSE 目录结构

![](https://qcloudimg.tencent-cloud.cn/raw/1711edcd1e0789aed28f6a295dfe5361.png)

conf 目录下：
- masters：master 服务器的 IP 配置文件
- workers：worker 服务器的 IP 配置文件
- goosefs-site.properties：goosefs 配置文件
- libexec：goosefs-fuse 运行依赖的 lib 库文件
- goosefs-fuse-1.1.0.jar：goosefs-fuse 后台运行的 jar 包
- log：日志目录

## 可选配置

GooseFS-FUSE 基于标准的 GooseFS-core-client-fs 进行操作。如果您希望它像使用其他应用的 client 一样，自定义该 GooseFS-core-client-fs 的行为。

可通过编辑 $GOOSEFS_HOME/conf/goosefs-site.properties 配置文件来更改客户端选项。
>! 所有的更改应该在 GooseFS-FUSE 启动之前完成。
>

## 局限性

目前，GooseFS-FUSE 支持大多数基本文件系统的操作。然而，由于 GooseFS 某些内在的特性，您需要注意以下几点：

-  文件只能顺序地写入一次，并且无法修改。这意味着如果要修改一个文件，您需要先删除该文件，然后再重新创建。例如当目标文件存在时，拷贝命令 cp 会失败。
-  GooseFS 没有 hard-link 和 soft-link 的概念，所以不支持与之相关的命令，例如 ln。此外关于 hard-link 的信息也不在 ll 的输出中显示。
-  只有当 GooseFS 的 GooseFS.security.group.mapping.class 选项设置为ShellBasedUnixGroupsMapping 的值时，文件的用户与分组信息才与 Unix 系统的用户分组对应。否则 chown 与 chgrp 的操作不生效，而 ll 返回的用户与分组为启动 GooseFS-FUSE 进程的用户与分组信息。

## 性能考虑

由于 FUSE 和 JNR 的配合使用，与直接使用原生文件系统 API 相比，使用挂载文件系统的性能会相对较差。

大多数性能问题的原因在于，每次进行 read 或 write 操作时，内存中都存在若干个副本，并且 FUSE 将写操作的最大粒度设置为128KB。其性能可以利用 kernel 3.15 引入的 FUSE 回写（write-backs）缓存策略从而得到大幅提高（但 libfuse 2.x 用户空间库目前尚不支持该特性）。

## GooseFS-FUSE 配置参数

以下是 GooseFS-FUSE 相关的配置参数：

| **参数**                                    | **默认值**   | **描述**                                                     |
| ------------------------------------------- | ------------ | ------------------------------------------------------------ |
| goosefs.fuse.cached.paths.max               | 500          |   定义内部 GooseFS-FUSE 缓存的大小，该缓存维护本地文件系统路径和 Alluxio 文件 URI 之间最常用的转换。                                                           |
| goosefs.fuse.debug.enabled                  | false        | 允许 FUSE 调试输出，该输出会被重定向到`goosefs.logs.dir`指定目录中的`fuse.out`日志文件。 |
| goosefs.fuse.fs.name                        | goosefs-fuse | FUSE 挂载文件系统使用的描述性名称。                           |
| goosefs.fuse.jnifuse.enabled                | true         |   使用 JNI-Fuse 库以获得更好的性能。 如果禁用，将使用 JNR-Fuse。                                                           |
| goosefs.fuse.shared.caching.reader.enabled  | false        |  （实验性）使用共享 grpc 数据读取器，通过 GooseFS JNI Fuse 在多进程文件读取中获得更好的性能。块数据将缓存在客户端，因此 Fuse 进程需要更多内存。                                                            |
| goosefs.fuse.logging.threshold              | 10s          |  当花费的时间超过阈值时记录 FUSE API 调用。                                                            |
| goosefs.fuse.maxwrite.bytes                 | 131072       | FUSE 写操作的粒度（bytes），注意目前128KB是 Linux 内核限制的上界。 |
| goosefs.fuse.user.group.translation.enabled | false        | 是否在 FUSE API 中将 GooseFS 的用户与组转化为对应的 Unix 用户与组。当设为 false 时，所有 FUSE 文件的用户与组将会显示为挂载 goosefs-fuse 线程的用户与组。 |

## 常见问题

缺少 libfuse 库文件，需要安装 libfuse。
![](https://qcloudimg.tencent-cloud.cn/raw/7a535eed0fac0da06f530fb04ca9702b.png)
- **方式一**
安装命令：
```
yum install fuse-devel
```
查看是否安装成功：
```
find / -name libfuse.so*
```
- **方式二**
更新旧版本 libfuse.so.2.9.2，安装步骤如下：
>? 在 CentOS 7安装 libfuse，CentOS 7默认安装的是 libfuse.so.2.9.2。
>
首先，下载 [libfuse 源码](https://github.com/libfuse/libfuse/releases/tag/fuse-2.9.7)，并编译生成 libfuse.so.2.9.7。
```
tar -zxvf fuse-2.9.7.tar.gz
cd fuse-2.9.7/ && ./configure && make && make install
echo -e '\n/usr/local/lib' >> /etc/ld.so.conf
ldconfig
```
其次，下载、编译及生成 libfuse.so.2.9.7 后，然后按照以下步骤进行安装替换。
 1. 执行以下命令，查找旧版本 libfuse.so.2.9.2 库链接。
```
find / -name libfuse.so*
```
 2. 执行以下命令，将 libfuse.so.2.9.7拷贝至旧版本库 libfuse.so.2.9.2 所在位置。
```
cp /usr/local/lib/libfuse.so.2.9.7 /usr/lib64/
```
 3. 执行以下命令， 删除旧版本 libfuse.so 库的所有链接。
```
rm -f /usr/lib64/libfuse.so
rm -f /usr/lib64/libfuse.so.2
```
 4. 执行以下命令，建立与被删除旧版本链接类似的 libfuse.so.2.9.7 库链接。
```
ln -s /usr/lib64/libfuse.so.2.9.7 /usr/lib64/libfuse.so
ln -s /usr/lib64/libfuse.so.2.9.7 /usr/lib64/libfuse.so.2
```
 

 

 
