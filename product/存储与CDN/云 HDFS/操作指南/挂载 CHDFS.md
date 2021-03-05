
创建 CHDFS 及挂载点后，可以通过挂载点挂载 CHDFS，本文为您详细介绍如何挂载 CHDFS。

## 前提条件
- 确保挂载的机器或者容器内安装了 Java 1.8。
- 确保挂载的机器或者容器其 VPC ，与挂载点指定 VPC 相同。
- 确保挂载的机器或者容器其 VPC IP，与挂载点指定权限组中有一条权限规则授权地址匹配。

## 操作步骤
1.  下载 [CHDFS-Hadoop](https://github.com/tencentyun/chdfs-hadoop-plugin) JAR 包。
2.	将 JAR 包放置对应的目录下，对于 EMR 集群，可同步到所有节点的`/usr/local/service/hadoop/share/hadoop/common/lib/`目录下。
3.	编辑 core-site.xml 文件，新增以下基本配置：
```
<!--chdfs 的实现类-->
<property>
		 <name>fs.AbstractFileSystem.ofs.impl</name>
		 <value>com.qcloud.chdfs.fs.CHDFSDelegateFSAdapter</value>
</property>
<property>
		 <name>fs.ofs.impl</name>
		 <value>com.qcloud.chdfs.fs.CHDFSHadoopFileSystemAdapter</value>
</property>
<!--本地 cache 的临时目录, 对于读写数据, 当内存 cache 不足时会写入本地硬盘, 这个路径若不存在会自动创建-->
<property>
		 <name>fs.ofs.tmp.cache.dir</name>
		 <value>/data/chdfs_tmp_cache</value>
</property>
<!--appId-->      
<property>
		 <name>fs.ofs.user.appid</name>
		 <value>1250000000</value>
</property>
```
4.	将 core-site.xml 同步到所有 hadoop 节点上。
>?对于 EMR 集群，以上步骤3、4可在 EMR 控制台的组件管理中，修改 HDFS 配置即可。
5.	使用 hadoop fs 命令行工具，运行`hadoop fs –ls ofs://${mountpoint}/`命令，这里 mountpoint 为挂载地址。如果正常列出文件列表，则说明已经成功挂载 CHDFS。
6.	用户也可使用 hadoop 其他配置项，或者 mr 任务在 CHDFS 上运行数据任务。对于 mr 任务，可以通过`-Dfs.defaultFS=ofs://${mountpoint}/`将本次任务的默认输入输出 FS 改为 CHDFS。

## 其他配置项

|        配置项      |                             说明                             |  默认值   | 是否必填 |
| :------------------------------| :----------------------------------------------------| :-------| :------ |
|       fs.ofs.tmp.cache.dir        |   存放临时数据    |    无     |    是    |
|       fs.ofs.map.block.size       | chdfs 文件系统的 block 大小，单位为字节。默认为128MB（只对 map 切分有影响，和 chdfs 底层存储切块大小无关） | 134217728 |    否    |
| fs.ofs.data.transfer.thread.count |               chdfs 传输数据时的并行线程数                |    32     |    否    | 
| fs.ofs.block.max.memory.cache.mb  | chdfs 插件使用的内存 buffer 的大小，单位为 MB。(对读写都有加速作用) |    16     |    否    |
|  fs.ofs.block.max.file.cache.mb   |  chdfs 插件使用的磁盘 buffer 的大小，单位为 MB。（对写有加速作用）  |    256    |    否    |
|   fs.ofs.prev.read.block.count    | 读取时，预读的 chdfs block 数量（chdfs 的底层 block 大小一般为4MB）|     4     |    否    |
|      fs.ofs.plugin.info.log       |          是否打印插件的调试日志，日志以 info 级别打印。可选值为 true、false |   false   |    否    |

