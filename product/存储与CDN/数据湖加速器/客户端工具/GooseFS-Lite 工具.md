## 功能说明 

GooseFS-Lite 工具支持将对象存储（Cloud Object Storage，COS）存储桶挂载到本地，像使用本地文件系统一样直接操作腾讯云对象存储中的对象，相比于 COSFS 工具，GooseFS-Lite  可提供更高的大文件读写速度，不受本地磁盘的性能限制。GooseFS-Lite 支持 POSIX 文件系统的主要功能，例如文件顺序/随机读，顺序写、目录操作等功能。

## 局限性

**GooseFS-Lite 仅适合挂载后对文件进行简单的管理，不支持本地文件系统的一些功能用法。**请注意以下不适用的场景：
- 不支持对文件进行随机写和 truncate 操作。
- 多个客户端挂载同一个 COS 存储桶时，依赖用户自行协调多个客户端的行为。例如避免多个客户端写同一个文件等。
- 文件/文件夹的 rename 操作非原子操作。
- 不支持读取和 rename 当前挂载点正在写入的文件。
- 元数据操作。例如 list directory，性能较差，因为需要远程访问 COS 服务器。
- 不支持 soft/hard link。
- 追加写性能较差，涉及服务端数据拷贝和下载被追加文件。
>! 外网挂载和非低频存储的追加写操作，会产生下载流量费用。
>

## 使用环境

- JDK 11及以上。
- Linux 系统：libfuse 2.9.3及以上。

## 使用方法

### 步骤1：安装依赖

执行如下命令，安装依赖。
```
yum install -y fuse-devel java-11-openjdk-devel
```

### 步骤2：下载 GooseFS-Lite 安装包

1. 执行如下命令，获取 GooseFS-Lite 安装包：
```
curl -LO https://downloads.tencentgoosefs.cn/goosefs-lite/goosefs-lite-1.0.2.tar.gz
```
2. 执行如下命令，获取 GooseFS-Lite 的 Md5 文件：
```
curl -LO https://downloads.tencentgoosefs.cn/goosefs-lite/goosefs-lite-1.0.2-md5.txt
```
3. 执行如下命令，验证文件的完整性。
```
md5sum --check goosefs-lite-1.0.2-md5.txt
```
执行以上三步后，当看到如下图所示，则表示文件完整性验证通过。
![](https://qcloudimg.tencent-cloud.cn/raw/408ed5acc4d6d0866499f94362fe70aa.png)

### 步骤3：解压 GooseFS-Lite 安装包
```
tar -xvf goosefs-lite-${version}.tar.gz
```
您可以将上述命令中的 ${version} 替换为使用的 GooseFS-Lite 版本，例如 1.0.2。当看到如下图所示，则表示解压成功，并生成了一个 goosefs-lite-${version}的目录。
<img src="https://qcloudimg.tencent-cloud.cn/raw/d9fb1f5c09e49799a31fd63446cd95d8.png" style="width: 70%" />


### 步骤4：配置密钥文件

进入./conf 目录下，修改配置文件 conf/core-site.xml 中的配置项，如下图所示：
<img src="https://qcloudimg.tencent-cloud.cn/raw/e08ad0e443d783172a759ffb9764b456.png" style="width: 70%" />

- 将 fs.cosn.userinfo.secretKey 配置为腾讯云密钥 ID。
- 将 fs.cosn.userinfo.secretId 配置为腾讯云密钥 Key。
- 将 fs.cosn.bucket.region 配置为存储桶地域。

>!
>- 建议用户尽量避免在配置中使用永久密钥，采取配置子账号密钥或者临时密钥的方式有助于提升业务安全性。为子账号授权时建议按需授权子账号可执行的操作和资源，避免发生预期外的数据泄露。
>- 如果您一定要使用永久密钥，建议对永久密钥的权限范围进行限制，可通过限制永久密钥的可执行操作、资源范围和条件（访问 IP 等），提升使用安全性。
>

**示例：**

```xml
<configuration>
  <!--账户的 API 密钥信息。可登录 [访问管理控制台](https://console.cloud.tencent.com/capi) 查看云 API 密钥。-->
  <!--建议使用子账号密钥或者临时密钥的方式完成配置，提升配置安全性。为子账号授权时建议按需授权子账号可执行的操作和资源-->
  <property>
    <name>fs.cosn.impl</name>
    <value>org.apache.hadoop.fs.CosFileSystem</value>
  </property>
  <property>
    <name>fs.cosn.userinfo.secretKey</name>
    <value>AKIDnQxxxxx</value>
  </property>
  <property>
    <name>fs.cosn.bucket.region</name>
    <value>ap-guangzhou</value>
  </property>
  <property>
    <name>fs.cosn.userinfo.secretId</name>
    <value>YYYY</value>
  </property>
  <property>
    <name>fs.cosn.read.ahead.queue.size</name>
    <value>16</value>
  </property>
  <property>
    <name>fs.cosn.upload_thread_pool</name>
    <value>32</value>
  </property>
</configuration>
```

如果您挂载的是 [元数据加速](https://cloud.tencent.com/document/product/436/56971) 存储桶，则需要您先对元数据加速存储桶进行如下配置：
1. 性能配置 > HDFS 权限配置 > HDFS 用户配置，添加超级用户，例如 root。
2. 性能配置 > HDFS 权限配置 > HDFS 权限配置，添加访问 COS 存储桶的 VPC 和 IP 地址信息。
3. 在本机执行如下命令，添加 hadoop 用户和 supergroup 组。
```shell
useradd hadoop
groupadd supergroup
```
4. 修改配置信息：
```xml
<configuration>
  <!--账户的 API 密钥信息。可登录 [访问管理控制台](https://console.cloud.tencent.com/capi) 查看云 API 密钥。-->
  <!--建议使用子账号密钥或者临时密钥的方式完成配置，提升配置安全性。为子账号授权时建议按需授权子账号可执行的操作和资源-->
  <property>
    <name>fs.cosn.impl</name>
    <value>org.apache.hadoop.fs.CosFileSystem</value>
  </property>
  <property>
    <name>fs.cosn.userinfo.secretId</name>
    <value>AKIDnQxxxxx</value>
  </property>
  <property>
    <name>fs.cosn.userinfo.secretKey</name>
    <value>YYYY</value>
  </property>
  <property>
    <name>fs.cosn.bucket.region</name>
    <value>ap-guangzhou</value>
  </property>
  <property>
    <name>fs.cosn.trsf.fs.ofs.bucket.region</name>
    <value>ap-guangzhou</value>
  </property>
  <property>
    <name>fs.cosn.trsf.fs.ofs.plugin.info.log</name>
    <value>true</value>
  </property>
  <property>
    <name>fs.cosn.trsf.fs.ofs.user.appid</name>
    <value>1250000000</value>
  </property>
  <property>
    <name>fs.cosn.trsf.fs.ofs.tmp.cache.dir</name>
    <value>/data/tmp/ofs</value>
  </property>
</configuration>
```

### 步骤5：运行工具

执行如下命令，将密钥文件中配置的存储桶挂载到指定目录：
```shell
 ./bin/goosefs-lite mount <MountPoint> cosn://<BucketName>/
```
其中：
- &lt;MountPoint&gt; 为本地挂载目录（例如 `/mnt/goosefs-lite-mnt-dir`）。
- &lt;BucketName&gt; 为存储桶名称（例如 examplebucket-1250000000）。

**示例：**

```shell
mkdir -p /mnt/gooosefs-lite-mnt
./bin/goosefs-lite mount /mnt/goosefs-lite-mnt/ cosn://examplebucket-1250000000/
```

查看本地挂载点和对应的 COS 存储桶，输出信息依次为进程 ID、本地挂载点和 COS 路径：
```
$ ./bin/goosefs-lite stat
pid     mount_point     cos_path
13815   /mnt/goosefs-lite-mnt/  cosn://examplebucket-1250000000/
```

如果您需要在命令行中，同时指定多个挂载参数，可以使用逗号分隔多个参数，例如，下面的命令设置挂载点只读，且允许除其他用户访问挂载点：
```
./bin/goosefs-lite mount -o"ro,allow_other"  mnt/ cosn://examplebucket-1250000000/
```

其中：
- -oallow_other：如果要允许其他用户访问挂载文件夹，可以在运行 GooseFS-Lite 的时候指定该参数。
- -oro：将挂载点设置为只读，不允许写入和删除操作。


>?单个参数可通过 `-o` 指定，例如`-oro`；多个参数可通过逗号分割，例如 `-o"ro,allow_other"`。

### 步骤6：卸载存储桶

卸载存储桶示例：
```shell
$./bin/goosefs-lite umount /mnt/goosefs-lite-mnt
Unmount fuse at /mnt/goosefs-lite-mnt/ (PID: 17206).
```

### 步骤7：参数调优

GooseFS-Lite 包含两个配置文件，分别为 conf/core-site.xml 及 conf/goosefs-lite.properties。
您可以通过修改 conf/core-site.xml 调优上传下载带宽。常用参数如下，更多参数可参见 [Hadoop-COS](https://cloud.tencent.com/document/product/436/6884) 文档。

| 属性键           | 说明                                           | 默认值 | 必填项 |
| ---------------- | ---------------------------------------------- | ------ | ------ |
| fs.cosn.useHttps | 配置是否使用 HTTPS 作为与 COS 后端的传输协议。 | true | 否     |
| fs.cosn.upload. part.size | 分块上传的每个 part size 的大小。由于 COS 的分块上传最多只能支持10000块，因此需要预估最大可能使用到的单文件大小。 例如，part size 为8MB时，最大能够支持78GB的单文件上传。 part size 最大可以支持到2GB，即单文件最大可支持19TB。 | 8388608（8MB） | 否   |
| fs.cosn. upload_thread_pool | 文件流式上传到 COS 时，并发上传的线程数目。 | 10   | 否   |
| fs.cosn. read.ahead.block.size | 预读块的大小。   | 1048576（1MB） | 否   |
| fs.cosn. read.ahead.queue.size | 预读队列的长度。 | 8              | 否   |
| fs.cosn.trsf.fs.ofs.tmp.cache.dir   | 元数据加速存储桶的临时文件目录。 |无 | 是   |
| fs.cosn.trsf.fs.ofs.user.appid  | 元数据加速存储桶的 Appid。 | 无              | 是 |
| fs.cosn.trsf.fs.ofs.bucket.region | 元数据加速存储桶所在的地域，如 ap-shanghai，ap-beijing。 |无     | 是   |


您可以通过修改 conf/goosefs-lite.properties 对 GooseFS-Lite 的行为进行调整。常用参数如下：

| 属性           | 说明                                           | 默认值 | 必填项 |
| ---------------- | ---------------------------------------------- | ------ | ------ |
| goosefs.fuse.list.entries.cache.enabled | 是否开启客户端 List 缓存 | true | 否     |
| goosefs.fuse.list.entries.cache.max.size            | 客户端 List 最大缓存的条目数，单位：条 | 100000 | 否   |
| goosefs.fuse.list.entries.cache.max.expiration.time | 客户端 List 缓存的有效时间，单位：ms | 15000 | 否   |
| goosefs.fuse.async.release.wait_time.max.ms         | open 和 rename 操作的文件正在被写入时，等待写入操作完成的时间，单位：ms | 5000 | 否   |
| goosefs.fuse.umount.timeout                         | 卸载文件系统时，等待未完成操作的时间，单位：ms | 120000        | 否   |

当您的读取和写入并发度较大，您可以通过如下方式，调整 GooseFS-Lite 最大 JVM 运行内存，避免 FullGC 和 OutOfMemoryError。JVM 默认值为 `-Xms2G -Xmx2G -XX:MaxDirectMemorySize=4G -XX:+UseG1GC`，调整方式如下：
```
export JAVA_OPTS=" -Xms16G -Xmx16G  -XX:MaxDirectMemorySize=16G -XX:+UseG1GC"
./bin/goosefs-lite mount /mnt/goosefs-lite-mnt/ cosn://examplebucket-1250000000/
ps -ef|grep goosefs-lite|grep -v grep
```



### 常见问题

#### 1. 缺少 libfuse 库文件，该如何处理？

需要安装 libfuse:
![img](https://qcloudimg.tencent-cloud.cn/raw/7a535eed0fac0da06f530fb04ca9702b.png)
- 方式一
执行如下命令，安装 fuse-devel。
```
yum install fuse-devel
```
执行如下命令，查看安装是否成功。
```
find / -name libfuse.so*
```
- 方式二
更新旧版本 libfuse.so.2.9.2，安装步骤如下：
>? CentOS 7默认安装的是 libfuse.so.2.9.2。
>
 1. 下载 [libfuse 源码](https://github.com/libfuse/libfuse/releases/tag/fuse-2.9.7)，并编译生成 libfuse.so.2.9.7。
```
tar -zxvf fuse-2.9.7.tar.gz
cd fuse-2.9.7/ && ./configure && make && make install
echo -e '\n/usr/local/lib' >> /etc/ld.so.conf
ldconfig
```
 2. 编译及生成 libfuse.so.2.9.7 后，可按照以下步骤进行替换：
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

#### 2. 如何配置开机挂载？
步骤一:
编辑文件 /usr/lib/systemd/system/goosefs-lite.service，追加如下内容，您可以将 examplebucket-1250000000 换为您的存储桶：
```
[Unit]
Description=The Tencent Cloud GooseFS Lite for COS
Requires=network-online.target
After=network-online.target

[Service]
Type=forking
User=root
Environment="JAVA_OPTS=-Xms16G -Xmx16G -XX:MaxDirectMemorySize=16G -XX:+UseG1GC"
ExecStart=/usr/local/goosefs-lite-1.0.0/bin/goosefs-lite mount /mnt/goosefs-mnt cosn://examplebucket-1250000000/
ExecStop=/usr/local/goosefs-lite-1.0.0/bin/goosefs-lite umount /mnt/goosfs-mnt

[Install]
WantedBy=multi-user.target
```
步骤二：
执行如下命令，执行挂载命令和查看后台 Daemon 进程状态：
```
# 让 goosefs-lite 的 systemd 配置生效
systemctl daemon-reload
# 启动后台 Fuse 进程
systemctl start goosefs-lite
# 查看后台 Daemon 进程状态
systemctl status goosefs-lite
# 查看挂载点列表
/usr/local/goosefs-lite-1.0.0/bin/goosefs-lite stat

```
设置为开机启动时尝试挂载：
```
systemctl enable goosefs-lite
```

步骤三：
卸载挂载点，重启机器，并查看 Fuse 进程状态：
```
# 执行卸载，注意：请勿在数据写入的时卸载，否则会导致数据不完整
systemctl stop goosefs-lite
# 重启操作系统，请谨慎操作，不要影响业务
reboot -h now
# 查看后台 Daemon 进程状态
systemctl status goosefs-lite
# 查看挂载点列表
/usr/local/goosefs-lite-1.0.0/bin/goosefs-lite stat
```

#### 3. GooseFS-Lite 每天在某个时间段里 CPU 使用率较高，且向 COS 发出大量 Head、List 请求，产生大量请求次数费用，该怎么处理？

这通常是由于您机器上存在定时扫盘任务导致的，Linux 系统上常见的扫盘程序是 updatedb，您可以将 GooseFS-Lite 挂载点目录，添加到 updatedb 的配置文件 /etc/updatedb.conf 文件的 PRUNEPATHS 配置项中，避免该程序的扫盘行为。此外，您可以使用 Linux 工具 auditd，查找访问 GooseFS-Lite 挂载点的程序：

操作步骤如下：

步骤一：安装 auditd

Ubuntu:

```
ap-get install auditd -y
```

CentOS：

```
yum install audit audit-libs
```

步骤二：启动 auditd 服务

```
systemctl start auditd
systemctl enable auditd
```

步骤三：监控挂载目录
>?`-w` 指定 GooseFS-Lite 挂载目录，`-k` 为输出在 audit 日志中的 key。

```
auditctl -w /usr/local/service/mnt/ -k goosefs_lite_mnt
```

步骤四：根据日志确定访问程序

audit 的日志目录： /var/log/audit，查询命令如下：

```
ausearch -i|grep 'goosefs_lite_mnt'
```

步骤五：停止 auditd 服务
如果您需要停止 auditd 服务，可以使用如下命令：

```
/sbin/service auditd stop
```

>!如果访问挂载点的程序一直在运行，新启动的 auditd，并不会监控到该程序的访问行为；程序中关于挂载目录的多次调用，只会记录第一次。
