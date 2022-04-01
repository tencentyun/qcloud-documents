## 简介

对象存储（Cloud Object Storage，COS）可以通过开启元数据加速能力，拥有 HDFS 协议访问的能力。开启元数据加速能力后，COS 会为存储桶生成一个挂载点，您可以通过下载 [HDFS 客户端](https://github.com/tencentyun/chdfs-hadoop-plugin/tree/master/jar)，在客户端中输入该挂载点挂载 COS。本文将详细介绍如何在计算集群中挂载开启元数据加速的存储桶。

## 前提条件

- 确保计算集群中需要挂载的机器或者容器内已安装 [Java 1.8](https://www.oracle.com/java/technologies/downloads/)。
- 确保计算集群中需要挂载的机器或者容器已授权访问，您需要在 HDFS 权限配置里指定可访问的 VPC 网络和 IP 地址。

## 操作步骤

1. 下载 [Hadoop 客户端工具安装包](https://github.com/tencentyun/chdfs-hadoop-plugin/tree/master/jar) 。
2. 将安装包放置到计算作业对应的目录下。对于 EMR 集群，可同步到所有节点的`/usr/local/service/hadoop/share/hadoop/common/lib/`目录下。
3. 编辑 `core-site.xml`文件，新增以下基本配置：
```
<!--chdfs 的实现类-->
<property>
		 <name>fs.AbstractFileSystem.ofs.impl</name>
		 <value>com.qcloud.chdfs.fs.CHDFSDelegateFSAdapter</value>
</property>

<!--chdfs 的实现类-->
<property>
		 <name>fs.ofs.impl</name>
		 <value>com.qcloud.chdfs.fs.CHDFSHadoopFileSystemAdapter</value>
</property>

<!--本地 cache 的临时目录, 对于读写数据, 当内存 cache 不足时会写入本地硬盘, 这个路径若不存在会自动创建-->
<property>
		 <name>fs.ofs.tmp.cache.dir</name>
		 <value>/data/chdfs_tmp_cache</value>
</property>

<!--用户的appId, 可登录腾讯云控制台(https://console.cloud.tencent.com/developer)查看-->      
<property>
		 <name>fs.ofs.user.appid</name>
		 <value>1250000000</value>
</property>

<!--flush语义, 默认false(异步刷盘), 请参考下图数据可见性与持久化详细说明 -->      
<property>
		 <name>fs.ofs.upload.flush.flag</name>
		 <value>false</value>
</property>

```
4. 将 `core-site.xml`同步到所有`hadoop`节点上。
>?对于 EMR 集群，以上步骤3、4可在 EMR 控制台的组件管理中，修改 HDFS 配置即可。
>
5. 使用 `hadoop fs` 命令行工具，运行`hadoop fs -ls ofs://${bucketname-appid}/`命令，这里 `bucketname-appid` 为挂载地址，即存储桶名称。如果正常列出文件列表，则说明已经成功挂载 COS 存储桶。
6. 用户也可使用 `hadoop` 其他配置项，或者 `mr` 任务在开启了元数据加速能力的 COS 存储桶上运行数据任务。对于 `mr` 任务，可以通过`-Dfs.defaultFS=ofs://${bucketname-appid}/`将本次任务的默认输入输出 `FS` 改为对应的存储桶。

## 场景说明

### 数据可见性与持久化

开启元数据加速能力后，可以将 `COS` 作为一个云端分布式文件系统使用。通过 `Hadoop` 客户端工具打开一个文件，客户端会在满足一定大小时（通常为 4MB）异步刷盘，将数据写入到公有云`COS`存储桶中。如果上层计算业务主动调用数据输出流的 `Flush` 接口，**默认的行为是忽略（和通常的 flush 同步刷盘语义不同）**，客户端会等待后续满足写入量达到一定大小后才异步 `flush`，最后调用 `Close` 时才会强制同步刷盘，`Close` 成功的数据表示已经持久化成功，可保证后续可正常读取到。

`Hadoop` 客户端工具默认选择异步 `Flush`的原因是相比于本地磁盘，云端访问延迟较大，异步 `Flush` 可以减少与云端的交互，避免  `Flush` 的操作卡主用户写入操作，可以显著提升写入性能，减少作业时间。风险点是如果最终没有主动调用`Close`接口，未刷盘的数据会存在丢失风险。

因此，**对于需要实时写入数据，保证数据立即可见和持久化到云端的场景，例如存储 `Hbase Wal Log`，`Journal`日志等，请参考配置项`fs.ofs.upload.flush.flag`说明，开启同步`Flush`的选项。**

## 配置项说明

|        配置项      |                             说明                             |  默认值   | 是否必填 |
| :------------------------------| :----------------------------------------------------| :-------| :------ |
|       fs.ofs.tmp.cache.dir        |   存放临时数据    |    无     |    是    |
|       fs.ofs.map.block.size       | 客户端会将数据分成多个 `Block`写入，该参数用于控制数据的 block 大小，单位为字节。默认为128MB（只对 map 切分有影响，和 CHDFS 底层存储切块大小无关） | 134217728 |    否    |
| fs.ofs.data.transfer.thread.count |               客户端传输数据时的并行线程数                |    32     |    否    |
| fs.ofs.block.max.memory.cache.mb  | 客户端插件使用的内存 `Buffer` 的大小，单位为 MB。（对读写都有加速作用） |    16     |    否    |
|  fs.ofs.block.max.file.cache.mb   |  CHDFS 插件使用的磁盘 `Buffer` 的大小，单位为 MB。（对写入有加速作用）  |    256    |    否    |
|   fs.ofs.prev.read.block.count    | 读取时，预读的数据 `Block` 数量（大小一般为4MB），对于随机读场景，请适当减少这数值；对于顺序读场景，可适当增大该值以及内存 buffer 大小|     4     |    否    |
|  fs.ofs.prev.read.block.release.enable| 是否释放已经读取的上一块 `Block` 的 Buffer，对于顺序读，建议打开。对于随机读，如果反复读取某部分数据较频繁，建议关闭。可选值为 `true（打开）`、`false（关闭）` | `true` | 否 |
|      fs.ofs.plugin.info.log       |          是否打印客户端的调试日志，日志以 info 级别打印。可选值为 true（打开）、false（关闭） |   false   |    否    |
|      fs.ofs.upload.flush.flag     | 写数据，调用输出流 `Flush` 接口时，是否同步刷数据，默认为异步输数据（`false`）。如需同步刷盘, 请设置为 `true` | false | 否 |

